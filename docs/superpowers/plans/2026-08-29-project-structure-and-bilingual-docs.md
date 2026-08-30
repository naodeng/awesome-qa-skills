<div align="right"><strong>🇨🇳 中文</strong> | <a href="./2026-08-29-project-structure-and-bilingual-docs_EN.md">🇬🇧 English</a></div>

# 项目目录与双语文档实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在不调整 `skills/` 目录的前提下整理项目级目录，并让当前有效项目文档形成正确、中文优先、可双向切换的中英文镜像。

**Architecture:** 根目录只保留稳定入口，项目文档按 catalog、governance、generated、reviews 和 archive 分类。路径变更通过链接检查和双语清单校验保护，历史记录不回写为当前文档。

**Tech Stack:** Markdown、Python 3 标准库、Bash、Git

**Spec:** `docs/superpowers/specs/2026-08-29-project-structure-and-bilingual-docs-design.md`

## Global Constraints

- 不移动、不改名、不删除 `skills/` 下任何目录。
- 中文是当前项目文档的默认语言；英文使用 `_EN.md` 镜像并双向切换。
- Skill 内部文档不增加语言切换。
- 保留用户已有未提交脚本修改，不回退无关差异。

---

### Task 1: 扩展文档校验契约

**Files:**
- Modify: `scripts/check_docs_bilingual.py`
- Modify: `scripts/tests/test_check_docs_bilingual.py`

**Interfaces:**
- Consumes: `PROJECT_PAIRS` 与仓库根路径
- Produces: `check_relative_links(root: Path, paths: Iterable[str]) -> list[str]`

- [x] **Step 1:** 增加失败用例：迁移后的项目文档对缺失、相对链接断开时返回 finding。
- [x] **Step 2:** 运行 `python3 -m unittest scripts.tests.test_check_docs_bilingual -v`，确认新增用例先失败。
- [x] **Step 3:** 更新文档对路径并实现相对 Markdown 链接检查；忽略 URL、锚点、邮件和代码块内容。
- [x] **Step 4:** 重跑单元测试，确认全部通过。

### Task 2: 迁移项目级文件并修复引用

**Files:**
- Move: 根级 catalog、报告与草稿文件到设计指定目录
- Move: `docs/DOCUMENTATION_POLICY*`、`docs/QA_SKILLS_EVOLUTION_ROADMAP*`
- Modify: `README.md`, `README_EN.md`, `FAQ.md`, `FAQ_EN.md`
- Modify: `scripts/validate_agents_metadata.py`

**Interfaces:**
- Consumes: 设计文档中的迁移表
- Produces: 稳定的 `docs/catalog/`、`docs/governance/`、`docs/generated/` 和归档结构

- [x] **Step 1:** 使用可追踪移动建立新目录结构。
- [x] **Step 2:** 更新当前文档中的相对链接与 README 文档地图。
- [x] **Step 3:** 将 metadata 校验报告默认输出调整为 `docs/generated/skills-metadata-report.md`，保留脚本现有其他修改。
- [x] **Step 4:** 扫描旧路径，区分需要修复的当前引用与只作历史记录的命令文本。

### Task 3: 审查并修正文档双语内容

**Files:**
- Modify: `CONTRIBUTING.md`, `CONTRIBUTING_EN.md`
- Modify: `FAQ.md`, `FAQ_EN.md`
- Modify: `README.md`, `README_EN.md`
- Modify: `docs/catalog/skills-index.md`, `docs/catalog/skills-index_EN.md`
- Modify: `docs/governance/*.md`
- Create or Modify: current project-document English mirrors found missing during audit

**Interfaces:**
- Consumes: 当前 156 个 Skill、65 个 testing type 的验证事实
- Produces: 结构一致、数字正确、中文优先、双向切换的当前文档集

- [x] **Step 1:** 去除中文贡献指南和 FAQ 中重复嵌入的完整英文正文，保留中文版本与切换入口。
- [x] **Step 2:** 对比中英文标题结构、表格条目、数字和关键结论，修复差异。
- [x] **Step 3:** 核对所有当前项目文档顶部切换链接与返回链接。
- [x] **Step 4:** 更新双语文档治理策略中的新目录和排除边界。

### Task 4: 全量验证与交付

**Files:**
- Modify: this plan pair to mark completed steps

**Interfaces:**
- Consumes: Tasks 1–3 的最终工作树
- Produces: 可提交的验证证据

- [x] **Step 1:** 比较 `HEAD` 基线与当前 `skills/` 目录集合，确认没有路径变化。
- [x] **Step 2:** 运行 `python3 -m unittest scripts.tests.test_check_docs_bilingual -v`。
- [x] **Step 3:** 运行 `bash scripts/check_skills_quality.sh` 与 `git diff --check`。
- [x] **Step 4:** 审查暂存内容，排除用户无关修改。
- [x] **Step 5:** 使用 Conventional Commit 提交、推送 `explore` 并核对 PR #4。
