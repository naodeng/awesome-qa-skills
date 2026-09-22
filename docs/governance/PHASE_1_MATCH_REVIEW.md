<div align="right"><a href="./PHASE_1_MATCH_REVIEW_EN.md">English</a></div>

# v1.6 Phase 1 项目上下文 Match 复核

本文记录 Project #4 的 v1.6 四张 Match Review 卡如何与一个真实项目上下文对齐。它是有边界的项目证据登记，不是语义等价、生产运行、模型效果或业务验收证明。

## 固定范围与证据

- Project：`Awesome QA Skills — Governance & Roadmap`，Project #4。
- 四张卡：`capacity-planning`、`workload-modeling`、`requirement-change-impact-analysis`、`quality-risk-identification`。
- 项目上下文：[`naodeng/dsh-qa@6d650ca`](https://github.com/naodeng/dsh-qa/tree/6d650cae72be8fc582bc4f47d6ba48e3fc28157d)。
- 需求证据：[`2026-09-15-requirements.md`](https://github.com/naodeng/dsh-qa/blob/6d650cae72be8fc582bc4f47d6ba48e3fc28157d/docs/quality-workbench/2026-09-15-requirements.md)。
- 容量证据：[`2026-08-25-technical-design.md`](https://github.com/naodeng/dsh-qa/blob/6d650cae72be8fc582bc4f47d6ba48e3fc28157d/docs/quality-workbench/2026-08-25-technical-design.md)、[`server/quality/test-runner.js`](https://github.com/naodeng/dsh-qa/blob/6d650cae72be8fc582bc4f47d6ba48e3fc28157d/server/quality/test-runner.js)。
- 生命周期证据：[`test/e2e/dsh-panel-lifecycle.spec.js`](https://github.com/naodeng/dsh-qa/blob/6d650cae72be8fc582bc4f47d6ba48e3fc28157d/test/e2e/dsh-panel-lifecycle.spec.js)。

本阶段将项目材料作为输入事实交给目标 Skill 的双语 Eval。它不要求 Eval 运行时访问 dsh-qa，也不把输出中的 `MATCH` 自动升级为实现变更。

## 复核结果

| Candidate | Target Skill | 观察到的项目合同 | 结论 | 状态与边界 | Eval 证据 |
| --- | --- | --- | --- | --- | --- |
| `requirement-change-impact-analysis` | `change-impact-analysis` | Panel/Slot 壳层迁移、保留 iframe/API 边界、MutationObserver 生命周期和真实宿主检查，要求区分直接/传递影响、回滚与证据缺口。 | `MATCH` | `REVIEWED_WITH_LIMITATION`; semantic state=`UNASSESSED`。 | [`zh phase-1-project-context`](../../skills/zh/testing-types/change-impact-analysis/evals/cases/phase-1-project-context.yaml)、[`en phase-1-project-context`](../../skills/en/testing-types/change-impact-analysis/evals/cases/phase-1-project-context.yaml) |
| `workload-modeling` | `performance-workload-modeling` | 每项目一个运行中测试、全局两个、`MAX_ACTIVE_PREVIEWS=20`、排队/运行/终态以及容量超限行为，要求区分交易模型、到达率和并发。 | `MATCH` | `REVIEWED_WITH_LIMITATION`; semantic state=`UNASSESSED`。 | [`zh phase-1-project-context`](../../skills/zh/testing-types/performance-workload-modeling/evals/cases/phase-1-project-context.yaml)、[`en phase-1-project-context`](../../skills/en/testing-types/performance-workload-modeling/evals/cases/phase-1-project-context.yaml) |
| `capacity-planning` | `capacity-planning-analysis` | 运行并发和预览上限、预留槽位、队列与 `QUALITY_RUN_CAPACITY_EXCEEDED`，要求连接吞吐、资源、SLO、降级和扩容时效。 | `MATCH` | `REVIEWED_WITH_LIMITATION`; semantic state=`UNASSESSED`。 | [`zh phase-1-project-context`](../../skills/zh/testing-types/capacity-planning-analysis/evals/cases/phase-1-project-context.yaml)、[`en phase-1-project-context`](../../skills/en/testing-types/capacity-planning-analysis/evals/cases/phase-1-project-context.yaml) |
| `quality-risk-identification` | `quality-risk-analysis` | Panel/Slot 生命周期、iframe/API 边界、运行容量限制和 E2E 生命周期覆盖，要求登记失败模式、概率、影响、可探测性、控制和剩余风险。 | `MATCH` | `REVIEWED_WITH_LIMITATION`; semantic state=`UNASSESSED`。 | [`zh phase-1-project-context`](../../skills/zh/testing-types/quality-risk-analysis/evals/cases/phase-1-project-context.yaml)、[`en phase-1-project-context`](../../skills/en/testing-types/quality-risk-analysis/evals/cases/phase-1-project-context.yaml) |

## 决策边界

- 四条记录继续复用现有双语目标 Skill；没有创建重复目录，也没有把候选名改成新的 canonical name。
- `MATCH` 表示项目上下文与既有目标能力的观察面相符，不表示 Prompt 已完成语义等价证明。
- 项目文档、源代码和 Eval 输出属于静态/项目上下文/评测证据；它们不能替代真实模型对比、外部目标执行、生产观测、人工审批或业务验收。
- 目标 Skill 原有 `eval_execution`、`quality_score` 和生产/业务状态不因本次登记自动升级；缺少对应证据时继续保持 `NOT_RUN`、`NOT_SCORED` 或 `UNASSESSED`。
- 若后续出现实际差异，必须在现有目标 Skill 上开 enhancement/implementation card；不得因为本次 Match Review 直接创建平行目录。

## 复现

```bash
python3 scripts/generate_skill_governance_matrix.py --check
python3 scripts/check_docs_bilingual.py --repo-root .
skill-up validate skills/zh/testing-types/change-impact-analysis/evals/eval.yaml
skill-up validate skills/en/testing-types/change-impact-analysis/evals/eval.yaml
```

八个双语目标 Eval 的项目上下文用例均登记在各自 `eval.yaml`；真实模型回放、生产容量和业务验收仍需单独授权与证据。

截至 2026-09-22，8 个新增项目上下文用例的历史回放均以 `PASS` 结束；四个目标 Skill 的既有三用例回归在中英文两侧也全部 `PASS`，历史证据合计 32/32 个最终 case 通过。该 32/32 记录对应本轮领域事实断言加固之前的配置。修复后，新增项目上下文用例保留每用例 `720s` 的专用预算，既有回归用例保持 `180s` 默认预算，避免无关扩大模型执行成本；本轮 fresh Phase 1 回放首个用例的运行结果是 `ERROR`（达到 `720s` case timeout），因此当前严格断言下的模型证据暂记为 `INSUFFICIENT_EVIDENCE`，不判作 Skill 失败。requirements-analysis 的中英文边界与语义用例已在本轮重新 `PASS`。这些结果只证明目标 Skill 在固定输入上的输出契约和本次模型回放，不升级为语义等价、生产或业务验收。
