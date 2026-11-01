# Debugging Help

Use your local AI model to get unstuck when code breaks.

Never paste passwords, API keys, or real customer data into any prompt.

---

## The debugging loop

1. Read the error message
2. Paste the error and your code into Ollama
3. Try the suggested fix
4. Run the code again
5. Repeat if needed

---

## Debugging prompt template

```
This code is supposed to <WHAT IT SHOULD DO>, but instead it
<WHAT IT ACTUALLY DOES>.

Error message:

<PASTE THE COMPLETE ERROR MESSAGE>

Code:

<PASTE YOUR CODE>

Suggest a fix and explain what went wrong in simple terms.
```

---

## Worked example

File `calc.py`:

```python
def total(prices):
    return sum(prices)

print(total(["10", "20", "30"]))
```

Error:

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Prompt to Ollama:

```
This code is supposed to add up a list of prices, but it crashes with
TypeError: unsupported operand type(s) for +: 'int' and 'str'.

Error message:

TypeError: unsupported operand type(s) for +: 'int' and 'str'

Code:

def total(prices):
    return sum(prices)

print(total(["10", "20", "30"]))

Suggest a fix and explain what went wrong in simple terms.
```

Ollama will likely suggest converting the strings to numbers:

```python
def total(prices):
    return sum(float(p) for p in prices)

print(total(["10", "20", "30"]))
```

Copy the fix, save the file, and run it again:

```
python calc.py
```

---

## If the fix does not work

Paste the new error and your updated code back into Ollama:

```
I tried your fix and now I get this error:

<PASTE NEW ERROR MESSAGE>

Here is my updated code:

<PASTE UPDATED CODE>

What should I change next?
```

---

## Safety rules for debugging

| Do | Do not |
|----|--------|
| Use fake names, numbers, and addresses | Paste real API keys (`sk-...`, `ghp_...`) |
| Paste error messages (they usually contain no secrets) | Paste real customer or patient data |
| Read code before you run it | Run AI-suggested code without checking it |
| Remove secrets before sharing code | Commit real secrets to GitHub |

---

## Common beginner errors

| Error | What it usually means |
|-------|----------------------|
| `NameError: name 'x' is not defined` | You used a variable before creating it |
| `TypeError` | You tried to use a value in the wrong way (e.g. adding text to a number) |
| `SyntaxError` | There is a typo, missing colon, or mismatched parenthesis |
| `FileNotFoundError` | The file path is wrong or the file is missing |

When you see one, paste it into Ollama with your code and ask for a fix.

---

## Credits

Created and maintained by **Asdale Dynamics, LLC** (Indiana). Dylan Asdale is
the founder and author of *The Massive AI Manual*. Hub site:
https://dylanasdale.github.io

License: MIT. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.
