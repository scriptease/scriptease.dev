---
title: "Colormaxing II — Benchmaxing My Own Benchmark"
url: "https://scriptease.dev/posts/2026-08-22-colormaxing-ii-benchmaxing-my-own-benchmark/"
author: "Scriptease"
created: "2026-08-22"
published: "2026-08-23T20:49:35+02:00"
description: "The initial plan was simple: run a test over all 60,000 colors and see how good the new model really is. The plan didn't hold for long. By the end of the day two models were competing — and even the original dataset was on trial."
tags: ["ai", "llm", "ml", "saga"]
---

# Colormaxing II — Benchmaxing My Own Benchmark

_The [Colormaxing saga](https://scriptease.dev/sagas/#colormaxing): [0. The Prequel](https://scriptease.dev/posts/2026-07-30-a-color-speaks-more-than-a-thousand-words/) · [1. One Simple Job](https://scriptease.dev/posts/2026-08-22-colormaxing-i-how-many-parameters-does-one-job-need/) · 2. Benchmaxing My Own Benchmark · [3. In Public](https://scriptease.dev/posts/2026-08-22-colormaxing-iii-in-public/)_

The initial plan was simple: run a test over all 60,000 colors and see how good the new model really is. The plan didn't hold for long. By the end of the day two models were competing — and even the original dataset was on trial.

## The first data set: Trusting the old model

Everything my model knows, it learned from 25,000 answers the old model had already given. That was the first dataset, and it rested on one silent assumption: that those answers were correct.

The AI world has a word for grading a model against the very data it trained on: benchmaxing. It's an accusation — a perfect score proves copying, nothing more. I did it anyway, on purpose, because the score wasn't what I was after. Each time I trained a new version, a small pattern appeared: on the messy names, the new model's answer sometimes looked *better* than the answer it was supposed to copy. A hunch is not a finding. To check it, I needed both models' answers side by side — for every one of the 60,223 color names the live service had ever translated.

## The second data set: Tuning down the noise

But the model heading into that test was already one repair beyond those original 25,000 answers — because the names in it carry noise, and the noise is ours, not the shops'. When the same color name appears on two versions of a product, the two entries have to stay distinguishable — two blues are not the same blue — so our system appends a number: `blau 2764`. The first version read meaning into those digits. So the second dataset taught it, with eight thousand digit-suffixed examples, that the number is bookkeeping: answer the color, ignore the number.

The same round turned the color *up*. The service reserves one special answer, the literal word `colorful`, for genuinely multicolored products — kunterbunt, if you read part one. In 25,000 cached answers the old model had never used it once, so the rule was unlearnable from those answers alone; made-up examples put it within reach.

Less noise, more color: version two. That's the model that took the 60,000-name test.

## 60,000 rows — we're going to need a bigger boat

The run took the afternoon, ten names at a time, with the same safety net the live service uses: one retry, give up only after a second failure.

![Unsloth Studio's live traffic page during the run: 51 requests in the window, zero errors, 1.4 seconds per batch.](https://scriptease.dev/posts/2026-08-22-colormaxing-ii-benchmaxing-my-own-benchmark/assets/colormaxing-ii-benchmaxing-my-own-benchmark/unsloth-api-live-60k.png)

Halfway through I checked the failure counter. Previous incarnations had struggled with the output format, but this fight was over: three broken answers in over three thousand batches.

Now I had sixty thousand rows — enough to fill a spreadsheet, but not a spreadsheet you'd want to read. It was time to build a tool. Or two, or three.

Tool one was an explorer: one web page, every name, old model's color and new model's color as swatches side by side, filterable by how different the two colors are. Beautiful, honest — and useless for a verdict, because staring at it mostly proves you can't hold sixty thousand judgments in your head.

Tool two had opinions. For the ten thousand names where the two models really diverged, it looked up every real color word in the name — across German, English, French, Spanish, Turkish and friends — and asked one question: whose answer is close to what the name actually says? Every disagreement landed in a bucket, and the buckets became clickable verdict cards.

## Reading the results reveals the flaws

The cards said: old model clearly wrong, 1,415 times. New model clearly wrong, 706. Both wrong, 495. Then the two biggest buckets: 4,773 split decisions — names like `weiss/türkis` where one model picked the white and the other the turquoise, both defensible — and 3,410 names with no color you could work out from the words at all. Nobody can be wrong about `top secret`.

But the analysis had shifted: it was no longer a before-and-after comparison being graded — the colors themselves became the grade. And when the colors become visible, the original dataset gets graded with them. Where a name contains a checkable color word, the old model was wrong twice as often as the new one.

The same sixty thousand rows exposed the training data's own flaws. A huge part of it came from a single sports shop's catalog — the same base colors repeated over and over, teaching the model the wrong lesson. The results also looked worse for some colors in languages like Turkish, French and Spanish. And the format itself had taught a bad habit: always ten names per batch. Ask for a single color and the model panicked — seven answers came back, the right one first, then six invented from words in the prompt.

## Calling in the experts

By the end of the day, several AI conversations were running in parallel, each with its own job.

For the language gap I wrote a handoff and spawned an expert whose entire world was one task: collect objective color-name lists in every language the shops speak. It came back with 11,377 color names and their codes across thirteen languages — Wikipedia's color lists, official industrial palettes, every source license-checked.

Another expert had researched something else entirely: how to host the finished model on Hugging Face, the public site where anyone could try it — more on that in part three. That research is what surfaced the single-color question in the first place: a visitor to a public demo types one color name, never ten. And it made the caching argument click — every answered name is stored and reused, so what a live model actually sees is a handful of *new* names at a time. Batches of ten are the exception, not the rule.

And one more expert sat quietly to the side, writing down everything that happened — to turn it into a blog post. Or better: a series of them.

None of them started as an expert. Each got one small document — here, work on this, come back with the result — and the task is what made them one.

![The training job board: version 3 finished, version 4 already running — the day's whole lineage on one screen.](https://scriptease.dev/posts/2026-08-22-colormaxing-ii-benchmaxing-my-own-benchmark/assets/colormaxing-ii-benchmaxing-my-own-benchmark/studio-training-lineage.jpg)

My machine spent the whole day on fire — fans blasting.

## The third data set: The one that never got to be

The single-color fix became the third dataset: the same names, now also served in batches of every size from one to nine, so a lonely single name would no longer be a sight the model had never seen. Version three trained beautifully on it, getting better and better at the examples it was studying, all the way to the end.

It never shipped. But a little U-turn in the learning graph made it interesting.

When training models, the interesting part is not the data the model knows — it's the data it doesn't: a secret test the model never sees during training, kept aside to check whether its answers are actually getting better. Version three's secret-test score improved for one pass through the data, then made a U-turn and got steadily *worse* the longer training ran. It turns out training a model too much is a bad thing.

## The fourth data set: Bringing in the colors

The fourth dataset got everything at once. The sports catalog was finally capped — thousands of rows collapsed to their stem by name, so they could no longer drown out everything else. The mixed batch sizes stayed. And the experts' harvest came in: thirteen languages of real color words. 

And my AI told me about a cool feature: training takes snapshots every now and then, so you can look at the nice graph of the secret-test score and min-max it — just pick the best snapshot. That's what we did: the final model is the snapshot right at the sweet spot, at the bottom of the curve.

Then the same test again, all 60,000 names, three columns side by side: the old model, version two, version four. And the results were promising — not perfect, but what we lost in memorization we gained in language accuracy.

## Mystery of the missing colors

The third tool — the three-way visualization — also showed something I hadn't ordered: refusals. Version four sometimes gives no answer at all. The page had no such number for the previous version, so I asked for it — and the refusals had increased sevenfold.

![Rows from the three-way comparison: long compound names where the old model and version two return exactly the same colors, while version four's column reads "no answer".](https://scriptease.dev/posts/2026-08-22-colormaxing-ii-benchmaxing-my-own-benchmark/assets/colormaxing-ii-benchmaxing-my-own-benchmark/showdown-refusals.png)

But it's not what it seems. That isn't seven times the errors; it uncovered a scheme. The previous version had memorized those answers: instead of finding the color in a convoluted brand-color name, it had used a cheat sheet. The refusal is actually the correct response to ambiguity — and dealing with those long names is a task for another dataset.

## The fifth data set?

Somewhere in those refusals, a fifth dataset is waiting. I left the question unanswered.

That's where I left the model too: good enough, and better than expected. There's a packaged version sitting on my computer that can run anywhere. 

But that would not be the way to end this saga. In part three, it goes public.
