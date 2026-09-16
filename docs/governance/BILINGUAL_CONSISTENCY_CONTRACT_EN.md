<div align="right"><a href="./BILINGUAL_CONSISTENCY_CONTRACT.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Bilingual Consistency Quality Contract

This contract defines structural consistency for current project documents and Skill packages. It checks reproducible paths, entry points, and links; it does not treat textual similarity as semantic equivalence or prove runtime effectiveness.

## Consistency requirements

| Scope | Contract |
| --- | --- |
| Project docs | `NAME.md` and `NAME_EN.md` exist as a pair and expose reciprocal language switches at the top |
| Skill directories | `skills/zh` and `skills/en` use the same physical slugs and maintained-file structure |
| Skill content | `SKILL.md`, primary Prompt, README, quick-start, tutorial, output-formats, reference, and Workflow references mirror by relative path |
| Catalog | Chinese and English indexes list the same Skills; root README `data-skill` markers are unique, complete, and known |
| Generated views | Matrix, Inventory, Register, and similar views are rebuilt from sources; generated output need not be translated file-by-file but must have bilingual entry points |
| Links | Relative links in current entry points resolve; cross-Skill navigation does not link into another Skill's internal files |

## Current coverage

- Each language has 162 Skill packages, for 324 physical directories in total.
- All 10 current `testing-workflows` packages appear individually in the bilingual installation/Eval checklist.
- Generated governance views are determined by the Registry, Virtual Domain manifest, and generators; every source change requires regeneration and `--check`.

## Quality gate

```bash
python3 scripts/check_docs_bilingual.py --repo-root .
python3 scripts/generate_skill_governance_inventory.py --check
python3 scripts/generate_skill_governance_matrix.py --check
bash scripts/check_skills_quality.sh
```

A passing check proves reproducible structure, mirrors, and links only. Semantic behavior, model Eval, runtime, and release state remain `UNASSESSED`, `NOT_RUN`, or `N/A` as appropriate.

## Navigation

- [Bilingual documentation policy](./DOCUMENTATION_POLICY_EN.md)
- [Workflow/Eval installation synchronization](./WORKFLOW_EVAL_INSTALL_SYNC_EN.md)
- [v1.4 closeout](./PHASE_0_V1_4_CLOSEOUT_EN.md)
