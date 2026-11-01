#!/usr/bin/env python3
"""Verification for the Free AI Coding with Local Models guide.

Checks file existence, license text, README credit, well-formed HTML,
print styles, secret patterns, and internal links. Exits non-zero on failure.
"""
import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT = os.path.dirname(ROOT)

EXPECTED_FILES = [
    "README.md",
    "LICENSE",
    "STATUS.md",
    "docs/manual.md",
    "docs/ollama-setup.md",
    "docs/code-prompts.md",
    "docs/debugging.md",
    "docs/privacy.md",
    "docs/cheat-sheet.md",
    "site/index.html",
    "site/ollama-setup.html",
    "site/code-prompts.html",
    "site/debugging.html",
    "site/privacy.html",
    "site/cheat-sheet.html",
    "site/style.css",
]

COPYRIGHT_LINE = "Copyright (c) 2026 Asdale Dynamics, LLC"

SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{20,}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"API_KEY\s*=\s*['\"]",
    r"SECRET\s*=\s*['\"]",
    r"AKIA[0-9A-Z]{16}",
    r"password\s*=\s*['\"][^'\"]+['\"]",
]


def read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


class HTMLValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        self.void_elements = {
            "area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr",
        }

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.stack:
            self.errors.append(f"unexpected closing tag </{tag}>")
            return
        if self.stack[-1] != tag:
            self.errors.append(f"closed </{tag}> but expected </{self.stack[-1]}>")
        self.stack.pop()

    @property
    def unclosed(self):
        return [f"unclosed <{t}>" for t in reversed(self.stack)]


def check_files():
    errors = []
    for rel in EXPECTED_FILES:
        path = os.path.join(PROJECT, rel)
        if not os.path.isfile(path):
            errors.append(f"missing file: {rel}")
    return errors


def check_license():
    errors = []
    text = read(os.path.join(PROJECT, "LICENSE"))
    if COPYRIGHT_LINE not in text:
        errors.append("LICENSE missing exact copyright line")
    if "MIT License" not in text:
        errors.append("LICENSE missing MIT License header")
    return errors


def check_readme():
    errors = []
    text = read(os.path.join(PROJECT, "README.md"))
    if "Asdale Dynamics, LLC" not in text:
        errors.append("README does not credit Asdale Dynamics, LLC")
    if COPYRIGHT_LINE not in text:
        errors.append("README missing copyright line")
    return errors


def check_no_workflows():
    path = os.path.join(PROJECT, ".github", "workflows")
    if os.path.isdir(path):
        return [".github/workflows directory present (must not exist)"]
    return []


def check_secrets():
    errors = []
    for dirpath, _, filenames in os.walk(PROJECT):
        parts = dirpath.split(os.sep)
        if ".git" in parts or "verify" in parts:
            continue
        for name in filenames:
            if name == ".gitignore":
                continue
            path = os.path.join(dirpath, name)
            try:
                text = read(path)
            except (OSError, UnicodeDecodeError):
                continue
            rel = os.path.relpath(path, PROJECT)
            for pat in SECRET_PATTERNS:
                if re.search(pat, text, re.IGNORECASE):
                    errors.append(f"possible secret in {rel}: {pat}")
    return errors


def check_html():
    errors = []
    html_files = [
        "site/index.html",
        "site/ollama-setup.html",
        "site/code-prompts.html",
        "site/debugging.html",
        "site/privacy.html",
        "site/cheat-sheet.html",
    ]
    for rel in html_files:
        text = read(os.path.join(PROJECT, rel))
        validator = HTMLValidator()
        validator.feed(text)
        for err in validator.errors + validator.unclosed:
            errors.append(f"{rel}: {err}")
        if "Asdale Dynamics, LLC" not in text:
            errors.append(f"{rel}: missing Asdale Dynamics, LLC credit")
        if rel == "site/cheat-sheet.html" and "@media print" not in text:
            errors.append(f"{rel}: missing print media query")
        # internal links to site files must exist
        for m in re.finditer(r'href="([^"]+)"', text):
            href = m.group(1)
            if href.startswith("http") or href.startswith("#") or href.startswith("../"):
                continue
            target = os.path.join(PROJECT, os.path.dirname(rel), href)
            if not os.path.isfile(target):
                errors.append(f"{rel}: broken link {href}")
    return errors


def main():
    errors = []
    errors += check_files()
    errors += check_license()
    errors += check_readme()
    errors += check_no_workflows()
    errors += check_secrets()
    errors += check_html()

    if errors:
        print("VERIFICATION FAILED")
        for err in errors:
            print(f"  - {err}")
        return 1
    print("VERIFICATION PASSED")
    print(f"  files checked: {len(EXPECTED_FILES)}")
    print(f"  html pages validated: 6")
    print(f"  license copyright line: exact match")
    print(f"  readme credit: present")
    print(f"  secret scan: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
