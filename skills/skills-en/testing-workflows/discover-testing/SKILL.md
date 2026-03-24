---
name: discover-testing
description: Use this skill when you need to route a testing request to the right testing-type or testing-workflow skill quickly; triggers include testing skill discovery, skill routing, and test approach selection.
---

# 测试技能路由（中文版）

用于在执行前快速选出最合适的测试技能，避免“选错技能导致输出不匹配”。

**English:** See section "Testing Skill Discovery (English)" below.

## 输出格式选项（中文）

默认输出为 Markdown。若需 Excel / CSV / JSON，请在需求末尾补一句格式要求。  
详细说明见 **[output-formats.md](output-formats.md)**。

## 何时使用

- 用户问「这个需求应该用哪个测试 skill？」
- 一个需求同时涉及多个测试域（例如功能 + API + 报告）
- 需要把项目阶段（日常 / Sprint / 发布）映射到具体 workflow skill

## 如何使用（中文）

1. 先判断需求是“测试类型问题”还是“阶段流程问题”。
2. 打开 [reference.md](reference.md)，先选 1 个主技能。
3. 如果有需要，再加 1 个辅助技能（例如报告输出）。

## 目标受众（中文）

- 需要先选对技能再执行的 QA
- 需要统一团队使用路径的测试负责人
- 希望让 AI 输出稳定一致的使用者

## 不适用场景（中文）

- 目标技能已经明确的直接执行请求
- 非测试领域需求

## 关键成功因素（中文）

- 先定主技能，再决定是否加辅助技能（最多 1 个）
- workflow skill 必须匹配当前项目阶段和时间约束
- 产出要可追踪（需求 -> 测试活动 -> 结果）

---

# Testing Skill Discovery (English)

Use this gateway skill to choose the right testing skill before execution.

## Output Format Options

Default output is Markdown. If you need Excel / CSV / JSON, append one format sentence at the end of your request.  
See **[output-formats.md](output-formats.md)** for details.

## When to Use

- User asks "which testing skill should I use"
- Request mixes multiple testing domains (e.g. functional + API + report)
- Need to map project phase to a concrete workflow skill

## How to Use

1. Identify request intent: type-specific testing vs phase workflow.
2. Use [reference.md](reference.md) to map to the best primary skill.
3. If needed, add one supporting skill for output/reporting.

## Target Audience

- QA engineers selecting the most suitable skill before execution
- Team leads standardizing skill selection across projects
- AI users who need consistent routing from requirement to test output

## Not Recommended For

- Direct execution requests where the target skill is already explicit
- Non-testing requests outside QA scope

## Critical Success Factors

- Choose one primary skill first, then add at most one supporting skill
- Match workflow skills to project phase and time constraints
- Keep deliverables traceable from requirement to report

## Reference Files

- [reference.md](reference.md) — Testing skill routing map (ZH/EN)
- [output-formats.md](output-formats.md) — Output format guide

## Output Templates and Parsing Scripts

- Template directory: `output-templates/`
- Parser scripts directory: `scripts/`
- Convert scripts directory: `scripts/`

Examples:
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/convert_to_markdown.py output-templates/template-json.json
python3 scripts/batch_convert_templates.py --skip-same
```
