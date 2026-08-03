#!/usr/bin/env python3
"""Scaffold skill-up compatible evals/ for a skill directory."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EVAL_YAML = """\
schema_version: v1alpha1

environment:
  type: none

skills:
  - source: local_path
    path: .

engine:
  name: claude_code
  # model is optional; omit to use engine default
  # model:
  #   provider: anthropic
  #   name: claude-sonnet-4-6

cases:
  files:
{case_files}
  defaults:
    timeout_seconds: 180
    max_turns: 8
    expect:
      exit_code: 0
      must_not_contain:
        - "TODO"
        - "I cannot"

report:
  formats: [json]
"""

CASE_ZH = """\
id: {case_id}
title: {title}
description: |
  {description}

input:
  prompt: |
{prompt}

expect:
  must_contain:
{must_contain}
  must_not_contain:
    - "TODO"
    - "我无法"

judge:
  type: rule_based
  success:
    - output_contains:
        all:
{judge_all}
"""

CASE_EN = """\
id: {case_id}
title: {title}
description: |
  {description}

input:
  prompt: |
{prompt}

expect:
  must_contain:
{must_contain}
  must_not_contain:
    - "TODO"
    - "I cannot"

judge:
  type: rule_based
  success:
    - output_contains:
        all:
{judge_all}
"""


def read_name(skill_dir: Path) -> str:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    m = re.search(r"^name:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else skill_dir.name


def indent_block(text: str, spaces: int = 4) -> str:
    pad = " " * spaces
    return "\n".join(pad + line if line.strip() else "" for line in text.strip("\n").splitlines())


def yaml_list(items: list[str], spaces: int = 4) -> str:
    pad = " " * spaces
    return "\n".join(f'{pad}- "{item}"' for item in items)


def default_cases(lang: str, skill_name: str) -> list[dict]:
    if lang == "zh":
        return [
            {
                "case_id": "basic-success",
                "title": f"{skill_name}：完整上下文下的可用产出",
                "description": "用户提供相对完整的范围与目标，期望得到可执行、有优先级的结果。",
                "prompt": (
                    f"请使用 {skill_name} 技能完成以下任务。\n"
                    "背景：电商订单模块即将发版，核心流程为下单→支付→发货。\n"
                    "环境：SIT；角色：买家、卖家运营、仓配。\n"
                    "请给出聚焦高风险路径的可执行产出，并标明假设与信息缺口。"
                ),
                "must_contain": ["风险", "优先级"],
                "judge_all": ["任务理解", "待确认"],
            },
            {
                "case_id": "edge-incomplete-input",
                "title": f"{skill_name}：信息不完整时仍给初版",
                "description": "输入缺少环境/接口细节时，仍应产出可用初版并显式标注缺口，而不是拒绝或空转。",
                "prompt": (
                    f"请用 {skill_name} 帮我做测试相关产出。\n"
                    "我只有一句话：新版本加了积分兑换。其他文档还没有。\n"
                    "请先给可用初版，并列出必须补齐的信息。"
                ),
                "must_contain": ["假设", "缺口"],
                "judge_all": ["假设", "缺口"],
            },
            {
                "case_id": "edge-risk-priority",
                "title": f"{skill_name}：必须按风险排优先级",
                "description": "防止平均摊铺；结果应区分 P0/高优先级与可延后项。",
                "prompt": (
                    f"使用 {skill_name}。功能很多：登录、搜索、下单、支付、优惠券、积分、客服工单、后台报表。\n"
                    "发版窗口只有半天。请只保留最关键路径，并说明为什么其他项可降级。"
                ),
                "must_contain": ["P0", "优先级"],
                "judge_all": ["P0", "优先级"],
            },
        ]
    return [
        {
            "case_id": "basic-success",
            "title": f"{skill_name}: usable output with adequate context",
            "description": "User provides enough scope and goals; expect an executable, prioritized result.",
            "prompt": (
                f"Use the {skill_name} skill.\n"
                "Context: ecommerce order module release; core flow place order → pay → ship.\n"
                "Environment: SIT; roles: buyer, seller ops, warehouse.\n"
                "Produce an executable, risk-focused result and mark assumptions and gaps."
            ),
            "must_contain": ["risk", "priority"],
            "judge_all": ["understanding", "open"],
        },
        {
            "case_id": "edge-incomplete-input",
            "title": f"{skill_name}: incomplete input still yields a draft",
            "description": "Missing docs should yield a usable draft with explicit gaps, not a refusal.",
            "prompt": (
                f"Use {skill_name}.\n"
                "I only know: the new release adds points redemption. No other docs yet.\n"
                "Give a usable first draft and list the information we must fill in."
            ),
            "must_contain": ["assumption", "gap"],
            "judge_all": ["assumption", "gap"],
        },
        {
            "case_id": "edge-risk-priority",
            "title": f"{skill_name}: prioritize by risk",
            "description": "Avoid flat coverage lists; distinguish P0 from deferrable work.",
            "prompt": (
                f"Use {skill_name}. Features: login, search, checkout, payment, coupons, points, tickets, admin reports.\n"
                "Release window is half a day. Keep only critical paths and explain what can be deferred."
            ),
            "must_contain": ["P0", "priority"],
            "judge_all": ["P0", "priority"],
        },
    ]


def write_case(path: Path, case: dict, lang: str) -> None:
    tmpl = CASE_ZH if lang == "zh" else CASE_EN
    text = tmpl.format(
        case_id=case["case_id"],
        title=case["title"],
        description=case["description"],
        prompt=indent_block(case["prompt"], 4),
        must_contain=yaml_list(case["must_contain"], 4),
        judge_all=yaml_list(case["judge_all"], 10),
    )
    path.write_text(text, encoding="utf-8")


def scaffold(skill_dir: Path, force: bool = False) -> bool:
    skill_dir = skill_dir.resolve()
    if not (skill_dir / "SKILL.md").exists():
        raise SystemExit(f"Not a skill directory (missing SKILL.md): {skill_dir}")

    evals = skill_dir / "evals"
    if evals.exists() and not force:
        print(f"skip (exists): {skill_dir.relative_to(ROOT)}")
        return False

    lang = "zh" if "/zh/" in str(skill_dir).replace("\\", "/") else "en"
    name = read_name(skill_dir)
    cases_dir = evals / "cases"
    cases_dir.mkdir(parents=True, exist_ok=True)

    cases = default_cases(lang, name)
    case_files = []
    for case in cases:
        rel = f"evals/cases/{case['case_id']}.yaml"
        write_case(cases_dir / f"{case['case_id']}.yaml", case, lang)
        case_files.append(f"    - {rel}")

    (evals / "eval.yaml").write_text(
        EVAL_YAML.format(case_files="\n".join(case_files)),
        encoding="utf-8",
    )
    print(f"scaffolded: {skill_dir.relative_to(ROOT)}")
    return True


def iter_skills(lang: str | None = None) -> list[Path]:
    roots = []
    if lang in (None, "zh"):
        roots += [
            ROOT / "skills/zh/testing-types",
            ROOT / "skills/zh/testing-workflows",
        ]
    if lang in (None, "en"):
        roots += [
            ROOT / "skills/en/testing-types",
            ROOT / "skills/en/testing-workflows",
        ]
    out: list[Path] = []
    for root in roots:
        if not root.exists():
            continue
        out.extend(sorted(p for p in root.iterdir() if p.is_dir() and (p / "SKILL.md").exists()))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold skill-up evals/ for skills.")
    parser.add_argument("--skill", type=Path, help="Path to one skill directory")
    parser.add_argument("--all-missing", action="store_true", help="Scaffold all skills missing evals/")
    parser.add_argument("--lang", choices=["zh", "en"], help="Limit --all-missing to one language")
    parser.add_argument("--force", action="store_true", help="Overwrite existing evals/")
    parser.add_argument(
        "--pilot",
        action="store_true",
        help="Scaffold the recommended pilot skill set (zh+en)",
    )
    args = parser.parse_args()

    pilots = {
        "functional-testing",
        "api-testing",
        "bug-reporting",
        "performance-test-k6",
        "test-case-writing",
    }

    targets: list[Path] = []
    if args.skill:
        targets = [args.skill]
    elif args.pilot:
        targets = [p for p in iter_skills() if p.name in pilots]
    elif args.all_missing:
        targets = iter_skills(args.lang)
    else:
        parser.error("Specify --skill, --pilot, or --all-missing")

    created = 0
    for t in targets:
        if scaffold(t, force=args.force):
            created += 1
    print(f"done: {created} skill(s) scaffolded")


if __name__ == "__main__":
    main()
