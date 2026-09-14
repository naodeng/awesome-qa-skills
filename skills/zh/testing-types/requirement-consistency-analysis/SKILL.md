---
name: requirement-consistency-analysis
description: Use when multiple requirement artifacts may disagree on terminology, identifiers, formats, states, rules, or behavior; triggers include 需求一致性分析, requirement consistency, and cross-document consistency.
---

# 需求一致性分析

比较用户提供的多份需求、契约、设计或规则材料，判断术语、标识、格式、状态、规则和行为描述是否在同一适用范围内一致。它保留来源和版本边界，不静默合并互斥约束。

## 何时使用

- PRD、用户故事、API 契约、原型、技术说明或验收标准使用了不同名称或状态。
- 需要核对多份材料是否对同一角色、字段、流程和结果给出一致描述。
- 同一流程在不同版本、时间或平台的规则可能不同，需要先区分适用范围。

不适用于只有一个来源且只需要通用需求分析的任务，也不用于替业务裁决显式冲突。

## 工作方式

1. 阅读并遵循 `prompts/requirement-consistency-analysis.md`。
2. 建立来源、版本、时间、角色、平台和适用范围清单；没有比较对象时标明限制。
3. 用稳定比较键对照术语、标识、格式、状态、规则和行为；逐项保留证据和关系。
4. 区分 `aligned`、`inconsistent`、`missing`、`stale` 和 `unassessed`；明确互斥规则转为 `conflict`，不静默合并。
5. 给出影响、优先级、责任角色、待确认问题、关闭条件和验证方式。

## 核心约束

- 使用 `RC-##` 标识发现；每行至少有 source pair、comparison key、status、evidence、scope/version、impact 和 action。
- 不把相似名称直接当成同义，不把缺少第二来源当成一致。
- 不跨版本或不同适用范围判定同一事实；范围不明时保留 `stale`/`unassessed`。
- 显式互斥规则建议使用 `requirement-conflict-detection`，只写 Skill 名称，不链接内部文件。
- 不补造状态迁移、字段含义、平台支持或最终规范。

## 按需加载

- 每次产出前必须阅读 `prompts/requirement-consistency-analysis.md`。
- 需要回归本 Skill 时使用 `evals/eval.yaml` 和 `evals/cases/`；结构门禁不证明跨来源语义正确。

## 交付前自检

- [ ] 每个比较结论都列出来源、版本/范围和最小证据
- [ ] 已区分一致、不一致、缺失、过期和未评估
- [ ] 明确冲突没有被静默合并或被错误降级为普通不一致
- [ ] P0/P1 问题有责任角色、待决策问题和验证方式
- [ ] 没有把名称匹配、文档存在或静态表格写成运行结果

## 常见误区

- 看到两个术语相近就直接判定为同一个对象。
- 忽略文档版本、发布日期、平台或租户范围。
- 用一份材料的缺省内容填补另一份材料。
- 把冲突双方改写成一个未经批准的折中规则。
