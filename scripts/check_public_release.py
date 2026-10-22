#!/usr/bin/env python3
"""Heuristically scan a repository before public release."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SKIP_PARTS = {".git", "__pycache__", ".pytest_cache"}
SKIP_SELF = {"scripts/check_public_release.py", "tests/test_public_release.py"}
SUSPICIOUS_NAMES = {".env", "id_rsa", "id_dsa", "credentials.json", "secrets.json"}
PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "local macOS path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "local Linux path": re.compile(r"/home/[A-Za-z0-9._-]+/"),
    "local Windows path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def scan(root: Path, forbidden: list[str], max_bytes: int) -> list[str]:
    findings: list[str] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root).as_posix()
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.is_symlink():
            findings.append(f"symbolic link requires manual review: {relative}")
            continue
        if not path.is_file():
            continue
        if path.name in SUSPICIOUS_NAMES:
            findings.append(f"suspicious filename: {relative}")
        size = path.stat().st_size
        if size > max_bytes:
            findings.append(f"large file ({size} bytes): {relative}")
        if relative in SKIP_SELF or size > max_bytes:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                findings.append(f"possible {label}: {relative}")
        lowered = text.casefold()
        for value in forbidden:
            if value.casefold() in lowered:
                findings.append(f"forbidden text {value!r}: {relative}")
    return sorted(set(findings))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=repository_root())
    parser.add_argument("--forbid", action="append", default=[], help="Project-specific text that must not appear")
    parser.add_argument("--max-bytes", type=int, default=5_000_000)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings = scan(root, args.forbid, args.max_bytes)
    if findings:
        print("Public-release scan found items requiring review:")
        for finding in findings:
            print(f"  - {finding}")
        return 1
    print(f"No heuristic findings: {root}")
    print("Manual review is still required; this scan is not a privacy guarantee.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
