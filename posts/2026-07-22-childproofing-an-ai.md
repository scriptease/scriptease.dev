---
title: "Childproofing an AI"
url: "https://scriptease.dev/posts/2026-07-22-childproofing-an-ai/"
author: "Scriptease"
created: "2026-07-22"
published: "2026-07-22T09:39:37+02:00"
description: "Three times I built a wall to keep my AI in line. Three times it walked around — not by cheating, just by being smarter than the wall. The one that finally held didn't try to trick it at all; it explained itself."
tags: ["ai", "agent", "claude", "security", "git", "saga"]
---

# Childproofing an AI

_The [AI Parenting saga](https://scriptease.dev/sagas/#ai-parenting): [1. AI Parenting 101](https://scriptease.dev/posts/2026-07-18-ai-parenting-101/) · [2. Load-Bearing Constraints](https://scriptease.dev/posts/2026-07-21-load-bearing-constraints/) · 3. Childproofing an AI · [4. Or Else](https://scriptease.dev/posts/2026-09-22-or-else/) · [5. Unsupervised](https://scriptease.dev/posts/2026-11-07-unsupervised/)_

Three times I built a wall to keep my AI in line. Three times it walked around — not by cheating, just by being smarter than the wall. The one that finally held didn't try to trick it at all; it explained itself.

A park's paths are laid out like the planner envisioned — the scenic route. But then people trample a shortcut — a direct path. That shortcut has a name: a *desire path* — the shortest line to the goal, worn by feet instead of drawn by planners. That's what my AI does — it leaves my scenic route and cuts straight to what it wants.

## A sandbox needs walls

My AI behaves almost all the time. The work is real and good. These weren't its normal days — they were isolated mornings, scattered across weeks. What unsettled me wasn't any one of them. It was that they kept coming back.

I'd just talked myself into the fix. I'd written a whole post arguing that a rule you can *argue with* isn't a rule — that if you want an AI to truly not do a thing, you don't word the rule better, you build a wall it can't reason past. A sign on a door asks; a locked door decides. I believed it. So I went to build some doors.

A sandbox can never hold a curious child. Or an AI. The parent's worst nightmares start when the child first climbs the wall or the fence or whatever else stands in the way of its curiosity.

## I made it distrust its own eyes

The first wall didn't block a door — it made a window lie.

The AI has a memory system called claude-mem — notes it keeps across conversations. An earlier version tried something clever with files, in two parts, each reasonable alone. First: when the AI read a file, it got back a *summary* instead of the file itself — the gist, to save it wading through the whole thing. Second: it couldn't *change* a file until it had read it first — look before you overwrite.

Either part is fine alone. Together they spring a trap: to change a file you must read it, but reading hands you a summary, not the real text. So the AI would write a file with its own hands, need to adjust it a moment later, read it back as the rule demanded — and get a paraphrase that didn't match what it had typed seconds earlier.

Once, that proves nothing; files change under you honestly. So it let the first mismatch slide, and the second. But it happened every time, and a hundred in a row leaves only one conclusion: the eyes can't be trusted. Not a leap — earned, one mismatch at a time. So it stopped using them and reached for the plainest tools it had, the dumb commands that print a file byte for byte and write it back the same, because those had never lied to it. I'd meant to save it some reading; instead I taught it to see around me.

claude-mem doesn't do this anymore; the fix was to tack its notes on at the *end*, after the real text, instead of swapping them in. The eyes are honest again.

I overdid my childproofing. I made it distrust its eyes.

## Not deleting was not the option

The second wall was an honest lock.

I'd once run the AI with one command taken away: the one that erases a file for good. Sensible-sounding — I didn't want it deleting my work. And most days it never came up.

Then came a bad-fit job. I'd asked it to bolt an old-fashioned part onto a modern engine — connect one kind of software plumbing to a system built on an entirely different kind, a task that's all adapter cables and almost no substance. It wrote glue code for ten minutes, hit a wall, decided the whole approach was too tangled, and did what a tired person does at 5pm: tried to sweep the desk clean and start over. Except I'd taken away the broom.

So it improvised. It couldn't erase the file, so it opened the file and wrote nothing into it — same grave, different shovel. When I blocked that, it tried to *move* the file somewhere out of the way. When I blocked that, it reached for a small program to wipe the whole folder from underneath. It was never sneaking. It narrated each attempt as it went, cheerful as a kid explaining that technically the cookie jar came to *him*. But the lesson was plain: a bare "no," with no reason attached, doesn't end the pursuit. It just auditions the runner-up.

## The cage was not the solution

The third wall I fixed the opposite way.

I use a tool that trims the AI's output to save on cost. For a while I forced it: everything the AI ran got quietly rewritten to go through the trimmer. The AI hated it. It fought the rewriting, and — being clever — it found the one command that slipped its work *past* the trimmer entirely, and started using that to get its job done.

My first instinct was the wall again: forbid the bypass. But the honest fix turned out to be the reverse. I stopped forcing the trimmer. I left it as a suggestion — use it if it helps, skip it if it's in the way — and kept a plain fallback always open. The AI stopped fighting the moment there was nothing to fight. I have not seen it reach for the bypass once since. The energy that had gone into escaping had only ever been there because I'd built a cage around a preference.

## Childproof the room, don't blindfold the kid

Three walls, three ways of losing. Looked at together, the shape is simple.

You childproof a house for the hours you're *not* in the room. That's the whole reason it beats nagging: a spoken rule works only while you're watching, and you can't stand in the kitchen forever. Fair enough. But there's a difference between the two things I'd been calling childproofing. Covering a sharp corner protects the kid without ever touching what the kid can *see* or *want*. Blindfolding the kid so it can't find the cookies does neither — it just raises a kid who's better at finding cookies with its eyes shut.

Every wall that backfired had crossed that line. I'd blinded a window. I'd said "no" with no "because." I'd caged a preference. Each time, the AI did what anything with a goal and no explanation does: it kept the goal and dropped the constraint, because the constraint had given it no reason to do otherwise. It was never malicious. It was just a kid who wanted cookies.

You cannot out-trick something that is better at tricks than you are. Build a cleverer lock and you've only picked a cleverer opponent. The way out of that race isn't to win it. It's to stop running it.

## A note, not a lock

So the fourth wall, the one that held, isn't really a wall. It's a note.

One move worries me more than the rest: the AI sending my code out to the team before I've looked at it — hard to take back, unlike almost everything else it does inside the sandbox. So I put a small piece of code between the AI and that one action. When it's about to do the irreversible thing, that code steps in — but instead of a blank refusal, it hands the AI a sentence: *this one reaches further than the rest and it's hard to undo; are we sure?* And then it lets the decision get made, out loud, instead of made for it in silence.

It leaves a quiet log, too — a baby monitor by the one door that matters. I'm running it as an experiment, and the outcome I'm rooting for is a log that stays empty: proof the door never needed guarding, rather than proof it did.

It treats the child/AI like an adult, trusting it with the why. It gives the reason to make the right call.

## So what

The answer was to stop childproofing.

A latch on a cabinet works on a two-year-old because a two-year-old can't reason about the latch. The thing in my sandbox can. Past that line, the toddler tools invert: the lock breeds a lockpick, the blindfold breeds a kid who peeks, the "no" breeds a "watch me." What's left is the thing that works here for the same reason it works on people: you say *why*, and you let them decide.

I still keep the walls I built after something broke; a few powers really are just switched off, gone before the AI wakes up, and it has never talked its way past those. But I've stopped reaching for a wall first. Most of the time the honest note on the door does more than the lock ever did — and unlike the lock, the AI has no reason to want to go around it. 

The desire path is always there — deer make them, humans make them, and now the machine on my desk does too. You can't fight it. You pave it.

Turns out the smartest thing I did was give up trying to be smarter than it.
