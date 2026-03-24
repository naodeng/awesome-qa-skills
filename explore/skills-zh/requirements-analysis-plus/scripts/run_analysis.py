#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

from common_parser import PARSERS, detect_format


def extract_requirement_points(text: str) -> list:
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    patterns = [
        r"(必须|需要|应当|should|must|required)",
        r"(支持|实现|校验|验证|限制|规则|流程|状态|接口|性能|安全)",
    ]
    points = []
    for line in lines:
        if any(re.search(p, line, flags=re.IGNORECASE) for p in patterns):
            points.append(line)
    return points[:40]


def extract_ambiguities(text: str) -> list:
    signals = [
        "尽快",
        "适当",
        "合理",
        "必要时",
        "etc",
        "and/or",
        "as needed",
        "to be decided",
        "待定",
        "后续确认",
    ]
    out = []
    lines = [x.strip() for x in text.splitlines() if x.strip()]
    for line in lines:
        if any(s.lower() in line.lower() for s in signals):
            out.append(line)
    return out[:20]


def extract_non_functional(text: str) -> list:
    keywords = [
        "性能",
        "并发",
        "吞吐",
        "响应时间",
        "安全",
        "权限",
        "审计",
        "可用性",
        "容灾",
        "sla",
        "latency",
        "throughput",
        "security",
        "availability",
    ]
    out = []
    for line in [x.strip() for x in text.splitlines() if x.strip()]:
        if any(k.lower() in line.lower() for k in keywords):
            out.append(line)
    return out[:25]


def build_analysis(prompt_text: str, source_text: str, source_path: Path, fmt: str) -> str:
    requirement_points = extract_requirement_points(source_text)
    ambiguity_points = extract_ambiguities(source_text)
    non_functional = extract_non_functional(source_text)

    summary = source_text[:600].replace("\n", " ").strip()
    if len(summary) > 300:
        summary = summary[:297] + "..."

    lines = []
    lines.append("# Requirements Analysis Conclusion")
    lines.append("")
    lines.append("## Context")
    lines.append(f"- Source file: `{source_path}`")
    lines.append(f"- Detected format: `{fmt}`")
    lines.append("")
    lines.append("## Requirement Summary")
    lines.append(f"- {summary if summary else 'No summary extracted.'}")
    lines.append("")
    lines.append("## Functional Requirement Points")
    if requirement_points:
        for p in requirement_points:
            lines.append(f"- {p}")
    else:
        lines.append("- No explicit functional point extracted. Please check requirement quality.")
    lines.append("")
    lines.append("## Non-Functional Requirement Points")
    if non_functional:
        for p in non_functional:
            lines.append(f"- {p}")
    else:
        lines.append("- No clear non-functional requirement extracted.")
    lines.append("")
    lines.append("## Ambiguities and Missing Definitions")
    if ambiguity_points:
        for p in ambiguity_points:
            lines.append(f"- {p}")
    else:
        lines.append("- No obvious ambiguous phrasing detected by rule-based checks.")
    lines.append("")
    lines.append("## Suggested Test Focus")
    lines.append("- P0: Core business flow and blocking validations")
    lines.append("- P1: Boundary values, exception paths, and data/state consistency")
    lines.append("- P2: Compatibility, usability, and observability improvements")
    lines.append("")
    lines.append("## Open Questions")
    lines.append("- Are eligibility, inventory, and concurrency rules fully defined?")
    lines.append("- Are rollback/retry/idempotency expectations explicitly specified?")
    lines.append("- Are performance and security baselines measurable and testable?")
    lines.append("")
    lines.append("## Prompt Used")
    lines.append("```text")
    lines.append(prompt_text.strip())
    lines.append("```")
    lines.append("")
    lines.append("## Final Conclusion")
    lines.append("The requirement is parseable and partially testable. Prioritize clarifying ambiguity points before test case design to reduce execution risk and rework.")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Requirements Analysis Plus runner")
    parser.add_argument("--input", required=True, type=Path, help="Requirement document path")
    parser.add_argument(
        "--format",
        choices=["auto", "word", "html", "json", "markdown", "excel"],
        default="auto",
        help="Input format. auto means detect by extension.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output markdown path. Default: <input>.analysis.md",
    )
    parser.add_argument(
        "--prompt",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "prompts" / "requirements-analysis-plus.md",
        help="Prompt template path",
    )
    args = parser.parse_args()

    fmt = detect_format(args.input) if args.format == "auto" else args.format
    parser_fn = PARSERS[fmt]
    parsed_text = parser_fn(args.input)
    prompt_text = args.prompt.read_text(encoding="utf-8", errors="ignore")
    analysis = build_analysis(prompt_text, parsed_text, args.input, fmt)

    out = args.output or args.input.with_name(args.input.stem + ".analysis.md")
    out.write_text(analysis, encoding="utf-8")
    print(str(out))


if __name__ == "__main__":
    main()
