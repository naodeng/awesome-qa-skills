from pathlib import Path
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
