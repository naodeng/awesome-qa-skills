from __future__ import annotations

import json
import re
import tempfile
import unittest
from pathlib import Path

from scripts import generate_skill_composition_views as generator


MINIMAL_MANIFEST = {
    "format": "json-compatible-yaml",
    "version": 1,
    "routes": [
        {
            "id": "new-feature-quality",
            "label": {"zh": "新功能质量准备", "en": "New feature quality readiness"},
            "intent": {"zh": "把需求转成可测试目标", "en": "Turn a requirement into testable goals"},
            "phase": {"zh": "需求分析", "en": "Requirements analysis"},
            "not_for": {
                "zh": ["不执行目标测试"],
                "en": ["Does not execute target tests"],
            },
            "primary": "requirements-analysis",
            "optional": "test-strategy",
            "handoff": {
                "zh": "交接风险与验收条件",
                "en": "Hand off risks and acceptance conditions",
            },
        }
    ],
    "relations": [],
}


class SkillCompositionViewGeneratorTest(unittest.TestCase):
    def prepare_root(self, root: Path) -> None:
        (root / "docs/governance").mkdir(parents=True)
        (root / "skills/zh/testing-types/requirements-analysis").mkdir(parents=True)
        (root / "skills/en/testing-types/requirements-analysis").mkdir(parents=True)
        (root / "skills/zh/testing-types/test-strategy").mkdir(parents=True)
        (root / "skills/en/testing-types/test-strategy").mkdir(parents=True)
        (root / "skills/zh/testing-workflows/discover-testing").mkdir(parents=True)
        (root / "skills/en/testing-workflows/discover-testing").mkdir(parents=True)
        for language in ("zh", "en"):
            for slug in ("requirements-analysis", "test-strategy"):
                (root / "skills" / language / "testing-types" / slug / "SKILL.md").write_text(
                    f"---\nname: {slug}\n---\n", encoding="utf-8"
                )
        (root / "docs/governance/skill-composition.yaml").write_text(
            json.dumps(MINIMAL_MANIFEST, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    def test_generates_bilingual_self_contained_reference_and_catalog(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.prepare_root(root)
            generated = generator.generate_views(root)

            self.assertEqual(len(generated), 4)
            zh_reference = (root / "skills/zh/testing-workflows/discover-testing/reference.md").read_text(
                encoding="utf-8"
            )
            en_reference = (root / "skills/en/testing-workflows/discover-testing/reference.md").read_text(
                encoding="utf-8"
            )
            zh_catalog = (root / "docs/catalog/skills-composition.md").read_text(encoding="utf-8")
            en_catalog = (root / "docs/catalog/skills-composition_EN.md").read_text(encoding="utf-8")

            self.assertIn("新功能质量准备", zh_reference)
            self.assertIn("requirements-analysis", zh_reference)
            self.assertIn("test-strategy", zh_reference)
            self.assertIn("需求分析", zh_reference)
            self.assertIn("不执行目标测试", zh_reference)
            self.assertIn("New feature quality readiness", en_reference)
            self.assertIn("Requirements analysis", en_reference)
            self.assertIn("Does not execute target tests", en_reference)
            self.assertIn("skills/zh/testing-types/requirements-analysis", zh_catalog)
            self.assertIn("skills/en/testing-types/requirements-analysis", en_catalog)
            self.assertNotIn(str(root), zh_reference + en_reference + zh_catalog + en_catalog)
            self.assertIsNone(re.search(r"\]\([^)]*(?:SKILL\.md|prompts/|agents/|evals/)", zh_reference + en_reference + zh_catalog + en_catalog))
            self.assertNotIn("../", zh_reference + en_reference + zh_catalog + en_catalog)

    def test_check_detects_manually_changed_generated_output(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.prepare_root(root)
            generator.generate_views(root)
            self.assertEqual(generator.stale_outputs(root), [])

            output = root / "docs/catalog/skills-composition.md"
            output.write_text(output.read_text(encoding="utf-8") + "\nmanual edit\n", encoding="utf-8")
            stale = generator.stale_outputs(root)
            self.assertEqual(stale, ["docs/catalog/skills-composition.md"])
            self.assertEqual(generator.main(["--repo-root", str(root), "--check"]), 1)


if __name__ == "__main__":
    unittest.main()
