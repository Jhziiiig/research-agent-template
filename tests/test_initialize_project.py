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


initializer = load_module("initialize_project", ROOT / "scripts/initialize_project.py")


class InitializeProjectTests(unittest.TestCase):
    def test_replaces_project_tokens_and_writes_marker(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "AGENTS.md").write_text("owner={{OWNER}}\n", encoding="utf-8")
            (root / "PROJECT.md").write_text(
                "{{PROJECT_NAME}}\n{{PROJECT_PURPOSE}}\nYYYY-MM-DD\n", encoding="utf-8"
            )
            changed = initializer.initialize(
                root,
                {"name": "Example", "purpose": "Test a method", "owner": "Team"},
            )
            self.assertIn(root / "PROJECT.md", changed)
            self.assertEqual((root / "AGENTS.md").read_text(encoding="utf-8"), "owner=Team\n")
            text = (root / "PROJECT.md").read_text(encoding="utf-8")
            self.assertIn("Example", text)
            self.assertIn("Test a method", text)
            self.assertNotIn("{{", text)
            self.assertTrue((root / ".template-initialized.json").is_file())

    def test_refuses_second_initialization_without_force(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "AGENTS.md").write_text("{{OWNER}}\n", encoding="utf-8")
            values = {"name": "Example", "purpose": "Test", "owner": "Team"}
            initializer.initialize(root, values)
            with self.assertRaises(RuntimeError):
                initializer.initialize(root, values)


if __name__ == "__main__":
    unittest.main()
