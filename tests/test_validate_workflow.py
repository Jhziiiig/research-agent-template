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


validator = load_module("validate_workflow", ROOT / "scripts/validate_workflow.py")


class ValidateWorkflowTests(unittest.TestCase):
    def test_template_repository_is_structurally_valid(self):
        self.assertEqual(validator.validate(ROOT, template_mode=True), [])

    def test_running_task_requires_real_id(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in validator.REQUIRED_FILES:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# Placeholder\n", encoding="utf-8")
            headings = "\n".join(f"## {heading}\n" for heading in validator.ACTIVE_HEADINGS)
            (root / "work/ACTIVE_TASK.md").write_text(
                f"# Active task\n\nStatus: running\n\n- Task ID: NONE\n\n{headings}",
                encoding="utf-8",
            )
            errors = validator.validate(root, template_mode=True)
            self.assertTrue(any("real Task ID" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
