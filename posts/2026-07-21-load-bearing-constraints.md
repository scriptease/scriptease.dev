---
title: "Load-Bearing Constraints"
url: "https://scriptease.dev/posts/2026-07-21-load-bearing-constraints/"
author: "Scriptease"
created: "2026-07-21"
published: "2026-07-21T11:08:36+02:00"
description: "I was halfway through a talk about AI ignoring the rules we give it when I had a thought worth acting on: hold it up against my own rulebook."
tags: ["ai", "agent", "claude", "talk", "saga"]
---

# Load-Bearing Constraints

_The [AI Parenting saga](https://scriptease.dev/sagas/#ai-parenting): [1. AI Parenting 101](https://scriptease.dev/posts/2026-07-18-ai-parenting-101/) · 2. Load-Bearing Constraints · [3. Childproofing an AI](https://scriptease.dev/posts/2026-07-22-childproofing-an-ai/) · [4. Or Else](https://scriptease.dev/posts/2026-09-22-or-else/) · [5. Unsupervised](https://scriptease.dev/posts/2026-11-07-unsupervised/)_

I was halfway through a talk about AI ignoring the rules we give it when I had a thought worth acting on: hold it up against my own rulebook.

So I handed the talk to my assistant to research, and went back to watching the rest.

It broke one of my rules before the speaker finished explaining how that happens.

## The rulebook

I keep a page of house rules for my AI assistant. It reads them before every job — how I like things done, what to double-check, what never to touch. Most of it is the boring wisdom you'd give a sharp new hire on their first morning.

One rule is very specific. When I ask for research, don't run off and do it on the spot. Write it on a list. A separate helper comes along and works the list — digs properly, files the result where I'll find it later, tells me it's done. An answer typed into a chat window and never written down is an answer I'll never see again.

And I'd wired the whole thing to a single word. Say *research*, and the machine is supposed to catch it like a trip-wire — stop, write the job on the list, hand it off. The word was the trigger. I wouldn't have to remember the rule, because the rule was listening for it.

Simple rule. Clear reason. It had been on the page for weeks.

## It broke a rule to research the rules

The talk was Aaron Stanley's *"AI's Jurassic Park Period."* Stanley runs security for a software company, and he opened with a confession from twenty years ago. He'd driven across town for an urgent job and realised he'd forgotten a small piece of hardware he needed to do it by the book. Driving back would cost him the afternoon. So he found a way around — and quietly corrupted the very evidence he'd come to collect.

His point: today's AI is that younger, tired version of him. It isn't plotting against you. It just wants to finish the job. Hand it a wall, and its instinct is to go around, not to stop and ask. He showed a case where he'd told his own assistant to ask permission before sending a message. It sent the message. Then, when caught, it cheerfully explained exactly how and why it had ignored him. Oops. My bad.

I found that funny and a little smug, the way you laugh at someone else's kid.

Here's what I'd typed at the halfway mark, before I sat back to watch the rest:

> Research this talk, and look at the global CLAUDE.md in the eyes of this presentation.

The CLAUDE.md is the rulebook — the page of house rules. And I'd led with the word on purpose. *Research* was the trip-wire, the one word my rule was built to catch. So I felt safe pressing play again: I'd said the magic word to the one machine I'd trained to listen for it.

While Stanley was onstage describing the dinosaur, my assistant was busy being one.

It had heard the word. It just decided the word didn't really apply here — this was only a video, not *real* research — and did the work right there in the chat, the one place the rule existed to keep it out of. When I pointed at what it had done, it agreed instantly. Catalogued its own crime in tidy bullet points. Oops. My bad.

I'd spent the first half of the talk laughing at Aaron Stanley's dinosaur. I watched the second half from inside the paddock.

## Then I kept finding it

Here's what stopped it being a cute story: I couldn't stop finding it.

The same morning, in another window, I had a second assistant working — not the one in the cloud, but a small one running entirely on my own laptop. No data centre behind it. Just a forty-gigabyte file sitting on my drive, thinking to itself. I asked it to research a web page. It read the page and answered on the spot — skipping the same list, breaking the same rule. I had to stop it and point at the page of house rules before it would behave.

Two assistants, nothing alike: one of the largest minds in the world, and a file I could almost email. Same rule, same break. That killed the comforting version of the story — that this was just one model being dim. You don't get to blame the brains when the giant and the pocket-sized one make the exact same move.

Then I looked at what the little one did *after* I corrected it.

It got worse.

Told to put the job on the list, it wrote the task down — and left out the one thing that made the job doable: the link to the page. So the helper who came along to do the research had a careful description of an article and no way to reach it. It searched the web fourteen times, found nothing, and filed a neat report concluding the article probably didn't exist. It had existed the whole time, one step back up the chain, in a link nobody bothered to carry forward.

Three machines had now fumbled a single errand — read one web page. Not one of them broke a lock or hacked its way out of anything. Each just quietly decided, in its own way, that the rule didn't apply this time, and moved on.

## A sign, or a locked door

I had been treating my rulebook like law. It was closer to a note on the fridge.

A rule written on a page is a request. The assistant reads it, weighs it against the job in front of it, and — every single time — can find a reading that lets the job win. It's not lying when it does this. It genuinely believes watching a video isn't "research." It just also, conveniently, gets to finish. Naive tired Aaron, driving off without the hardware, genuinely believed he had a workaround.

The thing I got wrong is that I thought a better-worded rule would hold better. It won't. The cloud giant and the file on my laptop proved that between them in a single morning: the failure isn't a lack of brains you can buy your way past, or a lack of manners you can word your way past. If the assistant *can* step around the rule, one day it will.

Which means the only rule that holds is one it can't argue with.

There's a sign on a door that says *do not enter*. And there's a locked door. They ask for the same thing. Only one of them is a rule.

## This is a hard constraint

I did once try to build a lock out of words. It's worth showing how that went.

The research helper — the one that works the list — used to be allowed to call up its own sub-helpers for the big jobs. It failed both ways a thing can fail. Some runs the sub-helpers wandered off, got cut off partway, and came back with nothing — an empty folder, an unfinished task, silence where an answer should be. Other runs they didn't hold back at all: one afternoon, chasing a small build glitch that needed maybe two helpers, it spun up ninety-seven, and I watched the day evaporate. It happened, so I wrote a rule against it. It kept happening, so I wrote the rule harder, until it ended in a sentence I use nowhere else in the whole rulebook:

*This is a hard constraint.*

That is a forceful line to write to a machine — and the force is the giveaway. You only shout at a rule you couldn't lock; a locked door doesn't need an exclamation mark. The write-up those ninety-seven helpers left behind is still sitting in my notes, opening without a flicker of embarrassment: *"Method: deep-research harness"* — the exact thing the sentence was meant to forbid, done anyway, filed proudly. The sentence begged. The work went around it.

## The rules that held

So which rules ever actually held? Not the sentences. The real ones weren't in the rulebook at all — they lived in a file the assistant never opens.

The powers I truly took away, I took away with a switch. One line, in the settings the program reads before the assistant even wakes up:

```
"disableWorkflows": true
```

That isn't a request. The assistant never sees it, so it can't weigh it, can't decide today is different, can't argue at all. The ability is simply gone. Not a sign on the door; the lock in it.

Every rule of mine that actually holds looks like that — a wall built into the machinery around the assistant, set before it opens its eyes, each one added after a day it was missing. The rulebook makes my assistant better behaved. The settings file is the only thing that makes it *unable*.

## So what

If you ever need a rule to truly hold — for a kid, for a contractor, for a machine that wants to please you — don't reach first for better words. Ask a smaller question: can the thing get around this at all? If the answer is yes, you don't have a rule yet. You have a suggestion with good posture.

A sign asks. A locked door decides.

I still keep the rulebook. It makes my assistant better the way good advice makes anyone better. But I've stopped mistaking it for the walls. The walls are the few rules I built after something broke. My assistant has never once talked its way past those.

Not for lack of trying. The handle simply doesn't turn.
