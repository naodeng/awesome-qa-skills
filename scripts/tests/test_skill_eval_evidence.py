from __future__ import annotations

from pathlib import Path
import subprocess
from tempfile import TemporaryDirectory
import unittest

from scripts import skill_eval_evidence as evidence


class SkillEvalEvidenceTest(unittest.TestCase):
    def test_infers_skill_root_from_an_eval_file(self) -> None:
        with TemporaryDirectory() as temporary:
            skill_root = Path(temporary) / "skill"
            evals = skill_root / "evals"
            evals.mkdir(parents=True)
            (skill_root / "SKILL.md").write_text("name: demo\n", encoding="utf-8")
            prompts = evals / "trigger-prompts.csv"
            prompts.write_text("id,should_trigger,prompt,mode\ncase,true,hello,explicit\n", encoding="utf-8")

            self.assertEqual(evidence.infer_skill_root(prompts), skill_root.resolve())

    def test_metadata_uses_unknown_for_unavailable_values_and_hashes_eval_inputs(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill_root = root / "skill"
            skill_root.mkdir()
            eval_file = skill_root / "eval.yaml"
            prompt_file = skill_root / "prompts.csv"
            eval_file.write_text("schema_version: v1alpha1\n", encoding="utf-8")
            prompt_file.write_text("id,prompt\ncase,hello\n", encoding="utf-8")

            metadata = evidence.build_run_metadata(
                skill_root=skill_root,
                eval_paths=[eval_file, prompt_file],
                engine="codex",
                requested_model=None,
                provider=None,
                environment="none",
                skill_up_version="unknown",
                run_id="run-test-001",
                case_id="case-1",
            )

        payload = metadata.to_dict()
        self.assertEqual(payload["run_id"], "run-test-001")
        self.assertEqual(payload["requested_model"], "unknown")
        self.assertEqual(payload["provider"], "unknown")
        self.assertEqual(payload["case_id"], "case-1")
        self.assertNotEqual(payload["eval_version"], "unknown")
        self.assertRegex(payload["timestamp"], r"^20\d\d-")

    def test_dirty_skill_content_changes_skill_version_identity(self) -> None:
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            skill_root = root / "skill"
            skill_root.mkdir()
            tracked = skill_root / "SKILL.md"
            tracked.write_text("version one\n", encoding="utf-8")
            subprocess.run(["git", "init", "-q"], cwd=skill_root, check=True)
            git_env = {"GIT_AUTHOR_NAME": "Test", "GIT_AUTHOR_EMAIL": "test@example.com",
                       "GIT_COMMITTER_NAME": "Test", "GIT_COMMITTER_EMAIL": "test@example.com"}
            subprocess.run(["git", "add", "SKILL.md"], cwd=skill_root, check=True)
            subprocess.run(["git", "commit", "-q", "-m", "initial"], cwd=skill_root, check=True, env=git_env)

            clean_version = evidence._git_revision(skill_root)
            tracked.write_text("version two\n", encoding="utf-8")
            dirty_version = evidence._git_revision(skill_root)

            self.assertIn("+clean-", clean_version)
            self.assertIn("+dirty-", dirty_version)
            self.assertNotEqual(clean_version, dirty_version)

    def test_eval_version_is_stable_across_checkout_directories(self) -> None:
        with TemporaryDirectory() as first, TemporaryDirectory() as second:
            first_root = Path(first) / "skill" / "evals"
            second_root = Path(second) / "skill" / "evals"
            first_root.mkdir(parents=True)
            second_root.mkdir(parents=True)
            first_files = [first_root / "eval.yaml", first_root / "prompts.csv"]
            second_files = [second_root / "eval.yaml", second_root / "prompts.csv"]
            contents = ["schema_version: v1alpha1\n", "id,prompt\ncase,hello\n"]
            for first_file, second_file, content in zip(first_files, second_files, contents):
                first_file.write_text(content, encoding="utf-8")
                second_file.write_text(content, encoding="utf-8")

            self.assertEqual(evidence._sha256(first_files), evidence._sha256(second_files))

    def test_evidence_state_distinguishes_dry_run_failure_blocked_and_pass(self) -> None:
        self.assertEqual(
            evidence.evidence_state(dry_run=True, runner_exit_code=0, eval_exit_code=0, trace_event_count=0),
            "NOT_RUN",
        )
        self.assertEqual(
            evidence.evidence_state(dry_run=False, runner_exit_code=0, eval_exit_code=0, trace_event_count=2),
            "PASS",
        )
        self.assertEqual(
            evidence.evidence_state(dry_run=False, runner_exit_code=0, eval_exit_code=1, trace_event_count=2),
            "FAIL",
        )
        self.assertEqual(
            evidence.evidence_state(dry_run=False, runner_exit_code=0, eval_exit_code=2, trace_event_count=1),
            "BLOCKED",
        )
        self.assertEqual(
            evidence.evidence_state(dry_run=False, runner_exit_code=1, eval_exit_code=1, trace_event_count=0),
            "BLOCKED",
        )
        self.assertEqual(
            evidence.evidence_state(dry_run=False, runner_exit_code=0, eval_exit_code=1, trace_event_count=0),
            "BLOCKED",
        )
        self.assertEqual(
            evidence.evidence_state(
                dry_run=False,
                runner_exit_code=0,
                eval_exit_code=1,
                trace_event_count=0,
                trace_error_count=1,
            ),
            "FAIL",
        )

    def test_failure_classification_is_explicit_and_not_guessed_for_a_trace_failure(self) -> None:
        self.assertEqual(
            evidence.failure_classification(
                state="FAIL",
                trace_event_count=2,
                requested="EVAL_DEFECT",
            ),
            "EVAL_DEFECT",
        )
        self.assertEqual(
            evidence.failure_classification(state="FAIL", trace_event_count=2, requested=None),
            "UNKNOWN",
        )
        self.assertEqual(
            evidence.failure_classification(state="BLOCKED", trace_event_count=0, requested=None),
            "INFRASTRUCTURE_DEFECT",
        )
        self.assertEqual(
            evidence.failure_classification(
                state="FAIL",
                trace_event_count=0,
                trace_error_count=1,
                requested=None,
            ),
            "UNKNOWN",
        )
        self.assertIsNone(evidence.failure_classification(state="PASS", trace_event_count=2, requested=None))


if __name__ == "__main__":
    unittest.main()
