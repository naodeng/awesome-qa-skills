import unittest

from scripts.tests.v20_skill_contracts import V20SkillContractMixin
from scripts.tests.v3_v4_skill_contracts import BATCH_1, DOMAIN_MARKERS, NEW_SKILLS, PREFIXES


class V34Batch1SkillContractsTest(V20SkillContractMixin, unittest.TestCase):
    BATCH = {slug: PREFIXES[slug] for slug in BATCH_1}
    PLACEHOLDER_FREE = {
        (language, slug)
        for language in ("zh", "en")
        for slug in BATCH_1
    }
    DOMAIN_MARKERS = {slug: DOMAIN_MARKERS[slug] for slug in BATCH_1}

    def setUp(self):
        missing_packages = [
            f"skills/{language}/testing-types/{slug}"
            for language in ("zh", "en")
            for slug in BATCH_1
            if not (self.package(language, slug)).is_dir()
        ]
        if missing_packages:
            self.fail("Batch 1 packages are not created yet: " + ", ".join(missing_packages))

    def test_batch1_contract_targets_exact_new_set(self):
        self.assertEqual(set(BATCH_1), set(self.BATCH))
        self.assertEqual(set(BATCH_1), set(NEW_SKILLS) & set(BATCH_1))
        self.assertNotIn("prompt-regression-testing", self.BATCH)


if __name__ == "__main__":
    unittest.main()
