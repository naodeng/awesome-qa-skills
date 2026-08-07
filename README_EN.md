<div align="right"><strong><a href="./README.md">🇨🇳中文</a></strong> | <strong>🇬🇧English</strong></div>

# Awesome QA Skills

A language-partitioned **AI testing skills library** (Agent Skills) for Codex, Cursor, Claude Code, Kiro, OpenCode, Trae, and similar tools. It ships independently installable, composable skills for testing workflows and testing types.

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](./LICENSE)
[![Skills](https://img.shields.io/badge/skills-76%20(zh%2Ben)-0A7EA4)](./skills-index.md)
[![Workflows](https://img.shields.io/badge/workflows-4-informational)](./skills/en/testing-workflows/)
[![Testing types](https://img.shields.io/badge/testing%20types-34-informational)](./skills/en/testing-types/)

**Online site:** [https://inaodeng.com/qaskills/](https://inaodeng.com/qaskills/)

---

## Why this repository

| Capability | Description |
| --- | --- |
| Bilingual parity | `skills/zh` and `skills/en` share the same folder names and layout |
| Full testing chain | From requirements and strategy through cases, execution, defects, and reporting |
| Workflows + type skills | Daily / sprint / release workflows, composed with 34 specialized type skills |
| Ready to install | One-click installers plus per-skill shortcut scripts |
| Evaluable & evolvable | Every skill includes `evals/`; validate and run with [skill-up](https://github.com/alibaba/skill-up) |

Each skill directory is meant to be self-contained when copied out: `SKILL.md`, primary prompts, tool metadata, plus optional examples, templates, scripts, and eval cases.

## Supported AI tools

| Tool | Typical install target |
| --- | --- |
| Codex | `~/.codex/skills/` |
| Cursor | `~/.cursor/skills/` |
| Claude Code | Claude skills directory (see install guide) |
| Kiro / OpenCode / Trae | See [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) |

You can also `cp -r` a single skill folder into the tool’s skills path.

## 5-minute start

### 1. Clone the repository

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. Install skills (pick one)

```bash
# One-click: all tools × both languages
bash ./install-skills-mac.sh --tool all --lang all

# Codex + English only
bash ./install-skills-mac.sh --tool codex --lang en

# Single skill (example: functional-testing → Codex)
bash installers/en/functional-testing/mac/codex.sh
```

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\install-skills-windows.ps1 -Tool all -Lang all
```

Manual copy:

```bash
cp -r skills/en/testing-types/functional-testing ~/.cursor/skills/
```

Full options and tool paths: [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)

### 3. Invoke in your AI tool

```text
@skill functional-testing
Help me generate test cases for user login
```

Unsure which skill to use? Start with the router:

```text
@skill discover-testing
I need a pre-release regression — which skills should I use?
```

---

## Skill catalog

**38** skills per language (4 workflows + 34 testing types); **76** directories with zh/en parity. Full index: [skills-index.md](skills-index.md).

### Workflow skills

| Skill | Path | When to use |
| --- | --- | --- |
| Daily Testing Workflow | [`daily-testing-workflow`](skills/en/testing-workflows/daily-testing-workflow/) | Daily smoke, bug follow-up, day plan |
| Sprint Testing Workflow | [`sprint-testing-workflow`](skills/en/testing-workflows/sprint-testing-workflow/) | Sprint planning, incremental acceptance, iteration risk |
| Release Testing Workflow | [`release-testing-workflow`](skills/en/testing-workflows/release-testing-workflow/) | Release gates, regression scope, go-live checks |
| Discover Testing Router | [`discover-testing`](skills/en/testing-workflows/discover-testing/) | Recommend skills from a testing goal |

### Testing-type skills

#### Core execution

| Skill | Path |
| --- | --- |
| Functional Testing | [`functional-testing`](skills/en/testing-types/functional-testing/) |
| API Testing | [`api-testing`](skills/en/testing-types/api-testing/) |
| Automation Testing | [`automation-testing`](skills/en/testing-types/automation-testing/) |
| Manual / Exploratory Testing | [`manual-testing`](skills/en/testing-types/manual-testing/) |
| Performance Testing | [`performance-testing`](skills/en/testing-types/performance-testing/) |
| Security Testing | [`security-testing`](skills/en/testing-types/security-testing/) |
| Mobile Testing | [`mobile-testing`](skills/en/testing-types/mobile-testing/) |
| Accessibility Testing | [`accessibility-testing`](skills/en/testing-types/accessibility-testing/) |

#### Process & artifacts

| Skill | Path |
| --- | --- |
| Requirements Analysis | [`requirements-analysis`](skills/en/testing-types/requirements-analysis/) |
| Test Strategy | [`test-strategy`](skills/en/testing-types/test-strategy/) |
| Test Case Writing | [`test-case-writing`](skills/en/testing-types/test-case-writing/) |
| Test Case Review | [`test-case-reviewer`](skills/en/testing-types/test-case-reviewer/) |
| Code Review | [`code-review`](skills/en/testing-types/code-review/) |
| Bug Reporting | [`bug-reporting`](skills/en/testing-types/bug-reporting/) |
| Test Reporting | [`test-reporting`](skills/en/testing-types/test-reporting/) |
| AI-Assisted Testing | [`ai-assisted-testing`](skills/en/testing-types/ai-assisted-testing/) |

#### Tool-specific

| Skill | Path |
| --- | --- |
| API Test (Bruno) | [`api-test-bruno`](skills/en/testing-types/api-test-bruno/) |
| API Test (Postman) | [`api-test-postman`](skills/en/testing-types/api-test-postman/) |
| API Test (Pytest) | [`api-test-pytest`](skills/en/testing-types/api-test-pytest/) |
| API Test (Rest Assured) | [`api-test-restassure`](skills/en/testing-types/api-test-restassure/) |
| API Test (Supertest) | [`api-test-supertest`](skills/en/testing-types/api-test-supertest/) |
| UI Test (Selenium) | [`ui-test-selenium`](skills/en/testing-types/ui-test-selenium/) |
| UI Test (Playwright) | [`ui-test-playwright`](skills/en/testing-types/ui-test-playwright/) |
| UI Test (TestCafe) | [`ui-test-testcafe`](skills/en/testing-types/ui-test-testcafe/) |
| UI Test (Cypress) | [`ui-test-cypress`](skills/en/testing-types/ui-test-cypress/) |
| UI Test (Puppeteer) | [`ui-test-puppeteer`](skills/en/testing-types/ui-test-puppeteer/) |
| UI Test (WebdriverIO) | [`ui-test-webdriverio`](skills/en/testing-types/ui-test-webdriverio/) |
| Performance Test (k6) | [`performance-test-k6`](skills/en/testing-types/performance-test-k6/) |
| Performance Test (Gatling) | [`performance-test-gatling`](skills/en/testing-types/performance-test-gatling/) |
| Performance Test (JMeter) | [`performance-test-jmeter`](skills/en/testing-types/performance-test-jmeter/) |

#### Plus variants

| Skill | Path |
| --- | --- |
| Requirements Analysis Plus | [`requirements-analysis-plus`](skills/en/testing-types/requirements-analysis-plus/) |
| Test Strategy Plus | [`test-strategy-plus`](skills/en/testing-types/test-strategy-plus/) |
| Testcase Writer Plus | [`testcase-writer-plus`](skills/en/testing-types/testcase-writer-plus/) |
| Test Case Reviewer Plus | [`test-case-reviewer-plus`](skills/en/testing-types/test-case-reviewer-plus/) |

> Chinese versions live under `skills/zh/...` with the same folder names. Language indexes: [skills/en/README.md](skills/en/README.md) · [skills/zh/README.md](skills/zh/README.md)

---

## Repository layout

```text
awesome-qa-skills/
├── skills/
│   ├── zh/                      # Chinese skills
│   │   ├── testing-workflows/
│   │   └── testing-types/
│   └── en/                      # English skills (same shape)
├── scripts/                     # Install, validate, and eval helpers
├── installers/                  # Generated per-skill / per-tool shortcuts
├── AGENTS.md                    # Conventions for coding agents
├── skills-index.md              # Full skill index
├── README.md / README_EN.md
└── LICENSE                      # GPL-3.0
```

### Per-skill layout

```text
skills/{zh|en}/{testing-types|testing-workflows}/<skill-name>/
├── SKILL.md                 # Entry + YAML frontmatter (required)
├── prompts/                 # Primary prompts (required)
├── agents/openai.yaml       # OpenAI / Codex metadata (required)
├── evals/                   # skill-up eval cases (present for all skills here)
├── output-formats.md        # Optional multi-format output notes
├── quick-start.md           # Optional shortest path
├── references/ · examples/ · scripts/
└── ...
```

Details: [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md) · [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)

## Design principles

- **Language partition, name parity:** zh/en share skill folder names; no `-en` suffix; English prompt filenames do not use `_EN`.
- **Independently installable:** do not hard-link skill A to skill B internals; cross-skill advice stays in prose.
- **Progressive disclosure:** keep `SKILL.md` lean; put depth in `prompts/`, `references/`, and `examples/`.
- **Actionable outputs:** Markdown by default; switch via `output-formats.md` for Excel/CSV/JSON/Word.
- **Secure by default:** never hard-code real tokens, passwords, or private keys in examples or docs.

## Quality and evaluation

Before submitting changes, run from the repo root:

```bash
bash scripts/check_skills_quality.sh
```

This gate covers directory hygiene, agents metadata, install independence, integrity checks, and skill-up evals YAML validation.

Optional validate / run with [skill-up](https://github.com/alibaba/skill-up):

```bash
curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash
bash scripts/validate_skill_evals.sh
bash scripts/run_skill_eval.sh skills/en/testing-types/functional-testing/evals/eval.yaml
```

Suggested pilots: `functional-testing`, `api-testing`, `api-test-bruno`, `bug-reporting`, `performance-test-k6`. See [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md).

## Documentation map

| Document | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Coding-agent conventions and quality checks |
| [skills-index.md](skills-index.md) | Full skill index |
| [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md) | Directory and naming rules |
| [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md) | Authoring and skill-up eval conventions |
| [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) | Install options and tool paths |
| [FAQ_EN.md](FAQ_EN.md) | FAQ (English) |
| [CONTRIBUTING.md](CONTRIBUTING.md) / [CONTRIBUTING_EN.md](CONTRIBUTING_EN.md) | Contribution guide |
| [skills-graph.md](skills-graph.md) | Skill relationship graph (reference) |

## Contributing

Issues and PRs are welcome: new skills, bilingual parity, prompt/evals improvements, installers, and docs.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)
2. Update zh and en together unless the change is intentionally single-language
3. Run `bash scripts/check_skills_quality.sh` before opening a PR

## License

This repository is licensed under [GNU GPL v3](./LICENSE). You may use, modify, and redistribute it under the same license terms.
