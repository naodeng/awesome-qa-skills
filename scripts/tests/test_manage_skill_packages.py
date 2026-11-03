"""TDD coverage for standalone Skill packaging and safe install cleanup."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "manage_skill_packages.py"


class ManageSkillPackagesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def make_skill(self, path: Path, name: str = "sample-skill") -> None:
        (path / "agents").mkdir(parents=True)
        (path / "prompts").mkdir()
        (path / "evals" / "cases").mkdir(parents=True)
        (path / "SKILL.md").write_text(f"---\nname: {name}\n---\n# Sample\n", encoding="utf-8")
        (path / "agents" / "openai.yaml").write_text("version: 1\n", encoding="utf-8")
        (path / "prompts" / f"{name}.md").write_text("prompt\n", encoding="utf-8")
        (path / "evals" / "eval.yaml").write_text("{}\n", encoding="utf-8")

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_pack_creates_leaf_only_zip_with_relative_paths(self) -> None:
        source = self.root / "sample-skill"
        self.make_skill(source)
        output = self.root / "sample-skill.zip"

        result = self.run_cli("pack", "--skill-dir", str(source), "--output", str(output))

        self.assertEqual(result.returncode, 0, result.stderr)
        import zipfile

        with zipfile.ZipFile(output) as archive:
            names = set(archive.namelist())
        self.assertIn("SKILL.md", names)
        self.assertIn("agents/openai.yaml", names)
        self.assertNotIn("sample-skill/SKILL.md", names)
        self.assertNotIn("../SKILL.md", names)

    def test_pack_rejects_manifest_directory_name_mismatch(self) -> None:
        source = self.root / "sample-skill"
        self.make_skill(source, name="other-skill")
        result = self.run_cli("pack", "--skill-dir", str(source), "--output", str(self.root / "x.zip"))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("name", result.stderr)

    def test_uninstall_defaults_to_dry_run_and_apply_removes_only_named_leaf(self) -> None:
        install_root = self.root / "installed"
        package = install_root / "sample-skill"
        package.mkdir(parents=True)
        (package / "SKILL.md").write_text("skill", encoding="utf-8")
        other = install_root / "keep-me"
        other.mkdir()

        preview = self.run_cli("uninstall", "--install-root", str(install_root), "--skill", "sample-skill")
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertTrue(package.exists())
        self.assertIn("DRY_RUN", preview.stdout)

        applied = self.run_cli("uninstall", "--install-root", str(install_root), "--skill", "sample-skill", "--apply")
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertFalse(package.exists())
        self.assertTrue(other.exists())

    def test_uninstall_rejects_symlink_package(self) -> None:
        install_root = self.root / "installed"
        install_root.mkdir()
        target = self.root / "outside"
        target.mkdir()
        (target / "keep.txt").write_text("keep", encoding="utf-8")
        (install_root / "sample-skill").symlink_to(target, target_is_directory=True)

        result = self.run_cli("uninstall", "--install-root", str(install_root), "--skill", "sample-skill", "--apply")
        self.assertNotEqual(result.returncode, 0)
        self.assertTrue((target / "keep.txt").exists())

    def test_residue_check_reports_legacy_and_unknown_packages(self) -> None:
        repo = self.root / "repo"
        for language in ("zh", "en"):
            (repo / "skills" / language / "testing-workflows" / "sample-skill").mkdir(parents=True)
        install_root = self.root / "installed"
        for slug, declared in (("sample-skill-en", "sample-skill"), ("retired-skill", "retired-skill")):
            path = install_root / slug
            path.mkdir(parents=True)
            (path / "SKILL.md").write_text(f"---\nname: {declared}\n---\n", encoding="utf-8")

        result = self.run_cli(
            "check-residue", "--install-root", str(install_root), "--repo-root", str(repo), "--json"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        findings = json.loads(result.stdout)
        self.assertEqual({finding["path"] for finding in findings}, {"sample-skill-en", "retired-skill"})
        self.assertTrue(any(finding["kind"] == "legacy-language-suffix" for finding in findings))
        self.assertTrue(any(finding["kind"] == "not-in-repository" for finding in findings))

    def test_residue_check_finds_packages_in_installer_language_layout(self) -> None:
        repo = self.root / "repo"
        (repo / "skills" / "zh" / "testing-workflows" / "sample-skill").mkdir(parents=True)
        install_root = self.root / "installed"
        legacy = install_root / "en" / "testing-workflows" / "sample-skill-en"
        legacy.mkdir(parents=True)
        (legacy / "SKILL.md").write_text("---\nname: sample-skill\n---\n", encoding="utf-8")
        retired = install_root / "zh" / "testing-types" / "retired-skill"
        retired.mkdir(parents=True)
        (retired / "SKILL.md").write_text("---\nname: retired-skill\n---\n", encoding="utf-8")

        result = self.run_cli(
            "check-residue", "--install-root", str(install_root), "--repo-root", str(repo), "--json"
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        findings = json.loads(result.stdout)
        self.assertEqual(
            {finding["path"] for finding in findings},
            {"en/testing-workflows/sample-skill-en", "zh/testing-types/retired-skill"},
        )
        self.assertTrue(any(finding["kind"] == "legacy-language-suffix" for finding in findings))
        self.assertTrue(any(finding["kind"] == "not-in-repository" for finding in findings))


if __name__ == "__main__":
    unittest.main()
