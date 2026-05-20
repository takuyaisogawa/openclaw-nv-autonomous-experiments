#!/usr/bin/env python3
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATTERNS = [
    ("windows_absolute_path", re.compile(r"[A-Za-z]:\\")),
    ("private_unc_path", re.compile(r"\\\\18\.25\.10\.245")),
    ("private_unc_url", re.compile(r"//18\.25\.10\.245")),
    ("home_path", re.compile(r"/home/")),
    ("mnt_path", re.compile(r"/mnt/")),
    ("original_case_id", re.compile(r"podmr_\d{3}_")),
    ("api_key", re.compile(r"api[_-]?key", re.I)),
    ("secret", re.compile(r"secret", re.I)),
    ("password", re.compile(r"password", re.I)),
    ("token", re.compile(r"token", re.I)),
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
    for name, pattern in PATTERNS:
        if name == "original_case_id" and "analysis_notes" in path.parts:
            continue
        if pattern.search(text):
            bad.append((path.relative_to(ROOT), name))
            break

if bad:
    for path, name in bad:
        print(f"redaction hit: {path} pattern={name}")
    sys.exit(1)
print("public package verification passed")
