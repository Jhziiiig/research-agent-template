from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


release_scan = load_module("check_public_release", ROOT / "scripts/check_public_release.py")


class PublicReleaseTests(unittest.TestCase):
    def test_detects_forbidden_text_and_local_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "note.md").write_text(
                "SecretProject lives at /Users/example/private\n", encoding="utf-8"
            )
            findings = release_scan.scan(root, ["SecretProject"], 5_000_000)
            self.assertTrue(any("forbidden text" in item for item in findings))
            self.assertTrue(any("local macOS path" in item for item in findings))

    def test_clean_text_passes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "note.md").write_text("Public example\n", encoding="utf-8")
            self.assertEqual(release_scan.scan(root, [], 5_000_000), [])


if __name__ == "__main__":
    unittest.main()
