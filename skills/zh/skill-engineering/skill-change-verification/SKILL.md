---
name: skill-change-verification
description: Use this skill when selecting and reporting verification for Skill changes; triggers include Skill 变更验证、质量门禁、evidence level。
---

# Skill 变更验证

## 何时使用

需要根据变更范围选择最小但足够的检查，并准确说明证据能支持什么结论时使用。

## 执行流程

1. 将变更分为内容、元数据/目录、脚本、Evals 和运行时影响。
2. 选择对应的静态、结构、评测、运行时和人工审查证据。
3. 记录已执行命令、结果、未执行项目及原因。
4. 输出残余风险，以及“可以声称/不能声称”的结论边界。

## 核心约束

- `skill-up validate` 不等于运行时语义验证。
- 不知道项目命令时标记待确认，不得猜测。
- 验证范围必须覆盖实际变更，不因运行全量检查而隐藏缺口。

## 按需加载

产出前阅读 `prompts/skill-change-verification.md`；需要评测时阅读 `evals/`。
