from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from scripts import optimize_skills_skillup as optimizer
from scripts import scaffold_tool_specific_skills as scaffold


class SkillVersionGenerationTests(unittest.TestCase):
    def test_optimizer_preserves_existing_frontmatter_metadata(self):
        with TemporaryDirectory() as temporary:
            skill = Path(temporary) / "demo"
            skill.mkdir()
            path = skill / "SKILL.md"
            path.write_text(
                '---\nname: demo\ndescription: Use this skill when testing.\n'
                'license: MIT\nmetadata:\n  version: "2.3.4"\n'
                '  compatibility: "Known platform"\n  author: "QA"\n---\n\n# Demo\n',
                encoding="utf-8",
            )
            with patch.object(optimizer, "ROOT", Path(temporary)):
                optimizer.optimize_skill(skill)
            output = path.read_text(encoding="utf-8")
            self.assertIn('license: MIT\nmetadata:\n  version: "2.3.4"\n'
                          '  compatibility: "Known platform"\n  author: "QA"\n', output)

    def test_scaffolding_initializes_new_skill_metadata(self):
        for lang in ("zh", "en"):
            with self.subTest(lang=lang):
                output = scaffold.skill_md(scaffold.SKILLS[0], lang)
                language_code = "zh-CN" if lang == "zh" else "en"
                self.assertIn('metadata:\n  version: "1.0.0"\n  compatibility: ""\n', output)
                self.assertIn('license: PolyForm-Noncommercial-1.0.0\n', output)
                self.assertIn('  author: "Awesome QA Skills contributors"\n', output)
                self.assertIn(f'  language: "{language_code}"\n', output)
                self.assertIn('  category: "testing-types"\n', output)
                self.assertIn('  source: "https://github.com/naodeng/awesome-qa-skills"\n', output)
                self.assertIn('  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"\n', output)

    def test_scaffolding_matches_generated_license_url_to_preserved_license(self):
        output = scaffold.skill_md(scaffold.SKILLS[0], "en", license_field="license: >-\n  MIT")

        self.assertIn('license: >-\n  MIT\n', output)
        self.assertIn('license-url: "https://spdx.org/licenses/MIT.html"\n', output)
        self.assertNotIn("polyformproject.org", output)

    def test_optimizer_does_not_confuse_nested_metadata_with_skill_identity(self):
        with TemporaryDirectory() as temporary:
            skill = Path(temporary) / "actual-skill"
            skill.mkdir()
            path = skill / "SKILL.md"
            path.write_text(
                '---\nname: actual-skill\ndescription: Use this skill when testing.\n'
                'metadata:\n  version: "1.0.0"\n  compatibility: ""\n'
                '  name: "Other name"\n  description: "Other description"\n---\n\n# Actual\n',
                encoding="utf-8",
            )
            with patch.object(optimizer, "ROOT", Path(temporary)):
                optimizer.optimize_skill(skill)
            output = path.read_text(encoding="utf-8")
            self.assertIn('name: actual-skill\ndescription: Use this skill when testing.\n', output)
            self.assertIn('  name: "Other name"\n  description: "Other description"\n', output)

    def test_scaffolding_preserves_existing_version_metadata(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            spec = scaffold.SKILLS[0]
            for lang in ("zh", "en"):
                path = root / lang / "testing-types" / spec.skill_id / "SKILL.md"
                path.parent.mkdir(parents=True)
                path.write_text(
                    f'---\nname: {spec.skill_id}\ndescription: Existing.\n'
                    'license: MIT\nmetadata:\n  version: "3.1.4"\n  compatibility: "Known"\n'
                    '  author: "QA"\n---\n\n# Existing\n', encoding="utf-8"
                )
            with patch.object(scaffold, "SKILLS_ROOT", root), patch.object(scaffold, "SKILLS", [spec]):
                scaffold.main()
            for lang in ("zh", "en"):
                output = (root / lang / "testing-types" / spec.skill_id / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn('license: MIT\n', output)
                self.assertIn('metadata:\n  version: "3.1.4"\n'
                              '  compatibility: "Known"\n  author: "QA"\n', output)

    def test_scaffolding_preserves_metadata_across_blank_lines_and_top_level_fields(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            spec = scaffold.SKILLS[0]
            source = (
                f'---\nname: {spec.skill_id}\ndescription: Existing.\n'
                'license: >-\n  MIT\nmetadata:\n  author: "QA contributors"\n\n'
                '  version: "4.2.0"\n  compatibility: "Known platform"\n'
                '  language: "en"\n  category: "testing-types"\n'
                '  source: "https://example.com/repo"\n'
                '  license-url: "https://example.com/license"\n'
                'compatibility: "Top-level compatibility"\n---\n\n# Existing\n'
            )
            for lang in ("zh", "en"):
                path = root / lang / "testing-types" / spec.skill_id / "SKILL.md"
                path.parent.mkdir(parents=True)
                path.write_text(source, encoding="utf-8")
            with patch.object(scaffold, "SKILLS_ROOT", root), patch.object(scaffold, "SKILLS", [spec]):
                scaffold.main()
            for lang in ("zh", "en"):
                output = (root / lang / "testing-types" / spec.skill_id / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn('license: >-\n  MIT\n', output)
                self.assertIn('  author: "QA contributors"\n\n  version: "4.2.0"\n', output)
                self.assertIn('compatibility: "Top-level compatibility"\n', output)


if __name__ == "__main__":
    unittest.main()
