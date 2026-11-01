# Printable Cheat Sheet

Free AI coding with local models — one page, desk-ready.

Print this page (Ctrl+P / Cmd+P) or print `site/cheat-sheet.html`.

---

## Ollama commands

```
ollama --version        Check Ollama is installed
ollama list             List models on your machine
ollama pull <model>     Download a model
ollama run <model>      Start chatting with a model
/bye                    Exit a chat session
ollama stop <model>     Stop a running model
ollama rm <model>       Delete a model to free space
```

Good starter model: `ollama pull qwen2.5-coder:3b`

---

## Code prompts (fill in the brackets)

Explain code:

```
Explain this code line by line:

<PASTE CODE>
```

Write a function:

```
Write a Python function that <DOES WHAT>.
Include an example of how to call it.
```

Write tests:

```
Write unittest tests for this function:

<PASTE FUNCTION>
```

Find bugs:

```
Look for bugs and suggest fixes:

<PASTE CODE>
```

Add comments:

```
Add beginner-friendly comments:

<PASTE CODE>
```

Plain English to code:

```
Write a Python script that <PLAIN ENGLISH GOAL>.
Show how to save and run it.
```

---

## Debugging template

```
This code should <GOAL>, but it <ACTUAL BEHAVIOR>.

Error:

<PASTE ERROR MESSAGE>

Code:

<PASTE CODE>

Suggest a fix and explain what went wrong.
```

If the fix fails, paste the new error and updated code back and ask again.

---

## Privacy rules

- [ ] No passwords in prompts
- [ ] No API keys (`sk-...`, `ghp_...`) in prompts
- [ ] No real customer/patient names or data
- [ ] Use fake example data
- [ ] Read AI code before running it
- [ ] Keep secrets in `.env`, never in GitHub

---

## Files in this guide

- `docs/manual.md` — full manual
- `docs/ollama-setup.md` — install Ollama
- `docs/code-prompts.md` — prompt library
- `docs/debugging.md` — debugging help
- `docs/privacy.md` — privacy-safe habits
- `site/cheat-sheet.html` — printable HTML version

---

Created and maintained by **Asdale Dynamics, LLC** (Indiana). Dylan Asdale is
the founder and author of *The Massive AI Manual*. Hub site:
https://dylanasdale.github.io

License: MIT. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.
