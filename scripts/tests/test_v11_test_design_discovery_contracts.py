from __future__ import annotations

import csv
import json
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = ("zh", "en")
TRIGGER_MODES = {"explicit", "implicit", "contextual", "negative"}

NEW_SLUGS = (
    "test-gap-analysis",
    "risk-based-testing",
    "edge-case-discovery",
    "negative-scenario-discovery",
    "test-data-requirement-analysis",
)

PACKAGE_MARKERS = {
    "test-gap-analysis": {
        "artifact": ("TG-",),
        "boundary": (
            "not a coverage claim",
            "not coverage proof",
            "not full coverage",
            "不等同于覆盖",
            "覆盖证明",
            "不把缺口写成覆盖",
        ),
    },
    "risk-based-testing": {
        "artifact": ("RBT-",),
        "boundary": ("not a full test strategy", "不生成完整测试策略"),
    },
    "edge-case-discovery": {
        "artifact": ("EC-",),
        "boundary": ("do not invent thresholds", "不发明阈值"),
    },
    "negative-scenario-discovery": {
        "artifact": ("NS-",),
        "boundary": ("do not run fault injection", "不执行故障注入"),
    },
    "test-data-requirement-analysis": {
        "artifact": ("TDR-",),
        "boundary": ("do not generate data", "不生成数据"),
    },
}

AUDIT_MARKERS = {
    "zh": ("已知事实", "信息缺口", "冲突", "过期", "范围外", "假设"),
    "en": ("known", "missing", "conflicting", "stale", "out_of_scope", "assumptions"),
}


def package_path(language: str, slug: str) -> Path:
    return REPO_ROOT / "skills" / language / "testing-types" / slug


def read_trigger_rows(package: Path) -> list[dict[str, str]]:
    with (package / "evals" / "trigger-prompts.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        return list(csv.DictReader(stream))


class V11TestDesignDiscoveryContractTest(unittest.TestCase):
    def test_new_packages_have_required_bilingual_contract(self):
        required_cases = (
            "basic-success.yaml",
            "edge-incomplete-input.yaml",
            "edge-scope-boundary.yaml",
        )

        for language in LANGUAGES:
            for slug in NEW_SLUGS:
                package = package_path(language, slug)
                for relative_path in ("SKILL.md", "agents/openai.yaml", "evals/eval.yaml"):
                    self.assertTrue((package / relative_path).is_file(), package / relative_path)
                self.assertTrue(
                    (package / "prompts" / f"{slug}.md").is_file(),
                    package / "prompts" / f"{slug}.md",
                )
                for case_name in required_cases:
                    self.assertTrue(
                        (package / "evals" / "cases" / case_name).is_file(),
                        package / case_name,
                    )

                skill_text = (package / "SKILL.md").read_text(encoding="utf-8")
                prompt_text = (package / "prompts" / f"{slug}.md").read_text(encoding="utf-8")
                combined = f"{skill_text}\n{prompt_text}"
                normalized = combined.casefold()

                for marker in AUDIT_MARKERS[language]:
                    self.assertIn(marker.casefold(), normalized, f"missing audit marker {marker}: {package}")
                self.assertTrue(
                    any(marker.casefold() in normalized for marker in PACKAGE_MARKERS[slug]["artifact"]),
                    f"missing artifact marker for {package}",
                )
                self.assertTrue(
                    any(marker.casefold() in normalized for marker in PACKAGE_MARKERS[slug]["boundary"]),
                    f"missing boundary marker for {package}",
                )

                rows = read_trigger_rows(package)
                self.assertEqual({row.get("mode") for row in rows}, TRIGGER_MODES, package)
                self.assertEqual({row.get("should_trigger") for row in rows}, {"true", "false"}, package)
                self.assertEqual(len(rows), len({row.get("id") for row in rows}), package)
                self.assertTrue(all((row.get("prompt") or "").strip() for row in rows), package)

                rules = json.loads(
                    (package / "evals" / "local-rules.json").read_text(encoding="utf-8")
                )
                self.assertEqual(rules.get("skill"), slug, package)


if __name__ == "__main__":
    unittest.main()
