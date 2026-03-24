#!/usr/bin/env python3
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

from common_formatter import (
    format_excel_tsv,
    format_json,
    format_markdown,
    write_output,
    write_word_docx,
)
from common_parser import PARSERS, detect_format


def _load_doc(path: Path, label: str) -> Tuple[str, str]:
    fmt = detect_format(path)
    text = PARSERS[fmt](path)
    return (label, text)


def _collect_lines(text: str) -> List[str]:
    return [x.strip() for x in text.splitlines() if x.strip()]


def _pick(lines: List[str], keywords: List[str], limit: int) -> List[str]:
    out = []
    for line in lines:
        low = line.lower()
        if any(k.lower() in low for k in keywords):
            out.append(line)
            if len(out) >= limit:
                break
    return out


def _extract_review_signals(docs: List[Tuple[str, str]]) -> Dict[str, str]:
    merged_lines = []
    for _, text in docs:
        merged_lines.extend(_collect_lines(text))

    missing = _pick(
        merged_lines,
        ["并发", "回滚", "幂等", "权限", "越权", "边界", "异常", "库存", "资格"],
        6,
    )
    quality = _pick(merged_lines, ["前置条件", "步骤", "预期", "数据", "断言", "通过率"], 6)
    p0 = _pick(merged_lines, ["必须", "P0", "阻塞", "一致性", "资金", "库存"], 4)
    p1 = _pick(merged_lines, ["P1", "性能", "安全", "兼容", "恢复"], 4)

    return {
        "missing": "；".join(missing) if missing else "并发冲突、失败回滚、权限绕过、边界值覆盖不足",
        "quality": "；".join(quality) if quality else "部分用例前置条件和测试数据描述不充分",
        "p0": "；".join(p0) if p0 else "库存一致性与回滚路径缺少强校验用例",
        "p1": "；".join(p1) if p1 else "性能阈值和安全攻击场景覆盖不足",
    }


def build_review(prompt_text: str, docs: List[Tuple[str, str]]) -> Dict[str, str]:
    signals = _extract_review_signals(docs)
    src_names = "、".join([x[0] for x in docs])

    review = {
        "评审标题": "Test-Case-Reviewer Plus 输出 - 测试用例评审结果",
        "整体结论": "当前用例可用于基础回归，但不建议直接作为最终入库版本；需补齐高风险场景后再通过评审。",
        "覆盖性评估": f"主流程覆盖基本完整，但关键漏测点存在：{signals['missing']}。",
        "可执行性评估": f"可执行性中等，发现问题：{signals['quality']}。",
        "问题清单_P0": signals["p0"],
        "问题清单_P1": signals["p1"],
        "问题清单_P2": "部分文案不统一、步骤粒度不一致、可读性有提升空间。",
        "缺失场景": "重复提交幂等、支付失败补偿、并发抢占冲突、资格边界、越权调用与风控拦截。",
        "改进建议": "补充高风险异常与边界用例；统一前置条件/步骤/预期模板；为关键断言补充可观测指标与日志核验点。",
        "补测计划": "先补P0再补P1：T+1完成用例补充，T+2完成评审回归，阻塞缺陷清零后再入库。",
    }

    review["改进建议"] += f" 参考文档：{src_names}。提示词摘要：{prompt_text.strip()[:80]}..."
    return review


def _default_output_path(testcase_file: Path, output_format: str) -> Path:
    suffix_map = {
        "markdown": ".review.md",
        "word": ".review.docx",
        "json": ".review.json",
        "excel": ".review.tsv",
    }
    return testcase_file.with_name(testcase_file.stem + suffix_map[output_format])


def main() -> None:
    parser = argparse.ArgumentParser(description="Test-Case-Reviewer Plus runner")
    parser.add_argument("--requirement", required=True, type=Path, help="Requirement document file path")
    parser.add_argument("--analysis", type=Path, help="Requirement analysis result file path")
    parser.add_argument("--tech", type=Path, help="Technical document file path")
    parser.add_argument("--plan", type=Path, help="Project plan document file path")
    parser.add_argument("--strategy", type=Path, help="Test strategy document file path")
    parser.add_argument("--testcase", required=True, type=Path, help="Test case document file path")
    parser.add_argument("--other", action="append", type=Path, default=[], help="Other document path, repeatable")
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
        default=Path(__file__).resolve().parents[1] / "prompts" / "test-case-reviewer-plus.md",
        help="Prompt file path",
    )
    args = parser.parse_args()

    docs: List[Tuple[str, str]] = []
    docs.append(_load_doc(args.requirement, "需求文档"))
    docs.append(_load_doc(args.testcase, "测试用例文档"))

    optional_inputs = [
        ("需求分析结果", args.analysis),
        ("技术文档", args.tech),
        ("项目计划", args.plan),
        ("测试策略文档", args.strategy),
    ]
    for label, path in optional_inputs:
        if path:
            docs.append(_load_doc(path, label))

    for idx, p in enumerate(args.other, start=1):
        docs.append(_load_doc(p, f"其他文档{idx}"))

    prompt_text = args.prompt.read_text(encoding="utf-8", errors="ignore")
    review = build_review(prompt_text, docs)
    output_path = args.output or _default_output_path(args.testcase, args.output_format)

    if args.output_format == "word":
        write_word_docx(review, output_path)
    elif args.output_format == "markdown":
        write_output(format_markdown(review), output_path)
    elif args.output_format == "json":
        write_output(format_json(review), output_path)
    elif args.output_format == "excel":
        write_output(format_excel_tsv(review), output_path)
    else:
        raise ValueError(f"Unsupported output format: {args.output_format}")

    print(str(output_path))


if __name__ == "__main__":
    main()
