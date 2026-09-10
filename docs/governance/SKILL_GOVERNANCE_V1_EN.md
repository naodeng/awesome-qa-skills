<div align="right"><a href="./SKILL_GOVERNANCE_V1.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.0 Skill Governance Baseline

## Purpose and boundary

v1.0 establishes a reproducible **source-governance record** for the repository's current 79 bilingual Skill pairs. It reviews only package directories and declarations in `SKILL.md`, `agents/openai.yaml`, and `evals/`; it does not run Skill prompts, helper scripts, models, or real test targets.

The baseline therefore provides no Quality Score and never presents a static record as runtime effectiveness, test pass rate, or capability-quality conclusion. Runtime behavior, semantic equivalence, model evaluation, and effectiveness are `UNASSESSED` when matching execution evidence is unavailable.

## Field contract

| Field | Meaning | Allowed conclusion boundary |
| --- | --- | --- |
| Virtual Domain | Logical classification from the current directory layout and full catalog. | Navigation classification, not an installation dependency or execution order. |
| Status | `STRUCTURALLY_RECORDED` means this script found both packages, declared metadata, and Eval file structure; a gap is `UNASSESSED (structural gap)`. | Not a functional, quality, or execution-success status. |
| Scope boundary | Preserves the source description per package and states what static review excludes. | Does not infer unexecuted capability from a description. |
| Similar/Plus relation | Records only explicit Plus variants, named tool families, or an unassessed semantic relation. | Naming is not proof of semantic equivalence. |
| Eval structure | `eval.yaml`, actual case count, and case count declared by the configuration. | File-structure evidence only; it does not mean an Eval ran or passed. |
| Capability Match evidence | Traceable paths for zh/en directories, frontmatter name, Agent metadata, and Eval structure. | Semantics and effectiveness remain `UNASSESSED` unless separate execution evidence exists. |

## Reproducible inventory

- [Per-package governance inventory](../generated/skill-governance-inventory_EN.md): one record for each of 79 logical bilingual Skill pairs.
- Generate: `python3 scripts/generate_skill_governance_inventory.py`
- Freshness check: `python3 scripts/generate_skill_governance_inventory.py --check`

The generator uses the current `skills/{zh,en}/{testing-workflows,testing-types,skill-engineering}` directories and maps testing-type Virtual Domains from headings in `docs/catalog/skills-index.md`. Regenerate after any package addition, removal, rename, or Eval-structure change; `check_skills_quality.sh` checks for drift.

## Project Card

| Item | Status | Acceptance evidence | Explicitly excluded |
| --- | --- | --- | --- |
| v1.0 source-governance closeout | `LOCALLY_VERIFIED` | 79 per-package records, bilingual entry points, Catalog/Graph links, reproducible generator, `--check`, and the complete local quality gate | Skill/model/script execution, runtime quality scoring, release, push |

`LOCALLY_VERIFIED` means fresh evidence exists for the full quality gate, generated-artifact freshness check, and Git diff check. It still does not mean runtime effectiveness or publication.
