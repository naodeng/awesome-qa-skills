<div align="right"><strong>🇨🇳中文</strong> | <strong><a href="./README_EN.md">🇬🇧English</a></strong></div>

# AI 测试辅助技能合集

这是一个按语言分区整理好的 AI 测试技能库，适合放到 Cursor、Claude Code、Kiro 等工具里直接使用。

## 当前结构

- 中文技能：`skills/zh`
- 英文技能：`skills/en`
- 工作流技能：`testing-workflows`
- 测试类型技能：`testing-types`

现在仓库里包含：
- 4 个工作流技能
- 25 个测试类型技能
- 中英文双版本

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

## 推荐入口

### 中文工作流技能

- `skills/zh/testing-workflows/daily-testing-workflow`
- `skills/zh/testing-workflows/sprint-testing-workflow`
- `skills/zh/testing-workflows/release-testing-workflow`
- `skills/zh/testing-workflows/discover-testing`

### 中文测试类型技能

- `skills/zh/testing-types/functional-testing`
- `skills/zh/testing-types/api-testing`
- `skills/zh/testing-types/automation-testing`
- `skills/zh/testing-types/manual-testing`
- `skills/zh/testing-types/performance-testing`
- `skills/zh/testing-types/security-testing`
- `skills/zh/testing-types/mobile-testing`
- `skills/zh/testing-types/accessibility-testing`
- `skills/zh/testing-types/bug-reporting`
- `skills/zh/testing-types/test-case-writing`
- `skills/zh/testing-types/test-case-reviewer`
- `skills/zh/testing-types/test-reporting`
- `skills/zh/testing-types/test-strategy`
- `skills/zh/testing-types/requirements-analysis`
- `skills/zh/testing-types/ai-assisted-testing`

### 中文增强型技能

- `skills/zh/testing-types/api-test-bruno`
- `skills/zh/testing-types/api-test-pytest`
- `skills/zh/testing-types/api-test-restassure`
- `skills/zh/testing-types/api-test-supertest`
- `skills/zh/testing-types/performance-test-k6`
- `skills/zh/testing-types/performance-test-gatling`
- `skills/zh/testing-types/requirements-analysis-plus`
- `skills/zh/testing-types/test-case-reviewer-plus`
- `skills/zh/testing-types/test-strategy-plus`
- `skills/zh/testing-types/testcase-writer-plus`

> 对应英文版本位于 `skills/en/...`，目录名和技能名都与中文保持一致。

## 一键安装

```bash
# macOS / Linux
bash scripts/install-skills-mac.sh --tool all --lang all

# Windows PowerShell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool all -Lang all
```

更多说明见：[scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)

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
