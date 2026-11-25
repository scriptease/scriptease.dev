---
title: "AXI All the Things"
url: "https://scriptease.dev/posts/2026-09-26-axi-all-the-things/"
author: "Scriptease"
created: "2026-09-26"
published: "2026-09-26T12:53:42+02:00"
description: "I just got a notification on my phone: one of my testers' apps had crashed. It didn't say where."
tags: ["ai", "agent", "commandline", "skills", "automation", "saga"]
---

# AXI All the Things

_The [AXI saga](https://scriptease.dev/sagas/#axi): [1. The Checklist I'd Been Following](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/) · 2. AXI All the Things · [3. Not My First Rodeo](https://scriptease.dev/posts/2026-10-07-not-my-first-rodeo/) · [4. Back in AXIon](https://scriptease.dev/posts/2026-10-09-back-in-axion/) · [5. Anticipation](https://scriptease.dev/posts/2026-10-09-anticipation/) · [6. Making Our App Leak Its Secrets](https://scriptease.dev/posts/2026-10-18-making-our-app-leak-its-secrets/)_

I just got a notification on my phone: one of my testers' apps had crashed. It didn't say where.

## Why do I look for the crashes myself?

Before an iPad app ships, testers get it early through TestFlight, Apple's app for beta versions. When it crashes on them, I get a report. What reached me was a note about a crash, without the report.

The actual crash reports live somewhere else: Firebase Crashlytics, Google's black box recorder for apps. Every time an app dies, it writes down where, on which device, and in which version. So I went looking for this one. I couldn't find it.

Then I thought: why do I look for the crashes myself, if I can let AI do it for me?

## "Is there a CLI version of it?"

I asked my AI whether there was a way to read Firebase crash reports. There was: install a plug-in. MCP, the standard way to hook an AI up to a tool.

The catch is how plug-ins work. The AI reads the plug-in's whole menu at the start of every conversation, and thinking about crashes will always be in the back of its mind. I told it: I don't like the MCP server, because then I will always have it in my context. Is there a CLI version of it, a plain command instead?

No. Google's command-line tool can upload crash data, but not read it. For reading, the plug-in is the only way in.

So the AI suggested the obvious workaround: a small command that starts the plug-in, asks it, gets the answer and shuts it down again. The AI only knows about looking up crashes when needed.

## "Let's create a folder"

I dictate everything, and what I said came out as "let's create a folder". The AI asked whether I meant skill. I did. Skills are recipes for AIs, and I've been writing them for work for a while.

A month earlier I'd written [a post about AXI](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/): ten rules for commands whose reader is an AI instead of a person. Lead with the answer, keep it to a few columns, say "none" when there's nothing. That same night I'd put the ten rules into the recipe my AI uses to write new recipes.

While the AI was building, I sent one line after it: "Make sure we follow the axi markdown file." The new command came back named `crashlytics-axi`, with every AXI rule checked off in its summary.

My plan was to point it at the one app that started the quest as soon as it worked. I never had to. To test its own work, the AI needed a sample app, and for some reason it picked exactly the one I'd been looking for. Its summary ended with that app's crashes from the last three months.

But the workaround needs patience. Every command takes about fifteen seconds.

## "From when were they?"

Its summary listed three crashes. I recognised one: a crash I'd written a ticket for days earlier. The AI found the ticket, matched it to the crash in Firebase, and posted a comment. I asked it to add that the comment was made using a new skill.

The other two came without dates, so I had to ask. Both were from July. None of the three was the crash I was looking for.

That's rule seven: hand over the obvious next piece of information without being asked. The AI got back to work, and now the date comes with the first answer.

## "Already reserved"

One of the July crashes had no ticket, so I had it create one. The AI wrote down its best guess at the cause. It added that the code hadn't changed since, so the crash might still happen.

Minutes later I opened a second AI session and gave it the ticket to analyze.

It came back with: "The ticket's hypothesis is wrong." The crash was already fixed.

One AI wrote the ticket. Another AI closed it. I dictated "report it as already reserved", but meant resolved. Five minutes after it was created, the ticket was done.

Half an hour after my first question, the skill was up for review with my colleagues.

## "Call it standup"

The crash from that notification still wasn't there. So I wanted the checking to happen without me: the day it shows up, I want to know. My vault, the folder of notes, already runs a small job every morning. I asked for one more step at the end: look for new crash reports and ping me on Discord if there are any.

Across all our customers, test versions included, that's 57 apps in Firebase. At fifteen seconds of startup per command, a full round would take fourteen minutes.

The AI's first version worked around that by fiddling with the AXI tool we'd just built. It worked, but it could break any day. While it was still at it, I asked whether we shouldn't just add this to the command itself.

So the command got a new verb for exactly that. I dictated "call it um stand up", and it became `standup`, next to the old per-app command, still untouched. One go, all 57 apps, thirty seconds. The morning job keeps a list of the crashes it has seen and only tells me when a new one appears.

To test it, the AI made the job forget one crash it had already seen.

## "Just got the notification"

My phone buzzed. One new crash, the app, the version, two users. That one was a test.

I've never typed any of these commands or tools myself, and I never will. An AI wrote them, and an AI is the only one that runs them.

That's the idea behind AXI: code written by AI, for AI. No person reads its output. Its whole job is to have the next answer ready, so the AI can keep going instead of spending tokens to dig it up. When I had to ask for the dates, that wasn't a missing feature. It was the command failing at its only job. The checklist is in the recipe that writes the commands, so every new one comes out AXI.

## "I mentioned axi in my request"

To write this post, I had an AI read back the sessions where all of this was built. It reported I had never asked for AXI.

I had, and I had the receipt. "Make sure we follow the axi markdown file." It searched again and found the line I'd sent while the first AI was busy building. The tool that reads my sessions had skipped every message I'd typed while an AI was working: hundreds of them, across many sessions.

So the post about AXI turned into a side quest: fixing another tool written by AI, for AI, that had failed at its only job. It reads those messages now. It also got a new name: `load-session-axi`.

All three crashes the crash command found are fixed by now. The one I'm actually interested in hasn't arrived yet. Tomorrow, or on Monday, my phone will tell me.
