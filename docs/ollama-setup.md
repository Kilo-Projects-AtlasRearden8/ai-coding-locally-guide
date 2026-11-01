# Ollama Setup

Install and run Ollama so you can code with free local AI models.

No account. No API key. Nothing leaves your machine.

---

## What is Ollama?

Ollama is a free, open-source tool that lets you download and run AI models on
your own computer. Think of it like a music player: Ollama is the player, and
the AI model is the song. You install Ollama once, then "pull" whichever models
you want to use.

Because the model runs on your computer, your code and questions never leave
your machine.

---

## Step 1: Install Ollama

1. Open your web browser and go to https://ollama.com
2. Click the download button for your computer:
   - Windows — download the Windows installer
   - Mac — download the Mac version
   - Linux — use the install script or download the package
3. Run the installer and follow the on-screen prompts. Accept the defaults.

---

## Step 2: Verify the installation

Open a terminal:

- Windows: Command Prompt or PowerShell
- Mac: Terminal
- Linux: your terminal application

Type:

```
ollama --version
```

You should see something like:

```
ollama version is 0.6.x
```

If you see an error like "ollama: command not found", close and reopen your
terminal, then try again. On Linux you may need to log out and back in.

---

## Step 3: Confirm Ollama is running

Ollama runs quietly in the background. Check it:

```
ollama list
```

Expected output:

```
NAME            SIZE    MODIFIED
```

An empty list is normal — you have not downloaded any models yet. No error
message means Ollama is working.

---

## Step 4: Pull a coding model

Choose a model and download it. Recommended for beginners:

| Model | Size | Good for |
|-------|------|----------|
| `qwen2.5-coder:3b` | ~2 GB | Learning, fast answers, older computers |
| `deepseek-coder:6.7b` | ~4 GB | Stronger coding help |
| `codellama:7b` | ~4 GB | All-around coding assistant |

Pull one now:

```
ollama pull qwen2.5-coder:3b
```

Wait for the download to finish. You only need to do this once per model.

---

## Step 5: Chat with your model

```
ollama run qwen2.5-coder:3b
```

Type a question and press Enter:

```
>>> Write a Python function that adds two numbers
```

Ollama answers right in your terminal. Type `/bye` to exit, or press Ctrl+D.

---

## Quick command reference

| Command | What it does |
|---------|--------------|
| `ollama --version` | Shows the installed Ollama version |
| `ollama list` | Lists models on your machine |
| `ollama pull <model>` | Downloads a model |
| `ollama run <model>` | Starts a chat session |
| `/bye` | Exits a chat session (inside `ollama run`) |
| `ollama stop <model>` | Stops a running model |
| `ollama rm <model>` | Deletes a model to free disk space |

---

## Troubleshooting

**Problem: `ollama` command not found**

- Restart your terminal. On Linux, log out and back in after installing.

**Problem: Download is slow or fails**

- Check your internet connection. You only need internet to download the model;
  after that, everything works offline.

**Problem: Model runs slowly or your computer gets hot**

- Try the smaller `qwen2.5-coder:3b` model. Close other heavy programs while
  chatting. Models run faster on computers with a graphics card (GPU), but a
  processor (CPU) works fine too.

**Problem: "Connection refused" when running a model**

- Make sure the Ollama background service is running. Restart your computer and
  try `ollama list` again.

---

## Credits

Created and maintained by **Asdale Dynamics, LLC** (Indiana). Dylan Asdale is
the founder and author of *The Massive AI Manual*. Hub site:
https://dylanasdale.github.io

License: MIT. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.
