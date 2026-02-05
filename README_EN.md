<div align="right"><strong><a href="./README.md">🇨🇳中文</a></strong> | <strong>🇬🇧English</strong></div>

# Awesome QA Skills

This repo provides **QA workflow Skills** for **Cursor**, **Claude Code**, and **OpenCode**, based on prompts and workflows from [awesome-qa-prompt](https://github.com/awesome-qa-prompt).  
**Chinese and English are split at the directory level:** Chinese skill dirs (e.g. `daily-testing-workflow`), English skill dirs (e.g. `daily-testing-workflow-en`). Copy the dir for your language; no need to depend on the repo root.

---

## The Three Workflows

| Workflow | Name | Summary |
|----------|------|---------|
| **Daily Testing** | Daily Testing Workflow | Morning routine, test case creation, automation, exploratory testing, bug reporting, afternoon review, wrap-up |
| **Sprint Testing** | Sprint Testing Workflow | 2-week sprint: planning, setup & early testing, active testing, intensive regression, stabilization, review & demo, retrospective & next-sprint prep |
| **Release Testing** | Release Testing Workflow | 1–2 weeks before release through post-release: T-14 planning, feature freeze, specialized testing (performance/security/accessibility/visual), RC, Go/No-Go, deployment, post-release monitoring & retro |

Each workflow includes **When to Use**, **steps**, **How to Use the Prompts**, **Common Pitfalls**, **Best Practices**, and **Reference Files** so AI and testers can follow step-by-step.

---

## Directory Layout (CN/EN skill dirs)

For each workflow, Cursor, Claude, and OpenCode each have a **Chinese** and an **English** skill dir:

- **Chinese skill:** e.g. `daily-testing-workflow` — Chinese `SKILL.md`, `reference.md`, and `prompts/` with Chinese prompts only (`xxx.md`).
- **English skill:** e.g. `daily-testing-workflow-en` — English `SKILL.md`, `reference.md`, and `prompts/` with English prompts only (`xxx_EN.md`).

**Copy the dir for your language to use standalone;** no dependency on the repo root `prompts/`.

| Language | Example dir names | Note |
|----------|-------------------|------|
| Chinese | daily-testing-workflow, sprint-testing-workflow, release-testing-workflow | Skill name = dir name |
| English | daily-testing-workflow-en, sprint-testing-workflow-en, release-testing-workflow-en | Skill name has `-en` suffix |

```
awesome-qa-skills/
├── cursor/                          # For Cursor
│   ├── daily-testing-workflow/      # Daily (Chinese)
│   │   ├── SKILL.md
│   │   ├── reference.md
│   │   └── prompts/                 # Chinese .md only
│   ├── daily-testing-workflow-en/   # Daily (English)
│   │   ├── SKILL.md
│   │   ├── reference.md
│   │   └── prompts/                 # xxx_EN.md only
│   ├── sprint-testing-workflow/
│   ├── sprint-testing-workflow-en/
│   ├── release-testing-workflow/
│   └── release-testing-workflow-en/
├── claude/                          # For Claude Code (same layout)
├── opencode/                        # For OpenCode (same layout)
├── prompts/                         # Root prompt source (CN + EN, for maintenance)
├── README.md                        # This repo (Chinese default)
└── README_EN.md                     # This file (English)
```

---

## Usage by Platform

### Cursor

- **Project-level:** Copy the skill dir into the project’s `.cursor/skills/`.
  ```bash
  # Chinese
  cp -r cursor/daily-testing-workflow /path/to/your/project/.cursor/skills/
  # English
  cp -r cursor/daily-testing-workflow-en /path/to/your/project/.cursor/skills/
  ```
- **User-level:** Copy to `~/.cursor/skills/`, again choosing `daily-testing-workflow` or `daily-testing-workflow-en` by language.
- Convention: `SKILL.md` must include `name`, `description` (third person, with trigger context); body &lt; 500 lines recommended.

### Claude Code

- Put skill dirs under the project’s `.claude/skills/`; dir name must match the skill `name`.
  ```bash
  mkdir -p .claude/skills
  cp -r claude/daily-testing-workflow .claude/skills/           # Chinese
  cp -r claude/daily-testing-workflow-en .claude/skills/       # English
  ```
- Convention: frontmatter must include `name`, `version` (semver), `description` (≤ 200 chars recommended).

### OpenCode

- **Project-level:** `.opencode/skills/<skill-name>/SKILL.md`
- **Global:** `~/.config/opencode/skills/<skill-name>/SKILL.md`
  ```bash
  mkdir -p .opencode/skills
  cp -r opencode/daily-testing-workflow .opencode/skills/      # Chinese
  cp -r opencode/daily-testing-workflow-en .opencode/skills/   # English
  ```
- Convention: `name` is lowercase letters, digits, single hyphen (1–64 chars), same as dir name; `description` 1–1024 chars.

---

## Prompts and reference (CN/EN)

- **Root `prompts/`:** 13 prompt categories from awesome-qa-prompt’s `testing-types/<type>/`, each with **Chinese `xxx.md`** and **English `xxx_EN.md`** for maintenance and reference. Each skill dir’s `prompts/` matches the language: **Chinese skills** only `xxx.md`, **English skills** only `xxx_EN.md`. For a given step, open the corresponding file under that skill’s `prompts/` and use it with the AI.
- **Each workflow’s `reference.md`:** Lists prompt types used, their role in the workflow, and a step→prompt mapping so you can look up and run “step → prompt” inside a single skill dir.
- **“How to Use the Prompts” in SKILL.md:** Describes the three steps: check reference → open the matching file under this dir’s `prompts/` → run with context and the AI.

---

## Source and conventions

- Workflow phases, steps, checklists, and recommended prompts come from **awesome-qa-prompt**’s `workflows/` (CN and EN).
- The actual prompts (Role, Task, execution instructions) come from awesome-qa-prompt’s `testing-types/<type>/`, provided in this repo in root `prompts/` and each workflow’s `prompts/` in both languages, and summarized in each skill’s `reference.md` for quick lookup.
- Each platform splits into **Chinese skill dirs** (e.g. `daily-testing-workflow`) and **English skill dirs** (e.g. `daily-testing-workflow-en`); skill `name` matches dir name; frontmatter and length follow each platform’s rules.

---

## License

Aligned with awesome-qa-prompt; this repo only provides Skill packaging for AI tools and does not claim additional copyright.
