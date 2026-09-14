<div align="right"><a href="./2026-09-14-v1-1-requirements-quality-skills-design.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# v1.1 First Five Requirement-Quality Skills Design

## Goal

Start the first five v1.1 P0 candidate Skills in Project #4 on the baseline where `develop` is synchronized with remote `main`:

1. `requirement-quality-review`
2. `requirement-ambiguity-analysis`
3. `requirement-consistency-analysis`
4. `requirement-conflict-detection`
5. `requirement-traceability-analysis`

Each Skill must be an independently copyable bilingual package. It must produce a bounded first draft when requirements, acceptance criteria, change notes, or evidence are incomplete. It must not present inference, recommendations, mappings, or static checks as executed tests, approved decisions, or release conclusions.

## Baseline and Scope

- Code baseline: `develop` was fast-forwarded to remote `main` at `afe51cd`.
- The five Project #4 cards are `In Progress`; that status represents development activity, not release or risk acceptance.
- Existing `requirements-analysis` covers general requirement understanding, test points, boundaries, dependencies, and risks. `requirements-analysis-plus` covers multi-format, multi-source synthesis.
- The new Skills handle narrow, reviewable concerns. They do not copy the full workflow of an existing composite Skill or read another Skill's internal files.
- `awesome-qa-prompt` contains a reference baseline for `requirement-traceability-analysis`. The other four have no same-named baseline in the local checkout, so they will be designed from the repository's requirement-analysis constraints and the Project card boundaries rather than copied from an external directory layout.

## Capability Match Boundary

All five candidates are implemented in the `NEW` direction but recorded as `PROPOSED`, because the current evidence can establish package, Prompt, and navigation boundaries only; it cannot establish business semantic equivalence, model quality, or effectiveness on a real project. Each registry entry must record six match fields—name, purpose, inputs, outputs, decision logic, and Workflow role—and explicit Scope and Non-goals.

If implementation shows that a candidate is semantically covered by an existing Skill, stop creating independent behavior for it. Update the Matching Register to `ENHANCE`, `MERGE`, or `MATCH` with difference evidence instead of preserving duplication to satisfy the card count.

## Specialist Boundaries

| Skill | Owns | Does not own |
| --- | --- | --- |
| `requirement-quality-review` | A high-level review of completeness, clarity, verifiability, feasibility, scope, and evidence quality, including routing to specialist analyses | It does not replace the four specialist analyses or produce a numeric quality score or release decision |
| `requirement-ambiguity-analysis` | Unclear references, actors, scope, quantities, conditions, and non-decidable wording | It does not treat an explicit cross-source contradiction as ordinary ambiguity or choose an interpretation for the user |
| `requirement-consistency-analysis` | Agreement of terminology, identifiers, formats, states, rules, and behavior across supplied materials | It does not silently merge mutually exclusive constraints; explicit conflicts remain a conflict-detection and human-decision concern |
| `requirement-conflict-detection` | Evidence-backed mutually exclusive rules, constraints, or acceptance conditions, preserving both sides, scope, and the decision needed | It does not decide precedence, ownership, waiver, or the final business rule |
| `requirement-traceability-analysis` | Bidirectional relationships among requirements, acceptance criteria, design/implementation, test assets, defects, and evidence, including orphans and uncovered items | It does not treat matching names as real links or claim that a test was executed or passed |

## Shared Output Contract

Every Prompt starts with an input audit and includes these shared fields:

1. Input audit: `known`, `missing`, `conflicting`, `stale`, `out_of_scope`, and `assumptions`.
2. Evidence layers: direct source facts, evidence-backed inferences, recommendations, and human decision items remain separate.
3. Findings: each item should include `ID`, `Topic`, `Sources`, `Status`, `Impact`, `Priority`, `Evidence`, `Question or decision needed`, `Suggested owner`, `Suggested next action`, and `Validation method`.
4. Specialist result table: domain-specific fields may be added, but source, status, evidence, and action fields remain present.
5. Risk and dependency handling: distinguish gaps, conflicts, untestable statements, uncovered items, and open questions; every P0/P1 item needs an owner role and a closeable next action.
6. Self-check: look for unsupported conclusions, fact/inference confusion, out-of-scope judgments, unmarked assumptions, and fabricated execution or approval claims.

The packages do not use a shared numeric score. They must not invent SLAs, thresholds, fields, endpoints, owners, environments, or root causes. With incomplete input, they return a minimum usable draft and 3–5 high-value questions; if safe continuation is impossible, they state the blocker and required evidence.

## Package Layout and Documentation Sync

Each language package uses this minimum structure:

```text
skills/{zh,en}/testing-types/<skill-name>/
├── SKILL.md
├── prompts/<skill-name>.md
├── agents/openai.yaml
└── evals/
    ├── eval.yaml
    └── cases/
        ├── basic-success.yaml
        ├── edge-incomplete-input.yaml
        └── edge-scope-boundary.yaml
```

Every Skill includes success, incomplete-input, and scope/risk-boundary Evals; specialist packages add conflict, orphan, or multi-source cases where useful. Chinese and English directories, frontmatter `name`, Agent metadata key, Prompt filename, and Eval structure must align.

After the packages exist, update:

- `skills/zh/README.md` and `skills/en/README.md`;
- `docs/catalog/skills-index.md` and `_EN.md`;
- root `README.md` and `README_EN.md`;
- `docs/catalog/skills-graph.md` and `_EN.md`;
- a Phase 1 requirement-quality governance note and its English mirror;
- `docs/governance/skill-governance-registry.yaml`, then regenerate Matrix, Matching Register, and governance inventory.

These entry points provide navigation and capability boundaries only. They must not create cross-Skill relative internal links or turn recommended composition into an installation dependency.

## Development and Verification Order

Complete the Skills in Project-card order. Each Skill independently goes through:

1. Write and run a pressure or boundary Eval, or an equivalent failing baseline, to record the incorrect behavior it exposes;
2. Write the minimum `SKILL.md`, Prompt, metadata, and three case types that address that failure;
3. Run Skill-up structure checks and usable Evals, confirming that source, status, and human-decision boundaries survive;
4. Review new unsupported inferences, silent merges, or out-of-scope conclusions and make the smallest correction;
5. Run the package's complete static checks before moving to the next Skill.

The final gate is `bash scripts/check_skills_quality.sh`, the governance generators' `--check` modes, `git diff --check`, a Git status check, and verification of the five Project cards. Static gates prove package structure, documentation, metadata, and Eval-file contracts only. Model output quality, runtime behavior, and real-project coverage remain `UNASSESSED` without independent execution evidence.

## Non-goals

- Do not change or delete the behavior of `requirements-analysis` or `requirements-analysis-plus`.
- Do not add shared runtime code, third-party dependencies, external services, or real test targets.
- Do not create GitHub Issues, publish a version, push remote branches, or change Project cards outside this batch.
- Do not use one generic template to hide semantic differences among the five specialists.
