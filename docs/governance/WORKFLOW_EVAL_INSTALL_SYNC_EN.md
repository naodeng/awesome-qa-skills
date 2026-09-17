<div align="right"><a href="./WORKFLOW_EVAL_INSTALL_SYNC.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Workflow / Eval / Installation Synchronization Checklist

This checklist keeps the physical paths, bilingual packages, minimum Eval artifacts, and installation entry points for the 10 current cross-phase Workflows together. It is documentation and structural evidence, not proof that a Workflow ran in a real project.

## 10 Workflows

| Workflow | Chinese path | English path | Eval structure |
| --- | --- | --- | --- |
| `daily-testing-workflow` | `skills/zh/testing-workflows/daily-testing-workflow` | `skills/en/testing-workflows/daily-testing-workflow` | `eval.yaml` + three case classes |
| `discover-testing` | `skills/zh/testing-workflows/discover-testing` | `skills/en/testing-workflows/discover-testing` | `eval.yaml` + three case classes |
| `multi-role-quality-synthesis` | `skills/zh/testing-workflows/multi-role-quality-synthesis` | `skills/en/testing-workflows/multi-role-quality-synthesis` | `eval.yaml` + three case classes |
| `product-quality-perspective` | `skills/zh/testing-workflows/product-quality-perspective` | `skills/en/testing-workflows/product-quality-perspective` | `eval.yaml` + three case classes |
| `project-delivery-perspective` | `skills/zh/testing-workflows/project-delivery-perspective` | `skills/en/testing-workflows/project-delivery-perspective` | `eval.yaml` + three case classes |
| `qa-quality-perspective` | `skills/zh/testing-workflows/qa-quality-perspective` | `skills/en/testing-workflows/qa-quality-perspective` | `eval.yaml` + three case classes |
| `release-testing-workflow` | `skills/zh/testing-workflows/release-testing-workflow` | `skills/en/testing-workflows/release-testing-workflow` | `eval.yaml` + three case classes |
| `sprint-testing-workflow` | `skills/zh/testing-workflows/sprint-testing-workflow` | `skills/en/testing-workflows/sprint-testing-workflow` | `eval.yaml` + three case classes |
| `technical-quality-perspective` | `skills/zh/testing-workflows/technical-quality-perspective` | `skills/en/testing-workflows/technical-quality-perspective` | `eval.yaml` + three case classes |
| `ux-quality-perspective` | `skills/zh/testing-workflows/ux-quality-perspective` | `skills/en/testing-workflows/ux-quality-perspective` | `eval.yaml` + three case classes |

## Installation entry points

```bash
# macOS / Linux
bash scripts/install-skills-mac.sh --tool codex --lang zh
bash scripts/install-skills-mac.sh --tool codex --lang en --dry-run

# Windows
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool codex -Lang zh

# npx skills
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/en/testing-workflows/discover-testing -g -a codex -y
```

`--lang zh|en|all` selects the source language and `--skill` uses the physical slug. Install Chinese and English same-named packages separately to avoid overwriting each other. The root installers, Windows script, and per-Skill shortcuts are documented in the [installation guide](../../scripts/INSTALL_SKILLS.md).

## Acceptance

- Bilingual directories, `SKILL.md`, `agents/openai.yaml`, `evals/eval.yaml`, and three case classes exist.
- Installer dry-runs parse language, tool, and Skill parameters; real installation and execution still require user-environment verification.
- Run `check_docs_bilingual.py`, `validate_skill_evals.sh`, and the full quality gate.

## Navigation

- [Quality Score and minimum Eval contract](./QUALITY_SCORE_EVAL_CONTRACT_EN.md)
- [Bilingual consistency contract](./BILINGUAL_CONSISTENCY_CONTRACT_EN.md)
- [v1.4 closeout](./PHASE_0_V1_4_CLOSEOUT_EN.md)
