---
title: "Good Ideas Never Die"
url: "https://scriptease.dev/posts/2026-08-28-good-ideas-never-die/"
author: "Scriptease"
created: "2026-08-28"
published: "2026-08-28T12:25:55+02:00"
description: "I showed a friend the VS Code extension I had just built. 'That's funny,' he said. 'I already use this. And you told me about it two years ago.'"
tags: ["ai", "programming", "vscode"]
---

# Good Ideas Never Die

I showed a friend the VS Code extension I had just built.

"That's funny," he said. "I already use this. And you told me about it two years ago."

## I no longer write code. I read it.

My job has changed. AI writes most of my code now. I spend more of my time reading what it wrote: following a value through a program, checking which parts call which other parts, and making sure the whole thing says what we meant.

The tools around me had not caught up. A normal code editor is built around files and folders because that is how code is stored. I wanted to browse by meaning: show me everything concerned with orders, or everything that talks to an outside system, even when those pieces live in different folders.

So I asked an AI model called ox-alpha to build me a source-code browser for one of our servers. It scanned 508 files and turned them into one self-contained web page. I could enter through features, architecture layers, recurring patterns, or dependencies, then move between those views without losing the file I was reading.

We kept working on it. Source code opened inside the page. A click on a file showed both the code and every file connected to it. Search looked through all 508 files and jumped to the matching line. Imports, the long list of other code a file uses, started collapsed so the actual work appeared first.

After the file icons and navigation landed, I wrote: "This is perfect :D."

Seven minutes later, after code search landed: "This is the best thing ever!"

The browser was becoming the editor I needed now that reading had replaced writing.

## Then I remembered Polychromatic

The source view worked, but its colors still described the grammar of the programming language: keywords in one color, text in another, types in a third. That tells you what each word is. It does not help much when you are trying to follow one particular name through a page of code.

I remembered an old Xcode plugin called [Polychromatic](https://github.com/kolinkrewinkel/Polychromatic). Xcode is Apple's programming environment, and the plugin had stopped working years ago. I checked out its source code so I could give it to ox-alpha.

That is how I work now. I get the code, or let the AI get the code, and let it use the original instead of making me describe the implementation from memory.

Polychromatic gave every identifier, every variable, property, and function name, its own stable color. The same name got the same color wherever it appeared. Types faded into the background. The names carrying data and behavior came forward.

Ox-alpha read the source, found the small formula that turned a name into one of 4,096 colors, and carried it into the source browser's HTML formatter.

Polychromatic always felt a little like seeing the Matrix. Instead of seeing the structure of the code, you see the flow.

## This should not stay at work

The source browser was built around one private project. I could use it, but I could not hand it to anyone outside work.

Two days later I had another thought: the coloring did not have to remain inside that browser. Visual Studio Code, a widely used editor, already understands which words are variables, properties, functions, and methods. An extension could take that information and apply Polychromatic's stable colors to any supported language.

I had never built a Visual Studio Code extension. My first question to the AI was: "Can you do a web search on how to implement a template in Visual Studio Code? I have actually no idea."

It turned out not to be a template at all. We needed an extension. We built it, tested it, packaged it, installed it, and put it on GitHub. The private browser had produced a small public tool: [Polychromatic for VS Code](https://github.com/scriptease/polychromatic-vscode).

Then I showed it to my friend over a Slack screen share.

## You told me about it two years ago

"That's funny," he said. "I already use this. And you told me about it two years ago."

We looked up the extension he had installed. It was called [Color Identifiers](https://marketplace.visualstudio.com/items?itemName=MatthewNespor.vscode-color-identifiers-mode). It already gave identifiers stable colors in Visual Studio Code.

Then I remembered. He was right. I had recommended it to him.

I had remembered Polychromatic, the original Xcode plugin. I had remembered what it changed about reading code and why I liked it. I had remembered the Matrix. What I had forgotten was the name of the Visual Studio Code extension that already carried the same idea forward, and that I had already found it and told someone else to use it.

The product name disappeared. The idea survived intact.

## Good ideas never die

Before AI, I found things I liked and told my friends about them.

Now I build things I like, show them to my friends, and they tell me I already recommended the same thing two years ago.

AI shortened the distance between remembering an idea and making it real. It did nothing for my memory.

Good ideas never die. Sometimes I just rebuild them.
