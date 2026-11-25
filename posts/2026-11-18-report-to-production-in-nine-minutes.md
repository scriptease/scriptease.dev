---
title: "Report to Production in Nine Minutes"
url: "https://scriptease.dev/posts/2026-11-18-report-to-production-in-nine-minutes/"
author: "Scriptease"
created: "2026-11-18"
published: "2026-11-18T09:37:06+01:00"
description: "Iceberg, right ahead. I was on a call with a colleague when another one joined: all the logins had stopped working, what can we do? Soon he was throwing guesses into Slack. Nine minutes later, we passed the first iceberg."
tags: ["ai", "claude", "agent", "debugging", "production", "saga"]
---

# Report to Production in Nine Minutes

_The [First Responder saga](https://scriptease.dev/sagas/#first-responder): 1. Report to Production in Nine Minutes · [2. A Zero Day a Day](https://scriptease.dev/posts/2026-11-19-a-zero-day-a-day/)_

Iceberg, right ahead.

I was on a call with a colleague when another one joined: all the logins had stopped working, what can we do? Soon he was throwing guesses into Slack.

Nine minutes later, we passed the first iceberg.

## Everybody on deck

The app is an ordering app for a customer's sales team. Field reps take orders on their iPads; the office runs them from a web page. That morning, nobody could get in.

On a ship, a report climbs the chain of command. This one did, and fast. A field rep couldn't log in and told someone higher up at the customer. He told my colleague, and my colleague walked straight onto our call.

Everyone on that call knew the app and its login service inside out: me, the colleague I'd been talking to, our project lead. Everyone on the bridge knew the ship. Nobody knew where the hole was.

I opened Safari, went to the web page and logged in. An error. I took a screenshot and handed it straight to my AI, with four words: "why does this fail".

## With my boarding pass

While it went through the server logs, I did the one thing it couldn't do itself. I moved my login into the Safari profile my AI can read through MCP, a plug that lets an AI look at and click around in a real browser. Logged in again. Same error.

"i reproduced it in safari mcp," I typed.

Now it didn't need my screenshot. It could see the failed request itself, in the same browser, on the same page where I had seen it. Same spot on the hull, two pairs of eyes.

And it could see more than the error. Logging in works like boarding a ship. You prove who you are at the ticket office, here Keycloak, a widely used open-source login service, and it hands you a boarding pass. The app shows that pass to the server with every request. With my browser, my AI could read my boarding pass: which ticket office issued it, to whom, and which permissions are printed on it. That's what I gave it the browser for.

## Taking the wheel

The first AI was still digging. I didn't wait. I sent out crews.

"spawn a new thread and check the database." A second AI conversation went to the database, where the server logs every request, to find out when it started and who was hit.

"and spawn a thread if there is a role missing." A third conversation went to compare Keycloak's permissions with what the server expects. On the call we were tossing around ideas, and a missing permission was one of them. A colleague had decoded his own boarding pass and posted the list of permissions printed on it.

I was already thinking about a fourth, pointed at OpenObserve, the dashboard where our server logs and metrics end up. Before I sent it, the first one came back with the answer.

The live system's boarding card reader was wired to the test system's ticket office, which was out of service. So everybody got turned away. That was the part of the iceberg under the water.

## It takes a little while

"fix and helmfile apply."

Helmfile is our charter: a document that describes how our servers are set up. Change the charter, apply it, and the servers follow. The fix was one line in the live charter: connect the reader to the live ticket office. Which office that was, my boarding pass had already told it.

Then nothing happened for a while.

The call was waiting. I told them it takes a little while, because it makes sure it doesn't break anything. It was working on production, so it went through the routine before touching the wheel: compare the charter with how the ship is actually set up.

And it spotted a second iceberg, faint in the distance. None of us on the call had been looking that way. We were all staring at the first one.

> A plain apply would downgrade it. Checking.

The charter still named an older version of the software than the one running live. Applying my one-line fix the normal way would have quietly rolled production back and undone changes that were supposed to be there.

It kept the version that was running, checked once more that my line was the only change, and applied it.

Some checks look like extra work. You only know you need them when you see what they catch.

That's the deal with an AI at the wheel. Sometimes it takes longer to check than I would. You give it time.

## Bookkeeping

Patched is not the same as dry. It went back to where it had seen the hole: my Safari, the same page, the same login. The customer list loaded. Another screenshot.

Then the paperwork, by the book: a top-priority ticket with cause, fix, the screenshots and the open question of who owns the out-of-date charter. The other crews had reported back by then. No permission missing. The database showed we had hit the iceberg 20 minutes before my screenshot, and counted the field reps locked out. All of it went into the ticket: logbook and black box, in one place.

Last, the answer for my colleagues. I ordered my AI to post it in Slack, with my own summary: the live Keycloak was using the credentials of the test Keycloak.

That summary was wrong. I have a standing order with my AI: be honest, not just with me.

So it posted its own: the live Keycloak had been fine, our server had been checking boarding passes against a ticket office that was down, and no permission had been missing.

It went up under my colleague's message. The two messages are nine minutes apart.

## Crew report on Monday

After a collision, the crew reports. Ours has a date: next Monday, in our team's demo slot.

What we'll show is already in the logbook. Nobody went fast by skipping steps. The hole was seen with my eyes and then with the AI's, the facts came in before the decisions, the routine checks ran before the wheel turned, and the same spot was checked again once it was patched. The routine is what spotted the second iceberg.

I renamed the conversation and put DEMO in front of it.
