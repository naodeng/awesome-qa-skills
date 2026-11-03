<div align="right"><a href="./SKILL_LIFECYCLE_POLICY.md">🇨🇳 Chinese</a> | <strong>🇬🇧 English</strong></div>

# Skill Lifecycle Governance

## States

Lifecycle state is separate from capability-governance labels such as `Existing`, `Planned-P0`, or `Enhance`. Without evidence of real effectiveness and adoption, lifecycle remains `UNASSESSED`. A directory, valid Eval configuration, or passing static gate does not by itself prove stability or user value.

| State | Meaning | Entry and exit evidence |
| --- | --- | --- |
| `UNASSESSED` | Evidence is insufficient for a lifecycle decision | Default; review after usage, behavior, and maintenance evidence is available |
| `EXPERIMENTAL` | Pilot for a new capability or material change | Requires bounded scope, an owner, and Eval; request `STABLE` after reliability and adoption evidence, or retire it |
| `STABLE` | Behavior, compatibility, and maintenance expectations are repeatedly verified | Requires versioned behavior Evals, compatibility evidence, recorded use cases, and a maintenance commitment |
| `MAINTENANCE` | Retained for users without further feature expansion | Record support boundaries, known limits, necessary security fixes, and migration target; review deprecation if demand ends |
| `DEPRECATED` | Not recommended for new adoption; existing users receive a migration window | Must state an alternative, compatibility window, migration steps, and end-of-support date; never remove silently |
| `ARCHIVED` | No longer maintained and removed from routine distribution | Archive after migration and retention windows; preserve source and compatibility history |

The current governance Registry `status` describes capability matching or roadmap classification. A separate `lifecycle` field records lifecycle. Older entries without actual use/effectiveness data are `UNASSESSED`. The three orchestration pilots remain `EXPERIMENTAL`; a structural gate or individual Eval pass does not automatically promote them.

## Review evidence

Lifecycle review checks at least:

- **Use value:** Verifiable real-use records; mark it `UNASSESSED` when adoption data is unavailable.
- **Effectiveness and reliability:** Versioned Evals and regressions; distinguish config validation, rule assertions, model behavior, and host execution.
- **Uniqueness and overlap:** Capability scope, inputs/outputs, and trigger semantics; a human reviews overlap before enhancing, merging, or retiring a Skill.
- **Compatibility and maintenance:** Standalone installation, resource closure, agent compatibility boundaries, maintenance cost, and security ownership.
- **Criticality:** Low-frequency, high-risk capabilities (such as disaster recovery and security incidents) may be retained for criticality; call counts never auto-retire them.

Changes to `STABLE`, `MAINTENANCE`, `DEPRECATED`, or `ARCHIVED` record the review date, evidence paths, rationale, and reviewer. Model self-assessment does not replace independent adoption or business acceptance evidence.

## Retirement and residual installs

Before deprecation, check references, indexes, install entry points, and downstream compatibility, then publish migration guidance. The residual-install checker is read-only and scans only the user-selected install root. It identifies legacy `-en` suffixes, Skills absent from the repository, and package directories whose name differs from the `SKILL.md` canonical name. It never deletes automatically.

```bash
python3 scripts/manage_skill_packages.py check-residue \
  --install-root /path/to/agent/skills --repo-root . --json
```

A standalone Skill can be packaged as a ZIP. Uninstall is a preview by default; only explicit `--apply` removes one direct child directory containing `SKILL.md` from the selected install root. Upgrades use the existing installer to replace the same canonical directory; broad deletion scans are not part of upgrade or cleanup.

```bash
python3 scripts/manage_skill_packages.py pack \
  --skill-dir skills/en/testing-workflows/pr-quality-review \
  --output /tmp/pr-quality-review-en.zip
python3 scripts/manage_skill_packages.py uninstall \
  --install-root /path/to/agent/skills --skill pr-quality-review  # preview
```

## Validation

Governance views use the existing Registry and matrix generator. Evidence, lifecycle state, and installation compatibility gates report their own scope. After updating a Skill's index, classification, or lifecycle state, run `bash scripts/check_skills_quality.sh` and `bash scripts/check_skills_cli_compatibility.sh`.
