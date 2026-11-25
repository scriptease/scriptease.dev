---
title: "The Ticket That Filed Itself"
url: "https://scriptease.dev/posts/2026-07-05-the-ticket-that-filed-itself/"
author: "Scriptease"
created: "2026-07-05"
published: "2026-07-05T21:31:30+02:00"
description: "Somewhere on the autobahn to Austria, a colleague filed a support ticket at 130 km/h — both hands on the wheel the whole time."
tags: ["ai", "jira", "gerrit", "automation", "voice", "saga"]
---

# The Ticket That Filed Itself

_The [Hands-Free saga](https://scriptease.dev/sagas/#hands-free): 1. The Ticket That Filed Itself · [2. Siri, Add Something to My Research Queue](https://scriptease.dev/posts/2026-07-18-siri-add-something-to-my-research-queue/) · [3. My Personal Hacker News](https://scriptease.dev/posts/2026-07-25-my-personal-hacker-news/) · [4. On the Shoulders of Giants](https://scriptease.dev/posts/2026-10-04-on-the-shoulders-of-giants/) · [5. Factory Reset](https://scriptease.dev/posts/2026-10-11-factory-reset/) · [6. Two Nos Make a Yes](https://scriptease.dev/posts/2026-10-18-two-nos-make-a-yes/) · [7. Reviewing the Reviewer](https://scriptease.dev/posts/2026-11-07-reviewing-the-reviewer/)_

Somewhere on the autobahn to Austria, a colleague filed a support ticket — both hands on the wheel the whole time.

We were carpooling to a company trip. He'd taken over driving; the rest of us were in the backseat, deep in some AI discussion. Then a few phones buzzed at once: a work notification saying *he* had just created a new ticket in our tracker. Someone laughed — *he's filing tickets with his knees at 130 on the autobahn?*

He hadn't touched a thing. A little robot he'd built had done it for him, on its own, while he drove.

## What the robot did

A quick translation, because none of this means anything outside our world.

Teams like ours track work in two systems. One is **Redmine** — think of it as the shared to-do list the business side files requests into. The other is **JIRA** — the to-do list the developers actually work out of. For years, someone had to read a request in the first list and re-type it as a task in the second. Boring, constant, easy to forget.

My colleague had automated exactly that. He'd built a small program that watches the first list and, whenever a new request shows up, files the matching task in the second one automatically — no human, no typing. That's the "ticket" that appeared while he was driving: the request had come in, and his robot did what he'd otherwise have done by hand.

Everyone else thought it was a party trick. I thought: *I have a chore just like that. I could do the same thing.*

## My chore

Here's mine. When developers change code, the change goes through a review gate called **Gerrit** before it's allowed in — like a bouncer who checks every edit. The trouble is the review happens in Gerrit, but the *task* lives over in JIRA, and the two don't talk. So to know "is the code for this task actually done and approved?" you had to open a second tool and go look.

For years I'd papered over this with a scrappy little script on my own laptop. Every half hour it woke up, checked Gerrit, and pasted a short status note onto the matching JIRA task. To avoid spamming everyone, it kept a tiny file per task remembering what it last said, and only spoke up when something actually changed.

It worked. It was also held together with tape: it ran only when my laptop was awake, and — I'll just admit it — my personal password to JIRA was typed directly into the script, in plain text. The kind of thing you'd be mortified to show anyone. It was mine, it was private, it was fine.

## The lawn chair

The next morning in Austria I woke up before everyone else. I took an iPad out to a lawn chair, looked at the mountains, and — without touching a keyboard — talked a whole software project into existence.

The setup is the same one I use to water my tomatoes from abroad: I speak, and **Maestro** (my voice-to-agent system) and **Maestro Relay** (the piece that carries my voice to a computer elsewhere) turn the words into work. I asked it to go find my colleague's robot — the actual job, the actual code behind it — using the Jenkins API skill, a helper I have for searching our build system. It found his project, made its own copy, and I said, in effect: *build me this exact thing, but for my chore instead of his.*

So the thing that inspired me became the literal template. I didn't start from a blank page. I started from his working robot and pointed it at my problem.

## Making it better

Getting the basic version working — a robot posting the status notes instead of me — immediately made me want to push it further. A single task often has several code changes attached to it, and I wanted all their statuses gathered neatly in one place, not scattered across separate notes. My first idea was to add a small custom box to every JIRA task to hold them.

I could have just asked. The person who administers our JIRA was right there on the trip with us — I could have leaned over and requested permission to add that box. But before bothering anyone, I fired off a research request — a question my agents go off and answer on their own — for the best way to do it.

It came back with a comparison table that settled the whole thing in one glance, and it had found something better than my own idea. JIRA has a built-in feature for **links to outside things** that needs no special permissions at all — just the everyday ability to add a link, which my setup already had. Each link can even carry its own little status. So instead of a custom box I'd have to ask a colleague to switch on, I'd attach one tidy, self-updating link per change — no favours, no permissions, nothing for anyone to approve. A better idea, and entirely mine to ship.

## The trail

The rest got decided on a mountain bike.

My computer stayed behind at home — the guesthouse we were staying in — awake and listening. Maestro Relay carried my voice from the trail to that machine, and a cloud session did the actual work. I asked it to dig up a real task with a lot of code changes piled onto it — the messiest case I could throw at it — and send me the link. I opened it on my phone mid-ride, looked, and thumbed back a two-word verdict: *doesn't fit.*

Here's the part that stuck with me. It didn't ask me what I wanted instead. It just went and made four versions, each formatted a different way — and rather than describing them to me in words, it put all four *directly onto a real JIRA task*, so I could see the actual thing rendered on my phone instead of imagining it from a description. I wasn't picking between paragraphs of text; I was looking at four live options on a mountainside and choosing the one that looked right.

So we'd stop at a viewpoint, pull the task up, and argue — as a group, sweaty and cheerful — about which little symbol should mean what. Green for approved. Red for a hard rejection. A skull-ish mark for a change someone had abandoned. A separate signal for "the automated tests are failing." A table of grown engineers voting on emoji on a bike trail, while a laptop 10 kilometres away did the typing and the rendering.

That's how the traffic lights were born.

## The fifteen minutes I thought I'd broken everything

Once the format looked right, I let it loose on everything — every open change across every task. To stress-test it, I had it pick the single worst case: the ticket with the most changes piled onto it. I opened that one to admire the result, and it wouldn't load. Just an error.

My stomach dropped. This is the system the entire company runs its work through. If my little robot had wrecked a ticket by stuffing too many links onto it, how many others had I quietly broken — from a mountain, with no laptop in reach?

So I tried to reproduce it properly. Different browser — same error. I stopped the script and had it strip every link back off that ticket, then reloaded it completely clean, no links at all. *Same error.*

Which was, oddly, the best news possible. If the ticket was broken *with* my links and *without* them, then I hadn't broken it — JIRA itself was just having a bad moment. Sure enough, about fifteen minutes later it opened fine. I switched the robot back on, it put every link back where it belonged, and everything worked.

But for those fifteen minutes on a mountainside, I was genuinely certain I'd found a way to remotely break every ticket my company owns.

So the small robot that runs every 30 minutes and updates the tickets in the background is finally back online.

## So what

The funny part was never that a ticket got filed at 130 km/h. It's that the *entire* life of a real piece of company software — cloning a colleague's idea, arguing about emoji on a bike trail, breaking it (or so I thought), and shipping it — all happened on the move. From a lawn chair, a mountain bike, and a phone, in my own voice, on vacation, while the laptop stayed home.

When building software gets this cheap and this portable, the hard part stops being the code. The hard part becomes taste: *which* chore is worth automating, and what the green light should mean. We spent a company trip in the Alps arguing about exactly that.

Same lawn where I water the tomatoes. Turns out it also ships for me.
