#!/usr/bin/env python3
import argparse
import re
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


def _summary_from_docs(docs: List[Tuple[str, str]]) -> Dict[str, str]:
    merged_lines = []
    for _, text in docs:
        merged_lines.extend(_collect_lines(text))

    core = _pick(merged_lines, ["必须", "应当", "required", "must", "规则", "流程", "资格", "库存"], 5)
    perf = _pick(merged_lines, ["性能", "并发", "rps", "响应", "latency", "throughput"], 3)
    sec = _pick(merged_lines, ["安全", "权限", "鉴权", "风控", "owasp", "token", "越权"], 3)
    schedule = _pick(merged_lines, ["t-", "里程碑", "上线", "计划", "deadline", "release"], 4)

    return {
        "core": "；".join(core) if core else "核心业务流程、资格校验、库存一致性",
        "perf": "；".join(perf) if perf else "高峰并发与稳定性验证",
        "sec": "；".join(sec) if sec else "认证鉴权、越权、数据保护",
        "schedule": "；".join(schedule) if schedule else "按项目节奏分阶段执行与评审",
    }


def build_strategy(prompt_text: str, docs: List[Tuple[str, str]]) -> Dict[str, str]:
    src_names = "、".join([label for label, _ in docs])
    summary = _summary_from_docs(docs)

    strategy = {
        "策略标题": "Test Strategy Plus 输出 - 业务活动质量保障策略",
        "质量目标": f"保障关键链路正确性、稳定性与安全性。重点：{summary['core']}；性能关注：{summary['perf']}。",
        "范围_包含": "资格校验、活动参与、库存扣减、订单状态联动、失败回滚、幂等控制、关键接口与前端主流程。",
        "范围_不包含": "非活动范围的历史模块重构验证、与当前发布无关的低风险边缘特性。",
        "测试类型与覆盖": "功能+接口为P0，性能压测/稳定性为P1，安全与权限为P1，兼容与可访问性为P2；覆盖正常、异常、边界、并发冲突场景。",
        "环境与工具": "独立测试环境（网关/服务/缓存/消息队列/数据库）+ API自动化 + UI回归 + 性能压测工具 + 安全扫描工具。",
        "测试数据策略": "构造多层级用户与库存数据集，覆盖资格达标/不达标、库存充足/不足、重复提交、失败补偿；敏感数据脱敏。",
        "准入准出标准": "准入：需求冻结、接口文档可用、环境联通；准出：P0用例通过率100%，P1通过率>=95%，阻塞缺陷清零，高风险项有结论。",
        "风险与缓解": f"风险：并发超卖、状态不一致、越权与刷单、回滚失败。缓解：前置压测、幂等校验、风控规则验证、补偿链路演练。补充：{summary['sec']}。",
        "里程碑与角色": f"里程碑：{summary['schedule']}。角色：QA负责人统筹策略与门禁，测试工程师执行分层测试，开发与SRE协同定位和修复。",
        "交付物与度量": f"交付物：测试策略、测试计划、用例集、缺陷报告、测试总结。度量：需求覆盖率、缺陷密度、通过率、回归耗时、线上问题逃逸率。来源文档：{src_names}。",
    }

    strategy["交付物与度量"] += f" 提示词约束摘要：{prompt_text.strip()[:80]}..."
    return strategy


def _default_output_path(requirement_file: Path, output_format: str) -> Path:
    suffix_map = {
        "markdown": ".strategy.md",
        "word": ".strategy.docx",
        "json": ".strategy.json",
        "excel": ".strategy.tsv",
    }
    return requirement_file.with_name(requirement_file.stem + suffix_map[output_format])


def main() -> None:
    parser = argparse.ArgumentParser(description="Test Strategy Plus runner")
    parser.add_argument("--requirement", required=True, type=Path, help="Requirement document file path")
    parser.add_argument("--analysis", type=Path, help="Requirement analysis result file path")
    parser.add_argument("--tech", type=Path, help="Technical document file path")
    parser.add_argument("--plan", type=Path, help="Project plan document file path")
    parser.add_argument("--other", action="append", type=Path, default=[], help="Other reference document path, repeatable")
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
        default=Path(__file__).resolve().parents[1] / "prompts" / "test-strategy-plus.md",
        help="Prompt file path",
    )
    args = parser.parse_args()

    docs: List[Tuple[str, str]] = []
    docs.append(_load_doc(args.requirement, "需求文档"))

    optional_inputs = [
        ("需求分析结果", args.analysis),
        ("技术文档", args.tech),
        ("项目计划", args.plan),
    ]
    for label, path in optional_inputs:
        if path:
            docs.append(_load_doc(path, label))

    for idx, p in enumerate(args.other, start=1):
        docs.append(_load_doc(p, f"其他文档{idx}"))

    prompt_text = args.prompt.read_text(encoding="utf-8", errors="ignore")
    strategy = build_strategy(prompt_text, docs)
    output_path = args.output or _default_output_path(args.requirement, args.output_format)

    if args.output_format == "word":
        write_word_docx(strategy, output_path)
    elif args.output_format == "markdown":
        write_output(format_markdown(strategy), output_path)
    elif args.output_format == "json":
        write_output(format_json(strategy), output_path)
    elif args.output_format == "excel":
        write_output(format_excel_tsv(strategy), output_path)
    else:
        raise ValueError(f"Unsupported output format: {args.output_format}")

    print(str(output_path))


if __name__ == "__main__":
    main()
