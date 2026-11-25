---
title: "The Checklist I'd Been Following for Ten Years"
url: "https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/"
author: "Scriptease"
created: "2026-08-30"
published: "2026-08-31T08:43:05+02:00"
description: "A stranger's blog post gave a name to something I'd been doing for ten years without noticing. An hour later I was checking my own work against his ten rules."
tags: ["ai", "agent", "commandline", "automation", "skills", "saga"]
---

# The Checklist I'd Been Following for Ten Years

_The [AXI saga](https://scriptease.dev/sagas/#axi): 1. The Checklist I'd Been Following · [2. AXI All the Things](https://scriptease.dev/posts/2026-09-26-axi-all-the-things/) · [3. Not My First Rodeo](https://scriptease.dev/posts/2026-10-07-not-my-first-rodeo/) · [4. Back in AXIon](https://scriptease.dev/posts/2026-10-09-back-in-axion/) · [5. Anticipation](https://scriptease.dev/posts/2026-10-09-anticipation/) · [6. Making Our App Leak Its Secrets](https://scriptease.dev/posts/2026-10-18-making-our-app-leak-its-secrets/)_

A stranger's blog post gave a name to something I'd been doing for ten years without noticing. An hour later I was checking my own work against his ten rules.

## The question I stopped asking

At work, when I finish a piece of code, I send it off to be judged. A colleague reads it, and so does a machine: somewhere in a server room a computer rebuilds the whole product and runs a few thousand checks. Twenty minutes, if nothing is queued ahead of me. A no means I just broke something.

When I built with AI, I'd let it send the code off and judge the verdict automatically — but it had to relearn how to do that every time, and wade through heaps of data to figure out what was running and when it was done. All while a meter was running.

An absurdly expensive way to learn one bit of information. So I rationed the question. For anything big I'd still ask — but for a one-line fix, the kind where the answer is almost certainly yes, I'd let it go and find out whenever I next happened to look. Sometimes that was the following morning.

## The important part was the name

Then a video pointed me at a benchmark by Kun Chen, an engineer who'd left big tech to build his own AI setup. He'd pitted the fashionable ways of wiring an AI up to its tools against one plain typed command designed, deliberately, for a machine to use. Not more powerful. Just curated. It won on every measure: right more often, faster, a third of the cost.

His diagnosis is what stuck. Software for humans got decades of design attention; nobody ships a phone with a three-hundred-page manual any more, they ship a home screen. Tools built for AI are still mostly the manual — everything in one undifferentiated pile, good luck.

So he wrote down ten rules for tools whose reader is software, and gave them a name: AXI. That's the part that turned out to matter. Not the benchmark. Not his tools. The name.

## Ten years of Automator automation

I read the ten rules and kept nodding. It wasn't *what a good idea*. It was *that's what my scripts already do*.

Show the answer, not a preamble. Three or four columns, not thirty. Cut long output, but say how much you cut and how to get the rest. Never ask a question mid-run — there's nobody at the keyboard to answer it. I hadn't reasoned my way to any of that; it's just what survives when the thing calling your script is a machine that pays by the word.

Then I followed the thread back further than I expected.

Long before any of this, macOS shipped a program called Automator: a way to build a little double-clickable app that does one chore. I made a pile of them. One I still use — drag a box around anything on screen and read the text inside it, from [an earlier post here](https://scriptease.dev/posts/2026-07-29-three-different-ocrs/). The rest were work plumbing: visualize where a running server is spending its time, look inside it while it's running and more.

Each one hiding the details of how to make something work, and making it easy to repeat.

When AI assistants arrived, I ported them into what are now called skills — recipes for AIs.

## If it's scripted, it's free

So that night I looked at one of the recipes and thought: this is the one to make AI-friendly. I already had it — ask our build system whether anything's wrong — but it went the long way round, hand-typed commands and then everything they returned, all of it, every time.

The obvious fix would be to have my AI ask the build server to find my job. But there are hundreds of jobs, and it'd have to check which one runs for which project — exactly the kind of thing I don't want it to do on a meter.

The trick is to ask the reviewer, not the builder. Code at work waits in a review system called Gerrit, and when the machines finish they always stamp their verdict on the change itself: plus one if it's happy, minus one if it isn't. Every project, same stamp, no job names required.

So the command reads which change I just sent off — the repository already knows — and then it waits. That's it. No thinking, no reading, no meter. Waiting is free when nobody is watching.

It says in one line if it passed or failed. I pointed it at a build that had failed earlier that day: it turned 7,830 lines of log into four — the failing step, and nothing else.

And I can just type "Submit and tell me when it's green" again.

## If the answer is nothing, say so

The eighth of the ten rules says finding nothing is still a result: print *0 results*, never just stop.

My scripts broke it. They printed nothing, and my recipe even documented the silence. I knew what the emptiness meant — an AI can only guess, retry, or go exploring, all costlier than a simple *0 servers matched*.

I also updated the recipes to state what the AI should expect now.

## A name alone opens all the doors

It didn't change anything I couldn't have changed myself. The list isn't new or fundamental — it's a checklist I'd already been following in parts, and now apply to every new recipe.

What I got was the word. AXI: agent experience interface. *Agent* is what the industry calls an AI that goes off and does a job for you rather than just answering you. *Experience* is lifted from user experience. *Interface* is the surface where the two meet. Design for a user made of software.

The name is something simple you add: `-axi` at the end, and it means AI-friendly and follows the checklist.

## Steal this

The whole list, in my words — the original with the benchmark is in [Kun Chen's write-up](https://kunchenguid.medium.com/i-benchmarked-github-cli-vs-mcp-vs-tool-search-vs-code-mode-turns-out-the-best-solution-is-none-93528d5039e4).

1. **Say it in fewer words.** Write the column names once at the top instead of repeating a label on every row.
2. **Show three or four things, not thirty.** Default to what anyone would want; put the rest behind a flag.
3. **Cut long output, and say what you cut.** "Showing the last 80 of 7,830 lines" — plus how to ask for the rest.
4. **Lead with the answer.** Not a banner, not a wall of help text. The thing that was asked for.
5. **Suggest the next move at the end.** After the answer, where it's useful, not in a manual nobody read first.
6. **One predictable way to ask what it does.** Same shape for every command.
7. **Do the arithmetic yourself.** If the caller will obviously need the count, the age, or the step that broke, work it out and hand it over.
8. **Say "none".** Zero results is an answer. Print it.
9. **Fail in a sentence, never in a question.** There's nobody at the keyboard to answer it.
10. **Keep the channels clean.** Answer on one, chatter on the other, and an exit code that tells the truth about which one happened.
