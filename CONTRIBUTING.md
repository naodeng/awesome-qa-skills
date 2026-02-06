# 贡献指南 | Contributing Guide

[English](#english) | [中文](#中文)

---

## 中文

感谢您对 Awesome QA Skills 项目的关注！我们欢迎所有形式的贡献。

### 如何贡献

#### 1. 报告问题（Bug Report）

如果您发现了 bug 或有改进建议：

1. 先搜索 [Issues](https://github.com/your-repo/awesome-qa-skills/issues) 确认问题未被报告
2. 使用 Issue 模板创建新的 Issue
3. 提供详细的问题描述、复现步骤和环境信息

#### 2. 提交功能请求（Feature Request）

如果您有新功能的想法：

1. 先搜索现有的 Feature Requests
2. 创建新的 Issue，标签选择 `enhancement`
3. 详细描述功能需求、使用场景和预期效果

#### 3. 贡献代码（Pull Request）

##### 3.1 准备工作

```bash
# Fork 项目到您的 GitHub 账号

# Clone 您的 fork
git clone https://github.com/YOUR_USERNAME/awesome-qa-skills.git
cd awesome-qa-skills

# 添加上游仓库
git remote add upstream https://github.com/original-repo/awesome-qa-skills.git

# 创建新分支
git checkout -b feature/your-feature-name
```

##### 3.2 开发规范

**目录结构规范**：
```
skills/
├── testing-types/
│   └── your-skill/
│       ├── SKILL.md              # Skill 元数据和说明
│       ├── quick-start.md        # 快速开始指南
│       ├── output-formats.md     # 输出格式说明
│       ├── prompts/              # 提示词目录
│       │   ├── basic.md          # 基础层提示词
│       │   ├── intermediate.md   # 中级层提示词
│       │   └── advanced.md       # 高级层提示词
│       ├── examples/             # 代码示例
│       └── tests/                # 测试用例
```

**SKILL.md 元数据规范**：
```yaml
---
name: your-skill-name
version: 1.0.0
last-updated: 2024-02-06
description: 简短描述（一句话）
category: testing-types | testing-workflows | advanced
level: beginner | intermediate | expert
tags: [tag1, tag2, tag3]
dependencies: []
recommended-with: [skill1, skill2]
context-aware: true | false
context-patterns:
  project-types: [web, mobile, api, desktop]
  frameworks: [react, vue, angular]
  test-frameworks: [jest, vitest, playwright]
output-formats: [markdown, excel, csv, json]
examples-count: 3
has-tutorial: true
has-troubleshooting: true
---
```

**代码示例规范**：
- 所有代码示例必须可运行
- 包含必要的注释和说明
- 提供完整的依赖信息
- 遵循语言的最佳实践

**文档规范**：
- 使用 Markdown 格式
- 中英文版本保持同步
- 链接使用相对路径
- 代码块指定语言

##### 3.3 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type 类型**：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 构建/工具相关

**示例**：
```
feat(functional-testing): 添加 Playwright 代码示例

- 添加登录功能测试示例
- 添加表单提交测试示例
- 更新 troubleshooting 章节

Closes #123
```

##### 3.4 测试

提交前请确保：

```bash
# 运行质量检查
./tools/quality-check.sh

# 运行中英文同步检查
./tools/sync-check.sh

# 验证代码示例
./tools/example-validator.sh

# 运行测试
./tests/run-all-tests.sh
```

##### 3.5 提交 Pull Request

1. 推送到您的 fork：
```bash
git push origin feature/your-feature-name
```

2. 在 GitHub 上创建 Pull Request
3. 填写 PR 模板，详细描述变更内容
4. 等待 CI 检查通过
5. 等待 Code Review

#### 4. 贡献文档

文档贡献同样重要！您可以：

- 修正拼写错误和语法问题
- 改进文档结构和可读性
- 添加示例和教程
- 翻译文档到其他语言

#### 5. 贡献代码示例

我们欢迎更多真实的代码示例：

1. 确保示例可运行
2. 添加详细注释
3. 提供依赖信息
4. 说明使用场景

### 创建新 Skill

使用 Skill 生成器快速创建新 skill：

```bash
./tools/skill-generator.sh \
  --name your-skill-name \
  --category testing-types \
  --level intermediate \
  --language zh
```

生成器会创建完整的目录结构和模板文件。

### 质量检查清单

提交前请检查：

- [ ] 代码/文档符合项目规范
- [ ] 所有代码示例可运行
- [ ] 中英文版本同步（如适用）
- [ ] 更新了 CHANGELOG.md
- [ ] 添加了必要的测试
- [ ] 通过了所有 CI 检查
- [ ] 文档链接有效
- [ ] 没有拼写错误

### Code Review 流程

1. **自动检查**：CI 会自动运行测试和质量检查
2. **人工审查**：维护者会审查代码和文档
3. **反馈**：根据反馈进行修改
4. **合并**：审查通过后合并到主分支

### 行为准则

- 尊重所有贡献者
- 保持友好和专业
- 接受建设性批评
- 关注项目目标

### 许可证

贡献的代码将采用项目的许可证（MIT License）。

### 获取帮助

如有疑问，可以：

1. 查看 [FAQ.md](FAQ.md)
2. 在 Issue 中提问
3. 加入社区讨论

---

## English

Thank you for your interest in contributing to Awesome QA Skills! We welcome all forms of contributions.

### How to Contribute

#### 1. Report Issues

If you find a bug or have suggestions:

1. Search [Issues](https://github.com/your-repo/awesome-qa-skills/issues) first
2. Create a new Issue using the template
3. Provide detailed description, reproduction steps, and environment info

#### 2. Feature Requests

If you have ideas for new features:

1. Search existing Feature Requests
2. Create a new Issue with `enhancement` label
3. Describe the feature, use cases, and expected behavior

#### 3. Code Contributions

##### 3.1 Setup

```bash
# Fork the project to your GitHub account

# Clone your fork
git clone https://github.com/YOUR_USERNAME/awesome-qa-skills.git
cd awesome-qa-skills

# Add upstream remote
git remote add upstream https://github.com/original-repo/awesome-qa-skills.git

# Create a new branch
git checkout -b feature/your-feature-name
```

##### 3.2 Development Standards

**Directory Structure**:
```
skills/
├── testing-types/
│   └── your-skill/
│       ├── SKILL.md              # Skill metadata and description
│       ├── quick-start.md        # Quick start guide
│       ├── output-formats.md     # Output format documentation
│       ├── prompts/              # Prompts directory
│       │   ├── basic.md          # Basic level prompts
│       │   ├── intermediate.md   # Intermediate level prompts
│       │   └── advanced.md       # Advanced level prompts
│       ├── examples/             # Code examples
│       └── tests/                # Test cases
```

**SKILL.md Metadata**:
```yaml
---
name: your-skill-name
version: 1.0.0
last-updated: 2024-02-06
description: Brief description (one sentence)
category: testing-types | testing-workflows | advanced
level: beginner | intermediate | expert
tags: [tag1, tag2, tag3]
dependencies: []
recommended-with: [skill1, skill2]
context-aware: true | false
context-patterns:
  project-types: [web, mobile, api, desktop]
  frameworks: [react, vue, angular]
  test-frameworks: [jest, vitest, playwright]
output-formats: [markdown, excel, csv, json]
examples-count: 3
has-tutorial: true
has-troubleshooting: true
---
```

**Code Example Standards**:
- All examples must be runnable
- Include necessary comments
- Provide complete dependency information
- Follow language best practices

**Documentation Standards**:
- Use Markdown format
- Keep Chinese and English versions in sync
- Use relative paths for links
- Specify language for code blocks

##### 3.3 Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation update
- `style`: Code formatting (no functional change)
- `refactor`: Refactoring
- `test`: Test related
- `chore`: Build/tooling related

**Example**:
```
feat(functional-testing): add Playwright code examples

- Add login functionality test example
- Add form submission test example
- Update troubleshooting section

Closes #123
```

##### 3.4 Testing

Before submitting, ensure:

```bash
# Run quality checks
./tools/quality-check.sh

# Run sync checks
./tools/sync-check.sh

# Validate code examples
./tools/example-validator.sh

# Run tests
./tests/run-all-tests.sh
```

##### 3.5 Submit Pull Request

1. Push to your fork:
```bash
git push origin feature/your-feature-name
```

2. Create Pull Request on GitHub
3. Fill in the PR template
4. Wait for CI checks to pass
5. Wait for Code Review

#### 4. Documentation Contributions

Documentation contributions are equally important! You can:

- Fix typos and grammar
- Improve structure and readability
- Add examples and tutorials
- Translate documentation

#### 5. Code Example Contributions

We welcome more real-world code examples:

1. Ensure examples are runnable
2. Add detailed comments
3. Provide dependency information
4. Explain use cases

### Creating New Skills

Use the Skill generator to quickly create a new skill:

```bash
./tools/skill-generator.sh \
  --name your-skill-name \
  --category testing-types \
  --level intermediate \
  --language en
```

The generator creates complete directory structure and template files.

### Quality Checklist

Before submitting, check:

- [ ] Code/docs follow project standards
- [ ] All code examples are runnable
- [ ] Chinese and English versions are in sync (if applicable)
- [ ] Updated CHANGELOG.md
- [ ] Added necessary tests
- [ ] Passed all CI checks
- [ ] Documentation links are valid
- [ ] No spelling errors

### Code Review Process

1. **Automated Checks**: CI runs tests and quality checks
2. **Manual Review**: Maintainers review code and docs
3. **Feedback**: Make changes based on feedback
4. **Merge**: Merge to main branch after approval

### Code of Conduct

- Respect all contributors
- Be friendly and professional
- Accept constructive criticism
- Focus on project goals

### License

Contributed code will be licensed under the project's license (MIT License).

### Getting Help

If you have questions:

1. Check [FAQ.md](FAQ.md)
2. Ask in Issues
3. Join community discussions

---

## 感谢 | Thank You

感谢您的贡献！每一个贡献都让这个项目变得更好。

Thank you for your contributions! Every contribution makes this project better.
