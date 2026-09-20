<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_EVALUATION_CONTRACT_EN.md">🇬🇧 English</a></div>

# Skill Evaluation Contract

本契约定义评测结果能证明什么，避免把静态检查、模型效果和发布结论混在一起。

## Evidence state

| State | 含义 | 允许的结论 |
| --- | --- | --- |
| `PASS` | 配置的断言有对应证据且通过 | 该断言在本次 run 中通过 |
| `FAIL` | 有证据且断言失败 | 记录失败，不自动归因于 Skill |
| `BLOCKED` | 缺少必要 trace、工具、权限或环境证据 | 不能对该断言下结论 |
| `NOT_RUN` | 本次没有执行该层评测 | 不得声称已验证 |
| `NOT_SCORED` | 没有合法 Quality Score 评分证据 | 不得声称有分数 |
| `UNASSESSED` | 当前范围没有评估该维度 | 保持未评估 |
| `INSUFFICIENT_EVIDENCE` | 有运行痕迹，但不足以支持强结论 | 只能做限制性报告 |

`BLOCKED`、`NOT_RUN`、`UNASSESSED` 和 `INSUFFICIENT_EVIDENCE` 都不是通过。

## Evidence levels

1. `Static`：文件、frontmatter、格式和本地脚本。
2. `Structural`：双语配对、独立安装、索引、Eval 结构。
3. `Evaluation`：`skill-up validate` 或实际 `skill-up run`。
4. `Runtime`：真实 Skill、工具、目标和产物执行。
5. `Human review`：语义、术语、风险和 judge calibration。

低层证据不能自动升级为高层证据。例如 `skill-up validate` 不是 runtime 语义验证，Project `Done` 不是 release approval。

## Run metadata

有意义的运行至少记录：

```text
run_id, case_id, variant, skill_version, eval_version,
skill_up_version, engine, provider, requested_model, observed_model,
judge_type, judge_model, environment, timestamp
```

未知值写 `unknown`，不得猜测。报告应保留 eval 定义、case result、trace、judge result、产物路径、限制和失败分类；不得复制不必要的 secrets。

## Failure classification

| 分类 | 典型证据 | 处理 |
| --- | --- | --- |
| `SKILL_DEFECT` | 输入、契约和环境有效，Skill 行为违反要求 | 修 Skill，再重跑受影响用例 |
| `EVAL_DEFECT` | prompt、expect、judge 或 fixture 与契约不一致 | 修 Eval，不把失败归给 Skill |
| `INFRASTRUCTURE_DEFECT` | runner、provider、权限、依赖或目标环境失败 | 修环境或标记 blocked |
| `UNKNOWN` | 证据不足以可靠归因 | 保留限制，不强行定性 |

本地 runner 可以记录分类，但不会根据一个失败自动猜测归因。

## Judge contract

按以下顺序选择：可确定断言用 `rule_based`；可执行产物用 `script`；只有需要语义判断时用 `agent_judge`。Agent Judge 进入治理 gate 前必须用 known-good、known-bad、borderline 样例校准，并记录 variance。

## Trigger and regression

Expected selection 来自 case；observed selection 必须由 `skill.selection` trace 支持。缺少事件为 `BLOCKED`。Benchmark（with Skill vs without Skill）与 Version Regression（previous vs current）是两个不同问题，不能合并。

强 regression 结论需要可比的 Skill commit、Eval dataset、engine/model、judge、environment 和时间窗口；单次 semantic failure 只能写成 observation，除非契约明确允许。

## Standard report

```markdown
# Skill Evaluation Report
## Scope
## Run Metadata
## Configuration
## Evaluation Coverage
## Summary
## Case Results
## Trigger Evidence
## Process Evidence
## Outcome / Artifact Evidence
## Semantic Evidence
## Benchmark / Regression Findings
## Flaky / Blocked / Infrastructure Errors
## Eval Validity Findings
## Limitations
## Recommended Actions
```

Quality Score 继续使用 [`QUALITY_SCORE_EVAL_CONTRACT.md`](./QUALITY_SCORE_EVAL_CONTRACT.md)，本契约不新增评分体系。
