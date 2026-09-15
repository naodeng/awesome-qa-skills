import unittest

from scripts.tests.v20_skill_contracts import V20SkillContractMixin


BATCH_1 = {
    "decision-table-testing": "DTT-",
    "state-transition-testing": "STT-",
    "boundary-value-testing": "BVT-",
    "equivalence-partitioning": "EP-",
    "pairwise-testing": "PWT-",
    "combinatorial-testing": "CT-",
    "model-based-testing": "MBT-",
    "property-based-testing": "PBT-",
    "metamorphic-testing": "MT-",
}


class V20Batch1SkillContractsTest(V20SkillContractMixin, unittest.TestCase):
    BATCH = BATCH_1
    PLACEHOLDER_FREE = {
        ("en", "combinatorial-testing"),
        ("en", "metamorphic-testing"),
        ("en", "model-based-testing"),
        ("en", "property-based-testing"),
    }
    DOMAIN_MARKERS = {
        "decision-table-testing": {"zh": "规则", "en": "rule"},
        "state-transition-testing": {"zh": "状态", "en": "state"},
        "boundary-value-testing": {"zh": "边界", "en": "boundary"},
        "equivalence-partitioning": {"zh": "等价类", "en": "equivalence"},
        "pairwise-testing": {"zh": "成对", "en": "pairwise"},
        "combinatorial-testing": {"zh": "组合", "en": "combination"},
        "model-based-testing": {"zh": "模型", "en": "model"},
        "property-based-testing": {"zh": "不变量", "en": "invariant"},
        "metamorphic-testing": {"zh": "变换", "en": "transformation"},
    }


if __name__ == "__main__":
    unittest.main()
