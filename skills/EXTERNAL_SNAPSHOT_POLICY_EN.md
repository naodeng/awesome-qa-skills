<div align="right"><a href="./EXTERNAL_SNAPSHOT_POLICY.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# External Reference Policy

This repository keeps every Skill self-contained and maintainable.

## Rules

1. Prefer approved direct source links or formal files inside the Skill.
2. `_external` snapshots are discouraged by default.
3. If `_external` is temporarily necessary:
   - use readable names rather than hash-only names;
   - annotate the source in the file header;
   - keep no more than five files per Skill;
   - remove the snapshot after localization.

## Required Check

```bash
bash scripts/check_skills_quality.sh
```

The gate covers metadata, Skill independence, snapshot hygiene, bilingual documentation, eval YAML, and release structure.
