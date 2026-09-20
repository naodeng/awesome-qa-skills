import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts import virtual_domains


ROOT = Path(__file__).resolve().parents[2]
EXPECTED_DOMAIN_IDS = tuple(f"D{index:02d}" for index in range(1, 17))


class VirtualDomainCatalogTest(unittest.TestCase):
    def test_manifest_has_exact_sixteen_domain_ids(self):
        catalog = virtual_domains.load_catalog(ROOT / "docs/governance/virtual-domains.yaml")

        self.assertEqual(catalog.domain_ids(), EXPECTED_DOMAIN_IDS)
        self.assertEqual(catalog.label("D01", "zh"), "D01 需求质量")
        self.assertEqual(catalog.label("D16", "en"), "D16 AI / LLM / Agent Quality")

    def test_rejects_duplicate_or_unknown_domain_configuration(self):
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / "virtual-domains.yaml"
            path.write_text(
                json.dumps(
                    {
                        "domains": [
                            {"id": "D01", "name_zh": "需求质量", "name_en": "Requirement Quality"},
                            {"id": "D01", "name_zh": "重复", "name_en": "Duplicate"},
                        ],
                        "section_defaults": {"testing-workflows": "D99"},
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "exactly D01-D16"):
                virtual_domains.load_catalog(path)

    def test_rejects_unknown_domain_mapping_after_valid_domain_list(self):
        with TemporaryDirectory() as temporary:
            path = Path(temporary) / "virtual-domains.yaml"
            domains = [
                {
                    "id": domain_id,
                    "name_zh": domain_id,
                    "name_en": domain_id,
                    "description_zh": domain_id,
                    "description_en": domain_id,
                }
                for domain_id in EXPECTED_DOMAIN_IDS
            ]
            path.write_text(
                json.dumps(
                    {
                        "domains": domains,
                        "section_defaults": {"testing-workflows": "D99"},
                    }
                ),
                encoding="utf-8",
            )

            with self.assertRaisesRegex(ValueError, "unknown Domain IDs"):
                virtual_domains.load_catalog(path)

    def test_missing_catalog_is_rejected_for_repository_validation(self):
        with TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(ValueError, "Virtual Domain catalog is required"):
                virtual_domains.load_required_catalog(Path(temporary))

    def test_slug_override_wins_over_heading_default(self):
        catalog = virtual_domains.load_catalog(ROOT / "docs/governance/virtual-domains.yaml")

        self.assertEqual(
            catalog.classify("testing-types", "api-testing", "测试执行与分析"),
            "D06",
        )
        self.assertEqual(
            catalog.classify("testing-types", "security-testing", "Reliability and Security — 可靠性与安全"),
            "D10",
        )
        self.assertEqual(catalog.classify("testing-workflows", "release-testing-workflow", None), "D12")

    def test_unmapped_skill_raises(self):
        catalog = virtual_domains.load_catalog(ROOT / "docs/governance/virtual-domains.yaml")

        with self.assertRaisesRegex(ValueError, "No virtual Domain mapping"):
            catalog.classify("testing-types", "not-in-catalog", "未知分类")

    def test_ambiguous_catalog_heading_requires_explicit_slug_override(self):
        catalog = virtual_domains.load_catalog(ROOT / "docs/governance/virtual-domains.yaml")

        for section, slug, heading in (
            ("testing-types", "new-security-skill", "Reliability and Security — 可靠性与安全"),
            ("testing-types", "new-observability-skill", "需求与质量左移"),
            ("skill-engineering", "new-security-skill", "Reliability and Security — 可靠性与安全"),
        ):
            with self.assertRaisesRegex(ValueError, "Ambiguous catalog heading"):
                catalog.classify(section, slug, heading)

    def test_current_repository_uses_all_sixteen_domains(self):
        mapping = virtual_domains.repository_mapping(ROOT)

        self.assertEqual(len(mapping), 164)
        self.assertEqual(set(mapping.values()), set(EXPECTED_DOMAIN_IDS))
        self.assertEqual(mapping[("testing-types", "api-testing")], "D06")
        self.assertEqual(mapping[("skill-engineering", "skill-prose-review")], "D14")


if __name__ == "__main__":
    unittest.main()
