<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SHIFT_LEFT_MILESTONE_EN.md">🇬🇧 English</a></div>

# v1.1–v1.4 Shift Left 里程碑

本里程碑把需求、变更、测试、性能、生产和 AI 质量问题前移到可组合的 Skill/Workflow 入口。表格描述治理范围和当前物理能力，不把版本标签或导航关系当作运行证据。

## 版本轨迹

| 版本 | Shift Left 重点 | 当前入口 | 证据边界 |
| --- | --- | --- | --- |
| v1.1 | 需求、设计和测试设计质量 | `requirements-analysis`、`requirement-quality-review`、`test-gap-analysis`、`test-scope-analysis` | 需求/设计输入不足时保留缺口，不推断覆盖 |
| v1.2 | 变更影响、风险与回归范围 | `change-impact-analysis`、`pr-test-impact-analysis`、`regression-scope-analysis`、`regression-test-selection` | 依赖真实 Diff/测试资产；无输入不宣称影响范围 |
| v1.3 | 执行智能、性能和生产证据 | `flaky-test-analysis`、`performance-result-analysis`、`production-verification`、`root-cause-analysis` | 结果、阈值、根因和生产放行保持证据有界 |
| v1.4 | Existing/Match/Merge/Enhance 治理收口 | Registry、Matrix、Lifecycle、Deprecation、Quality Gate、双语/安装清单 | 静态交付完成；运行、模型 Eval、发布审批仍 `NOT_RUN` |

## 组合原则

```text
Requirement → Change Impact → Regression Scope → Test Selection
                         ↘ Risk / Evidence Gap
```

- 组合是可选导航，不创建安装依赖或跨 Skill 内部链接。
- `MATCH` / `MERGE` / `ENHANCE` 先复核既有能力；只有 `NEW` 才进入独立 Skill 设计。
- Workflow 负责组合，Matrix 负责治理，Eval 负责输出契约和边界验证，人工负责发布/风险决策。

## 关联文档

- [治理 Matrix](../SKILL_MATRIX.md)
- [Skills 关系图](../catalog/skills-graph.md)
- [候选 Skill 15 步模板](./CANDIDATE_SKILL_15_STEP_TEMPLATE.md)
- [v1.4 收口](./PHASE_0_V1_4_CLOSEOUT.md)
