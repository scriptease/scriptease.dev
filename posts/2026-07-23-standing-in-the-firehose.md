---
title: "Standing in the Firehose"
url: "https://scriptease.dev/posts/2026-07-23-standing-in-the-firehose/"
author: "Scriptease"
created: "2026-07-23"
published: "2026-07-23T19:56:16+02:00"
description: "The premise was easy. An API call was supposed to return orders for one branch — and it kept handing back orders it had no business showing. I had the code. The code looked fine."
tags: ["java", "debugging", "eclipse", "performance", "ai"]
---

# Standing in the Firehose

The premise was easy. An API call was supposed to return orders for one branch — and it kept handing back orders it had no business showing.

I had the code. I looked at the code. The code looked fine.

So I did what I would always do. Attach a debugger and find out what's happening. Get the data before the method call. Get the data after the method call. Compare them. Done. Do that a couple of times in different places in the code, and you find the bug.

But…

## The debugger kept freezing

The method I needed to watch runs on a hot path. Not once per click — constantly. Every order query on that pod goes through it.

So the breakpoint fired. And fired. And fired. Every hit suspends the thread and hands control to me, and I'm not fast enough to wave through thousands of hits looking for the one branch I care about. Worse: it's a shared test pod. Suspend it and I don't just freeze my own debugging, I freeze everyone else pointed at the same box.

So I let it sit. I queued up a research task so I wouldn't forget about it, and came back in the morning energized. Let's read the research. Let's do this.

## The research worked. It couldn't help.

The research was good. It came back with a list of actionable things. Connect through localhost instead of the hostname — I could skip that one. Clean up my breakpoints. Change the build mode. A handful of routine checks.

Over a minute down to thirty seconds. Great! Not great, let me explain.

Because the problem was never the speed. The problem is the firehose. Too many requests, too many things happening at once, a hot path that cannot be interrupted. No amount of tuning the connection touches that.

## Three solutions, all the same

I tested out a few ideas. One was an MCP server — if I could get Claude in the loop, maybe Claude could sit there and do the tedious part. Then I tried a different IDE, and it was faster, but it still had the same flaw. If the code that introspects works synchronously, it has to ask a question and wait for the answer before the program is allowed to move on. And you cannot put synchronous code inside a firehose.

So I asked the AI what my options were. I genuinely sat with it. And we landed on the obvious suggestion: add log statements.

But that's not my workflow. A log statement only helps if I already know where to put it — and if I know exactly where to put it, I already know where the problem is. At that point the log tells me nothing I didn't know.

Because debugging, for me, is a binary search. I'm not hunting the bug directly. I'm excluding the space around it. If the data is correct going into this method, I jump to the farthest method downstream and look again. If it's wrong there, the problem lives somewhere between the two. So I halve the gap. Then I halve it again. And again. Each step throws away half of what's left, until there's nowhere for the bug to hide.

A log statement breaks that. To move my probe I'd have to edit the code and redeploy. I'd be running the exact same search — just one slow compile-and-wait cycle at a time.

## Four out of four

Then the AI came back with a name: Arthas.

It ran down my four criteria — interactive, no redeploy, no suspending the world, and let me see the data going in and coming out at a single point — and Arthas hit all four.

Everything I tried was watching from the outside. Arthas does its watching from the inside — it evaluates the question right there in the running program and only hands me back the one answer I asked for. Nothing stops. Nothing waits. The firehose keeps running and I get my sample anyway.

I was intrigued.

I looked up the tool's GitHub page, and it even had flame graphs. I love flame graphs. They make it obvious where the load-bearing work happens — where the time actually goes, across the synchronous and the asynchronous paths. And I already had a skill that produces them.

So I pointed the AI at it. Here's my skill. Can you make it work? It read the skill and said the handyman work was already done — the building blocks were all there. Then it updated the research document with the plan, and flagged exactly one thing that could stop us: it needs a specific runtime.

I stopped it there. I had what I wanted for now — a feasible path, written down. I hadn't decided to walk it yet.

## Evening: let's make it happen

Later that evening, after the day's work was done, I decided. Let's make it happen.

I started a fresh session inside my skills project and handed it everything: here's the research, here's the handoff. First question first — is the one thing that could block us actually there? It probed, and came back: yes. We're clear.

So I let it work. And it did a lot. Then it stopped and asked the obvious question: do you want to test it, or commit it? Obviously!

We let it run. It attached, it ran through its steps, it reported success, and it tore itself back down. Done. Uneventful!

I watched the AI building it — creating each piece, downloading what it needed, slotting everything into its place.

The test was boring. It only showed the parts moving; you can only see it working when you take it for a test drive.

## Back in the firehose

So I went back to the original session. The one that had watched me fail. The session that held the frustration about it not working, the session that ran the research, the session that updated the research — the one that already knew everything there was to know about the problem I was actually trying to solve. The skills project knew how to build the tool. This session knew what I needed it for.

The real test did not go smoothly. It got hit with one blockage after another.

First, the script didn't behave. The events didn't trickle through. And every attempt was slow in its own right — attach, fire the watch, wait, read the results once the wait was over — call it forty seconds a round. Every round came back empty.

Also, I pointed it at the wrong machine — and it took way too long to figure that one out.

With that sorted, we were back to real testing. Except our own code fights back. Lazy loading, in-memory processing — all the things that make it fast, and all the things that make it hard to get a foot in the door. The value I wanted to look at wasn't a tidy list sitting there waiting; it was a lazy stream that hadn't even unpacked itself yet.

So we narrowed the scope. We didn't run the exact test I'd had in mind — we ran a smaller one. But I saw it. The method fired, and it captured real data. The AI came back celebrating:

> We got it. The method fired and captured real data. Look at those two branch-key values flowing through.

But even the AI wasn't satisfied yet. It had the input, but the answer itself was cut off — and it wasn't willing to call that done:

> Let me bump the truncation, make one small adjustment, and do one more run.

And it worked. I had a table in front of me: the data going in, and the data coming out.

## So what

Building the tool took less than fifteen minutes. The test run took half an hour — longer than it had taken me the day before to just fix the actual bug by hand.

It's a bad trade. I spent more time proving the tool than the bug had cost me.

But it was worth every minute. I came out of it understanding how my new process works — and so did the AI. It even suggested two changes to the script so the next AI has an easier time.

What matters is that I now have something I didn't have before: a tool where I can point it at the code, step into the firehose, and stand there while the traffic flows around me — watching the data stream through, one clean sample at a time, without stopping the world to do it.

I didn't have that yesterday. Today I do. And it isn't just a clever evening — it's codified as a skill, another addition to my Swiss army knife, ready for the next mission.
