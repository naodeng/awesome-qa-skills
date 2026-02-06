<div align="right"><strong><a href="./README.md">🇨🇳中文</a></strong> | <strong>🇬🇧English</strong></div>

# Awesome QA Skills

This repo provides **one set of QA workflow Skills** for **Cursor**, **Claude Code**, and **OpenCode**, based on prompts and workflows from [awesome-qa-prompt](https://github.com/awesome-qa-prompt).  
**Chinese and English are split at the directory level:** Chinese skill dirs (e.g. `daily-testing-workflow`), English skill dirs (e.g. `daily-testing-workflow-en`). Copy the matching dir from **`skills/`** into your tool’s skill location; no need to depend on the repo root.

---

## The Three Workflows

| Workflow | Name | Summary |
|----------|------|---------|
| **Daily Testing** | Daily Testing Workflow | Morning routine, test case creation, automation, exploratory testing, bug reporting, afternoon review, wrap-up |
| **Sprint Testing** | Sprint Testing Workflow | 2-week sprint: planning, setup & early testing, active testing, intensive regression, stabilization, review & demo, retrospective & next-sprint prep |
| **Release Testing** | Release Testing Workflow | 1–2 weeks before release through post-release: T-14 planning, feature freeze, specialized testing (performance/security/accessibility/visual), RC, Go/No-Go, deployment, post-release monitoring & retro |

Each workflow includes **When to Use**, **steps**, **How to Use the Prompts**, **Common Pitfalls**, **Best Practices**, and **Reference Files** so AI and testers can follow step-by-step.

---

## Directory Layout (single `skills/`)

All skills live under **`skills/`**, with Chinese and English dirs:

- **Chinese skill:** e.g. `daily-testing-workflow` — Chinese `SKILL.md`, `reference.md`, and `prompts/` with Chinese prompts only (`xxx.md`).
- **English skill:** e.g. `daily-testing-workflow-en` — English `SKILL.md`, `reference.md`, and `prompts/` with English prompts only (`xxx_EN.md`).

**Copy the dir for your language from `skills/` into your tool;** no dependency on the repo root `prompts/`.

| Language | Example dir names | Note |
|----------|-------------------|------|
| Chinese | daily-testing-workflow, sprint-testing-workflow, release-testing-workflow | Skill name = dir name |
| English | daily-testing-workflow-en, sprint-testing-workflow-en, release-testing-workflow-en | Skill name has `-en` suffix |

```
awesome-qa-skills/
├── skills/                           # Single skill set (Cursor / Claude Code / OpenCode)
│   ├── daily-testing-workflow/       # Daily (Chinese)
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
├── prompts/                          # Root prompt source (CN + EN, for maintenance)
├── README.md                         # This repo (Chinese default)
└── README_EN.md                      # This file (English)
```

---

## Usage by Tool

Copy the matching skill dir from **`skills/`** into your tool’s skill directory. The same skill set works for all tools below.

### Cursor

- **Project-level:** Copy into the project’s `.cursor/skills/`.
  ```bash
  cp -r skills/daily-testing-workflow /path/to/your/project/.cursor/skills/       # Chinese
  cp -r skills/daily-testing-workflow-en /path/to/your/project/.cursor/skills/   # English
  ```
- **User-level:** Copy to `~/.cursor/skills/`, again choosing by language.

### Claude Code

- Copy into the project’s `.claude/skills/`; dir name must match the skill `name`.
  ```bash
  mkdir -p .claude/skills
  cp -r skills/daily-testing-workflow .claude/skills/           # Chinese
  cp -r skills/daily-testing-workflow-en .claude/skills/       # English
  ```

### OpenCode

- **Project-level:** `.opencode/skills/<skill-name>/`
- **Global:** `~/.config/opencode/skills/<skill-name>/`
  ```bash
  mkdir -p .opencode/skills
  cp -r skills/daily-testing-workflow .opencode/skills/         # Chinese
  cp -r skills/daily-testing-workflow-en .opencode/skills/   # English
  ```

---

## Prompts and reference (CN/EN)

- **Root `prompts/`:** 13 prompt categories from awesome-qa-prompt’s `testing-types/<type>/`, each with **Chinese `xxx.md`** and **English `xxx_EN.md`** for maintenance and reference. Each skill dir’s `prompts/` matches the language: **Chinese skills** only `xxx.md`, **English skills** only `xxx_EN.md`. For a given step, open the corresponding file under that skill’s `prompts/` and use it with the AI.
- **Each workflow’s `reference.md`:** Lists prompt types used, their role in the workflow, and a step→prompt mapping so you can look up and run “step → prompt” inside a single skill dir.
- **“How to Use the Prompts” in SKILL.md:** Describes the three steps: check reference → open the matching file under this dir’s `prompts/` → run with context and the AI.

---

## Source and conventions

- Workflow phases, steps, checklists, and recommended prompts come from **awesome-qa-prompt**’s `workflows/` (CN and EN).
- The actual prompts (Role, Task, execution instructions) come from awesome-qa-prompt’s `testing-types/<type>/`, provided in this repo in root `prompts/` and each workflow’s `prompts/` in both languages, and summarized in each skill’s `reference.md` for quick lookup.
- Skill `name` matches dir name; keep the dir name when copying into each tool.

---

## License

Aligned with awesome-qa-prompt; this repo only provides Skill packaging for AI tools and does not claim additional copyright.
