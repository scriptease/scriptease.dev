---
title: "A Team of Strangers"
url: "https://scriptease.dev/posts/2026-09-26-a-team-of-strangers/"
author: "Scriptease"
created: "2026-09-26"
published: "2026-09-26T09:35:23+02:00"
description: "I've never met most of my team. One made the model, one ported it, one shrank it, one merges the code, one tested it in Andalusian Spanish. I learned who most of them were from a page my AI kept."
tags: ["voice", "ai", "opensource", "github", "saga", "whisper"]
---

# A Team of Strangers

_The [Whisper saga](https://scriptease.dev/sagas/#whisper): [1. The Fork I Was Happy to Delete](https://scriptease.dev/posts/2026-07-12-the-fork-i-was-happy-to-delete/) · [2. Voice Input Revisited](https://scriptease.dev/posts/2026-09-20-voice-input-revisited/) · 3. A Team of Strangers · [4. Who Signs for Claude?](https://scriptease.dev/posts/2026-10-01-who-signs-for-claude/)_

I've never met most of my team. One made the model, one ported it, one shrank it, one merges the code, one tested it in Andalusian Spanish. I learned who most of them were from a page my AI kept.

## "Sometimes it takes ten seconds or more"

Last time I ended on the dead pause being gone. I'd switched to R2T2, a speech model that writes while you talk instead of after you stop, and the words chased my voice a fraction of a second behind.

Mostly. Every now and then, after a long sentence, I let go of the key and nothing happened. The graphics chip sat at 100%, and ten seconds later the text arrived all at once. The pause was back, and it was worse than the one I'd left.

We had tried the obvious knobs. Longer listening windows made it slow. Shorter windows made it worse.

## Rereading everything

The model listens in slices of a third of a second. For each new slice it went back and re-listened to everything I had said so far, from the first word. Imagine writing a letter where you reread the whole thing from the top every time you add a word. The first line is fine. By the second page you're falling behind.

That's what happened. Once re-listening took longer than the slice it was listening to, the slices piled up in a queue. When I stopped talking, the model was still working through my last ten seconds. Shorter slices meant more rereading.

The fix was to remember. The model hears audio in four-second blocks, and a finished block never changes, so its work can be kept and only the unfinished tail redone. On a one-minute recording, the wait after the last word went from 24.9 seconds to 0.37.

I tried it on myself first: "I dictated for over a minute and it immediately returns like I wanted it to."

## "I don't want to bulldoze over his code"

Then I went to send the fix back and found someone had got there first.

R2T2 runs on my Mac through audio.cpp, an open-source program that runs speech models on the Mac's own graphics chip. A developer named David Feng had brought R2T2 into audio.cpp, and he had also packed the model into the file format my setup uses. His own copy of the project had a branch, a side version of the code, with the same three ideas as mine, written two days earlier, with stricter safety checks. He'd never sent it in.

I could have sent mine straight to 0xShug0, who maintains audio.cpp. What I told my AI was: "I don't want to override his intentions and basically bulldoze over his code." David's copy had no place to file an issue, so I sent my fix to him directly, as a draft: here's mine, yours is better, how do you want to do this?

Then nothing. He had also gone quiet after the maintainer reviewed another change from him.

## We kept everything in a note

This team has no office, no chat and no meetings. It's a scatter of discussions across GitHub, where the code lives, and Hugging Face, where the models live. Nobody reads all of them.

My AI does. That first night I asked it to write everything into a note in my Obsidian vault, the folder where I keep my notes. It had been keeping its own private memory too, and I dictated back: "You can remove the memory. I don't need it. The Obsidian void is the memory."

That note started at 38 lines. It's 111 now, and it links 15 discussions across five projects: who asked what, who answered, who went quiet, and what we're waiting on. When I asked it to check for anything new, it read the discussions, checked them against the note, and answered from both.

## A week in AI is like a month

Four days later I released version 0.2.0 of my plugin with my fixed server inside. The release notes said plainly that it came from my copy, not the official one.

By then I wasn't the only user. A colleague, hooked by my rambling about it, had installed it and battle-tested it in Andalusian Spanish. The model nailed it, no issue whatsoever. So I asked my AI whether it was time to go over David's head. "It's also like a week, and in a week in AI is like a month."

It said yes, with conditions: tell David first, credit his work, link his branch, and offer to close mine the moment he wants to send his. So I opened a pull request, a proposed change the maintainer can accept or reject, and dictated why I cared: "Somebody else can find the PR and get their bug fixed. So it's basically spreading the idea how to fix the bug. I don't care if it gets merged. That's a lie. I care a little bit that it gets merged."

## Details added by Claude

That same afternoon the note turned up a stranger. Someone called NairoDorian had shrunk R2T2 to half its size, 1.2 gigabytes instead of 2.5, and reported it ran about 20% faster with no loss in quality. Shrinking a model like this is called quantizing. You store every number in the model with fewer digits, like rounding prices to the nearest euro.

My AI downloaded it, and audio.cpp refused to load it. A check in the code allowed only the bigger model files. My AI's advice was to wait for the person who made it to fix audio.cpp.

I didn't want to wait. If rebuilding was five minutes of work, I could test the stranger's model and tell them what fixed it. It was one line. It ran, so I dictated a thank-you through it: "I transcribed the very text you're reading right now using your quant, and the only fix that's needed is to allow your quant."

My AI turned that into a nicer comment, full of things I had never said. Worse, it still claimed I had dictated every word of it.

"But now it's a lie because you basically put in a bunch of stuffs that I never actually dictated."

We settled on my dictation as spoken, followed by a section headed *Details added by Claude* with the error message and the one-line change. That's what got posted. My plugin's page got a table of all three model sizes that now exist. "It's cool to give people options." I put out 0.2.1 with the smaller model working. "I'm not paying for the traffic GitHub does."

## "Fixed as suggested"

By that night the maintainer had made the one-line change in the official audio.cpp and closed the discussion with three words: "Fixed as suggested."

He also tested my bigger fix, and found a real hole in it. If you start quietly and then speak up, the model adjusts to the new volume. That changes the early audio too. My remembered blocks were remembered at the old volume. In a test with a quiet first eight seconds, 18 of the slices came out different from the original. My shortcut had changed the answer.

The fix was to keep a copy of what each remembered block looked like and compare it every time. If anything changed, redo that block. It cost no speed: the one-minute recording still finished in 36 seconds against 80. At a quarter to four in the morning the change was up and my reply was posted.

That check was exactly the kind David's branch had from the start. The hole the maintainer found was the one the first stranger had already closed.

Meanwhile on Hugging Face, someone had asked David whether the smaller format would work. He answered in Chinese: probably, he just hadn't tested the quality and was short on disk space. Nobody handed out roles. Everybody did one anyway.

## Waiting on audio.cpp

The last section of the note is called *waiting on audio.cpp*. My fix is in front of the maintainer again. The stranger hasn't answered my thank-you yet. David hasn't answered my draft.

My plugin is supposed to disappear. TypeWhisper, the dictation app it plugs into, takes new plugins into its own code, and I've asked in their discussion board how they'd like it. Once everything lands in the official projects, my copy of audio.cpp, my plugin page and my self-built server can all go. The new plugin would download the official audio.cpp and the model size you pick, and start them on its own.

I thought about waiting for the merge before writing this. Then this whole week would have been one section in a post about a finished plugin.

The first time in this saga, I won by deleting my copy. I'm hoping to win the same way again.

## "Great job orchestrating the real world"

_Update, the same evening._

I published this in the morning. By the evening, everyone had answered.

TypeWhisper's maintainer went first. They build and sign community plugins themselves, so mine moves into their code under my own name. I asked the question the last section ended on: could my plugin download the official audio.cpp and start it on its own? Yes, with rules. Pin every download to one exact, checked version, and make sure the server can't outlive the app.

So I asked 0xShug0 the same thing. It was a Saturday. "It's flying, everyone working on the weekend." He said yes: a published release never changes, and the next one is planned for next week.

He also suggested I host the smaller model myself. It wasn't mine to host, so I offered NairoDorian the job. They sent the change themselves, and by the evening their model was on audio.cpp's official list, next to David's.

Ten hours after I decided not to wait for it, my fix was merged. "Merged! Thanks!" I sent my AI one word: "success."

I closed my draft on David's copy with a thank-you pointing at the merged fix, and deleted my copies of the fix. Same win as the first time.

The team of strangers has assembled. The only thing missing is next week's release.

Then the Whisper saga continues.
