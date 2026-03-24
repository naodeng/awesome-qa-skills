<div align="right"><strong>🇨🇳中文</strong> | <strong><a href="./README_EN.md">🇬🇧English</a></strong></div>

# AI 测试辅助技能合集 (AI Testing Assistant Skills)

本仓库提供一套**专为 AI 编码助手设计的测试技能库（Skills）**，让 **Cursor**、**Claude Code**、**Kiro** 等 AI 工具成为你的专业测试助手。

## 🎯 项目核心

提供 **18 个精心设计的测试 Skills**：
- ✅ **15 个测试类型 Skills** - 覆盖功能、API、自动化、性能、安全等全方位测试
- ✅ **3 个工作流 Skills** - 日常测试、Sprint 测试、发布测试完整流程

每个 Skill 都包含：
- 📋 结构化的提示词（Prompts）
- 🎯 最佳实践和使用指南
- 🔄 智能输出格式支持
- 🌐 中英文双语版本

> 目录说明：核心技能目录仍使用 `-en` 区分英文版本（如 `functional-testing-en`）。
> `skills/skills-en` 是英文浏览视图，名称已去掉 `-en`，用于按语言浏览，不是新的核心目录。

## 🚀 5 分钟快速开始

### 1. 克隆项目

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. 安装 Skill 到 AI 工具

```bash
# Cursor 示例 - 复制功能测试 skill（中文）
cp -r skills/testing-types/functional-testing ~/.cursor/skills/

# 或复制日常测试工作流（中文）
cp -r skills/testing-workflows/daily-testing-workflow ~/.cursor/skills/
```

### 3. 在 AI 工具中使用

```
@skill functional-testing
帮我为用户登录功能生成测试用例
```

AI 将自动：
- 📋 分析需求并识别测试场景
- ✅ 生成结构化的测试用例
- 🔍 识别边界条件和异常场景
- 📊 提供测试数据建议

## 📦 Skills 列表

### 🔄 三个工作流 Skills

| Skill | 说明 | 目录 |
|-------|------|------|
| **日常测试工作流** | 每日测试计划、用例编写、缺陷分析、测试报告 | `skills/testing-workflows/daily-testing-workflow` |
| **Sprint 测试工作流** | Sprint 规划、回归测试优先级、风险评估 | `skills/testing-workflows/sprint-testing-workflow` |
| **发布测试工作流** | 发布检查清单、Go/No-Go 决策、回滚计划 | `skills/testing-workflows/release-testing-workflow` |

### 🧪 十五个测试类型 Skills

| Skill | AI 辅助能力 | 目录 |
|-------|------------|------|
| **功能测试** | 自动识别测试场景、生成测试用例、边界值分析 | `skills/testing-types/functional-testing` |
| **API 测试** | 从 API 文档生成测试用例、自动化脚本生成 | `skills/testing-types/api-testing` |
| **自动化测试** | POM 模式代码生成、数据驱动测试设计 | `skills/testing-types/automation-testing` |
| **性能测试** | 性能场景设计、负载模型生成、瓶颈分析 | `skills/testing-types/performance-testing` |
| **安全测试** | OWASP Top 10 检查清单、安全测试用例生成 | `skills/testing-types/security-testing` |
| **移动端测试** | 跨平台测试策略、兼容性矩阵生成 | `skills/testing-types/mobile-testing` |
| **可访问性测试** | WCAG 合规检查、无障碍测试用例 | `skills/testing-types/accessibility-testing` |
| **缺陷上报** | 智能缺陷分类、根因分析建议 | `skills/testing-types/bug-reporting` |
| **测试用例编写** | 用例模板生成、测试数据建议 | `skills/testing-types/test-case-writing` |
| **测试报告** | 自动化报告生成、数据可视化建议 | `skills/testing-types/test-reporting` |
| **测试策略** | 风险评估、测试范围建议 | `skills/testing-types/test-strategy` |
| **需求分析** | 需求拆解、可测性分析 | `skills/testing-types/requirements-analysis` |
| **手动测试** | 探索性测试章程、测试路径建议 | `skills/testing-types/manual-testing` |
| **测试用例评审** | 用例质量评分、改进建议 | `skills/testing-types/test-case-reviewer` |
| **AI 辅助测试** | 智能测试数据生成、缺陷预测 | `skills/testing-types/ai-assisted-testing` |

> 💡 每个 Skill 都有对应的英文版本，目录名后缀为 `-en`

## 🛠️ 各工具使用方式

### 一键安装（推荐）

```bash
# macOS / Linux：安装到全部工具（中英文）
bash scripts/install-skills-mac.sh --tool all --lang all

# Windows PowerShell：安装到全部工具（中英文）
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills-windows.ps1 -Tool all -Lang all
```

更多参数说明见：[scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)

### Cursor

```bash
# 项目级
cp -r skills/testing-types/functional-testing /你的项目/.cursor/skills/

# 用户级
cp -r skills/testing-types/functional-testing ~/.cursor/skills/
```

### Claude Code

```bash
mkdir -p .claude/skills
cp -r skills/testing-types/functional-testing .claude/skills/
```

### Kiro

```bash
mkdir -p .kiro/skills
cp -r skills/testing-types/functional-testing .kiro/skills/
```

## 📂 项目结构

```
ai-testing-assistant-skills/
├── skills/                           # 核心技能库
│   ├── testing-workflows/            # 3 个工作流 Skills
│   │   ├── daily-testing-workflow/   # 中文版
│   │   ├── daily-testing-workflow-en/# 英文版
│   │   └── ...
│   └── testing-types/                # 15 个测试类型 Skills
│       ├── functional-testing/       # 中文版
│       ├── functional-testing-en/    # 英文版
│       └── ...
│   ├── skills-zh/                    # 中文分区视图（软链接）
│   ├── skills-en/                    # 英文分区视图（软链接，名称不带 -en）
│   └── release/                      # 发布打包目录（非软链接，脚本生成）
├── Reference/                        # 参考资料（可选）
│   ├── examples/                     # 代码示例
│   └── templates/                    # 测试模板
└── README.md
```

## 🗂️ 目录选择建议

- 日常开发与维护：使用 `skills/testing-types` 与 `skills/testing-workflows`
- 按语言浏览：使用 `skills/skills-zh` 与 `skills/skills-en`
- 对外发布/分发：使用 `skills/release`（由 `scripts/build_release_skill_dirs.py` 生成）

目录治理与一键整理见：`skills/DIRECTORY_GUIDE.md`（可运行 `python3 scripts/organize_project_dirs.py` 自动修复/重建目录映射）。

## 🎯 Skill 特性

### 1. 智能输出格式

每个 Skill 支持多种输出格式：
- 📝 **Markdown** - 默认格式，适合文档
- 📊 **Excel** - 制表符分隔，适合导入测试管理工具
- 📋 **CSV** - 通用格式
- 🔷 **JSON** - 结构化数据
- 🎯 **Jira/TestRail/Azure DevOps** - 直接适配主流工具

### 2. 上下文感知

Skills 能够智能识别：
- 🔍 项目类型（Web/Mobile/API/Desktop）
- 🎨 技术栈（React/Vue/Angular/Flutter 等）
- 🧪 测试框架（Jest/Vitest/Pytest/JUnit）

### 3. 中英文双语

所有 Skills 提供完整的中英文版本，适配全球团队。

## 📊 项目统计

- ✅ **18 个 AI 测试 Skills**（15 个测试类型 + 3 个工作流）
- ✅ **中英文双版本**（共 36 个 Skill 目录）
- ✅ **60,000+ 行精心设计的提示词和文档**

## 🤝 贡献

欢迎贡献新的 Skills 或改进现有 Skills！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 📞 相关链接

- 📖 [Skills 索引](skills-index.md) - 按类别查看所有 Skills
- 🔗 [Skills 关系图](skills-graph.md) - Skills 依赖关系
- ❓ [常见问题](FAQ.md) - 使用帮助

## 许可证

本仓库提供专为 AI 工具设计的测试辅助技能库。
