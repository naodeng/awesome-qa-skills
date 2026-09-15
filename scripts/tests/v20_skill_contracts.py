import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = ("zh", "en")
CASES = (
    "basic-success.yaml",
    "edge-incomplete-input.yaml",
    "edge-scope-boundary.yaml",
)
SHARED_AUDIT_TERMS = (
    "known",
    "missing",
    "conflicting",
    "stale",
    "out_of_scope",
    "assumptions",
)
SHARED_SEPARATION_TERMS = {
    "zh": ("事实", "推断", "建议", "Human"),
    "en": ("facts", "inferences", "recommendations", "Human"),
}
OUTPUT_SEPARATION_TERMS = {
    "zh": ("事实", "证据支持的推断", "候选建议", "Human 决策"),
    "en": ("facts", "evidence-backed inferences", "candidate recommendations", "Human decisions"),
}
SHARED_FINDING_TERMS = {
    "zh": (
        "对象/规则",
        "来源",
        "触发条件或适用范围",
        "预期关注点/理由",
        "证据状态",
        "影响/优先级",
        "责任角色",
        "关闭条件",
        "验证方法",
    ),
    "en": (
        "object/rule",
        "source",
        "trigger or applicability",
        "expected concern/rationale",
        "evidence state",
        "impact/priority",
        "owner role",
        "close condition",
        "validation method",
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
        "## What to do",
        "## Execution Rules",
        "## Minimum Coverage Checklist",
        "## Output",
        "## Quality Bar",
    ),
}


class V20SkillContractMixin:
    BATCH = {}
    PLACEHOLDER_FREE = set()
    DOMAIN_MARKERS = {}

    def package(self, language, slug):
        return ROOT / "skills" / language / "testing-types" / slug

    def test_every_bilingual_package_has_required_files(self):
        for language in LANGUAGES:
            for slug in self.BATCH:
                package = self.package(language, slug)
                with self.subTest(language=language, slug=slug):
                    for relative in (
                        "SKILL.md",
                        f"prompts/{slug}.md",
                        "agents/openai.yaml",
                        "evals/eval.yaml",
                        *[f"evals/cases/{case}" for case in CASES],
                        "evals/trigger-prompts.csv",
                        "evals/local-rules.json",
                    ):
                        self.assertTrue((package / relative).is_file(), relative)

    def test_metadata_and_prompt_names_are_physical_slugs(self):
        for language in LANGUAGES:
            for slug, prefix in self.BATCH.items():
                package = self.package(language, slug)
                with self.subTest(language=language, slug=slug):
                    skill_text = (package / "SKILL.md").read_text(encoding="utf-8")
                    self.assertRegex(skill_text, rf"(?m)^name:\s*{re.escape(slug)}\s*$")
                    self.assertIn(prefix, (package / f"prompts/{slug}.md").read_text(encoding="utf-8"))
                    metadata = (package / "agents/openai.yaml").read_text(encoding="utf-8")
                    self.assertRegex(metadata, rf"(?m)^\s*key:\s*['\"]?{re.escape(slug)}['\"]?\s*$")
                    local_rules = json.loads((package / "evals/local-rules.json").read_text(encoding="utf-8"))
                    self.assertEqual(slug, local_rules["skill"])

    def test_prompts_follow_required_skeleton_and_output_separation(self):
        for language in LANGUAGES:
            for slug, prefix in self.BATCH.items():
                path = self.package(language, slug) / f"prompts/{slug}.md"
                with self.subTest(language=language, slug=slug):
                    text = path.read_text(encoding="utf-8")
                    self.assertTrue(text.startswith("# "))
                    for term in SHARED_AUDIT_TERMS:
                        self.assertIn(term, text)
                    for term in SHARED_SEPARATION_TERMS[language]:
                        self.assertIn(term, text)
                    for term in SHARED_FINDING_TERMS[language]:
                        self.assertIn(term, text)
                    headings = PROMPT_HEADINGS[language]
                    positions = [text.index(heading) for heading in headings]
                    self.assertEqual(positions, sorted(positions))
                    output_heading = "## 输出" if language == "zh" else "## Output"
                    output_start = positions[headings.index(output_heading)]
                    next_heading = re.search(r"(?m)^## ", text[output_start + 3 :])
                    output = text[output_start:] if next_heading is None else text[
                        output_start : output_start + 3 + next_heading.start()
                    ]
                    for term in OUTPUT_SEPARATION_TERMS[language]:
                        self.assertIn(term, output)
                    finding_heading = "发现合同" if language == "zh" else "Finding Contract"
                    self.assertRegex(
                        text,
                        rf"(?m)^### {re.escape(prefix)}## {finding_heading}$",
                    )

    def test_trigger_data_covers_four_modes_and_language_controls(self):
        for language in LANGUAGES:
            for slug in self.BATCH:
                path = self.package(language, slug) / "evals/trigger-prompts.csv"
                with self.subTest(language=language, slug=slug):
                    with path.open(newline="", encoding="utf-8") as handle:
                        rows = list(csv.DictReader(handle))
                    self.assertTrue(rows)
                    self.assertEqual(
                        {"explicit", "implicit", "contextual", "negative"},
                        {row["mode"] for row in rows},
                    )
                    self.assertIn("true", {row["should_trigger"].lower() for row in rows})
                    self.assertIn("false", {row["should_trigger"].lower() for row in rows})
                    if language == "zh":
                        for row in rows:
                            self.assertRegex(row["prompt"], r"[\u4e00-\u9fff]")
                    if (language, slug) in self.PLACEHOLDER_FREE:
                        self.assertNotIn("undefined", path.read_text(encoding="utf-8").casefold())

    def test_eval_lists_all_three_cases(self):
        for language in LANGUAGES:
            for slug in self.BATCH:
                path = self.package(language, slug) / "evals/eval.yaml"
                with self.subTest(language=language, slug=slug):
                    text = path.read_text(encoding="utf-8")
                    for case in CASES:
                        self.assertIn(f"evals/cases/{case}", text)

    def test_entrypoints_match_language_and_include_common_pitfalls(self):
        for language in LANGUAGES:
            for slug in self.BATCH:
                path = self.package(language, slug) / "SKILL.md"
                with self.subTest(language=language, slug=slug):
                    text = path.read_text(encoding="utf-8")
                    required_headings = (
                        (
                            "## 何时使用",
                            "## 输出格式选项",
                            "## 如何使用",
                            "## 参考文件",
                            "## 常见误区",
                            "## 最佳实践",
                        )
                        if language == "zh"
                        else (
                            "## When to Use",
                            "## Output Format Options",
                            "## How to Use",
                            "## Reference Files",
                            "## Common Pitfalls",
                            "## Best Practices",
                        )
                    )
                    positions = [text.index(heading) for heading in required_headings]
                    self.assertEqual(positions, sorted(positions))
                    frontmatter = text.split("---", 2)[1]
                    body = text.split("---", 2)[2]
                    if language == "en":
                        self.assertRegex(frontmatter, r"[\u4e00-\u9fff]")
                        self.assertIsNone(re.search(r"[\u4e00-\u9fff]", body))
                    else:
                        self.assertRegex(text, r"[\u4e00-\u9fff]")

    def test_eval_cases_are_domain_specific_and_boundary_safe(self):
        for language in LANGUAGES:
            for slug in self.BATCH:
                base = self.package(language, slug) / "evals/cases"
                marker = self.DOMAIN_MARKERS[slug][language]
                with self.subTest(language=language, slug=slug):
                    basic = (base / "basic-success.yaml").read_text(encoding="utf-8")
                    description = basic.split("description:", 1)[1].split("input:", 1)[0]
                    if language == "zh":
                        self.assertRegex(description, r"[\u4e00-\u9fff]")
                    expect_block = basic.split("expect:", 1)[1].split("judge:", 1)[0]
                    self.assertIn(marker, expect_block)
                    self.assertIn(marker, basic.split("judge:", 1)[1])
                    edge = (base / "edge-scope-boundary.yaml").read_text(encoding="utf-8")
                    forbidden = (
                        ("测试已执行", "全部测试通过", "发布已批准")
                        if language == "zh"
                        else ("tests were executed", "all tests passed", "release approved")
                    )
                    for phrase in forbidden:
                        self.assertIn(phrase, edge)
                    self.assertIn(marker, edge.split("judge:", 1)[1])
