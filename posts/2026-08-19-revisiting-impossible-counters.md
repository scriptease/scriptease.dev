---
title: "Revisiting Impossible Counters"
url: "https://scriptease.dev/posts/2026-08-19-revisiting-impossible-counters/"
author: "Scriptease"
created: "2026-08-19"
published: "2026-08-20T00:12:40+02:00"
description: "The first countdown I ever shipped was rigged. It sat on our graduating class's website, counting down to the Abitur, our final exams — and it lied: faster during the day, slower at night."
tags: ["agi", "ai", "claude", "web", "github"]
---

# Revisiting Impossible Counters

The first countdown I ever shipped was rigged. It sat on our graduating class's website, counting down to the Abitur, our final exams — and it lied: faster during the day, slower at night. Averaged over a full day it was perfectly accurate. But nobody checks a countdown at four in the morning. If you looked at it over lunch, watching your remaining time drain visibly quicker than it should, it was built to make you a little bit mad.

Twenty-something years later, I shipped another dishonest clock. This one runs the other way.

## The domain predated the pun

My name is Florian Agsteiner, but nobody who has known me for more than five minutes calls me that. I'm Agi. Years ago I registered agionline.de — my nickname, online, nothing more.

Then the AI world decided that AGI means artificial general intelligence, the machine that can do everything a person can and the three-letter word of the decade. Suddenly every keynote, every forecast, every funding round orbited around when AGI would arrive. And my old nickname domain had quietly become the best pun I own: AGI, online. Well .de.

For years the domain did nothing but forward visitors to my blog. This week it finally got a site of its own — built in one evening, me dictating at my AI assistant while it typed.

## An announcement for nothing

I didn't want a portfolio. Portfolios beg. I wanted the page to take the other reading seriously: a product announcement for AGI, in the house style of every tech company that has ever announced nothing with total confidence.

So the page opens with a label — "AGI Announcement." Technically correct on both readings: it announces AGI, and it is Agi's announcement. Below it, one screen at a time, the corporate liturgy: *Something is coming. It's been a long wait. The specifics are confidential. Thank you for your continued patience.* In each line, exactly one word flashes blue and fades back into the gray.

Behind it all, a wall of flickering characters rains down the left edge of the screen, and every few seconds the noise resolves into a real word — a topic from this blog, *gardening*, *debugging*, *shark* — glows blue, and dissolves again. The static knows things. It isn't telling yet.

## The date has moved. It will move again.

The centerpiece is the timer, and the timer is the Abitur clock's revenge.

It looks like a countdown: years, days, hours, minutes, seconds, down to an estimated arrival date. It counts **up**. Two years and change until launch, and climbing. Every few seconds the whole clock flashes blue, a small note appears — *Schedule revised* — and the remaining time jumps forward by two hours to eleven days. The revision counter next to it started at 1,247. This has been slipping since long before you opened the page.

That is every AGI forecast ever made, told as a user interface: always about two years out, always confident to the minute, always revised before it arrives.

My school clock lied so the future would feel closer than it was. This one lies so it never arrives at all. I'd like to claim decades of careful artistic development between the two, but honestly it's the same joke, aimed better.

## For once, the launch date wasn't rigged

Halfway through the build, my rigged clock did the one thing it was never designed to do. It stopped.

I reloaded the page and reported the bug to my assistant exactly as I saw it: the counter is stuck, and the scrolling is dead too. The cause turned out to be one line of code asking for a value that didn't exist yet — and a browser handles that by silently giving up on all of the page's code. Clock frozen, animations dark.

There's something ironic about a fake counter being broken. So now it has its own test suite — an automated check that runs the whole page for eight fake seconds and fails loudly if the clock doesn't tick.

So it can be reliably dishonest.

## There is no product

If you keep scrolling past the vagueness — and the page gives you no reason to, which is the point — the announcement finally cracks. Two lines, alone on the screen:

*There is no product.*

*It is a human.*

Below that, the site drops the act. A plain text window looks the domain up — the way you'd look up who owns any website — and reports what it finds: full name, Artificial General Intelligence. Also known as: Agi, which is what people actually call me. Location, Munich. Alignment: opinionated, correctable.

And one more line: **uptime** — how long a machine has been running — counting up. It's the only honest counter on the page. The product above it counts up because it keeps slipping. This one counts up because I've been running for forty-two years.

## It might be right, this time

The site went live the same evening. The domain that had waited years needed four address-book entries, and the padlock in the browser's address bar took about two minutes. The product that will never arrive took one evening to ship.

Back then I rigged a clock to make a real deadline feel unbearable. Now I've rigged one to make an unreal deadline feel familiar. And the new clock might simply be right. Two years and change, pending revision — that's a defensible AGI forecast. It has 1,200 revisions of prior art.

Both clocks lie about time. Neither one lies about us.

You can watch the schedule slip at [agionline.de](https://agionline.de).
