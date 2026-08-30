<div align="right"><a href="./2026-08-29-project-structure-and-bilingual-docs-design.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Project Structure and Bilingual Documentation Design

## Goal

Organize project-level files so the repository root retains only user entry points, contribution entry points, licensing, agent guidance, and compatibility installer wrappers. Review all active project documentation so Chinese remains the default, English mirrors are complete, content is accurate, and language switching works in both directions.

The `skills/` tree is an installation and distribution contract. No directory under it will be moved, renamed, or removed.

## Directory Design

```text
docs/
├── catalog/       # Skill indexes and relationship graph
├── governance/    # Documentation policy and capability roadmap
├── generated/     # Regenerable project reports
├── reviews/       # Active reviews
├── superpowers/   # Designs and implementation records
└── archive/
    ├── reviews/   # Superseded reviews
    └── internal/  # Internal drafts
```

The root keeps `README*`, `CONTRIBUTING*`, `FAQ*`, `LICENSE`, `AGENTS.md`, both compatibility installer entry points, and existing engineering directories.

## File Moves

- `skills-index.md` / `skills-index_EN.md` → `docs/catalog/`
- `skills-graph.md` → `docs/catalog/skills-graph.md`
- `skills-metadata-report.md` → `docs/generated/skills-metadata-report.md`
- `docs/DOCUMENTATION_POLICY*` → `docs/governance/`
- `docs/QA_SKILLS_EVOLUTION_ROADMAP*` → `docs/governance/`
- `SKILLS_REVIEW_REPORT.md` → `docs/archive/reviews/SKILLS_REVIEW_REPORT-2026-08-07.md`
- `SYSTEM_AGENT_DRAFT.md` → `docs/archive/internal/SYSTEM_AGENT_DRAFT.md`

Internal links, validation manifests, and generator output paths will be updated. Root installer wrappers stay in place to preserve the interface used by the README and generated installers.

## Bilingual Documentation Boundary

Active project-level user and governance documents must use Chinese `NAME.md` and English `NAME_EN.md` files with two-way switching at the top. Chinese remains the default entry.

Historical archives, generated reports, internal drafts, third-party licenses, evaluations, and local runtime artifacts do not require mirrors. Internal Skill documents remain mirrored by identical paths under `skills/zh` and `skills/en`, without per-file switch links.

## Content Review

The review checks more than file presence:

- Chinese and English titles, sections, and key conclusions align;
- Skill counts, classifications, and evolution status match the repository;
- relative links still resolve after the moves;
- Chinese documents remain the default and English documents link back;
- superseded reports are not presented as current conclusions.

## Automated Validation

Extend `scripts/check_docs_bilingual.py` to:

- use the new project-document paths;
- validate project-level document pairs and two-way switches;
- check relative Markdown links in maintained project documents;
- retain README catalog completeness and zh/en Skill-directory parity checks.

Final verification runs unit tests, `bash scripts/check_skills_quality.sh`, `git diff --check`, and a before/after comparison of the `skills/` directory tree.

## Workspace Safety

The repository currently contains unrelated uncommitted script changes. They will be preserved. If this task must touch an overlapping script, only the task-specific delta will be committed and unrelated edits will not be reverted.
