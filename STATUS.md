# STATUS

Free AI Coding with Local Models — beginner manual + static HTML site.

## What was built

A beginner-friendly guide to coding with free, local AI models using Ollama.
No account, no API key, nothing leaves your machine.

**Docs (`docs/`):**
- `manual.md` — full beginner manual (welcome, Ollama setup, first prompt,
  code prompts, debugging, privacy habits, cheat sheet, credits)
- `ollama-setup.md` — install Ollama, verify, pull a model, run it,
  command reference, troubleshooting
- `code-prompts.md` — prompt library (explain, write function, write tests,
  find bugs, add comments, refactor, plain English to code) with worked example
- `debugging.md` — debugging loop, prompt template, worked TypeError example,
  safety rules, common beginner errors
- `privacy.md` — local-first privacy, daily checklist, do/do-not table,
  where real secrets belong (.env, .gitignore)
- `cheat-sheet.md` — printable one-page reference

**Static HTML site (`site/`):**
- `index.html` — manual landing page with section index
- `ollama-setup.html`, `code-prompts.html`, `debugging.html`, `privacy.html`
- `cheat-sheet.html` — printable cheat sheet with `@media print` styles
- `style.css` — shared styles, skip link, semantic markup, print styles

**Other:**
- `README.md` — overview, credits Asdale Dynamics, LLC, quick start, verification steps
- `.gitignore` — keeps `.env`, keys, cache, and OS files out of version control
- `LICENSE` — MIT License, Copyright (c) 2026 Asdale Dynamics, LLC
- `verify/verify.py` — verification script (files, license, credit, HTML,
  print styles, secrets, links)
- `STATUS.md` — this file

Created and maintained by Asdale Dynamics, LLC (Indiana). Dylan Asdale is the
founder and author of *The Massive AI Manual*. Hub site:
https://dylanasdale.github.io

## How to run it

Read the markdown files in `docs/`, or open `site/index.html` in any web
browser. All pages are static — no build step, no server needed.

Print the cheat sheet: open `site/cheat-sheet.html` and press Ctrl+P (or
Cmd+P). Print styles hide navigation and show only the cheat sheet.

Run verification:

```
python3 verify/verify.py
```

## Verification results

`python3 verify/verify.py` -> VERIFICATION PASSED

Checks performed:
- All 18 expected files present (includes `.gitignore`)
- `LICENSE` contains the exact line `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` credits Asdale Dynamics, LLC and includes the copyright line
- All 6 HTML pages parse as well-formed HTML (no unclosed or mismatched tags)
- Every HTML page credits Asdale Dynamics, LLC
- `site/cheat-sheet.html` includes `@media print` print styles
- All internal HTML links resolve to existing files
- No `.github/workflows` directory
- Secret scan clean (no API keys, passwords, or tokens in files)

## Known gaps

- Ollama itself is not installed in this repository; users install it from
  https://ollama.com (documented in `docs/ollama-setup.html`).
- No code editor integration (VS Code/Ollama extensions) is included;
  suggested as a next step in the manual.
- HTML pages link to the markdown source files and to Ollama's website; no
  other external dependencies.
- No tests are automated beyond `verify/verify.py`; the guide is documentation
  rather than software with unit tests.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.
