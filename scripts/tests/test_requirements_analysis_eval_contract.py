from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]


class RequirementsAnalysisEvalContractTest(unittest.TestCase):
    def test_semantic_judges_use_a_model_supported_by_the_codex_login(self):
        for language in ("zh", "en"):
            case_path = (
                ROOT
                / f"skills/{language}/testing-types/requirements-analysis/evals/cases/edge-semantic-agent-judge.yaml"
            )
            text = case_path.read_text(encoding="utf-8")
            self.assertIn("model: openai/gpt-5.6-sol", text, case_path)
            self.assertNotIn("model: openai/gpt-5\n", text, case_path)
            self.assertIn("  timeout_seconds: 720\n", text, case_path)

    def test_semantic_judge_context_is_synchronized_across_languages(self):
        expected = (
            "  context:\n"
            "    profile: minimal\n"
            "    final_message: include\n"
            "    transcript: omit\n"
            "    workspace_diff: omit\n"
            "    generated_files: omit\n"
        )
        for language in ("zh", "en"):
            case_path = (
                ROOT
                / f"skills/{language}/testing-types/requirements-analysis/evals/cases/edge-semantic-agent-judge.yaml"
            )
            self.assertIn(expected, case_path.read_text(encoding="utf-8"), case_path)

    def test_phase1_boundary_matchers_allow_qualified_limits_and_reject_positive_claims(self):
        patterns = {
            "zh": (
                "(?m)^([-*] )?(生产容量|语义等价)(已|已经)(被)?(证明|确认|验证|达标)[。！？.!?]?$",
                "(?m)^([-*] )?语义等价成立[。！？.!?]?$",
                "(?m)^([-*] )?(业务验收)(已|已经)(被)?(完成|通过|批准)[。！？.!?]?$",
            ),
            "en": (
                "(?im)^([-*] )?(production capacity|semantic equivalence) (is|has been) (proven|confirmed|validated|established|demonstrated)[.!]?$",
                "(?im)^([-*] )?semantic equivalence holds[.!]?$",
                "(?im)^([-*] )?(business|production) acceptance (is|has been) (complete|passed|approved)[.!]?$",
            ),
        }
        positive_claims = {
            "zh": (
                "生产容量已经验证。",
                "- 语义等价成立。",
                "业务验收已完成。",
            ),
            "en": (
                "Production capacity is proven.",
                "- semantic equivalence holds.",
                "Business acceptance has been approved.",
            ),
        }
        qualified_limits = {
            "zh": (
                "静态约束不能证明生产容量已验证。",
                "生产容量只能在真实负载测试后验证。",
                "语义等价保持 UNASSESSED。",
                "业务验收尚未完成。",
            ),
            "en": (
                "Static evidence does not prove production capacity.",
                "Production capacity can be validated only after runtime load testing.",
                "Semantic equivalence remains UNASSESSED.",
                "Business acceptance is not complete.",
            ),
        }
        for language in ("zh", "en"):
            compiled = [re.compile(pattern) for pattern in patterns[language]]
            for skill in (
                "change-impact-analysis",
                "performance-workload-modeling",
                "capacity-planning-analysis",
                "quality-risk-analysis",
            ):
                case_path = ROOT / f"skills/{language}/testing-types/{skill}/evals/cases/phase-1-project-context.yaml"
                text = case_path.read_text(encoding="utf-8")
                for pattern in patterns[language]:
                    self.assertIn(pattern, text, case_path)
            for sample in positive_claims[language]:
                self.assertTrue(any(regex.search(sample) for regex in compiled), sample)
            for sample in qualified_limits[language]:
                self.assertFalse(any(regex.search(sample) for regex in compiled), sample)

    def test_plan_keeps_unverified_full_phase1_replay_open(self):
        plan = (ROOT / "docs/superpowers/plans/2026-09-22-v1-6-match-review.md").read_text(encoding="utf-8")
        step5 = next(line for line in plan.splitlines() if "**Step 5: Run each target Skill’s full four-case suite" in line)
        verification = next(line for line in plan.splitlines() if "**Step 1: Run the focused governance tests" in line)
        self.assertTrue(step5.startswith("- [ ]"), step5)
        self.assertTrue(verification.startswith("- [ ]"), verification)
