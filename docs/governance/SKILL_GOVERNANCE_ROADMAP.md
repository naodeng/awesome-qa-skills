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

`IN_PROGRESS`：registry 已覆盖 79 个逻辑双语 Skill 对，Matrix/Register 已可由生成器复现，13 个候选已登记为 `PROPOSED`。候选源材料与六项 Capability Match 证据仍未完成，因此本阶段不能标记为 `verified` 或进入新增 Skill 实施；Quality Score 与 Eval 执行状态继续保持 `NOT_SCORED` / `NOT_RUN`。

## 阶段复盘

每期执行 Coverage、Duplicate、Match、Merge、Enhancement、Eval、Usage 与 Maintenance Review；Review 结论区分已验证、失败、未运行、阻塞和不适用，不能把静态检查写成运行效果。
