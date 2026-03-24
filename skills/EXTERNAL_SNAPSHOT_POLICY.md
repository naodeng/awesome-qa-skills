# External Reference Policy

This repository uses a strict policy to keep each skill self-contained and maintainable.

## Rule

1. Prefer direct source links (for approved cross-language prompt links) or in-skill formal files.
2. `_external` snapshots are discouraged by default.
3. If `_external` must be used temporarily:
   - readable file name (no hash-only naming),
   - source annotation in file header,
   - max 5 files per skill,
   - remove after source is localized.

## Required checks

Run before commit:

```bash
bash scripts/check_skills_quality.sh
```

This check includes:
- metadata validation
- skills independence validation
- external snapshot hygiene validation
- non-symlink release build generation
