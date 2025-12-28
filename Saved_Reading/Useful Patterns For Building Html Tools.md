---
saved_date: 2025-12-28T22:04:31.202Z
title: "Useful patterns for building HTML tools"
---

# Useful Patterns For Building Html Tools

# [Simon Willison’s Weblog](/)

 [Subscribe](/about/#subscribe)       
## Useful patterns for building HTML tools

 
10th December 2025

 
I’ve started using the term **HTML tools** to refer to HTML applications that I’ve been building which combine HTML, JavaScript, and CSS in a single file and use them to provide useful functionality. I have built [over 150 of these](https://tools.simonwillison.net/) in the past two years, almost all of them written by LLMs. This article presents a collection of useful patterns I’ve discovered along the way.

 
First, some examples to show the kind of thing I’m talking about:

 
-  **[svg-render](https://tools.simonwillison.net/svg-render?url=https://gist.githubusercontent.com/simonw/aedecb93564af13ac1596810d40cac3c/raw/83e7f3be5b65bba61124684700fa7925d37c36c3/tiger.svg)** renders SVG code to downloadable JPEGs or PNGs
-  **[pypi-changelog](https://tools.simonwillison.net/pypi-changelog?package=llm&compare=0.27...0.27.1)** lets you generate (and copy to clipboard) diffs between different PyPI package releases.
-  **[bluesky-thread](https://tools.simonwillison.net/bluesky-thread?url=https%3A%2F%2Fbsky.app%2Fprofile%2Fsimonwillison.net%2Fpost%2F3m7gzjew3ss2e&view=thread)** provides a nested view of a discussion thread on Bluesky.

  [![screenshot of svg-render](https://static.simonwillison.net/static/2025/html-tools/svg-render.jpg)](https://tools.simonwillison.net/svg-render?url=https://gist.githubusercontent.com/simonw/aedecb93564af13ac1596810d40cac3c/raw/83e7f3be5b65bba61124684700fa7925d37c36c3/tiger.svg) [![screenshot of pypi-changelog](https://static.simonwillison.net/static/2025/html-tools/pypi-changelog.jpg)](https://tools.simonwillison.net/pypi-changelog?package=llm&compare=0.27...0.27.1) [![screenshot of bluesky-thread](https://static.simonwillison.net/static/2025/html-tools/bluesky-thread.jpg)](https://tools.simonwillison.net/bluesky-thread?url=https%3A%2F%2Fbsky.app%2Fprofile%2Fsimonwillison.net%2Fpost%2F3m7gzjew3ss2e&view=thread)  
These are some of my recent favorites. I have dozens more like this that I use on a regular basis.

 
You can explore my collection on **[tools.simonwillison.net](https://tools.simonwillison.net/)**—the [by month](https://tools.simonwillison.net/by-month) view is useful for browsing the entire collection.

 
If you want to see the code and prompts, almost all of the examples in this post include a link in their footer to “view source” on GitHub. The GitHub commits usually contain either the prompt itself or a link to the transcript used to create the tool.

 
- [The anatomy of an HTML tool](https://simonwillison.net/2025/Dec/10/html-tools/#the-anatomy-of-an-html-tool)
- [Prototype with Artifacts or Canvas](https://simonwillison.net/2025/Dec/10/html-tools/#prototype-with-artifacts-or-canvas)
- [Switch to a coding agent for more complex projects](https://simonwillison.net/2025/Dec/10/html-tools/#switch-to-a-coding-agent-for-more-complex-projects)
- [Load dependencies from CDNs](https://simonwillison.net/2025/Dec/10/html-tools/#load-dependencies-from-cdns)
- [Host them somewhere else](https://simonwillison.net/2025/Dec/10/html-tools/#host-them-somewhere-else)
- [Take advantage of copy and paste](https://simonwillison.net/2025/Dec/10/html-tools/#take-advantage-of-copy-and-paste)
- [Build debugging tools](https://simonwillison.net/2025/Dec/10/html-tools/#build-debugging-tools)
- [Persist state in the URL](https://simonwillison.net/2025/Dec/10/html-tools/#persist-state-in-the-url)
- [Use localStorage for secrets or larger state](https://simonwillison.net/2025/Dec/10/html-tools/#use-localstorage-for-secrets-or-larger-state)
- [Collect CORS-enabled APIs](https://simonwillison.net/2025/Dec/10/html-tools/#collect-cors-enabled-apis)
- [LLMs can be called directly via CORS](https://simonwillison.net/2025/Dec/10/html-tools/#llms-can-be-called-directly-via-cors)
- [Don’t be afraid of opening files](https://simonwillison.net/2025/Dec/10/html-tools/#don-t-be-afraid-of-opening-files)
- [You can offer downloadable files too](https://simonwillison.net/2025/Dec/10/html-tools/#you-can-offer-downloadable-files-too)
- [Pyodide can run Python code in the browser](https://simonwillison.net/2025/Dec/10/html-tools/#pyodide-can-run-python-code-in-the-browser)
- [WebAssembly opens more possibilities](https://simonwillison.net/2025/Dec/10/html-tools/#webassembly-opens-more-possibilities)
- [Remix your previous tools](https://simonwillison.net/2025/Dec/10/html-tools/#remix-your-previous-tools)
- [Record the prompt and transcript](https://simonwillison.net/2025/Dec/10/html-tools/#record-the-prompt-and-transcript)
- [Go forth and build](https://simonwillison.net/2025/Dec/10/html-tools/#go-forth-and-build)

 
#### The anatomy of an HTML tool [#](/2025/Dec/10/html-tools/#the-anatomy-of-an-html-tool)

 
These are the characteristics I have found to be most productive in building tools of this nature:

 
1. A single file: inline JavaScript and CSS in a single HTML file means the least hassle in hosting or distributing them, and crucially means you can copy and paste them out of an LLM response.
2. Avoid React, or anything with a build step. The problem with React is that JSX requires a build step, which makes everything massively less convenient. I prompt “no react” and skip that whole rabbit hole entirely.
3. Load dependencies from a CDN. The fewer dependencies the better, but if there’s a well known library that helps solve a problem I’m happy to load it from CDNjs or jsdelivr or similar.
4. Keep them small. A few hundred lines means the maintainability of the code doesn’t matter too much: any good LLM can read them and understand what they’re doing, and rewriting them from scratch with help from an LLM takes just a few minutes.

 
The end result is a few hundred lines of code that can be cleanly copied and pasted into a GitHub repository.

 
#### Prototype with Artifacts or Canvas [#](/2025/Dec/10/html-tools/#prototype-with-artifacts-or-canvas)

 
The easiest way to build one of these tools is to start in ChatGPT or Claude or Gemini. All three have features where they can write a simple HTML+JavaScript application and show it to you directly.

 
Claude calls this “Artifacts”, ChatGPT and Gemini both call it “Canvas”. Claude has the feature enabled by default, ChatGPT and Gemini may require you to toggle it on in their “tools” menus.

 
Try this prompt in Gemini or ChatGPT:

  
`Build a canvas that lets me paste in JSON and converts it to YAML. No React.`

  
Or this prompt in Claude:

  
`Build an artifact that lets me paste in JSON and converts it to YAML. No React.`

  
I always add “No React” to these prompts, because otherwise they tend to build with React, resulting in a file that is harder to copy and paste out of the LLM and use elsewhere. I find that attempts which use React take longer to display (since they need to run a build step) and are more likely to contain crashing bugs for some reason, especially in ChatGPT.

 
All three tools have “share” links that provide a URL to the finished application. Examples:

 
-  [ChatGPT JSON to YAML Canvas](https://chatgpt.com/canvas/shared/6938e8ece53c8191a2f9d7dfcd090d11) made with GPT-5.1 Thinking—here’s [the full ChatGPT transcript](https://chatgpt.com/share/6938e926-ee14-8006-9678-383b3a8dac78) 
-  [Claude JSON to YAML Artifact](https://claude.ai/public/artifacts/61fdecb8-6e3b-4162-a5ab-6720dfe5ed19) made with Claude Opus 4.5—here’s [the full Claude transcript](https://claude.ai/share/421bacb9-54b4-45b4-b41c-a436bc0ebd53) 
-  [Gemini JSON to YAML Canvas](https://gemini.google.com/share/03c1ac87aa40) made with Gemini 3 Pro—here’s [the full Gemini transcript](https://gemini.google.com/share/1e27a1d8cdca) 

 
#### Switch to a coding agent for more complex projects [#](/2025/Dec/10/html-tools/#switch-to-a-coding-agent-for-more-complex-projects)

 
Coding agents such as Claude Code and Codex CLI have the advantage that they can test the code themselves while they work on it using tools like Playwright. I often upgrade to one of those when I’m working on something more complicated, like my Bluesky thread viewer tool shown above.

 
I also frequently use **asynchronous coding agents** like Claude Code for web to make changes to existing tools. I shared a video about that in [Building a tool to copy-paste share terminal sessions using Claude Code for web](https://simonwillison.net/2025/Oct/23/claude-code-for-web-video/).

 
Claude Code for web and Codex Cloud run directly against my [simonw/tools](https://github.com/simonw/tools) repo, which means they can publish or upgrade tools via Pull Requests (here are [dozens of examples](https://github.com/simonw/tools/pulls?q=is%3Apr+is%3Aclosed)) without me needing to copy and paste anything myself.

 
#### Load dependencies from CDNs [#](/2025/Dec/10/html-tools/#load-dependencies-from-cdns)

 
Any time I use an additional JavaScript library as part of my tool I like to load it from a CDN.

 
The three major LLM platforms support specific CDNs as part of their Artifacts or Canvas features, so often if you tell them “Use PDF.js” or similar they’ll be able to compose a URL to a CDN that’s on their allow-list.

 
Sometimes you’ll need to go and look up the URL on [cdnjs](https://cdnjs.com/) or [jsDelivr](https://www.jsdelivr.com/) and paste it into the chat.

 
CDNs like these have been around for long enough that I’ve grown to trust them, especially for URLs that include the package version.

 
The alternative to CDNs is to use npm and have a build step for your projects. I find this reduces my productivity at hacking on individual tools and makes it harder to self-host them.

 
#### Host them somewhere else [#](/2025/Dec/10/html-tools/#host-them-somewhere-else)

 
I don’t like leaving my HTML tools hosted by the LLM platforms themselves for a couple of reasons. First, LLM platforms tend to run the tools inside a tight sandbox with a lot of restrictions. They’re often unable to load data or images from external URLs, and sometimes even features like linking out to other sites are disabled.

 
The end-user experience often isn’t great either. They show warning messages to new users, often take additional time to load and delight in showing promotions for the platform that was used to create the tool.

 
They’re also not as reliable as other forms of static hosting. If ChatGPT or Claude are having an outage I’d like to still be able to access the tools I’ve created in the past.

 
Being able to easily self-host is the main reason I like insisting on “no React” and using CDNs for dependencies—the absence of a build step makes hosting tools elsewhere a simple case of copying and pasting them out to some other provider.

 
My preferred provider here is [GitHub Pages](https://docs.github.com/en/pages) because I can paste a block of HTML into a file on github.com and have it hosted on a permanent URL a few seconds later. Most of my tools end up in my [simonw/tools](https://github.com/simonw/tools) repository which is configured to serve static files at [tools.simonwillison.net](https://tools.simonwillison.net/).

 
#### Take advantage of copy and paste [#](/2025/Dec/10/html-tools/#take-advantage-of-copy-and-paste)

 
One of the most useful input/output mechanisms for HTML tools comes in the form of **copy and paste**.

 
I frequently build tools that accept pasted content, transform it in some way and let the user copy it back to their clipboard to paste somewhere else.

 
Copy and paste on mobile phones is fiddly, so I frequently include “Copy to clipboard” buttons that populate the clipboard with a single touch.

 
Most operating system clipboards can carry multiple formats of the same copied data. That’s why you can paste content from a word processor in a way that preserves formatting, but if you paste the same thing into a text editor you’ll get the content with formatting stripped.

 
These rich copy operations are available in JavaScript paste events as well, which opens up all sorts of opportunities for HTML tools.

 
-  **[hacker-news-thread-export](https://tools.simonwillison.net/hacker-news-thread-export)** lets you paste in a URL to a Hacker News thread and gives you a copyable condensed version of the entire thread, suitable for pasting into an LLM to get a useful summary.
-  **[paste-rich-text](https://tools.simonwillison.net/paste-rich-text)** lets you copy from a page and paste to get the HTML—particularly useful on mobile where view-source isn’t available.
-  **[alt-text-extractor](https://tools.simonwillison.net/alt-text-extractor)** lets you paste in images and then copy out their alt text.

  [![screenshot of hacker-news-thread-export](https://static.simonwillison.net/static/2025/html-tools/hacker-news-thread-export.jpg)](https://tools.simonwillison.net/hacker-news-thread-export) [![screenshot of paste-rich-text](https://static.simonwillison.net/static/2025/html-tools/paste-rich-text.jpg)](https://tools.simonwillison.net/paste-rich-text) [![screenshot of alt-text-extractor](https://static.simonwillison.net/static/2025/html-tools/alt-text-extractor.jpg)](https://tools.simonwillison.net/alt-text-extractor)  
#### Build debugging tools [#](/2025/Dec/10/html-tools/#build-debugging-tools)

 
The key to building interesting HTML tools is understanding what’s possible. Building custom debugging tools is a great way to explore these options.

 
**[clipboard-viewer](https://tools.simonwillison.net/clipboard-viewer)** is one of my most useful. You can paste anything into it (text, rich text, images, files) and it will loop through and show you every type of paste data that’s available on the clipboard.

 
![Clipboard Format Viewer. Paste anywhere on the page (Ctrl+V or Cmd+V). This shows text/rtf with a bunch of weird code, text/plain with some pasted HTML diff and a Clipboard Event Information panel that says Event type: paste, Formats available: text/rtf, text/plain, 0 files reported and 2 clipboard items reported.](https://static.simonwillison.net/static/2025/clipboard-viewer.jpg)

 
This was key to building many of my other tools, because it showed me the invisible data that I could use to bootstrap other interesting pieces of functionality.

 
More debugging examples:

 
-  **[keyboard-debug](https://tools.simonwillison.net/keyboard-debug)** shows the keys (and `KeyCode` values) currently being held down.
-  **[cors-fetch](https://tools.simonwillison.net/cors-fetch)** reveals if a URL can be accessed via CORS.
-  **[exif](https://tools.simonwillison.net/exif)** displays EXIF data for a selected photo.

  [![screenshot of keyboard-debug](https://static.simonwillison.net/static/2025/html-tools/keyboard-debug.jpg)](https://tools.simonwillison.net/keyboard-debug) [![screenshot of cors-fetch](https://static.simonwillison.net/static/2025/html-tools/cors-fetch.jpg)](https://tools.simonwillison.net/cors-fetch) [![screenshot of exif](https://static.simonwillison.net/static/2025/html-tools/exif.jpg)](https://tools.simonwillison.net/exif)  
#### Persist state in the URL [#](/2025/Dec/10/html-tools/#persist-state-in-the-url)

 
HTML tools may not have access to server-side databases for storage but it turns out you can store a _lot_ of state directly in the URL.

 
I like this for tools I may want to bookmark or share with other people.

 
-  **[icon-editor](https://tools.simonwillison.net/icon-editor#cmdiKDIwMSwgNDYsIDg2KSxyZ2IoMjIzLCA0OCwgOTIpLHJnYigzNCwgODAsIDE3OSkscmdiKDIzNywgNTYsIDk1KSxyZ2IoMTgzLCA1MywgOTYpLHJnYigzOCwgMTA3LCAyMTApLHJnYigyMDQsIDY1LCAxMDUpLHJnYigxNzksIDEwMywgMTM2KSxyZ2IoMjMyLCA5NywgMTQ4KSxyZ2IoMzgsIDkxLCAyMDkpLHJnYigzNiwgOTUsIDIwNCkscmdiKDE5NSwgODYsIDEyOSkscmdiKDE3MywgMzEsIDU4KSxyZ2IoMjEyLCA2MSwgMTA2KSxyZ2IoOTIsIDEwNSwgMTg4KSxyZ2IoMjM3LCA3MSwgMTIzKSxyZ2IoMzksIDk2LCAyMTkpLHJnYigyOCwgODYsIDIxMCkscmdiKDIyMywgMjEyLCAzNCkscmdiKDE3MywgMTUzLCAyNikscmdiKDE0NCwgNzksIDI4KSxyZ2IoMjI0LCA1NiwgOTcpLHJnYigxOTYsIDQ4LCA4NSkscmdiKDIyMCwgNTAsIDk4KSxyZ2IoMTY2LCAxMjYsIDI1KSxyZ2IoMjA5LCAxMzAsIDE5KSxyZ2IoMTg3LCAxMTQsIDEzKSxyZ2IoMTQ3LCAxMDQsIDE4KSxyZ2IoMjE2LCA1OCwgODEpLHJnYigxNTIsIDM5LCA2NCkscmdiKDMyLCA3NSwgMTczKSxyZ2IoMTY2LCAxMjYsIDI5KSxyZ2IoMjM3LCAxODAsIDU0KSxyZ2IoMjA0LCAxMzgsIDIyKSxyZ2IoMTgxLCAxMjksIDIzKSxyZ2IoMjM0LCA4NiwgNzYpLHJnYigxOTAsIDY4LCA3NSkscmdiKDI0NSwgODksIDEzNSkscmdiKDIxMywgNjcsIDExMSkscmdiKDE0MSwgMzEsIDU2KSxyZ2IoNzIsIDc5LCAxMTYpLHJnYigxODcsIDE1NCwgNTIpLHJnYigyMDcsIDE3OSwgNzIpLHJnYigyMTAsIDE2MiwgNDMpLHJnYigyMTQsIDE0OSwgMzEpLHJnYigyMzksIDkwLCA4NCkscmdiKDIzNSwgMTMyLCA3NykscmdiKDE4MSwgMTM4LCAyOSkscmdiKDI0NSwgMTI4LCAxNzgpLHJnYigyMTcsIDk5LCAxNDUpLHJnYigxMTYsIDEwNSwgMTIyKSxyZ2IoMjA2LCAxNzYsIDY1KSxyZ2IoMTkxLCAxNjMsIDY0KSxyZ2IoMjA1LCAxNjksIDU4KSxyZ2IoMjM2LCAxNjUsIDQ2KSxyZ2IoMjM3LCA3OSwgODUpLHJnYigyMzUsIDE0NCwgODcpLHJnYigyNDksIDIwMiwgNDUpLHJnYigyMTAsIDE2NiwgMzQpLHJnYigyMjcsIDEwMywgMTYyKSxyZ2IoMjEzLCA5MCwgMTMwKSxyZ2IoNDQsIDQ4LCAxMjMpLHJnYigxMjUsIDg2LCAxNTEpLHJnYigxOTAsIDE2MywgMTA2KSxyZ2IoMTk5LCAxNjYsIDQ4KSxyZ2IoMjAyLCAxNjQsIDU2KSxyZ2IoMjIxLCAxNzAsIDUzKSxyZ2IoMjM0LCAxMzUsIDc1KSxyZ2IoMjQxLCAxNzUsIDc1KSxyZ2IoMjU1LCAyMjIsIDY1KSxyZ2IoMjU0LCAyMjYsIDY5KSxyZ2IoMjM1LCAyMDEsIDQ0KSxyZ2IoNzMsIDEzNywgMjQ3KSxyZ2IoODAsIDE0MywgMjQ4KSxyZ2IoNzksIDEzOSwgMjQzKSxyZ2IoMTM4LCA5MiwgMTc0KSxyZ2IoMTU2LCAxMTMsIDE3NikscmdiKDIwMSwgMTY4LCA2MykscmdiKDIxMSwgMTY5LCA0NikscmdiKDIxNCwgMTcxLCA1NSkscmdiKDIyOCwgMTgyLCA1NikscmdiKDI0MywgMTk1LCA1OCkscmdiKDI0NSwgMjA0LCA2NykscmdiKDI1NSwgMjIxLCA2NykscmdiKDI1NSwgMjI2LCA2OCkscmdiKDE1NCwgMTYyLCAxMzMpLHJnYigyNiwgMTA1LCAyNTUpLHJnYig2OCwgMTI5LCAyNTIpLHJnYig4NywgMTM1LCAyNDQpLHJnYig4MywgMTMxLCAyMzUpLHJnYig4MiwgMTI3LCAyMjYpLHJnYig4NSwgMTMwLCAyMjcpLHJnYig3OSwgMTIyLCAyMTgpLHJnYigxNjcsIDE0NiwgMzIpLHJnYigxNzQsIDEzOCwgMTI0KSxyZ2IoMTMzLCA2OSwgMjA1KSxyZ2IoMTcxLCAxMjAsIDE0NCkscmdiKDIxNSwgMTc2LCA1NykscmdiKDIyMCwgMTc1LCA0OSkscmdiKDIyMywgMTc5LCA1OCkscmdiKDIzNywgMTg4LCA2MCkscmdiKDI0MSwgMTkxLCA1NikscmdiKDIwMCwgMTc2LCAxMDUpLHJnYigxMTIsIDE0MSwgMjAzKSxyZ2IoODQsIDEyNywgMjM1KSxyZ2IoMTE1LCAxMzgsIDE5MSkscmdiKDgyLCAxMDMsIDE3NCkscmdiKDE1OCwgNDEsIDc2KSxyZ2IoMTcwLCA0MywgNjQpLHJnYigxOTAsIDE1NywgNTApLHJnYigyMDMsIDE3NywgNjUpLHJnYigxNjEsIDEwMiwgMTQyKSxyZ2IoMTQxLCA1OSwgMjA5KSxyZ2IoMTgwLCAxMjIsIDE1MSkscmdiKDIyOCwgMTg1LCA1OCkscmdiKDIzMywgMTg2LCA1MikscmdiKDI0MCwgMTg5LCA2NikscmdiKDI1NCwgMjEwLCA2OCkscmdiKDIwMSwgMTkxLCAxMTMpLHJnYigxMzcsIDEzOSwgMTU3KSxyZ2IoMjExLCAxNjIsIDg4KSxyZ2IoMjUwLCAyMDAsIDUwKSxyZ2IoMTc5LCAxMzEsIDIzKSxyZ2IoMTk2LCAxNjUsIDY0KSxyZ2IoMjA1LCAxNzQsIDU0KSxyZ2IoMjA5LCAxNjAsIDU5KSxyZ2IoMTY2LCA5MSwgMTYxKSxyZ2IoMTQyLCA2MCwgMjIzKSxyZ2IoMTk3LCAxMzksIDE1MCkscmdiKDI0MCwgMTk2LCA3MikscmdiKDI1MSwgMjA4LCA2MSkscmdiKDI1NSwgMjI0LCA4MCkscmdiKDI1NSwgMjUwLCA5MikscmdiKDI1NSwgMjM0LCA4OSkscmdiKDI0OSwgMTg2LCA1MSkscmdiKDI1MCwgMTgwLCAzOSkscmdiKDI0MCwgMTY2LCAzNSkscmdiKDIwMiwgMTc0LCA3MikscmdiKDIxNSwgMTY4LCA1MCkscmdiKDIyMiwgMTc1LCA0MykscmdiKDIxMiwgMTY1LCA2OSkscmdiKDE3NCwgMTAzLCAxNjcpLHJnYigxNjAsIDc4LCAyMzQpLHJnYigyMDUsIDE0NiwgMTg0KSxyZ2IoMjQ3LCAyMTgsIDEwOCkscmdiKDI1NSwgMjQ4LCA4NSkscmdiKDI1NSwgMjU1LCAxMDIpLHJnYigyNTUsIDI1NSwgMTIyKSxyZ2IoMjQwLCAyMTAsIDgyKSxyZ2IoMjE0LCAxNTAsIDMxKSxyZ2IoMjI0LCAxNTAsIDI1KSxyZ2IoMTc2LCAxMjEsIDI1KSxyZ2IoMTg5LCAxODMsIDUyKSxyZ2IoMTIyLCA4MCwgMTU4KSxyZ2IoMTkxLCAxNTEsIDEyMikscmdiKDIyOSwgMTc0LCA0MCkscmdiKDIyNSwgMTcyLCA1MSkscmdiKDIyOSwgMTg1LCA1MSkscmdiKDIzNywgMTkwLCA2MCkscmdiKDIwOSwgMTQ2LCAxNjEpLHJnYigxOTUsIDExNywgMjUxKSxyZ2IoMjI1LCAxNTUsIDIzOSkscmdiKDI1NCwgMjI3LCAxODQpLHJnYigyNTUsIDI1NSwgMTE3KSxyZ2IoMjQ5LCAyMzcsIDc2KSxyZ2IoMjA0LCAxNjcsIDU1KSxyZ2IoMTU3LCAxMTUsIDI1KSxyZ2IoMTM1LCA5OCwgMTYpLHJnYigyMDMsIDEyNSwgNTcpLHJnYigxOTgsIDEyNSwgNTMpLHJnYigxNTcsIDExMCwgMTQ0KSxyZ2IoMTQ5LCA4NCwgMTk0KSxyZ2IoMjEyLCAxNTcsIDk0KSxyZ2IoMjMyLCAxODUsIDQ3KSxyZ2IoMjM1LCAxODYsIDYyKSxyZ2IoMjUwLCAyMDQsIDY1KSxyZ2IoMjUzLCAyMzIsIDgxKSxyZ2IoMjQzLCAyMTUsIDE0OCkscmdiKDI0NywgMTgzLCAyMzMpLHJnYigyNDMsIDE2MywgMjUwKSxyZ2IoMTk4LCAxMzgsIDE3NSkscmdiKDE2MCwgMTEzLCA4MikscmdiKDEyNCwgODksIDM3KSxyZ2IoMTU3LCAxMzYsIDM2KSxyZ2IoMjAzLCAxNjQsIDgyKSxyZ2IoMTQ4LCA3MiwgMTg5KSxyZ2IoMTU4LCA4NCwgMjA0KSxyZ2IoMjE3LCAxNjgsIDExNykscmdiKDI1MCwgMjEwLCA2NykscmdiKDI1NSwgMjI5LCA3OCkscmdiKDI1NSwgMjU1LCA5NikscmdiKDI1NSwgMjU1LCA5NCkscmdiKDI0MywgMjE4LCA5NSkscmdiKDE3OCwgMTE4LCAxMDYpLHJnYigxMDMsIDQwLCAxMDIpLHJnYigxODgsIDExMSwgMjcpLHJnYigxODMsIDE1NiwgNTkpLHJnYigyMTUsIDE3NiwgNDgpLHJnYigyMDMsIDE0OCwgOTEpLHJnYigxNjcsIDg5LCAxOTcpLHJnYigxNzgsIDEwMywgMjM1KSxyZ2IoMjM1LCAxOTMsIDE3NSkscmdiKDI1NSwgMjUxLCAxMjQpLHJnYigyNDksIDI0MCwgOTIpLHJnYigyMTMsIDE4NiwgNjApLHJnYigxNjAsIDEyMSwgMjEpLHJnYigxOTEsIDE1NSwgMTA4KSxyZ2IoMjIxLCAxODAsIDQwKSxyZ2IoMjM3LCAxODksIDQ3KSxyZ2IoMjMzLCAxODYsIDk2KSxyZ2IoMjE5LCAxNjIsIDIwNykscmdiKDIzMSwgMTU5LCAyNDkpLHJnYigyMTAsIDE1OCwgMTkxKSxyZ2IoMTY5LCAxMzAsIDc1KSxyZ2IoMTQwLCA5NiwgMTE5KSxyZ2IoMTU1LCA4NSwgMjAwKSxyZ2IoMjA5LCAxNTcsIDExNSkscmdiKDI1NCwgMjI2LCA3MCkscmdiKDI1NSwgMjU1LCA4MCkscmdiKDIzNSwgMjE3LCA3NikscmdiKDE3OCwgMTMzLCA5MSkscmdiKDIwOSwgMTEwLCAxNTEpLHJnYigxNTIsIDExOCwgNTYpLHJnYigxODYsIDExNiwgMTY4KSxyZ2IoMTkzLCAxMjEsIDIzNikscmdiKDIyOSwgMTk1LCAxNjEpLHJnYigxOTcsIDE4MCwgNzUpLHJnYigxOTksIDE1OCwgNzApLHJnYigxOTcsIDE0OCwgMTM2KXxfX19fX19fXzAxX19fX19fX19fX19fX19fMl9fX19fX18zNDVfX19fX182X183OF9fOWFfX19fX2JjZGVfX19fX19fX19fZl9fX2doX2lqa19fbF9fX19fX19fbV9uX19fX19fX19vcHFyc19fX19fX19fdF9fX19fX3VfX192d3h5ejEwX19fMTExMl9fMTNfX19fX19fX18xNDE1MTYxNzE4MTkxYTFiX18xYzFkX19fX19fX19fX19fMWUxZjFnMWgxaTFqMWsxbDFtXzFuMW9fX19fX19fX19fXzFwMXExcjFzMXQxdTF2MXcxeDF5MXpfX19fXzIwMjEyMl9fX19fXzIzMjQyNTI2MjcyODI5MmEyYjJjMmQyZTJmMmcyaDJpMmoya19fX19fMmwybTJuMm8ycDJxMnIyczJ0MnUydjJ3MngyeV9fX19fX19fMnozMDMxMzIzMzM0MzUzNjM3MzgzOTNhM2IzYzNkM2VfX19fX19fX19fM2YzZzNoM2kzajNrM2wzbTNuM28zcDNxM3Izc19fX19fX19fX18zdDN1M3YzdzN4M3kzejQwNDE0MjQzNDQ0NTQ2NDc0OF9fX19fX180OTRhNGI0YzRkNGU0ZjRnNGg0aTRqNGs0bDRtNG5fX180bzRwX19fXzRxNHI0czR0NHU0djR3NHg0eTR6NTA1MTUyX19fX19fX19fXzUzNTQ1NTU2NTc1ODU5NWE1YjVjNWQ1ZV9fX19fXzVmX19fX181ZzVoNWk1ajVrNWw1bTVuNW81cF9fX19fX19fX19fX19fNXE1cjVzNXQ1dTV2NXc1eF9fX19fX19fX19fX19fXzV5NXo2MDYxNjI2MzY0X19fX19fX19fX19fNjVfX19fNjY2NzY4Njk2YV9fX19fX19fX19fX19fX19fX19fNmI2Y19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19f)** is a custom 24x24 icon editor I built to help hack on icons for [the GitHub Universe badge](https://simonwillison.net/2025/Oct/28/github-universe-badge/). It persists your in-progress icon design in the URL so you can easily bookmark and share it.

 
#### Use localStorage for secrets or larger state [#](/2025/Dec/10/html-tools/#use-localstorage-for-secrets-or-larger-state)

 
The [localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) browser API lets HTML tools store data persistently on the user’s device, without exposing that data to the server.

 
I use this for larger pieces of state that don’t fit comfortably in a URL, or for secrets like API keys which I really don’t want anywhere near my server —even static hosts might have server logs that are outside of my influence.

 
-  **[word-counter](https://tools.simonwillison.net/word-counter)** is a simple tool I built to help me write to specific word counts, for things like conference abstract submissions. It uses localStorage to save as you type, so your work isn’t lost if you accidentally close the tab.
-  **[render-markdown](https://tools.simonwillison.net/render-markdown)** uses the same trick—I sometimes use this one to craft blog posts and I don’t want to lose them.
-  **[haiku](https://tools.simonwillison.net/haiku)** is one of a number of LLM demos I’ve built that request an API key from the user (via the `prompt()` function) and then store that in `localStorage`. This one uses Claude Haiku to write haikus about what it can see through the user’s webcam.

  [![screenshot of word-counter](https://static.simonwillison.net/static/2025/html-tools/word-counter.jpg)](https://tools.simonwillison.net/word-counter) [![screenshot of render-markdown](https://static.simonwillison.net/static/2025/html-tools/render-markdown.jpg)](https://tools.simonwillison.net/render-markdown) [![screenshot of haiku](https://static.simonwillison.net/static/2025/html-tools/haiku.jpg)](https://tools.simonwillison.net/haiku)  
#### Collect CORS-enabled APIs [#](/2025/Dec/10/html-tools/#collect-cors-enabled-apis)

 
CORS stands for [Cross-origin resource sharing](https://en.wikipedia.org/wiki/Cross-origin_resource_sharing). It’s a relatively low-level detail which controls if JavaScript running on one site is able to fetch data from APIs hosted on other domains.

 
APIs that provide open CORS headers are a goldmine for HTML tools. It’s worth building a collection of these over time.

 
Here are some I like:

 
- iNaturalist for fetching sightings of animals, including URLs to photos
- PyPI for fetching details of Python packages
- GitHub because anything in a public repository in GitHub has a CORS-enabled anonymous API for fetching that content from the raw.githubusercontent.com domain, which is behind a caching CDN so you don’t need to worry too much about rate limits or feel guilty about adding load to their infrastructure.
- Bluesky for all sorts of operations
- Mastodon has generous CORS policies too, as used by applications like [phanpy.social](https://phanpy.social/)

 
GitHub Gists are a personal favorite here, because they let you build apps that can persist state to a permanent Gist through making a cross-origin API call.

 
-  **[species-observation-map](https://tools.simonwillison.net/species-observation-map#%7B%22taxonId%22%3A123829%2C%22taxonName%22%3A%22California%20Brown%20Pelican%22%2C%22days%22%3A%2230%22%7D)** uses iNaturalist to show a map of recent sightings of a particular species.
-  **[zip-wheel-explorer](https://tools.simonwillison.net/zip-wheel-explorer?package=llm)** fetches a `.whl` file for a Python package from PyPI, unzips it (in browser memory) and lets you navigate the files.
-  **[github-issue-to-markdown](https://tools.simonwillison.net/github-issue-to-markdown?issue=https%3A%2F%2Fgithub.com%2Fsimonw%2Fsqlite-utils%2Fissues%2F657)** fetches issue details and comments from the GitHub API (including expanding any permanent code links) and turns them into copyable Markdown.
-  **[terminal-to-html](https://tools.simonwillison.net/terminal-to-html)** can optionally save the user’s converted terminal session to a Gist.
-  **[bluesky-quote-finder](https://tools.simonwillison.net/bluesky-quote-finder?post=https%3A%2F%2Fbsky.app%2Fprofile%2Fsimonwillison.net%2Fpost%2F3m7auwt3ma222)** displays quotes of a specified Bluesky post, which can then be sorted by likes or by time.

  [![screenshot of species-observation-map](https://static.simonwillison.net/static/2025/html-tools/species-observation-map.jpg)](https://tools.simonwillison.net/species-observation-map#%7B%22taxonId%22%3A123829%2C%22taxonName%22%3A%22California%20Brown%20Pelican%22%2C%22days%22%3A%2230%22%7D) [![screenshot of zip-wheel-explorer](https://static.simonwillison.net/static/2025/html-tools/zip-wheel-explorer.jpg)](https://tools.simonwillison.net/zip-wheel-explorer?package=llm) [![screenshot of github-issue-to-markdown](https://static.simonwillison.net/static/2025/html-tools/github-issue-to-markdown.jpg)](https://tools.simonwillison.net/github-issue-to-markdown?issue=https%3A%2F%2Fgithub.com%2Fsimonw%2Fsqlite-utils%2Fissues%2F657) [![screenshot of terminal-to-html](https://static.simonwillison.net/static/2025/html-tools/terminal-to-html.jpg)](https://tools.simonwillison.net/terminal-to-html) [![screenshot of bluesky-quote-finder](https://static.simonwillison.net/static/2025/html-tools/bluesky-quote-finder.jpg)](https://tools.simonwillison.net/bluesky-quote-finder?post=https%3A%2F%2Fbsky.app%2Fprofile%2Fsimonwillison.net%2Fpost%2F3m7auwt3ma222)  
#### LLMs can be called directly via CORS [#](/2025/Dec/10/html-tools/#llms-can-be-called-directly-via-cors)

 
All three of OpenAI, Anthropic and Gemini offer JSON APIs that can be accessed via CORS directly from HTML tools.

 
Unfortunately you still need an API key, and if you bake that key into your visible HTML anyone can steal it and use to rack up charges on your account.

 
I use the `localStorage` secrets pattern to store API keys for these services. This sucks from a user experience perspective—telling users to go and create an API key and paste it into a tool is a lot of friction—but it does work.

 
Some examples:

 
-  **[haiku](https://tools.simonwillison.net/haiku)** uses the Claude API to write a haiku about an image from the user’s webcam.
-  **[openai-audio-output](https://tools.simonwillison.net/openai-audio-output)** generates audio speech using OpenAI’s GPT-4o audio API.
-  **[gemini-bbox](http://tools.simonwillison.net/gemini-bbox)** demonstrates Gemini 2.5’s ability to return complex shaped image masks for objects in images, see [Image segmentation using Gemini 2.5](https://simonwillison.net/2025/Apr/18/gemini-image-segmentation/).

  [![screenshot of haiku](https://static.simonwillison.net/static/2025/html-tools/haiku.jpg)](https://tools.simonwillison.net/haiku) [![screenshot of openai-audio-output](https://static.simonwillison.net/static/2025/html-tools/openai-audio-output.jpg)](https://tools.simonwillison.net/openai-audio-output) [![screenshot of gemini-bbox](https://static.simonwillison.net/static/2025/html-tools/gemini-bbox.jpg)](http://tools.simonwillison.net/gemini-bbox)  
#### Don’t be afraid of opening files [#](/2025/Dec/10/html-tools/#don-t-be-afraid-of-opening-files)

 
You don’t need to upload a file to a server in order to make use of the `<input type="file">` element. JavaScript can access the content of that file directly, which opens up a wealth of opportunities for useful functionality.

 
Some examples:

 
-  **[ocr](https://tools.simonwillison.net/ocr)** is the first tool I built for my collection, described in [Running OCR against PDFs and images directly in your browser](https://simonwillison.net/2024/Mar/30/ocr-pdfs-images/). It uses `PDF.js` and `Tesseract.js` to allow users to open a PDF in their browser which it then converts to an image-per-page and runs through OCR.
-  **[social-media-cropper](https://tools.simonwillison.net/social-media-cropper)** lets you open (or paste in) an existing image and then crop it to common dimensions needed for different social media platforms—2:1 for Twitter and LinkedIn, 1.4:1 for Substack etc.
-  **[ffmpeg-crop](https://tools.simonwillison.net/ffmpeg-crop)** lets you open and preview a video file in your browser, drag a crop box within it and then copy out the `ffmpeg` command needed to produce a cropped copy on your own machine.

  [![screenshot of ocr](https://static.simonwillison.net/static/2025/html-tools/ocr.jpg)](https://tools.simonwillison.net/ocr) [![screenshot of social-media-cropper](https://static.simonwillison.net/static/2025/html-tools/social-media-cropper.jpg)](https://tools.simonwillison.net/social-media-cropper) [![screenshot of ffmpeg-crop](https://static.simonwillison.net/static/2025/html-tools/ffmpeg-crop.jpg)](https://tools.simonwillison.net/ffmpeg-crop)  
#### You can offer downloadable files too [#](/2025/Dec/10/html-tools/#you-can-offer-downloadable-files-too)

 
An HTML tool can generate a file for download without needing help from a server.

 
The JavaScript library ecosystem has a huge range of packages for generating files in all kinds of useful formats.

 
-  **[svg-render](https://tools.simonwillison.net/svg-render)** lets the user download the PNG or JPEG rendered from an SVG.
-  **[social-media-cropper](https://tools.simonwillison.net/social-media-cropper)** does the same for cropped images.
-  **[open-sauce-2025](https://tools.simonwillison.net/open-sauce-2025)** is my alternative schedule for a conference that includes a downloadable ICS file for adding the schedule to your calendar. See [Vibe scraping and vibe coding a schedule app for Open Sauce 2025 entirely on my phone](https://simonwillison.net/2025/Jul/17/vibe-scraping/) for more on that project.

  [![screenshot of svg-render](https://static.simonwillison.net/static/2025/html-tools/svg-render.jpg)](https://tools.simonwillison.net/svg-render) [![screenshot of social-media-cropper](https://static.simonwillison.net/static/2025/html-tools/social-media-cropper.jpg)](https://tools.simonwillison.net/social-media-cropper) [![screenshot of open-sauce-2025](https://static.simonwillison.net/static/2025/html-tools/open-sauce-2025.jpg)](https://tools.simonwillison.net/open-sauce-2025)  
#### Pyodide can run Python code in the browser [#](/2025/Dec/10/html-tools/#pyodide-can-run-python-code-in-the-browser)

 
[Pyodide](https://pyodide.org/) is a distribution of Python that’s compiled to WebAssembly and designed to run directly in browsers. It’s an engineering marvel and one of the most underrated corners of the Python world.

 
It also cleanly loads from a CDN, which means there’s no reason not to use it in HTML tools!

 
Even better, the Pyodide project includes [micropip](https://github.com/pyodide/micropip)—a mechanism that can load extra pure-Python packages from PyPI via CORS.

 
-  **[pyodide-bar-chart](https://tools.simonwillison.net/pyodide-bar-chart)** demonstrates running Pyodide, Pandas and matplotlib to render a bar chart directly in the browser.
-  **[numpy-pyodide-lab](https://tools.simonwillison.net/numpy-pyodide-lab)** is an experimental interactive tutorial for Numpy.
-  **[apsw-query](https://tools.simonwillison.net/apsw-query)** demonstrates the [APSW SQLite library](https://github.com/rogerbinns/apsw) running in a browser, using it to show EXPLAIN QUERY plans for SQLite queries.

  [![screenshot of pyodide-bar-chart](https://static.simonwillison.net/static/2025/html-tools/pyodide-bar-chart.jpg)](https://tools.simonwillison.net/pyodide-bar-chart) [![screenshot of numpy-pyodide-lab](https://static.simonwillison.net/static/2025/html-tools/numpy-pyodide-lab.jpg)](https://tools.simonwillison.net/numpy-pyodide-lab) [![screenshot of apsw-query](https://static.simonwillison.net/static/2025/html-tools/apsw-query.jpg)](https://tools.simonwillison.net/apsw-query)  
#### WebAssembly opens more possibilities [#](/2025/Dec/10/html-tools/#webassembly-opens-more-possibilities)

 
Pyodide is possible thanks to WebAssembly. WebAssembly means that a vast collection of software originally written in other languages can now be loaded in HTML tools as well.

 
[Squoosh.app](https://squoosh.app/) was the first example I saw that convinced me of the power of this pattern—it makes several best-in-class image compression libraries available directly in the browser.

 
I’ve used WebAssembly for a few of my own tools:

 
-  **[ocr](https://tools.simonwillison.net/ocr)** uses the pre-existing [Tesseract.js](https://tesseract.projectnaptha.com/) WebAssembly port of the Tesseract OCR engine.
-  **[sloccount](https://tools.simonwillison.net/sloccount)** is a port of David Wheeler’s Perl and C [SLOCCount](https://dwheeler.com/sloccount/) utility to the browser, using a big ball of WebAssembly duct tape. [More details here](https://simonwillison.net/2025/Oct/22/sloccount-in-webassembly/).
-  **[micropython](https://tools.simonwillison.net/micropython)** is my experiment using [@micropython/micropython-webassembly-pyscript](https://www.npmjs.com/package/@micropython/micropython-webassembly-pyscript) from NPM to run Python code with a smaller initial download than Pyodide.

  [![screenshot of ocr](https://static.simonwillison.net/static/2025/html-tools/ocr.jpg)](https://tools.simonwillison.net/ocr) [![screenshot of sloccount](https://static.simonwillison.net/static/2025/html-tools/sloccount.jpg)](https://tools.simonwillison.net/sloccount) [![screenshot of micropython](https://static.simonwillison.net/static/2025/html-tools/micropython.jpg)](https://tools.simonwillison.net/micropython)  
#### Remix your previous tools [#](/2025/Dec/10/html-tools/#remix-your-previous-tools)

 
The biggest advantage of having a single public collection of 100+ tools is that it’s easy for my LLM assistants to recombine them in interesting ways.

 
Sometimes I’ll copy and paste a previous tool into the context, but when I’m working with a coding agent I can reference them by name—or tell the agent to search for relevant examples before it starts work.

 
The source code of any working tool doubles as clear documentation of how something can be done, including patterns for using editing libraries. An LLM with one or two existing tools in their context is much more likely to produce working code.

 
I built **[pypi-changelog](https://tools.simonwillison.net/pypi-changelog)** by telling Claude Code:

  
`Look at the pypi package explorer tool`

  
And then, after it had found and read the source code for [zip-wheel-explorer](https://tools.simonwillison.net/zip-wheel-explorer):

  
`Build a new tool pypi-changelog.html which uses the PyPI API to get the wheel URLs of all available versions of a package, then it displays them in a list where each pair has a "Show changes" clickable in between them - clicking on that fetches the full contents of the wheels and displays a nicely rendered diff representing the difference between the two, as close to a standard diff format as you can get with JS libraries from CDNs, and when that is displayed there is a "Copy" button which copies that diff to the clipboard`

  
Here’s [the full transcript](https://gistpreview.github.io/?9b48fd3f8b99a204ba2180af785c89d2).

 
See [Running OCR against PDFs and images directly in your browser](https://simonwillison.net/2024/Mar/30/ocr-pdfs-images/) for another detailed example of remixing tools to create something new.

 
#### Record the prompt and transcript [#](/2025/Dec/10/html-tools/#record-the-prompt-and-transcript)

 
I like keeping (and publishing) records of everything I do with LLMs, to help me grow my skills at using them over time.

 
For HTML tools I built by chatting with an LLM platform directly I use the “share” feature for those platforms.

 
For Claude Code or Codex CLI or other coding agents I copy and paste the full transcript from the terminal into my [terminal-to-html](https://tools.simonwillison.net/terminal-to-html) tool and share that using a Gist.

 
In either case I include links to those transcripts in the commit message when I save the finished tool to my repository. You can see those [in my tools.simonwillison.net colophon](https://tools.simonwillison.net/colophon).

 
#### Go forth and build [#](/2025/Dec/10/html-tools/#go-forth-and-build)

 
I’ve had _so much fun_ exploring the capabilities of LLMs in this way over the past year and a half, and building tools in this way has been invaluable in helping me understand both the potential for building tools with HTML and the capabilities of the LLMs that I’m building them with.

 
If you’re interested in starting your own collection I highly recommend it! All you need to get started is a free GitHub repository with GitHub Pages enabled (Settings -> Pages -> Source -> Deploy from a branch -> main) and you can start copying in `.html` pages generated in whatever manner you like.

 
**Bonus transcript**: Here’s [how I used Claude Code](http://gistpreview.github.io/?1b8cba6a8a21110339cbde370e755ba0) and [shot-scraper](https://shot-scraper.datasette.io/) to add the screenshots to this post.

  Posted [10th December 2025](/2025/Dec/10/) at 9 pm · Follow me on [Mastodon](https://fedi.simonwillison.net/@simon), [Bluesky](https://bsky.app/profile/simonwillison.net), [Twitter](https://twitter.com/simonw) or [subscribe to my newsletter](https://simonwillison.net/about/#subscribe) 


   
## More recent articles

 
- [How Rob Pike got spammed with an AI slop "act of kindness"](/2025/Dec/26/slop-acts-of-kindness/) - 26th December 2025
- [A new way to extract detailed transcripts from Claude Code](/2025/Dec/25/claude-code-transcripts/) - 25th December 2025
- [Cooking with Claude](/2025/Dec/23/cooking-with-claude/) - 23rd December 2025

      
This is **Useful patterns for building HTML tools** by Simon Willison, posted on [10th December 2025](/2025/Dec/10/).

  
Part of series **[How I use LLMs and ChatGPT](/series/using-llms/)**

 
1. [Getting DeepSeek-OCR working on an NVIDIA Spark via brute force using Claude Code](/2025/Oct/20/deepseek-ocr-claude-code/) - Oct. 20, 2025, 5:21 p.m. 
2. [Video: Building a tool to copy-paste share terminal sessions using Claude Code for web](/2025/Oct/23/claude-code-for-web-video/) - Oct. 23, 2025, 4:14 a.m. 
3. [Video + notes on upgrading a Datasette plugin for the latest 1.0 alpha, with help from uv and OpenAI Codex CLI](/2025/Nov/6/upgrading-datasette-plugins/) - Nov. 6, 2025, 6:26 p.m. 
4. **Useful patterns for building HTML tools** - Dec. 10, 2025, 9 p.m. 
5. [I ported JustHTML from Python to JavaScript with Codex CLI and GPT-5.2 in 4.5 hours](/2025/Dec/15/porting-justhtml/) - Dec. 15, 2025, 11:58 p.m. 
6. [Cooking with Claude](/2025/Dec/23/cooking-with-claude/) - Dec. 23, 2025, 5:01 a.m. 

  [ definitions 42 ](/tags/definitions/) [ github 176 ](/tags/github/) [ html 94 ](/tags/html/) [ javascript 731 ](/tags/javascript/) [ projects 513 ](/tags/projects/) [ tools 48 ](/tags/tools/) [ ai 1755 ](/tags/ai/) [ webassembly 85 ](/tags/webassembly/) [ generative-ai 1552 ](/tags/generative-ai/) [ llms 1516 ](/tags/llms/) [ ai-assisted-programming 294 ](/tags/ai-assisted-programming/) [ vibe-coding 63 ](/tags/vibe-coding/) [ coding-agents 116 ](/tags/coding-agents/) [ claude-code 68 ](/tags/claude-code/) 
**Next:** [GPT-5.2](/2025/Dec/11/gpt-52/)

 
**Previous:** [Under the hood of Canada Spends with Brendan Samek](/2025/Dec/9/canada-spends/)

 [![Sponsored: Augment](https://media.ethicalads.io/media/images/2025/11/EthicalAd_-_240x180_ZuMdgVD.png)](https://server.ethicalads.io/proxy/click/9839/019b66fb-f16c-73c1-82eb-e828abc9b572/)[**The AI Agent that gets your codebase **Copilot & Cursor letting you down? Try Augment.** Install Now**](https://server.ethicalads.io/proxy/click/9839/019b66fb-f16c-73c1-82eb-e828abc9b572/)www.augmentcode.com[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-image)![](https://server.ethicalads.io/proxy/view/9839/019b66fb-f16c-73c1-82eb-e828abc9b572/)![](https://server.ethicalads.io/proxy/viewtime/9839/019b66fb-f16c-73c1-82eb-e828abc9b572/?view_time=46)  
###  Monthly briefing 

 
 Sponsor me for **$10/month** and get a curated email digest of the month's most important LLM developments. 

 
 Pay me to send you less! 

 [ Sponsor & subscribe ](https://github.com/sponsors/simonw/)        
- [Colophon](/about/#about-site)
- ©
- [2002](/2002/)
- [2003](/2003/)
- [2004](/2004/)
- [2005](/2005/)
- [2006](/2006/)
- [2007](/2007/)
- [2008](/2008/)
- [2009](/2009/)
- [2010](/2010/)
- [2011](/2011/)
- [2012](/2012/)
- [2013](/2013/)
- [2014](/2014/)
- [2015](/2015/)
- [2016](/2016/)
- [2017](/2017/)
- [2018](/2018/)
- [2019](/2019/)
- [2020](/2020/)
- [2021](/2021/)
- [2022](/2022/)
- [2023](/2023/)
- [2024](/2024/)
- [2025](/2025/)
-          

  image-gallery:not(:defined) img {max-height: 150px;}  document.addEventListener('DOMContentLoaded', () => { document.querySelectorAll('h2[id],h3[id],h4[id],h5[id],h6[id]').forEach(el => { const id = el.getAttribute('id'); const permalinkContext = el.closest('[data-permalink-context]'); if (permalinkContext) { const url = permalinkContext.getAttribute('data-permalink-context'); const hashLink = document.createElement('a'); hashLink.style.borderBottom = 'none'; hashLink.style.color = '#666'; hashLink.style.fontSize = '1em'; hashLink.style.opacity = 0.8; hashLink.setAttribute('href', url + '#' + id); hashLink.innerText = '#'; el.appendChild(document.createTextNode('\u00A0')); el.appendChild(hashLink); } }); });   const config = [ {"tag": "lite-youtube", "js": "/static/lite-yt-embed.js", "css": "/static/lite-yt-embed.css"}, {"tag": "image-gallery", "js": "/static/image-gallery.js", "css": null} ]; for (const {tag, js, css} of config) { if (document.querySelector(tag)) { if (css) { document.head.appendChild( Object.assign(document.createElement('link'), { rel: 'stylesheet', href: css }) ); } if (js) { await import(js); } } }   document.addEventListener('DOMContentLoaded', () => { if (window.localStorage.getItem('ADMIN')) { document.querySelectorAll('.edit-page-link').forEach(el => { const url = el.getAttribute('data-admin-url'); if (url) { const a = document.createElement('a'); a.href = url; a.className = 'edit-link'; a.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path><path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path></svg> Edit'; el.appendChild(a); el.style.display = 'block'; } }); } });   // Random tag navigation - shows button if recently came from tag random (function() { const stored = localStorage.getItem('random_tag'); if (!stored) return; try { const data = JSON.parse(stored); const elapsed = Date.now() - data.timestamp; // Only show if within 5 seconds if (elapsed > 5000) return; const header = document.getElementById('smallhead-inner'); if (!header) return; const btn = document.createElement('a'); btn.href = '/random/' + encodeURIComponent(data.tag) + '/'; btn.className = 'random-tag-nav'; btn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 3 21 3 21 8"></polyline><line x1="4" y1="20" x2="21" y2="3"></line><polyline points="21 16 21 21 16 21"></polyline><line x1="15" y1="15" x2="21" y2="21"></line><line x1="4" y1="4" x2="9" y2="9"></line></svg> Random ' + data.tag; btn.addEventListener('click', function(e) { // Bump the timestamp before navigating localStorage.setItem('random_tag', JSON.stringify({ tag: data.tag, timestamp: Date.now() })); }); // Insert before the Subscribe link const subscribeLink = document.getElementById('smallhead-about'); if (subscribeLink) { header.insertBefore(btn, subscribeLink); } else { header.appendChild(btn); } } catch (e) { // Invalid JSON, clear it localStorage.removeItem('random_tag'); } })();   // Theme toggle functionality (function() { const toggle = document.getElementById('theme-toggle'); const iconAuto = document.getElementById('icon-auto'); const iconLight = document.getElementById('icon-light'); const iconDark = document.getElementById('icon-dark'); // Theme states: 'auto' (default), 'light', 'dark' function getTheme() { return localStorage.getItem('theme') || 'auto'; } function setTheme(theme) { if (theme === 'auto') { localStorage.removeItem('theme'); document.documentElement.removeAttribute('data-theme'); } else { localStorage.setItem('theme', theme); document.documentElement.setAttribute('data-theme', theme); } updateIcon(theme); } function updateIcon(theme) { iconAuto.style.display = theme === 'auto' ? 'block' : 'none'; iconLight.style.display = theme === 'light' ? 'block' : 'none'; iconDark.style.display = theme === 'dark' ? 'block' : 'none'; // Update aria-label for accessibility const labels = { 'auto': 'Theme: Auto (system preference). Click to switch to light.', 'light': 'Theme: Light. Click to switch to dark.', 'dark': 'Theme: Dark. Click to switch to auto.' }; toggle.setAttribute('aria-label', labels[theme]); } // Cycle through themes: auto -> light -> dark -> auto function cycleTheme() { const current = getTheme(); const next = current === 'auto' ? 'light' : current === 'light' ? 'dark' : 'auto'; setTheme(next); } // Initialize updateIcon(getTheme()); toggle.addEventListener('click', cycleTheme); })();   ![](chrome-extension://kipdpbpgbehkppnchehlfodlgclbcfkh/icon.png)