#!/usr/bin/env python3
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATTERNS = [
    re.compile(r"[A-Za-z]:\\"),
    re.compile(r"\\\\18\.25\.10\.245"),
    re.compile(r"//18\.25\.10\.245"),
    re.compile(r"/home/"),
    re.compile(r"/mnt/"),
    re.compile(r"podmr_\d{3}_"),
    re.compile(r"api[_-]?key", re.I),
    re.compile(r"secret", re.I),
    re.compile(r"password", re.I),
    re.compile(r"token", re.I),
]

bad = []
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix.lower() in {".png"}:
        continue
    if path.parts[-2:] and "scripts" in path.parts:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    for pattern in PATTERNS:
        if pattern.search(text):
            bad.append((path.relative_to(ROOT), pattern.pattern))
            break

if bad:
    for path, pattern in bad:
        print(f"redaction hit: {path} pattern={pattern}")
    sys.exit(1)
print("public package verification passed")
