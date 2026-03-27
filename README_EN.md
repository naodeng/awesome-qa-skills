<div align="right"><strong><a href="./README.md">🇨🇳中文</a></strong> | <strong>🇬🇧English</strong></div>

# AI Testing Assistant Skills

This repository is a language-first AI testing skills library for tools such as Codex, Cursor, Claude Code, Kiro, OpenCode, and Trae.

Online URL: https://inaodeng.com/qaskills/

## What You Get

- Chinese and English skill sets
- 4 workflow skills
- 25 testing-type skills
- Ready-to-copy folders for major AI tools

## Core Layout

- Chinese skills: `skills/zh`
- English skills: `skills/en`
- Workflow skills: `testing-workflows`
- Testing-type skills: `testing-types`

## 5-Minute Start

### 1. Clone the repository

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. Copy one skill into your AI tool

```bash
# Example: copy the English functional testing skill into Cursor
cp -r skills/en/testing-types/functional-testing ~/.cursor/skills/

# Example: copy the Chinese daily testing workflow into Cursor
cp -r skills/zh/testing-workflows/daily-testing-workflow ~/.cursor/skills/
```

### 3. Call it in your AI tool

```text
@skill functional-testing
Help me generate test cases for user login functionality
```

## Recommended Skill Entry Points (English)

### Workflow Skills

| Skill | Path |
| --- | --- |
| Daily Testing Workflow | `skills/en/testing-workflows/daily-testing-workflow` |
| Sprint Testing Workflow | `skills/en/testing-workflows/sprint-testing-workflow` |
| Release Testing Workflow | `skills/en/testing-workflows/release-testing-workflow` |
| Discover Testing Router | `skills/en/testing-workflows/discover-testing` |

### Testing-Type Skills

| Skill | Path |
| --- | --- |
| Functional Testing | `skills/en/testing-types/functional-testing` |
| API Testing | `skills/en/testing-types/api-testing` |
| Automation Testing | `skills/en/testing-types/automation-testing` |
| Manual / Exploratory Testing | `skills/en/testing-types/manual-testing` |
| Performance Testing | `skills/en/testing-types/performance-testing` |
| Security Testing | `skills/en/testing-types/security-testing` |
| Mobile Testing | `skills/en/testing-types/mobile-testing` |
| Accessibility Testing | `skills/en/testing-types/accessibility-testing` |
| Bug Reporting | `skills/en/testing-types/bug-reporting` |
| Test Case Writing | `skills/en/testing-types/test-case-writing` |
| Test Case Review | `skills/en/testing-types/test-case-reviewer` |
| Test Reporting | `skills/en/testing-types/test-reporting` |
| Test Strategy | `skills/en/testing-types/test-strategy` |
| Requirements Analysis | `skills/en/testing-types/requirements-analysis` |
| AI-Assisted Testing | `skills/en/testing-types/ai-assisted-testing` |
| API Test (Bruno) | `skills/en/testing-types/api-test-bruno` |
| API Test (Pytest) | `skills/en/testing-types/api-test-pytest` |
| API Test (Rest Assured) | `skills/en/testing-types/api-test-restassure` |
| API Test (Supertest) | `skills/en/testing-types/api-test-supertest` |
| Performance Test (k6) | `skills/en/testing-types/performance-test-k6` |
| Performance Test (Gatling) | `skills/en/testing-types/performance-test-gatling` |
| Requirements Analysis Plus | `skills/en/testing-types/requirements-analysis-plus` |
| Test Case Reviewer Plus | `skills/en/testing-types/test-case-reviewer-plus` |
| Test Strategy Plus | `skills/en/testing-types/test-strategy-plus` |
| Testcase Writer Plus | `skills/en/testing-types/testcase-writer-plus` |

> Chinese versions are available under `skills/zh/...` with the same folder names.

## One-Click Install

```bash
# macOS / Linux
bash ./install-skills-mac.sh --tool all --lang all

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File .\install-skills-windows.ps1 -Tool all -Lang all
```

For all options, see [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md).

If you want a one-click installer for a single skill, use the generated shortcut folders, for example:

```bash
# Install the English functional-testing skill into Codex
bash installers/en/functional-testing/mac/codex.sh
```

## Project Structure

```text
awesome-qa-skills/
├── skills/
│   ├── zh/
│   │   ├── testing-workflows/
│   │   └── testing-types/
│   └── en/
│       ├── testing-workflows/
│       └── testing-types/
├── scripts/
├── README.md
├── README_EN.md
└── skills-index.md
```

## Rules

- Language is separated by `skills/zh` and `skills/en`
- Each skill keeps its prompts directly under `prompts/`
- English prompt filenames do not use `_EN`
- Chinese and English skill names are aligned and no longer use `-en`

## Useful Documents

- [skills-index.md](skills-index.md): full skill index
- [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md): directory rules
- [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md): installation guide
- [FAQ.md](FAQ.md): common questions

## License

This repository provides an AI-oriented testing skills library for direct team reuse and extension.
