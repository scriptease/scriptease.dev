---
title: "Every Login All at Once"
url: "https://scriptease.dev/posts/2026-09-05-every-login-all-at-once/"
author: "Scriptease"
created: "2026-09-10"
published: "2026-09-10T09:26:43+02:00"
description: "Most of Saturday went into one wrong assumption. The AI and I blamed the iOS 27 beta for eating keystrokes. The real culprit was a stuck process on my Mac, and I literally had to kill it twice because it refused to die."
tags: ["ai", "agent", "ios", "simulator", "password", "saga"]
---

# Every Login All at Once

_The [Login Everywhere saga](https://scriptease.dev/sagas/#login-everywhere): 1. Every Login All at Once · [2. Built Over His Lunch Break](https://scriptease.dev/posts/2026-10-06-built-over-his-lunch-break/) · [3. Sharpening My Axe](https://scriptease.dev/posts/2026-10-31-sharpening-my-axe/)_

Most of Saturday went into one wrong assumption. The AI and I blamed the iOS 27 beta for eating keystrokes. The real culprit was a stuck process on my Mac, and I literally had to kill it twice because it refused to die.

## Continue three times, select login, continue twice, enter code, continue again

Logging into the app I work on is not one step. The app ships in several variants, and they log in three different ways. The simplest is a list of users and a PIN pad. The second goes through Keycloak, a service that first asks you to pick how you want to sign in, then hands you on. The third is Microsoft's corporate login: an email form that bounces you through two more pages and ends at a six-digit code from an authenticator app. All of that before you are in our app.

Once you are in, you stay in. The problem is not repetition. We have many customers and multiple servers and each has its own flow, its own username, its own password. Remembering which combination opens which app is always a hassle. And in the age of AI I want to hand the app to an AI: set it up, drive it, run its own tests. It can't do anything stuck on a login screen. I want to give my fingerprint once and have the AI run every variant we ship.

A single sign-on for all of them wouldn't work. The login token has to come from the identity systems behind Keycloak and Microsoft, not from us. There is no way around it: every login has to walk the same path a human walks.

So the plan was a script that looks at the screen, decides which of the login pages it is on, and acts, instead of replaying a fixed list of taps. The knowledge of how to log in lives in code. The passwords live in 1Password.

## Sharing secrets without spilling secrets

That last part had a history.

1Password protects everything behind a fingerprint. If my scripts talk to it, it can pass a password straight to the program that needs it, sealed, behind the script's back. I knew that. My problem was discovery. Before you can fetch a password you have to find the right one, and the search costs a fingerprint too. The two prompts look exactly the same.

Two prompts in a row, and I could not tell whether that was "search, then password" or "search, then search again because the first came back empty". Add an AI to the loop and every wrong guess is another prompt. I was pressing the sensor three times in a row with no idea what each press did.

A while back I sat down with an AI and designed a way out. The insight was that the *address* of a secret is not a secret. Which vault, which saved login inside it, which box on that login: writing that down reveals nothing. So: search once, deliberately, and keep the addresses in a catalog. From then on every fingerprint during work means exactly one saved login, known in advance.

The whole design hung on one question: does 1Password ask once per program, or once per address? I built a proof of concept with two test entries and ran it. "It only showed one confirm."

I wrote a README, committed it, and let it sit.

## Automating something you shouldn't automate

A login script needed credentials. A script that types passwords into login forms is frowned upon, for good reason, and it is a necessary evil here: the screens are the only way in, and an AI that cannot get past them cannot test anything. I said "I want to use a mechanism like the one I had", and the proof of concept got its first job.

The PIN login came together on Friday afternoon. I test the app in the iOS simulator, a fake iPad running on my Mac. The script reads the simulator's screen through a tool called Argent, over the same channel a screen reader uses, finds the user row, taps the digits, and lands on the home screen. All in one fell swoop.

One detail I wanted: the row for each user carries that user's login name as its accessibility label, the hidden name a screen reader would read out. The same name is the username in 1Password, so the screen and the vault agree on who is logging in and the script picks the right one.

By evening it had an interactive mode. Run it with no arguments, it lists the running simulators, you type a number, you pick login or logout. Usable without an AI.

## Everything I tried made it worse

The web flow worked once. Chooser, email, password, six-digit code, home. Thirty seconds.

Then the email field got the `@` sign as a `"`. Then it typed spaces. Then, on the next run, `tytytyty`. Then `hhzzzz`. Then `zu zuzu zu`.

Argent types by pretending to be the hardware keyboard, and it sends key *positions*, not letters, assuming a US layout. My Mac is German. On a German keyboard the key in the Y position is Z, and the key that gives `@` on a US layout gives `"`. iOS kept reading the US positions as German keys. The password had a lowercase y in it, and y sits in a different place on the two keyboards.

The fix seemed simple: switch the on-screen keyboard to English before typing. Except while a hardware keyboard is connected, iOS hides the on-screen keyboard, and with it the globe key you switch layouts with. The one control we needed was behind the one thing we were doing.

I got annoyed with the simulator constantly flipping to English, deleted the English keyboard, and recreated it. Badly. From then on the keyboard rendered as a half-screen bar whose buttons were not where the screen said they were.

Then I updated Argent, and it had renamed a parameter with the opposite meaning.

By now nothing worked, not even the parts that had worked in the morning. "Can you revert the changes before we dealt with the keyboard? Now everything is broken and I want to check in a solution that at least somewhat works." We rolled back to the last commit that had logged in.

## "Really interesting, it tried not to get killed"

Saturday morning I had a theory. I had two Xcodes installed, the release and the iOS 27 beta, and the command line was pointing at the wrong one. Half right, the AI said after testing: taps worked on both simulated iOS versions, but typing only reached the iOS 26.5 iPad. Verdict: the iOS 27 simulator drops keystrokes.

We built on that verdict for hours. Trying again, taking other routes, and a rule that refused to type a password unless the layout switch had been confirmed, so a third wrong attempt could not lock the test account.

Then typing died on the 26.5 iPad too.

The thing that had actually broken was CoreSimulatorService, the switchboard between the fake iPad and the Mac. Every fake keystroke and every tap on a system dialog goes through it, and it was stuck. I killed it. It came back. I killed it again, harder.

Fresh boot, and typing worked again. On both iOS versions. The verdict had been wrong all day.

Three more things had to hold before the script was robust. The keyboard named "Deutsch u. English" is German too, so only a keyboard whose name starts with "English" counts. On iOS 27 the globe key cycles through the Emoji keyboard, where the globe stops being a globe, so the script keeps cycling until it sees English. And the beta's new simulator window has no switch to disconnect the hardware keyboard, but if you open the old Simulator app on the same device, its window still has one.

## "We are in!"

```
[applogin] round 1: screen = app-retry
[applogin] round 2: screen = entra-email
[applogin] round 3: screen = entra-password
[applogin] round 4: screen = entra-otp
[applogin] round 5: screen = entra-kmsi
[applogin] round 7: screen = home
[applogin] logged in
```

All three recipes, PIN pad, Keycloak and Microsoft, in every variant we ship, on both iOS versions. One command, one fingerprint, logged in.

Before shipping I handed the script to a second AI for review. It made good suggestions and we fixed and hardened how the secrets are transmitted.

I still have to demo it and clean it up, but it's already a Swiss Army knife for logins.

## The right amount of indirection

Developers wrap everything in layers. Each layer is an indirection: instead of doing the thing, you point at something that does the thing. Every additional step costs you, and most systems have too many.

This script has three, and all carefully chosen.

The first is the catalog. It knows what exists in 1Password and where, and it can rebuild itself with one command. Nothing else in the script ever talks to 1Password. And it only contains pointers.

The second is the mapping. A table that says which app variant needs which recipe, and which username. Add a variant, add a line.

The third is the recipe. It does not know the sequence of screens in advance. It reads the screen through accessibility labels, classifies which of the login pages it is looking at, and acts accordingly. Up to seven steps, retry button to home, without a script telling it what comes next.

Where are the secrets. Which login does this app need. What is on the screen right now.
