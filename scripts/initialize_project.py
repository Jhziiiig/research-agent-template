#!/usr/bin/env python3
"""Initialize a repository created from research-agent-template."""

from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path


TOKENS = {
    "{{PROJECT_NAME}}": "name",
    "{{PROJECT_PURPOSE}}": "purpose",
    "{{OWNER}}": "owner",
}


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def text_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() in {".md", ".yaml", ".yml"}:
            yield path


def initialize(root: Path, values: dict[str, str], force: bool = False) -> list[Path]:
    marker = root / ".template-initialized.json"
    if marker.exists() and not force:
        raise RuntimeError(
            f"{marker.name} already exists; use --force only when reapplying these fields is intended"
        )

    changed: list[Path] = []
    replacements = {token: values[key] for token, key in TOKENS.items()}
    replacements["YYYY-MM-DD"] = dt.date.today().isoformat()

    for path in text_files(root):
        original = path.read_text(encoding="utf-8")
        updated = original
        for token, value in replacements.items():
            updated = updated.replace(token, value)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(path)

    marker.write_text(
        json.dumps(
            {
                "template": "research-agent-template",
                "template_version": "0.1.0",
                "initialized_on": dt.date.today().isoformat(),
                **values,
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    changed.append(marker)
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True, help="Project name")
    parser.add_argument("--purpose", required=True, help="One-sentence project purpose")
    parser.add_argument("--owner", required=True, help="Human owner or team")
    parser.add_argument("--root", type=Path, default=repository_root())
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if not (root / "AGENTS.md").is_file():
        raise SystemExit(f"Not a template repository root: {root}")
    try:
        changed = initialize(
            root,
            {"name": args.name, "purpose": args.purpose, "owner": args.owner},
            force=args.force,
        )
    except RuntimeError as exc:
        raise SystemExit(str(exc)) from exc
    print(f"Initialized {root}")
    for path in changed:
        print(f"  updated {path.relative_to(root)}")
    print("Next: complete PROJECT.md, PLAN.md, and work/ACTIVE_TASK.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
