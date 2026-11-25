---
title: "Taking Over the Workspace"
url: "https://scriptease.dev/posts/2026-10-25-taking-over-the-workspace/"
author: "Scriptease"
created: "2026-10-25"
published: "2026-10-28T19:27:24+01:00"
description: "For weeks my AI ran one of our workspaces on its own. It merged, built, deployed and tested, and nobody else touched that code. Then, for the first time, I asked it to set up a workspace I could look at too."
tags: ["ai", "claude", "agent", "automation", "saga"]
---

# Taking Over the Workspace

_The [Hands-Off saga](https://scriptease.dev/sagas/#hands-off): [1. Non-Load-Bearing](https://scriptease.dev/posts/2026-07-21-non-load-bearing/) · 2. Taking Over the Workspace · [3. Better Call Sol](https://scriptease.dev/posts/2026-10-28-better-call-sol/) · [4. It's Time to Settle](https://scriptease.dev/posts/2026-10-30-its-time-to-settle/) · [5. Fake It Till You Merge It](https://scriptease.dev/posts/2026-11-21-fake-it-till-you-merge-it/)_

For weeks my AI ran one of our workspaces on its own. It merged, built, deployed and tested, and nobody else touched that code. Then, for the first time, I asked it to set up a workspace I could look at too.

## "That was fast"

A colleague from our web team sent my AI a message in Slack, our work chat, with an upside-down smiley: "Create a ticket on how we can set up git repo for [both customers'] web". Repo is the tool that sets up our workspaces, with several projects side by side.

My AI wrote the ticket and answered in the thread. Four minutes after the request, my colleague replied: "That was fast."

We gave it the label for planning poker, the round where the team estimates work together. That was for next week.

## Prototype before the estimate

Over the weekend I picked up the ticket from my phone.

The idea in it: our web apps are built from several projects that share code. Today a change in one has to be released before the others can even try it. Release first, find out later. The ticket asked how to test changes across projects together, before anything is released. Our servers already work that way.

"I don't want to impose anything on the Web app team. I just want to explore how it could work."

My AI set up one workspace with all eight web projects. Then it suggested where to start: the web app I had built only days before, which reuses parts of another one.

I had planned to plant a bug for the demo, something that only breaks when the two are built together. I didn't have to. They had already drifted apart, and nobody had noticed, because each project only ever saw the last released version of the other.

"This is actually perfect"

So the demo is two changes, one in each project, tied together by a topic: a label that creates a virtual workspace where both projects sit next to each other, changes included. "we let it fail once and then we add a topic and the second run is successful".

The first run, without the topic, failed. The second, with both changes under one topic, passed. Half an hour after my first message from the phone.

Both changes are marked work in progress, not to be merged. The ticket is still waiting for its estimate.

## A recursion of traffic lights

The other prototype started with a colleague mentioning that we now have OpenObserve, a tool that collects what our servers report and draws charts from it.

I gave my AI the reins. It logged into the web page through a browser it controls and built a dashboard for the machines our servers run on. What it couldn't read was the part I cared about, the numbers for each running app. Nobody was collecting them yet. So it drafted the request, and I asked the colleague who runs our servers to install the missing piece.

Then I thought about what I actually wanted. Our servers have a health check: a tree of small automatic checks, where one red light turns every light above it red, all the way up to the server. Known problems can be muted, so one of them doesn't keep the whole server red forever.

I asked my AI to build that, locally: a throwaway OpenObserve on my Mac and a few small demo servers to feed it. It came back with a dashboard. Tables, an alert, a timeline. It worked.

It wasn't what I wanted.

"So my idea is basically a recursion of aggregated traffic lights if you know what I mean." A tile for each server, red or green, that opens into its parts. A button to break something, a button to mute it, and a dark red for muted but still failing.

Halfway through I hit my usage limit, and it had to wait. The second version had the tiles. On the way it found a bug in our real mute logic: a muted problem could still keep the light above it red.

My quest is to [turn every traffic light on the road green](https://scriptease.dev/posts/2026-07-13-remote-remoting/). This time I had to build the traffic lights first.

## The AI-only workspace

The workspace from the beginning of this story was our move to Java 25, a newer version of the language our servers are written in. It [started in July](https://scriptease.dev/posts/2026-07-12-all-i-wanted-was-one-project/), when all I wanted was one project running on my laptop. That story ended on yellow: every light a machine could turn was green, and the last one waited for a person.

Now Java 25 runs on our development systems.

Meanwhile, in another chat, my AI reworked the admin pages of those servers, the pages we use to change their settings and track down problems. They fell apart on small screens: tables you couldn't scroll, buttons cut off at the edge. I let Fable, one of the Claude AI models, test the pages on its own, on every server we already run on Java 25. It started each one on my Mac, opened every page in a browser it drives, shrank the window to phone width and looked for anything cut off. Fix, shut down, next server. On one of them, a single error message had made a table wider than a dozen screens.

When I asked "Any unsolved issues you found?", it listed what it hadn't tested.

The workspace it finally set up for me was a copy of my usual editor setup, "so it keeps my formatting and comment settings". Then I opened the code and looked at what it had been up to.

## The perfect workflow for you too

I spent weeks giving my AI what it needs to do the work by itself: workspaces where it can change several projects at once, test runs it can start on its own, a browser it can log into, ways to read our servers. That's why a joke ticket became a working proof over a weekend.

My colleagues don't have that yet. Between their change and seeing it run, someone still has to step in. What I want for them is continuous delivery: a change goes from their keyboard to a running test system on its own.

Before the joke, I had already promised them: "on monday we will create the perfect workflow for you 2 :-)"

The next week, the demo went well. I left them with the workspace, the pieces and a goal: set it up, try it on something nothing depends on yet, and then:

Make it work. Make it fast (where the AI still struggles). Then make it right.
