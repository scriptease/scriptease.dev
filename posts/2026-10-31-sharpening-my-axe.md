---
title: "Sharpening My Axe"
url: "https://scriptease.dev/posts/2026-10-31-sharpening-my-axe/"
author: "Scriptease"
created: "2026-10-31"
published: "2026-10-31T11:54:14+01:00"
description: "For two months I've had my automatic login, and Apple has broken it every chance they got. I've lost count of how many times I rewrote the part that translates the keyboard. Today I decided to give it another go."
tags: ["ai", "agent", "simulator", "keyboard", "opensource", "saga"]
---

# Sharpening My Axe

_The [Login Everywhere saga](https://scriptease.dev/sagas/#login-everywhere): [1. Every Login All at Once](https://scriptease.dev/posts/2026-09-05-every-login-all-at-once/) · [2. Built Over His Lunch Break](https://scriptease.dev/posts/2026-10-06-built-over-his-lunch-break/) · 3. Sharpening My Axe_

For two months I've had my automatic login, and Apple has broken it every chance they got. I've lost count of how many times I rewrote the part that translates the keyboard. Today I decided to give it another go.

## Computer use to the rescue?

The excuse was a video. Theo, a developer whose videos I follow, mentioned cua, an open-source tool that lets an AI use a computer the way a person does: look at the screen, click and type.

He said it "will be in T3 Code very soon". T3 Code is the app I talk to my AIs in.

I wanted to see whether cua could fix my long-term issues with Device Hub, the window on my Mac where Apple keeps all the fake iPhones and iPads I test our app on.

I installed it and gave it a couple of tasks, to see how it could interact with my apps. It did them without touching my mouse.

Then the fake iPad. cua could see our app, every button and its name, and tap one. And Device Hub jumped in front of whatever I was doing.

My verdict: better at using a computer than the last tool I tried, "but it doesn't solve any of the issues that I'm trying to solve with it". It stays in its own little folder.

## "Every little trick just fails because of another reason"

The issue was the keyboard. My Mac is German. The tools my AI typed with assumed an American keyboard. So when my AI typed, the iPad swapped the z and the y, and mistyped the `@` that's in every email address.

In [the first post of this saga](https://scriptease.dev/posts/2026-09-05-every-login-all-at-once/) I worked around it. Before every login my AI flipped a handful of switches until the iPad expected an American keyboard, typed, and flipped them all back so I could still type German myself. Every new version of the iPad's software named those switches differently. It worked. I hated it.

So this morning we tried every shortcut again.

A fake iPad set to English only, so there was nothing German to switch away from. It came back German after the restart anyway.

Translating on the way in: if the iPad expected German, have the AI type y when it meant z. That fixed the letters. The `@` stayed broken.

"But I hope you now understand a little bit my frustration that every little trick just fails because of another reason."

We thought we were out of options. I even considered the last one: switching my own Mac to an American layout. "Sometimes I think maybe I want English keyboard layout on my Mac." But the keys on my MacBook have German letters printed on them, and I can't swap the keyboard. It's attached to the laptop. The AI even suggested a little program that would let me and my AI use the keyboard at the same time.

I switched the layout anyway, and the AI typed correctly. "I mean it would work, but it's also annoying as heck because that would mean that while my AI is running tests, I have to use a different keyboard layout." And even switching the keyboard didn't come without problems. It felt like the wrong fix for my problem.

There was one more way. Normally you type on an iPad with the keyboard on its screen, and my AI could tap that too, letter by letter. But then it had to hunt for every key, tap Shift for capitals and switch to the symbol keys, and that keyboard looked different in every version of the iPad's software. Slow, fragile, and I want to automate the login, and "if a password contains a z y or a apostrophe, then I'm f&%#ed".

## Why don't they just have a way to send the text?

That was my real question to Apple. Why can't a tool just hand the iPad the finished text, instead of pretending to press keys?

My AI explained what was going wrong. The tools I was using sent key presses, not finished text, and how the iPad read those key presses depended on its keyboard.

I queued a research task: are there other tools that handle German keyboards? And I added a note of my own. I had dug into Argent, one of the two tools my AI used to drive the fake iPad. The part that types is closed source: private software that only its makers can change. The other one, I assumed, came the same way: a ready-to-run program, without the recipe for changing it. "It's also closed source and a binary."

## "Why not build it ourselves"

It isn't.

The other tool is axe, and it's open source. My AI looked inside: axe knew which key to press for every character from one list, and that list was American. One list. Add a German one next to it.

"But thanks, this looks actually as a feasible way if I basically instead of complaining about not having a way to send a string layout independent to the simulator, why not build it ourselves, right?"

The AI built its own axe, added the German list, and typed every special character a German keyboard has into the fake iPad. No switches flipped.

Two of them came out wrong. Apple's German keyboards have two keys that trade places with each other. One more line in the list, and the next run came through exactly as sent. Letters, German umlauts, `@`, apostrophes, the lot.

## Splitting hairs

Then I wanted to break it. I switched my Mac to American again. axe didn't care. It only listens to the iPad's keyboard.

Then I remembered seeing keyboards on the iPad that are German and English at once. The AI found where to add one and tried to switch to it. Its tap missed, and the next one opened the wrong menu. "Oh, you tested the wrong one." I switched it by hand: this mixed keyboard needed the American list.

Which list was right depended only on which keyboard the iPad had active, and the iPad wrote that down. So the AI taught axe to read it before typing and pick the list itself, and to refuse to type at all on a keyboard it doesn't know. Typing the wrong characters into a password field is worse than failing.

I switched between the mixed keyboard and the German one. axe picked the right list both times.

## What Apple should fix

Two months of workarounds, and the fix was inside a tool I had used every day without ever opening it. From "yes, let's try it" to the first clean German run took a couple of minutes.

The research I had queued arrived while we were on the final steps. Every tool that types into the fake iPad by pressing keys carries the same American list, and nobody had even filed a bug about it. Nobody in the world supported my German keyboard.

The one alternative was a tool that piggybacks on Apple's testing framework, the one developers use to test their own apps. That sounds official. It isn't. It's a hack, not a way Apple supports, so it broke with every beta of Apple's tools. When I tried it, setting it up took more than half an hour, and then it barely worked. Two weeks later I tried again, and it was broken again.

The only way to fix it was to fix it myself.

So now I have another working prototype. This time it's my own axe, 38 megabytes. For it to help anyone but me, every developer at our company would need my version of axe instead of the one that comes with their tools. Or the maker of axe takes the change. I already [filed it and suggested the fix](https://github.com/cameroncooke/AXe/issues/81).

All to fix something Apple should have fixed in the first place.
