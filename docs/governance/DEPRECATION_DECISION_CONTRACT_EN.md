<div align="right"><a href="./DEPRECATION_DECISION_CONTRACT.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Deprecation Decision Contract

This contract makes deprecation traceable and reversible. It complements the [Skill Deprecation and Archival Guide](../SKILL_DEPRECATION_GUIDE_EN.md) and [Skill Lifecycle](../SKILL_LIFECYCLE_EN.md); it never deletes a directory automatically or uses deprecation to hide an unverified Match conclusion.

## State boundary

| State | Meaning | Required action |
| --- | --- | --- |
| `Deprecated` | A replacement path is confirmed, but historical installation still needs compatibility | Record replacement, retained boundary, migration, and impact |
| `Archived` | The replacement is stable and historical use has been handled | Keep history and docs; stop routine maintenance |
| `UNASSESSED` | Project evidence is insufficient for a deprecation decision | Keep the current path and collect requirement, usage, or maintenance evidence |

## Required record

Every deprecation proposal records at least:

1. `skill`: physical directory and bilingual paths.
2. `decision`: `Deprecated`, `Archived`, or `UNASSESSED`.
3. `replacement`: target Skill, mode, or Workflow; no replacement means no `Deprecated` state.
4. `retained_boundary`: what the old Skill still owns and what it no longer owns.
5. `migration`: install path, invocation, documentation links, and compatibility window.
6. `affected_docs`: Matrix, Catalog, Map, README, Workflow, and installation docs.
7. `eval_install_impact`: Eval, triggers, installers, and script impact; use `NOT_RUN` or `N/A` without evidence.
8. `evidence`: requirements, Issue/PR, usage feedback, or reviewable code evidence.
9. `human_decision`: owner, date, and risk acceptance; use `UNASSESSED` without a human decision.

## Mandatory rules

- Complete Capability Match before deciding Enhance, Merge, or Deprecation; never use deprecation to hide an unreviewed relationship.
- Keep physical directories, historical paths, and bilingual entry points while Deprecated; mark Archived only after migration impact is explicit.
- Synchronize replacement paths in the Matrix, Catalog, Map, README, Workflow, and installers.
- A deprecation record does not prove semantic equivalence, runtime effectiveness, Quality Score, or release approval for the replacement.

## Reproduce and navigate

```bash
python3 scripts/generate_skill_governance_matrix.py --check
python3 scripts/check_docs_bilingual.py --repo-root .
```

- [Governance Matrix](../SKILL_MATRIX_EN.md)
- [Matching Register](../SKILL_MATCHING_REGISTER_EN.md)
- [v1.4 closeout](./PHASE_0_V1_4_CLOSEOUT_EN.md)
