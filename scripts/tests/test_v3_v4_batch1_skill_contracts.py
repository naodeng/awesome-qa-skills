import unittest

from scripts.tests.v20_skill_contracts import SHARED_FINDING_TERMS, V20SkillContractMixin
from scripts.tests.v3_v4_skill_contracts import (
    BATCH_1,
    DOMAIN_MARKERS,
    NEW_SKILLS,
    PREFIXES,
    assert_packages_exist,
)


class V34Batch1SkillContractsTest(V20SkillContractMixin, unittest.TestCase):
    BATCH = {slug: PREFIXES[slug] for slug in BATCH_1}
    PLACEHOLDER_FREE = {
        (language, slug)
        for language in ("zh", "en")
        for slug in BATCH_1
    }
    DOMAIN_MARKERS = {slug: DOMAIN_MARKERS[slug] for slug in BATCH_1}

    def setUp(self):
        assert_packages_exist(self, BATCH_1)

    def test_batch1_contract_targets_exact_new_set(self):
        self.assertEqual(set(BATCH_1), set(self.BATCH))
        self.assertEqual(set(BATCH_1), set(NEW_SKILLS) & set(BATCH_1))
        self.assertNotIn("prompt-regression-testing", self.BATCH)

    def test_v3_v4_basic_cases_require_finding_prefix(self):
        for language in ("zh", "en"):
            for slug, prefix in self.BATCH.items():
                path = self.package(language, slug) / "evals/cases/basic-success.yaml"
                text = path.read_text(encoding="utf-8")
                with self.subTest(language=language, slug=slug):
                    expect_block = text.split("expect:", 1)[1].split("judge:", 1)[0]
                    self.assertIn(prefix, expect_block)
                    judge_block = text.split("judge:", 1)[1]
                    self.assertIn(prefix, judge_block)
                    for term in SHARED_FINDING_TERMS[language]:
                        self.assertIn(term, expect_block)
                        self.assertIn(term, judge_block)


if __name__ == "__main__":
    unittest.main()
