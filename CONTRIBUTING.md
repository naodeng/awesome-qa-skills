<div align="right"><strong>🇨🇳 中文</strong> | <a href="./CONTRIBUTING_EN.md">🇬🇧 English</a></div>

# 贡献指南 | Contributing Guide

[English](#english) | [中文](#中文)

---

## 中文

感谢您对 AI 测试辅助技能合集项目的关注！我们欢迎所有形式的贡献。

### 如何贡献

#### 1. 报告问题（Bug Report）

如果您发现了 bug 或有改进建议：

1. 先搜索 [Issues](https://github.com/naodeng/awesome-qa-skills/issues) 确认问题未被报告
2. 创建新的 Issue
3. 提供详细的问题描述、复现步骤和环境信息

#### 2. 提交功能请求（Feature Request）

如果您有新 Skill 的想法：

1. 先搜索现有的 Feature Requests
2. 创建新的 Issue，标签选择 `enhancement`
3. 详细描述 Skill 需求、使用场景和预期效果

#### 3. 贡献新 Skill

##### 3.1 Skill 目录结构

```
skills/zh/testing-types/your-skill/
├── SKILL.md              # Skill 元数据和说明
├── quick-start.md        # 快速开始指南
├── output-formats.md     # 输出格式说明
├── prompts/              # 提示词目录
│   └── your-skill.md     # 主提示词
├── agents/openai.yaml    # OpenAI / Codex 元数据
├── evals/                # skill-up 评测用例
└── references/           # 深度参考资料（可选）
```

##### 3.2 SKILL.md 元数据规范

```yaml
---
name: your-skill-name
version: 1.0.0
last-updated: 2024-02-06
description: 简短描述（一句话）
category: testing-types | testing-workflows
level: beginner | intermediate | advanced
tags: [tag1, tag2, tag3]
dependencies: []
recommended-with: [skill1, skill2]
output-formats: [markdown, excel, csv, json]
---
```

##### 3.3 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

<body>
```

**Type 类型**：
- `feat`: 新 Skill 或新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `refactor`: 重构

**示例**：
```
feat(functional-testing): 添加边界值测试提示词

- 添加边界值分析章节
- 更新 quick-start.md
- 优化输出格式

Closes #123
```

#### 4. 贡献文档

文档贡献同样重要！您可以：

- 修正拼写错误和语法问题
- 改进文档结构和可读性
- 添加使用示例
- 翻译文档到其他语言

### 质量检查清单

提交前请检查：

- [ ] Skill 符合目录结构规范（见 [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md)、[skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)）
- [ ] `SKILL.md` 的 `name` / `description`（含 `Use this skill when...` 与触发词）完整
- [ ] 中英文版本同步（目录名一致；除非明确只要单语）
- [ ] 提示词清晰易懂；无真实 token/密钥
- [ ] 文档链接有效；不跨 skill 硬链内部文件
- [ ] **若改了 skill / evals：** 本地通过 `bash scripts/check_skills_quality.sh`（含 `skill-up validate`；需已安装 [skill-up](https://github.com/alibaba/skill-up)）
- [ ] 推荐用 `bash scripts/run_skill_eval.sh <skill>/evals/eval.yaml` 实跑关键 case（产物写入 `.skill-up-workspaces/`）

```bash
# 改 skill 后最低要求
bash scripts/check_skills_quality.sh

# 可选：安装 skill-up / skill-upper 后实跑与演进
curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash
# Codex：npx skills add https://github.com/alibaba/skill-up/tree/main/skills/skill-upper -g -a codex -y
bash scripts/run_skill_eval.sh skills/zh/testing-types/functional-testing/evals/eval.yaml --include-case-name "basic-success"
```

### 行为准则

- 尊重所有贡献者
- 保持友好和专业
- 接受建设性批评
- 关注项目目标：提供高质量的测试 Skills

### 许可证

贡献的内容将采用项目的许可证。

### 获取帮助

如有疑问，可以：

1. 查看 [FAQ.md](FAQ.md)
2. 在 Issue 中提问
3. 查看现有 Skills 作为参考

---

## English

Thank you for your interest in contributing to AI Testing Assistant Skills! We welcome all forms of contributions.

### How to Contribute

#### 1. Report Issues

If you find a bug or have suggestions:

1. Search [Issues](https://github.com/naodeng/awesome-qa-skills/issues) first
2. Create a new Issue
3. Provide detailed description, reproduction steps, and environment info

#### 2. Feature Requests

If you have ideas for new Skills:

1. Search existing Feature Requests
2. Create a new Issue with `enhancement` label
3. Describe the Skill requirements, use cases, and expected behavior

#### 3. Contribute New Skills

##### 3.1 Skill Directory Structure

```
skills/en/testing-types/your-skill/
├── SKILL.md              # Skill metadata and description
├── quick-start.md        # Quick start guide
├── output-formats.md     # Output format documentation
├── prompts/              # Prompts directory
│   └── your-skill.md     # Primary prompt
├── agents/openai.yaml    # OpenAI / Codex metadata
├── evals/                # skill-up eval cases
└── references/           # Deep reference materials (optional)
```

##### 3.2 SKILL.md Metadata Standards

```yaml
---
name: your-skill-name
version: 1.0.0
last-updated: 2024-02-06
description: Brief description (one sentence)
category: testing-types | testing-workflows
level: beginner | intermediate | advanced
tags: [tag1, tag2, tag3]
dependencies: []
recommended-with: [skill1, skill2]
output-formats: [markdown, excel, csv, json]
---
```

##### 3.3 Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>
```

**Types**:
- `feat`: New Skill or feature
- `fix`: Bug fix
- `docs`: Documentation update
- `refactor`: Refactoring

**Example**:
```
feat(functional-testing): add boundary value testing prompts

- Add boundary value analysis section
- Update quick-start.md
- Optimize output formats

Closes #123
```

#### 4. Documentation Contributions

Documentation contributions are equally important! You can:

- Fix typos and grammar
- Improve structure and readability
- Add usage examples
- Translate documentation

### Quality Checklist

Before submitting, check:

- [ ] Skill follows [DIRECTORY_GUIDE](skills/DIRECTORY_GUIDE.md) / [SKILL_AUTHORING](skills/SKILL_AUTHORING.md)
- [ ] `SKILL.md` `name` / `description` (`Use this skill when...` + triggers) are complete
- [ ] zh/en stay in sync (same directory names) unless single-language is intentional
- [ ] Prompts are clear; no real tokens/secrets
- [ ] Links are valid; no hard links into other skills' internal files
- [ ] **If you touched a skill / evals:** `bash scripts/check_skills_quality.sh` passes (includes `skill-up validate` when skill-up is installed)
- [ ] Prefer `bash scripts/run_skill_eval.sh <skill>/evals/eval.yaml` for real runs (outputs go under `.skill-up-workspaces/`)

### Code of Conduct

- Respect all contributors
- Be friendly and professional
- Accept constructive criticism
- Focus on project goals: providing high-quality testing Skills

### License

Contributed content will be licensed under the project's license.

### Getting Help

If you have questions:

1. Check [FAQ.md](FAQ.md)
2. Ask in Issues
3. Review existing Skills as reference

---

## 感谢 | Thank You

感谢您的贡献！每一个贡献都让这个项目变得更好。

Thank you for your contributions! Every contribution makes this project better.
