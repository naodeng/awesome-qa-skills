#!/usr/bin/env python3
import argparse
import re
from pathlib import Path
from typing import List, Dict

from common_formatter import (
    format_excel_tsv,
    format_json,
    format_markdown,
    write_word_docx,
    write_output,
)
from common_parser import PARSERS, detect_format


def _extract_candidate_points(req_text: str, ana_text: str) -> List[str]:
    text = "\n".join([req_text, ana_text])
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    patterns = [
        r"(必须|需要|应当|规则|流程|状态|接口|校验|验证|限制)",
        r"(must|should|required|rule|flow|state|api|validate|eligibility)",
    ]
    points = []
    for line in lines:
        if any(re.search(p, line, flags=re.IGNORECASE) for p in patterns):
            points.append(line)
    if not points:
        points = lines[:8]
    return points[:12]


def _priority_for_index(i: int) -> str:
    if i <= 2:
        return "P0"
    if i <= 6:
        return "P1"
    return "P2"


def _normalize_step_text(raw: str) -> str:
    raw = re.sub(r"\s+", " ", raw).strip()
    if len(raw) > 80:
        return raw[:77] + "..."
    return raw


def generate_test_cases(req_text: str, ana_text: str) -> List[Dict]:
    points = _extract_candidate_points(req_text, ana_text)
    cases = []
    for idx, p in enumerate(points, start=1):
        short = _normalize_step_text(p)
        case = {
            "title": f"TC-{idx:03d} {short}",
            "priority": _priority_for_index(idx),
            "type": "功能/接口",
            "preconditions": "活动配置已生效，测试账号和库存数据已准备",
            "steps": f"1) 进入活动页 2) 执行与“{short}”相关操作 3) 观察页面与接口返回",
            "data": "测试账号、活动ID、礼品ID、资格条件参数",
            "expected": "业务结果与规则一致，状态更新正确，无越权和异常漏处理",
            "actual": "",
            "status": "",
            "remark": "",
        }
        cases.append(case)
    return cases


def _render(content_cases: List[Dict], output_format: str) -> str:
    if output_format == "markdown":
        return format_markdown(content_cases)
    if output_format == "json":
        return format_json(content_cases)
    if output_format == "excel":
        return format_excel_tsv(content_cases)
    raise ValueError(f"Unsupported output format: {output_format}")


def _default_output_path(requirement_file: Path, output_format: str) -> Path:
    suffix_map = {
        "markdown": ".testcases.md",
        "word": ".testcases.docx",
        "json": ".testcases.json",
        "excel": ".testcases.tsv",
    }
    return requirement_file.with_name(requirement_file.stem + suffix_map[output_format])


def main() -> None:
    parser = argparse.ArgumentParser(description="TestcaseWriter Plus runner")
    parser.add_argument("--requirement", required=True, type=Path, help="Requirement document file path")
    parser.add_argument("--analysis", required=True, type=Path, help="Requirement analysis result file path")
    parser.add_argument(
        "--output-format",
        default="markdown",
        choices=["markdown", "word", "json", "excel"],
        help="Output format, default is markdown",
    )
    parser.add_argument("--output", type=Path, help="Output file path")
    parser.add_argument(
        "--prompt",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "prompts" / "testcase-writer-plus.md",
        help="Prompt file path",
    )
    args = parser.parse_args()

    req_fmt = detect_format(args.requirement)
    ana_fmt = detect_format(args.analysis)
    req_text = PARSERS[req_fmt](args.requirement)
    ana_text = PARSERS[ana_fmt](args.analysis)

    # Prompt is loaded to keep writing policy tied to this skill execution.
    _ = args.prompt.read_text(encoding="utf-8", errors="ignore")

    cases = generate_test_cases(req_text, ana_text)
    output_path = args.output or _default_output_path(args.requirement, args.output_format)
    if args.output_format == "word":
        write_word_docx(cases, output_path)
    else:
        rendered = _render(cases, args.output_format)
        write_output(rendered, output_path)
    print(str(output_path))


if __name__ == "__main__":
    main()
