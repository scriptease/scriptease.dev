---
title: "Anticipation"
url: "https://scriptease.dev/posts/2026-10-09-anticipation/"
author: "Scriptease"
created: "2026-10-09"
published: "2026-10-09T22:17:56+02:00"
description: "Every command I write for my AI has one job before the real one: anticipate what the AI will do next, and tell it before it asks. The first colleague to try one got no head start at all. The command failed, the AI pondered, and then he pondered."
tags: ["ai", "agent", "commandline", "skills", "saga"]
---

# Anticipation

_The [AXI saga](https://scriptease.dev/sagas/#axi): [1. The Checklist I'd Been Following](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/) · [2. AXI All the Things](https://scriptease.dev/posts/2026-09-26-axi-all-the-things/) · [3. Not My First Rodeo](https://scriptease.dev/posts/2026-10-07-not-my-first-rodeo/) · [4. Back in AXIon](https://scriptease.dev/posts/2026-10-09-back-in-axion/) · 5. Anticipation · [6. Making Our App Leak Its Secrets](https://scriptease.dev/posts/2026-10-18-making-our-app-leak-its-secrets/)_

Every command I write for my AI has one job before the real one: anticipate what the AI will do next, and tell it before it asks. The first colleague to try one got no head start at all. The command failed, the AI pondered, and then he pondered.

## "can you find the comment"

I no longer open Jira, the to-do list our team shares, myself. When a colleague commented on one of my tickets, I asked my AI to find it.

"can you find the comment … had on one of my axi tickets"

The ticket was the web login [from the lunch break](https://scriptease.dev/posts/2026-10-06-built-over-his-lunch-break/): a command that opens Chrome, the web browser, goes to one of our apps that run in the browser and types the password straight from 1Password, the password manager, so the AI never sees it. Two colleagues had watched me use it the day before, for over an hour. Now one of them had finally tried it on his own Mac.

The AI found the comment. The login had worked, on a customer's test site in Mexico. The password never showed up as readable text, and two screenshots were attached.

His first try had failed. The 1Password tool on his Mac, the command's way into the password manager, wasn't connected to his account yet, a switch you flip once in the app's settings. The command hadn't said so.

A failed first try is exactly what an AXI, a command written for an AI reader, is [supposed to prevent](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/). Every answer carries what the AI will need next. Here the error carried nothing, and what reached me was: update your skill, the AI's written recipe for the tool.

## The documentation was not the problem

A skill comes with a setup guide, so my first move was the obvious one: "can we add that to the prerequiste sections"

"No change needed." The guide already said it, both points, added the day before his comment. He most likely never opened the file, the AI said. "The doc isn't the weak spot; the error message is." The obvious fix: when the 1Password tool fails, the command itself says what to do next. A course of action a stranger would confirm the next evening.

I agreed. Now it answers with the switch to flip and the file to read. Then the AI sent my colleague a thank-you and the link to the fix through my Slack command, the one that lets the AI write in Slack, our work chat.

The manual had been right for a day. Nobody reads the manual at the moment they need it. The error message, they read.

## "does the slack axi allow to add a :done?"

The next day my Slack command hit a roadblock of its own.

A fix had gone out for a customer, and the AI had posted the status beneath the original Slack message, in its chain of replies. Then I wanted the last touch: our done-mark on that original message, the word "done" inside a red rectangle, like a rubber stamp. Anyone scrolling past can see at a glance that this one is finished.

"does the slack axi allow to add a :done to the root message?"

It didn't. So I added what was missing, and asked Slack for the wrong permission along the way. Slack's permissions only ever grow, never shrink, so I threw the command's key away, its pass into Slack, and started with a fresh one. By the afternoon, the command could stamp.

The AXI had grown by one afternoon of being used.

## "I haven't watched it yet, but I will watch it now"

While we were writing this post, the AI asked me whether I had watched the talk it was about to quote: "Did you watch the Airbyte talk yourself, or only read the research note?" A YouTube video released two hours earlier, which I hadn't even seen.

"I haven't watched it yet, but I will watch it now"

My [YouTube watcher](https://scriptease.dev/posts/2026-10-04-on-the-shoulders-of-giants/), the tool that finds talks for my notes, had queued it that evening: eighteen minutes from the AI Engineer conference, by an engineer at Airbyte, a data company. "Designing CLIs for Agents, Not Humans": CLIs are the typed kind of tool, the kind every AXI is, and the agents are AIs using them on someone's behalf. Before I knew the talk existed, the research AI had been through the whole of it.

Its verdict: "High topical fit, low novelty."

The talk's rules for a command an AI will use: every command follows the same pattern, so the AI guesses right without reading the manual. Ship the recipe with the tool, or the AI doesn't know the tool exists. Never stop to ask a question, because "it can't sit there and wait for you to type a prompt into the CLI … they'll just kind of get stuck there." And one I hadn't heard put that way, about changing the tool's rules to match how the AI keeps trying to use it: "if you see agents making the same mistake over and over, calling the wrong command a bunch of times, consider making that your contract. Make it dead simple for agents to stumble across the right way to use things."

That was my colleague's first try, in one sentence. The research AI found one idea worth stealing: errors that say whether trying again would help.

Then I watched the talk myself, while writing this. Mostly the AXI ideas, and my own experience of writing skills that pre-empt the trouble before it happens. His point that the plug-in standard suits non-technical users better is fair. My one addition: the AI picks the right recipe reliably when its description says what it's *for*, not what it does. Every one of mine starts with "Use when the user asks…".

That's a cool thing about having a pipeline that constantly feeds you with information.

## Low novelty, high topical fit

Two months ago, [a stranger's blog post](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/) gave a name to something I had been doing for years. This week a stranger's talk gave it a verdict.

Low novelty. The best thing a checklist can be told.
