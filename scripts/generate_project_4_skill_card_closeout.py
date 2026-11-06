#!/usr/bin/env python3
"""Generate bilingual Project #4 Skill-card closeout evidence from the governance registry."""

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "docs/governance/skill-governance-registry.yaml"
OUTPUTS = {
    "zh": ROOT / "docs/governance/PROJECT_4_SKILL_CARDS_CLOSEOUT.md",
    "en": ROOT / "docs/governance/PROJECT_4_SKILL_CARDS_CLOSEOUT_EN.md",
}
CONCLUSIONS = ("EXISTING", "MATCH", "ENHANCE", "MERGE", "NEW")


def status_label(result: str, locale: str) -> str:
    labels = {
        "PASS": "通过" if locale == "zh" else "PASS",
        "FAIL": "失败" if locale == "zh" else "FAIL",
        "BLOCKED": "受阻" if locale == "zh" else "BLOCKED",
        "NOT_RUN": "未运行" if locale == "zh" else "NOT_RUN",
        "N/A": "不适用" if locale == "zh" else "N/A",
        "PENDING": "待最终门禁" if locale == "zh" else "PENDING FINAL GATE",
    }
    return labels.get(result, result)


def markdown_target(registry: dict[str, Any], slug: str, locale: str) -> str:
    language = "zh" if locale == "zh" else "en"
    paths = []
    for candidate in registry["candidates"]:
        paths.extend(
            path for path in candidate.get("target_evidence_paths", [])
            if path.startswith(f"skills/{language}/")
            and path.endswith(f"/{slug}/SKILL.md")
        )
    paths = list(dict.fromkeys(paths))
    link_paths = []
    for path in paths:
        relative = f"../../{path}"
        link_paths.append(f"[{slug}]({relative})")
    return "<br>".join(link_paths) if link_paths else f"`{slug}`"


def render_closeout(data: dict[str, object], locale: str) -> str:
    english = locale == "en"
    rows = data.get("project_reviews", [])
    batch = data.get("project_4_batch", {})
    candidates = data.get("candidates", [])
    if len(rows) != 23:
        raise ValueError(f"expected 23 Project #4 card reviews, found {len(rows)}")
    project_slugs = {row["candidate"] for row in rows}
    project_candidates = [candidate for candidate in candidates if candidate["slug"] in project_slugs]
    conclusion_counts = {
        conclusion: sum(candidate.get("conclusion") == conclusion for candidate in project_candidates)
        for conclusion in CONCLUSIONS
    }

    if english:
        title = "Project #4 Skill Cards — Batch Closeout"
        intro = (
            f"Review snapshot: {batch['snapshot_date']}. Project #4 had {batch['snapshot_total_items']} items and "
            f"{batch['snapshot_todo_items']} Todo items; this closeout covers {batch['in_scope_items']} Skill cards "
            f"(all Todo at the snapshot). The other {batch['out_of_scope_todo_items']} Todo items are outside scope."
        )
        method_title = "Capability match method"
        axes = [
            ("Name", "Check canonical names and synonyms."),
            ("Purpose", "Compare the quality problem and intended user decision."),
            ("Inputs", "Compare required evidence, context, constraints, and dependencies."),
            ("Outputs", "Compare findings, recommendations, and artifacts."),
            ("Decision logic", "Compare analysis rules, risk models, and evidence boundaries."),
            ("Workflow role", "Compare the stage and composition position."),
        ]
        boundary = (
            "`REVIEWED_WITH_LIMITATION` records a repository-backed capability review. It does not prove semantic "
            "equivalence, runtime behavior, model effectiveness, host availability, release approval, or business acceptance."
        )
        table_head = "| Project item ID | Card title | Priority / target | Conclusion | Existing target capabilities | Bounded review result | Status |"
        table_rows = ["| --- | --- | --- | --- | --- | --- | --- |"]
        evidence_label = "[Six-field evidence](../SKILL_MATCHING_REGISTER_EN.md)"
        dup_title = "Duplicate cards and shared evidence"
        eval_title = "Eval and behavior evidence"
        eval_text = (
            "No Skill behavior contract changed in this batch, so new Skill-up behavior Eval runs are `N/A`. The existing "
            "bilingual Eval files and cases remain in place and are covered by the static quality/eval-structure gates. "
            "Real-model and host/runtime evaluation remains `NOT_RUN`; semantic equivalence and business acceptance remain `UNASSESSED`."
            " Quality Score remains `NOT_SCORED`."
        )
        matrix_text = (
            f"The registry records 21 distinct capability candidates and 23 card reviews: {conclusion_counts['EXISTING']} EXISTING, "
            f"{conclusion_counts['MATCH']} MATCH, {conclusion_counts['ENHANCE']} ENHANCE, {conclusion_counts['MERGE']} MERGE, "
            f"and {conclusion_counts['NEW']} NEW. The generated Matrix links "
            "each affected target package to this closeout record; the generated Matching Register carries the six-field "
            "evidence. Existing Skill lifecycle/status fields are unchanged."
        )
        verification_title = "Verification results"
        result_head = "| Command / evidence | Result |"
    else:
        title = "Project #4 Skill 卡片批次收口"
        intro = (
            f"复核快照：{batch['snapshot_date']}。Project #4 共 {batch['snapshot_total_items']} 张卡，其中 {batch['snapshot_todo_items']} 张为 Todo；"
            f"本记录覆盖 {batch['in_scope_items']} 张 Skill 卡（快照时均为 Todo），其余 {batch['out_of_scope_todo_items']} 张 Todo 卡不在本批范围。"
        )
        method_title = "能力匹配方法"
        axes = [
            ("名称", "核对 canonical name 与同义名称。"),
            ("目的", "比较解决的质量问题和预期决策。"),
            ("输入", "比较所需证据、上下文、约束和依赖。"),
            ("输出", "比较发现、建议和产物。"),
            ("决策逻辑", "比较分析规则、风险模型和证据边界。"),
            ("Workflow 角色", "比较阶段位置与组合关系。"),
        ]
        boundary = (
            "`REVIEWED_WITH_LIMITATION` 表示基于仓库证据完成能力复核，不证明语义等价、运行行为、模型效果、宿主可用性、"
            "发布批准或业务验收。"
        )
        table_head = "| Project item ID | 卡片标题 | Priority / Target Version | 结论 | 现有目标能力 | 有边界的复核结果 | 状态 |"
        table_rows = ["| --- | --- | --- | --- | --- | --- | --- |"]
        evidence_label = "[六项证据](../SKILL_MATCHING_REGISTER.md)"
        dup_title = "重复卡与共享证据"
        eval_title = "Eval 与行为证据"
        eval_text = (
            "本批没有改变任何 Skill 行为合同，因此新增 skill-up 行为 Eval 为 `N/A`。现有双语 Eval 配置和用例保留，"
            "并由静态质量/结构门禁覆盖。真实模型与宿主/运行时评测仍为 `NOT_RUN`；语义等价和业务验收仍为 `UNASSESSED`。"
            "质量评分保持 `NOT_SCORED`。"
        )
        matrix_text = (
            f"Registry 记录 21 个不同能力候选项和 23 条卡片复核：EXISTING {conclusion_counts['EXISTING']}、"
            f"MATCH {conclusion_counts['MATCH']}、ENHANCE {conclusion_counts['ENHANCE']}、"
            f"MERGE {conclusion_counts['MERGE']}、NEW {conclusion_counts['NEW']}。"
            "生成后的 Matrix 将受影响目标包链接到本收口记录；"
            "生成后的 Matching Register 保存六项匹配证据。现有 Skill 生命周期/状态字段保持不变。"
        )
        verification_title = "验证结果"
        result_head = "| 命令 / 证据 | 结果 |"

    lines = [
        '<div align="right">' + ('<a href="./PROJECT_4_SKILL_CARDS_CLOSEOUT.md">中文</a>' if english else '<a href="./PROJECT_4_SKILL_CARDS_CLOSEOUT_EN.md">English</a>') + '</div>',
        "",
        f"# {title}",
        "",
        intro,
        "",
        f"## {method_title}",
        "",
        "| Axis | Review rule |" if english else "| 维度 | 复核规则 |",
        "| --- | --- |",
        *[f"| {axis} | {rule} |" for axis, rule in axes],
        "",
        boundary,
        "",
        matrix_text,
        "",
        "## Card decisions" if english else "## 卡片结论",
        "",
        table_head,
        *table_rows,
    ]
    for row in rows:
        target_links = "<br>".join(markdown_target(data, slug, locale) for slug in row["target_skills"])
        summary = row["summary_en" if english else "summary_zh"]
        action = row["next_action_en" if english else "next_action_zh"]
        duplicate_note = row.get("duplicate_note_en" if english else "duplicate_note_zh", "")
        result = summary + (" " + duplicate_note if duplicate_note else "") + " " + action + f" {evidence_label}."
        status = f"{row['baseline_status']} → {row['current_status']}" if not english else f"{row['baseline_status']} → {row['current_status']}"
        table_rows.append(
            f"| `{row['item_id']}` | {row['title']} | {row['priority']} / {row['target_version']} | `{'REVIEWED_WITH_LIMITATION'}` · `{row['conclusion']}` | {target_links} | {result} | `{status}` |"
        )
    lines.extend(table_rows[1:])

    if english:
        lines.extend([
            "",
            f"## {dup_title}",
            "",
            "- `continuous-quality-workflow`: the v3.4 and v4.0 cards share one capability review; each card keeps its own item ID, priority, target version, and status.",
            "- `ai-native-quality-workflow`: the two v4.0 cards have the same title and body; they share one capability review and retain separate Project items.",
            "- Duplicate Project items were not deleted or merged; the shared candidate and evidence are recorded once in the Registry and referenced from both rows above.",
            "",
            f"## {eval_title}",
            "",
            eval_text,
            "",
            f"## {verification_title}",
            "",
            result_head,
            "| --- | --- |",
        ])
    else:
        lines.extend([
            "",
            f"## {dup_title}",
            "",
            "- `continuous-quality-workflow`：v3.4 与 v4.0 两张卡共用同一能力复核；各自 item ID、Priority、Target Version 和状态仍独立保留。",
            "- `ai-native-quality-workflow`：两张 v4.0 卡的标题和正文相同，共用同一能力复核，Project item 仍分别保留。",
            "- 不删除或合并重复 Project item；Registry 中只登记一份共享候选能力证据，并由上方两行分别关联。",
            "",
            f"## {eval_title}",
            "",
            eval_text,
            "",
            f"## {verification_title}",
            "",
            result_head,
            "| --- | --- |",
        ])
    for result in batch.get("validation_results", []):
        command = result.get("command", "")
        state = status_label(str(result.get("result", "PENDING")), locale)
        notes = result.get("notes_en" if english else "notes_zh", "")
        lines.append(f"| `{command}` | `{state}`{': ' + notes if notes else ''} |")
    if not batch.get("validation_results"):
        pending = "Final validation entries will be recorded here." if english else "最终验证结果将在此记录。"
        lines.append(f"| {pending} | `PENDING` |")
    lines.extend([
        "",
        "## Closeout boundary" if english else "## 收口边界",
        "",
        (
            "Project `Done` closes this bounded governance review only. It does not advance package lifecycle, semantic equivalence, Eval execution, runtime validation, release state, or business acceptance."
            if english else
            "Project `Done` 只表示本次有边界的治理复核完成，不升级 Skill 包生命周期、语义等价、Eval 执行、运行时验证、发布状态或业务验收。"
        ),
        "",
        "Registry source: `docs/governance/skill-governance-registry.yaml`. Regenerate with `python3 scripts/generate_project_4_skill_card_closeout.py`; check with `python3 scripts/generate_project_4_skill_card_closeout.py --check`.",
    ])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated closeout views are stale")
    args = parser.parse_args()
    data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    stale = []
    for locale, path in OUTPUTS.items():
        expected = render_closeout(data, locale)
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(expected, encoding="utf-8")
    if stale:
        print("Stale Project #4 closeout view(s): " + ", ".join(stale))
        return 1
    if args.check:
        print("Project #4 bilingual closeout views are up to date.")
    else:
        print("Generated bilingual Project #4 closeout views.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
