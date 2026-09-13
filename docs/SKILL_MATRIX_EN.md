<div align="right"><a href="./SKILL_MATRIX.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Governance Matrix

The authoritative source is the [Skill Inventory](generated/skill-inventory.md): a snapshot generated from the current 158 physical directories that records verifiable languages and physical categories. Each row includes Skill, bilingual names, physical category, virtual Domain, SDLC phase, role, status, priority, inputs, outputs, related Skills, Workflow, Match With, Merge Into, Enhance Reason, Deprecation Target, and Quality Score.

## Virtual Domains

| ID | Domain | Chinese |
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

## Status vocabulary

`Existing`, `Enhance`, `Merge`, `Match`, `Planned-P0`, `Planned-P1`, `Planned-P2`, `Experimental`, `Deprecated`, and `Archived`. `SKILL_LIFECYCLE.md` defines their meaning and transitions.

Use `SKILL_MATCHING_GUIDE.md` and `SKILL_MATCHING_REGISTER.md` for matching, `SKILL_QUALITY_GATE.md` for scoring and minimum Evals, and `SKILL_DEPRECATION_GUIDE.md` for replacement paths.

Until the inventory is generated, this file must not be used to infer coverage or quality. Candidates remain Candidate/Planned; a directory is created only after a `NEW` match decision.

| Skill | Virtual Domain | Status | Match evidence | Next action |
| --- | --- | --- | --- | --- |
| _158 physical directories inventoried_ | _pending_ | Candidate | filesystem snapshot | Complete capability classification |
