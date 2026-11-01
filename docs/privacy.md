# Privacy-Safe Habits

How to use local AI coding tools while keeping your code, secrets, and data on
your own machine.

---

## Local-first means private by default

When you run models through Ollama on your own computer:

- Your prompts stay on your computer
- Your code stays on your computer
- No company reads your code or questions
- No internet is needed after you download the model

Ollama does not require an account, and it does not need an API key. That means
there is no account to leak and no key to steal.

---

## Daily privacy checklist

Before you paste anything into any AI tool, ask:

- [ ] Does this contain a password?
- [ ] Does this contain an API key or secret token?
- [ ] Does this contain a real customer, patient, or employee name?
- [ ] Does this contain an address, phone number, or ID number?
- [ ] Am I using fake example data instead?

If the answer to any of the first four is "yes," do not paste it. Replace real
data with fake data first.

---

## Do and do not

| Do | Do not |
|----|--------|
| Run models locally with Ollama | Paste `sk-...`, `ghp_...`, or other API keys into prompts |
| Use fake names (`"Dylan"`, `"123 Fake Street"`, `555-0100`) | Paste real patient or customer information |
| Keep secrets in environment variables or `.env` files | Paste secrets into code you might commit |
| Read AI-written code before running it | Run code from AI without checking it |
| Keep Ollama and models updated | Share AI output that contains secrets online |

---

## Where real secrets belong

If your project genuinely needs a secret (for example, a database password):

1. Store it in an environment variable or a `.env` file
2. Never paste it into an AI prompt
3. Add `.env` to your `.gitignore` so it is never committed
4. Never upload `.env` or files with real keys to GitHub

Example `.gitignore`:

```
.env
*.key
*.pem
secrets/
```

---

## About this guide

This guide is educational. It is not medical advice, legal advice, or a
substitute for professional security review. If you handle regulated data
(healthcare, finance, etc.), consult your organization's compliance rules
before using AI tools with that data.

---

## Credits

Created and maintained by **Asdale Dynamics, LLC** (Indiana). Dylan Asdale is
the founder and author of *The Massive AI Manual*. Hub site:
https://dylanasdale.github.io

License: MIT. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.
