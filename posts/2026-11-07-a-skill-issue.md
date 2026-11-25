---
title: "A Skill Issue"
url: "https://scriptease.dev/posts/2026-11-07-a-skill-issue/"
author: "Scriptease"
created: "2026-11-07"
published: "2026-11-07T12:08:35+01:00"
description: "I found the bug. I fixed it. I sat down to blog about it, and it happened again."
tags: ["ai", "claude", "skills", "plugins", "debugging", "saga"]
---

# A Skill Issue

_The [Eyes Closed saga](https://scriptease.dev/sagas/#eyes-closed): [1. Redacted](https://scriptease.dev/posts/2026-09-05-redacted/) · [2. Groundhog Day](https://scriptease.dev/posts/2026-11-05-groundhog-day/) · 3. A Skill Issue · [4. Cascading Redactions](https://scriptease.dev/posts/2026-11-15-cascading-redactions/)_

I found the bug. I fixed it. I sat down to blog about it, and it happened again.

## Something broke

A few days earlier I was improving the AI that reviews code at work, and I wanted a second opinion before shipping it. So I called Sol. Sol is [my review loop](https://scriptease.dev/posts/2026-10-28-better-call-sol/): a second AI from a different company reads the work and lists what's wrong.

Sol didn't pick up. All I got back was one line: `Launching skill: better-call-sol`.

My AI took that as a good sign: "The review by Sol is running."

It was not. Almost an hour later I typed two words into my phone: "Something broke".

Sol lives in a skill. A skill is a note with instructions for an AI, stored on a shelf with just a label. Asking for one gets back an envelope: the label on the outside, the note inside.

This time the envelope came back empty. Once I complained, my AI opened the note file by hand and ran the review the long way round. Sol approved in the end.

## The usual suspects

It had happened once before, so I spun up a fresh AI to find out who to blame. "Is this a T3 Code issue? Is this a Claude Code issue?" T3 Code is the app I run my AI conversations in; Claude Code is the coding assistant inside it.

I thought two connections had dropped and come back just as the skill failed. Three suspects, all with motive.

The digger ruled out the dropped connections first: they happened almost an hour later, right when I sent "Something broke".

Then it read every skill request in every conversation I'd saved. The failures started one afternoon some days earlier. Not twice: almost twenty times. Most of them were the skill that talks to Jira, the work-tracking tool, and every time the AI had simply carried on without its instructions. I'd noticed twice.

And every one of them had happened in T3 Code, all on the same version. Suspect number one, caught red-handed. Except it was a coincidence: I hadn't updated T3 Code since the day the trouble started, and I'd been working in nothing else.

## "Reduction hook, comes from me"

Something had started rewriting the answers my AI got back. The digger followed the trail to a plugin installed that afternoon.

I knew that plugin. I wrote it. It's redact, the one from [Groundhog Day](https://scriptease.dev/posts/2026-11-05-groundhog-day/), which hides my passwords from my AI by swapping them for placeholders. That post ended with me installing it everywhere: "Even the secrets, in all my conversations… with Claude."

All my conversations. That line was the bug going live.

I sent the digger a voice message: "Reduction hook, comes from me."

Gamers have a reply for anyone blaming the game: it's a skill issue. It means the problem is you. Mine was a skill issue in both senses, and I was mostly relieved: "It's good to know that if it causes some issues that it's not a T3 code thing."

## The missing skill

My plugin checked every answer my AI got back and masked anything that looked like a password. Then it copied the label onto a fresh envelope and passed that on.

The note stayed behind in the old one, even when there was nothing to mask.

The fix: if there's nothing to mask, pass on the original envelope, note and all.

If there *is* something to mask, the note still stays behind. The plugin never read it, so it could carry the very password the plugin just blacked out on the outside. A missing note is annoying. A leaked password can't be taken back.

The proof was one question to a fresh AI with the plugin switched on: did the note arrive? The old version said `NOT_LOADED`. The new one said `LOADED`. Done.

## Third time's a charm

Then I opened a new conversation to write this post, and my AI reached for the blog note.

`Launching skill: blog`

No note. The fix wasn't installed yet. I told the AI that fixed it to install it and to send the blogging conversation a message: it's fixed, try again.

The envelope was still empty.

A running conversation keeps the plugin it started with. The digger had seen it days earlier without either of us noticing: the last note that arrived after I first installed redact came from a conversation that had started before it. Same rule, other direction.

While I waited, I asked one more question: could the plugin just leave skills alone? The answer was no, and the reason was another bug.

When my AI asks for a note, it can add a line of its own: "use this password", with the password still a placeholder. My plugin put the real password back, as it would for a tool that needed the password to do its job. But this letter had the same sender and recipient. The line goes into the note, and the note comes straight back to my AI. The plugin was mailing my AI the very password it was hiding from it.

One last fix. One restart of T3 Code. Then I asked my AI a third time, and finally, the note arrived.

I can finally blog about it.

When I started, I thought the title A Skill Issue was way too corny, and that nobody would write about one skill that wouldn't load.

It turned out to be a gold mine.
