<div align="right"><a href="./SKILL_MATCHING_GUIDE.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Capability Matching Guide

Per-candidate decisions live in `governance/skill-governance-registry.yaml`; the Matching Register is a generated view. Regenerate it and run `--check` after changing the registry.

Every candidate must be matched before a directory is created. The only outcomes are `EXISTING`, `ENHANCE`, `MERGE`, `MATCH`, and `NEW`.

Review name, purpose, inputs, outputs, decision logic, and workflow role. `EXISTING` and `MATCH` create no directory; `ENHANCE` improves an existing Skill; `MERGE` adds a mode, rule, or subflow; only `NEW` may create a bilingual standalone Skill. Record evidence in the Matrix and Project. Static review is not runtime proof.

## Limited review state

`REVIEWED_WITH_LIMITATION` means the six evidence fields were located and structurally compared, but project context, semantic equivalence, runtime results, or Eval evidence is still missing. It is not an approval or executable state; `MATCH`, `MERGE`, `ENHANCE`, and `NEW` remain candidate conclusions until Phase 1 review, so the Registry alone must not create, modify, or delete a Skill.

## Phase 0 typical mapping review

The [20-row typical mapping review](./governance/PHASE_0_MATCH_MERGE_REVIEW_EN.md) is generated from the Registry and covers 13 candidate mappings plus 7 Existing self-reviews. The Matrix `Related / Workflow` column surfaces relationship summaries for target Skills; the candidate six-field evidence remains in the [Matching Register](./SKILL_MATCHING_REGISTER_EN.md).

The review only records navigation and follow-up actions: `EXISTING` / `MATCH` create no duplicate directory, `MERGE` enters mode/rule/subflow evaluation, and `ENHANCE` enters an existing-Skill enhancement review. Every outcome remains `REVIEWED_WITH_LIMITATION`; it does not replace project semantic review, runtime evaluation, or human approval.

Reproduce with `python3 scripts/generate_skill_governance_matrix.py --check`, then run `python3 scripts/check_docs_bilingual.py --repo-root .`.
