<div align="right"><a href="./PHASE_0_PROMPT_BASELINE_SOURCES_EN.md">English</a></div>

# Phase 0 候选 Prompt Baseline 来源登记

## 来源锁定

Phase 0 的候选能力参考源是相邻仓库 `naodeng/awesome-qa-prompt`。本次审查固定在
`develop` 提交 `554178fe9b93d851ec01388597ceb7996d22bd1c`，仓库地址为
`https://github.com/naodeng/awesome-qa-prompt`。

这些文件是只读的内容质量与主题覆盖基线，不是 `awesome-qa-skills` 的运行时依赖。Skill
包不得复制 `Standard-version/`、框架变体目录或跨仓库相对链接；本登记只保存来源定位和
匹配证据。

## 六项证据的取法

| 字段 | Baseline 证据位置 |
| --- | --- |
| name | 中英文 `README.md` 标题与 Prompt 的角色/标题 |
| purpose | `README.md` 的用途说明与 Prompt purpose 注释 |
| inputs | `Standard-version/*.md` 的 `必要输入` / `Required inputs` |
| outputs | `Standard-version/*.md` 的 `执行指令` / `Execution instructions` |
| decision_logic | `分析方法` / `分析与设计方法`、专项聚焦与降级规则 |
| workflow_role | 本仓库 `QA_SKILLS_EVOLUTION_ROADMAP.md` 的阶段边界与 Baseline 的专项输出角色 |

## 候选映射

下表中的路径均相对于上述固定提交；`zh` 与 `en` 目录成对存在。

| Candidate | 当前 Target | 结论 | Prompt Baseline | 适配边界 |
| --- | --- | --- | --- | --- |
| `requirement-change-impact-analysis` | `change-impact-analysis` | MATCH | `testing-types/{zh,en}/change-impact-analysis/` | 变更到直接/间接影响；不替代需求缺口分析 |
| `test-impact-analysis` | `change-impact-analysis`, `pr-test-impact-analysis` | MERGE | `change-impact-analysis/` + `pr-risk-analysis/` | 合并变更影响与 PR 测试影响；不把风险分析当执行结果 |
| `code-change-risk-analysis` | `pr-test-impact-analysis` | MERGE | `testing-types/{zh,en}/pr-risk-analysis/` | PR/Diff 风险、关键路径与测试影响；不替代完整代码审查 |
| `workload-modeling` | `performance-workload-modeling` | MATCH | `testing-types/{zh,en}/workload-model-design/` | 负载来源、事务分布、到达/并发和增长假设 |
| `capacity-planning` | `capacity-planning-analysis` | MATCH | `testing-types/{zh,en}/capacity-planning-analysis/` | 容量需求、资源约束和增长假设；不编造指标 |
| `regression-scope-selection` | `regression-scope-analysis`, `regression-test-selection` | MERGE | `regression-scope-analysis/` + `regression-test-selection/` | 先定义回归范围，再从已知资产选择执行集 |
| `ai-test-case-review` | `ai-generated-test-review` | MATCH | `testing-types/{zh,en}/ai-generated-test-review/` | 审核 AI 生成用例；以需求和技术材料为依据 |
| `ai-log-analysis` | `log-analysis` | ENHANCE | `testing-types/{zh,en}/log-analysis/` | 日志事件、时间线、错误和关联证据 |
| `ai-root-cause-analysis` | `root-cause-analysis` | ENHANCE | `testing-types/{zh,en}/root-cause-analysis/` | 证据、原因假设和验证路径；不宣称未证实根因 |
| `quality-risk-identification` | `quality-risk-analysis` | MATCH | `testing-types/{zh,en}/quality-risk-analysis/` | 风险、影响、证据和缓解选项 |
| `ai-test-data-generation` | `test-data-generation` | ENHANCE | `testing-types/{zh,en}/test-data-generation/` | 测试目标、约束、隐私和可追溯数据方案 |
| `llm-output-quality-testing` | `llm-testing` | ENHANCE | `testing-types/{zh,en}/llm-output-quality-evaluation/` | 输出质量维度、评分标准和证据；不等同于运行评测结果 |
| `llm-evaluation` | `llm-evaluation-design` | MATCH | `ai-evaluation-design/` + `llm-output-quality-evaluation/` | 评测目标、数据集、指标、判定规则和复现要求 |

## 限制

上述来源足以支持候选名称、目的、输入、输出、决策逻辑和 Workflow 角色的结构化审查。
它们不提供具体项目的业务需求、Issue/PR 约束、模型运行结果或真实质量分数；因此候选
`decision_state` 使用 `REVIEWED_WITH_LIMITATION`，Quality Score 与 Eval 执行仍保持
`NOT_SCORED` / `NOT_RUN`，Prompt 语义等价与运行有效性仍为 `UNASSESSED`。
