---
title: "It's Time to Settle"
url: "https://scriptease.dev/posts/2026-10-30-its-time-to-settle/"
author: "Scriptease"
created: "2026-10-30"
published: "2026-10-30T08:08:32+01:00"
description: "I left a wish in a YouTube comment. Less than an hour later I had the parts of it working myself, using only the tools the app already had."
tags: ["ai", "agent", "automation", "git", "opensource", "saga", "t3code"]
---

# It's Time to Settle

_The [Hands-Off saga](https://scriptease.dev/sagas/#hands-off): [1. Non-Load-Bearing](https://scriptease.dev/posts/2026-07-21-non-load-bearing/) · [2. Taking Over the Workspace](https://scriptease.dev/posts/2026-10-25-taking-over-the-workspace/) · [3. Better Call Sol](https://scriptease.dev/posts/2026-10-28-better-call-sol/) · 4. It's Time to Settle · [5. Fake It Till You Merge It](https://scriptease.dev/posts/2026-11-21-fake-it-till-you-merge-it/)_

I left a wish in a YouTube comment. Less than an hour later I had the parts of it working myself, using only the tools the app already had.

## "Can you add support for non github focused stuff?"

My workday happens in T3 Code, an open-source app where I run my AI coding assistants side by side, one conversation per task. Its maker, Theo, had posted a video tour of the new version the day before.

One feature in it is settling. When a conversation's work is done, the app files it away, like an email you archive once it's answered. The sidebar stays an inbox of things that still need me. And it can settle on its own: once the code change the conversation produced is merged, the conversation disappears by itself.

That only works if your code lives on GitHub, a place for open-source code. Ours doesn't. So I typed this under the video:

> Can you add support for non github focused stuff?
>
> Like being able to remove worktrees, other url formats for pr style urls like gerrit, or a way to automate settle if you are not using prs?

Three wishes. This post is about the last one.

## Masquerading as a pull request

At work we review code in Gerrit, a code review system from Google. A change waits there until a colleague approves it, then it's merged.

T3 Code knows GitHub's "pull requests", which are the same idea under a different name. A month ago I taught it to take Gerrit changes for pull requests. My standing instructions tell every AI how to attach a Gerrit change to its conversation in pull-request format, and a small rule on our server makes that made-up link open the real change.

So the links were all there. I asked my AI to find out why my conversations still never settled, and to read T3 Code's source to see what auto-settle actually checks.

The answer: T3 Code tries to ask each linked pull request whether it's merged. A Gerrit link can't answer, so its status stays blank. And a blank status doesn't just skip that link. It blocks auto-settle for the whole conversation, including the fallback that tidies up anything untouched for days.

My disguise wasn't just failing to help. It was why those conversations never went away.

## "Reverse engineer the auto-settling"

Waiting for Theo was one option. The other was in my own message to the AI: "So I'm basically exploring how to reverse engineer the auto settling, but match it to our process."

My rule for this: no fork, no patch to T3 Code. The app already gives its AIs tools to read conversations, link pull requests and settle threads. I wanted a small script on my Mac to use those same tools, and to decide "done" the way we decide it: the Gerrit change is merged *and* the Jira ticket behind it is resolved.

There were two cases to cover. In the first, I start the conversation, the AI writes the code and pushes it to Gerrit, so the link is already there. In the second, I'm testing a colleague's work. I start the conversation from their ticket, and the script has to go find the changes itself. Searching Gerrit for the ticket number found all six changes for my test ticket. The ticket itself only pointed to the last one.

## The key to the wrong door

The script needs a key to talk to T3 Code. The first one we made worked fine for reading. When it tried to settle anything, it was refused.

The key's access level was "ask before acting", and my conversations run on "full access". T3 Code won't let a weaker key change a stronger conversation. The rule makes sense. It was still in my way.

My AI's recommendation was the polite route: T3 Code's command-line tool already gets full access for the moment it runs, and a "settle" command would be about twenty lines. Propose it to the maintainers, then wait for a release.

That was my YouTube comment again, just more specific. Ask, then wait for an update.

So I tried a shortcut: let the conversation settle *itself*. The script sends it a message, "your work is merged, settle this thread", and the AI inside does it.

"This thread will settle when this turn ends," it replied. Then it was gone.

"It worked. Both of the demo thread just disappeared on both of my devices."

## Caution: risk of burning tokens

It worked, and I didn't want it.

"The bad thing about it is that it settles by burning additional tokens, and it also might be way too expensive to run because if I have a five hundred thousand token [most expensive model] session and I settle this with this mechanism, then it would put everything in the cache again just to remove it immediately."

Every message wakes the AI, and the AI rereads the whole conversation before it can do anything.

And it isn't only the cost. A colleague merges my change or resolves my ticket, and an AI on my Mac wakes up and starts working while I'm not looking. Nobody should be able to start my AI except me.

The fix was already in the app. T3 Code lets you log a tool in through the browser: it opens a page and asks for a pairing code. "It's basically opening a browser window and asking for a pairing token." You choose the access level there, full access included, and the key is good for 30 days.

With that key the script settled and unsettled my demo conversation directly. No AI involved, no tokens spent.

## "Would it work with the baseline"

I didn't write the script myself. I asked my AI to have another T3 Code conversation build it, inside our team's repository of helper scripts, so my colleagues can install it too. Each of them runs their own copy on their own Mac, against their own T3 Code. Every five minutes a background job checks Gerrit and Jira and settles whatever is done. Midway I asked it to get the ticket status through the Jira tool we already have instead of building its own. That tool already reported everything needed.

While wiring that in, the builder found something I hadn't asked about. Our Jira tool put its password in the list of running programs, where any app on my Mac could read it.

A real bug, small and mine: "let's use this bug as an end to end test." A fresh conversation would write the ticket, fix the bug, send the fix to Gerrit, link it to itself and ping me when it was ready for review.

My AI started it the way my instructions say. Those instructions forbid one T3 Code feature: giving each conversation its own private copy of the project, a *worktree*. The copies stay behind after the work is done and pile up. That was the first wish in my comment.

I stopped it. "Because my Claude MD is there to prohibit this kind of bugs, but the task we're trying to get to work is to avoid having this special case." And then: "Because what we're building at the moment is basically would it work with the baseline."

No workarounds this time. The conversation ran the way T3 Code is meant to be used.

## It's time to settle

The fix came in, I reviewed it and merged it. I made a new Jira password, and the fix's own conversation checked that the new one worked and that nothing showed up in the list of running programs. Then it marked its ticket resolved.

The background job had just run, a few seconds before. It missed.

Five minutes later the next run came. Gerrit said merged, Jira said resolved. The conversation that had filed the bug, fixed it and tested it disappeared from my sidebar, and nobody had to tell it to.

## Settling for good

My conversations now settle on their own. The private copies of the project are another matter. There are still rough edges in how they get cleaned up, so the line in my instructions that forbids them stays.

But that's for another day. Two of my three wishes came true the same morning. The disguised Gerrit links had been there for a month, but until now they were only something to click. Now they're load-bearing.

When this post went out, my YouTube comment still said "1 hour ago".

## Did you know?

The video I commented under had a sponsor: Apify. The little program my script uses to talk to T3 Code, and the one behind our Jira tool, is [mcpc](https://github.com/apify/mcpc), and it's Apify's too. The ad ran in the video I left my wish under, and its sponsor's tool ended up granting it.
