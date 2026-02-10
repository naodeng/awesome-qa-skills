<div align="right"><strong><a href="./README.md">🇨🇳中文</a></strong> | <strong>🇬🇧English</strong></div>

# AI Testing Assistant Skills

A comprehensive **testing skills library designed specifically for AI coding assistants**, transforming **Cursor**, **Claude Code**, **Kiro**, and other AI tools into your professional testing assistant.

## 🎯 Project Core

Provides **18 carefully designed testing Skills**:
- ✅ **15 Testing Type Skills** - Covering functional, API, automation, performance, security, and more
- ✅ **3 Workflow Skills** - Complete processes for daily testing, Sprint testing, and release testing

Each Skill includes:
- 📋 Structured prompts
- 🎯 Best practices and usage guides
- 🔄 Intelligent output format support
- 🌐 Chinese and English versions

## 🚀 5 Minute Quick Start

### 1. Clone the Project

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. Install Skills to AI Tool

```bash
# Cursor example - Copy functional testing skill (English)
cp -r skills/testing-types/functional-testing-en ~/.cursor/skills/

# Or copy daily testing workflow (English)
cp -r skills/testing-workflows/daily-testing-workflow-en ~/.cursor/skills/
```

### 3. Use in AI Tool

```
@skill functional-testing-en
Help me generate test cases for user login functionality
```

AI will automatically:
- 📋 Analyze requirements and identify test scenarios
- ✅ Generate structured test cases
- 🔍 Identify boundary conditions and exception scenarios
- 📊 Provide test data suggestions

## 📦 Skills List

### 🔄 Three Workflow Skills

| Skill | Description | Directory |
|-------|-------------|-----------|
| **Daily Testing Workflow** | Daily test plans, test case writing, defect analysis, test reports | `skills/testing-workflows/daily-testing-workflow` |
| **Sprint Testing Workflow** | Sprint planning, regression test prioritization, risk assessment | `skills/testing-workflows/sprint-testing-workflow` |
| **Release Testing Workflow** | Release checklists, Go/No-Go decisions, rollback plans | `skills/testing-workflows/release-testing-workflow` |

### 🧪 Fifteen Testing Type Skills

| Skill | AI Capabilities | Directory |
|-------|----------------|-----------|
| **Functional Testing** | Auto-identify test scenarios, generate test cases, boundary value analysis | `skills/testing-types/functional-testing` |
| **API Testing** | Generate test cases from API docs, auto-generate automation scripts | `skills/testing-types/api-testing` |
| **Automation Testing** | POM pattern code generation, data-driven test design | `skills/testing-types/automation-testing` |
| **Performance Testing** | Performance scenario design, load model generation, bottleneck analysis | `skills/testing-types/performance-testing` |
| **Security Testing** | OWASP Top 10 checklists, security test case generation | `skills/testing-types/security-testing` |
| **Mobile Testing** | Cross-platform test strategy, compatibility matrix generation | `skills/testing-types/mobile-testing` |
| **Accessibility Testing** | WCAG compliance checks, accessibility test cases | `skills/testing-types/accessibility-testing` |
| **Bug Reporting** | Intelligent defect classification, root cause analysis suggestions | `skills/testing-types/bug-reporting` |
| **Test Case Writing** | Test case template generation, test data suggestions | `skills/testing-types/test-case-writing` |
| **Test Reporting** | Automated report generation, data visualization suggestions | `skills/testing-types/test-reporting` |
| **Test Strategy** | Risk assessment, test scope recommendations | `skills/testing-types/test-strategy` |
| **Requirements Analysis** | Requirements decomposition, testability analysis | `skills/testing-types/requirements-analysis` |
| **Manual Testing** | Exploratory testing charters, test path suggestions | `skills/testing-types/manual-testing` |
| **Test Case Review** | Test case quality scoring, improvement suggestions | `skills/testing-types/test-case-reviewer` |
| **AI-Assisted Testing** | Intelligent test data generation, defect prediction | `skills/testing-types/ai-assisted-testing` |

> 💡 Each Skill has a corresponding English version with `-en` suffix in the directory name

## 🛠️ Usage by Tool

### Cursor

```bash
# Project-level
cp -r skills/testing-types/functional-testing-en /your/project/.cursor/skills/

# User-level
cp -r skills/testing-types/functional-testing-en ~/.cursor/skills/
```

### Claude Code

```bash
mkdir -p .claude/skills
cp -r skills/testing-types/functional-testing-en .claude/skills/
```

### Kiro

```bash
mkdir -p .kiro/skills
cp -r skills/testing-types/functional-testing-en .kiro/skills/
```

## 📂 Project Structure

```
ai-testing-assistant-skills/
├── skills/                           # Core skills library
│   ├── testing-workflows/            # 3 Workflow Skills
│   │   ├── daily-testing-workflow/   # Chinese version
│   │   ├── daily-testing-workflow-en/# English version
│   │   └── ...
│   └── testing-types/                # 15 Testing Type Skills
│       ├── functional-testing/       # Chinese version
│       ├── functional-testing-en/    # English version
│       └── ...
├── Reference/                        # Reference materials (optional)
│   ├── examples/                     # Code examples
│   └── templates/                    # Test templates
└── README.md
```

## 🎯 Skill Features

### 1. Intelligent Output Formats

Each Skill supports multiple output formats:
- 📝 **Markdown** - Default format, suitable for documentation
- 📊 **Excel** - Tab-separated, suitable for importing into test management tools
- 📋 **CSV** - Universal format
- 🔷 **JSON** - Structured data
- 🎯 **Jira/TestRail/Azure DevOps** - Direct adaptation to mainstream tools

### 2. Context Awareness

Skills can intelligently identify:
- 🔍 Project type (Web/Mobile/API/Desktop)
- 🎨 Tech stack (React/Vue/Angular/Flutter, etc.)
- 🧪 Testing frameworks (Jest/Vitest/Pytest/JUnit)

### 3. Bilingual Support

All Skills provide complete Chinese and English versions for global teams.

## 📊 Project Statistics

- ✅ **18 AI Testing Skills** (15 testing types + 3 workflows)
- ✅ **Bilingual Versions** (36 Skill directories total)
- ✅ **60,000+ Lines of Carefully Designed Prompts and Documentation**

## 🤝 Contributing

Welcome to contribute new Skills or improve existing ones! Please check [CONTRIBUTING.md](CONTRIBUTING.md).

## 📞 Related Links

- 📖 [Skills Index](skills-index.md) - View all Skills by category
- 🔗 [Skills Graph](skills-graph.md) - Skills dependency relationships
- ❓ [FAQ](FAQ.md) - Usage help

## License

This repository provides a testing assistant skills library designed specifically for AI tools.
