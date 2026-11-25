---
title: "Tomato Maxing II — The Pump Talks Back"
url: "https://scriptease.dev/posts/2026-07-11-tomato-maxing-ii/"
author: "Scriptease"
created: "2026-07-11"
published: "2026-07-11T23:15:23+02:00"
description: "Last time, I could water my tomatoes by voice from another country. What I couldn't do was watch it happen. This is the part where the pump started talking back."
tags: ["gardening", "automation", "commandline", "ai", "saga"]
---

# Tomato Maxing II — The Pump Talks Back

_The [Tomato Maxing saga](https://scriptease.dev/sagas/#tomato-maxing): [1. Tomato Maxing](https://scriptease.dev/posts/2026-07-05-tomato-maxing/) · 2. The Pump Talks Back · [3. Only Six Percent Left](https://scriptease.dev/posts/2026-07-15-tomato-maxing-iii/)_

Last time, I could water my tomatoes by voice from another country. What I couldn't do was *watch* it happen. This is the part where the pump started talking back.

If you missed part one: I have a €30 WiFi pump keeping tomatoes alive on my balcony, and after a week-long fight I got it under my control so I could water them from a mountain in Austria — out loud, by voice.

But that voice control ran through my own plumbing. The words went to Maestro, the same agent setup I use to build software at work, which handed off to a little tool I wrote. It worked, but it lived in *my* workshop. My iPhone knew nothing about it. Ask Siri to water the tomatoes and she'd shrug. And I still couldn't see a thing while it ran — I was pouring water into a bucket I couldn't watch.

I wanted it in the front door of the house, not the workshop out back. I wanted it in Apple's **Home app** — the built-in iPhone screen where your lights and locks live — so Siri knew it existed and so I got a real button with a real readout.

## The translator

The problem: Apple's Home only trusts a short list of blessed brands, and a no-name Chinese bucket pump is not on it.

The way around it is a small free program called **Homebridge** — think of it as a translator that sits on my Mac, speaks fluent gadget on one side and fluent Apple on the other, and quietly tells the iPhone "trust me, this thing is a real smart-home device." You teach it, once, how to flip your gadget on and off, and the gadget shows up in Home as if Apple had blessed it all along.

So I taught it about the pump. And that's when the story got cheap in the best way.

## The second one was free

While I was in there, I realised my **robot vacuum** — a Lefant M310, one of those hockey-puck floor cleaners — was *also* one of these no-name Chinese devices under the hood. Same guts as the pump, different sticker.

And here's what made me laugh out loud. Remember the wall that cost me a week in part one? The one move I could never pull off was **linking my pump's account to the developer platform** — the app simply refused, which is why I'd had to burn the whole setup down and re-pair from scratch. For the vacuum, that exact move — the impossible one — *just worked*. I linked the account, and the robot was there. No factory reset, no lying QR code, no fight. The thing I'd bled for in part one was free the second time.

Then came the fun part. A vacuum doesn't have a simple on/off — it *drives*. So the AI I build with rigged up a little calibration game: it watched the robot's internal log while I picked up the physical remote and pressed each button in turn — forward, back, left, right, go-home, start, stop. Every press showed up in the log; the AI matched each button to the secret code the robot spoke and wrote down the phrasebook. A dozen button-presses, and my computer had learned to drive the vacuum.

The best bit: I did the whole thing sitting at my desk. Never touched the robot once — which held right up until I told it to move for the first time. It reversed straight out of its dock, backed onto a folding clothes-drying rack, and beached itself, wheels spinning in the air. So the one and only time I laid a finger on that machine all evening was to walk over and lift my brand-new, remote-controlled robot off a laundry rack it had impaled itself on.

Now the vacuum answers to Siri too. Two devices, one translator — and the account trick I'd bled for in part one quietly paid for itself twice.

## Apple built me a sprinkler

Here's the detail I grinned at.

When you add something to Apple's Home, you have to tell it *what kind* of thing it is — a light, a lock, a fan. And it turns out one of the built-in kinds is a **sprinkler system**. A proper one: the sort a landscaper installs in a lawn, with a set watering time and a countdown while it runs. Apple built that mode for people with gardens and irrigation contractors.

I pointed it at my €30 bucket.

And it fit *perfectly* — because a bucket pump on a timer and a lawn sprinkler are, secretly, the same machine: turn on, run for N seconds, turn off. So my balcony hack inherited a polished interface Apple had designed for a completely different, much fancier world. Set a duration, press the drop, and — in theory — watch it count itself down to zero.

In theory.

## I blamed the machine. It was me.

Here's the thing: I didn't even know that countdown was supposed to be *real*.

When I first wired the pump into Home, I assumed I'd built a dumb switch. Flip it on, the pump runs; flip it off, the pump stops — and *I* was the one who had to flip it off. A light switch that happened to move water. That was my whole mental model.

But that's not what the sprinkler mode does. You switch it on and it runs *itself*: it watches the clock, shows you the seconds ticking down, and shuts the pump off on its own when the timer hits zero. Hands-free. I had no idea any of that was even on the table.

All I knew was that my version was subtly broken. The button on my phone and the actual pump were never in sync — the app's idea of "on" drifted from what the pump was really doing, and it certainly never counted anything down. I chalked it up to the obvious: it's a €30 bucket pump wearing a borrowed costume, of course the fancy parts don't fully work. That's the ceiling for a bootleg. A technical wall — and part one had trained me to expect walls.

It was not a wall. Today I had the AI take a fresh look, and the verdict was almost insulting: the countdown had been built and working the entire time. The auto-stop, the live seconds, all of it. Nothing was missing — except a single letter in one line of my own code.

My code asked the pump "are you running?" and checked the answer against the word **"on."** The pump was answering **"ON,"** in capitals. And the one character that would have told my check to *ignore capital letters* — a lone `i`, the little flag you tack onto that kind of text-match — was missing. So my code stared at "ON," failed to recognise its own lowercase "on," and concluded the pump was off. A pump that's "off" has nothing to count down.

The entire bug was one absent letter. And of all the letters it could have been, the one missing from a fix that was *entirely about capital letters* — was `i`.

One character added. The pump lit up as running, and the seconds finally started to fall.

## The payoff

Now I press the water drop on my phone and a number counts down in front of me — 120, 119, 118 — while the pump does its thing on the balcony. It's not the *whole* of the "flying blind" problem I ended part one with — I still can't see how much water is left in the tank. But for the first time I can watch the thing *work*. The bucket finally tells me something back.

Siri waters the tomatoes. Siri sends the vacuum out and calls it home. Both of them show up in the same app as everyone's smart bulbs, behaving like they belong there — which, functionally, they now do.

## The next thread

And of course, one discovery pointed straight at the next one.

Poking around the Home app, I noticed something I'd walked past for months: my **HomePod** — Apple's little smart speaker sitting in the room — has a thermometer and a humidity sensor built right into it. The temperature and how damp the air is, quietly measured and shown in the app the whole time.

My first thought, naturally: *can my watering code read that number?* If the pump knew it was 35°C, it could water hard on a scorching day and ease off on a cool one — no forecasts, no guessing, just react to the real heat.

The catch: Apple keeps that sensor locked in the box. You can *see* the reading; there's no door to pull it out to my own code. It's a walled garden with a lovely window and no handle.

But there may be a way in that needs no code at all. The iPhone has its own built-in **automations** — "when this, then that" rules you set up by tapping, no programming — and one of the available triggers is *"when the HomePod's temperature rises above X."* So the idea I'm circling: wire the HomePod's own thermometer straight to the pump, entirely inside the phone. Room crosses a heat threshold, the tomatoes get a drink; mild day, they don't.

Yes, it's the *indoor* reading, not the balcony. But in summer my windows are open all day, so the room is really just the outside temperature in the shade — close enough to trigger on, and the humidity reading comes along for free. It doesn't make the idea any smaller.

Not built yet — same as the water-level sensor I dreamed up at the end of part one. But that's the pattern, isn't it: every tool I finish hands me the blueprint for the next.

## Tomato maxing, again

The lesson from part one was that code got cheap enough to automate your garden. Part two adds the sequel to that: the *second* thing is cheaper than the first, and the third is nearly free — because the hard part was never the pump or the vacuum. It was building the translator in the middle. Once that exists, every new gadget is a couple of lines and an afternoon.

You don't automate one thing. You build the thing that automates things. Then you go looking for what else in the apartment secretly speaks the same language.

Tomato maxing.
