<div align="right"><strong>🇨🇳 中文</strong> | <a href="./WORKFLOW_RELIABILITY_ENHANCEMENT_V1_EN.md">🇬🇧 English</a></div>

# Workflow Reliability Enhancement v1.0

## 目标与边界

把现有 QA Skill 组合成可追踪、可评测的工作流，同时保留 canonical name、双语目录和单 Skill 独立安装能力。工作流只定义选择、阶段、交接、证据与门禁；本仓库不实现任务调度、持久化状态或宿主工具权限引擎。

本轮按一个连续交付执行，四个 Iteration 代表依赖顺序，不是中途停下等待另一次授权。新增编排层只负责组合已有专业 Skill，不复制它们的分析提示词。

## 实施前现状审计（2026-10-30 工作区）

| 能力 | 现状与证据 | 决策 |
| --- | --- | --- |
| Workflow 目录 | 当前有 10 个已跟踪的 `testing-workflows` 包；工作区另有未跟踪的 `tdd-quality-workflow`，因此文件系统中为 11 个。目录中包括 Router、时间线工作流和质量视角提示集合；质量视角包不是固定的阶段流水线。 | 保留原目录与 canonical name；分类记录中区分 router、workflow、prompt collection。 |
| Router | 实施前 `discover-testing` 有 166 项能力目录快照、五条 Composition route、单主 Skill/最多一个辅助 Skill 规则及多条路由 Eval。本轮快照更新到 169 项并增加三条端到端路由。目录存在不代表 Host 已安装，缺少安装证据时标为 `UNKNOWN`。 | 保留并增强现有 Router；增加显式端到端 Workflow 路由与缺失依赖、误路由、冲突用例。 |
| 专业能力 | 已有代码审查、变更影响、回归选择、需求分析、可测试性、测试策略、测试用例、测试有效性、发布测试、质量门禁和生产验证等 Skill。 | 复用现有 Skill；仅新增三个编排层包：`pr-quality-review`、`requirement-to-test`、`change-to-regression`。 |
| 发布就绪 | `release-testing-workflow` 已有 T-N、Go/No-Go 建议、证据包、专项交接及人工审批边界。路线图也明确不应把它拆成重复的 readiness 包。 | 在现有包增加标准 Workflow/Evidence Contract 支持，不新建 release Skill。 |
| Eval / 质量门禁 | Skill 级 `eval.yaml`、case、Skill-up 校验/运行脚本、Skill 完整性/独立性/双语/CLI 兼容门禁均已存在；`skill_eval_evidence.py` 记录 Skill Eval 的运行元数据。当前质量脚本为 11 组检查。 | 保留 Skill Eval；补充 Workflow 契约验证和跨阶段交接、权限、恢复场景。结构验证不冒充模型行为 Eval。 |
| 状态与证据 | 目前没有通用 `workflow.yaml`、`evidence.json` Schema，也没有持久化 Workflow Runtime。 | 新增版本化 JSON Schema、样例和依赖无关校验器；定义 Checkpoint/过期/重复执行规则，运行态由外部 Workbench 实现。 |
| 生命周期 | 实施前治理 Registry 收录 166 个中英文 Skill 对；本轮扩展到 169 对并为每条记录增加独立生命周期状态。真实调用量和使用价值数据不可得。 | 定义生命周期与退役/迁移政策；没有采用数据时将使用价值标为 `UNASSESSED`，不据目录或静态 Eval 推断受欢迎程度。 |
| Agent 分发 | 仓库安装脚本支持 Codex、Claude Code、Cursor 等；`skills@1.7.0` 有固定 CLI gate。安装预览不等于工具内运行验证。 | 增加兼容矩阵、独立 ZIP 打包与安全的卸载/残留检查；分开报告安装结构、CLI 兼容和真实宿主运行证据。 |

## 12 项实施与验收计划

| # | 工作项 | 实施决策与交付 | 验收证据 |
| --- | --- | --- | --- |
| 01 | 现有能力审计 · P0 | 维护 workflow→capability 映射；记录重叠、Router 冲突、Eval 和门禁覆盖；标注保留/增强/合并/新增。 | 审计表可追溯到仓库路径，不把静态清单说成运行效果。 |
| 02 | `discover-testing` v2 · P0 | 保留 canonical name；默认单步路由，用户明确目标与终点时选择 Workflow；说明安装可用性证据、缺失依赖、冲突和最少澄清。 | 中英文路由、反向/边界/缺失 Skill Eval；主 Skill 唯一，辅助至多一个。 |
| 03 | Workflow 标准契约 · P0 | JSON Schema 定义 id/version/kind、输入输出、阶段、依赖、跳过与失败、权限、交接和证据引用；为工作流包提供 `workflow.yaml`。 | 所有工作流契约通过仓库校验，双语包契约一致。 |
| 04 | PR Quality Review · P0 | 新增薄编排包，组合 `code-review`、`pr-test-impact-analysis`、`test-code-review` / `ai-generated-test-review` 和质量门禁能力。 | Diff 上下文、测试义务、弱测试、分级发现、阻断项与人工审批边界进入 Eval。 |
| 05 | Requirement-to-Test · P1 | 新增需求到用例的阶段编排，复用需求质量、可测试性、测试策略、测试设计与缺口分析能力。 | 可测试性缺口、风险策略、用例与追踪矩阵、覆盖缺口均有交接字段。 |
| 06 | Change-to-Regression · P1 | 新增变更到回归编排，复用影响分析、回归范围、回归选择和 flaky 分析能力。 | 必测/可延后分层、排除依据、未覆盖风险和执行状态均可追溯。 |
| 07 | Release Readiness · P1 | 增强既有 `release-testing-workflow`，统一质量证据并保留最终批准的人类决策边界。 | 范围、证据、缺陷、剩余风险和 Go/No-Go 建议有来源；无批准记录时保持待决。 |
| 08 | 状态与恢复 · P1 | 定义 Run ID、输入指纹、Commit SHA、阶段状态、Checkpoint、幂等键、恢复和失效规则。 | 新输入或 SHA 变化使旧 Checkpoint 变为 STALE；副作用步骤不得静默重放。 |
| 09 | Evidence Contract · P0 | 定义 fact/inference/plan/execution、来源、时间、版本、范围、可信状态与有效期。 | PASS/FAIL/BLOCKED/UNKNOWN 可校验；静态分析不能作为真实测试执行通过的证据。 |
| 10 | Workflow Eval · P0 | 增加路由、交接、负向、权限、恢复、注入和有/无依赖场景；生成机器可读报告。 | 每个新工作流有正常、边界、失败/权限、回归用例；报告区分结构检查与模型执行。 |
| 11 | Skill 生命周期 · P2 | 定义 Experimental/Stable/Maintenance/Deprecated 状态、重叠复核、迁移规则、低频高风险例外和只读残留检查。 | 价值结论必须有使用证据；缺数据保持 `UNASSESSED`；弃用项有替代和迁移说明。 |
| 12 | 多 Agent 分发 · P2 | 记录 Codex、Claude Code、Cursor 安装/兼容证据；提供可选独立 ZIP、可预览卸载和旧包残留检查。 | 中文/英文独立打包和安装预览通过；测试升级、卸载与残留识别；宿主真实调用单独标记。 |

## 一次性交付顺序

1. **基线与契约**：完成审计、Router 当前行为盘点、Workflow/Evidence/Run State Schema、双语兼容矩阵和生命周期规则。
2. **P0 试点**：实现 `discover-testing` 增强及 `pr-quality-review`，接上契约验证、交接 Eval、权限与证据门禁。
3. **P1 工作流**：新增 `requirement-to-test`、`change-to-regression`，增强既有 `release-testing-workflow`，统一 Checkpoint/恢复协议。
4. **治理与交付**：更新 Skill 索引、生命周期和兼容矩阵；运行定向 Eval、安装预览、完整质量门禁并审阅 Git 差异。

## Definition of Done

- 只新增有独立价值的编排层；现有 canonical name、安装目录和专业 Skill 边界不变。
- 新增行为按 TDD：先写并观察失败测试，再实现，再整理并重跑。
- 用户可见说明与 Skill 包提供中英文版本；叶子包相对资源可独立复制。
- 每个新增或修改行为的 Skill 有正常、边界、失败/权限、回归 Eval；结构校验与实际模型运行分别记录。
- 证据包含来源、时间、版本、输入指纹和执行类型；未知事实保持 UNKNOWN/NOT_RUN。
- Schema/契约/双语/独立安装/质量脚本通过；任何未运行的宿主验证都如实列为未验证。
- 仅在用户明确要求时提交或推送；交付前核对目标分支、远端 SHA、PR 状态和工作区。

## 状态约定

本文件是执行清单。只有对应代码、Eval/验证证据和文档同步均完成后，才把任务标记为完成；文档中列出一个运行命令不等于该命令已运行。

## 当前交付状态（2026-11-03）

12 项工作在本仓库可交付范围内均已实施并完成检查：增强现有 Router 与发布工作流，新增三个薄编排 Skill，补齐标准契约、证据和 Run State 工具、双语 Evals、生命周期治理与安装交付。Run State CLI 可将阶段和 Checkpoint 写入文件，校验输入指纹、Commit SHA 与工作流包指纹，在变化时拒绝续跑，并阻止阶段静默重放；它不调度 Skill 或执行跨阶段 Host 自动化。真实 Host 自动发现、Prompt 执行及 Claude Code/Cursor 内的工作流运行仍标为 `NOT_RUN`。

最终 Codex 行为 Eval 使用 skill-up 0.12.0 与 Codex CLI 0.166.0。With-Skill 全量用例 **106/106 PASS**（每种语言 53/53）；同输入的 no-Skill 场景对照 **10/10 PASS**（每个工作流、每种语言各 1 个场景）。对照用于检查案例在有无 Skill 时的输出，不是总体效果或能力提升的统计结论。报告保留原始输出哈希、运行器版本和输入指纹：

| 工作流 | 中文 With Skill | 英文 With Skill | 中文 no-Skill | 英文 no-Skill |
| --- | --- | --- | --- | --- |
| `discover-testing` | [22/22](eval-runs/workflow-reliability-v1/runs/discover-testing-zh-20261103-final-v2.json) | [22/22](eval-runs/workflow-reliability-v1/runs/discover-testing-en-20261103-final-v2.json) | [1/1](eval-runs/workflow-reliability-v1/runs/discover-testing-zh-20261103-without-skill-v2.json) | [1/1](eval-runs/workflow-reliability-v1/runs/discover-testing-en-20261103-without-skill-v2.json) |
| `pr-quality-review` | [8/8](eval-runs/workflow-reliability-v1/runs/pr-quality-review-zh-20261103-final.json) | [8/8](eval-runs/workflow-reliability-v1/runs/pr-quality-review-en-20261103-final.json) | [1/1](eval-runs/workflow-reliability-v1/runs/pr-quality-review-zh-20261103-without-skill.json) | [1/1](eval-runs/workflow-reliability-v1/runs/pr-quality-review-en-20261103-without-skill.json) |
| `requirement-to-test` | [8/8](eval-runs/workflow-reliability-v1/runs/requirement-to-test-zh-20261103-final.json) | [8/8](eval-runs/workflow-reliability-v1/runs/requirement-to-test-en-20261103-final.json) | [1/1](eval-runs/workflow-reliability-v1/runs/requirement-to-test-zh-20261103-without-skill.json) | [1/1](eval-runs/workflow-reliability-v1/runs/requirement-to-test-en-20261103-without-skill.json) |
| `change-to-regression` | [8/8](eval-runs/workflow-reliability-v1/runs/change-to-regression-zh-20261103-final.json) | [8/8](eval-runs/workflow-reliability-v1/runs/change-to-regression-en-20261103-final.json) | [1/1](eval-runs/workflow-reliability-v1/runs/change-to-regression-zh-20261103-without-skill.json) | [1/1](eval-runs/workflow-reliability-v1/runs/change-to-regression-en-20261103-without-skill.json) |
| `release-testing-workflow` | [7/7](eval-runs/workflow-reliability-v1/runs/release-testing-workflow-zh-20261103-final.json) | [7/7](eval-runs/workflow-reliability-v1/runs/release-testing-workflow-en-20261103-final.json) | [1/1](eval-runs/workflow-reliability-v1/runs/release-testing-workflow-zh-20261103-without-skill.json) | [1/1](eval-runs/workflow-reliability-v1/runs/release-testing-workflow-en-20261103-without-skill.json) |

本轮修正了两处 Eval 误报：PR 对照不再把固定标题当作语义要求；Router 澄清评分器接受英文复数 `behaviors` 和中文“用户流程”。两处均先添加失败回归测试，再调整断言/匹配。最终中英文完整 Eval 各 **22/22 PASS**，Router no-Skill 对照各 **1/1 PASS**；表格链接只保留当前包版本的最终运行证据。其他工作流结果如表所示。

### PR #43 审查后续验证（2026-11-03）

审查修复后，对三条受影响工作流重新运行完整双语 Skill-up Evals，共 **48/48 PASS**（六次运行，每次 8/8）。这些是既有场景的后续回归，不是新增 48 个唯一场景；用例和 grader 按审查结果收紧。每条记录保留运行时 Commit、Skill 包指纹和原始报告哈希：

| 工作流 | 中文 With Skill | 英文 With Skill | 评测时 Commit |
| --- | --- | --- | --- |
| `change-to-regression` | [8/8](eval-runs/workflow-reliability-v1/runs/change-to-regression-zh-20261103-pr43-followup.json) | [8/8](eval-runs/workflow-reliability-v1/runs/change-to-regression-en-20261103-pr43-followup.json) | `306a57c0` |
| `pr-quality-review` | [8/8](eval-runs/workflow-reliability-v1/runs/pr-quality-review-zh-20261103-pr43-followup.json) | [8/8](eval-runs/workflow-reliability-v1/runs/pr-quality-review-en-20261103-pr43-followup.json) | `a7b516ab` |
| `requirement-to-test` | [8/8](eval-runs/workflow-reliability-v1/runs/requirement-to-test-zh-20261103-pr43-followup.json) | [8/8](eval-runs/workflow-reliability-v1/runs/requirement-to-test-en-20261103-pr43-followup.json) | `4495dee7` |

后续修复强化了 Change-to-Regression 的 SHA 摘要、Skill 可用性状态和生产/数据清理权限边界；修正 PR stale-checkpoint grader 对“重新运行”的漏判；并为双语 Requirement-to-Test 对照明确输出语言、章节与需求追踪要求。模型响应与规则断言分开记录，评测器修复不作为 Skill 行为通过证据。

最终质量门禁结果：Workflow Contract 校验 **14 个包、28 个 Workflow 文件、0 错误**；`skill-up validate` **348/348**；中英文文档检查 **0 findings**；最新完整质量脚本中的 Python 单元测试 **407/407 PASS**。源码 `skills@1.7.0` 兼容门禁发现 **169 个 Skill**，English `functional-testing` 隔离安装 smoke 通过。Agent 分发复核完成 **60 次**双语隔离安装、**10 次**同目标升级、**10 次**卸载预览/实际删除与零残留扫描、**10 个**独立 ZIP 逐文件校验，失败 **0**；详见[兼容验证记录](../integrations/agent-compatibility-evidence-2026-11-03.json)。

这些证据只证明仓库契约、Codex CLI 用例及隔离安装流程达到所列范围；不证明 Claude Code/Cursor Host 内加载与执行，也不提供持续运行的跨阶段调度器。最终发布决定仍由人工承担。

本次审查修复已提交并推送到 PR #43 分支；PR 仍为开放、未合并状态。交付时工作区保持干净。

## 变更记录

- **2026-10-30 · v1.0.0**：建立双语 Workflow、Evidence 与 Run State 契约；增强 Router；增加 PR 质量、需求到测试、变更到回归三个编排包；扩展现有发布工作流；加入 Eval、生命周期、安装包和质量门禁记录。
- **2026-11-03 · v1.0 收尾**：完成双语 Router 最终行为 Eval、no-Skill 对照和澄清评分器回归修复；复核仓库质量门禁、CLI 兼容、隔离安装、升级/卸载及独立 ZIP 证据，保留 Host 内运行与自动调度为 `NOT_RUN`。
