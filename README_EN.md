<div align="right"><strong><a href="./README.md">🇨🇳中文</a></strong> | <strong>🇬🇧English</strong></div>

# Awesome QA Skills

This repo provides **one set of QA workflow Skills** for **Cursor**, **Claude Code**, and **OpenCode**.  
**Chinese and English are split at the directory level:** Chinese skill dirs (e.g. `daily-testing-workflow`), English skill dirs (e.g. `daily-testing-workflow-en`).  
- **Workflow skills** live under **`skills/testing-workflows/`** (daily / sprint / release).  
- **Testing-type skills** live under **`skills/testing-types/`** (15 types × CN/EN).  
Copy the matching dir into your tool's skill location; no need to depend on the repo root.

---

## The Three Workflows (`skills/testing-workflows/`)

| Workflow | Name | Summary |
|----------|------|---------|
| **Daily Testing** | Daily Testing Workflow | Morning routine, test case creation, automation, exploratory testing, bug reporting, afternoon review, wrap-up |
| **Sprint Testing** | Sprint Testing Workflow | 2-week sprint: planning, setup & early testing, active testing, intensive regression, stabilization, review & demo, retrospective & next-sprint prep |
| **Release Testing** | Release Testing Workflow | 1–2 weeks before release through post-release: T-14 planning, feature freeze, specialized testing (performance/security/accessibility/visual), RC, Go/No-Go, deployment, post-release monitoring & retro |

Each workflow includes **When to Use**, **steps**, **How to Use the Prompts**, **Common Pitfalls**, **Best Practices**, and **Reference Files** so AI and testers can follow step-by-step.

---

## Testing Type Skills (`skills/testing-types/`)

Skills per **testing type**; **Chinese and English** are separate dirs (e.g. `functional-testing` / `functional-testing-en`).  

**Output formats:** Default is **Markdown**; you can request **Excel** (tab-separated), **CSV**, or **JSON** by adding a short instruction at the **end** of your request. Each skill dir has **output-formats.md** with examples.

Types: functional-testing, api-testing, automation-testing, bug-reporting, manual-testing, test-case-writing, test-reporting, test-strategy, requirements-analysis, performance-testing, security-testing, accessibility-testing, ai-assisted-testing, test-case-reviewer, mobile-testing (15 types × CN/EN). Prompts are bundled in each skill’s `prompts/`.

See **[skills/testing-types/README.md](skills/testing-types/README.md)**.

---

## Directory Layout

All skills live under **`skills/`**, in two groups:

- **`skills/testing-workflows/`** — The three workflows (daily / sprint / release), each with CN and EN dirs.
- **`skills/testing-types/`** — Per–testing-type skills (15 types × CN/EN), with output format options.

**Chinese skill:** e.g. `daily-testing-workflow` — Chinese `SKILL.md`, `reference.md`, and `prompts/` with Chinese prompts only (`xxx.md`).  
**English skill:** e.g. `daily-testing-workflow-en` — English `SKILL.md`, `reference.md`, and `prompts/` with English prompts only (`xxx_EN.md`).  
**Copy the dir for your language into your tool;** no dependency on the repo root `prompts/`.

| Type | Chinese dir example | English dir example |
|------|---------------------|---------------------|
| Workflows | testing-workflows/daily-testing-workflow, sprint-testing-workflow, release-testing-workflow | testing-workflows/daily-testing-workflow-en, …-en |
| Testing types | testing-types/functional-testing, api-testing, … | testing-types/functional-testing-en, …-en |

```
awesome-qa-skills/
├── skills/
│   ├── testing-workflows/            # Three workflows (CN/EN)
│   │   ├── daily-testing-workflow/   # Daily (Chinese)
│   │   │   ├── SKILL.md
│   │   │   ├── reference.md
│   │   │   └── prompts/              # Chinese .md only
│   │   ├── daily-testing-workflow-en/
│   │   ├── sprint-testing-workflow/
│   │   ├── sprint-testing-workflow-en/
│   │   ├── release-testing-workflow/
│   │   └── release-testing-workflow-en/
│   └── testing-types/                # Per–testing-type (CN/EN + output formats)
│       ├── functional-testing/
│       ├── functional-testing-en/
│       ├── … 15 types × CN/EN
│       └── README.md
├── prompts/                          # Root prompt source (for maintenance)
├── README.md
└── README_EN.md
```

---

## Usage by Tool

Copy the matching skill dir from **`skills/testing-workflows/`** or **`skills/testing-types/`** into your tool’s skill directory. The same skill set works for all tools below.

### Cursor

- **Project-level:** Copy into the project’s `.cursor/skills/`.
  ```bash
  # Workflow example
  cp -r skills/testing-workflows/daily-testing-workflow /path/to/your/project/.cursor/skills/       # Chinese
  cp -r skills/testing-workflows/daily-testing-workflow-en /path/to/your/project/.cursor/skills/   # English
  ```
- **User-level:** Copy to `~/.cursor/skills/`, again choosing by language.

### Claude Code

- Copy into the project’s `.claude/skills/`; dir name must match the skill `name`.
  ```bash
  mkdir -p .claude/skills
  cp -r skills/testing-workflows/daily-testing-workflow .claude/skills/           # Chinese
  cp -r skills/testing-workflows/daily-testing-workflow-en .claude/skills/       # English
  ```

### OpenCode

- **Project-level:** `.opencode/skills/<skill-name>/`
- **Global:** `~/.config/opencode/skills/<skill-name>/`
  ```bash
  mkdir -p .opencode/skills
  cp -r skills/testing-workflows/daily-testing-workflow .opencode/skills/         # Chinese
  cp -r skills/testing-workflows/daily-testing-workflow-en .opencode/skills/   # English
  ```

---

## Prompts and reference (CN/EN)

- **Root `prompts/`:** Multiple prompt categories, each with **Chinese `xxx.md`** and **English `xxx_EN.md`** for maintenance and reference. Each skill dir’s `prompts/` matches the language: **Chinese skills** only `xxx.md`, **English skills** only `xxx_EN.md`. For a given step, open the corresponding file under that skill’s `prompts/` and use it with the AI.
- **Each workflow’s `reference.md`:** Lists prompt types used, their role in the workflow, and a step→prompt mapping so you can look up and run “step → prompt” inside a single skill dir.
- **“How to Use the Prompts” in SKILL.md:** Describes the three steps: check reference → open the matching file under this dir’s `prompts/` → run with context and the AI.

---

## Conventions

- Skill `name` matches dir name; keep the dir name when copying into each tool.

---

## License

This repo provides Skill packaging for AI tools only.
