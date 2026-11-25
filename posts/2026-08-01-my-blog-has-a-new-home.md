---
title: "My Blog Has a New Home: scriptease.dev"
url: "https://scriptease.dev/posts/2026-08-01-my-blog-has-a-new-home/"
author: "Scriptease"
created: "2026-08-01"
published: "2026-08-02T00:39:27+02:00"
description: "It started with a fish tank. The next day that silly free fish tank had talked me out of paying to run my own blog."
tags: ["github", "opensource", "ssl", "static", "web"]
---

# My Blog Has a New Home: scriptease.dev

It started with a fish tank. Not a real one — a cartoon coral reef on a web page, seventeen fish drifting through the coral, and a shark I could grab with the mouse and drag around to send them scattering. I built it to relax. Then I put it on the internet, for free, at its own address, and forgot about it — you can still find it [here](https://scriptease.dev/posts/2026-07-31-hosting-fish-slop/).

The next day, that silly free fish tank had talked me out of paying to run my own blog.

## The free fish tank

To share the reef, I'd used GitHub Pages. GitHub is where programmers keep their code; Pages is the free website hosting bolted onto the side of it — you hand it a folder of files and it serves them to the world, no server to rent, no monthly bill. The reef went up, and it's still there, costing nothing, doing its slow underwater thing whether anyone's watching or not.

I didn't notice the string attached. GitHub Pages serves a folder for free *only if anyone is allowed to see it*. The reef was a toy — I had no reason on earth to hide it, so the string never pulled tight. Free felt like free.

## Ads on my own words

My actual blog lived somewhere else, on WordPress — a hosted service that runs your blog for you. I was on the free tier, and the free tier has a way of paying for itself: it puts ads on your posts. Writing I give away, wrapped in adverts I never chose and don't earn a cent from. I'd made peace with it, the way you make peace with a squeaky door, because the alternative was renting a server and babysitting it forever.

And it had served me well. When I moved off Tumblr years ago, WordPress swallowed the whole thing — every saved link migrated over, tags and all — and it had been hosting more than seven thousand of them ever since, basically for free.

## A secure redirect

Then there was the domain. I own scriptease.dev — I rent that name from a company called IONOS. And `.dev` is a fussy kind of address: it's run by Google, and it has one iron rule — every `.dev` site *must* be served securely, over HTTPS. HTTPS is the little padlock in the address bar, the encrypted connection that stops strangers reading along. Browsers won't even open a `.dev` address without it. No padlock, no page.

Here's the absurd part. At that point my domain barely did anything — typing scriptease.dev just bounced you onward to the WordPress address. A redirect, nothing more. And to add a padlock to the URL, IONOS offered to sell me a certificate. A yearly fee, to secure a page whose entire job was to point at a different page.

I thought this was the way to go, but…

## Moving in with the fish

So I moved the whole blog to where the fish already lived.

It turned out to be less work than it sounds, because my posts are already just text files — written in Markdown, a plain way of writing where a `#` marks a heading and stars mean bold, no fancy editor required. I wrote a small script — a short program with one repetitive job — that reads every post, turns each into a web page, and drops the lot into a folder. That folder *is* the website. Push it to GitHub, and Pages serves it, exactly like the reef.

And since the page was finally mine, I made it feel that way: I built a sidebar to hold links to wherever I wanted to send people, and I added the little shark from the reef.

And since the whole folder runs on my machine, I can ask to spin up a private server and click through it before the world gets to meet the finished page.

Then I pointed the domain at GitHub instead of at WordPress, and waited.

## But the browser didn't like it

For a few minutes, my own site told visitors to run.

Bright red warning, full width: *this connection is not private*. Because `.dev` demands the padlock and the free padlock hadn't been minted yet, the browser assumed the worst and slammed the door. I sat there refreshing, being warned off my own blog like it was a scam.

Then it went green. GitHub had noticed the domain was mine and quietly issued a real HTTPS certificate for it — automatically, for free, from Let's Encrypt, a nonprofit that gives them away — and it renews itself from here on. The exact thing IONOS wanted to sell me every year, GitHub handed over for nothing while I watched.

So I cancelled the certificate pack.

What I was left with: my own domain, not a spare room in someone else's house. The padlock, free and self-renewing. Not a single ad on my words. And that same shark, shrunk to twenty pixels, even sits in the browser tab now as the site's little icon.

## Open means everything

Here's the catch, said straight, because it's the whole point.

GitHub gives you all of this — the hosting, the certificate, the traffic your site serves — and asks for exactly one thing in return: that everything is public. Not just the finished pages. The Markdown behind them. The script that builds them. Every edit I've ever made to any of it. Open source means open source, and open source means *everything* — the tooling and the page, all of it, out in the open where anyone can read it, copy it, or laugh at it.

That's the trade. You give up any expectation of privacy, and the infrastructure costs nothing.

A blog is writing I'm already handing to strangers. Making the posts public isn't a price — it's the job. And the little script that stitches them together? I had no reason to hide that either; if anything, someone might want it.

If you want a private blog, you can stick to WordPress, or home-grow your own. But if you want global availability, free hosting, free everything — then GitHub is the best.

## Steal me

If you want proof of everything I just said, it's the site itself. The blog you're reading, the little script that builds it, every edit I've ever made to any of it — all of it sits in one public repository — a project folder with its full history — at [github.com/scriptease/scriptease.dev](https://github.com/scriptease/scriptease.dev). Nothing behind a login, nothing held back. Open it, read it, or take the script and point it at your own folder of writing. That's the whole deal, and it's the same one for anyone willing to work in the open.
