<div align="right"><a href="./DIRECTORY_GUIDE.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Skills Directory Guide

The repository uses one skills root with language partitions:

- `skills/zh/testing-types`
- `skills/zh/testing-workflows`
- `skills/zh/skill-engineering`
- `skills/en/testing-types`
- `skills/en/testing-workflows`
- `skills/en/skill-engineering`

## Physical Layout and Logical Capability Stages

The physical package families above are stable installation contracts. Do not create a new top-level directory for a capability stage or move a Skill merely to reflect product positioning.

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

- `testing-types` contains concrete quality deliverables.
- `testing-workflows` owns cross-phase orchestration, cadence, gates, and handoffs.
- `skill-engineering` owns Skill authoring and repository governance.
- Before creating a directory, inspect the [evolution roadmap](../docs/governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md). Add a Skill only when its input, primary output, and routing triggers are independently bounded.

## Per-Skill Layout

- `SKILL.md`: lightweight activation entry.
- `prompts/`: complete execution specification.
- `agents/openai.yaml`: OpenAI / Codex metadata.
- `evals/`: skill-up suite with `eval.yaml` and `cases/`.
- `reference.md`, `output-formats.md`, `references/`, `examples/`, and `scripts/`: optional support material.

See [SKILL_AUTHORING_EN.md](SKILL_AUTHORING_EN.md) for authoring conventions.

```bash
python3 scripts/organize_project_dirs.py
bash scripts/check_skills_quality.sh
```
