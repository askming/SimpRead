Save Article to GitHub — Chrome Extension

What this does:
- Adds a popup button to save the current page's main article as a Markdown (or HTML) file into a GitHub repo.

Installation (developer / unpacked mode):
1. Create a GitHub Personal Access Token with `repo` scope.
2. In Chrome, go to `chrome://extensions` and enable "Developer mode".
3. Click "Load unpacked" and select the `chrome-extension` directory from this repo.
4. Open the extension's options and paste your token, owner and repo.

Usage:
- Click the extension icon, choose format (Markdown/HTML), optionally supply a filename or path prefix, then click Save.
- The extension will create the file under the path you provide in the configured repository.

Notes & limitations:
- This extension uses a simple built-in HTML->Markdown converter (covers headings, links, lists, images, emphasis).
- I implemented Markdown and HTML outputs. If you meant EPUB, please confirm — I can add an EPUB conversion step, but that requires adding a browser-compatible EPUB generator or a small server-side converter.
- The extension stores your token in `chrome.storage.sync` — this is local to the browser profile. Keep your token scope minimal.

Security:
- The extension calls the GitHub REST API directly with your token. Do not publish this extension with tokens included.

Next steps I can do for you:
- Add EPUB generation (ask whether you meant EPUB), or
- Add a configurable filename template, or
- Add auto-detection of article title and publication date for filenames.
