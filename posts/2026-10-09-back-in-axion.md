---
title: "Back in AXIon"
url: "https://scriptease.dev/posts/2026-10-09-back-in-axion/"
author: "Scriptease"
created: "2026-10-09"
published: "2026-10-09T21:08:20+02:00"
description: "At lunch I was the one holding the iPad, turning it while my AI waited for my verdict. By the evening the AI was logging in and out of that iPad by itself."
tags: ["ai", "agent", "commandline", "skills", "ios", "saga"]
---

# Back in AXIon

_The [AXI saga](https://scriptease.dev/sagas/#axi): [1. The Checklist I'd Been Following](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/) · [2. AXI All the Things](https://scriptease.dev/posts/2026-09-26-axi-all-the-things/) · [3. Not My First Rodeo](https://scriptease.dev/posts/2026-10-07-not-my-first-rodeo/) · 4. Back in AXIon · [5. Anticipation](https://scriptease.dev/posts/2026-10-09-anticipation/) · [6. Making Our App Leak Its Secrets](https://scriptease.dev/posts/2026-10-18-making-our-app-leak-its-secrets/)_

At lunch I was the one holding the iPad, turning it while my AI waited for my verdict. By the evening the AI was logging in and out of that iPad by itself.

## This is not enough

Our iPad app has a barcode scanner, and on iOS 27, the newest version of the iPad's operating system, the camera picture had started coming up sideways. The fix had been in for a week. What was missing was the proof, and this one can't be faked on a fake iPad: the bug only shows on a real one, turned in your hands.

So the AI built the app and put it on my iPad through `xcrun devicectl`, Apple's own tool for talking to a device by typing commands. Then it handed me instructions: open the scanner with the iPad sideways, both ways, and check that the camera picture stays upright. I turned it, then held it upright. "its upright even in portrait everything fine"

"Can you take a screenshot of the device?" It could. The same Apple command takes screenshots. The ticket in Jira, the to-do list our team shares, got the comment and the picture through [the command from last time](https://scriptease.dev/posts/2026-10-07-not-my-first-rodeo/), and was closed.

So the AI could build, install, screenshot and close. What it couldn't do was touch the screen. The turning and the tapping were still me, with the AI waiting for my verdict.

This is not enough, I thought.

## Let's continue the AXIfication

Three days earlier, over a colleague's lunch break, the AI had gotten [its own login for our web app](https://scriptease.dev/posts/2026-10-06-built-over-his-lunch-break/). It cut my testing time to a fifth. Chrome, Google's browser, is simply a faster horse than the simulator, the fake iPad on my Mac. The AI drives the fake one through Argent, its remote control.

Which left the real iPad as the slowest one in the stable.

Let's continue the AXIfication.

## "i want to make them optional"

The iPad project had two plug-ins in my AI's head. MCP is the standard socket an AI uses to hook up an outside tool; a plug-in is one tool on that socket. Argent, for the fake iPad. MobileBuildMCP, which builds the app. Every conversation in that project started with both loaded, whether the task was a login or a one-line fix, and two was already too many.

Talking to a real iPad would take a third: mobile-mcp, a plug-in for real phones and iPads, which a colleague had recommended and I had never gotten around to.

The morning of the iPad test, one sentence from me, "can we reuse the pattern we used in jira-axi and use mcpc?", had moved the crash-report command onto the same trick as the Jira one. mcpc is the small tool from last time that starts a plug-in only when asked and keeps it running between questions. The trick had become copy-paste.

So instead of adding a third plug-in, I decided to turn all three into commands. I switched the two off, the same move as with Rovo, the Jira plug-in from last time, this time from a menu, and asked for the trick three more times: "lets create a folder in scripts named mcp and then create an axi for" the three, "each using mcpc". An AXI is a command written for an AI reader, [following ten rules](https://scriptease.dev/posts/2026-08-30-the-checklist-id-been-following/). And, so it knew why: "at the moment i run them … as mcps but i want to make them optional".

The AI didn't write three commands.

It wrote one file, 98 lines, and gave it three names.

On a Mac a file can have extra names that point at it, and the script looks at which name it was called by and picks its plug-in from that. One body, three faces. My polymorphic MCP wrapper.

One thing fought back. The build plug-in had renamed its settings folder in its latest version without saying so, and everything came back empty until the AI found the rename.

From then on, the three ran as commands, only when asked.

## "nothing happened"

New session, one hint: "using mobile-axi". mobile-mcp, the plug-in I had never tried, was running within ten minutes. The AI built the app for the real iPad, installed it through the new command, and reported it running.

"nothing happened"

The launch had reported success and the iPad had stayed dark. It was locked. Unlocked, the app was there, under the short name the test build gives it.

Then the question I had come for: "its running can we make applogin-axi.py work for the device"

The login script, [the one that logs the AI into our app on the fake iPad](https://scriptease.dev/posts/2026-09-05-every-login-all-at-once/), exists twice by now: the original in Python, and a newer port in Go, a different programming language. "do it in pythin first". The AI read the real iPad's screen the way it reads the fake one, found the same fields, the e-mail box, the password form, and mapped every tap, swipe and keystroke onto the small helper app mobile-mcp installs on the iPad itself. For the first time, it held the reins of a real iPad.

E-mail went in. Password went in. The six-digit code went in. Nothing moved.

## A Heisenbug

I wanted a picture of this. An AI typing into your iPad is something you want to show people, so I pressed the two buttons that take a screenshot. On this iPad, a screenshot opens a feedback window on top of whatever is running. The return key that should have sent the code went nowhere.

"i think i caused it with a screenshot"

A Heisenbug: a bug that changes its behaviour when you try to observe it, named after the physicist Heisenberg. I had been messing with the AI by trying to photograph the AI. Try taking a photo from the saddle without pulling on the reins.

The rerun cleared the stale code, typed a fresh one, and landed on the app's home screen.

"log out and in between the 2 … users as a test each 2 times"

Four logouts, four logins, two test users with two different sign-in paths, every one of them ending on the home screen. A login took about a minute and a half. A logout, sixteen seconds.

## A first draft

On the simulator the keyboard was [the whole story](https://scriptease.dev/posts/2026-09-05-every-login-all-at-once/): German layout, US key positions, a globe key hidden behind the thing we were doing. On the real iPad the letters arrive as letters, so that one is gone.

The rest isn't. The "fill password?" box pops up on every login and has to be closed every time. The sign-out row comes back without a label, so the log says it tapped nothing, while it tapped the right row. And the password travels as part of the command that starts the typing, where other programs on my Mac could glimpse it for a second. The AI flagged that one itself; the Go version will take a different route.

## "feedback welcome"

I showed it to a colleague. Then the AI posted it in our iOS channel in Slack, our work chat, through the Slack command, as an early test version: "Alpha version of the skill & script to drive the login automation also on physical devices … if somebody wants to check it out, feedback welcome." Signed, as always, "Send by :claude:". It's "Sent by" now. This version still had the typo.

At lunch the iPad had been the one screen in my setup my AI couldn't touch. By the evening it was logging in and out of it while I watched.

Now I have three to choose from: the fastest, Chrome, for changes that only touch the server, the computer behind the app; the simulator for changes to the iPad app; and the iPad itself for the things that only work on the real thing.

Still a wild horse. But I'm back on it.
