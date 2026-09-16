<div align="right"><a href="./SKILL_GOVERNANCE_V1.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# v1.0 Skill Governance Baseline

## Purpose and boundary

v1.0 establishes a reproducible **source-governance record** for the repository's current 162 logical bilingual Skill pairs. The earlier baseline covered 79 logical pairs; the current tree also includes the later v1.1, v2.0, and v3-v4 deliveries, so the generator is the current count authority. It reviews only package directories and declarations in `SKILL.md`, `agents/openai.yaml`, and `evals/`; it does not run Skill prompts, helper scripts, models, or real test targets.

The baseline therefore provides no Quality Score and never presents a static record as runtime effectiveness, test pass rate, or capability-quality conclusion. Runtime behavior, semantic equivalence, model evaluation, and effectiveness are `UNASSESSED` when matching execution evidence is unavailable.

## Field contract

| Field | Meaning | Allowed conclusion boundary |
| --- | --- | --- |
| Virtual Domain | Assigns one primary Domain to each logical Skill using the [D01–D16 source](./virtual-domains.yaml). | Navigation classification, not an installation dependency, execution order, semantic-equivalence proof, or quality conclusion. |
| Status | `STRUCTURALLY_RECORDED` means this script found both packages, declared metadata, and Eval file structure; a gap is `UNASSESSED (structural gap)`. | Not a functional, quality, or execution-success status. |
| Scope boundary | Preserves the source description per package and states what static review excludes. | Does not infer unexecuted capability from a description. |
| Similar/Plus relation | Records only explicit Plus variants, named tool families, or an unassessed semantic relation. | Naming is not proof of semantic equivalence. |
| Match/Merge review | `match_reviews` records typical relationships, target Skills, evidence paths, and follow-up actions. | The relationship review remains `REVIEWED_WITH_LIMITATION`; it does not authorize directory creation, modification, or deletion. |
| Eval structure | `eval.yaml`, actual case count, and case count declared by the configuration. | File-structure evidence only; it does not mean an Eval ran or passed. |
| Capability Match evidence | Traceable paths for zh/en directories, frontmatter name, Agent metadata, and Eval structure. | Semantics and effectiveness remain `UNASSESSED` unless separate execution evidence exists. |

## D01–D16 Virtual Domains

| ID | English | 中文 |
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
| D16 | AI / LLM / Agent Quality | AI / LLM / Agent 质量 |

Each Skill has one primary Domain. Mixed catalog groups use explicit slug overrides; a new unmapped directory must be added to the taxonomy source before it can pass validation.

## Reproducible inventory

- [Per-package governance inventory](../generated/skill-governance-inventory_EN.md): one record for each of 162 logical bilingual Skill pairs.
- [Governance Matrix](../SKILL_MATRIX_EN.md): displays D01–D16 labels, priority, and evidence boundaries.
- [Typical Match/Merge review](./PHASE_0_MATCH_MERGE_REVIEW_EN.md): displays the 20 Registry relationships and follow-up actions.
- [v1.4 Phase 0 closeout](./PHASE_0_V1_4_CLOSEOUT_EN.md): records evidence, acceptance states, and version boundaries for 35 Project cards.
- [Taxonomy source](./virtual-domains.yaml): Domain definitions, section defaults, and slug overrides.
- Generate: `python3 scripts/generate_skill_governance_inventory.py`
- Freshness check: `python3 scripts/generate_skill_governance_inventory.py --check`
- Matrix generation and check: `python3 scripts/generate_skill_governance_matrix.py --check`

The generator uses the current `skills/{zh,en}/{testing-workflows,testing-types,skill-engineering}` directories and reuses the taxonomy source to resolve catalog headings and slug overrides. Regenerate after any package addition, removal, rename, or Eval-structure change; missing Domain mappings and generated-file drift fail the quality gate.

## Project Card

| Item | Status | Acceptance evidence | Explicitly excluded |
| --- | --- | --- | --- |
| v1.0 source-governance closeout | `LOCALLY_VERIFIED` | 162 current per-package records, D01–D16 taxonomy source, bilingual entry points, Catalog/Graph links, reproducible generator, `--check`, and the complete local quality gate | Skill/model/script execution, runtime quality scoring, release, push |

`LOCALLY_VERIFIED` means fresh evidence exists for the full quality gate, generated-artifact freshness check, and Git diff check. It still does not mean runtime effectiveness or publication.
