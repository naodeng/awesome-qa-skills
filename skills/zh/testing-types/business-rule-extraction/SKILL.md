---
name: business-rule-extraction
description: Use this skill when requirements, policies, contracts, or workflows need traceable business rules extracted before design or testing; triggers include 业务规则提取, business rule extraction, and policy rule inventory.
---

# 业务规则提取

从需求、政策、契约、流程、验收标准和用户提供的例子中提取可追溯的原子业务规则，保留来源、适用范围、例外和未知项。它是规则盘点与后续评审的输入，不是业务、合规或发布审批。

## 何时使用

- 需要把分散的自然语言规则整理成可比较、可验证的 `BR-##` 条目。
- 需要识别角色、对象、触发、前置条件、动作、结果、不变量和例外。
- 需要在材料不完整或来源冲突时先交付有证据边界的规则初版。

不适用于凭常识补造规则、决定最终优先级、执行系统验证或替业务角色批准政策。

## 工作方式

1. 先阅读并遵循 `prompts/business-rule-extraction.md`，审计目标、版本、时间和适用范围。
2. 将输入分为 `known`、`missing`、`conflicting`、`stale`、`out_of_scope` 和 `assumptions`；保留每个来源的原文和定位。
3. 只在材料支持时合并句子；否则拆成原子规则，并为每条规则建立 `BR-##`、来源和最小证据。
4. 分离直接事实、证据推断、建议和 Human 决策；单独列出例外、未知项、影响和验证提示。
5. 信息不足时交付受限初版，提出可指派、可关闭的补证问题，不把假设升级为事实。

## 核心约束

- 不发明阈值、优先级、状态迁移、角色权限、默认例外或适用范围。
- 不把示例、建议、文档存在或名称匹配写成已执行、已通过、已批准或已发布。
- 每条 `BR-##` 至少包含规则、来源、主体/对象、触发、前置条件、动作/结果、约束/不变量、例外、证据、未知项、影响和验证方法。
- 冲突保留双方来源；无法证明时使用 `missing`、`stale` 或 `unassessed`，不要静默选择一方。

## 按需加载

- 每次产出前必须阅读 `prompts/business-rule-extraction.md`。
- 需要回归时读取 `evals/eval.yaml` 和匹配的 `evals/cases/`；这些文件不证明真实业务语义已执行。
- 需要检查触发行为时使用 `evals/trigger-prompts.csv` 与 `evals/local-rules.json` 运行仓库 trace runner；没有 `skill.selection` 证据时报告 `BLOCKED`。

## 交付前自检

- [ ] 已记录六类输入审计项和适用范围
- [ ] 每条 `BR-##` 都可追溯到最小来源证据
- [ ] 事实、推断、建议和 Human 决策已分开
- [ ] 例外、冲突、未知项和验证提示没有被省略
- [ ] 没有把静态材料或规则清单写成运行结果、审批或发布结论

## 常见误区

- 把多个相似句子合并成一条却丢失版本或地区范围。
- 用“通常”“及时”“合理”等常识替材料补出阈值。
- 只输出规则正文，不保留来源、例外、证据和未决问题。
