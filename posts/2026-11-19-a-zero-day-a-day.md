---
title: "A Zero Day a Day"
url: "https://scriptease.dev/posts/2026-11-19-a-zero-day-a-day/"
author: "Scriptease"
created: "2026-11-19"
published: "2026-11-19T07:20:54+01:00"
description: "Tuesday night our servers got a new kernel. Wednesday morning two of them kept dying, every minute or so. By Wednesday evening we had worked around a security hole on our Java servers. Thursday at six, the next one was announced."
tags: ["security", "java", "kubernetes", "ai", "production", "saga"]
---

# A Zero Day a Day

_The [First Responder saga](https://scriptease.dev/sagas/#first-responder): [1. Report to Production in Nine Minutes](https://scriptease.dev/posts/2026-11-18-report-to-production-in-nine-minutes/) · 2. A Zero Day a Day_

Tuesday night our servers got a new kernel. Wednesday morning two of them kept dying, every minute or so. By Wednesday evening we had worked around a security hole on our Java servers.

Thursday at six, the next one was announced.

## Both get OOM killed

Our servers run on a fleet of machines, managed by Kubernetes. Each server program lives in its own box, a container, with a fixed memory allowance. Step over it and Kubernetes kills the box and starts a new one. The kill has a name, OOMKilled: out of memory.

Tuesday night the machines under those boxes were reinstalled with a new Linux kernel, the core of the operating system. Wednesday morning I opened the dashboard. Two were dying. I sent my AI a screenshot: "why both get OOM killed".

## A small box that thinks it has all the memory

Java, the engine our server programs run on, decides at startup how much memory it may use. In a container it's supposed to ask the box. These servers asked the whole machine instead. They saw its big numbers, all of its memory and all of its processors, not the small ones they were allowed to use. So they planned for a warehouse and moved into a closet.

The new kernel had stopped listing memory in the one place older Java versions look for it. They didn't find it, quietly gave up on the box, and sized themselves for the machine. There was no warning. Even the usual memory check printed the right limit, because it reads a different place than the part that actually decides.

Newer Java versions look somewhere else and get it right. Ours were older.

I asked my AI: "does a kernel flag something like use cgroups v1 fix it?" Not that one, it said, but there's another: `cgroup_v1_proc=true` puts memory back where the old Java looks for it. We built two throwaway servers, an old Java and a new one, and pinned them to the one machine that already had the flag. Both picked the right size. A colleague restarted the machines one by one with the flag.

I also split three Java upgrades across three AI conversations, so those programs wouldn't need the kernel flag at all. "spawn a new thread and fix" the first one. "spawn 2 more."

## A new Java CVE came up, can you add that

At lunchtime the second thing arrived. Java had a new CVE, a public case number for a security hole. This one came with a nickname, Java4Shell, and no fix yet in the Java we use.

The hole sits in Java's base64 code. Base64 packs any data into text, so it can travel through places that only take text, like a web address. Java has a shortcut for unpacking it again, using special instructions on newer processors. The shortcut can write past the space set aside for its result, like writing past one field on a form into the next. That's a heap overflow.

Only some processors have those instructions, and we run a mix. The same program could be vulnerable on one machine and fine on the next. So we checked our systems one by one. Not many were affected.

There's a switch that turns the shortcut off: `-XX:-UseBASE64Intrinsics`. Java falls back to the slow, boring way, which works. We put the switch on anyway, on every affected Java version we run.

Our move to Java 25 has lived in a single AI conversation [since October](https://scriptease.dev/posts/2026-10-25-taking-over-the-workspace/), the longest one I have. I pasted the ticket into it: "lets add this flag and redeploy all dev systems running java 25". It came back with seven systems switched, each one checked in the running program. I asked one more question: "so there are no java-25 missing without the base64 fix?" Two test systems were. Now they're on the list.

Some of those were the same three programs I had just moved to a newer Java that morning. "came up can you add that." They went out twice in one day.

By evening the switch was running on our live servers.

## A watcher that would wait forever

The real fix is a new Java. We use Temurin, a free edition, packaged as container images: the ready-to-run contents of our server boxes. The fixed images weren't out yet. So I had my AI set up a watcher: every hour, check whether they're out, and ping me.

Its first bug: the fix would be labeled `21.0.13.1_1`, the broken one is `21.0.13_9`. The watcher read the fix as the older of the two. It would have ignored the very release it was waiting for. We fixed the watcher first.

## Thursday, six o'clock

Just after midnight, my colleague posted in our infrastructure channel: the live machines had the kernel flag too, and were rebooted. The memory fix was out.

Six hours later, a security warning landed: four holes in nginx, the web server that hands out our web apps. I asked my AI how many of our servers were affected.

On the machines we could reach, thirty-six copies of nginx ran a version on the warning's list. My AI checked the settings of every one. Each hole needed an optional feature switched on.

Not one of the thirty-six had any of them.

We dodged it. I updated the oldest one anyway, from 2022, and removed a copy nobody needed.

If any of them had matched, it would have been Wednesday again: scan, switch, roll out, wait. [Groundhog Day](https://scriptease.dev/posts/2026-11-05-groundhog-day/).

## Still watching

As I write this, Temurin's tracker shows the fixed Java built and the container images still being prepared. We're safe behind the switch. When the images land, every one of those servers goes out again.

## An old friend: base64

In 2011, our own iPhone app had a base64 bug. It had just gone out through the App Store. We went for lunch. On the walk there, crash reports started rolling in. Real users, real phones. On our test system it had never crashed once.

Our base64 code set aside exactly enough memory for the result, then wrote one more byte after it. One byte past the end. A heap overflow, in base64.

We couldn't put a new app on everyone's phone that afternoon. So we fixed it from the outside. At certain lengths, that extra byte did no harm. So we padded every web address to one of those lengths: a `#` and some garbage at the end. The `#` meant the same page still loaded. Our base64 code counted the garbage anyway.

Then we fixed the code.

Fifteen years later Java had the same kind of bug, in base64 again, and we did what we did in 2011: went around it until the real fix arrives.

It's seven a.m. now. Time for some Java.
