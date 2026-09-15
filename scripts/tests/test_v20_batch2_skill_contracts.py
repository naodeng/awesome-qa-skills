import csv
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = ("zh", "en")
BATCH_2 = {
    "api-schema-validation": "ASV-",
    "api-negative-testing": "ANT-",
    "api-idempotency-testing": "AIT-",
    "api-pagination-testing": "APT-",
    "api-rate-limit-testing": "ARL-",
    "api-version-compatibility-testing": "AVC-",
    "api-error-contract-testing": "AEC-",
    "ui-test-strategy": "UTS-",
    "ui-test-selector-review": "USR-",
    "ui-test-wait-strategy-review": "UWR-",
    "visual-regression-testing": "VRT-",
    "cross-browser-testing": "CBT-",
    "test-code-review": "TCR-",
    "mutation-testing-analysis": "MTA-",
    "mock-quality-review": "MQR-",
    "test-suite-health-analysis": "TSH-",
}
CASES = (
    "basic-success.yaml",
    "edge-incomplete-input.yaml",
    "edge-scope-boundary.yaml",
)
PLACEHOLDER_FREE = {
    ("zh", "api-error-contract-testing"),
    ("zh", "api-pagination-testing"),
    ("zh", "api-version-compatibility-testing"),
    ("en", "api-error-contract-testing"),
    ("en", "api-pagination-testing"),
    ("en", "api-version-compatibility-testing"),
}
DOMAIN_MARKERS = {
    "api-schema-validation": {"zh": "schema", "en": "schema"},
    "api-negative-testing": {"zh": "负向", "en": "negative"},
    "api-idempotency-testing": {"zh": "幂等", "en": "idempotency"},
    "api-pagination-testing": {"zh": "分页", "en": "pagination"},
    "api-rate-limit-testing": {"zh": "限流", "en": "rate limit"},
    "api-version-compatibility-testing": {"zh": "兼容", "en": "compatibility"},
    "api-error-contract-testing": {"zh": "错误契约", "en": "error contract"},
    "ui-test-strategy": {"zh": "UI", "en": "UI"},
    "ui-test-selector-review": {"zh": "选择器", "en": "selector"},
    "ui-test-wait-strategy-review": {"zh": "等待", "en": "wait"},
    "visual-regression-testing": {"zh": "视觉", "en": "visual"},
    "cross-browser-testing": {"zh": "浏览器", "en": "browser"},
    "test-code-review": {"zh": "测试代码", "en": "test code"},
    "mutation-testing-analysis": {"zh": "变异", "en": "mutation"},
    "mock-quality-review": {"zh": "Mock", "en": "mock"},
    "test-suite-health-analysis": {"zh": "健康", "en": "health"},
}
SHARED_AUDIT_TERMS = ("known", "missing", "conflicting", "stale", "out_of_scope", "assumptions")
SHARED_SEPARATION_TERMS = {
    "zh": ("事实", "推断", "建议", "Human"),
    "en": ("facts", "inferences", "recommendations", "Human"),
}
SHARED_FINDING_TERMS = {
    "zh": ("对象/规则", "来源", "触发条件或适用范围", "预期关注点/理由", "证据状态", "影响/优先级", "责任角色", "关闭条件", "验证方法"),
    "en": ("object/rule", "source", "trigger or applicability", "expected concern/rationale", "evidence state", "impact/priority", "owner role", "close condition", "validation method"),
}


class V20Batch2SkillContractsTest(unittest.TestCase):
    def test_every_bilingual_package_has_required_files(self):
        for language in LANGUAGES:
            for slug in BATCH_2:
                package = ROOT / "skills" / language / "testing-types" / slug
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
            for slug, prefix in BATCH_2.items():
                package = ROOT / "skills" / language / "testing-types" / slug
                with self.subTest(language=language, slug=slug):
                    if not (package / "SKILL.md").is_file():
                        continue
                    skill_text = (package / "SKILL.md").read_text()
                    self.assertRegex(skill_text, rf"(?m)^name:\s*{re.escape(slug)}\s*$")
                    self.assertIn(prefix, (package / f"prompts/{slug}.md").read_text())
                    metadata = (package / "agents/openai.yaml").read_text()
                    self.assertRegex(metadata, rf"(?m)^\s*key:\s*['\"]?{re.escape(slug)}['\"]?\s*$")
                    local_rules = json.loads((package / "evals/local-rules.json").read_text())
                    self.assertEqual(slug, local_rules["skill"])

    def test_prompts_preserve_shared_input_and_output_contract(self):
        for language in LANGUAGES:
            for slug, prefix in BATCH_2.items():
                path = ROOT / "skills" / language / "testing-types" / slug / f"prompts/{slug}.md"
                with self.subTest(language=language, slug=slug):
                    text = path.read_text(encoding="utf-8")
                    for term in SHARED_AUDIT_TERMS:
                        self.assertIn(term, text)
                    for term in SHARED_SEPARATION_TERMS[language]:
                        self.assertIn(term, text)
                    for term in SHARED_FINDING_TERMS[language]:
                        self.assertIn(term, text)
                    self.assertIn("## 输出" if language == "zh" else "## Output", text)
                    self.assertRegex(
                        text,
                        rf"(?m)^## {re.escape(prefix)}## {('发现合同|合同' if language == 'zh' else 'Finding Contract|Contract')}$",
                    )

    def test_trigger_data_covers_four_modes_and_positive_negative_controls(self):
        for language in LANGUAGES:
            for slug in BATCH_2:
                path = ROOT / "skills" / language / "testing-types" / slug / "evals/trigger-prompts.csv"
                with self.subTest(language=language, slug=slug):
                    if not path.is_file():
                        continue
                    with path.open(newline="") as handle:
                        rows = list(csv.DictReader(handle))
                    self.assertTrue(rows)
                    self.assertEqual(
                        {"explicit", "implicit", "contextual", "negative"},
                        {row["mode"] for row in rows},
                    )
                    self.assertIn("true", {row["should_trigger"].lower() for row in rows})
                    self.assertIn("false", {row["should_trigger"].lower() for row in rows})
                    if (language, slug) in PLACEHOLDER_FREE:
                        self.assertNotIn("undefined", path.read_text(encoding="utf-8").casefold())

    def test_eval_lists_all_three_cases(self):
        for language in LANGUAGES:
            for slug in BATCH_2:
                path = ROOT / "skills" / language / "testing-types" / slug / "evals/eval.yaml"
                with self.subTest(language=language, slug=slug):
                    if not path.is_file():
                        continue
                    text = path.read_text()
                    for case in CASES:
                        self.assertIn(f"evals/cases/{case}", text)

    def test_entrypoints_match_language_and_include_common_pitfalls(self):
        for language in LANGUAGES:
            for slug in BATCH_2:
                path = ROOT / "skills" / language / "testing-types" / slug / "SKILL.md"
                with self.subTest(language=language, slug=slug):
                    text = path.read_text(encoding="utf-8")
                    heading = "## 常见误区" if language == "zh" else "## Common Pitfalls"
                    self.assertIn(heading, text)
                    self.assertIn("## 输出格式选项" if language == "zh" else "## Output Format Options", text)
                    self.assertIn("## 最佳实践" if language == "zh" else "## Best Practices", text)
                    required_headings = (
                        ("## 何时使用", "## 输出格式选项", "## 如何使用", "## 参考文件", "## 常见误区", "## 最佳实践")
                        if language == "zh" else
                        ("## When to Use", "## Output Format Options", "## How to Use", "## Reference Files", "## Common Pitfalls", "## Best Practices")
                    )
                    positions = [text.index(heading) for heading in required_headings]
                    self.assertEqual(positions, sorted(positions))
                    if language == "en":
                        self.assertIsNone(re.search(r"[\u4e00-\u9fff]", text))

    def test_eval_cases_are_domain_specific_and_boundary_safe(self):
        for language in LANGUAGES:
            for slug in BATCH_2:
                base = ROOT / "skills" / language / "testing-types" / slug / "evals/cases"
                marker = DOMAIN_MARKERS[slug][language]
                with self.subTest(language=language, slug=slug):
                    basic = (base / "basic-success.yaml").read_text(encoding="utf-8")
                    expect_block = basic.split("expect:", 1)[1].split("judge:", 1)[0]
                    self.assertIn(marker, expect_block)
                    self.assertIn(marker, basic.split("judge:", 1)[1])
                    edge = (base / "edge-scope-boundary.yaml").read_text(encoding="utf-8")
                    forbidden = ("测试已执行", "全部测试通过", "发布已批准") if language == "zh" else (
                        "tests were executed", "all tests passed", "release approved"
                    )
                    for phrase in forbidden:
                        self.assertIn(phrase, edge)
                    self.assertIn(marker, edge.split("judge:", 1)[1])


if __name__ == "__main__":
    unittest.main()
