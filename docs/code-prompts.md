# Code Prompts

Prompts that actually help you write code with local AI models.

Copy and paste these into Ollama, replacing the bracketed parts with your own
code or task.

---

## How to prompt for code

- Ask for one thing at a time (one function, one script, one fix)
- Say what language you want (Python, JavaScript, HTML, etc.)
- Paste error messages exactly as they appear
- Tell the model your experience level ("explain like I am a beginner")

---

## Prompt library

### Explain code

Use this when you find code you do not understand.

```
Explain this code line by line in simple terms:

<PASTE YOUR CODE HERE>
```

### Write a function

```
Write a Python function that <DESCRIBE WHAT IT DOES>.
Include comments and a short example of how to call it.
```

Example:

```
Write a Python function that checks whether a number is even or odd.
Include comments and a short example of how to call it.
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

### Refactor (make cleaner)

```
Make this code simpler and easier to read. Explain each change:

<PASTE YOUR CODE HERE>
```

### Turn plain English into code

```
Write a Python script that <PLAIN ENGLISH DESCRIPTION>.
Show me how to save and run it.
```

Example:

```
Write a Python script that reads a file called names.txt and prints each name
in uppercase. Show me how to save and run it.
```

### Write comments for a whole file

```
Add a docstring at the top of this file explaining what it does, then comment
each function:

<PASTE YOUR FILE CONTENTS HERE>
```

---

## Example: from prompt to running code

1. Prompt Ollama:

   ```
   Write a Python program that asks for your name and prints a greeting.
   Show me how to save and run it.
   ```

2. Copy the code into a file named `greet.py`.

3. Run it:

   ```
   python greet.py
   ```

4. If it errors, copy the error and your code into the debugging prompt
   (see `docs/debugging.md`).

---

## Prompt tips

| Do this | Not this |
|---------|----------|
| "Write a Python function that..." | "Write code..." |
| Paste the full error message | "It does not work" |
| Ask for one function at a time | "Build me a whole app" |
| Say your language and level | Assume the model knows your setup |

---

## Credits

Created and maintained by **Asdale Dynamics, LLC** (Indiana). Dylan Asdale is
the founder and author of *The Massive AI Manual*. Hub site:
https://dylanasdale.github.io

License: MIT. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.
