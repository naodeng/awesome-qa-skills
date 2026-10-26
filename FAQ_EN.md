<div align="right"><a href="./FAQ.md">🇨🇳 中文</a> | <strong>🇬🇧 English</strong></div>

# Frequently Asked Questions

## Project and Skills

### 1. What does this project contain?

A bilingual QA Agent Skills library for AI coding agents. Each language has 165 Skills: 10 testing workflows, 150 testing types, and 5 Skill Engineering packages, for 330 Skill directories total. Browse the [complete index](docs/catalog/skills-index_EN.md).

### 2. Which AI tools are supported?

See the README's [supported tools and installation methods](README_EN.md#supported-ai-tools). Actual compatibility depends on each tool's Skill discovery behavior; the project does not label unverified tool versions as tested.

### 3. How do I find the right Skill?

Start with the [task-based Skill navigation](README_EN.md#find-a-skill-by-task) or use the `discover-testing` routing Skill. The [complete index](docs/catalog/skills-index_EN.md) lists all names and purposes.

### 4. What is the difference between the Chinese and English Skills?

Chinese and English Skills share canonical names and live under `skills/zh/` and `skills/en/`. Their content is maintained by language. Install one language per tool target by default to avoid same-name directory conflicts.

## Installation and use

### 5. How do I install a Skill?

With the Agent Skills CLI, install an English Skill from the repository entry point. Select `skills/zh` explicitly for a Chinese Skill:

```bash
npx skills add naodeng/awesome-qa-skills --skill functional-testing
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing
```

See the [installation guide](scripts/INSTALL_SKILLS_EN.md) for the CLI, macOS/Linux and Windows installers, shortcuts, and manual copy.

### 6. How do I use an installed Skill?

Tools that discover Agent Skills automatically can receive a natural-language task. Some tools also support explicit syntax such as `@skill functional-testing`; syntax varies by tool. See the README's [supported tools](README_EN.md#supported-ai-tools).

### 7. Do multiple Skills run together automatically?

No automatic orchestration is provided. You can use Skills sequentially as needed. The [Composition routes](docs/catalog/skills-composition_EN.md) suggest task paths and primary/optional Skills for navigation and selection.

### 8. Does a Skill run tests or guarantee executable code?

No. A Skill can help design tests or draft scripts; execution and successful results depend on the Agent, tools, and target project. Review generated code and record evidence from actual runs.

### 9. Can I request Excel, CSV, or another output format?

Markdown is the default. Support for Excel, CSV, JSON, and other formats depends on the specific Skill. Check its `output-formats.md` or state the required format in your request.

### 10. What should I check if installation or discovery fails?

Check the language source, the target tool's Skills directory, the Skill's `SKILL.md`, and whether the other language version with the same name is already installed. For Chinese CLI installs, select `skills/zh`. See the [installation guide](scripts/INSTALL_SKILLS_EN.md) for troubleshooting.

### 11. Are community-recommended Skills part of this project?

No. The README's [community list](README_EN.md#community-recommended-external-skills) helps you discover Skills maintained by external projects. Check each upstream source for its license, version, dependencies, and compatibility; inclusion does not mean this repository has runtime-evaluated it.

## Contributing and license

### 12. How do I add or update a Skill?

Read the [contribution guide](CONTRIBUTING_EN.md) and [Skill Authoring Guide](skills/SKILL_AUTHORING_EN.md). Skill changes must maintain bilingual directories, metadata, and Eval cases, and should pass the repository quality checks.

### 13. How do I report a problem or request a Skill?

Search [existing Issues](https://github.com/naodeng/awesome-qa-skills/issues) first. If there is no matching report, open an Issue with reproduction steps, use case, and expected result.

### 14. What license does the project use?

This repository uses the [PolyForm Noncommercial License 1.0.0](LICENSE), which permits noncommercial use only. Community-recommended Skills retain their upstream licenses.

---

**Last updated: 2026-10-26**
