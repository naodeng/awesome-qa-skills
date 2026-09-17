<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_GOVERNANCE_ROADMAP_EN.md">🇬🇧 English</a></div>

# Skill 治理与长期路线图

> 本文是后续治理的上下文入口。既有 `QA_SKILLS_EVOLUTION_ROADMAP.md` 保留已完成版本的历史记录；两者不互相覆盖。

## 治理原则

坚持“先匹配，后增强；先合并，后新增”。稳定物理目录负责兼容性；虚拟 Domain、Matrix、metadata、Workflow 和文档负责发现与治理。

## 执行顺序

1. Phase 0：Inventory、16 个虚拟 Domain、Matching、Lifecycle、Quality Score、最低 Eval 与矩阵。
2. Phase 1：Shift-Left Quality，候选项先通过 Match 后再决定 New/Enhance/Merge。
3. Phase 2：Test Engineering，分离测试方法论与框架/工具 Adapter。
4. Phase 3：Reliability、安全、QE 效能与 AI Native Quality，并复核 Performance 和 AI 既有能力。

## Project 与文档同步

GitHub Project `Awesome QA Skills — Governance & Roadmap` 是执行看板。每张卡必须含目标、范围、非目标、依赖、交付物、验收与关联文档；卡片状态不等同于发布或风险接受。

每次状态变化同步检查：`SKILL_MATRIX.md`、中英文入口 README、Catalog/Graph、Workflow、Eval、`agents/openai.yaml`、安装与贡献文档。未适用项显式标记 `N/A`。

## Phase 0 当前状态（2026-09-16）

`COMPLETED_WITH_LIMITATIONS`：registry 当前逐条覆盖 162 个逻辑双语 Skill 对；每条保留中英文 `SKILL.md`、主 prompt、Eval 结构和 `agents/openai.yaml` 的证据路径，D01–D16 分类源以及 Matrix/Register 均由生成器复现并受质量门禁检查。当前登记 100 个候选条目，每条保留六项证据字段；其中 Phase 0 Prompt Baseline 继续固定在 `554178fe9b93d851ec01388597ceb7996d22bd1c` 的 `awesome-qa-prompt` 提交（详见 [Phase 0 来源登记](./PHASE_0_PROMPT_BASELINE_SOURCES.md)）。候选结论保留 `MATCH` / `MERGE` / `ENHANCE` / `NEW`，`decision_state` 按阶段保留 `REVIEWED_WITH_LIMITATION` / `REVIEWED` / `PROPOSED`；业务语义等价仍需项目需求、Issue/PR 或测试资产复核，不得据此直接创建或修改 Skill。Phase 0 未执行模型、外部测试目标或真实质量评估，因此 Quality Score / Eval 执行仍为 `NOT_SCORED` / `NOT_RUN`；Prompt 语义等价、运行行为与有效性继续为 `UNASSESSED`。

典型映射复核（2026-09-16）已将 20 条路线图关系写入 Registry 的 `match_reviews`，包括 13 条候选映射和 7 条 Existing 自映射；[双语复核视图](./PHASE_0_MATCH_MERGE_REVIEW.md)与 Matrix/Matching Register 均由生成器产生。该复核只固化关系、目标 Skill、证据路径和后续动作，不授权创建重复目录，也不把静态关系记录升级为语义等价、运行效果、模型评测或发布批准。

v1.4 的 35 张 Project 卡由 [Phase 0 收口视图](./PHASE_0_V1_4_CLOSEOUT.md)统一登记；[Deprecation 契约](./DEPRECATION_DECISION_CONTRACT.md)、[双语一致性契约](./BILINGUAL_CONSISTENCY_CONTRACT.md)、[Quality Score/Eval 契约](./QUALITY_SCORE_EVAL_CONTRACT.md)、[Workflow/Eval/安装同步清单](./WORKFLOW_EVAL_INSTALL_SYNC.md)、[Enhancement Sprint](./ENHANCEMENT_SPRINT.md)、[15 步模板](./CANDIDATE_SKILL_15_STEP_TEMPLATE.md)和 [Shift Left 里程碑](./SHIFT_LEFT_MILESTONE.md)分别保留可执行规则。v1.5–v1.8 仍按版本规划排队，不在本收口中提前执行。

## Phase 1 当前工作项（2026-09-14）

`ACCEPTED_WITH_DEFERRED_EVAL`：v1.1 第一批五个需求质量 Skill、后续十个质量 Skill 卡片和本批五个测试设计发现 Skill 已完成统一实现范围验收；对应 20 张 Project #4 卡片移至 `Done`。范围、卡片 ID、输入审计约束、证据边界和验收命令见 [Phase 1 需求质量记录](./PHASE_1_REQUIREMENTS_QUALITY.md)。真实模型 Eval 按用户决定延期并保持 `NOT_RUN`，因此不能据此宣称语义效果、质量评分或版本发布完成。

## Phase 3 当前工作项（2026-09-15）

`ACCEPTED_WITH_DEFERRED_EVAL`：v3-v4 Phase 3 的 Batch 1（Reliability + Security）17 张卡片和 Batch 2（Quality Engineering + AI Native）25 张卡片，其 Match、RED 契约、Skill 实现、治理同步和质量门禁交付物均已完成；Project 当前快照显示 42 张卡片为 `Done`。现有 Project 查询不能证明历史上完整经历过 `In Progress → Done`，因此 transition audit 保持 `UNASSESSED`。Batch 2 交付 24 个双语物理 Skill 包，并将 `prompt-regression-testing` 作为 `prompt-testing` 的增强模式，不创建别名目录。真实模型 Eval、外部目标执行、质量分数和业务验收继续保持 `NOT_RUN` / `NOT_SCORED` / `INCOMPLETE`。详见 [v3-v4 Phase 3 记录](./PHASE_3_V3_V4.md)。

## 阶段复盘

每期执行 Coverage、Duplicate、Match、Merge、Enhancement、Eval、Usage 与 Maintenance Review；Review 结论区分已验证、失败、未运行、阻塞和不适用，不能把静态检查写成运行效果。
