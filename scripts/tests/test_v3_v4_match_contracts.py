import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / "scripts/tests/v3_v4_skill_contracts.py"
REGISTRY_PATH = ROOT / "docs/governance/skill-governance-registry.yaml"

EXPECTED_BATCH_1 = {
    "reliability-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc5w",
    "resilience-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc68",
    "chaos-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc8M",
    "failover-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc90",
    "recovery-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc_w",
    "retry-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdAw",
    "timeout-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdCU",
    "circuit-breaker-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdEM",
    "dependency-failure-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdFo",
    "disaster-recovery-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdHI",
    "authentication-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdJA",
    "authorization-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdLg",
    "session-security-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdNI",
    "api-security-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdPY",
    "security-requirement-review": "PVTI_lAHOAHP1as4BjBhVzg6SdQ0",
    "threat-modeling": "PVTI_lAHOAHP1as4BjBhVzg6SdSk",
    "secrets-exposure-review": "PVTI_lAHOAHP1as4BjBhVzg6SdUg",
}

EXPECTED_BATCH_2 = {
    "quality-gate-design": "PVTI_lAHOAHP1as4BjBhVzg6SdWc",
    "quality-metrics-design": "PVTI_lAHOAHP1as4BjBhVzg6SdY4",
    "quality-dashboard-design": "PVTI_lAHOAHP1as4BjBhVzg6SdaY",
    "quality-debt-analysis": "PVTI_lAHOAHP1as4BjBhVzg6SdcE",
    "quality-maturity-assessment": "PVTI_lAHOAHP1as4BjBhVzg6Sddo",
    "test-effectiveness-analysis": "PVTI_lAHOAHP1as4BjBhVzg6SdfA",
    "automation-roi-analysis": "PVTI_lAHOAHP1as4BjBhVzg6Sdg8",
    "testing-bottleneck-analysis": "PVTI_lAHOAHP1as4BjBhVzg6Sdig",
    "regression-optimization": "PVTI_lAHOAHP1as4BjBhVzg6SdkQ",
    "ci-test-optimization": "PVTI_lAHOAHP1as4BjBhVzg6SdnA",
    "test-runtime-optimization": "PVTI_lAHOAHP1as4BjBhVzg6Sdo4",
    "test-maintenance-cost-analysis": "PVTI_lAHOAHP1as4BjBhVzg6Sdqc",
    "quality-productivity-metrics": "PVTI_lAHOAHP1as4BjBhVzg6SdsA",
    "prompt-regression-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdtI",
    "rag-quality-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sdus",
    "rag-retrieval-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sdwg",
    "agent-loop-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdyQ",
    "agent-memory-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sdzo",
    "agent-permission-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd1E",
    "agent-failure-recovery-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd2I",
    "agent-long-running-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd3w",
    "multi-agent-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd5g",
    "llm-hallucination-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd7Q",
    "llm-consistency-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd8Q",
    "ai-safety-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd9w",
}

EXPECTED_PREFIXES = {
    "reliability-testing": "RLT-",
    "resilience-testing": "RES-",
    "chaos-testing": "CHS-",
    "failover-testing": "FOV-",
    "recovery-testing": "RCV-",
    "retry-testing": "RTY-",
    "timeout-testing": "TMO-",
    "circuit-breaker-testing": "CBR-",
    "dependency-failure-testing": "DPF-",
    "disaster-recovery-testing": "DRT-",
    "authentication-testing": "AUT-",
    "authorization-testing": "AZT-",
    "session-security-testing": "SST-",
    "api-security-testing": "AST-",
    "security-requirement-review": "SRR-",
    "threat-modeling": "THM-",
    "secrets-exposure-review": "SER-",
    "quality-gate-design": "QGD-",
    "quality-metrics-design": "QMD-",
    "quality-dashboard-design": "QDD-",
    "quality-debt-analysis": "QDA-",
    "quality-maturity-assessment": "QMA-",
    "test-effectiveness-analysis": "TEA-",
    "automation-roi-analysis": "ARO-",
    "testing-bottleneck-analysis": "TBA-",
    "regression-optimization": "RGO-",
    "ci-test-optimization": "CTO-",
    "test-runtime-optimization": "TRO-",
    "test-maintenance-cost-analysis": "TMC-",
    "quality-productivity-metrics": "QPM-",
    "prompt-regression-testing": "PRT-",
    "rag-quality-testing": "RAGQ-",
    "rag-retrieval-testing": "RAGT-",
    "agent-loop-testing": "ALT-",
    "agent-memory-testing": "AMT-",
    "agent-permission-testing": "AGP-",
    "agent-failure-recovery-testing": "AFR-",
    "agent-long-running-testing": "ALR-",
    "multi-agent-testing": "MAT-",
    "llm-hallucination-testing": "LHT-",
    "llm-consistency-testing": "LCT-",
    "ai-safety-testing": "AIS-",
}


class V34MatchContractsTest(unittest.TestCase):
    @classmethod
    def load_contract(cls):
        if not CONTRACT_PATH.is_file():
            raise AssertionError(f"missing shared contract: {CONTRACT_PATH}")
        spec = importlib.util.spec_from_file_location("v3_v4_skill_contracts", CONTRACT_PATH)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_candidate_partition_and_live_card_ids_are_exact(self):
        contract = self.load_contract()
        self.assertEqual(EXPECTED_BATCH_1, contract.BATCH_1)
        self.assertEqual(EXPECTED_BATCH_2, contract.BATCH_2)
        self.assertEqual(17, len(contract.BATCH_1))
        self.assertEqual(25, len(contract.BATCH_2))
        self.assertEqual(42, len(set(contract.BATCH_1) | set(contract.BATCH_2)))
        self.assertEqual(set(contract.BATCH_1) | set(contract.BATCH_2), set(contract.CARD_IDS))

    def test_prefixes_and_domains_cover_every_candidate_once(self):
        contract = self.load_contract()
        candidates = set(contract.CARD_IDS)
        self.assertEqual(candidates, set(contract.PREFIXES))
        self.assertEqual(EXPECTED_PREFIXES, contract.PREFIXES)
        self.assertEqual(candidates - {"prompt-regression-testing"}, set(contract.DOMAIN_MARKERS))
        for slug, markers in contract.DOMAIN_MARKERS.items():
            with self.subTest(slug=slug):
                self.assertEqual({"zh", "en"}, set(markers))
                self.assertTrue(all(markers.values()))

    def test_match_records_are_complete_and_evidence_bounded(self):
        contract = self.load_contract()
        candidates = set(contract.CARD_IDS)
        self.assertEqual(candidates, set(contract.MATCH_RECORDS))
        for slug, record in contract.MATCH_RECORDS.items():
            with self.subTest(slug=slug):
                self.assertEqual(slug, record["slug"])
                self.assertEqual("testing-types", record["target_section"])
                self.assertIn(record["conclusion"], {"NEW", "ENHANCE", "MERGE", "MATCH", "EXISTING"})
                self.assertTrue(record["existing_targets"])
                self.assertTrue(record["difference"])
                self.assertNotIn("all tests pass", record["difference"].casefold())
                self.assertNotIn("release approved", record["difference"].casefold())

    def test_new_and_enhancement_sets_follow_match_records(self):
        contract = self.load_contract()
        self.assertEqual(41, len(contract.NEW_SKILLS))
        self.assertNotIn("prompt-regression-testing", contract.NEW_SKILLS)
        self.assertEqual(41, len(set(contract.NEW_SKILLS)))
        self.assertEqual({"prompt-regression-testing"}, set(contract.ENHANCEMENTS))
        self.assertEqual(
            {slug for slug, record in contract.MATCH_RECORDS.items() if record["conclusion"] == "NEW"},
            set(contract.NEW_SKILLS),
        )
        self.assertEqual(
            {slug for slug, record in contract.MATCH_RECORDS.items() if record["conclusion"] == "ENHANCE"},
            set(contract.ENHANCEMENTS),
        )
        enhancement = contract.ENHANCEMENTS["prompt-regression-testing"]
        self.assertEqual("prompt-testing", enhancement["target"])
        self.assertEqual("PRT-", enhancement["prefix"])

    def test_registry_targets_follow_shared_match_ledger_for_new_skills(self):
        contract = self.load_contract()
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        candidates = {candidate["slug"]: candidate for candidate in registry["candidates"]}
        for slug in contract.NEW_SKILLS:
            with self.subTest(slug=slug):
                self.assertEqual(
                    contract.MATCH_RECORDS[slug]["existing_targets"],
                    candidates[slug]["capability_match"]["existing_targets"],
                )

    def test_package_contract_is_explicit(self):
        contract = self.load_contract()
        self.assertEqual(
            {
                "SKILL.md",
                "prompts/{slug}.md",
                "agents/openai.yaml",
                "evals/eval.yaml",
                "evals/cases/basic-success.yaml",
                "evals/cases/edge-incomplete-input.yaml",
                "evals/cases/edge-scope-boundary.yaml",
                "evals/trigger-prompts.csv",
                "evals/local-rules.json",
            },
            set(contract.REQUIRED_PACKAGE_FILES),
        )
        self.assertEqual(
            {"known", "missing", "conflicting", "stale", "out_of_scope", "assumptions"},
            set(contract.SHARED_AUDIT_TERMS),
        )


if __name__ == "__main__":
    unittest.main()
