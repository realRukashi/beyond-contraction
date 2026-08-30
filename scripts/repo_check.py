#!/usr/bin/env python3
"""Small pre-release check: parse notebooks, scan obvious secret patterns, and report sizes."""
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parents[1]
patterns = {
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    "Hugging Face token": re.compile(r"hf_[A-Za-z0-9]{20,}"),
    "GitHub PAT": re.compile(r"(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
}
problems = []
for p in ROOT.rglob("*.ipynb"):
    text = p.read_text(encoding="utf-8")
    try:
        json.loads(text)
    except Exception as e:
        problems.append(f"invalid notebook {p}: {e}")
    for name, pattern in patterns.items():
        if pattern.search(text): problems.append(f"possible {name} in {p}")
    size_mb = p.stat().st_size / 1024**2
    print(f"{p.relative_to(ROOT)}: {size_mb:.2f} MiB")
if problems:
    print("\nProblems:")
    for x in problems: print("-", x)
    sys.exit(1)
print("\nRepository notebook check passed.")
