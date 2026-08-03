#!/usr/bin/env python3
"""Optimize skill SKILL.md entries for skill-up / Agent Skills best practices.

- Normalize description to "Use this skill when ...; triggers include ..."
- Rewrite hollow SKILL.md bodies with progressive disclosure + delivery checklist
- Keep prompts/ as the full execution spec; SKILL.md becomes a lean activation entry
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Weak / incomplete descriptions → WHAT + WHEN + bilingual triggers
DESC_FIXES: dict[tuple[str, str], str] = {
    ("zh", "api-test-bruno"): (
        "Use this skill when you need to parse multi-format API definitions and generate Bruno "
        "collections for executable regression; triggers include Bruno、Bruno 集合 and Bruno API testing."
    ),
    ("en", "api-test-bruno"): (
        "Use this skill when you need to parse multi-format API definitions and generate Bruno "
        "collections for executable regression; triggers include Bruno collections and Bruno API testing."
    ),
    ("zh", "api-test-pytest"): (
        "Use this skill when you need to parse multi-format API definitions and generate Pytest "
        "API automation; triggers include Pytest 接口测试、pytest api and API automation with Pytest."
    ),
    ("en", "api-test-pytest"): (
        "Use this skill when you need to parse multi-format API definitions and generate Pytest "
        "API automation; triggers include Pytest API tests and API automation with Pytest."
    ),
    ("zh", "api-test-restassure"): (
        "Use this skill when you need to parse multi-format API definitions and generate Rest Assured "
        "Java test classes; triggers include Rest Assured、RestAssured and Java API automation."
    ),
    ("en", "api-test-restassure"): (
        "Use this skill when you need to parse multi-format API definitions and generate Rest Assured "
        "Java test classes; triggers include Rest Assured, RestAssured, and Java API automation."
    ),
    ("zh", "api-test-supertest"): (
        "Use this skill when you need to parse multi-format API definitions and generate executable "
        "Supertest scripts; triggers include Supertest、Node.js API 测试 and Supertest automation."
    ),
    ("en", "api-test-supertest"): (
        "Use this skill when you need to parse multi-format API definitions and generate executable "
        "Supertest scripts; triggers include Supertest, Node.js API testing, and Supertest automation."
    ),
    ("zh", "performance-test-k6"): (
        "Use this skill when you need k6 load/stress/spike/soak scope, scripts, or runnable entry points; "
        "triggers include k6、k6 性能测试 and k6 performance testing."
    ),
    ("en", "performance-test-k6"): (
        "Use this skill when you need k6 load/stress/spike/soak scope, scripts, or runnable entry points; "
        "triggers include k6, k6 scripts, and k6 performance testing."
    ),
    ("zh", "performance-test-gatling"): (
        "Use this skill when you need Gatling performance scope, simulations, or runnable entry points; "
        "triggers include Gatling、Gatling 性能测试 and Gatling simulation."
    ),
    ("en", "performance-test-gatling"): (
        "Use this skill when you need Gatling performance scope, simulations, or runnable entry points; "
        "triggers include Gatling, Gatling simulations, and Gatling performance testing."
    ),
    ("zh", "requirements-analysis-plus"): (
        "Use this skill when you need to parse Word/HTML/JSON/Markdown/Excel requirements and produce a "
        "structured analysis; triggers include 需求分析增强、requirements analysis plus and requirement parsing."
    ),
    ("en", "requirements-analysis-plus"): (
        "Use this skill when you need to parse Word/HTML/JSON/Markdown/Excel requirements and produce a "
        "structured analysis; triggers include requirements analysis plus and requirement document parsing."
    ),
    ("zh", "testcase-writer-plus"): (
        "Use this skill when you need high-quality test cases from requirements and analysis artifacts; "
        "triggers include 测试用例编写增强、testcase writer plus and advanced test case writing."
    ),
    ("en", "testcase-writer-plus"): (
        "Use this skill when you need high-quality test cases from requirements and analysis artifacts; "
        "triggers include testcase writer plus and advanced test case writing."
    ),
    ("zh", "test-strategy-plus"): (
        "Use this skill when you need a structured test strategy from requirement, analysis, tech, and plan "
        "docs; triggers include 测试策略增强、test strategy plus and advanced test strategy."
    ),
    ("en", "test-strategy-plus"): (
        "Use this skill when you need a structured test strategy from requirement, analysis, tech, and plan "
        "docs; triggers include test strategy plus and advanced test strategy."
    ),
    ("zh", "test-case-reviewer-plus"): (
        "Use this skill when you need structured test-case review findings from requirements, strategy, and "
        "case docs; triggers include 用例评审增强、test case reviewer plus and advanced test case review."
    ),
    ("en", "test-case-reviewer-plus"): (
        "Use this skill when you need structured test-case review findings from requirements, strategy, and "
        "case docs; triggers include test case reviewer plus and advanced test case review."
    ),
    ("zh", "discover-testing"): (
        "Use this skill when you need to route a request to the right testing skill before execution; "
        "triggers include 测试技能路由、discover testing and which testing skill."
    ),
    ("en", "discover-testing"): (
        "Use this skill when you need to route a request to the right testing skill before execution; "
        "triggers include discover testing, testing skill router, and which testing skill."
    ),
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    fm_raw = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    meta: dict[str, str] = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return meta, body


def extract_h1(body: str) -> str:
    m = re.search(r"^#\s+(.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def extract_when_bullets(body: str, lang: str) -> list[str]:
    marker = "## 何时使用" if lang == "zh" else "## When to Use"
    m = re.search(rf"{re.escape(marker)}\n(.*?)(\n## |\Z)", body, re.S)
    if not m:
        return []
    bullets = re.findall(r"^-\s+(.+)$", m.group(1), re.M)
    return [b.strip() for b in bullets]


def extract_prompt_checklist(prompt_path: Path, lang: str) -> list[str]:
    if not prompt_path.exists():
        return []
    text = prompt_path.read_text(encoding="utf-8")
    marker = "## 最低覆盖清单" if lang == "zh" else "## Minimum Coverage Checklist"
    m = re.search(rf"{re.escape(marker)}\n(.*?)(\n## |\Z)", text, re.S)
    if not m:
        return []
    items = re.findall(r"^-\s+(.+)$", m.group(1), re.M)
    # drop intro lines
    return [i for i in items if not i.startswith("除非") and not i.lower().startswith("unless")]


def progressive_refs(skill_dir: Path, lang: str) -> list[str]:
    lines: list[str] = []
    prompt = next(iter(sorted((skill_dir / "prompts").glob("*.md"))), None) if (skill_dir / "prompts").exists() else None
    if lang == "zh":
        if prompt:
            lines.append(
                f"- 产出前必须阅读并遵循 `{prompt.relative_to(skill_dir).as_posix()}`"
                "（最低覆盖清单、输出结构、质量要求）。"
            )
        if (skill_dir / "output-formats.md").exists():
            lines.append("- 需要 Excel/CSV/JSON/Word 等格式时：读 `output-formats.md`，并按用户格式要求输出。")
        if (skill_dir / "output-templates").exists():
            lines.append("- 需要套用现成模板时：读 `output-templates/` 中匹配的模板，不要自创冲突结构。")
        if (skill_dir / "examples").exists():
            lines.append("- 用户要示例或对标现有资产时：读 `examples/` 中相关样例。")
        if (skill_dir / "references").exists():
            lines.append(
                "- 需要框架规范、排障、报告 schema 等深资料时：只读 `references/` 里与当前问题相关的文件，"
                "不要整目录通读。"
            )
        if (skill_dir / "scripts").exists():
            lines.append("- 需要格式转换或辅助校验时：优先使用 `scripts/` 中已有脚本，而不是重写一遍。")
        if (skill_dir / "evals").exists():
            lines.append("- 需要评测/回归本 skill 时：使用 `evals/`，并用 skill-up 校验与运行。")
        if (skill_dir / "reference.md").exists():
            lines.append("- 需要步骤与提示词映射时：读 `reference.md`。")
        if (skill_dir / "quick-start.md").exists():
            lines.append("- 用户只要最短上手路径时：读 `quick-start.md`。")
    else:
        if prompt:
            lines.append(
                f"- Before producing output, read and follow `{prompt.relative_to(skill_dir).as_posix()}` "
                "(minimum coverage, output structure, quality bar)."
            )
        if (skill_dir / "output-formats.md").exists():
            lines.append("- When Excel/CSV/JSON/Word is requested: read `output-formats.md` and honor the format.")
        if (skill_dir / "output-templates").exists():
            lines.append("- When a ready-made template fits: use matching files under `output-templates/`.")
        if (skill_dir / "examples").exists():
            lines.append("- When the user wants examples or alignment with existing assets: read relevant `examples/`.")
        if (skill_dir / "references").exists():
            lines.append(
                "- For deep framework/troubleshoot/schema notes: read only the relevant file(s) under `references/`, "
                "do not load the whole directory."
            )
        if (skill_dir / "scripts").exists():
            lines.append("- For format conversion or helper checks: prefer existing `scripts/` over reinventing.")
        if (skill_dir / "evals").exists():
            lines.append("- For evaluating/regressing this skill: use `evals/` with skill-up.")
        if (skill_dir / "reference.md").exists():
            lines.append("- For step ↔ prompt mapping: read `reference.md`.")
        if (skill_dir / "quick-start.md").exists():
            lines.append("- For the shortest onboarding path: read `quick-start.md`.")
    return lines


def build_body_zh(
    skill_dir: Path,
    title: str,
    when: list[str],
    checklist: list[str],
    is_router: bool,
) -> str:
    when = when or [
        "需要在真实项目里完成本技能对应的测试任务。",
        "需要一份可直接用于执行、评审或跟进的结果。",
    ]
    when_block = "\n".join(f"- {w}" for w in when)
    refs = progressive_refs(skill_dir, "zh")
    refs_block = "\n".join(refs) if refs else "- 以 `prompts/` 主提示词为唯一执行规范。"

    if is_router:
        flow = """\
1. 先读用户请求，识别主要测试目标与阶段。
2. 阅读并遵循 `prompts/` 路由规范：先选 1 个主 skill；仅必要时再补 1 个辅助 skill。
3. 输出路由结论后，把请求交给目标 skill；不要在本 skill 内把整件事执行完。"""
        constraints = """\
- 一次只推荐少量 skill，避免菜单式罗列。
- 目标 skill 已经很明显时，直接指出，不要无效绕路。
- 路由结果要可执行：写清推荐 skill 名与理由。"""
        pitfalls = """\
- 不要一次推荐很多 skill。
- 不要把技能选择写成具体测试执行。
- 不要在信息不足时假装已经选定且可落地。"""
    else:
        flow = """\
1. 阅读并遵循「按需加载」中的主提示词（覆盖清单、输出结构、质量要求）。
2. 只补充真正影响结果的项目上下文：范围、环境、限制、风险、依赖、期望产出。
3. 信息不全时先给可用初版，并显式标出假设与信息缺口。
4. 默认 Markdown；用户指定其他格式时再切换。"""
        constraints = """\
- 按风险/业务影响排优先级，不要平均摊铺。
- 把「已确认事实」和「当前假设」分开写。
- 不要编造用户未提供的接口、字段、环境或根因细节。
- 结果必须可执行：场景具体、有优先级、能指导下一步。"""
        pitfalls = """\
- 范围和上下文都不清楚时，不要假装已经完整可用。
- 不要把所有项写成同等重要。
- 不要跳过假设与信息缺口。
- 不要输出大段与当前工具链无关的空泛理论。"""

    check_lines = [
        "- [ ] 已遵循主提示词的输出结构",
        "- [ ] 已覆盖最低清单，或标明为何省略",
        "- [ ] 高风险项有明确优先级",
        "- [ ] 未编造用户未提供的细节",
        "- [ ] 假设与信息缺口已标明",
    ]
    if checklist:
        preview = "、".join(checklist[:8])
        more = "…" if len(checklist) > 8 else ""
        check_lines.insert(1, f"- [ ] 最低覆盖关注：{preview}{more}（细节以主提示词为准）")

    return f"""# {title}

**英文版：** 见对应英文技能。

## 何时使用

{when_block}

## 执行流程

{flow}

## 核心约束

{constraints}

## 按需加载

{refs_block}

## 交付前自检

{chr(10).join(check_lines)}

## 常见误区

{pitfalls}
"""


def build_body_en(
    skill_dir: Path,
    title: str,
    when: list[str],
    checklist: list[str],
    is_router: bool,
) -> str:
    when = when or [
        "Need help with this testing task in a real project context.",
        "Need an output that can be used directly for execution, review, or follow-up.",
    ]
    when_block = "\n".join(f"- {w}" for w in when)
    refs = progressive_refs(skill_dir, "en")
    refs_block = "\n".join(refs) if refs else "- Treat `prompts/` as the full execution spec."

    if is_router:
        flow = """\
1. Read the user request and identify the primary testing goal and stage.
2. Follow the routing prompt under `prompts/`: pick 1 primary skill; add at most 1 helper only when needed.
3. Hand the request to the target skill; do not execute the full testing work inside this router skill."""
        constraints = """\
- Recommend few skills — avoid menu dumping.
- If the target skill is already obvious, say so directly.
- Make the route actionable: name the skill and the reason."""
        pitfalls = """\
- Do not recommend many skills at once.
- Do not turn skill selection into full test execution.
- Do not pretend a route is complete when information is insufficient."""
    else:
        flow = """\
1. Read and follow the main prompt listed under Progressive disclosure (coverage, structure, quality bar).
2. Add only project context that changes the result: scope, environment, constraints, risks, dependencies, expected deliverable.
3. If input is incomplete, return a usable first draft and explicitly mark assumptions and gaps.
4. Default to Markdown; switch formats only when the user asks."""
        constraints = """\
- Prioritize by risk / business impact — do not treat everything equally.
- Separate confirmed facts from current assumptions.
- Do not invent endpoints, fields, environments, or root causes the user did not provide.
- Keep output executable: concrete scenarios, clear priority, clear next steps."""
        pitfalls = """\
- Do not pretend completeness when scope/context is missing.
- Do not treat every item as equally important.
- Do not skip assumptions and information gaps.
- Do not dump generic theory unrelated to the current toolchain."""

    check_lines = [
        "- [ ] Followed the main prompt's output structure",
        "- [ ] Covered the minimum checklist, or explained omissions",
        "- [ ] High-risk items have explicit priority",
        "- [ ] Did not invent details the user did not provide",
        "- [ ] Assumptions and gaps are marked",
    ]
    if checklist:
        preview = ", ".join(checklist[:8])
        more = ", ..." if len(checklist) > 8 else ""
        check_lines.insert(1, f"- [ ] Minimum coverage focus: {preview}{more} (details in main prompt)")

    return f"""# {title}

**中文版：** See the corresponding Chinese skill.

## When to Use

{when_block}

## Workflow

{flow}

## Core Constraints

{constraints}

## Progressive Disclosure

{refs_block}

## Pre-delivery Checklist

{chr(10).join(check_lines)}

## Common Pitfalls

{pitfalls}
"""


def truncate_short_desc(desc: str, limit: int = 160) -> str:
    if len(desc) <= limit:
        return desc
    return desc[: limit - 1].rstrip() + "…"


def update_openai_yaml(skill_dir: Path, name: str, desc: str) -> None:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    short = truncate_short_desc(desc, 160)
    # escape for YAML double quotes
    short_esc = short.replace("\\", "\\\\").replace('"', '\\"')
    text2, n = re.subn(
        r'^(\s*short_description:\s*).+$',
        rf'\1"{short_esc}"',
        text,
        count=1,
        flags=re.M,
    )
    if n:
        path.write_text(text2, encoding="utf-8")


def optimize_skill(skill_dir: Path, dry_run: bool = False) -> bool:
    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    name = meta.get("name") or skill_dir.name
    lang = "zh" if "/zh/" in str(skill_dir).replace("\\", "/") else "en"

    desc = DESC_FIXES.get((lang, name), meta.get("description", ""))
    if desc and not desc.startswith("Use this skill when") and (lang, name) not in DESC_FIXES:
        # keep existing good-enough descriptions that already use the pattern via other wording
        pass

    title = extract_h1(body) or (f"{name}（中文版）" if lang == "zh" else f"{name} (EN)")
    when = extract_when_bullets(body, lang)
    prompt = next(iter(sorted((skill_dir / "prompts").glob("*.md"))), None)
    checklist = extract_prompt_checklist(prompt, lang) if prompt else []
    is_router = name == "discover-testing"

    new_body = (
        build_body_zh(skill_dir, title, when, checklist, is_router)
        if lang == "zh"
        else build_body_en(skill_dir, title, when, checklist, is_router)
    )
    new_text = f"---\nname: {name}\ndescription: {desc}\n---\n\n{new_body.rstrip()}\n"

    if dry_run:
        print(f"would update: {skill_dir.relative_to(ROOT)}")
        return True

    skill_md.write_text(new_text, encoding="utf-8")
    update_openai_yaml(skill_dir, name, desc)
    print(f"updated: {skill_dir.relative_to(ROOT)}")
    return True


def iter_skills(lang: str | None = None) -> list[Path]:
    roots = []
    if lang in (None, "zh"):
        roots += [ROOT / "skills/zh/testing-types", ROOT / "skills/zh/testing-workflows"]
    if lang in (None, "en"):
        roots += [ROOT / "skills/en/testing-types", ROOT / "skills/en/testing-workflows"]
    out: list[Path] = []
    for root in roots:
        out.extend(sorted(p for p in root.iterdir() if p.is_dir() and (p / "SKILL.md").exists()))
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Optimize skills for skill-up / Agent Skills practices.")
    parser.add_argument("--skill", type=Path, help="One skill directory")
    parser.add_argument("--lang", choices=["zh", "en"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    targets = [args.skill] if args.skill else iter_skills(args.lang)
    for t in targets:
        optimize_skill(t.resolve(), dry_run=args.dry_run)


if __name__ == "__main__":
    main()
