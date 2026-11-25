---
title: "Reviewing the Reviewer"
url: "https://scriptease.dev/posts/2026-11-07-reviewing-the-reviewer/"
author: "Scriptease"
created: "2026-11-07"
published: "2026-11-15T10:48:50+01:00"
description: "My AI code reviewer worked the way a demo works. It read every change we made, found real problems, and wrote them down in comments that were marked as done the moment they appeared."
tags: ["ai", "claude", "agent", "automation", "saga"]
---

# Reviewing the Reviewer

_The [Hands-Free saga](https://scriptease.dev/sagas/#hands-free): [1. The Ticket That Filed Itself](https://scriptease.dev/posts/2026-07-05-the-ticket-that-filed-itself/) · [2. Siri, Add Something to My Research Queue](https://scriptease.dev/posts/2026-07-18-siri-add-something-to-my-research-queue/) · [3. My Personal Hacker News](https://scriptease.dev/posts/2026-07-25-my-personal-hacker-news/) · [4. On the Shoulders of Giants](https://scriptease.dev/posts/2026-10-04-on-the-shoulders-of-giants/) · [5. Factory Reset](https://scriptease.dev/posts/2026-10-11-factory-reset/) · [6. Two Nos Make a Yes](https://scriptease.dev/posts/2026-10-18-two-nos-make-a-yes/) · 7. Reviewing the Reviewer_

My AI code reviewer worked the way a demo works. It read every change we made, found real problems, and wrote them down in comments that were marked as done the moment they appeared.

## "It felt like a demo project"

[Last time](https://scriptease.dev/posts/2026-10-18-two-nos-make-a-yes/) I wrote about how it got there: Opus, the biggest Claude model, reads every change at our company and pins its findings to the line in Gerrit, the tool where our changes wait for review. Each finding is rated HIGH, MEDIUM or LOW.

It worked. My colleagues liked having it. It also repeated itself: the same finding came back on the next upload in different words, sometimes HIGH, sometimes MEDIUM. Developers had replied to one percent of its comments. It was easy to ignore.

Then I watched [a video by Theo](https://youtu.be/TFCDWrEBaFM), a developer who read [Anthropic's write-up](https://claude.dev/blog/solving-code-review-at-anthropic/) of how they review their own code out loud and argued with it. Their reviewer sorts its findings before a human sees any of them. Mine notified the author about every finding.

I told my AI what I had missed:

"we were looking for getting as much review as possible in it, but what I didn't think about hard enough is how can I reduce the mental load on the developer so that only important stuff is actually read?"

## "Now it disappears"

We started on the sorting, and got stuck on a detail. Every time you upload a fix in Gerrit, the change gets a new version. My AI wanted the reviewer's comments to stay on the version they were written for. I was torn:

"if you upload, patch set 1, and then the AI reviews something, and then you upload. Patch set 2, even by making a small change unrelated to the 1st one. Now it disappears"

My AI went to check the code. It was already happening. The reviewer posted every comment already marked "resolved", like a ticket closed on arrival. Gerrit only carries open comments over to the next version. Since its first day, everything the reviewer said had vanished the moment the author uploaded anything.

I wanted to see it. A colleague keeps a project just for testing the machines that check our code. There my AI wrote a small change with three planted bugs: a sum that was off by one, a database query an attacker could rewrite, and a division by zero on an empty list. The reviewer caught them. Then we uploaded a second version.

I clicked through it on my phone and sent screenshots back. The wrong version first. "sorry".

Resolved, all three. On the second version, not a trace.

## Review amnesia

So the new reviewer leaves its HIGH and MEDIUM findings open. They travel with the change from version to version until somebody deals with them.

That makes the repeating worse: the same finding, posted again, next to itself. My AI suggested telling the reviewer what it had already said. I didn't want that. "If I am saying, you already reported this, don't report this," it learns to look away from a whole kind of bug. So it still reads every version as if for the first time, and plain code afterwards drops a finding that already sits open on the same line. With one exception: "we should be able to bump it on the same line, but not reduce it."

Then the sorting. Haiku, the smallest and cheapest Claude model, reads Opus's list and has exactly one power: lower a rating by one level. It may "not find new bugs", and it can't delete one. Only HIGH and MEDIUM still send the author a notification. The rest is there if you look.

In the first two test runs, Haiku lowered nothing. We shipped it anyway.

## Keeping secrets secret

The next day I had my AI go back through everything the reviewer had written since October: nearly 1,300 comments on almost 600 changes.

About one in fifty looked like a false alarm. More than half had been ignored.

Eighteen times it had pointed at a password or an access key sitting in a change that later went in. Fourteen of those were ignored.

Our code is internal, so none of this was out in the open. But AIs read all of it now, the reviewer among them.

I had caught some like these myself and talked to the author. That was how it worked: the reviewer found it, and the follow-up was me.

## "Did you really mean to add those?"

The side effect showed up in my own browser.

In Gerrit, approving a change and putting it into the real code are two steps. For the second one I have a little script of my own that adds a one-click merge button to the page. On some changes my button stopped working.

Gerrit doesn't let a change with open comments through quietly. It puts up a dialog first, with every open comment in its own box. Until the new version, the reviewer had never left an open comment. Now its findings sit in those boxes, between the approval and the merge, and my one click doesn't get past them.

There are three ways through. Mark the finding as resolved. Write a reply. Or merge and ignore it.

Review needs one more step now. But it's the question I used to ask the author myself. And last month I had called the one percent a chicken and egg problem: "nobody responds because it doesn't have an effect at the moment." Now ignoring them takes a confirmation.

I could have made an answer required. I didn't.

## The passwords came out

The week after, we went through our code and took the passwords out. Some were changed, the rest moved into a password manager, and the code now only holds a note saying where to find them.

Last time I hoped it would learn to say yes.

The reviewer leaves it open, so it just gives you one more opportunity to write down a why.
