---
title: "The Fork I Was Happy to Delete"
url: "https://scriptease.dev/posts/2026-07-12-the-fork-i-was-happy-to-delete/"
author: "Scriptease"
created: "2026-07-12"
published: "2026-07-12T09:23:44+02:00"
description: "This spring I spent weeks patching a dictation app until it behaved. This morning I threw all of that work away — and it was the best upgrade I've made this year."
tags: ["voice", "ai", "opensource", "macos", "saga", "whisper"]
---

# The Fork I Was Happy to Delete

_The [Whisper saga](https://scriptease.dev/sagas/#whisper): 1. The Fork I Was Happy to Delete · [2. Voice Input Revisited](https://scriptease.dev/posts/2026-09-20-voice-input-revisited/) · [3. A Team of Strangers](https://scriptease.dev/posts/2026-09-26-a-team-of-strangers/) · [4. Who Signs for Claude?](https://scriptease.dev/posts/2026-10-01-who-signs-for-claude/)_

This spring I spent weeks patching a dictation app until it behaved. This morning I threw all of that work away — and it was the best upgrade I've made this year.

I barely type to my computer anymore. Most of my working day is a conversation with AI agents — programs that can dig through files, run tools, and build things while I steer. Speaking is simply faster than typing: hold a key, talk, release, and the words appear in the terminal, the plain text window where I work. When the loop works, it feels like thinking out loud and having the thoughts executed.

It took four stages of trust to get here. In the beginning I typed my prompts carefully, like little letters. Then I realized the AI doesn't care about typos, and stopped fixing them. Then I started dictating, but proofread every transcript before sending. Today I dictate and press send without looking at the text at all — my agents carry a standing instruction that everything I say arrives through speech recognition, and that decoding what I meant is their job, not mine.

## The word problem

When the loop works. The catch is vocabulary. Speech recognition learns from enormous piles of recorded speech, so it's good at common words and hopeless at private ones — and my workday is full of private ones. My employer's name is a made-up compound word no dictionary contains, and the recognizer would confidently write it as whatever real words sounded closest. ChatGPT arrived as "JetGPT". A delivery platform we work with came out as two innocent English words. My agents learned to translate the garble back from context, the way you decode a friend's typos. But numbers have no context to save them: the day "0.9" arrived as "20.9", I stopped finding it charming.

## Three apps and a fork

I got here through three apps. I started where the YouTube videos point everyone: Wispr Flow. I really liked it. But serious use burned through the free weekly word budget almost immediately, the paid plan costs around ten euros a month, and your voice is sent over the internet to someone else's servers to be turned into text. For a tool I press a hundred times a day, I wanted it free, private, and running on my own machine.

I found OpenWispr: the same magic, but open source — code that's public, free to use, and free to change. It handed me a dilemma, though. The small speech models kept getting my words wrong. The large model got the words right — and on my old M1 MacBook took a two-second pause to think. Two seconds sounds small until you pay it on every sentence. Then you use the tool less without ever deciding to.

So I moved on to Ghost Pepper, another local dictation app, which closed the accuracy gap with a second, tiny AI proofreader that cleaned up the transcript after the fact. But Ghost Pepper fought me too. It was sluggish to start listening. It quarrelled with the clipboard — the invisible shelf your computer uses for copy and paste. And it had a well-meaning feature that paused your music while you spoke, which misfired and *launched* the Music app instead. There is a special kind of rage reserved for software that starts playing music while you're mid-sentence with a computer.

So I did what open source invites you to do: I forked it. A fork is a photocopy of someone else's recipe that you're allowed to scribble on. I ripped out the music feature, removed the part that checks for new versions, cut the artificial delays, and made the whole thing snappier. Only now do I see the punchline: I fixed Ghost Pepper's clipboard by transplanting code from OpenWispr, the app I had just left. My final commit message — the little note a programmer attaches to a saved change — reads like a mission statement: "Disable accessibility delay, speed up and remove update checker."

The fork worked. It was fast, it was quiet, it was mine. But it still ran a small speech model, so the vocabulary problem stayed.

## One model for both ears

In May, a separate problem forced the answer. I also send voice messages to my agents through Discord, a chat app, when I'm away from the desk — and that path needed speech recognition too. Research came back with a clear winner: Whisper large-v3-turbo, a big model that understands me switching between German and English mid-sentence, at six times the speed of the older large version. One recommendation stood out: use *one* shared model for everything, so both ears of the system hear the same way. The Discord side got the good model that week. My dictation fork kept limping along on the small one.

## Why do my voice messages hear better than my desktop?

Then came this morning. I had spent it dictating three blog posts — getting old war stories out of my head and onto the page — much of it as voice messages through Discord, and the transcripts came back so clean I kept noticing. At some point the obvious question surfaced: why do my voice messages hear better than my desktop? And then I remembered: both are built on the same engine — whisper.cpp, the open-source program that actually runs these speech models. Same engine, same models. The good one was already sitting on my disk; my desktop just wasn't using it. So I updated OpenWispr and gave my old starting point another shot.

I told my agent, roughly: find where the Discord voice settings live, and set up OpenWispr with the same model. It found the settings and pointed OpenWispr at the very same 1.5-gigabyte model file the Discord side already used — one model, two doors. I dictated a test sentence full of my weird tool names. Three out of four came through perfectly. The payment provider's name still came back as separate letters.

## The setting that wasn't there

I had come for the model, nothing more. But digging through OpenWispr's manual for that last name, my agent surfaced a feature I hadn't even known to wish for: a glossary. You can hand Whisper a page of hints before it listens — names, spellings, private vocabulary — and it leans toward those spellings. We added the company name, the tools, the platforms. I dictated the test again.

It got *worse*. Words that had been correct ten minutes earlier came back mangled.

A year ago, that would have cost me an evening. Instead, my agent pulled the readable text out of the installed app and searched it for the glossary setting. It wasn't misconfigured. It was absent. The version I had installed simply didn't contain the feature yet, and silently ignored the setting. The glossary had shipped in the *next* release, six days ago, and my package manager — the installer tool that fetches apps for developers — was still serving the old version. One upgrade later, the glossary was live.

I dictated the test sentence a third time. Sixteen technical terms out of sixteen, correct. The made-up company name, spelled right, for the first time ever. Then I tried German — it caught the language switch without being told, and wrote "185" as digits instead of spelling it out.

## Winning by deleting

Then I realized: both reasons my fork existed — the better model and my private vocabulary — now lived upstream, in the original project I had copied from. And the two-second toll that drove me away from OpenWispr in the first place was gone too: the model got faster, and my newer M5 laptop is simply stronger than the old M1. My patched Ghost Pepper had nothing left to do. I retired it. Weeks of my own careful work, obsolete, and the correct emotional response was relief. In open source you sometimes win by deleting your fork: the river you stepped out of has caught up with you, and rejoining it means every future improvement arrives for free.

One spooky footnote, because a frictionless ending would be a lie. The glossary raises the odds of *all* its words, so once — exactly once — I said "Obsidian" and the transcript said "ChatGPT". Not a garble. A perfectly fluent, perfectly wrong word. A mangled word announces itself; a substituted one reads clean and flips the meaning. So my agents now check whether a name makes sense in the sentence, not just how it's spelled. The safety net moved from spelling to meaning; it didn't disappear.

## So what

Here's what stays with me, beyond the dictation. The whole repair happened in short spoken loops: change one thing, test it, look inside the app, upgrade, test again — the agent doing the digging while I kept talking. Trying a different setup used to cost a weekend and enough friction that you'd talk yourself out of it. Now it costs minutes, so you just try. Like I keep saying: if you can dream it, you can build it.

And the request to write this very article? Dictated. Jenkins, Gerrit, Jira, Redmine, Obsidian, Maestro — six weird tool names — every one landed correctly on the first try.
