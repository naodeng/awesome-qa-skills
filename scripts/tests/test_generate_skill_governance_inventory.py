from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scripts import generate_skill_governance_inventory as inventory


class GovernanceInventoryTest(unittest.TestCase):
    def write_package(self, root: Path, lang: str, slug: str, *, skill: bool = True, inline_cases: bool = False) -> None:
        package = root / "skills" / lang / "testing-workflows" / slug
        (package / "agents").mkdir(parents=True)
        (package / "evals/cases").mkdir(parents=True)
        if skill:
            (package / "SKILL.md").write_text(
                f"---\nname: {slug}\ndescription: {lang} description\n---\n",
                encoding="utf-8",
            )
        (package / "agents/openai.yaml").write_text(f"metadata:\n  key: {slug}\n", encoding="utf-8")
        files = "files: [evals/cases/a.yaml, evals/cases/b.yaml]" if inline_cases else "files:\n  - evals/cases/a.yaml\n  - evals/cases/b.yaml"
        (package / "evals/eval.yaml").write_text(files, encoding="utf-8")
        (package / "evals/cases/a.yaml").write_text("id: a\n", encoding="utf-8")
        (package / "evals/cases/b.yaml").write_text("id: b\n", encoding="utf-8")

    def prepare_root(self, root: Path) -> None:
        for lang in inventory.LANGUAGES:
            for section in inventory.SECTIONS:
                (root / "skills" / lang / section).mkdir(parents=True, exist_ok=True)
        (root / "docs/catalog").mkdir(parents=True)
        (root / "docs/catalog/skills-index.md").write_text("# catalog\n", encoding="utf-8")

    def test_counts_inline_eval_case_declarations(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            package = root / "skill"
            (package / "evals/cases").mkdir(parents=True)
            (package / "evals/eval.yaml").write_text(
                "files: [evals/cases/a.yaml, evals/cases/b.yaml]\n", encoding="utf-8"
            )
            (package / "evals/cases/a.yaml").write_text("id: a\n", encoding="utf-8")
            (package / "evals/cases/b.yaml").write_text("id: b\n", encoding="utf-8")
            _, summary = inventory.eval_structure(package)
            self.assertIn("declared=2", summary)

    def test_records_english_only_package_as_structural_gap(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            self.prepare_root(root)
            self.write_package(root, "en", "english-only")
            with patch.object(inventory, "ROOT", root):
                rows = inventory.records()
            self.assertEqual([row.slug for row in rows], ["english-only"])
            self.assertEqual(rows[0].status, "UNASSESSED (structural gap)")

    def test_records_missing_skill_file_as_structural_gap(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            self.prepare_root(root)
            self.write_package(root, "zh", "missing-skill")
            self.write_package(root, "en", "missing-skill", skill=False)
            with patch.object(inventory, "ROOT", root):
                rows = inventory.records()
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0].status, "UNASSESSED (structural gap)")


if __name__ == "__main__":
    unittest.main()
