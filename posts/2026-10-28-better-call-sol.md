---
title: "Better Call Sol"
url: "https://scriptease.dev/posts/2026-10-28-better-call-sol/"
author: "Scriptease"
created: "2026-10-28"
published: "2026-10-28T19:58:45+01:00"
description: "I watched a YouTube video about a trick I already used. His version was fancier. Mine was about to get a better name."
tags: ["ai", "claude", "agent", "codereview", "skills", "saga"]
---

# Better Call Sol

_The [Hands-Off saga](https://scriptease.dev/sagas/#hands-off): [1. Non-Load-Bearing](https://scriptease.dev/posts/2026-07-21-non-load-bearing/) · [2. Taking Over the Workspace](https://scriptease.dev/posts/2026-10-25-taking-over-the-workspace/) · 3. Better Call Sol · [4. It's Time to Settle](https://scriptease.dev/posts/2026-10-30-its-time-to-settle/) · [5. Fake It Till You Merge It](https://scriptease.dev/posts/2026-11-21-fake-it-till-you-merge-it/)_

I watched a YouTube video about a trick I already used. His version was fancier. Mine was about to get a better name.

## "I already use Sol his way anyway"

Theo, a developer on YouTube, made a video called [These 3 skills changed my life](https://www.youtube.com/watch?v=5Bmp9cz1JN8). A skill is a written recipe my AI follows when I say a certain phrase. One of his three is the Sol Loop.

Sol is GPT-6.1 Sol, a model from OpenAI. Opus, the biggest Claude model, writes the code. Sol reads it and complains. Opus fixes what's right, argues with what's wrong, and hands it back. Theo calls Sol "the Rottweiler".

I already did that. Every draft of this blog goes to Sol before it goes out. Code too, when I remember. I write a handoff, a note with everything the other AI needs to know, send it over, read the answer, fix things.

Just not that fancy. No rounds, no rules, no record of who won the argument.

## Such a better name

Theo's loop has a budget. Three rounds. Five only if the change touches security or could lose data. If a round comes back with nothing but nitpicks, stop.

And a receipt. Every finished change ends with a line saying how many rounds it took and whether Sol approved. Theo added it because Opus sometimes forgot to mention that the reviewer was still unhappy.

I wanted all of that. But his recipe isn't published anywhere, and it's built for GitHub, a website for storing and reviewing code. At work, changes wait for review in Gerrit, and Jenkins, the build robot, builds and tests every one of them before it votes green or red. And Sol Loop is a fine name, but there is a TV show about a lawyer you call when you're in trouble. Sol is the one you call before you're in trouble.

Better Call Sol.

## Voice to skill

Two voices went in, both through speech to text. Theo's, as the automatic captions of his video. And mine, one dictated sentence: build it on my stack. Gerrit instead of GitHub, Jenkins instead of GitHub's checks, my own handoff skill for talking to Sol.

My AI listened to both and wrote the skill. 87 seconds.

The receipt became a comment on the change in Gerrit, with one line more: whether Jenkins went green.

## The Rottweiler didn't bite, yet

The first run was the next morning, on a small fix for a delivery date. Sol read it, found nothing, approved. Jenkins went green.

Then two more, same result. Three changes, zero findings.

Either my code was perfect, or the Rottweiler was asleep.

The fourth and fifth took two rounds each. On one, Sol asked for a test I had skipped, and got it. It also flagged two things I didn't agree with. I wrote one line each on why, and in the next round Sol let them go.

That's the part I didn't have before. Not the arguing, the rules: a budget for the argument, and a receipt when it ends.

Back when I sent things to Sol by hand, those reviews went many rounds. So a bite is only a matter of time. I'm waiting for the next opportunity.

## "I want to know who did that"

In between, a different review came in.

Since [last week](https://scriptease.dev/posts/2026-10-18-two-nos-make-a-yes/), every change at our company also gets read by Opus. Its verdict on one of them read:

```
AI review (claude-opus-5-5): 1 HIGH, 1 LOW
```

The change had only moved existing code between branches, parallel copies of the project. The HIGH was in our payment code. When a customer splits a payment across several cards, each part should keep the details of its own card. The code copied them from the order instead.

So I asked my AI: "Can you find the commit that introduces it? I want to know who did that so I can notify them."

## Git blame yourself

Programmers have a command for that question. It's called git blame: point it at a line, and it tells you whose change last touched it.

It came back with a name. Mine.

Three weeks earlier. Co-authored by Claude.

The change that got flagged hadn't introduced the bug. It had carried mine along. So the fix was mine too. One line: take the card details from the payment, not the order. The test put card 1111 on the order and card 4242 on the payment. The payment had to keep 4242. With the old line, it failed.

Then I called Sol.

One round. No findings. Jenkins green. The receipt went up on the change.

I asked a colleague whether an older release needed the fix too. "No need to backport." No release had ever shipped the bug.

Claude co-wrote the bug. Claude also found it. Sol signed off.

```
Reviewed with Better Call Sol: 3 rounds, github-copilot/gpt-6.1-sol
Sol verdict: approved
```
