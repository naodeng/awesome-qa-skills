<div align="right"><a href="./SKILL_MATCHING_GUIDE.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Capability Matching Guide

Per-candidate decisions live in `governance/skill-governance-registry.yaml`; the Matching Register is a generated view. Regenerate it and run `--check` after changing the registry.

Every candidate must be matched before a directory is created. The only outcomes are `EXISTING`, `ENHANCE`, `MERGE`, `MATCH`, and `NEW`.

Review name, purpose, inputs, outputs, decision logic, and workflow role. `EXISTING` and `MATCH` create no directory; `ENHANCE` improves an existing Skill; `MERGE` adds a mode, rule, or subflow; only `NEW` may create a bilingual standalone Skill. Record evidence in the Matrix and Project. Static review is not runtime proof.

## Limited review state

`REVIEWED_WITH_LIMITATION` means the six evidence fields were located and structurally compared, but project context, semantic equivalence, runtime results, or Eval evidence is still missing. It is not an approval or executable state; `MATCH`, `MERGE`, `ENHANCE`, and `NEW` remain candidate conclusions until Phase 1 review, so the Registry alone must not create, modify, or delete a Skill.
