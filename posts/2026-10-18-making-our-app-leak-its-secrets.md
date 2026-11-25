---
title: "Making Our App Leak Its Secrets"
url: "https://scriptease.dev/posts/2026-10-18-making-our-app-leak-its-secrets/"
author: "Scriptease"
created: "2026-10-18"
published: "2026-10-18T21:30:05+02:00"
description: "Every bug has two suspects: the app and the server. Normally I only interrogate the server, because the app won't talk. Today I made it talk, and halfway through my AI got stopped for cyber misconduct."
tags: ["ai", "agent", "commandline", "skills", "ios", "debugging", "saga"]
---

# Making Our App Leak Its Secrets

_The [AXI saga](https://scriptease.dev/sagas/#axi): [1. The Checklist I'd Been Following](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/) · [2. AXI All the Things](https://scriptease.dev/posts/2026-09-26-axi-all-the-things/) · [3. Not My First Rodeo](https://scriptease.dev/posts/2026-10-07-not-my-first-rodeo/) · [4. Back in AXIon](https://scriptease.dev/posts/2026-10-09-back-in-axion/) · [5. Anticipation](https://scriptease.dev/posts/2026-10-09-anticipation/) · 6. Making Our App Leak Its Secrets_

Every bug has two suspects: the app and the server. Normally I only interrogate the server, because the app won't talk. Today I made it talk, and halfway through my AI got stopped for cyber misconduct.

## The usual suspects

Our iPad apps talk to a server, the computer behind the app. When something goes wrong, the first question is always the same: which of the two is the culprit? If I know that, the problem is already halfway solved.

My colleagues answer it with Proxyman, a program on the Mac that sits between the app and the server and shows every message passing by. A wiretap. It has one catch: it has to be running before the bug happens.

I answer it from the other end. The server keeps records of everything the app ever sent it, and I ask its database. That works afterwards, which is exactly what a reported bug needs: a customer sends a screenshot, I find the receipt. My AI has [a command for this](https://scriptease.dev/posts/2026-08-02-connecting-50-databases-to-an-ai/) and asks the database itself.

Before, and after. Nobody could ask during. While the app sits on a screen in a strange state, an order half built, a payment running, the one thing holding the answer is the app, and it has no way to say anything. My AI drives the fake iPad on my Mac [through Argent](https://scriptease.dev/posts/2026-10-09-back-in-axion/), its remote control, and reads the screen the way a screen reader for the blind does: the labels on things, not the data behind them.

I had everything connected: the database, the bug tickets, the work chat, the fake iPad. The app itself was silent.

## "wouldn't it be easier if the app reveals its secrets?"

On a Sunday morning my [YouTube watcher](https://scriptease.dev/posts/2026-10-04-on-the-shoulders-of-giants/) had filed a talk from the AI Engineer conference in New York: "Teach Your Agent to Prove It's Done", by two engineers at WorkOS, a company that sells logins. Their demo bug: a sign-up form says success, you reload the page, and nothing was saved. An AI that only looks at the screen reports the job done. Their rule, trust the records over the AI's say-so: "status comes from records, not model prose." Their advice: let the AI see everything you would see.

I was watching it, and then I saw it. I could only debug this way because I had the server's receipts. Wouldn't it be easier if the app reveals its secrets? Without going through the server.

## Well hidden secrets

My first sentence to the AI was the complaint: it "can only read the accessibility labels and not the actual data behind it". I wanted the order the cart screen was showing, the customers a search had loaded, the state of a payment while it runs.

The AI went reading and found that the app already shares secrets with humans who know the knock. Four taps here, two taps there. Gestures hidden in plain sight.

Only on the fake iPad, never on a real one: "I don't want to expose this data to the outside."

Two views: one for the whole app, one for the current screen, whatever it is holding right now. Some objects, the order, the customer, the store and the user, come out in the exact format the app uses to send them to the server, "because I want to be able to compare these objects with the server state".

Everything else is plain text. "I'm fine with debug output that I can read." And a two-line summary per thing, with details on request, "so that we have progressive discovery": the AI skims first and digs only where it needs to.

The app already had a side door, built for its forms. The secrets went behind it, under a new address: /expose. "I also came up with a nice name for this kind of feature."

It's now in the foundation under all our iPad apps, so every app on top of it has it.

## Secrets and safety

The AI was trying to install the app on the fake iPad. Mid-sentence, it stopped.

"Your response above was stopped by a safety classifier. This is not a tool or API error. The rest of it was withheld." Category: cyber. "This request triggered restrictions on violative cyber content."

A feature named expose, whose whole job is to leak, and an alarm had tripped. The app was ours. The secrets were ours. The only one they were leaking to was me.

The AI carried on and didn't even mention it.

## Secret delivery service

A side door like that has a door number, a port, and the system hands out a different one every launch. A human never needed to know, but the AI needs it for a secret handshake.

So the app puts the door number on the screen: a one-pixel square, invisible to anyone looking.

But it carries a label, and labels are the one thing my AI reads.

## The confession

"Everything works as designed."

No wiretap running, no database open, no server asked. Just the app, answering for itself.

Two different apps, one foundation underneath, so both had the feature without a line of their own. In the first, the AI opened the flip-flops category and asked the screen. Back came the product with all its variants. In the second it asked the whole app: the customer's shopping in progress, four carts, the postcode data behind the shipping screen, the logged-in store. The parts each app adds of its own showed up too, nothing extra to do.

Then the AI had one warning. The user record carries a fingerprint of the PIN, the same one the app uploads to the server. "Simulator only, but do not paste it into tickets."

The app leaks its secrets. That was the point.

## Before, after and in the middle

That evening the AI filed the ticket and sent both changes for review: the app side, and the command that reads it, an [AXI](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/), a command written for an AI reader.

The talk had one more rule: keep receipts. Whenever an AI checks something, let it leave a screenshot and a record behind, because a pile of those is worth something later. Screenshots my AI already took. Now it has an AXI for the other half: the app's own account of what it held, in the server's words, filed next to the screenshot.

Three ways to look now. Proxyman, before. The server's receipts, after. And the app itself, in the middle of it.

The browser app is next. Maybe.

If there are multiple suspects, I make them talk.
