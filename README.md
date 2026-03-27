<div align="right"><strong>🇨🇳中文</strong> | <strong><a href="./README_EN.md">🇬🇧English</a></strong></div>

# AI 测试辅助技能合集

这是一个按语言分区整理好的 AI 测试技能库，适合放到 Codex、Cursor、Claude Code、Kiro、OpenCode、Trae 等工具里直接使用。

在线访问地址：https://inaodeng.com/qaskills/

## 你会在这里得到什么

- 中文与英文双版本技能
- 4 个工作流技能
- 25 个测试类型技能
- 可直接复制到常见 AI 工具中使用

## 核心目录

- 中文技能：`skills/zh`
- 英文技能：`skills/en`
- 工作流技能：`testing-workflows`
- 测试类型技能：`testing-types`

## 5 分钟开始

### 1. 克隆项目

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. 复制一个技能到你的 AI 工具

```bash
# 例：复制中文功能测试技能到 Cursor
cp -r skills/zh/testing-types/functional-testing ~/.cursor/skills/

# 例：复制英文日常测试工作流到 Cursor
cp -r skills/en/testing-workflows/daily-testing-workflow ~/.cursor/skills/
```

### 3. 在 AI 工具里调用

```text
@skill functional-testing
帮我为用户登录功能生成测试用例
```

## 推荐技能入口（中文）

### 工作流技能

| 中文名称 | 目录 |
| --- | --- |
| 日常测试工作流程 | `skills/zh/testing-workflows/daily-testing-workflow` |
| 迭代测试工作流程 | `skills/zh/testing-workflows/sprint-testing-workflow` |
| 发布测试工作流程 | `skills/zh/testing-workflows/release-testing-workflow` |
| 测试技能路由 | `skills/zh/testing-workflows/discover-testing` |

### 测试类型技能

| 中文名称 | 目录 |
| --- | --- |
| 功能测试 | `skills/zh/testing-types/functional-testing` |
| API 测试 | `skills/zh/testing-types/api-testing` |
| 自动化测试 | `skills/zh/testing-types/automation-testing` |
| 手动/探索性测试 | `skills/zh/testing-types/manual-testing` |
| 性能测试 | `skills/zh/testing-types/performance-testing` |
| 安全测试 | `skills/zh/testing-types/security-testing` |
| 移动端测试 | `skills/zh/testing-types/mobile-testing` |
| 可访问性测试 | `skills/zh/testing-types/accessibility-testing` |
| 缺陷上报 | `skills/zh/testing-types/bug-reporting` |
| 测试用例编写 | `skills/zh/testing-types/test-case-writing` |
| 测试用例评审 | `skills/zh/testing-types/test-case-reviewer` |
| 测试报告 | `skills/zh/testing-types/test-reporting` |
| 测试策略 | `skills/zh/testing-types/test-strategy` |
| 需求分析 | `skills/zh/testing-types/requirements-analysis` |
| AI 辅助测试 | `skills/zh/testing-types/ai-assisted-testing` |
| API 测试（Bruno） | `skills/zh/testing-types/api-test-bruno` |
| API 测试（Pytest） | `skills/zh/testing-types/api-test-pytest` |
| API 测试（Rest Assured） | `skills/zh/testing-types/api-test-restassure` |
| API 测试（Supertest） | `skills/zh/testing-types/api-test-supertest` |
| 性能测试（k6） | `skills/zh/testing-types/performance-test-k6` |
| 性能测试（Gatling） | `skills/zh/testing-types/performance-test-gatling` |
| 需求分析增强版 | `skills/zh/testing-types/requirements-analysis-plus` |
| 测试用例评审增强版 | `skills/zh/testing-types/test-case-reviewer-plus` |
| 测试策略增强版 | `skills/zh/testing-types/test-strategy-plus` |
| 测试用例编写增强版 | `skills/zh/testing-types/testcase-writer-plus` |

> 对应英文版本位于 `skills/en/...`，目录名和技能名保持一致。

## 一键安装

```bash
# macOS / Linux
bash ./install-skills-mac.sh --tool all --lang all

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File .\install-skills-windows.ps1 -Tool all -Lang all
```

更多说明见：[scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)

如果你想直接安装某一个 skill，也可以用已经生成好的分目录脚本，例如：

```bash
# 安装中文 functional-testing 到 Codex
bash installers/zh/functional-testing/mac/codex.sh
```

## 项目结构

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

## 规则说明

- 语言通过 `skills/zh` 和 `skills/en` 区分
- 每个 skill 下的 prompt 统一放在 `prompts/`
- 英文 prompt 文件名不带 `_EN`
- 中英文 skill 名称保持一致，不再使用 `-en`

## 常用文档

- [skills-index.md](skills-index.md)：技能总索引
- [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md)：目录规则说明
- [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)：安装说明
- [FAQ.md](FAQ.md)：常见问题

## 许可证

本仓库提供面向 AI 工具的测试技能库，便于团队直接复用和扩展。
