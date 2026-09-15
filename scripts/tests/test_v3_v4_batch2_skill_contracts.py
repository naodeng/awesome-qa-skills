import unittest

from scripts.tests.v20_skill_contracts import SHARED_FINDING_TERMS, V20SkillContractMixin
from scripts.tests.v3_v4_skill_contracts import (
    BATCH_2,
    DOMAIN_MARKERS,
    PREFIXES,
    assert_packages_exist,
)


NEW_BATCH_2 = tuple(slug for slug in BATCH_2 if slug != "prompt-regression-testing")


class V34Batch2SkillContractsTest(V20SkillContractMixin, unittest.TestCase):
    BATCH = {slug: PREFIXES[slug] for slug in NEW_BATCH_2}
    PLACEHOLDER_FREE = {
        (language, slug)
        for language in ("zh", "en")
        for slug in NEW_BATCH_2
    }
    DOMAIN_MARKERS = {slug: DOMAIN_MARKERS[slug] for slug in NEW_BATCH_2}

    def setUp(self):
        assert_packages_exist(self, NEW_BATCH_2)

    def test_batch2_contract_targets_exact_new_set(self):
        self.assertEqual(set(NEW_BATCH_2), set(self.BATCH))
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
