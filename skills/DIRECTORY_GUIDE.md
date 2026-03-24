# Skills Directory Guide

This repository has three layers of skill directories:

## 1) Core source (edit here)

- `skills/testing-types`
- `skills/testing-workflows`

These are the canonical source directories used by install scripts and validations.

## 2) Language views (browse here)

- `skills/skills-zh`
- `skills/skills-en`

These are symlink-based views:

- `skills-zh` maps to Chinese core skills (same names as source).
- `skills-en` maps to English core skills, but view names remove the `-en` suffix.

Example:

- `skills/skills-en/testing-types/functional-testing`
  -> `skills/testing-types/functional-testing-en`

## 3) Release package output (distribute here)

- `skills/release`

This is a non-symlink release build output for distribution.

## One-command directory maintenance

Run:

```bash
python3 scripts/organize_project_dirs.py
```

What it does:

1. Repairs missing core directories from `skills/release` when possible.
2. Rebuilds language views (`skills-zh`, `skills-en`) to keep mappings consistent.
3. Validates structure and fails fast on broken links.

## All-skills integrity check

To enforce independence and completeness for all skills in this project:

```bash
python3 scripts/validate_skills_integrity.py --fail-on-findings --report-md /tmp/skills-integrity-check.md
```

This includes core, explore, and release skills.
