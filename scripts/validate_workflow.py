#!/usr/bin/env python3
"""Validate the template structure and active workflow state."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_FILES = (
    "VERSION",
    "README.md",
    "AGENTS.md",
    "PROJECT.md",
    "PLAN.md",
    "memory/CURRENT.md",
    "memory/DECISIONS.md",
    "work/ACTIVE_TASK.md",
    "work/BACKLOG.md",
    "workflow/OPERATING_MODEL.md",
    "workflow/PROCESS_MAP.md",
    "workflow/REVIEW.md",
    "workflow/WRITING.md",
    "templates/REVIEW_PACKET.md",
    "templates/DECISION.md",
    ".agents/skills/research-task/SKILL.md",
    ".agents/skills/research-review/SKILL.md",
)

ACTIVE_HEADINGS = (
    "Identity",
    "Question in ordinary language",
    "Input and output",
    "What changes in this task",
    "What must remain unchanged",
    "Verification and evidence",
    "Completion conditions",
    "Stop conditions",
    "Human decision gate",
)

VALID_STATUSES = {
    "empty",
    "planned",
    "approved",
    "running",
    "review",
    "blocked",
    "completed",
    "invalidated",
    "superseded",
}

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER_PATTERN = re.compile(r"\{\{[A-Z0-9_]+\}\}")


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def local_markdown_links(path: Path):
    text = path.read_text(encoding="utf-8")
    for match in LINK_PATTERN.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        if target:
            yield target


def validate(root: Path, template_mode: bool = False) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")

    current = root / "memory/CURRENT.md"
    if current.is_file():
        line_count = len(current.read_text(encoding="utf-8").splitlines())
        if line_count > 120:
            errors.append(f"memory/CURRENT.md has {line_count} lines; maximum is 120")

    active = root / "work/ACTIVE_TASK.md"
    if active.is_file():
        text = active.read_text(encoding="utf-8")
        status_match = re.search(r"^Status:\s*([a-z_-]+)\s*$", text, re.MULTILINE)
        if not status_match:
            errors.append("work/ACTIVE_TASK.md has no machine-readable Status line")
        elif status_match.group(1) not in VALID_STATUSES:
            errors.append(f"invalid active task status: {status_match.group(1)}")
        for heading in ACTIVE_HEADINGS:
            if f"## {heading}" not in text:
                errors.append(f"work/ACTIVE_TASK.md is missing heading: {heading}")
        if status_match and status_match.group(1) in {"approved", "running", "review"}:
            if re.search(r"^- Task ID:\s*(NONE|TODO)\s*$", text, re.MULTILINE):
                errors.append("an active task must have a real Task ID")
            if "TODO" in text:
                errors.append("an approved, running, or review task still contains TODO")

    if not template_mode:
        for path in root.rglob("*.md"):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            if PLACEHOLDER_PATTERN.search(text):
                errors.append(f"uninitialized placeholder in {path.relative_to(root)}")

    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for link in local_markdown_links(path):
            destination = (path.parent / link).resolve()
            try:
                destination.relative_to(root.resolve())
            except ValueError:
                errors.append(f"local link escapes repository in {path.relative_to(root)}: {link}")
                continue
            if not destination.exists():
                errors.append(f"broken local link in {path.relative_to(root)}: {link}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=repository_root())
    parser.add_argument(
        "--template",
        action="store_true",
        help="Allow starter placeholders in the uninitialized template repository",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors = validate(root, template_mode=args.template)
    if errors:
        print("Workflow validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"Workflow validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
