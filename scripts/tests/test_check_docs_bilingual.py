from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.check_docs_bilingual import check_catalog, check_project_pairs


class DocsBilingualCheckTest(unittest.TestCase):
    def test_reports_missing_english_mirror(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("README_EN.md", encoding="utf-8")
            findings = check_project_pairs(root)
            self.assertIn("missing English mirror: README_EN.md", findings)

    def test_reports_missing_reverse_switch(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("README_EN.md", encoding="utf-8")
            (root / "README_EN.md").write_text("English only", encoding="utf-8")
            findings = check_project_pairs(root)
            self.assertIn("missing Chinese switch link: README_EN.md", findings)

    def test_catalog_reports_duplicate_and_missing_markers(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            for lang in ("zh", "en"):
                (root / f"skills/{lang}/testing-types/alpha").mkdir(parents=True)
                (root / f"skills/{lang}/testing-types/beta").mkdir(parents=True)
            body = "<!-- data-skill:alpha -->\n<!-- data-skill:alpha -->\n"
            (root / "README.md").write_text(body, encoding="utf-8")
            (root / "README_EN.md").write_text(body, encoding="utf-8")
            findings = check_catalog(root)
            self.assertTrue(any("duplicate Skill markers" in item for item in findings))
            self.assertTrue(any("missing Skill markers" in item for item in findings))

    def test_catalog_reports_language_directory_drift(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "skills/zh/testing-types/alpha").mkdir(parents=True)
            (root / "skills/en/testing-types/beta").mkdir(parents=True)
            (root / "README.md").write_text("", encoding="utf-8")
            (root / "README_EN.md").write_text("", encoding="utf-8")
            findings = check_catalog(root)
            self.assertIn("zh/en testing-type directory names differ", findings)


if __name__ == "__main__":
    unittest.main()
