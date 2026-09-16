"""Contract tests for the v1.4 governance and release closeout."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import unittest

from scripts import check_docs_bilingual
from scripts import generate_v14_closeout as closeout


ROOT = Path(__file__).resolve().parents[2]
CONTRACT_PATH = ROOT / "docs/governance/v1-4-closeout.yaml"

EXPECTED_TITLES = (
    "v1.0｜治理｜16 个虚拟 Domain 分类",
    "v1.0｜治理｜Deprecation 与替代路径规则",
    "v1.0｜治理｜中英文一致性质量契约",
    "v1.0｜治理｜Skill Quality Score 与最低 Eval 标准",
    "v1.0｜文档｜README 与双语入口治理",
    "v1.0｜文档｜Skill Map Graph Catalog 治理",
    "v1.0｜文档｜Workflow Eval 安装文档同步清单",
    "v1.0｜复盘｜Phase 0 Governance Review",
    "v1.0｜里程碑｜v1.0 Governance 发布准备",
    "v1.0｜治理｜典型 Match Merge 映射复核",
    "治理｜Enhancement Sprint 节奏",
    "治理｜候选 Skill 15 步执行模板",
    "里程碑｜v1.1-v1.4 Shift Left",
    "治理｜Match Enhance｜requirement-change-impact-analysis",
    "治理｜Merge｜test-impact-analysis",
    "治理｜Merge Enhance｜code-change-risk-analysis",
    "治理｜Match｜workload-modeling",
    "治理｜Match｜capacity-planning",
    "治理｜Existing｜performance-bottleneck-analysis",
    "治理｜Existing｜performance-result-analysis",
    "治理｜Existing｜performance-regression-analysis",
    "治理｜Existing｜flaky-test-analysis",
    "治理｜Existing｜production-verification",
    "治理｜Merge｜regression-scope-selection",
    "治理｜Match｜ai-test-case-review",
    "治理｜Match Enhance｜ai-log-analysis",
    "治理｜Match Enhance｜ai-root-cause-analysis",
    "治理｜Match｜quality-risk-identification",
    "治理｜Match Enhance｜ai-test-data-generation",
    "治理｜Match Enhance｜llm-output-quality-testing",
    "治理｜Match｜llm-evaluation",
    "治理｜Existing｜prompt-testing",
    "治理｜Existing｜agent-tool-testing",
    "Release DoD｜v1.0",
    "Release DoD｜v1.4",
)

EXPECTED_V10_TITLES = (
    "v1.0｜治理｜16 个虚拟 Domain 分类",
    "v1.0｜治理｜Deprecation 与替代路径规则",
    "v1.0｜治理｜中英文一致性质量契约",
    "v1.0｜治理｜Skill Quality Score 与最低 Eval 标准",
    "v1.0｜文档｜README 与双语入口治理",
    "v1.0｜文档｜Skill Map Graph Catalog 治理",
    "v1.0｜文档｜Workflow Eval 安装文档同步清单",
    "v1.0｜里程碑｜v1.0 Governance 发布准备",
    "v1.0｜治理｜典型 Match Merge 映射复核",
    "Release DoD｜v1.0",
)


class V14CloseoutContractTest(unittest.TestCase):
    def test_contract_covers_exactly_all_v14_project_cards(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        self.assertEqual(contract.target_version, "v1.4")
        self.assertEqual(contract.project_owner, "naodeng")
        self.assertEqual(contract.project_item_type, "DraftIssue")
        self.assertEqual(contract.project_status_verified_at, "2026-09-16")
        self.assertEqual(contract.final_project_counts["v1.4"], {"Done": 35, "In Progress": 0, "Todo": 0})
        self.assertEqual(len(contract.cards), 35)
        self.assertEqual(tuple(card.title for card in contract.cards), EXPECTED_TITLES)
        self.assertEqual({card.priority for card in contract.cards}, {"P0"})
        self.assertEqual(
            {card.project_status_before for card in contract.cards},
            {"Done", "In Progress"},
        )
        self.assertTrue(all(card.project_status_after == "Done" for card in contract.cards))
        self.assertEqual(closeout.validate_contract(contract, ROOT), [])

    def test_contract_keeps_static_runtime_model_and_release_states_separate(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        self.assertEqual(contract.boundaries["static"], "VERIFIED")
        self.assertEqual(contract.boundaries["runtime"], "NOT_RUN")
        self.assertEqual(contract.boundaries["model_eval"], "NOT_RUN")
        self.assertEqual(contract.boundaries["release_approval"], "NOT_RUN")
        self.assertIn("NOT_SCORED", contract.boundary_text)
        self.assertIn("UNASSESSED", contract.boundary_text)

    def test_generated_views_cover_every_card_and_both_locales(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        for locale in ("zh", "en"):
            rendered = closeout.render_closeout(contract, locale, ROOT)
            for title in EXPECTED_TITLES:
                self.assertIn(title, rendered)
            self.assertIn("Project item ID", rendered)
            self.assertIn(contract.cards[0].project_item_id, rendered)
            self.assertIn("change-impact-analysis", rendered)
            self.assertIn("Match review linkage" if locale == "en" else "Match Review 关联", rendered)
            card_rows = [line for line in rendered.splitlines() if line.startswith("| `") and "→" in line]
            self.assertEqual(len(card_rows), 35)
        for version in ("v1.0", "v1.4"):
            for locale in ("zh", "en"):
                rendered = closeout.render_release_dod(contract, version, locale, ROOT)
                self.assertIn(version, rendered)
                self.assertIn("NOT_RUN", rendered)
                self.assertIn("N/A", rendered)

    def test_release_dod_uses_explicit_version_scopes(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        self.assertEqual(
            tuple(card.title for card in contract.cards if card.title in EXPECTED_V10_TITLES[:-1]),
            EXPECTED_V10_TITLES[:-1],
        )
        self.assertEqual(contract.release_dod_scopes["v1.0"], EXPECTED_V10_TITLES)
        for locale in ("zh", "en"):
            v10 = closeout.render_release_dod(contract, "v1.0", locale, ROOT)
            v14 = closeout.render_release_dod(contract, "v1.4", locale, ROOT)
            v10_rows = [line for line in v10.splitlines() if line.startswith("| `")]
            v14_rows = [line for line in v14.splitlines() if line.startswith("| `")]
            self.assertEqual(len(v10_rows), len(EXPECTED_V10_TITLES))
            self.assertEqual(len(v14_rows), len(EXPECTED_TITLES))
            self.assertNotIn("Phase 0 Governance Review", v10)
            self.assertNotIn("35-card v1.4 closeout contract", v10)
            self.assertNotIn("35 张 v1.4 卡片", v10)

    def test_project_snapshot_requires_exact_done_draft_issue_scope(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        payload = {
            "items": [
                {
                    "id": card.project_item_id,
                    "title": card.title,
                    "status": card.project_status_after,
                    "content": {"type": contract.project_item_type, "title": card.title},
                }
                for card in contract.cards
            ]
        }
        self.assertEqual(closeout.validate_project_snapshot(contract, payload), [])
        payload_with_other_project_cards = {
            "items": [
                *payload["items"],
                {
                    "id": "PVTI_other_version_card",
                    "title": "v1.5 follow-up",
                    "status": "Todo",
                    "content": {"type": "DraftIssue", "title": "v1.5 follow-up"},
                },
            ]
        }
        self.assertEqual(
            closeout.validate_project_snapshot(contract, payload_with_other_project_cards),
            [],
        )
        payload_with_extra_v14_card = {
            "items": [
                *payload["items"],
                {
                    "id": "PVTI_unregistered_v14_card",
                    "title": "v1.4｜未纳入契约的额外卡",
                    "status": "In Progress",
                    "content": {
                        "type": contract.project_item_type,
                        "title": "v1.4｜未纳入契约的额外卡",
                    },
                },
            ]
        }
        self.assertTrue(
            any(
                "unexpected v1.4 Project item" in error
                for error in closeout.validate_project_snapshot(contract, payload_with_extra_v14_card)
            )
        )

        payload_with_duplicate_canonical_title = {
            "items": [
                *payload["items"][1:],
                {
                    "id": "PVTI_duplicate_canonical_title",
                    "title": contract.cards[0].title,
                    "status": "Done",
                    "content": {
                        "type": contract.project_item_type,
                        "title": contract.cards[0].title,
                    },
                },
            ]
        }
        self.assertTrue(
            any(
                "canonical title" in error
                for error in closeout.validate_project_snapshot(contract, payload_with_duplicate_canonical_title)
            )
        )

        wrong_status = {"items": [dict(item) for item in payload["items"]]}
        wrong_status["items"][0] = {**wrong_status["items"][0], "status": "Todo"}
        self.assertTrue(any("status" in error for error in closeout.validate_project_snapshot(contract, wrong_status)))

        wrong_type = {"items": [dict(item) for item in payload["items"]]}
        wrong_type["items"][0] = {
            **wrong_type["items"][0],
            "content": {"type": "Issue", "title": wrong_type["items"][0]["title"]},
        }
        self.assertTrue(any("type" in error for error in closeout.validate_project_snapshot(contract, wrong_type)))

        missing = {"items": payload["items"][1:]}
        self.assertTrue(any("missing" in error for error in closeout.validate_project_snapshot(contract, missing)))

    def test_contract_rejects_duplicate_ids_and_unavailable_evidence(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        duplicate = replace(contract, cards=(contract.cards[0], contract.cards[0], *contract.cards[2:]))
        errors = closeout.validate_contract(duplicate, ROOT)
        self.assertIn("duplicate project item id", errors)

        missing = replace(
            contract,
            cards=(replace(contract.cards[0], evidence_paths=("docs/does-not-exist.md",)), *contract.cards[1:]),
        )
        errors = closeout.validate_contract(missing, ROOT)
        self.assertIn("missing evidence path: docs/does-not-exist.md", errors)

        for invalid_path in ("/etc/hosts", "../README.md", "docs"):
            with self.subTest(invalid_path=invalid_path):
                invalid = replace(
                    contract,
                    cards=(replace(contract.cards[0], evidence_paths=(invalid_path,)), *contract.cards[1:]),
                )
                errors = closeout.validate_contract(invalid, ROOT)
                self.assertTrue(
                    any("evidence path must be repository-relative" in error or "missing evidence path" in error for error in errors),
                    errors,
                )

    def test_repository_relative_file_rejects_symlink_escape(self):
        from tempfile import TemporaryDirectory

        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            outside = root.parent / f"{root.name}-outside.txt"
            try:
                outside.write_text("outside", encoding="utf-8")
                link = root / "link.txt"
                link.symlink_to(outside)
                self.assertIn(
                    "stay within repository",
                    closeout.validate_repository_relative_file(root, "link.txt", "evidence path"),
                )
            finally:
                outside.unlink(missing_ok=True)

    def test_contract_rejects_replaced_project_card_identity(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        cards = list(contract.cards)
        cards[10] = replace(cards[10], project_item_id="PVTI_fake", title="v1.4｜替换卡片")

        errors = closeout.validate_contract(replace(contract, cards=tuple(cards)), ROOT)

        self.assertIn("cards must match the canonical v1.4 Project item ID/title set", errors)

    def test_contract_links_each_mapping_card_to_a_match_review(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        mapping_cards = [card for card in contract.cards if card.match_review_candidate]

        self.assertEqual(len(mapping_cards), 20)
        self.assertEqual(
            {card.match_review_candidate for card in mapping_cards},
            set(closeout.REQUIRED_MATCH_REVIEW_CANDIDATES),
        )

        cards = list(contract.cards)
        cards[13] = replace(cards[13], match_review_candidate="not-in-registry-candidate")
        errors = closeout.validate_contract(replace(contract, cards=tuple(cards)), ROOT)
        self.assertIn("mapping card match_review_candidate set must match Registry", errors)

    def test_contract_matches_complete_registry_review_links(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        links_by_id = {link.project_item_id: link for link in contract.match_review_links}
        mapping_cards = [card for card in contract.cards if card.kind == "mapping" and card.match_review_candidate]

        self.assertEqual(len(contract.match_review_links), 20)
        self.assertEqual(set(links_by_id), {card.project_item_id for card in mapping_cards})
        for card in mapping_cards:
            link = links_by_id[card.project_item_id]
            self.assertEqual(link.candidate, card.match_review_candidate)
            self.assertTrue(link.target_skills)
            self.assertTrue(link.evidence_paths)
            self.assertTrue(link.next_action)

        mutations = {
            "conclusion": replace(contract.match_review_links[0], conclusion="EXISTING"),
            "review_state": replace(contract.match_review_links[0], review_state="REVIEWED"),
            "target_skills": replace(contract.match_review_links[0], target_skills=("wrong-target",)),
            "evidence_paths": replace(contract.match_review_links[0], evidence_paths=("docs/README.md",)),
            "next_action": replace(contract.match_review_links[0], next_action="drifted action"),
        }
        for field, mutated_link in mutations.items():
            with self.subTest(field=field):
                mutated = list(contract.match_review_links)
                mutated[0] = mutated_link
                errors = closeout.validate_contract(
                    replace(contract, match_review_links=tuple(mutated)),
                    ROOT,
                )
                self.assertTrue(
                    any(f"match review {field} must match Registry" in error for error in errors),
                    errors,
                )

    def test_contract_rejects_release_claims_from_unrun_evidence(self):
        contract = closeout.load_contract(CONTRACT_PATH)
        invalid = replace(
            contract,
            boundaries={**contract.boundaries, "runtime": "PASS"},
        )
        self.assertIn("invalid runtime boundary", closeout.validate_contract(invalid, ROOT))

    def test_governance_contracts_and_install_sync_are_registered(self):
        pairs = {pair for pair in closeout.REQUIRED_BILINGUAL_PAIRS}
        self.assertIn(
            ("docs/governance/DEPRECATION_DECISION_CONTRACT.md", "docs/governance/DEPRECATION_DECISION_CONTRACT_EN.md"),
            pairs,
        )
        self.assertIn(
            ("docs/governance/BILINGUAL_CONSISTENCY_CONTRACT.md", "docs/governance/BILINGUAL_CONSISTENCY_CONTRACT_EN.md"),
            pairs,
        )
        self.assertIn(
            ("docs/governance/QUALITY_SCORE_EVAL_CONTRACT.md", "docs/governance/QUALITY_SCORE_EVAL_CONTRACT_EN.md"),
            pairs,
        )
        self.assertIn(
            ("docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md", "docs/governance/WORKFLOW_EVAL_INSTALL_SYNC_EN.md"),
            pairs,
        )
        self.assertIn(
            ("docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md", "docs/governance/PHASE_0_MATCH_MERGE_REVIEW_EN.md"),
            pairs,
        )

        install_sync = (ROOT / "docs/governance/WORKFLOW_EVAL_INSTALL_SYNC.md").read_text(encoding="utf-8")
        workflows = sorted(path.name for path in (ROOT / "skills/zh/testing-workflows").iterdir() if path.is_dir())
        for workflow in workflows:
            self.assertIn(f"`{workflow}`", install_sync)
        self.assertEqual(len(workflows), 10)

    def test_reader_facing_governance_counts_do_not_call_79_current(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        roadmap = (ROOT / "docs/governance/QA_SKILLS_EVOLUTION_ROADMAP.md").read_text(encoding="utf-8")

        self.assertNotIn("79 对静态记录入口", readme)
        self.assertIn("早期基线为 79 对逻辑 Skill", roadmap)

    def test_bilingual_project_pairs_are_unique(self):
        self.assertEqual(
            len(check_docs_bilingual.PROJECT_PAIRS),
            len(set(check_docs_bilingual.PROJECT_PAIRS)),
        )
        self.assertIn(
            ("docs/governance/PHASE_0_MATCH_MERGE_REVIEW.md", "docs/governance/PHASE_0_MATCH_MERGE_REVIEW_EN.md"),
            check_docs_bilingual.PROJECT_PAIRS,
        )

    def test_governance_contracts_expose_required_rules(self):
        required_terms = {
            "docs/governance/DEPRECATION_DECISION_CONTRACT.md": (
                "Deprecated", "Archived", "replacement", "retained_boundary", "migration", "human_decision", "UNASSESSED",
            ),
            "docs/governance/BILINGUAL_CONSISTENCY_CONTRACT.md": (
                "NAME.md", "NAME_EN.md", "SKILL.md", "data-skill", "Generated", "check_docs_bilingual.py",
            ),
            "docs/governance/QUALITY_SCORE_EVAL_CONTRACT.md": (
                "Problem Value", "Scope Clarity", "Eval Coverage", ">=80 Stable", "成功路径", "信息不完整", "范围或风险边界", "NOT_SCORED", "NOT_RUN",
            ),
            "docs/governance/ENHANCEMENT_SPRINT.md": (
                "2–3", "Prompt", "Non-goals", "Workflow", "Deprecation", "NOT_RUN",
            ),
            "docs/governance/CANDIDATE_SKILL_15_STEP_TEMPLATE.md": (
                "Identify Quality Gap", "Capability Match", "Define Non-goals", "Implement", "Eval", "Observe Usage", "Re-evaluate",
            ),
            "docs/governance/SHIFT_LEFT_MILESTONE.md": (
                "v1.1", "v1.2", "v1.3", "v1.4", "Requirement", "Change Impact", "Regression Scope", "NOT_RUN",
            ),
        }
        for rel_path, terms in required_terms.items():
            content = (ROOT / rel_path).read_text(encoding="utf-8")
            for term in terms:
                self.assertIn(term, content, f"{term} missing from {rel_path}")


if __name__ == "__main__":
    unittest.main()
