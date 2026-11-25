---
title: "Tomato Maxing"
url: "https://scriptease.dev/posts/2026-07-05-tomato-maxing/"
author: "Scriptease"
created: "2026-07-05"
published: "2026-07-05T18:36:26+02:00"
description: "It was 37°C in Munich. Taking a break from a talk about token maxing, my mind wandered to my tomatoes — and the pump keeping them alive, which I was fairly sure I'd just bricked."
tags: ["gardening", "automation", "commandline", "ai", "saga"]
---

# Tomato Maxing

_The [Tomato Maxing saga](https://scriptease.dev/sagas/#tomato-maxing): 1. Tomato Maxing · [2. The Pump Talks Back](https://scriptease.dev/posts/2026-07-11-tomato-maxing-ii/) · [3. Only Six Percent Left](https://scriptease.dev/posts/2026-07-15-tomato-maxing-iii/)_

It was 37°C in Munich — a record. I was deep in a presentation about token maxing — our jargon for squeezing every drop of work out of an AI — and to clear my head I stepped back from it and let my mind wander. It landed on the watering system out on my balcony — and the heat wave bearing down on it while I'd be gone.

Four days later we'd drive to Austria. An hour into trying to make that €30 WiFi watering pump do what I wanted, I was fairly sure I'd just bricked it.

Let me back up.

## One innocent question

The pump sits in a 35-litre bucket and pumps water to the plants. It came with a phone app called ELESION — tap a button, the pump runs. Fine, until you want to leave town during a heat wave and water your tomatoes from a mountain in Austria.

So I asked a simple question: *can I control this thing with code instead of my thumb?*

And one constraint made the whole thing hard. I'd be 300 km away. Any clever trick that only works while my laptop is on the same WiFi as the pump is useless from Austria. I didn't just need to control the pump — I needed to control it **through the internet**. That single requirement is what turned an afternoon into a fight.

## The fight

The way in is a platform called **Tuya** — the Chinese company that builds the guts of thousands of cheap smart gadgets. "ELESION" is just a sticker on top; underneath, it's a stock Tuya device. Tuya has a proper developer door. Getting through it took three walls.

**Wall one: a QR code that gaslit me.** To grant my code access, you scan a pairing code with the phone. Every time I scanned it and confirmed, the website instantly said "expired." Then I noticed the tell: *it only expired when I pressed the button. If I never confirmed, it never expired.* The one action that was supposed to grant access was the exact thing that killed it.

**Wall two: an account that didn't exist.** My ELESION login — correct, straight out of my iCloud Keychain — simply didn't work in Tuya's own app. Same email, same password, "no such person." My account was real; it was just locked in a drawer only the sticker-brand could open.

**Wall three: the region shell game.** Because it's an OEM (sticker-brand) device, it might be locked to a region. Europe splits into two data centers — Central and West — and the free tier lets you have *one project at a time*. So every time I wanted to test whether the *other* region was the problem, I had to **delete the whole project first**. One in, one out, over and over, just to find out which door the device was even behind.

## Rock bottom

Then it got genuinely bad — and it started with a decision I had to make on purpose.

One of these pumps can only be paired to **one app at a time**. To even *attempt* the new approach, I had to first remove it from the app where it already worked. So I burned the one boat I had: I disconnected the pump from the working setup, on faith that I could get it back somewhere better. That's the moment the safety net went away.

And then it wouldn't reconnect at all.

Part of the problem was the hardware itself. The pump has exactly two buttons: one for Wi-Fi, one to water. To factory-reset it, you hold the Wi-Fi button until the light flashes. But the pairing guides all hinge on *how* it flashes — a **fast** blink means the device wants one kind of setup, a **slow** blink means another. But mine only ever blinked at one speed — I held that button a full twenty seconds and it never changed. So I was being asked "fast or slow?" about a device that had only one answer, with no way to change its mind. I stood there with my phone paired to the pump, waiting a full minute for it to be picked up — and nothing. And that was just to claw back to *square one*, before any of the clever stuff.

So I did what everyone does: I updated the ELESION app, hoping a newer version would fix the connection. The update **deleted my device from the setup list entirely** — and iOS won't let you reinstall the old version. I wasn't back to zero. I was *worse* than zero, with a dead pump, wilting tomatoes, and four days until we drove to Austria.

I genuinely thought: *I broke it.*

## The eagle lands

The unlock was almost stupid. Stop fighting the account. Factory-reset the pump, wipe it clean, and re-pair it from scratch into a new Tuya account.

Except re-pairing wasn't the point-and-click it had been years ago. Back then, ELESION let me pick my pump from a list — there it was, by name. Tuya's app had no such entry, so I couldn't tell it *what* I was connecting; I had to add the thing as a generic, nameless "some Wi-Fi and Bluetooth gadget, figure it out" device and hope the pump raised its hand. And going back to ELESION wasn't a fallback either — the app update had already wiped the pump from its list too. Neither app would name my device anymore.

The trick that finally worked: not "irrigation device," which kept failing — plain **"Wi-Fi only."** Fifty seconds later, the pump showed up in an account my code was actually allowed to talk to.

*The eagle has landed.*

I test-fired it. It worked. It worked.

## Wasser an

Here's the part I still grin at. I don't type `water on` in a terminal. I say it out loud:

> **"Wasser an."** — the pump starts.
> **"Wasser aus."** — it stops.

The voice goes to Maestro and Maestro Relay — the same agent setup I use to build software at work. That hands off to the little **water CLI** I built, which is the bridge in the middle. The CLI talks to Tuya's **cloud**, and the cloud reaches the pump on my balcony — which means the command works whether I'm in the next room or in another country. That was the whole point.

The tomatoes survived Austria.

## Flying blind

It worked — but using it in anger taught me the next problem.

From Austria I was conservative at first: a minute of watering at a time. Then I bumped it to two. Then the news said 36, 37°C, record-breaking, and I pushed it to three minutes a run, nervous the whole time about whether I was overdoing it or not doing enough.

Then I got home and looked in the tank. It was only **half empty**. After four days of a heat wave, I hadn't even come close to the bottom. I'd been rationing water I had plenty of — because I had no way to *see* how much was left. I was flying blind the entire time.

So naturally I ended up in a conversation with the AI about fixing that too: point a camera at the tank, add a water-level sensor, or — the cheapest option — measure the pump's flow rate once and just *calculate* the remaining water from the log of how long it's run. The tool taught me what the next tool should be. (That one's not built yet.)

## Tomato maxing

Here's the thing that makes this more than a gadget story.

Code got cheap. Building a little tool like this used to be a weekend you couldn't justify; now it's an evening of procrastination and a conversation. So the leverage stops being about work. The exact same agent stack that ships our company's software also waters my tomatoes, by voice, from a mountain 300 km away.

That's the joke that's also the thesis. When code is this cheap, you don't just automate your job. You automate your garden.

Tomato maxing.
