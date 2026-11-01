# Free AI Coding with Local Models

A beginner-friendly manual for writing code with free, local AI models.

No account. No API key. Nothing leaves your machine.

Written by Asdale Dynamics, LLC — plain English, step by step, never condescending.

---

## 1. Welcome

AI can help you write code, explain code, and fix bugs. Most AI coding tools
want you to create an account and pay for a subscription. This guide shows you
how to do it for free, entirely on your own computer, using models that run
locally through a tool called Ollama.

Your code stays on your computer. No company reads it. No credit card required.

---

## 2. How local AI coding works

You install Ollama, download (or "pull") an AI model, and chat with it through
your terminal or through simple tools built on top of Ollama. The model does its
thinking on your computer's processor (or graphics card), not on someone else's
server.

Because everything runs locally:

- You do not need an internet connection after downloading the model
- You do not need an account or API key
- Your code never leaves your machine
- It works on airplanes, in coffee shops, and anywhere else

The trade-off: you need enough disk space for the model (usually 2–8 GB) and a
computer that is not too old. Any machine from the last several years should
work fine.

---

## 3. Ollama setup

### Step 1: Install Ollama

1. Go to https://ollama.com and download Ollama for your operating system
   (Windows, Mac, or Linux).
2. Run the installer and follow the prompts.
3. Open a terminal (Command Prompt or PowerShell on Windows, Terminal on Mac or
   Linux) and type:

   ```
   ollama --version
   ```

   You should see a version number. If the command is not found, restart your
   terminal and try again.

### Step 2: Verify Ollama is running

Ollama runs as a background service. Check that it is up:

```
ollama list
```

You should see an empty list of models (or a list of models you already have).
No error means Ollama is working.

### Step 3: Pull your first coding model

Good beginner coding models:

- `qwen2.5-coder:3b` — small, fast, great for learning (about 2 GB)
- `deepseek-coder:6.7b` — stronger coding ability (about 4 GB)
- `codellama:7b` — solid all-rounder (about 4 GB)

Pick one and pull it:

```
ollama pull qwen2.5-coder:3b
```

This downloads the model to your computer. It may take a few minutes depending
on your internet speed. You only need to do this once.

### Step 4: Run the model and chat

```
ollama run qwen2.5-coder:3b
```

You will see a prompt like `>>>`. Type your question and press Enter. When you
are done, type `/bye` to exit, or press Ctrl+D.

Example:

```
>>> Write a Python function that adds two numbers
...
```

Ollama will stream its answer back to you.

### Quick reference

| Command | What it does |
|---------|--------------|
| `ollama list` | Shows models on your machine |
| `ollama pull <model>` | Downloads a model |
| `ollama run <model>` | Starts a chat with a model |
| `ollama stop <model>` | Stops a running model |
| `ollama rm <model>` | Deletes a model to free space |

---

## 4. Your first code prompt

Open Ollama and try this prompt:

```
Explain this Python code line by line:

def greet(name):
    return "Hello, " + name

print(greet("Dylan"))
```

Then try:

```
Write a Python program that asks for a name and prints a greeting.
```

Read the answer, copy the code into a file called `hello.py`, and run it:

```
python hello.py
```

That is the whole loop: prompt, copy, run, repeat.

---

## 5. Code prompts that work

These prompts are written for beginners. Replace the bracketed parts with your
own code or task.

### Explain code

```
Explain this code line by line in simple terms:

<PASTE YOUR CODE HERE>
```

### Write a function

```
Write a Python function that <DOES WHAT YOU WANT>.
Include a short example of how to call it.
```

### Write tests

```
Write unit tests for this Python function using the built-in unittest module:

<PASTE YOUR FUNCTION HERE>
```

### Find bugs

```
Look for bugs or problems in this code and suggest fixes:

<PASTE YOUR CODE HERE>
```

### Add comments

```
Add clear comments to this code so a beginner can understand it:

<PASTE YOUR CODE HERE>
```

### Turn plain English into code

```
Write a Python script that <PLAIN ENGLISH DESCRIPTION OF WHAT YOU WANT>.
Save it as <filename>.py and show me how to run it.
```

Tip: start small. Ask for one function at a time instead of a whole program.

---

## 6. Debugging help

When your code breaks, you can ask a local model for help — just never paste
passwords, API keys, or real customer data (see Section 7).

### Debugging prompt template

```
This Python code is supposed to <WHAT IT SHOULD DO>, but instead it
<WHAT IT ACTUALLY DOES>. Here is the error message:

<PASTE THE ERROR MESSAGE>

Here is the code:

<PASTE YOUR CODE>

Suggest a fix and explain what went wrong in simple terms.
```

### Example

Suppose `calc.py` crashes:

```python
def total(prices):
    return sum(prices)

print(total(["10", "20", "30"]))
```

Error: `TypeError: unsupported operand type(s) for +: 'int' and 'str'`

Paste the code and error into Ollama:

```
This code should add up a list of prices, but it crashes with
TypeError: unsupported operand type(s) for +: 'int' and 'str'.

def total(prices):
    return sum(prices)

print(total(["10", "20", "30"]))

Suggest a fix and explain what went wrong.
```

The model will likely suggest converting the strings to numbers before adding
them. Try the fix, run the code again, and see if it works.

### If the model's fix does not work

Paste the new error message back and ask again:

```
I tried your fix and now I get this error:

<PASTE NEW ERROR>

Here is my updated code:

<PASTE UPDATED CODE>

What should I change next?
```

---

## 7. Privacy-safe habits

Local AI is private by default, but your habits matter more than the tool.

### Do

- Run models locally with Ollama
- Keep API keys, passwords, and tokens out of your code and out of your prompts
- Use fake names and fake data in examples (`"Dylan"`, `"123 Fake Street"`,
  `555-0100`)
- Review code before you run it, even if AI wrote it
- Keep Ollama and your models updated

### Do not

- Do not paste real API keys (`sk-...`, `ghp_...`, etc.) into any prompt
- Do not paste real customer names, addresses, or health information
- Do not run code from AI without reading it first
- Do not share your local models' output containing secrets online

### Where secrets belong

If you eventually need real secrets (for example, to connect to a database),
store them in environment variables or a `.env` file, never pasted into a chat.
Never commit real secrets to GitHub.

---

## 8. Printable cheat sheet

A one-page printable cheat sheet is included:

- Markdown: `docs/cheat-sheet.md`
- HTML: `site/cheat-sheet.html` (press Ctrl+P or Cmd+P to print)

Print it and keep it on your desk.

---

## 9. What to try next

- Pull a bigger model if your computer handles it well
- Try tools that connect Ollama to your code editor (look for "Ollama"
  extensions for VS Code or your editor of choice)
- Keep a folder of prompts that worked for you
- Explore other free local AI tools when you are ready

---

## Credits

Created and maintained by **Asdale Dynamics, LLC** (Indiana), beginner-friendly
AI education, books, and practical tools. Dylan Asdale is the founder and the
author of *The Massive AI Manual*. Hub site: https://dylanasdale.github.io

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.
