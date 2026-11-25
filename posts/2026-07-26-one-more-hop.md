---
title: "One More Hop Is All You Need"
url: "https://scriptease.dev/posts/2026-07-26-one-more-hop/"
author: "Scriptease"
created: "2026-07-26"
published: "2026-07-26T17:47:09+02:00"
description: "At home my iPad can already reach everything — my Mac's local AI, and the work tools my Mac reaches through the company's private network. RustDesk even beams the Mac's screen to my phone. But a screen you squint at through a café window isn't where you do real work. I wanted my iPad itself to reach what my Mac reaches — from anywhere."
tags: ["networking", "macos", "llm", "automation", "ai", "saga"]
---

# One More Hop Is All You Need

_The [Couch computing saga](https://scriptease.dev/sagas/#couch-computing): 1. One More Hop · [2. A Hoarder's Dream](https://scriptease.dev/posts/2026-09-12-a-hoarders-dream/) · [3. The couch group](https://scriptease.dev/posts/2026-09-14-the-couch-group/) · [4. Extending the Tail](https://scriptease.dev/posts/2026-09-19-extending-the-tail/)_

At home, at my desk, my Mac can reach everything I need for a day's work. Some of it runs *on* the Mac — a local AI I chat with, an AI model that lives on my own computer instead of on someone else's servers. And some of it runs somewhere else entirely: the internal work tools that only my Mac can open, because my Mac sits on my company's private network and knows the secret handshake. At my desk, all of it is one click away. The moment I leave the house, the door shuts.

## Screensharing on the go is clunky

I wasn't starting from nothing. I already had RustDesk — a free, open cousin of TeamViewer, the kind of app that mirrors one computer's screen onto another so you can click around from far away. From a café I can pull up my Mac's whole desktop on my phone and poke at it.

And it's the wrong tool for real work. RustDesk only shows me what the Mac *exposes* — its screen. Working through a mirrored desktop on a phone is like doing carpentry by describing the cut to someone on a video call and watching them make it. Fine for a glance; miserable for an afternoon. I didn't want to *watch* my Mac reach my work tools. I wanted my iPad, with its own browser and its own keyboard, to reach the very same things my Mac reaches — as if it, too, were sitting at my desk.

## One hop bridges the gap

The tool for that is Tailscale. It strings a private wire between your own gadgets over the open internet, so your phone, your iPad and your Mac behave as if they were all on the same home network — even when they're scattered across three cities.

I set it up on the Mac, the iPad and the phone, signed them all into the same account, and the first hop landed immediately. On the iPad, over cellular, I opened the chat app that talks to the local AI on my Mac — and it just answered, from outside my house. That first reply felt like cheating.

But talking to the Mac's own AI is a single hop: iPad to Mac, done. Reaching a work tool is two. Hop one lands my iPad on the Mac; hop two still has to carry on from there — out through the company's private network to the tool itself. Tailscale nails hop one. Hop two was where the trouble started.

## First hop down, but the second one didn't want to

So I tried the work tools next, and the wire went dead.

Those tools live behind a *second* tunnel — the tighter kind a workplace strings around its internal systems, so only the right machines can knock. My Mac makes that hop in its sleep: type the address into its own browser and the page loads, no fuss. So I assumed Tailscale, riding along on the same Mac, could carry on from where it dropped me.

It couldn't. Every way I tried to point the private wire at those services, it just hung — not slow, not an error, *nothing*. I ran the network equivalent of holding a stethoscope to the wire and watched for traffic. Zero. Not a single packet was leaving. Hop one worked flawlessly; hop two, Tailscale simply would not take.

## The third hop did the trick

This is where it turned into a back-and-forth with Claude, my AI pair.

I fed it the strange fact: the Mac itself makes hop two fine, but Tailscale can't. It seized on exactly that gap. The diagnosis: on a Mac, Tailscale runs *beside* the operating system rather than woven into it — a polite guest in its own room, not a member of the household. The household can walk into the second tunnel; the guest can't even reach the door.

Once it said that out loud, the move was obvious — and it was Claude's, built on the clue I'd handed it. Don't teach the guest to open a door it can't reach. Add a runner who's already inside the house. A tiny relay called `socat` takes the baton from Tailscale the moment it lands on the Mac, then makes the tunnel hop itself. The path stops being a two-hop journey Tailscale can't finish and becomes a three-hop relay: iPad to Mac, Mac to relay, relay through the tunnel to the tool. That extra hop in the middle is the whole trick.

We worked through it back and forth. One clue, one insight, one move at a time.

## It works, so let's turn it off

With the relay running the middle hop, the iPad opened the internal tool over a proper secured link, from anywhere — the last stubborn page finally showing up on the small screen in my hand.

And then I turned it off. That sounds backwards, but the point was never this one page. The point was opening the *door* — proving the three-hop relay works — so I could reach *any* of those work tools whenever I wanted, without leaving the relay running the rest of the time.

So instead of leaving it running, I had Claude write the recipe down. Now from the café I can tell Claude which tool I need reachable; it starts the relay, opens the door, and I get on with the actual work. The trial becomes a door I can open on command.

There's always one more hop you can automate.
