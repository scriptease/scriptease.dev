# Blog material — Firehose debugging (the method)

**Title:** *Standing in the Firehose* — draft stub at `Blog/drafts/2026-07-23-standing-in-the-firehose.md`

**Angle chosen:** the *method*, tool-agnostic. Arthas is the tool that happens to satisfy it, but the story is about *why every debugger you already own fails on hot paths, and what to do instead*.

**Source sessions (claude-mem):**
- Yesterday/this-morning thread (the *why/method* session): #S5410–S5419; key obs #32904, #32903, #32900, #32892, #32885, #32886, #33023
- Today evening thread (*live use*, war story): #S5437–S5443; key obs #33069, #33076, #33093, #33099, #33103
- Research note in vault: `Research/2026-07/2026-07-23-speed-up-remote-java-debugging-in-eclipse-vs-intellij/` (Background.md, Findings.md, Sources.md, Implementation.md, 📌 Overview.md)

---

## The narrative arc (as it actually happened)

1. **Debugging just wasn't working.** Remote Java debugging into a Kubernetes test pod (MieleServer, Miele order history) was painful. M5 Mac felt slower than the old M1. Attach took ~21s even with breakpoints disabled.
2. **Queued research** on "why Eclipse remote debug takes 60+s vs near-instant IntelliJ."
3. **Research came back with a ranked fix list** (see Findings). Discussed it.
4. **The research result didn't actually solve the real problem.** It explained the *connect-speed* gap (real, structural, Eclipse-side) — but that was the surface. The actual pain was something the fix list couldn't touch.
5. **Reframed to the real question — the firehose problem.** The bug lived on a code path that fires hundreds–thousands of times per interaction. And here's the kicker realization:
6. **Eclipse, IntelliJ, *and* an MCP-based JDWP server would ALL hit the same wall.** They all work by adding a breakpoint/predicate that requires round-tripping out of the JVM and blocking. That back-and-forth is fatal at firehose rate — regardless of IDE brand or how "agentic" the wrapper is.
7. **Named the governing law**, picked Arthas as the one tool that satisfies it, designed the integration, built it into the `caperwhite-tool-launcher` skill, then used it live on the real pod.

> The twist worth keeping: the *research answer was correct and still didn't help.* Speed was never the disease; it was a symptom that sent us looking in the right place.

---

## The core insight (the one-liner)

> **Push the predicate into the VM. Never pull events out to decide.**

Every JDWP-based debugger *pulls*: on every hit of the instrumented location, it suspends and ships an event out to an external process to evaluate your condition. That's fine at human frequency. On a path that fires thousands of times a second it's a self-inflicted DoS.

- **SUSPEND_ALL** → freezes the entire shared JVM (everyone on the test pod is now stuck).
- **SUSPEND_THREAD** → suspended threads pile up; steals view focus.
- **Conditional breakpoint** → the condition is evaluated *per hit, over the wire*. Real case: a session went **3 min → 30 min and never even hit** the breakpoint.

The brand of IDE is irrelevant. Eclipse, IntelliJ, and `FgForrest/mcp-jdwp-java` (a 47-tool MCP server — breakpoints, logpoints, eval, mutation) are all JDWP underneath. **The MCP server is *not* an escape hatch — it inherits the exact same suspend-and-pull limitation.** Wrapping a broken mechanism in an agent-friendly API doesn't fix the mechanism.

---

## The four requirements for binary-search debugging

You localize a bug by bisecting the call path — "clean in / dirty out" — even when you don't know where the defect is (you *do* know the architecture). To do that on a live, hot, shared JVM you need a tool that is all four at once:

| # | Requirement | IDE debugger | Static log lines | Arthas |
|---|-------------|:---:|:---:|:---:|
| 1 | **Interactive** (probe, look, move the probe) | ✅ | ❌ | ✅ |
| 2 | **No redeploy** (don't rebuild to add a probe) | ✅ | ❌ | ✅ |
| 3 | **No suspend** (firehose-safe) | ❌ | ✅ | ✅ |
| 4 | **In/out at a point** (see args + return at one spot) | ✅ | partial | ✅ |

- IDE debuggers fail #3.
- Log lines fail #1 and #2.
- **Arthas is the only one that hits all four** — because it instruments bytecode via the JVM attach API and evaluates the predicate *in-process*, so a non-matching hit costs ~nothing. Nothing crosses the wire until *you* pull a bounded result.

---

## Why "if I knew where to put the probe, I'd already know where the bug is"

This is the honest objection to "just add a logpoint." The answer is the **localization method**:

1. Probe the *known symptom* (Arthas `stack` on the method you can see misbehaving).
2. **Bisect the known architectural seams** — controller → service → store → merge — looking for the flip-point where data goes from clean-in to dirty-out.
3. You don't need to know where the bug is. You know the *structure*. The structure is the search tree.

Retroactively validated: the earlier **MIE-2738 order-leak** was solved by hand with exactly this bisection-at-seams approach (culprit was `mergeOrders`/interleave). Arthas just makes that same method possible *live, without redeploys*.

---

## Tiered calibration (when do debuggers actually work?)

Not every path is a firehose. Be honest about the tier:

- **Moderate (~1/sec)** — e.g. order/select interleave. Logpoints and conditional breakpoints are *fine* here. Don't reach for heavy machinery.
- **Extreme (millions of variant hits)** — e.g. a publication path. *No* debugger survives. JDWP per-hit evaluation overhead guarantees it. This is Arthas-or-nothing territory.

The MCP-server temptation lives right at this boundary: it's genuinely useful in the moderate tier, and genuinely useless (same as the IDEs) in the extreme tier. Naming the tier tells you which tool is a mistake.

---

## What Arthas is (the tool, briefly)

- `alibaba/arthas`, Apache 2.0. Attaches to a running JVM by PID via the **attach API — never suspends threads**.
- Commands: `watch` (params/return/exceptions), `trace` (slow sub-calls), `stack` (call stacks), `tt` (time-travel replay), `monitor` (QPS/latency/success-rate), `jad`, `sc`, `thread`, `profiler`.
- **HTTP API** at `POST :8563/api`: `init_session → async_exec → pull_results → interrupt_job`. Every probe is a **bounded window**, not a persistent watch — which is exactly what makes it agent-drivable (Claude can open a probe window, pull, and close it).
- **Hard requirement: JDK, not JRE.** A slim JRE pod image can't attach. Verify first.
- Integrated into `caperwhite-tool-launcher` as a two-phase op (attach via `kubectl cp` + `arthas-boot.jar`; drive via the existing `tunnel-run.sh` port-forward).

---

## The live war story (evening session) — great for a concrete ending

Using the freshly-built tool on the real problem produced a very human sequence of "the tool works, reality is annoying" moments — good material for showing the method is not magic:

1. **Watch on `interleave…ForBranchAndDates` → 45s, zero hits.** Negative finding: slow path doesn't go through here (or no traffic). This is the method *working* — a clean seam ruled out.
2. **Suspicion: is it the tool or the pod?** Dropped to the raw HTTP API to bypass our own `probe.sh` wrapper. Confirmed the watch attached perfectly (`TraceFilter#doFilterInternally`, classCount 1/methodCount 1) but **all 5 polls returned empty — the dev pod was receiving zero HTTP traffic.** The pod was simply idle. (Bonus discovery: JVM main class is `com.caperwhite.tomcat.StandaloneServer`, a custom standalone Tomcat, not Spring Boot.)
3. **Retargeted to the pod actually serving the iPad** (`miele-au-test`), method `MieleNext4CombinedQueryOrderApi.filterOrdersByBranchIfNeeded`. **Watch fired** — proved the iPad was hitting test correctly.
4. **OGNL gotcha:** `returnObj.{branchKey}` blew up with `NoSuchPropertyException` on a `…$$Lambda$3562`. Architectural finding: the Next4 query API returns a **lazy Lambda/streaming iterable, not a materialized `List<Order>`** — you have to force materialization before you can project a field.
5. **Tooling papercut fixed:** our output was truncating the watch payload at 1500 chars, burying the sizes we needed → raised to 9000 and extracted the inner `value` field directly. (Also fed back into a `probe.sh` fix so future diagnostic output isn't silently swallowed.)

**Ending beat:** the method didn't hand us the bug on a plate — but every step was a *clean, cheap, live* elimination on a shared pod that no breakpoint could have touched. That's the whole point.

---

## The payoff (the emotional close)

The frustration was never *not knowing what I wanted*. I knew *exactly* what I wanted — put me at this point, on the live path, and let me see the values going in and coming out. That's a completely reasonable thing to want. The tools just couldn't give it to me. Eclipse, IntelliJ, a breakpoint, a conditional — every one of them said "sure" and then either froze the world or spun for 30 minutes and never fired. That's the specific flavor of hair-tearing: not being lost, but being *right* and stonewalled by your own instruments.

The close is that **it all worked, and it's now permanent.** This isn't a one-off heroic debug session I'll have to reconstruct from memory next time. It's a **verified skill** — built, tested end-to-end (all attach/probe/detach steps passing), and reusable. The next time a hot path misbehaves, I don't re-derive any of this. I attach, I bisect the seams, I watch a bounded window. The thing that almost broke me is now a repeatable, on-demand procedure.

> The win isn't "I found the bug." The win is "I can now reproduce the *conditions* that made the bug impossible to find — on demand — and they no longer stop me."

## Pull-quotes / candidate hooks

- "The research answered my question and didn't solve my problem."
- "Push the predicate into the VM; never pull events out to decide."
- "Switching IDEs was never going to help — Eclipse, IntelliJ, and the shiny MCP debugger are the same machine wearing three coats."
- "If I knew where to put the probe, I'd already know where the bug is." — and the answer: you don't bisect the bug, you bisect the architecture.
- "A conditional breakpoint that goes from 3 minutes to 30 and never fires isn't slow. It's the wrong tool."
- "The problem was never that I didn't know what I wanted. It's that nothing could give it to me."
- "It's not a war story I have to remember. It's a skill I can run again."

## Writing-voice reminders (from vault memory)
Let the story do the talking; direct voice, no hyperbole; metaphor sparingly; ground in the real MieleServer/order-history story; AI-as-duet is fine but don't over-narrate the tooling. See `feedback_writing_voice` memory before final draft.
