---
title: "Tomato Maxing III — Only Six Percent Left"
url: "https://scriptease.dev/posts/2026-07-15-tomato-maxing-iii/"
author: "Scriptease"
created: "2026-07-15"
published: "2026-07-17T19:03:41+02:00"
description: "My phone buzzed with a warning: 6% left. Six percent of what? I didn't know I was spending anything — and when I went looking, the thing draining it wasn't my tomatoes. It was the robot vacuum, fast asleep in its dock."
tags: ["gardening", "automation", "performance", "ai", "saga"]
---

# Tomato Maxing III — Only Six Percent Left

_The [Tomato Maxing saga](https://scriptease.dev/sagas/#tomato-maxing): [1. Tomato Maxing](https://scriptease.dev/posts/2026-07-05-tomato-maxing/) · [2. The Pump Talks Back](https://scriptease.dev/posts/2026-07-11-tomato-maxing-ii/) · 3. Only Six Percent Left_

My phone buzzed with a warning: **6% left.** Six percent of *what?* I didn't know I was spending anything — and when I went looking, the thing draining it wasn't my tomatoes. It was the robot vacuum, fast asleep in its dock.

## The setup, for anyone just tuning in

Two summers of this on-and-off saga have been about one silly project: keeping tomatoes alive on a windy ninth-floor balcony while I'm not there to fuss over them.

I water them by typing. There's a little command I wrote — I called it `water` — that talks to a €30 WiFi pump sitting in a 35-litre bucket. And last time, I moved the whole contraption into Apple's **Home app** — the built-in iPhone screen where your lights and locks live — using a free translator program called **Homebridge**. Homebridge sits on my Mac and tells the iPhone, in effect, "trust me, this bucket pump is a real smart-home device." While I was in there, I taught it about my **robot vacuum** too — a Lefant M310, one of those hockey-puck floor cleaners.

Two gadgets, one translator, both answering to Siri. I was pleased with myself.

That's the setup. Here's what I was actually doing the evening it bit me.

## The rule I couldn't build

I hadn't opened all this back up for nothing. I wanted the pump to react to the *weather itself* — water hard when the air's hot and dry, ease off when it's cool and damp — without me deciding anything from another country.

And it looked easy, because the iPhone can already build "when this, then that" rules by tapping — no code at all. Apple even hands you the right trigger out of the box: *when the room gets warmer than X,* or the air drier than some level. The sensor's already sitting there. All I had to say was: when it dries out, water the tomatoes.

Except you can't. And the reason turned out to be a wall I didn't see coming.

Those tap-to-build rules can only ever **pull a trigger once.** They fire the *instant* a line is crossed — the temperature ticks past 30° — and then they're finished. What they cannot do is *hold a thought*: "for as long as the air stays dry, keep watering every few hours." There is no "while." It's a doorbell, not a thermostat — it can ring the moment someone shows up, but it can't sit there minding a condition all afternoon.

And watering isn't a single ring anyway. It's "run for two minutes, then stop." To even *offer* the pump to one of these rules, I'd had to dress it up as a plain on/off switch — and a one-shot pulse flipping a switch has no idea how to run a timed cycle, let alone when to shut itself off. So I built the switch, poked at it for an evening, and gave up. The one thing I actually wanted — a garden that waters itself by *feel* — the friendly no-code tool flatly refuses to do.

I closed the laptop annoyed. That should have been the whole story of the evening.

Then my phone buzzed.

## Six percent of what?

The warning came from **Tuya** — the Chinese company that builds the electronic guts inside thousands of no-name smart gadgets, including both of mine. "ELESION," "Lefant" — those are just stickers on the box; underneath, both devices speak Tuya.

Tuya gives you a free monthly allowance of what it calls **API calls** — think of them as little messages my code sends over the internet to reach the devices. Turn the pump on: one message. Ask if it's running: one message. I had apparently used 94% of the month's ration, and it was only the 15th.

So I checked what the previous months looked like. About **fifty** messages each. Fifty. This month: over **forty thousand**.

Fifty to forty thousand. Something had turned a trickle into a firehose, and I hadn't touched a thing.

## The usage page that made no sense

The breakdown Tuya showed me was, frankly, unhinged. My messages were filed under categories like *"Standard Version for Hotel," "Premium Version for Hotel,"* and — my favourite — *"Commercial version of smart door lock open capability."* I don't run a hotel. I have never owned a smart door lock. And every one of those lines showed the *same* number: 22,242.

My first, slightly cold thought: *is someone else on my account? Is there a hotel somewhere spending my tomatoes' allowance?*

No. It's just Tuya's accounting being Tuya's accounting. A single real message gets counted six times over, once under each product bucket it technically belongs to — hotel edition, door-lock edition, and so on. Six labels, one underlying stream. Strip the double-counting and the honest number was about **22,000 calls**, all mine, all from my own two gadgets. The tell was that every bucket moved in perfect lockstep — a hotel guest would have made the numbers drift apart. Nothing had broken in; my own code was the whole story.

Which left the real question: 22,000 messages for two gadgets I barely touch — *how?*

## The thing that never sleeps, and the thing that always does

Here's the mechanism, because it's the whole trick.

My code always tries the polite route first: reach the gadget over my home WiFi — fast, free, entirely inside my flat. Only if it can't find the device at home does it **fall back** to the internet, the slow route that Tuya counts. So the question narrowed to: which gadget kept vanishing from my own network, forcing my code to go the long, metered way around?

The pump was innocent. It's plugged into the wall, always on, always listening. When my code knocks, it answers instantly, at home, for free.

The vacuum was the culprit — and the reason is almost funny. A robot vacuum spends about 99% of its life asleep in its dock, charging. And a sleeping vacuum, to save power, **stops listening on the WiFi.** So every time my setup quietly asked, "hey, are you cleaning right now?", the docked robot didn't answer at home — and my code, hearing silence, assumed it must be *away*, and shouted the exact same question across the internet instead. That's the metered path. And it was doing this every thirty seconds, all day, all night — including while I sat ten feet away from the sleeping robot on my own sofa.

The gadget I was watching was fine. The gadget I'd forgotten about was running up the bill, and the very thing that made it expensive was that it was *asleep*.

There was one extra sting, and it points right back at the last chapter. The reason my code was asking questions so obsessively in the first place was the **countdown** I bragged about in Part II — the little "120, 119, 118…" ticking down on my phone while the pump waters. To keep a number like that alive on screen, something has to keep asking "how much time is left?" many times a minute. The feature I was proudest of last time was quietly part of the problem this time.

## Teach it to whisper

The fix was almost embarrassingly small.

I told the automatic questions to use the **home route only** — never fall back to the internet. If the vacuum's asleep and doesn't answer at home, fine: assume it's off (it is), and move on. Don't phone the cloud to double-check something you can already guess. Then I slowed the questions down for good measure — from every few seconds to once a minute.

But I kept one door open on purpose. There's a difference between my code *quietly checking* on a gadget and me *deliberately telling* one to do something. The constant background checks now stay local and silent. But if I sit on a mountain in Austria and type "water the tomatoes," *that* command is still allowed out onto the internet to reach the balcony — because that was the whole point of this project in the first place. Listening is free and local; acting can still cross a border. It just can't happen 40,000 times behind my back.

The meter stopped climbing that same afternoon.

## What it actually cost me

The bill was never money — it's a free tier. The worst that happens if you blow through it is the gadgets go quiet until the month resets, and my tomatoes miss a drink. Annoying, not expensive.

What it actually cost was an assumption: that "smart" is free and quiet. That once you've built the clever thing, it just sits there being clever at no charge. It doesn't. Every convenience you wire up runs a little meter somewhere, and most of the time you never see it — until a notification tells you you're at 6% and you realise you've been paying, in some currency, the whole time.

And the thing burning it is almost never the thing you're looking at. I spent two summers watching the pump. The one quietly screaming into the internet was the vacuum, asleep in the corner, doing what I thought was nothing.

## Tomato maxing

Part one's lesson was that code got cheap enough to automate your garden. Part two's was that the *second* gadget is nearly free, once you've built the translator in the middle.

Part three is the bill for all of it — not a big bill, but a real one. Every gadget you add is another quiet mouth pointed at a meter you'd forgotten you had. The skill was never adding them. It's noticing what they get up to when you're not watching.

Tomato maxing.
