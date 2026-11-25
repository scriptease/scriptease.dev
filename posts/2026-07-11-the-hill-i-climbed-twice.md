---
title: "The Hill I Climbed Twice"
url: "https://scriptease.dev/posts/2026-07-11-the-hill-i-climbed-twice/"
author: "Scriptease"
created: "2026-07-11"
published: "2026-07-17T19:09:42+02:00"
description: "A year ago, getting our iPhone app through SonarQube was an uphill fight I kept losing. This week the same walls fell in an afternoon — and I barely touched the keyboard."
tags: ["ci", "codereview", "security", "ios", "ai"]
---

# The Hill I Climbed Twice

A year ago, getting our iPhone app through **SonarQube** — the code scanner we use at work — was an uphill fight I kept losing. This week I watched the same walls fall in a single afternoon, and I barely touched the keyboard.

SonarQube is a **code health inspector**. You point it at your source code and it hands back a report card: here are the likely bugs, here are the security holes, here's the sloppy stuff, and here's how all of it is trending over time. We wanted one because it turns a vague sense that code is rotting into an actual list. Ours ran for about five minutes, a year ago, before I gave up on half of it.

## The first climb

Setting it up the first time was miserable. It needed a database of a very specific vintage, hand-installed, and every version had opinions about every other version. I fought it into place and got it grading our behind-the-scenes server code. A win, sort of.

Then I turned it on the **iPhone app**, and it just… wouldn't. The scan would churn for ages and hand back nothing — no bugs, no findings, a blank report for tens of thousands of lines of code. I'd tweak something, run it again, wait, get nothing. It felt like pushing a boulder uphill and watching it roll back every single time.

Eventually I did the thing every developer does with a fight they're losing: I wrote myself a ticket, assigned it to me, and marked it *someday*. That's the professional version of shoving something in a drawer. The drawer stayed shut for a year.

## Coming back to nothing

Last week, *someday* arrived. I opened the drawer.

It was empty — and that didn't surprise me, because I'd emptied it myself. When I gave up, I didn't just walk away; I ran the one command that tears the whole thing down and switched it off on purpose. So I wasn't dusting off an old setup. I was rebuilding from scratch, exactly as I'd left it: nothing.

And in a year, the ground had shifted under every piece. The database no longer came in the box — I had to bring my own. The old one couldn't come along anyway: the new version wanted a newer kind of database than my year-old data lived in, and hauling that data across would have been fiddly, high-stakes surgery. So I didn't. I let the old projects go and rebuilt from scratch — which sounds insane until you notice that rebuilding is now the *cheap* option, because the AI does the repetitive part. (The free edition had also grown a trap: miss one hidden switch and it quietly installs the *paid* version instead. I did not miss it.)

Exactly one thing survived the year intact. When the fresh install asked me to set a password, my keychain offered up the one from a year ago — still remembered, still valid. Everything else had to be rebuilt; that password was the only piece of past-me that made it across. Then I turned to the door that had beaten me last time: the iPhone app.

## The same walls, in the same order

That was the part I'd been dreading, for a specific reason. SonarQube doesn't understand Apple's code out of the box; you have to bolt on a separate **plugin** — an add-on that teaches it the language — and a year ago, wrestling that plugin into place had been its own miserable afternoon. This time it was smooth sailing: in a whole year the plugin had crept forward by the tiniest possible update, sitting almost exactly where I'd left it while everything else lurched years ahead. From its point of view, the year had never happened.

That was the good news. The bad news was everything the plugin then had to look at — because every other enemy from a year ago was still standing, in formation.

The scan that runs forever and reports nothing: back. The app going in and coming out the far side with no trace of its code — the report insisting I'd apparently written twenty thousand lines in one afternoon, because it couldn't actually *see* any of them: back. Same fights, same losses, exactly where I'd left them.

At the bottom of it all was a gloriously stupid root cause. Years ago someone had made a **shortcut** — a folder pretending to be another folder, the two names differing by a single capital letter. I'd been running the scanner *through the shortcut*. So the scanner filed its notes under one address, and the style-checker filed its complaints under the other, almost-identical address — and because the two addresses didn't match, SonarQube decided none of the complaints belonged to this project and threw **every last one in the bin.** Twenty-seven thousand five hundred and seven of them. Point the scanner at the real folder instead of the shortcut, and 0 findings became 27,507.

A year of "it just doesn't work on iOS." The monster in the drawer was a shortcut with a typo in its name.

## The difference was who showed up

Here's what actually changed between the two climbs. It wasn't the walls — the walls were identical. It was that this time I wasn't climbing alone.

The tool hands out two kinds of key. A **narrow** one that can only push and pull a single project's data, and a **master** one that can do anything, including create projects and mint those narrow keys itself. I didn't hand over a standing personal key. I minted a fresh master key *just for this session* — one meant to be thrown away — and gave that to my AI with a list: five projects, set them all up.

And it did. For each one it cut its own narrow key, ran the analysis, set the project private the way I like, and applied a rule change I'd asked for. (SonarQube grades every project against a pass/fail checklist. One default rule was failing our decade-old apps merely for not yet reporting any automated-test numbers — which told me nothing — so I changed that rule.) The barriers that had cost me a year — the shortcut, the endless scans, the reports full of nothing — fell in the time it took to make coffee. I wasn't heaving the boulder anymore. I was pointing at the hill and saying *that one*.

## Then I burned the key

Here's the part I'm proudest of. The moment the setup was done, I **destroyed that master key.**

And this is the quietly clever bit: it no longer matters that the key passed through the AI — that it's sitting in the session's history, that it was, in the loosest sense, *leaked*. A revoked key is a dead key. You could read it straight off my screen and it would open nothing. The risk was neutralised the instant I switched it off, by design rather than by trust.

What's left behind is only the good part: the AI wrote itself a note on exactly how the job is done. So next time there's no master key at all — I hand it one narrow, single-project key, it reads its own notes, and it runs the whole dance again, strictly inside the lines I've drawn. The capability stayed; the risk went back in the box.

## A million lines, and a little time travel

Because that workflow was now repeatable, I stopped doing one project at a time. They piled in fast — three iPhone apps, seven server projects. At some point I glanced at the running total and stopped: **a million lines of code**, all under one health inspection.

And here's the fun fact that stuck with me. Software quietly keeps a logbook of who last touched every single line, and when. So a lot of what the scanner flagged didn't just arrive with a description — it arrived with a **name and a date attached, some of them a decade old.** Security issues in code written before the phone in my pocket existed, still sitting there, now politely surfaced with the original author's name beside them.

It's a strange kind of time travel. The tool doesn't care that a line is ten years old; to it, an issue is an issue. Turn the lights on in a room nobody's swept since 2015 and you see all of it at once — including who tracked in the dirt.

And that's the honest, slightly deflating truth about these inspectors: point one at a big old codebase and it hands you a mountain you will never finish. Thousands of findings — enough to fill hours, then months, then years. You don't clear the list; you triage it, forever.

Which is what makes the last one such a happy ending — though it didn't start that way. The newest and smallest project — a little service we'd recently built that catches payment notifications from a payment provider — showed up to its first inspection with **thirteen issues** on the report card. Not a mountain, but not nothing. The difference was that I could hand it straight back to the same AI that had built the service, with a single instruction: upload it to SonarQube, read what the inspector flagged, fix it, upload again, check again. It ran that loop — detect, fix, re-check — until thirteen became zero and the board went green: **97% of the code checked by automated tests, and not a single issue left.** The only project in the whole million-line pile to get there — not because it was born clean, but because, for once, something worked the list all the way to the end.

## So what

The problem never got easier. The shortcut was still there, the scans were still slow, the tool had if anything grown *more* finicky in a year. Nothing about the hill had softened.

What changed is that I no longer had to climb it myself. I could hand the climb to something tireless, watch it write the route down, and take the keys back when it was done.

The password from a year ago still worked. So did the problems. The only thing that had changed was who showed up to solve them.
