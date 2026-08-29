<div align="right"><strong>🇨🇳 中文</strong> | <a href="./DIRECTORY_GUIDE_EN.md">🇬🇧 English</a></div>

# Skills 目录指南

本仓库使用一个 `skills` 根目录，并按中文/英文与测试类型、测试工作流、Skill Engineering 分类。物理目录是稳定安装契约，不随以下逻辑能力层变化：

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

- `testing-types` 承载具体质量能力。
- `testing-workflows` 负责跨研发测试阶段编排。
- `skill-engineering` 负责 Skill 编写与仓库治理。
- 新增 Skill 前必须确认其输入、主要产物和路由触发条件均有独立边界，否则应作为现有 Skill 的模式。

完整结构、维护命令和质量检查见下方英文技术说明；中文编写规范见 [SKILL_AUTHORING.md](SKILL_AUTHORING.md)。

## English Technical Reference

# Skills Directory Guide

Current structure uses one skills root with language partitions:

- `skills/zh/testing-types`
- `skills/zh/testing-workflows`
- `skills/zh/skill-engineering`
- `skills/en/testing-types`
- `skills/en/testing-workflows`
- `skills/en/skill-engineering`

## Physical layout and logical capability stages

The physical package families above are stable installation contracts. Do not create a new top-level directory for a capability stage, and do not move an existing Skill merely to reflect product positioning.

The repository uses this logical navigation model in documentation and routing:

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

- `testing-types` normally contains Shift Left, Change Intelligence, Execution Intelligence, Performance, Production Quality, and AI Native QA deliverables.
- `testing-workflows` owns cross-stage orchestration, calendar cadence, gates, and handoffs.
- `skill-engineering` owns Skill authoring and repository governance.
- Before creating a directory, check the [evolution roadmap](../docs/QA_SKILLS_EVOLUTION_ROADMAP.md) and existing Skills. A new name is justified only when it has distinct inputs, a primary output, and routing triggers; otherwise add it as a mode of the existing Skill.

Each skill directory now follows the same lightweight layout:

- `SKILL.md`: short activation entry (workflow, constraints, progressive disclosure, pre-delivery checklist)
- `prompts/`: full execution spec (required)
- `evals/`: optional skill-up eval suite (`eval.yaml` + `cases/`)
- `reference.md`: workflow mapping when needed
- `output-formats.md`: optional format guidance when supported
- `references/`: deeper notes loaded only when needed
- `examples/`: sample inputs or outputs when useful
- `scripts/`: helper tooling when needed

Authoring / evaluation conventions: [SKILL_AUTHORING.md](SKILL_AUTHORING.md)（对齐 [alibaba/skill-up](https://github.com/alibaba/skill-up)）。

Maintenance:

```bash
python3 scripts/organize_project_dirs.py
```

Quality check:

```bash
bash scripts/check_skills_quality.sh
```
