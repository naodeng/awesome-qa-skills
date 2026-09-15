import unittest

from scripts.tests.v20_skill_contracts import V20SkillContractMixin
from scripts.tests.v3_v4_skill_contracts import BATCH_2, DOMAIN_MARKERS, PREFIXES


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
        missing_packages = [
            f"skills/{language}/testing-types/{slug}"
            for language in ("zh", "en")
            for slug in NEW_BATCH_2
            if not self.package(language, slug).is_dir()
        ]
        if missing_packages:
            self.fail("Batch 2 packages are not created yet: " + ", ".join(missing_packages))

    def test_batch2_contract_targets_exact_new_set(self):
        self.assertEqual(set(NEW_BATCH_2), set(self.BATCH))
        self.assertNotIn("prompt-regression-testing", self.BATCH)


if __name__ == "__main__":
    unittest.main()
