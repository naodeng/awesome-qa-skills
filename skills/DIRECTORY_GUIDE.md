# Skills Directory Guide

Current structure uses one skills root with language partitions:

- `skills/zh/testing-types`
- `skills/zh/testing-workflows`
- `skills/en/testing-types`
- `skills/en/testing-workflows`

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
