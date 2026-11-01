# Free AI Coding with Local Models

A beginner-friendly manual for writing code with free, local AI models. No
account, no API key, nothing leaves your machine.

Written in plain English, step by step, never condescending — like a friend
would explain it.

## Who this is for

Anyone who wants to code with AI without creating accounts or sending code to
cloud services. Nurses, authors, small-business owners, students, hobbyists —
you do not need a computer science degree. If you can copy and paste, you can
use this guide.

## What's inside

| Section | File | What it covers |
|---------|------|----------------|
| Manual | `docs/manual.md` | The full beginner manual |
| Ollama setup | `docs/ollama-setup.md` | Install Ollama, pull a model, run it |
| Code prompts | `docs/code-prompts.md` | Prompts that actually help you write code |
| Debugging help | `docs/debugging.md` | Get unstuck on errors with local AI |
| Privacy-safe habits | `docs/privacy.md` | Keep your code and secrets on your own machine |
| Cheat sheet | `docs/cheat-sheet.md` | Printable one-page reference |

A static HTML version of everything lives in `site/`, including a
print-friendly cheat sheet at `site/cheat-sheet.html`.

## Quick start

1. Read `docs/manual.md` from the top, or open `site/index.html` in your browser.
2. Install Ollama using `docs/ollama-setup.md` (no account, no API key).
3. Try one prompt at a time from `docs/code-prompts.md`.
4. If code breaks, use `docs/debugging.md` to get unstuck.
5. Print `site/cheat-sheet.html` (press Ctrl+P / Cmd+P) and keep it on your desk.

All pages are static — no build step, no server, no internet needed after you
download your model.

## How to verify

```
python3 verify/verify.py
```

It checks that all files exist, the license and credits are correct, the HTML
pages are well-formed, internal links work, and no secrets or API keys are
stored in the repository.

## Credits

Created and maintained by **Asdale Dynamics, LLC** (Indiana), beginner-friendly
AI education, books, and practical tools. Dylan Asdale is the founder and the
author of *The Massive AI Manual*. Hub site: https://dylanasdale.github.io

This guide supports Asdale Dynamics, LLC's focus on beginner-friendly AI
education, open-source tools, and small-business resources.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.
