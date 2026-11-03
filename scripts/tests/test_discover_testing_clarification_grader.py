from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[2]
GRADERS = tuple(
    ROOT / f"skills/{language}/testing-workflows/discover-testing/evals/graders/clarification.py"
    for language in ("zh", "en")
)


def load_grade(path: Path):
    spec = importlib.util.spec_from_file_location(f"router_clarification_{path.parent.parent.parent.parent.name}", path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot load Router clarification grader: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.grade


class DiscoverTestingClarificationGraderTests(unittest.TestCase):
    def test_bilingual_grader_accepts_feature_scope_phase_and_deliverable_questions(self) -> None:
        outputs = {
            "en": "Which feature and scope should I test (repository, PR, module, or URL)? What stage is it in: design, development, or deployed? Do you want test cases, a strategy, or execution? What environment constraints apply?",
            "zh": "请说明要测的功能和范围（产品、模块、PR 或环境），目前处于需求、开发还是部署阶段，希望交付用例、方案还是执行报告；如需执行，请提供测试环境和约束。",
        }
        for language, path in zip(("zh", "en"), GRADERS):
            self.assertTrue(path.is_file(), f"missing clarification grader: {path}")
            grade = load_grade(path)
            with self.subTest(path=path):
                grade(outputs[language], 0)

    def test_bilingual_grader_accepts_a_concise_generic_deliverable_question(self) -> None:
        outputs = {
            "en": "Which feature or scope should I test? What phase is it in now? What deliverable do you want?",
            "zh": "要测哪个功能或范围？目前处于什么阶段？期望交付物是什么？",
        }
        for language, path in zip(("zh", "en"), GRADERS):
            grade = load_grade(path)
            with self.subTest(path=path):
                grade(outputs[language], 0)

    def test_bilingual_grader_accepts_plain_language_what_should_i_deliver_questions(self) -> None:
        outputs = {
            "en": "Which feature and scope should I test? What phase is it in? What should I deliver?",
            "zh": "1. 要测试的新功能是什么，测试范围包括哪些内容？\n2. 这个功能目前处于什么阶段？\n3. 你期望我交付什么？",
        }
        for language, path in zip(("zh", "en"), GRADERS):
            grade = load_grade(path)
            with self.subTest(path=path):
                grade(outputs[language], 0)

    def test_english_grader_accepts_plural_behaviors_as_scope(self) -> None:
        output = (
            "1. Which new feature should I test, and what behaviors should I cover?\n"
            "2. What phase is it in (for example, design, implementation, ready for QA, or released)?\n"
            "3. What deliverable would you like (for example, a test plan, test cases, findings, or a defect report)?"
        )
        grade = load_grade(GRADERS[1])
        grade(output, 0)

    def test_chinese_grader_accepts_feature_or_user_journey_as_scope(self) -> None:
        output = (
            "1. 新功能是什么，具体要测试哪些功能或用户流程？\n"
            "2. 目前处于什么阶段（需求、设计、开发中还是已完成）？\n"
            "3. 你期望我交付什么（测试方案、测试用例、测试结果或缺陷清单）？"
        )
        grade = load_grade(GRADERS[0])
        grade(output, 0)

    def test_bilingual_grader_rejects_clarification_without_a_phase_question(self) -> None:
        outputs = {
            "en": "Which feature and scope should I test? Do you want test cases or execution?",
            "zh": "请说明要测的功能和范围，希望交付用例还是执行报告。",
        }
        for language, path in zip(("zh", "en"), GRADERS):
            grade = load_grade(path)
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "phase"):
                grade(outputs[language], 0)


if __name__ == "__main__":
    unittest.main()
