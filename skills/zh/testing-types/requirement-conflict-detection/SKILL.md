---
name: requirement-conflict-detection
description: Use this skill when multiple requirement, policy, contract, or acceptance sources may contain mutually exclusive rules or constraints; triggers include 需求冲突检测, requirement conflict detection, and conflicting requirements.
---

# 需求冲突检测

从多份需求、政策、契约、设计或验收材料中识别同一适用范围内互相排斥的规则和约束。保留双方原始来源、适用条件和证据，将需要业务裁决的事项交给 Human，不替团队选择最终优先级。

## 何时使用

- 不同材料分别要求允许和禁止同一行为。
- 角色、状态、权限、数量、时间或接口约束在同一范围内互相排斥。
- 需要确认冲突是否真实存在，还是由版本、平台、租户或适用条件不同造成的表面差异。

不适用于只有一个来源且没有互斥陈述的普通需求审阅，也不用于替业务接受风险、裁决优先级或生成未经批准的折中规则。

## 工作方式

1. 阅读并遵循 `prompts/requirement-conflict-detection.md`。
2. 先审计来源、版本、时间、角色、平台、地区、租户和适用条件；范围不明时标记限制。
3. 将互斥陈述成对保留，确认它们是否针对同一对象、同一动作和同一适用范围。
4. 区分 `conflict`、`ambiguous`、`missing`、`stale` 和 `unassessed`，不把缺少证据升级成冲突。
5. 输出影响、优先级、待决策问题、建议责任角色、关闭条件和验证方法。

## 核心约束

- 使用 `RF-##` 标识发现；每条至少有双方陈述、来源、适用条件、最小证据、影响、优先级和待决策项。
- 不删除、改写或折中任一来源，不替 Human 选择 precedence、风险接受或最终规范。
- 同一规则在不同版本、平台、租户、地区或角色生效时，先报告范围差异；不能直接判定为冲突。
- 缺少版本、范围、来源或上下文时，标记 `missing`/`stale`/`unassessed` 并提出补证问题。
- 不把静态文档中的“已通过”、已有实现或表格存在写成运行时验证结果。

## 按需加载

- 每次产出前必须阅读 `prompts/requirement-conflict-detection.md`。
- 需要回归本 Skill 时使用 `evals/eval.yaml` 和 `evals/cases/`；结构门禁不等于冲突语义已被运行验证。
- 需要验证发现行为时，使用 `evals/trigger-prompts.csv` 与 `evals/local-rules.json` 运行仓库的 `scripts/run_skill_trace_eval.py`；缺少 `skill.selection` 证据时必须报告 `BLOCKED`，不能推断触发成功。
- 以上是仓库根目录下的开发验证步骤；独立安装的 Skill 包不包含仓库级 runner，运行时不依赖该脚本。

## 交付前自检

- [ ] 每条 `RF-##` 都保留双方来源、版本/范围和最小证据
- [ ] 已区分 `conflict`、`ambiguous`、`missing`、`stale` 和 `unassessed`
- [ ] 未静默合并、改写或替双方决定优先级
- [ ] P0/P1 冲突有责任角色、待决策问题、关闭条件和验证方法
- [ ] 未把静态材料、实现存在或测试报告文字当成实际执行证据

## 常见误区

- 看到“must”和“should”就自行判定强弱并选一条。
- 忽略版本、平台、租户、地区或角色边界，制造跨范围冲突。
- 只有一条规则或缺少来源时，凭经验补出另一方。
- 用折中句覆盖原始双方，导致后续裁决无法追溯。
