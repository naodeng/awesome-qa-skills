<div align="right"><a href="./2026-08-29-bilingual-lifecycle-navigation-design.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Bilingual Lifecycle Navigation Design

## Decision Summary

The project keeps its stable physical directories and adds two logical navigation layers:

```text
Capability evolution: Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
R&D and testing lifecycle: Discovery → Design → Development → Test Preparation → Test Execution → Release → Production → Improvement
```

The README, roadmap, indexes, and language entry points use the same mapping. Chinese is the default entry point, while every maintained project document provides an English mirror and two-way language switching.

## Goals

- Present all 78 Skills per language in the root README instead of only the former 36 testing types.
- Navigate first by the four capability stages, then by R&D and testing lifecycle phase.
- Give each Skill one primary home and represent cross-stage relationships only as secondary labels.
- Apply enforceable bilingual rules to root documents, `docs/`, language indexes, and Skill mirrors.
- Preserve every Skill directory, installation path, and name.

## Navigation Model

### Layer 1: Capability Evolution

1. **Core QA Skills** establishes the foundation across requirements, strategy, cases, execution, defects, and reporting.
2. **Engineering QA Skills** shifts quality into requirements, code, contracts, regression decisions, and performance engineering.
3. **Production Quality Skills** supports evidence-based release and production quality decisions.
4. **AI Native QA Skills** validates AI features, LLMs, prompts, agents, tool calls, and safety boundaries.

`skill-engineering` remains a cross-cutting governance layer. Workflows remain the orchestration layer across lifecycle phases. Neither becomes a fifth capability stage.

### Layer 2: R&D and Testing Lifecycle

Each capability stage uses only the lifecycle phases that contain real Skills; empty stage-phase combinations are not rendered:

1. Discovery and Requirements Analysis
2. Solution Design and Test Strategy
3. Development and Continuous Integration
4. Test Design and Preparation
5. Test Execution and Analysis
6. Release and Delivery
7. Production Operations and Incident Response
8. Retrospective and Continuous Improvement

### Primary Placement Rules

- Determine one primary placement from the Skill's main input, core decision, and primary deliverable.
- Tool-specific Skills follow the testing activity they enable instead of becoming a fifth capability stage.
- Plus variants follow their base Skill and are marked as enhanced variants.
- `ai-assisted-testing` is cross-cutting AI for QA. Place it under Engineering QA test-execution support and distinguish it from Testing for AI.
- `root-cause-analysis` belongs primarily to Engineering QA continuous improvement. Production incident guidance may route to it without listing it twice.

## README Information Architecture

Chinese `README.md` is the default entry point and English `README_EN.md` is its complete mirror. Both use this order:

1. Language switch, positioning, and accurate counts
2. Four-stage evolution map and usage guidance
3. Workflows and how they orchestrate lifecycle phases
4. Four capability stages, each divided by applicable lifecycle phase
5. Cross-cutting Skill Engineering governance
6. Installation, repository layout, quality gates, and contribution links

Each Skill table includes at least name, directory, and usage. Counts must resolve to 78 Skills per language and 156 bilingual directories, with each Skill appearing once in its primary classification.

## Bilingual Documentation Rules

### Root and `docs/`

- Chinese primary document: `NAME.md`
- English mirror: `NAME_EN.md`
- Both documents provide a relative two-way language switch at the top.
- README files, contribution guides, FAQs, indexes, roadmaps, directory guides, authoring standards, style guides, audit reports, designs, and implementation plans are in scope.

### Skill Documents

- `skills/zh/` and `skills/en/` use identical relative paths for language mirrors.
- Do not add `_EN` files inside a Skill; language switches link to the corresponding file under the other language directory.
- Mirror maintained Markdown that exists in only one language. Language-specific examples may remain when the Skill entry clearly states their language scope.

### Explicit Exclusions

- Historical compatibility content under `legacy-prompts/`
- External snapshots and generated artifacts
- Third-party license text
- `.git`, evaluation outputs, and temporary workspaces

These files do not require file-by-file translation, but maintained documentation must state their language status or official replacement entry.

## Automated Validation

Add a documentation parity check to the main quality gate. It verifies at least:

- Every Chinese primary document has an `_EN` mirror and vice versa.
- Both documents contain valid two-way language links.
- Maintained Markdown under `skills/zh` and `skills/en` has matching relative paths.
- README primary classifications contain every Skill exactly once and match actual directory counts.
- Markdown relative links have no obvious broken targets.

## Acceptance Criteria

- All 65 testing-type Skills appear in the README under the four-stage capability model and a lifecycle phase.
- The 10 workflows and 3 Skill Engineering packages have clear cross-cutting placement.
- Chinese remains the GitHub default entry, and every core maintained document can switch to English and back in one click.
- The roadmap, full index, and language indexes use the same classification vocabulary as the root README.
- The bilingual parity check and `bash scripts/check_skills_quality.sh` both pass.
- No directories move, installation paths remain valid, and unrelated worktree changes stay outside the task.
