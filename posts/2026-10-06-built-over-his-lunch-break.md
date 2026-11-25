---
title: "Built Over His Lunch Break"
url: "https://scriptease.dev/posts/2026-10-06-built-over-his-lunch-break/"
author: "Scriptease"
created: "2026-10-06"
published: "2026-10-06T20:32:18+02:00"
description: "I asked a colleague how we could build something new. Then he went to lunch. By the time he was back online, it was built, and the demo I gave him took longer than the build."
tags: ["ai", "agent", "browser", "password", "commandline", "saga"]
---

# Built Over His Lunch Break

_The [Login Everywhere saga](https://scriptease.dev/sagas/#login-everywhere): [1. Every Login All at Once](https://scriptease.dev/posts/2026-09-05-every-login-all-at-once/) · 2. Built Over His Lunch Break · [3. Sharpening My Axe](https://scriptease.dev/posts/2026-10-31-sharpening-my-axe/)_

I asked a colleague how we could build something new. Then he went to lunch. By the time he was back online, it was built, and the demo I gave him took longer than the build.

## A tool for the back of my head

The talk was called "MCP Doesn't Suck. Your Agent Does." MCP is a standard plug that lets an AI use an outside tool: a browser, a database, a ticket system. The speaker built a small program that turns any of those plugs into a plain command an AI can type, the way it already types a thousand other commands every day.

I watched about 60 percent of it before work. I had already done this twice by hand: taken an MCP plug and turned it into a command. Now someone had built a tool that does it for any plug. I filed it away: the next time this lands on my desk, I'll try it.

Then I forgot about it.

## "This is not a state I can be in"

The morning went into a different login tool, the one my AI uses to sign into our iPad app in the simulator, a fake iPad on my Mac. Until then it wanted my fingerprint every twelve hours. I rebuilt it so I give permission once per app and simulator, and from then on the AI logs in on its own. By late morning I had four agents working in parallel, none of them waiting for me.

Then I had to check a ticket for our web app. It had been sitting there for a week, and the bug was still there. Proving it was easy: two screenshots, taken by hand. Getting to them took twenty minutes of setup: open the right server, find the right test user, log in, click to the right screen.

I had just spent a morning running four things at once, and now I was spending twenty minutes on two screenshots.

This is not a state I can be in. So let's automate this one too.

## "But I don't want an MCP. I want a CLI."

I had no idea about browser automation. So I asked someone who had done it: one of my web colleagues. We talked about how we could build it.

Then he went to lunch.

So I asked around, and the piece I needed already existed. It's called playwright-secure-mcp. Playwright is a remote control for a web browser that a program can hold. The wrapper adds one trick: it types passwords straight from 1Password into the page, and the AI never sees them. Every reply that would contain a secret gets blacked out.

But it was an MCP plug, and I wanted a command. Better still, an AXI: a command that follows the [ten rules](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/) for tools whose reader is an AI instead of a person. The AI only reads up on it when it needs it, which is also what the talk argues. And then I remembered the morning.

I didn't remember what the project was called. I googled something like "some kind of API, some kind of MCP, some kind of CLI", and it was in the top results: mcpc, by Apify, the program from the morning's talk. The "API" I had remembered was the company's name.

I pasted the two links into a new session and wrote one sentence: "can you setup a cli that uses mcpc to wrap the playwright-secure-mcp".

## Just let me in

A Chrome window opened. A visible one: I had asked for that. It went to our web app, the app sent it to a sign-in page, and the AI asked for the username.

Refused.

The wrapper has a rule: it only types a password on web pages that are listed in that password's 1Password entry. Our login was on a different address than the app. So I added an address to the entry. "try again"

Still refused. I had added the wrong one: the form sat on yet another address. I added that one too.

The username went in. Then the sign-in page handed over to a third address for the password. Refused again. I added that one too. "added"

Logged in.

That rule is the reason the tool exists: the password only gets typed on addresses saved with it in 1Password. It just meant my first login was a negotiation, one door at a time.

About twenty-five minutes after the first message, the first version of playwright-axi was published.

## "logout and back in"

Then came the small stuff that turns a demo into a tool. With the same trick as the morning's, a catalog of which login lives where, adding a user became a list entry instead of a code change. "why does it ask for the password twice, once on start and once when chrome is there?" Now it asks once. Chrome stopped offering to save the password, and a German warning bar went away on the second try.

And logout, which in our app hides behind the menu button. I wanted to know it really worked, so I kept typing the same four words.

"logout and back in"

"logout and back in"

"logout and back in"

Once it reported an error for a logout that had worked: the redirect afterwards was slower than the tool's patience. One fix later, it held.

## Dogfooding in progress

While I was still polishing, word came back on the ticket: fixed. Time to eat my own dog food, as programmers call using your own tool for real work. One agent deployed the new version. Another one logged in with the new tool and tested it. Halfway through it needed a different user, so the tool got a second login, in the middle of its own first test.

The agent took the screenshots and wrote the ticket comment. All I did was drag the pictures in. Then the same version went to the test server our customers try new builds on.

The ticket that started it all went from still broken to in our customers' hands while the tool was being built.

Before the evening, the tool was up for review, had a documentation page, a setup guide, and a third login for a different country. Half an hour to build. An hour until it was ready to ship.

## The verdict

My colleague still wasn't back from lunch. While I waited, I showed it to our other web developer. When the first one came back online, I invited him too and demoed it to both of them, for over an hour.

Both of them use it now.

In the evening I finally watched the remaining 40 percent. Then I asked my vault whether I had researched the talk. It wasn't even in the queue. I queued it, and while the research agent went through the whole talk, I started writing this post.

The first draft and the verdict arrived at the same time. The verdict on my new tool: it "already runs this exact pattern, so the talk confirms current practice."

Informational. No action needed.
