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

## Phase 0 当前状态（2026-09-14）

`COMPLETED_WITH_LIMITATIONS`：registry 已逐条覆盖 79 个逻辑双语 Skill 对；每条保留中英文 `SKILL.md`、主 prompt、Eval 结构和 `agents/openai.yaml` 的证据路径，Matrix/Register 由生成器复现并受质量门禁检查。13 个候选均已逐项登记六步字段，并引用固定提交 `554178fe9b93d851ec01388597ceb7996d22bd1c` 的 `awesome-qa-prompt` Prompt Baseline（详见 [Phase 0 来源登记](./PHASE_0_PROMPT_BASELINE_SOURCES.md)）。候选结论保留 `MATCH` / `MERGE` / `ENHANCE` 提议，`decision_state` 统一为 `REVIEWED_WITH_LIMITATION`；业务语义等价仍需项目需求、Issue/PR 或测试资产复核，不得据此直接创建或修改 Skill。Phase 0 未执行模型、外部测试目标或真实质量评估，因此 Quality Score / Eval 执行仍为 `NOT_SCORED` / `NOT_RUN`；Prompt 语义等价、运行行为与有效性继续为 `UNASSESSED`。

## Phase 1 当前工作项（2026-09-14）

`IN_PROGRESS_WITH_LIMITATIONS`：第一批五个 v1.1 P0 需求质量 Skill 已完成中英文包和包级结构检查，Project #4 对应卡片保持 `In Progress`。范围、卡片 ID、输入审计约束、证据边界和验收命令见 [Phase 1 需求质量记录](./PHASE_1_REQUIREMENTS_QUALITY.md)；真实模型 Eval 尚未运行，不能据此宣称语义效果或发布完成。

## 阶段复盘

每期执行 Coverage、Duplicate、Match、Merge、Enhancement、Eval、Usage 与 Maintenance Review；Review 结论区分已验证、失败、未运行、阻塞和不适用，不能把静态检查写成运行效果。
