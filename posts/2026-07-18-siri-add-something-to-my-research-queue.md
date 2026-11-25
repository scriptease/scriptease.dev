---
title: "Siri, Add Something to My Research Queue"
url: "https://scriptease.dev/posts/2026-07-18-siri-add-something-to-my-research-queue/"
author: "Scriptease"
created: "2026-07-18"
published: "2026-07-18T23:07:48+02:00"
description: "The best ideas I have arrive when both my hands are on the handlebars, kilometres from a keyboard. For a while I could catch them. This week I taught the machine to actually do something with them."
tags: ["ai", "siri", "voice", "automation", "obsidian", "saga"]
---

# Siri, Add Something to My Research Queue

_The [Hands-Free saga](https://scriptease.dev/sagas/#hands-free): [1. The Ticket That Filed Itself](https://scriptease.dev/posts/2026-07-05-the-ticket-that-filed-itself/) · 2. Siri, Add Something to My Research Queue · [3. My Personal Hacker News](https://scriptease.dev/posts/2026-07-25-my-personal-hacker-news/) · [4. On the Shoulders of Giants](https://scriptease.dev/posts/2026-10-04-on-the-shoulders-of-giants/) · [5. Factory Reset](https://scriptease.dev/posts/2026-10-11-factory-reset/) · [6. Two Nos Make a Yes](https://scriptease.dev/posts/2026-10-18-two-nos-make-a-yes/) · [7. Reviewing the Reviewer](https://scriptease.dev/posts/2026-11-07-reviewing-the-reviewer/)_

The best ideas I have arrive when both my hands are on the handlebars, kilometres from a keyboard. For a while I could catch them. This week I taught the machine to actually do something with them.

## Hey Siri, add something

I ride a lot, and riding is where my head finally goes quiet enough to think. Which is the problem: the good thought shows up exactly when I can't write it down. Both hands are busy. Stopping to fish out my phone means the thought is already half gone by the time the screen wakes up.

I solved the catching part a while ago, and the fix was almost stupidly simple. I talk to Siri. "Hey Siri, add something to my Ideas list." I'd built a small habit around one quirk: if I try to dictate the whole idea in one breath — "add research whether jellyfish actually sleep to my ideas list" — Siri grabs the first few words, mangles the rest, and I get a note that says "add research whether." Useless. But if I say the vague version — "add *something* to my Ideas list" — Siri stops, and asks: "What's the something?" And *then* I get to talk. A whole sentence. Two, if I'm quick.

The ideas fill up, caught mid-ride, safe in a list.

## I'm hoarding ideas

A list like this isn't where ideas go to die. It's a staging area — the same reflex as waking with a thought and scribbling it on the pad by the bed. You're not solving anything at 3 a.m.; you're just making sure it's still there when you're properly awake.

My research queue is just another list — except this one gets processed. I drop a question in, and a background helper notices, goes off and researches the thing properly, reads a handful of real sources, writes up what it found with the links, and pings me on Discord when it's done. I'd been using it from my desk for weeks: type a question, get a cited write-up about ten minutes later. I could even talk to it in Discord, holding a push-to-talk button. Just not on a bike.

## The maestro kept dozing off

My maestro, the one that was supposed to lead the orchestra, kept nodding off. Its whole job was to notice a new question and kick off the work. It didn't.

One small job held the whole thing together: wake up and go. But sometimes it dropped a question. Sometimes it quietly lost work I'd already handed it. Sometimes it would only stir if I brought the app to the foreground, as if it were embarrassed to be caught working in the background. It was the specific kind of flaky that eats trust: once you've watched it miss twice, you start checking on it, and a system you have to babysit isn't saving you anything at all.

I didn't write the automation underneath — it's a free tool I lean on for exactly this kind of wiring. When I went digging, the tool's own author said it plainly: this particular corner, the tasks feature, was the least-tested part of the whole system.

So I rebuilt it myself — the noticing, and the not-losing-track — and left the tool doing only the thing it never fumbles: waking my code up on a timer, like an alarm clock. Same nudge as before, but now the careful part is mine. It doesn't drop things or need me watching over its shoulder. Now I could trust it with something as flighty as a thought I'd shouted on a bike.

## Five words, tops

I pointed the research queue at the voice list: dictate a question, let the machine pick it up.

Two walls, immediately.

The first wall: voice capture is rough. Even with the "add something" trick, what you get back is short. My very first test reminder, the one I dictated to prove the plumbing worked, said — in its entirety — "Test." My second said "Write a cue that turns this into research tasks," which is an instruction to a machine, not a research question. Real dictation is human. It's ambiguous. It's misunderstood.

The second wall: the research machine expects a real question, not garbled, mumbled words. Feed it "jellyfish sleep" and it does its best, but two words in makes for two words out — garbage in, politely-cited garbage out. Something had to turn my mumblings into a question worth researching before the machine ever saw it.

## Give the list a brain

When the helper checks my research list now, it doesn't just copy the terse line across. It takes my fragment — "jellyfish sleep" — and quietly expands it into a proper brief before handing it to the machine. It fills in the scope, the questions worth answering, what a good answer would even contain, and a note to cite real sources. It does for my half-thought exactly what I'd do if I sat down and wrote the question out in full — except I didn't have to sit down, and I didn't have to write it.

That's the whole trick: the dictation doesn't have to be good anymore. The machine meets me the rest of the way.

A mumble is enough.

And since it finishes my sentences for me, I let it finish the task as well: the helper reaches back into Apple Reminders and ticks the original reminder off.

## What did Siri actually hear?

When the machine expands my fragment into a polished brief, that brief goes into the queue — and it can be *wrong*. If Siri misheard me, the expansion confidently builds a whole research question on top of the misunderstanding. And once it's dressed up in full sentences, you can't tell it started life as three mumbled words. The evidence of the mishearing is gone.

I asked for a receipt. Every expanded question now carries the raw thing I actually said, tacked on the end in quotes — *(dictated: "Wie schlafen Delfine" — how do dolphins sleep)*. If the research comes back subtly off, I can glance at the receipt and see the fork in the road: was the idea bad, or did the phone just mishear me? Keep the original words, and a wrong turn is diagnosable instead of mysterious. Keeping them cost nothing; throwing them away would have cost real confusion.

## Hallo, Florian

One last test before I trusted it. I dictated to the research list: "if it works, send a Discord message saying hallo Florian." A little dare to the machine.

It did not, of course, send me a message that said "hallo Florian." It's a *research* machine. It took my dare completely at face value, expanded it into an earnest research question — what's the most reliable way to send a Discord message when something succeeds: a webhook or a bot, the two ways software can post into Discord? — went off and actually researched it, wrote up the answer with the official documentation linked, and then pinged me on Discord to tell me it was done.

My phone buzzed — a real, cited answer to something I'd only spoken out loud, without touching a key.

It missed the joke and nailed the point: the road was open, end to end.

## The list that empties itself

I'm on the bike. A thought lands — some question I'd never make time to chase. "Hey Siri, add something to my research list." "What's the something?" I say the half-formed version, whatever comes out, handlebars still under both hands. And it starts working, and comes back to me eventually.

Ten minutes later — often before I'm even home — the write-up is waiting: my mumble turned into a real question, researched, with the sources linked.

And I don't have to be home to hear it. When the research finishes it pings me with a sentence or two of what it found, written to be *listened* to. My phone can read a new notification aloud — it asks first, I say yes, and it reads the summary while I ride. Not seamless, but the answer reaches me on the way home instead of waiting at my desk.

I didn't build something new. I built the missing piece between things I already had — an extension for my research machine. Now it finishes my sentences, and it works while I'm on the bike.
