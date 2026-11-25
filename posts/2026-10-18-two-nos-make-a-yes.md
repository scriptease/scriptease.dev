---
title: "Two Nos Make a Yes"
url: "https://scriptease.dev/posts/2026-10-18-two-nos-make-a-yes/"
author: "Scriptease"
created: "2026-10-18"
published: "2026-10-25T14:07:10+01:00"
description: "In July I wrote that I didn't know what to do with an AI code reviewer. By October one was reading every change our company makes, with a vote, and last week it objected to being overruled."
tags: ["ai", "claude", "agent", "automation", "saga"]
---

# Two Nos Make a Yes

_The [Hands-Free saga](https://scriptease.dev/sagas/#hands-free): [1. The Ticket That Filed Itself](https://scriptease.dev/posts/2026-07-05-the-ticket-that-filed-itself/) · [2. Siri, Add Something to My Research Queue](https://scriptease.dev/posts/2026-07-18-siri-add-something-to-my-research-queue/) · [3. My Personal Hacker News](https://scriptease.dev/posts/2026-07-25-my-personal-hacker-news/) · [4. On the Shoulders of Giants](https://scriptease.dev/posts/2026-10-04-on-the-shoulders-of-giants/) · [5. Factory Reset](https://scriptease.dev/posts/2026-10-11-factory-reset/) · 6. Two Nos Make a Yes · [7. Reviewing the Reviewer](https://scriptease.dev/posts/2026-11-07-reviewing-the-reviewer/)_

In July I wrote that I didn't know what to do with an AI code reviewer. By October one was reading every change our company makes, with a vote, and last week it objected to being overruled.

## "I still don't know what to do with the reviewer"

[The reviewer I tried in July](https://scriptease.dev/posts/2026-07-29-three-different-ocrs/) wrote a dozen comments on one change. Half were opinions, one was real. I kept the one good lead and filed the idea under "maybe".

Since then, the models got better. And the tokens got free.

In October, Anthropic, the company behind Claude, started handing its subscription plans a monthly allowance that only programs may spend, never a person typing in the chat. For a team like ours, up to five hundred dollars a month, use it or lose it.

That flipped the question. Not "is an AI reviewer worth paying for" but "what would I run on money that evaporates at the end of the month".

## Read everything, touch nothing

The reviewer started as a script I ran by hand on a colleague's change, a second opinion before my own review. It became a skill, a written recipe my AI follows, so anyone on the team could run it. [Last week](https://scriptease.dev/posts/2026-10-11-factory-reset/) it became a favour for a colleague who had run out of allowance.

Then it went live. Every change, in every project, gets read by Opus, the biggest Claude model, in a sealed box with a read-only copy of the code. It may look, search and read. It may not change anything.

Its findings land in Gerrit, the tool where every change at our company waits for review, pinned to the line, each with a severity, a why and a fix. Gerrit lets a comment be marked as coming from a robot, and the old version of its web page, which most of us still use, hides those entirely. "Which I kind of like." Then it turned out my own AI couldn't see them either. So I dropped the robot label, and the reviewer became a commenter like the rest of us.

## Can it say no?

Within days my colleagues asked for more. The reviewer rates every finding HIGH, MEDIUM or LOW, from serious to minor. If it finds a HIGH, let it vote. In Gerrit a vote of minus one is a flag, not a lock. It says "look again", and it vanishes as soon as the change is updated. So I gave it the flag.

My test change showed the first crack. The same issue came back HIGH in one run and MEDIUM in the next. Same code, same reviewer, different mood.

"ok then lets push it and test on the next reviews"

The reviewer's first job after that was to review the change that gave it the vote. It found a minus one that never gets cleared. My AI checked the server's rules: the vote is dropped whenever the change is updated. "leave it."

The reviewer never heard that. Every run started from scratch.

## Only one percent replies

By Saturday I had a worry and wanted it "found in reality, not just implemented". A doom loop: HIGH findings, fixed, then MEDIUM, fixed, then LOW, forever.

The AI went through every review so far. The loop was real, but it wasn't a ladder. Each run reports a different random handful of what it sees, so a re-review finds "new" things that were there all along.

Developers had replied to one percent of the reviewer's comments.

"nobody responds because it doesn't have an effect at the moment. So it's kind of a chicken and egg problem."

So instead of feeding the reviewer its own past, I fed it ours. The next review now sees every finding a human has answered, and what the human said. A rejected finding stays rejected. Reply to the robot, and the robot listens.

"we are 10 people, so I can tell them on Monday."

## A valid concern

I pushed that change. The reviewer reviewed it, rated it MEDIUM, and warned me about prompt injection, the trick of smuggling orders to an AI inside text it reads:

> […] the owner (or any registered user) can reply 'not an issue' to a HIGH finding. […] The model is also told to obey these comments, so this is a direct prompt-injection path for non-reviewers.

The reviewer had looked at the one feature that lets people tell it no, and called it an attack. Its fix: stop listening to the person who wrote the change.

I replied on the line, the first human reply the new loop ever saw: "Intended: the owner rejecting a finding is the use case."

## Looping loops

On Monday afternoon I ran the doom loop on purpose. My AI had written a small command-line tool for our ticket system, and I told it: "push until only low". Fix the findings, upload the fix, wait for the review, repeat until nothing above LOW is left. Every round the reviewer found something new and sounded more convinced: the script "mostly works", "is mostly sound", "is mostly solid", "is solid overall". Round after round, and in under an hour it got there.

While that ran, another change of mine was ready, so I asked a colleague in Slack, our work chat, to review it.

The link in my message woke up my Slack watcher, the one from the favour. It had a second AI, a GPT model, review the change, and posted a HIGH on it in my name.

Then my colleague: "Review agent is complaining with a High."

Me: "s&%# I forgot the trigger ahaha"

My AI checked the finding. The code already did what it asked for. My AI answered it on the change, and I pasted the answer into Slack: "the HIGH finding is wrong, so there is nothing to fix." That message had the link in it too. The watcher woke up again and found a fresh HIGH, plus a few MEDIUMs.

My colleague: "oh, do the two of them want to step outside?"

And then: "the least you can do is comment it so a review agent stops nagging."

The findings I disagreed with already had a no on the change: one I had typed just before asking for the review, "It's fine there is only one window when this runs", and my AI's answer to the HIGH. I fixed what was left. The next Opus review ended: "both reviewer-rejected findings stay excluded." My colleague approved right after.

Both nos came from the change's owner. Intended.

It took no for an answer.

## Can it say yes?

On another change of mine, the first round found a mistake that would have broken the server's answer, hidden by a test I had written that checked a blank instead of the real thing. My colleagues' verdict, as I had summed it up that Saturday: "it's good to have it, and it's spotted some issues where we could have missed something." But it only knows one vote. It can flag a change. It can't approve one.

Not long after, [the news digest my AI writes for me](https://scriptease.dev/posts/2026-07-25-my-personal-hacker-news/) served [an article by Will Larson](https://lethain.com/small-changes/) about small changes at his company. There a change can skip the human approval if it's small, the AI review found nothing serious, and the author has a track record in that part of the code. The bot that approves them has "only two options: approve or ignore." Only a small share of changes qualifies so far.

That night I asked my AI what it would take here. One risk it named: a crafted change that talks the reviewer into finding nothing. Prompt injection, the attack the reviewer had warned me about days earlier. This time it was a valid concern. So the model can't be the only gate. The size, the author's track record and the projects too sensitive for automatic approval would be checked by plain code.

It's a ticket for the team to discuss now, not a feature. The first step is only to count how many of our changes would have qualified.

In a few months it went from a maybe to a reviewer that reads everything we write, flags what it rates high, and listens when we answer. It learned to take no for an answer. Next, maybe, it learns to say yes.
