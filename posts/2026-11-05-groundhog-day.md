---
title: "Groundhog Day"
url: "https://scriptease.dev/posts/2026-11-05-groundhog-day/"
author: "Scriptease"
created: "2026-11-05"
published: "2026-11-05T16:16:16+01:00"
description: "In September I built a plugin on a Claude Code feature that didn't officially exist yet. It's official now, under a new name. When I came back to it, it turned out that everything I'd given it to remember, it had forgotten. And it would forget it again. So I rebuilt it."
tags: ["ai", "claude", "security", "plugins", "agent", "saga"]
---

# Groundhog Day

_The [Eyes Closed saga](https://scriptease.dev/sagas/#eyes-closed): [1. Redacted](https://scriptease.dev/posts/2026-09-05-redacted/) · 2. Groundhog Day · [3. A Skill Issue](https://scriptease.dev/posts/2026-11-07-a-skill-issue/) · [4. Cascading Redactions](https://scriptease.dev/posts/2026-11-15-cascading-redactions/)_

In September I built a plugin on a Claude Code feature that didn't officially exist yet. It's official now, under a new name. When I came back to it, it turned out that everything I'd given it to remember, it had forgotten. And it would forget it again. So I rebuilt it.

## It has a name now

The plugin is called redact. In [Redacted](https://scriptease.dev/posts/2026-09-05-redacted/) I built it on a hidden switch in Claude Code, the AI I work with on my Mac: a way to change how Claude itself behaves. When a password or an email address shows up, the plugin swaps it for a placeholder like `REDACTED_EMAIL_1`. When the AI later uses that placeholder in a command, the plugin puts the real value back. The AI never holds the secret. The command still works.

Back then my research agent told me the feature didn't exist. Two months later it does. The switch is gone, the feature is on for everyone, and it has a name: mods.

This morning I asked my AI to find my old post, the plugin, and the official documentation, and to tell me one thing: does it work with the way I work now?

## Every morning it forgets

I work in T3 Code, an app where I run my AI conversations side by side, one per task, from my laptop or my phone. T3 Code tries to keep Claude running, but it doesn't promise to. An update or a restart of T3 Code, and Claude starts fresh with the saved conversation handed back to it. And I want to come back to a conversation hours or days later and carry on, restart or not.

The plugin kept its secrets only as long as Claude was running. Claude restarts, secrets gone.

The conversation still said `REDACTED_DB_PASS`. The plugin had no idea what that meant anymore, so the command got the placeholder instead of the password and failed. Nothing leaked. It just broke.

The plugin had redacted my secrets so well that it had forgotten them. Every morning it woke up, read a conversation full of placeholders, and recognized none of them.

## Stuck with 500 entries in my keychain

The AI's first idea was the Mac's Keychain, the password vault built into every Mac: one entry per secret.

I've built this plugin for database work. A single lookup in our customer database can return 500 customers, and 500 email addresses. That would be 500 entries in my keychain. One entry per conversation, then? The AI found the catch there: every read and write would hand the secrets to a Keychain command, and while it runs, any other program on the Mac can see them in the list of running programs. Hidden from the AI, on show to everyone else.

We settled on one master key in the Keychain, total. The secrets go into a file, locked with that key.

Claude Code keeps every conversation as a file on disk, with a folder of its own next to it. I asked to put the locked secrets right there, next to the conversation they belong to. Move the conversation, the secrets move with it. Copy it, and the plugin refuses to guess which copy is real. Delete it, and the secrets go too.

Then I thought about how I could break it.

Writing all the secrets down takes time. Stop Claude halfway through, and the locked file can't be unlocked at all. Every secret, gone. So the plugin now writes a fresh copy next to the old one and swaps it in with one move. A reader sees the old file or the new one, never half of one.

Mods come with a small set of security features of their own. They weren't enough to lock the file, so the plugin hands that job to `openssl`, the encryption tool that ships with every Mac.

## Catch it when it enters

Until then the plugin recognized secrets by their shape: an email looks like an email, and many keys come in well-known shapes and sizes. A key with no famous shape got through.

I had an idea about that. Secrets usually travel with a label. A web request carries its key in a labelled line, called a header, that starts with `Authorization:`. A settings file says `API_KEY=` right before the value. "If the header field could be used to identify a secret, then it would be masked… then we would catch it when it enters."

That's how it works now. The first time a value appears next to a name like that, the plugin remembers it, and from then on it's masked everywhere, label or not.

Then I wanted to see if my secrets were safe from the AI. I asked for a script that runs the detector over my key file line by line and prints only whether a line would be masked, never the line itself. The AI never read the file.

Every line with a password or key was masked except one: a key for Jira, the work-tracking tool, whose label didn't say "key". Jira's keys all start with `ATATT3`, and nobody had told the detector. One new pattern, and that line went dark too.

## Sharp knives

Along the way the AI tightened things I hadn't asked for. Placeholders would no longer be turned back into real values when they went to another AI. Fine. It also added a line telling the AI never to put placeholders into messages meant for people.

I thought about a normal day. Someone asks me to look up an order, and I want the AI to post the customer's email address in our chat. With that rule, the AI would refuse.

"My philosophy is, I want to give people sharp knives, because that means, yes, you can cut yourself, if you're doing the wrong thing, but it also doesn't make something impossible."

The line came out. Now the only thing that still gets placeholders is a handoff to another AI. Everything that goes to a person gets the real value.

## Better call Sol

By then the plugin had a test suite, a set of automatic checks: sample secrets and harmless bits of text, each one either masked or kept. Then I handed it to Sol.

Sol is [my review loop](https://scriptease.dev/posts/2026-10-28-better-call-sol/): a second AI from a different company reads the work and lists what's wrong, my AI writes a test that fails for each finding, fixes it, and sends it back. Up to five rounds.

The first round came back with a list. The worst finding was about the guard itself. When a mod crashes, or takes too long, Claude Code skips it and carries on. For most mods that's polite. For mine it meant the secret walked straight past. And some of my patterns were slow enough to trigger it on a few pages of text.

A guard that steps aside when it gets confused. Now it blocks instead: if the plugin can't check a message, the message doesn't go.

Sol never got to approve it. The last fix came after the fifth round, and five is the limit.

## I got you, babe

Then the real test, the one this morning was about. I opened a new conversation in T3 Code on my phone and gave it a fake password. The AI used it in a command, and the command got the real password. I restarted Claude and T3 Code, came back, and asked again.

It still worked. The plugin had found its file, unlocked it, and remembered.

The same test also showed where it can't help. T3 Code had named the conversation after my first message, the fake password in plain text. I didn't mind. I don't plan to type secrets into the chat. What I'm guarding against is an accident: a search through a settings file or a database lookup that pulls in a password, and an AI that then tells me, helpfully, that it just read a password.

Every morning in Groundhog Day, Phil wakes up to the same song, I Got You Babe, and the whole town has forgotten yesterday. Phil hasn't. Now my plugin remembers like Phil, after every restart.

Even the secrets, in all my conversations… with Claude.

Here is [the plugin](https://github.com/scriptease/claude-code-redact-plugin), and here are [the official docs for mods](https://code.claude.com/docs/en/plugins/mods/overview).
