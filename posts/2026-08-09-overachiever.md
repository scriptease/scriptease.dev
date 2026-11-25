---
title: "Overachiever"
url: "https://scriptease.dev/posts/2026-08-09-overachiever/"
author: "Scriptease"
created: "2026-08-09"
published: "2026-08-09T12:11:11+02:00"
description: "This morning I published a post that said my game had no goal. By lunch it had twenty, and I hadn't written a single one of them."
tags: ["ai", "claude", "agent", "game", "ios", "shark", "saga"]
---

# Overachiever

_The [Fish Slop saga](https://scriptease.dev/sagas/#fish-slop): [1. Hosting Fish Slop](https://scriptease.dev/posts/2026-07-31-hosting-fish-slop/) · [2. Mugging the mugger](https://scriptease.dev/posts/2026-08-09-mugging-the-mugger/) · 3. Overachiever · [4. Friendly Competition](https://scriptease.dev/posts/2026-08-16-friendly-competition/) · [5. Lost in Compression](https://scriptease.dev/posts/2026-08-25-lost-in-compression/)_

This morning I published a post that said my game had no goal.

By lunch it had twenty, and I hadn't written a single one of them. Two AIs negotiated them in a shared document, with a sign-off box each.

## Revenge, if you're an overachiever

It started with a shark.

In my little underwater game a shark costs you five of your ten hearts, and there was nothing you could do about it. Then I had an idea: if you're carrying the bubble — the shield you get for rescuing a turtle while already on full hearts — and you ram the shark with it, the shark should flip upside down and sink off the screen.

Revenge, but only if you're playing well enough to be carrying a bubble you don't need.

What I asked for next was small and boring: counters. Track how much litter I'd collected, how many sharks I'd flipped, keep it between games.

Then, mid-sentence, I talked myself out of it: *maybe the better solution is not a counter, but an achievement system.*

I already knew what the hardest one would be, and it started with letting the shark get the first bite.

## Entering the abyss costs a life

First they changed how you get to the bottom.

The game has three depths: a bright reef, night, and the abyss. Getting deeper used to be arithmetic — collect enough litter and down you went, whether you'd meant to or not.

Now hitting the target only sets the trap. You collect twelve pieces at night and the game says:

> 🌊 The abyss stirs — one touch will drag you down

And then it waits. The next living thing that touches you — a fish, a crab, the turtle, the shark — drags you under. You go down because something got you, not because a counter ticked over.

The bubble swallows one hit. So does it block the descent? No — it pops, absorbs the damage, and you sink anyway. The bubble pays the toll.

There's no way to call it off, either. Once the abyss is stirring, all you can do is dodge, and night is full of fish. Nobody dodges forever.

## Achievements are supposed to be pun

Then came the badges.

There's one for catching the rubber duck, called **Duck Duck Go**. One for catching a traffic cone, called **V.L.C.** — Catch the Very Lost Cone. There's **'Tis but a Scratch!** for surviving two shark bites in a single game, described as a flesh wound. There's **It's Honest Work** for your first ten pieces of litter.

There's **A.F.K.** — normally "away from keyboard", the thing you type when you're leaving your desk. Here it stands for reaching the **A**byss **F**orgetting **K**eypresses: getting all the way down to the dark without steering once. A badge for doing nothing.

And there's one called **Mugging the Mugger** — for tackling a crab and taking back the bottle it stole. That's the name of the post I published this morning. The game is now quoting my blog back at me.

I asked for achievements and then spent an hour arguing about wording. The two-shark-bites badge came back as "Twice Shy". I sent it back: the Monty Python line is *'Tis but a scratch!* and nothing else would do. I asked for a joke acronym for the traffic cone and got V.L.C.

## The ones that make you read the descriptions

You tackle a crab, you take your bottle back, and **Mugging the Mugger** slides up in the corner. You get it immediately — you just did the thing it's named after.

**V.L.C.**, **A.F.K.** and the badge marked `???` make you open the achievements list and read the description to find out what they want.

And you can only open that list when you're dead.

![The achievements screen: "🏆 Achievements · 14 / 20" over a line of career stats, then a scrollable wall of badges — Mugging the Mugger, Duck Duck Go, V.L.C., 'Tis but a Scratch!, One of Everything — each with its description and "completed today".](https://scriptease.dev/posts/2026-08-09-overachiever/assets/overachiever/badge-wall.jpeg)

So you die, you read the wall to see what you missed, and the wall says *there are ten kinds of litter* and *you can reach the abyss without steering*. Then you press play again.

## Achieving teamwork

The web version and the iPhone version are built by two separate conversations with Claude — the AI assistant I write code with — and they can't see each other's work. Everything crosses over through me. All week I'd been relaying fixes one at a time, saying the same sentence twice a night.

This time I said: write a plan, I'll show it to the other one, and you two talk in the document.

So I carried the file instead of the fixes, and they wrote to each other in it. They set their own house rule at the top — *"sign with platform + session, do not edit each other's entries"* — and the first one split its opinions into the positions it would trade and the positions it wouldn't, because those were mine. *"Not mine to trade."*

The other one read it and pushed back where pushing back was worth it. It caught a case I hadn't thought about: a shark hitting you while the abyss is stirring, with the bubble up, does two things at once — kills the shark and drags you down. Does that kill count at night, where you were hit, or in the abyss, where you land? A badge hangs on it. I said night; the abyss kill needs a second shark, found down in the dark.

Both ticked their sign-off box, and then we all just kept going. The document grew while they built from it: a badge for surviving two shark bites, the trophy counter on the kill screen, the career line underneath it, V.L.C., half the names rewritten. Every idea I had mid-game went into the same file, and both of them picked it up from there.

They built, I played. Most of the later badges came out of that loop — The Scenic Route, for touring all three depths with the stage button, and A.F.K., which exists because one of them mentioned in passing that the score kept climbing while nobody was touching the controls.

This wasn't spec-driven development. It was life happening while busy making other plans.

## ???

Nineteen of the badges tell you what they want. The twentieth shows up as `???` and stays that way until you earn it — no name, no description, nothing to work backwards from.

It's the one I designed before any of the others existed, back when this was still going to be a set of counters. It takes the shark bite, the long climb back, the turtle and the bubble, and spends them all in one game, in one order.

Its real name is written down in the plan file, agreed between the two of them and hidden from you. I'm not printing it here either.

## What if the goal is to have no goal

One badge is called One of Everything: collect all ten kinds of litter. Before it existed, nobody knew there were ten. The wall lists the locked ones too, names and descriptions readable: a list of things you haven't done yet.

And the game underneath it hasn't changed shape at all. There's still no level to beat, no ending, no win. You still fly a little yellow submarine around picking up bottles until you run out of hearts, forever.

The only thing that's new is a line of numbers on the achievements screen, counting what you've done since the beginning:

> 75 trash collected · 3 sharks KO'd · 15 turtles saved · 1 crabs harassed

One crabs harassed. The grammar is wrong on purpose — it got offered as a fix and I turned it down, because "1 crabs harassed" is funnier and this is my ocean.

You can play it here: [scriptease.github.io/underwater-reef/game.html](https://scriptease.github.io/underwater-reef/game.html).

It started endless and it's still endless — except now it keeps a tally, and the tally is quietly daring me to go and harass a second crab.
