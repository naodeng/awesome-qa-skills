<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-09-10-requirement-strategy-governance_EN.md">🇬🇧 English</a></div>

# Requirement / Strategy / Impact 治理审查

证据范围：中英文 `SKILL.md` 的用途、输入、流程和决策约束。本文不把静态审查当作运行效果或 Quality Score。

| Skill | 结论 | 依据与后续动作 |
| --- | --- | --- |
| requirements-analysis | Existing | 基础需求分析；保持基础输入路径。 |
| requirements-analysis-plus | Existing | 多材料、冲突和来源角色输入；保留为增强独立能力。 |
| requirement-gap-analysis | Existing | 聚焦缺口、冲突和不可验证项。 |
| acceptance-criteria-review | Existing | 聚焦 AC 的可验证性与异常路径。 |
| testability-analysis | Existing | 聚焦可控、可观测、隔离与可复现。 |
| quality-risk-analysis | Existing | 聚焦质量风险优先级。 |
| change-impact-analysis | Existing | 覆盖需求、配置、代码和依赖变更。 |
| pr-test-impact-analysis | Existing | 以 PR Diff、依赖和历史风险确定测试影响。 |
| test-strategy | Existing | 生成基础测试策略。 |
| test-strategy-plus | Existing | 增加里程碑、门禁、责任与取舍；不与基础版合并。 |
| test-strategy-review | Existing | 评审既有策略并输出 AI 辅助建议；不与生成类合并。 |

## Eval 结构核对

11 个 Skill 的中英文 `evals/cases/` 均存在：基础版各 3 个 case，`requirements-analysis-plus` 与 `test-strategy-plus` 各 4 个，`test-strategy-review` 各 5 个。该结果只证明最低 Eval 工件数量和双语对称性；尚未运行模型评测，因此不据此给出 Quality Score 或 Enhance 结论。
