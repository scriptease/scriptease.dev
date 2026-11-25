---
title: "OCR — Three Letters, Three Completely Different Things"
url: "https://scriptease.dev/posts/2026-07-29-three-different-ocrs/"
author: "Scriptease"
created: "2026-07-29"
published: "2026-07-29T07:14:08+02:00"
description: "I typed a three-letter command to run an AI code reviewer. It ran a screenshot reader instead. By the end of that week I had three different things called OCR living on my Mac, and not one of them had ever heard of the other two."
tags: ["ai", "llm", "macos", "claude", "automation", "localai", "saga"]
---

# OCR — Three Letters, Three Completely Different Things

_The [Local AI saga](https://scriptease.dev/sagas/#local-ai): [1. Little Gemma vs Big Desk](https://scriptease.dev/posts/2026-07-05-little-gemma-vs-big-desk/) · 2. Three Different OCRs · [3. Friendly Competition](https://scriptease.dev/posts/2026-08-16-friendly-competition/) · [4. 95% Done, 100% Blue Sky](https://scriptease.dev/posts/2026-08-17-95-done-100-blue-sky/) · [5. Lost in Compression](https://scriptease.dev/posts/2026-08-25-lost-in-compression/) · [6. Qwen Revisited](https://scriptease.dev/posts/2026-09-06-qwen-revisited/)_

I typed a three-letter command to run an AI code reviewer. It ran a screenshot reader instead. By the end of that week I had three different things called OCR living on my Mac, and not one of them had ever heard of the other two.

## Same three letters, three strangers

OCR normally means one thing: optical character recognition — pulling the words out of a picture, so a photo of a page turns into text you can copy. That's the textbook definition, and it was the least of my problems.

Because that week "OCR" also meant an AI code reviewer from Alibaba, called Open Code Review. And it meant a little screenshot tool I'd been quietly running for years, called macOCR. Three tools, one acronym, zero awareness of each other.

## The one I'd used blind for five years

I have a tiny app I love. I press a shortcut, drag a box around any part of my screen — a slide, a screenshot someone sent me, a photo of a whiteboard — and the words inside it land in my clipboard, ready to paste. A little notification pops up to say it worked. I do this a dozen times a day and barely notice it's there.

I started doing this years before Apple built the same trick into the Mac — Live Text, they call it, where you can now select words straight out of a picture. Back then you couldn't, and my little tool filled the gap.

And it still earns its keep for the one thing the built-in version can't touch: a screen that isn't mine. When a colleague shares their desktop on a Zoom or Teams call and a product number or a line of code flashes up, I can't select it — it's a live video of their screen, pixels, not text. I snip a box around it and my tool reads it off anyway.

Then I got a new Mac, and it started nagging me. Apple has spent a few years moving off the Intel chips it used to buy from someone else and onto its own — and a new Mac throws up a warning when you run an old program built for the dead chips. My beloved little tool was one of them.

I thought I'd fixed this already. I hadn't. The warning kept coming back.

So I opened the app to update it, and hit a wall. Inside was a single program file — a *binary*, meaning the finished program with no readable source code attached, no readme, nothing. It was just named `ocr`. I had no memory of where I'd got it. Try to look *that* up: search the web for "ocr" and you get the entire field of reading-text-from-images, none of them my orphan. The name that should have been a signpost was camouflage.

## "How do I even update this?"

This is where it became a back-and-forth with Claude, the AI I pair with.

I couldn't tell it where the thing came from, because I didn't know. So I handed it the only thing I had: the mystery binary itself. It read the fingerprints off it. Built in 2021 — which meant I'd been using this thing for five years without once wondering where it lived. Written in Swift, Apple's own language. Leaning on an older Apple framework — a built-in toolkit — for the actual text-reading.

Those three clues were enough. It went and found where it came from: an open-source project — public code anyone can read — called macOCR, whose own dates lined up with my binary's 2021 stamp. Same tool. It had identified a five-year-old unlabelled program from the inside out, something my own googling never got near. And it spotted that the project had since shipped a newer build that runs on Apple's new chips.

The fix itself was mechanical after that: update the app with the newest binary, and the warning disappeared.

One OCR down. This one only needed us to work out what it was.

## The one that reads

The second OCR was the textbook kind, and the reason the week started at all.

Baidu — one of China's big tech firms — had put out an AI model — a trained program — called Unlimited-OCR that reads text off scanned documents unusually well. I wanted it running on my own Mac, privately, instead of uploading company paperwork to someone else's server. One catch: it was built only for Nvidia's graphics cards, the kind that don't come in a Mac.

There was supposedly a version adapted for Apple's chips. There wasn't, really — the adapted code was broken and, as far as I could tell, had never once run. So I sat down with Claude and we fixed it ourselves — including a glitch where it got stuck reading the same line over and over on a crowded page.

Then it worked, and well. I fed it a fourteen-page scanned PDF and clean text came back in about a minute. It read printed tables it had no business reading. Its one blind spot was almost endearing: handwriting. Where someone had scrawled an order quantity by hand, it saw *that* something was written, shrugged, and typed the letter "A". Machines are still bad at our handwriting. So are most humans.

Two OCRs down. This one fought back, then delivered.

## The one that reviews

The third OCR was the one I'd typed the command for in the first place. Alibaba's Open Code Review: an AI that reads a proposed change to a program and leaves comments on it, the way a colleague marks up your work.

The idea was appealing. Instead of dropping a big change on a small AI running on my own machine and hoping, you put it on rails — a *harness* that makes it work in careful little steps, one thing at a time, so it can't wander off. Cute in theory.

I pointed it at a real change at work — a fix to a payment-terminal integration — and let it run.

The result was mostly noise. It wrote twelve comments. Four were the same handful of remarks, posted twice. One flagged a problem and then, mid-sentence, took it back: "My apologies for the false alarm." One concluded there was nothing wrong at all. When the dust settled, six actual opinions were left, and exactly one of them was real.

So I handed the whole messy review to a second, stronger AI — the one that had written the change — and asked what it made of it. Its verdict: "The review is ~35% signal."

And yet. That one real comment mattered — it pointed at a genuine threading bug I'd just introduced myself, the kind where two parts of the program run at once and trip over the same data. The reviewer got the *why* wrong and the fix wrong, but it pointed at the right spot. The second AI brushed aside the duplicates and the self-retraction and pulled that single real thread out. Not a verdict. A lead.

## Three strangers, one name

So that was my week with OCR: a screenshot tool that turned out to be a five-year-old stranger, a document reader I had to repair before it would read, and a code reviewer that was two-thirds hot air with one good instinct buried inside.

The joke is the name. Three letters, stamped on three tools that share nothing, sitting on one laptop. It sent a screenshot reader when I asked for a reviewer. It hid my own tool from me for an afternoon.

I still don't know what to do with the reviewer. Maybe it earns its keep as a cheap second opinion on the code you can't afford to get wrong, where even a noisy extra pass is worth the sift. Maybe its only real use is to make a better AI look at the same code twice, from a fresh angle. I haven't decided.

But the reader I'll keep. And the screenshot tool — now that I finally know its name — I'll happily go back to using blind for another five years.

Besides, of the three, it's still the only one that answers when I type `ocr`.

## Update: the signpost got built

The day this post went out, I went back to say thank you. I opened an issue on the macOCR project titled ["No issue"](https://github.com/schappim/macOCR/issues/44) — no bug, just the story: five years of quiet service inside an Automator app, and an AI reading fingerprints off the binary to find its way home.

The maintainer answered within the hour. "Five years quietly inside an Automator app is the best kind of bug report." The part that stung him was the camouflage — nothing in the tool pointed home, and he fixed it the same morning, in [v1.2.0](https://github.com/schappim/macOCR/releases/tag/v1.2.0): `ocr --help` now says what the tool is and where it lives. `ocr --version` lets a mystery binary on anyone's machine identify itself. And `ocr --update` fetches the newest build — it even notices when the Intel version is running on an Apple-chip Mac. My thank-you note also shook out two real bugs, fixed in the same release.

The next person who inherits an unlabelled `ocr` won't need an AI to find its family.
