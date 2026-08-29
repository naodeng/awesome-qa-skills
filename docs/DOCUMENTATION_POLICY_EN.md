<div align="right"><a href="./DOCUMENTATION_POLICY.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Bilingual Documentation Maintenance Policy

## Default Language

Chinese is the project's default language. The root `README.md` is the default GitHub entry; English readers switch to `README_EN.md` from the link at the top.

## Documents That Require Bilingual Mirrors

- Root README files, contribution guides, FAQs, and complete Skill indexes
- The active capability-evolution roadmap
- Current designs, implementation plans, and audit reports
- Directory, authoring, style, and external-snapshot governance under `skills/`
- Language entry README files under `skills/zh` and `skills/en`
- Internal Skill `SKILL.md`, primary prompts, README files, quick starts, tutorials, output formats, and workflow references

Project-level documents use `NAME.md` for Chinese and `NAME_EN.md` for English, with two-way switching at the top.

Internal Skill documents do not use `_EN` names or per-file language switches. They are mirrored through identical relative paths under `skills/zh` and `skills/en`.

## Content Excluded from File-by-File Translation

- Archived records under `docs/archive/`
- Completed historical plans and specs created before 2026-08-29
- Compatibility content under `legacy-prompts/`
- Language-specific examples, references, output templates, and eval fixtures
- Generated `skills-graph.md`, `skills-metadata-report.md`, and evaluation outputs
- Internal drafts, agent handoff context, and third-party license text

These files may remain single-language or keep their existing bilingual content, but they must not be the only official entry for current user documentation.

## Automated Validation

```bash
python3 scripts/check_docs_bilingual.py --repo-root .
bash scripts/check_skills_quality.sh
```

The checks cover project document mirrors, two-way switches, maintained Skill-document path parity, README classification completeness, and identical zh/en testing-type directory names.
