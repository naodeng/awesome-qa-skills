---
name: requirement-ambiguity-analysis
description: Use when requirement wording has unclear actors, references, scope, quantities, conditions, timing, states, or acceptance criteria; triggers include 需求歧义分析, requirement ambiguity, and unclear requirements.
---

# 需求歧义分析

识别需求中无法唯一理解或无法判定的表达，保留原句与来源，说明缺少哪个区分条件，以及如何由责任角色关闭问题。它分析 under-specification，不替用户选择解释。

## 何时使用

- 需求包含“及时”“快速”“必要时”“正常”“支持”等未定义词。
- 角色、对象、范围、数量、条件、时间、状态或验收判定有多种可能解释。
- 需要判断一句话是普通歧义，还是已经构成跨来源冲突。

不适用于已有明确互斥规则的最终裁决、测试执行或凭常识补全业务规则。

## 工作方式

1. 阅读并遵循 `prompts/requirement-ambiguity-analysis.md`。
2. 先做输入审计，区分已知、缺失、冲突、过期、范围外和最小假设。
3. 逐条保留含歧义的原句、来源、适用范围和缺失区分项；列出可能理解，但不选择其中一个。
4. 按交付、质量和可测性影响排序，给出可指派、可关闭的问题和验证方式。
5. 若材料明确互斥，标为冲突并建议使用 `requirement-conflict-detection`；只写 Skill 名称，不链接其内部文件。

## 核心约束

- 使用 `RA-##` 标识发现；至少区分 `ambiguous`、`missing`、`untestable`、`conflict` 和 `out_of_scope`。
- 不把缺失阈值、角色、格式、时限、状态或权限从常识中补出来。
- 每条重要发现保留 `source`、原句、缺失区分项、可能解释、影响、优先级、问题、责任角色和验证方式。
- 信息不足时仍给最小可用初版，并显式列出假设和 3–5 个高价值问题。
- 不决定哪种解释是最终需求，不代替产品、业务或合规角色裁决。

## 按需加载

- 每次产出前必须阅读 `prompts/requirement-ambiguity-analysis.md`。
- 需要回归本 Skill 时使用 `evals/eval.yaml` 和 `evals/cases/`；文件结构或规则评测不代表真实项目效果。

## 交付前自检

- [ ] 已引用歧义原句和来源
- [ ] 已说明缺少的可判定区分项，而不是只说“有歧义”
- [ ] 已把可能理解和最终裁决分开
- [ ] 已对 P0/P1 问题给出责任角色、关闭条件和验证方式
- [ ] 已将明确冲突路由出去，没有静默选边

## 常见误区

- 把“行业通常如此”当成需求事实。
- 只改写句子，不说明不同理解会造成什么影响。
- 把两个版本或不同适用范围的规则强行合并。
- 以“信息不足”为由拒绝输出任何可用初版。
