---
name: change-to-regression
description: Use this skill when you need pre-change regression guardrails or an explainable regression scope from a proposed or implemented change; triggers include change-to-regression, 变更到回归, and 编码前回归风险.
license: PolyForm-Noncommercial-1.0.0
metadata:
  version: "1.1.0"
  compatibility: ""
  author: "Awesome QA Skills contributors"
  language: "zh-CN"
  category: "testing-workflows"
  source: "https://github.com/naodeng/awesome-qa-skills"
  license-url: "https://polyformproject.org/licenses/noncommercial/1.0.0"
---

# 变更到回归工作流

## 何时使用

在编码前从拟议变更提炼回归护栏，或在编码后根据实际变更和风险选择可解释的回归范围时使用。

## 输出格式选项

默认使用 Markdown。编码前输出候选护栏与待验证假设；编码后输出必须执行/可延后/排除回归表。若用户要求 JSON，仍需按 Prompt 将事实、推断、计划、执行状态和来源分开。

## 核心约束

只组合已有专业 Skill，不复制分析规则；缺少 Host 安装证据时标 `UNKNOWN`。拟议变更没有 Diff/SHA 属正常输入，编码前影响必须标为假设/候选；编码后仍按实际 Diff/SHA 证据分析。不把计划或静态分析写成已执行结果；默认只读，对外写入需授权。

## 如何使用

执行前读取 `prompts/change-to-regression.md`；按契约检查输入，逐阶段完成分析、保留来源、输出风险和交接。通过 `README.md` 查看调用示例和 FAQ。

## 参考文件

- `prompts/change-to-regression.md`：完整工作流、覆盖范围、输出和恢复规则。
- `README.md`：使用示例和 FAQ。
- `evals/`：触发与行为回归用例。

## 交付前自检

- [ ] 输入范围和假设明确
- [ ] 已区分 `PRE_CHANGE` 提案分析与 `POST_CHANGE` Diff 分析
- [ ] 阶段交接保留来源、状态和缺口
- [ ] 执行证据与计划分开
- [ ] 下一步和授权边界明确

## 常见误区

不编造输入、不假设依赖已安装、不把建议当作实际执行或批准。

## 最佳实践

编码前给出已知行为和变更目标；编码后提供精确 base/head SHA、完整 Diff、测试耗时和环境限制。实际运行后附时间、Commit 和运行记录。
