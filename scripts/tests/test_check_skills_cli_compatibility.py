from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "scripts" / "check_skills_cli_compatibility.py"
REPRESENTATIVE_NAMES = (
    "requirements-analysis",
    "functional-testing",
    "api-testing",
    "performance-testing",
    "ai-agent-testing",
    "release-testing-workflow",
    "skill-change-verification",
)


class SkillsCliCompatibilityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def write_skill(
        self,
        language: str,
        category: str,
        name: str,
        *,
        description: str = "Use this skill when validating a QA workflow.",
    ) -> Path:
        skill = self.root / "skills" / language / category / name
        (skill / "prompts").mkdir(parents=True)
        (skill / "agents").mkdir()
        (skill / "evals" / "cases").mkdir(parents=True)
        language_code = "zh-CN" if language == "zh" else "en"
        (skill / "SKILL.md").write_text(
            f'---\nname: {name}\ndescription: {description}\n'
            'license: MIT\nmetadata:\n  version: "1.0.0"\n  compatibility: ""\n'
            f'  language: "{language_code}"\n'
            f'  category: "{category}"\n'
            '  author: "QA contributors"\n  source: "https://example.com/repo"\n'
            '  license-url: "https://example.com/license"\n---\n\n'
            f'# {name}\n',
            encoding="utf-8",
        )
        (skill / "prompts" / f"{name}.md").write_text("# Prompt\n", encoding="utf-8")
        (skill / "agents" / "openai.yaml").write_text(
            f'version: 1\nmetadata:\n  key: "{name}"\n', encoding="utf-8"
        )
        (skill / "evals" / "eval.yaml").write_text(
            "schema_version: v1alpha1\n", encoding="utf-8"
        )
        (skill / "evals" / "cases" / "basic.yaml").write_text(
            "id: basic\n", encoding="utf-8"
        )
        return skill

    def write_representative_skills(self, language: str = "en") -> None:
        for index, name in enumerate(REPRESENTATIVE_NAMES):
            self.write_skill(language, "testing-types" if index < 5 else "testing-workflows", name)

    def run_validator(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(VALIDATOR), "--skills-root", str(self.root / "skills"), *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_valid_bilingual_skills_pass_and_emit_summary(self) -> None:
        self.write_representative_skills("en")
        self.write_representative_skills("zh")

        result = self.run_validator("--fail-on-findings")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("skills_scanned=14", result.stdout)
        self.assertIn("findings=0", result.stdout)

    def test_yaml_block_scalar_description_is_accepted(self) -> None:
        self.write_representative_skills("en")
        self.write_representative_skills("zh")
        skill = self.root / "skills" / "en" / "testing-types" / "api-testing" / "SKILL.md"
        skill.write_text(
            "---\n"
            "name: api-testing\n"
            "description: |\n"
            "  Use this skill when validating API contracts.\n"
            "  Include request and response assertions.\n"
            'license: MIT\n'
            'metadata:\n  version: "1.0.0"\n  compatibility: ""\n'
            '  language: "en"\n  category: "testing-types"\n  author: "QA"\n'
            '  source: "https://example.com/repo"\n  license-url: "https://example.com/license"\n'
            "---\n\n"
            "# API Testing\n",
            encoding="utf-8",
        )

        result = self.run_validator("--fail-on-findings")

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_or_invalid_version_metadata_is_rejected(self) -> None:
        self.write_representative_skills("en")
        self.write_representative_skills("zh")
        skill = self.root / "skills" / "en" / "testing-types" / "api-testing" / "SKILL.md"
        for metadata in (
            'metadata:\n  compatibility: ""\n',
            'metadata:\n  version: "1.0"\n  compatibility: ""\n',
            'metadata:\n  version: "1.0.0"\n',
            'metadata:\n  version: "1.0.0"\n  compatibility:\n',
            'metadata:\n  version: "1.0.0"\n  compatibility: [codex]\n',
            'metadata:\n  version: "1.0.0"\n  compatibility: {agent: codex}\n',
        ):
            with self.subTest(metadata=metadata):
                skill.write_text(
                    '---\nname: api-testing\ndescription: Use this skill for API testing.\n'
                    'license: MIT\n'
                    f'{metadata}'
                    '  language: "en"\n  category: "testing-types"\n  author: "QA"\n'
                    '  source: "https://example.com/repo"\n  license-url: "https://example.com/license"\n---\n',
                    encoding="utf-8"
                )
                result = self.run_validator("--fail-on-findings")
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn("metadata", result.stdout)

    def test_semver_prerelease_and_string_compatibility_are_accepted(self) -> None:
        self.write_representative_skills("en")
        self.write_representative_skills("zh")
        skill = self.root / "skills" / "en" / "testing-types" / "api-testing" / "SKILL.md"
        skill.write_text(
            '---\nname: api-testing\ndescription: Use this skill for API testing.\n'
            'license: MIT\n'
            'metadata:\n  version: "2.1.0-rc.1+build.5"\n'
            '  compatibility: "Requires Python 3"\n  author: "QA"\n'
            '  language: "en"\n  category: "testing-types"\n'
            '  source: "https://example.com/repo"\n  license-url: "https://example.com/license"\n---\n',
            encoding="utf-8",
        )
        result = self.run_validator("--fail-on-findings")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_missing_provenance_or_mismatched_package_metadata_is_rejected(self) -> None:
        self.write_representative_skills("en")
        self.write_representative_skills("zh")
        skill = self.root / "skills" / "en" / "testing-types" / "api-testing" / "SKILL.md"
        original = skill.read_text(encoding="utf-8")
        for old, new, finding in (
            ('license: MIT\n', '', 'license'),
            ('  author: "QA contributors"\n', '', 'author'),
            ('  source: "https://example.com/repo"\n', '', 'source'),
            ('  license-url: "https://example.com/license"\n', '', 'license-url'),
            ('  language: "en"', '  language: "zh-CN"', 'language'),
            ('  category: "testing-types"', '  category: "testing-workflows"', 'category'),
        ):
            with self.subTest(finding=finding):
                self.assertIn(old, original)
                skill.write_text(original.replace(old, new), encoding="utf-8")
                result = self.run_validator("--fail-on-findings")
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn(finding, result.stdout)

    def test_contract_findings_include_missing_frontmatter_name_and_description(self) -> None:
        self.write_representative_skills("en")
        skill = self.write_skill("en", "testing-types", "good-name")
        skill.joinpath("SKILL.md").write_text("# no frontmatter\n", encoding="utf-8")
        bad_name = self.write_skill("en", "testing-types", "directory-name")
        bad_name.joinpath("SKILL.md").write_text(
            "---\nname: Wrong_Name\ndescription: \n---\n", encoding="utf-8"
        )

        result = self.run_validator("--fail-on-findings")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("CONTRACT", result.stdout)
        self.assertIn("frontmatter", result.stdout)
        self.assertIn("name", result.stdout)
        self.assertIn("description", result.stdout)

    def test_duplicate_names_are_rejected_within_language_but_not_across_languages(self) -> None:
        self.write_representative_skills("en")
        self.write_representative_skills("zh")
        self.write_skill("en", "testing-types", "same-name")
        self.write_skill("en", "testing-workflows", "same-name")

        result = self.run_validator("--fail-on-findings")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("BILINGUAL", result.stdout)
        self.assertIn("duplicate", result.stdout.lower())

    def test_missing_representative_skill_is_a_discovery_finding(self) -> None:
        self.write_skill("en", "testing-types", "api-testing")

        result = self.run_validator("--fail-on-findings")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("DISCOVERY", result.stdout)
        self.assertIn("requirements-analysis", result.stdout)

    def test_missing_skills_root_is_not_treated_as_a_clean_scan(self) -> None:
        result = self.run_validator("--fail-on-findings")

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("DISCOVERY", result.stdout)
        self.assertIn("skills root", result.stdout.lower())

    def test_json_report_contains_findings_and_summary(self) -> None:
        self.write_representative_skills("en")
        skill = self.root / "skills" / "en" / "testing-types" / "api-testing" / "SKILL.md"
        skill.write_text("# no frontmatter\n", encoding="utf-8")
        report = self.root / "report.json"

        result = self.run_validator("--report-json", str(report), "--fail-on-findings")

        self.assertNotEqual(result.returncode, 0)
        payload = json.loads(report.read_text(encoding="utf-8"))
        self.assertEqual(payload["summary"]["skills_scanned"], 7)
        self.assertTrue(any(item["category"] == "CONTRACT" for item in payload["findings"]))


if __name__ == "__main__":
    unittest.main()
