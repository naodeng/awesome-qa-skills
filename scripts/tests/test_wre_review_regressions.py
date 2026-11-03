from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = ("zh", "en")
NEW_WORKFLOW_SKILLS = (
    "change-to-regression",
    "pr-quality-review",
    "requirement-to-test",
)
SKILL_HEADINGS = {
    "zh": (
        "## 何时使用",
        "## 输出格式选项",
        "## 如何使用",
        "## 参考文件",
        "## 常见误区",
        "## 最佳实践",
    ),
    "en": (
        "## When to Use",
        "## Output Format Options",
        "## How to Use",
        "## Reference Files",
        "## Common Pitfalls",
        "## Best Practices",
    ),
}
PROMPT_HEADINGS = {
    "zh": (
        "## 输入",
        "## 你要做的事",
        "## 执行规则",
        "## 最低覆盖清单",
        "## 输出",
        "## 质量要求",
    ),
    "en": (
        "## Input",
        "## What to Do",
        "## Execution Rules",
        "## Minimum Coverage",
        "## Output",
        "## Quality Requirements",
    ),
}


class WREReviewRegressionTests(unittest.TestCase):
    def test_new_workflow_skill_entrypoints_follow_style_guide(self):
        for language in LANGUAGES:
            for slug in NEW_WORKFLOW_SKILLS:
                path = REPO_ROOT / "skills" / language / "testing-workflows" / slug / "SKILL.md"
                text = path.read_text(encoding="utf-8")
                with self.subTest(language=language, slug=slug):
                    positions = [text.index(heading) for heading in SKILL_HEADINGS[language]]
                    self.assertEqual(positions, sorted(positions))

    def test_new_workflow_prompts_follow_style_guide_skeleton(self):
        for language in LANGUAGES:
            for slug in NEW_WORKFLOW_SKILLS:
                path = REPO_ROOT / "skills" / language / "testing-workflows" / slug / "prompts" / f"{slug}.md"
                text = path.read_text(encoding="utf-8")
                with self.subTest(language=language, slug=slug):
                    positions = [text.index(heading) for heading in PROMPT_HEADINGS[language]]
                    self.assertEqual(positions, sorted(positions))

    def test_english_new_skill_descriptions_include_chinese_triggers(self):
        for slug in NEW_WORKFLOW_SKILLS:
            path = REPO_ROOT / "skills" / "en" / "testing-workflows" / slug / "SKILL.md"
            frontmatter = path.read_text(encoding="utf-8").split("---", 2)[1]
            description = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
            with self.subTest(slug=slug):
                self.assertIsNotNone(description)
                self.assertRegex(description.group(1), r"[\u4e00-\u9fff]")

    def test_release_skill_version_is_bumped_in_both_languages(self):
        for language in LANGUAGES:
            path = REPO_ROOT / "skills" / language / "testing-workflows" / "release-testing-workflow" / "SKILL.md"
            text = path.read_text(encoding="utf-8")
            match = re.search(r"(?m)^  version:\s*\"([^\"]+)\"$", text)
            with self.subTest(language=language):
                self.assertIsNotNone(match)
                self.assertNotEqual("1.0.0", match.group(1))

    def test_workflow_outputs_do_not_label_composite_results_as_facts(self):
        paths = sorted((REPO_ROOT / "skills").glob("*/testing-workflows/*/workflow.yaml"))
        paths.append(REPO_ROOT / "resources/workflows/templates/workflow.template.json")
        for path in paths:
            workflow = json.loads(path.read_text(encoding="utf-8"))
            with self.subTest(path=path.relative_to(REPO_ROOT)):
                output_ids = {output["id"] for output in workflow["outputs"]}
                self.assertNotIn("workflow_result", output_ids)
                for output in workflow["outputs"]:
                    description = output["description"].casefold()
                    self.assertFalse(
                        output["evidence_kind"] == "fact"
                        and all(term in description for term in ("result", "evidence", "gap", "handoff")),
                        output,
                    )
        for contract_name in ("WORKFLOW_CONTRACT.md", "WORKFLOW_CONTRACT_EN.md"):
            contract = (REPO_ROOT / "docs/workflows" / contract_name).read_text(encoding="utf-8")
            self.assertIn("workflow_result", contract)

    def test_eval_authoring_policy_distinguishes_raw_runs_from_curated_governance_evidence(self):
        for path in (REPO_ROOT / "skills" / "SKILL_AUTHORING.md", REPO_ROOT / "skills" / "SKILL_AUTHORING_EN.md"):
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path):
                self.assertIn("docs/governance/eval-runs/", text)
                if path.name.endswith("_EN.md"):
                    self.assertIn("curated", text.casefold())
                    self.assertIn(".skill-up-workspaces/<skill>-workspace/", text)
                else:
                    self.assertIn("经筛选", text)
                    self.assertIn("<skill>-workspace/", text)


if __name__ == "__main__":
    unittest.main()
