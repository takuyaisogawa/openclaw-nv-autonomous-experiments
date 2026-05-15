#!/usr/bin/env python3
"""Compile a LaTeX report for OpenClaw project deliverables.

The project agents use this wrapper instead of guessing which TeX engine is
available. It prefers the pinned local Tectonic binary installed under
~/.openclaw/tools, then falls back to PATH engines.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


DEFAULT_TECTONIC = Path(os.environ.get("OPENCLAW_TECTONIC", "tectonic")).expanduser()
WARNING_RE = re.compile(
    r"(^!|Overfull \\hbox|Undefined control sequence|LaTeX Warning:|Package .* Warning:)",
    re.MULTILINE,
)


def find_engine(preferred: str | None = None) -> tuple[str, list[str]]:
    candidates: list[str] = []
    if preferred:
        candidates.append(preferred)
    env_engine = os.environ.get("OPENCLAW_LATEX_ENGINE")
    if env_engine:
        candidates.append(env_engine)
    candidates.append(str(DEFAULT_TECTONIC))
    for name in ("tectonic", "latexmk", "xelatex", "pdflatex", "lualatex"):
        found = shutil.which(name)
        if found:
            candidates.append(found)

    seen: set[str] = set()
    checked: list[str] = []
    for candidate in candidates:
        if not candidate or candidate in seen:
            continue
        seen.add(candidate)
        checked.append(candidate)
        path = Path(candidate)
        if path.exists() and os.access(path, os.X_OK):
            return candidate, checked
        found = shutil.which(candidate)
        if found:
            return found, checked
    raise FileNotFoundError(
        "No LaTeX engine found. Install Tectonic at "
        f"{DEFAULT_TECTONIC} or set OPENCLAW_LATEX_ENGINE."
    )


def run_command(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def command_for_engine(engine: str, tex_path: Path) -> list[str]:
    name = Path(engine).name.lower()
    if name == "tectonic":
        return [engine, "--keep-logs", "--keep-intermediates", tex_path.name]
    if name == "latexmk":
        return [engine, "-pdf", "-interaction=nonstopmode", "-halt-on-error", tex_path.name]
    if name in {"xelatex", "pdflatex", "lualatex"}:
        return [engine, "-interaction=nonstopmode", "-halt-on-error", tex_path.name]
    return [engine, tex_path.name]


def verify_pdf(pdf_path: Path) -> dict[str, Any]:
    data = pdf_path.read_bytes()
    return {
        "pdf_path": str(pdf_path),
        "exists": pdf_path.exists(),
        "size_bytes": len(data),
        "header": data[:8].decode("ascii", errors="replace"),
        "header_ok": data.startswith(b"%PDF-"),
    }


def log_warnings(log_path: Path) -> list[str]:
    if not log_path.exists():
        return []
    text = log_path.read_text(errors="replace")
    warnings: list[str] = []
    for match in WARNING_RE.finditer(text):
        start = max(0, text.rfind("\n", 0, match.start()) + 1)
        end = text.find("\n", match.end())
        if end == -1:
            end = len(text)
        warnings.append(text[start:end].strip())
    return warnings


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tex", help="Path to the main .tex file")
    parser.add_argument("--engine", default="", help="Optional TeX engine path")
    parser.add_argument("--allow-warnings", action="store_true")
    parser.add_argument("--json", action="store_true", help="Print machine-readable build summary")
    args = parser.parse_args(argv)

    tex_path = Path(args.tex).expanduser().resolve()
    if not tex_path.exists():
        raise SystemExit(f"TeX file not found: {tex_path}")
    if tex_path.suffix.lower() != ".tex":
        raise SystemExit(f"Expected a .tex file, got: {tex_path}")

    engine, checked = find_engine(args.engine or None)
    cmd = command_for_engine(engine, tex_path)
    proc = run_command(cmd, tex_path.parent)

    pdf_path = tex_path.with_suffix(".pdf")
    log_path = tex_path.with_suffix(".log")
    summary: dict[str, Any] = {
        "tex_path": str(tex_path),
        "engine": engine,
        "checked_engines": checked,
        "command": cmd,
        "returncode": proc.returncode,
        "stdout_tail": proc.stdout[-4000:],
        "stderr_tail": proc.stderr[-4000:],
        "log_path": str(log_path),
        "log_warnings": log_warnings(log_path),
        "pdf": verify_pdf(pdf_path) if pdf_path.exists() else {"pdf_path": str(pdf_path), "exists": False},
    }

    ok = proc.returncode == 0 and bool(summary["pdf"].get("header_ok"))
    if summary["log_warnings"] and not args.allow_warnings:
        ok = False

    if args.json:
        print(json.dumps(summary, indent=2, ensure_ascii=False))
    else:
        print(f"engine: {engine}")
        print(f"pdf: {summary['pdf']}")
        if summary["log_warnings"]:
            print("warnings:")
            for warning in summary["log_warnings"]:
                print(f"- {warning}")
        if proc.stdout.strip():
            print(proc.stdout[-1200:])
        if proc.stderr.strip():
            print(proc.stderr[-1200:], file=sys.stderr)

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
