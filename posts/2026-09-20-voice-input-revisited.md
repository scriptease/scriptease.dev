---
title: "Voice Input Revisited"
url: "https://scriptease.dev/posts/2026-09-20-voice-input-revisited/"
author: "Scriptease"
created: "2026-09-20"
published: "2026-09-20T09:41:23+02:00"
description: "I asked my AI to build a plugin for the newest speech model I'd heard about that morning. It came back: done, everything streams, just start it on your GPU box. I don't have a GPU box."
tags: ["voice", "ai", "opensource", "macos", "localai", "saga", "whisper"]
---

# Voice Input Revisited

_The [Whisper saga](https://scriptease.dev/sagas/#whisper): [1. The Fork I Was Happy to Delete](https://scriptease.dev/posts/2026-07-12-the-fork-i-was-happy-to-delete/) · 2. Voice Input Revisited · [3. A Team of Strangers](https://scriptease.dev/posts/2026-09-26-a-team-of-strangers/) · [4. Who Signs for Claude?](https://scriptease.dev/posts/2026-10-01-who-signs-for-claude/)_

I asked my AI to build a plugin for the newest speech model I'd heard about that morning. It came back: done, everything streams, just start it on your GPU box. I don't have a GPU box.

## Some words it would always mess up

Ten weeks ago I wrote about deleting my private copy of a dictation app and going back to OpenWispr, the open-source app that turns my voice into text. The glossary feature had landed, my private vocabulary was finally getting through, and the story had a neat ending. The ending was mostly true.

I don't read my transcripts before sending them anymore. My agents know everything arrives through speech recognition, and decoding what I meant is their job. Most of the time this works. Sometimes the substitutions give me a chuckle -- like "vault" being constantly replaced by "world" -- two very similar words.

The other thing was the pause. The Whisper model underneath OpenWispr only starts working after you stop talking. And you feel every second you have to wait. This was the exact trade-off that sent me from OpenWispr to Ghost Pepper and back again: you're always paying quality for latency or latency for quality, and whichever side you pick, the other one nags.

## Whisper isn't Whisper

In September I asked my research automation to look into "Qwen3-ASR", a newer speech model that was beating Whisper on benchmarks. The answer closed the door: the model could not plug into the way my dictation app was built. Not "hard to swap in". Impossible. In order to try it, I'd need a different program to drive it.

## Trying out a new Whisper

TypeWhisper is that different program. Same idea -- hold a key, talk, text appears -- but with a plugin architecture. Third-party engines slot in without touching the app's own code. It already shipped a Qwen3-ASR plugin. I tried it. The transcription quality was noticeably better than I expected -- cleaner on technical terms, fewer phantom words.

But it didn't support a glossary. TypeWhisper has a dictionary feature for spelling corrections, but the Qwen3-ASR plugin didn't send the glossary to the model. My company name went back to being two innocent English words. After the July saga, glossary support wasn't a nice-to-have anymore. It was the line.

## "Just start it on your GPU box"

That same morning I'd seen a new model mentioned online: Confucius4-R2T2. Streaming speech recognition -- the kind where text appears while you're still talking, not after you stop. Two billion parameters, built by NetEase's research lab. No existing TypeWhisper plugin for it.

So I asked my AI to build one. It checked -- no plugin exists. It read TypeWhisper's plugin documentation, read the R2T2 model's documentation, and wrote a Swift plugin from scratch. Tests passed. Everything streamed. Then it told me how to start the server: a Python process that needs a CUDA GPU.

CUDA is Nvidia's toolkit for running heavy computation on their graphics cards. I have a MacBook. No Nvidia card. No GPU box. No server rack in the basement. The plugin was technically perfect and practically useless. I told the AI to scrap it.

## Selecting a new model

Here's the thing about popular AI models: they get repackaged. The same R2T2 model had been converted to GGUF -- a compressed format that runs on anything, including a Mac's own chip -- exactly one day earlier. One day. No wonder there was no plugin for it yet.

I told the AI: forget the Python server, use this instead. It rewired the plugin to talk to a small program running on my Mac that runs the GGUF model on the Mac's own graphics chip. I held the key and talked.

Text appeared while I was still speaking.

## Vault is vault not world

It worked. Text appeared while I was speaking, the streaming felt immediate, and the transcription was clean. Then I noticed what was missing: the glossary. The plugin didn't pass TypeWhisper's dictionary through to the model. It messed up the words again.

Make it work, then make it right.

So I built that too. The plugin now reads the dictionary and passes it to R2T2 as a prompt -- a hint that biases the model toward your spellings. I imported my sixteen terms from OpenWispr: the company name, the tools, the platforms.

I dictated a sentence full of project names, every one landed -- even the usual suspect "vault".

With Whisper, you speak into silence and wait for the result. With R2T2, the words chase your voice -- a fraction of a second behind, refining as they go. By the time I release the key, the model is almost done. The dead pause is gone.

It even works when I switch languages mid-sentence.

## My new stack

The setup is three things now: audio.cpp, a small local program running the R2T2 model; a Swift plugin that talks to it; and TypeWhisper, the app that hosts the plugin. Every part does its thing, and I can switch out the model when a new one comes along.

Last time I won by deleting my private copy and going back to the original project. This time I won by building something new -- but on top of a plugin system instead of inside someone else's app. A fork is stitched into the thing it copies. A plugin clicks in and clicks out. I can delete this one too, and nothing else breaks.

This article was dictated through the setup it describes. Every technical term in it landed correctly while the words were still chasing my voice. Even my AI noticed.

## Steal this

The plugin is out: [scriptease/typewhisper-r2t2-plugin](https://github.com/scriptease/typewhisper-r2t2-plugin). You'll need audio.cpp, the small program that runs speech models on a Mac's own graphics chip -- build it, hand it the R2T2 model file ([the GGUF conversion](https://huggingface.co/davidxifeng/Confucius4-R2T2-gguf), in the Q8_0 size), and it waits for audio in the background. The plugin itself is a `R2T2Plugin.bundle` in the release page: unzip and drop it in TypeWhisper's plugin folder, restart the app (1.7.0+ required), pick Confucius4-R2T2. The plugin is self-signed, so macOS needs to stop treating it as suspicious. The README has more info.

For the glossary, put your own words in TypeWhisper's dictionary and the plugin passes them to the model as a hint. That's the part that needed [a change in audio.cpp itself](https://github.com/0xShug0/audio.cpp/pull/618), merged the same day. 

Just add your own words or not, and hold the key and talk.
