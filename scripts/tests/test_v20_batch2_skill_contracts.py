import unittest

from scripts.tests.v20_skill_contracts import V20SkillContractMixin


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


class V20Batch2SkillContractsTest(V20SkillContractMixin, unittest.TestCase):
    BATCH = BATCH_2
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


if __name__ == "__main__":
    unittest.main()
