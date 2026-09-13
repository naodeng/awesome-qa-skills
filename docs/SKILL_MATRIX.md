<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_MATRIX_EN.md">🇬🇧 English</a></div>

# Skill 治理矩阵

本矩阵的权威数据源是 [Skill Inventory](generated/skill-inventory.md)：该快照基于当前 158 个实际目录生成，记录可验证的语言与物理分类。每一行至少包含：Skill、中文名、英文名、物理分类、虚拟 Domain、SDLC 阶段、角色、状态、优先级、输入、输出、关联 Skill、Workflow、Match With、Merge Into、Enhance Reason、Deprecation Target 和 Quality Score。

## 虚拟 Domain

| ID | Domain | 中文 |
| --- | --- | --- |
| D01 | Requirement Quality | 需求质量 |
| D02 | Engineering Quality | 工程质量 |
| D03 | Test Analysis & Strategy | 测试分析与策略 |
| D04 | Test Design | 测试设计 |
| D05 | Functional & Exploratory Testing | 功能与探索式测试 |
| D06 | API & Integration Quality | API 与集成质量 |
| D07 | UI & E2E Quality | UI 与端到端质量 |
| D08 | Automation Engineering | 自动化工程 |
| D09 | Performance Quality | 性能质量 |
| D10 | Security Quality | 安全质量 |
| D11 | Reliability & Resilience | 可靠性与韧性 |
| D12 | Release & Production Quality | 发布与生产质量 |
| D13 | Observability & Incident Quality | 可观测性与事故质量 |
| D14 | Quality Engineering & Productivity | QE 与效能 |
| D15 | AI for QA | AI 辅助 QA |
| D16 | AI / LLM / Agent Quality | AI 系统质量 |

## 状态词典

`Existing`、`Enhance`、`Merge`、`Match`、`Planned-P0`、`Planned-P1`、`Planned-P2`、`Experimental`、`Deprecated`、`Archived`。状态含义与转换规则以 `SKILL_LIFECYCLE.md` 为准。

能力匹配以 `SKILL_MATCHING_GUIDE.md` 和 `SKILL_MATCHING_REGISTER.md` 为准；质量评分与最低 Eval 以 `SKILL_QUALITY_GATE.md` 为准；弃用路径以 `SKILL_DEPRECATION_GUIDE.md` 为准。

在数据生成前，不以本文件的空表推断覆盖率或质量结论。候选项先记录为 Candidate/Planned，只有 Capability Match 结论为 `NEW` 才创建目录。

| Skill | Virtual Domain | Status | Match evidence | Next action |
| --- | --- | --- | --- | --- |
| _158 physical directories inventoried_ | _pending_ | Candidate | filesystem snapshot | Complete capability classification |
