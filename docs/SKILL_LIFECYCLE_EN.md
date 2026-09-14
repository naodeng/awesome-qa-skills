<div align="right"><a href="./SKILL_LIFECYCLE.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Lifecycle

`Idea → Candidate → Capability Match → Design → Implementation → Eval → Review → Stable`

The Phase 0 source of truth is `governance/skill-governance-registry.yaml` (JSON-compatible YAML); `SKILL_MATRIX_EN.md` and `SKILL_MATCHING_REGISTER_EN.md` are generator-owned views and must not be edited by hand. `Candidate` means matching evidence is pending, not that capability is absent or quality has failed.

Matching routes a candidate to Existing, Enhance, Merge, Match, or New. Stable Skills may return to Enhance or Merge when evidence changes. Deprecated Skills require a replacement path; Archived Skills remain traceable but are no longer maintained.

| Status | Entry condition | Exit condition |
| --- | --- | --- |
| Candidate | A quality gap or candidate name is recorded | Six-step Capability Match completes |
| Existing / Match | Existing coverage evidence is recorded | New evidence triggers Enhance or Merge Review |
| Enhance / Merge | Existing capability needs change or consolidation | Change, Eval, and rescore complete |
| Planned-P0/P1/P2 | Match concludes New and priority is scheduled | Enter Design |
| Experimental | Scope or evidence is insufficient for Stable | Meet score/Eval gate or Redesign |
| Deprecated / Archived | Replacement path and migration impact are recorded | Archived retains traceable history only |

### `REVIEWED_WITH_LIMITATION`

This Registry state means that all six evidence fields were located and structurally compared, while project context, semantic equivalence, runtime results, or Eval evidence is still incomplete. It is not a signal of human approval, release, risk acceptance, or permission to execute changes; `MATCH`, `MERGE`, `ENHANCE`, and `NEW` remain provisional candidate conclusions until Phase 1 reviews requirements and real assets, or explicitly retains the limitation.

Each transition records evidence, decision, ownership, affected bilingual paths, Eval state, and Matrix/documentation updates. No state implies automated human approval, release, or risk acceptance.
