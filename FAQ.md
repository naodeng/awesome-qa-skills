# 常见问题解答 | FAQ

[English](#english-faq) | [中文](#中文-faq)

---

## 中文 FAQ

### 基础问题

#### 1. 什么是 AI 测试辅助技能合集？

这是一套专为 AI 编码助手设计的测试技能库（Skills），包含 **18 个精心设计的测试 Skills**（15 个测试类型 + 3 个工作流），帮助 Cursor、Claude Code、Kiro 等 AI 工具成为你的专业测试助手。

#### 2. 支持哪些 AI 工具？

- **Cursor** (v0.40+)
- **Claude Code** (v1.0+)
- **Kiro** (v0.5+)

#### 3. 如何快速开始？

```bash
# 1. Clone 项目
git clone https://github.com/your-repo/ai-testing-assistant-skills.git

# 2. 复制需要的 skill
cp -r skills/testing-types/functional-testing ~/.cursor/skills/

# 3. 在 AI 工具中使用
@skill functional-testing
帮我为用户登录功能生成测试用例
```

#### 4. 中文和英文版本有什么区别？

功能完全相同，只是语言不同。中文 skill 目录名如 `functional-testing`，英文为 `functional-testing-en`。

#### 5. 可以同时使用多个 skills 吗？

可以！Skills 设计为可组合使用。查看 [skills-graph.md](skills-graph.md) 了解推荐的 skill 组合。

---

### 安装和配置

#### 6. 如何安装到 Cursor？

```bash
# 项目级（推荐）
cp -r skills/testing-types/functional-testing /path/to/your/project/.cursor/skills/

# 用户级（全局）
cp -r skills/testing-types/functional-testing ~/.cursor/skills/
```

#### 7. 如何安装到 Claude Code？

```bash
mkdir -p .claude/skills
cp -r skills/testing-types/functional-testing .claude/skills/
```

#### 8. 如何安装到 Kiro？

```bash
# 项目级
mkdir -p .kiro/skills
cp -r skills/testing-types/functional-testing .kiro/skills/

# 全局
mkdir -p ~/.kiro/skills
cp -r skills/testing-types/functional-testing ~/.kiro/skills/
```

#### 9. 如何更新 skills？

```bash
# 1. 拉取最新代码
cd ai-testing-assistant-skills
git pull origin main

# 2. 重新复制 skills
cp -r skills/testing-types/functional-testing /path/to/your/project/.cursor/skills/
```

#### 10. 如何自定义 skills？

1. 复制 skill 到您的项目
2. 修改 `prompts/` 目录下的提示词文件
3. 根据需要调整内容

---

### 使用问题

#### 11. 如何调用一个 skill？

在 AI 工具的对话框中：

```
@skill functional-testing
需求：用户登录功能
```

#### 12. 如何指定输出格式？

在需求末尾说明：

```
@skill functional-testing
需求：用户登录功能
请以 Excel 可粘贴的制表符分隔表格输出
```

支持的格式：Markdown（默认）、Excel、CSV、JSON、Jira、TestRail。

#### 13. 如何使用工作流？

```
@skill daily-testing-workflow
今天需要测试用户登录和注册功能
```

工作流会引导您完成一天的测试活动。

#### 14. 如何找到合适的 skill？

三种方式：
1. 查看 [README.md](README.md) - Skills 列表
2. 查看 [skills-index.md](skills-index.md) - 按类别索引
3. 查看 [skills-graph.md](skills-graph.md) - Skills 关系图

#### 15. 有哪些测试类型 Skills？

15 个测试类型 Skills：
- 功能测试、API 测试、自动化测试
- 性能测试、安全测试、移动端测试、可访问性测试
- 缺陷上报、测试用例编写、测试用例评审
- 测试报告、测试策略、需求分析
- 手动测试、AI 辅助测试

---

### 功能问题

#### 16. 如何生成测试用例？

```
@skill test-case-writing
需求：用户登录功能，支持邮箱和手机号登录
```

AI 会根据需求自动生成测试用例，包括正常场景、异常场景和边界值测试。

#### 17. 如何生成自动化测试代码？

```
@skill automation-testing
需求：为登录功能生成 Playwright 自动化测试代码
```

AI 会生成可运行的测试代码。

#### 18. 如何分析需求？

```
@skill requirements-analysis
需求：用户可以通过邮箱或手机号登录系统
```

AI 会分析需求并提取测试点。

#### 19. 如何制定测试策略？

```
@skill test-strategy
项目信息：
- 类型：Web 应用
- 技术栈：React + Node.js
- 团队规模：5 人
```

AI 会生成定制化的测试策略。

#### 20. 如何使用多个 Skills 组合？

参考 [skills-graph.md](skills-graph.md) 中的推荐组合，例如：

**新功能测试流程**：
```
1. @skill requirements-analysis
2. @skill test-strategy
3. @skill test-case-writing
4. @skill functional-testing
5. @skill automation-testing
```

---

### 故障排除

#### 21. Skill 无法加载怎么办？

检查：
1. 目录名是否正确
2. SKILL.md 文件是否存在
3. 文件权限是否正确
4. AI 工具版本是否支持

#### 22. 输出格式不正确怎么办？

确保在需求末尾明确说明格式：

```
请以 Excel 可粘贴的制表符分隔表格输出
```

#### 23. 中英文版本不同步怎么办？

请提交 Issue 报告，我们会及时修复。

#### 24. 如何选择合适的 Skill？

根据您的需求：
- **编写测试用例** → test-case-writing
- **功能测试** → functional-testing
- **API 测试** → api-testing
- **自动化测试** → automation-testing
- **性能测试** → performance-testing
- **安全测试** → security-testing

#### 25. Skills 之间有什么关系？

查看 [skills-graph.md](skills-graph.md) 了解 Skills 之间的依赖关系和推荐组合。

---

### 贡献和社区

#### 26. 如何贡献新的 skill？

1. Fork 项目
2. 创建新 Skill 目录
3. 编写 SKILL.md、prompts/ 等文件
4. 提交 Pull Request

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

#### 27. 如何报告 bug？

1. 搜索 [Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues)
2. 如果未被报告，创建新 Issue
3. 提供详细信息和复现步骤

#### 28. 如何请求新 Skill？

1. 搜索现有的 Feature Requests
2. 创建新 Issue，标签选择 `enhancement`
3. 详细描述 Skill 需求和使用场景

#### 29. 项目的许可证是什么？

MIT License。您可以自由使用、修改和分发。

#### 30. 如何获取更多帮助？

1. 查看本 FAQ
2. 查看 [README.md](README.md)
3. 搜索 [Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues)
4. 提问在 GitHub Issues

---

## English FAQ

### Basic Questions

#### 1. What is AI Testing Assistant Skills?

A testing skills library designed specifically for AI coding assistants, containing **18 carefully designed testing Skills** (15 testing types + 3 workflows) to help Cursor, Claude Code, Kiro, and other AI tools become your professional testing assistant.

#### 2. Which AI tools are supported?

- **Cursor** (v0.40+)
- **Claude Code** (v1.0+)
- **Kiro** (v0.5+)

#### 3. How to get started quickly?

```bash
# 1. Clone the project
git clone https://github.com/your-repo/ai-testing-assistant-skills.git

# 2. Copy needed skill
cp -r skills/testing-types/functional-testing-en ~/.cursor/skills/

# 3. Use in AI tool
@skill functional-testing-en
Help me generate test cases for user login functionality
```

#### 4. What's the difference between Chinese and English versions?

Functionally identical, just different languages. Chinese skill directories like `functional-testing`, English as `functional-testing-en`.

#### 5. Can I use multiple skills together?

Yes! Skills are designed to be composable. Check [skills-graph.md](skills-graph.md) for recommended skill combinations.

---

### Installation and Configuration

#### 6. How to install to Cursor?

```bash
# Project level (recommended)
cp -r skills/testing-types/functional-testing-en /path/to/your/project/.cursor/skills/

# User level (global)
cp -r skills/testing-types/functional-testing-en ~/.cursor/skills/
```

#### 7. How to install to Claude Code?

```bash
mkdir -p .claude/skills
cp -r skills/testing-types/functional-testing-en .claude/skills/
```

#### 8. How to install to Kiro?

```bash
# Project level
mkdir -p .kiro/skills
cp -r skills/testing-types/functional-testing-en .kiro/skills/

# Global
mkdir -p ~/.kiro/skills
cp -r skills/testing-types/functional-testing-en ~/.kiro/skills/
```

#### 9. How to update skills?

```bash
# 1. Pull latest code
cd ai-testing-assistant-skills
git pull origin main

# 2. Re-copy skills
cp -r skills/testing-types/functional-testing-en /path/to/your/project/.cursor/skills/
```

#### 10. How to customize skills?

1. Copy skill to your project
2. Modify prompt files in `prompts/` directory
3. Adjust content as needed

---

### Usage Questions

#### 11. How to invoke a skill?

In AI tool's chat:

```
@skill functional-testing-en
Requirement: User login functionality
```

#### 12. How to specify output format?

Specify at the end of requirement:

```
@skill functional-testing-en
Requirement: User login functionality
Please output as tab-separated table for Excel
```

Supported formats: Markdown (default), Excel, CSV, JSON, Jira, TestRail.

#### 13. How to use workflows?

```
@skill daily-testing-workflow-en
Today I need to test user login and registration features
```

Workflow will guide you through daily testing activities.

#### 14. How to find the right skill?

Three ways:
1. Check [README.md](README.md) - Skills list
2. Check [skills-index.md](skills-index.md) - By category
3. Check [skills-graph.md](skills-graph.md) - Skills relationships

#### 15. What testing type Skills are available?

15 testing type Skills:
- Functional Testing, API Testing, Automation Testing
- Performance Testing, Security Testing, Mobile Testing, Accessibility Testing
- Bug Reporting, Test Case Writing, Test Case Review
- Test Reporting, Test Strategy, Requirements Analysis
- Manual Testing, AI-Assisted Testing

---

### Feature Questions

#### 16. How to generate test cases?

```
@skill test-case-writing-en
Requirement: User login functionality, support email and phone login
```

AI will automatically generate test cases including normal, exception, and boundary value scenarios.

#### 17. How to generate automation test code?

```
@skill automation-testing-en
Requirement: Generate Playwright automation test code for login functionality
```

AI will generate runnable test code.

#### 18. How to analyze requirements?

```
@skill requirements-analysis-en
Requirement: Users can login to the system via email or phone number
```

AI will analyze requirements and extract test points.

#### 19. How to create test strategy?

```
@skill test-strategy-en
Project info:
- Type: Web application
- Tech stack: React + Node.js
- Team size: 5 people
```

AI will generate customized test strategy.

#### 20. How to use multiple Skills together?

Refer to recommended combinations in [skills-graph.md](skills-graph.md), for example:

**New Feature Testing Flow**:
```
1. @skill requirements-analysis-en
2. @skill test-strategy-en
3. @skill test-case-writing-en
4. @skill functional-testing-en
5. @skill automation-testing-en
```

---

### Troubleshooting

#### 21. Skill cannot be loaded?

Check:
1. Directory name is correct
2. SKILL.md file exists
3. File permissions are correct
4. AI tool version supports Skills

#### 22. Output format is incorrect?

Ensure you specify format at the end of requirement:

```
Please output as tab-separated table for Excel
```

#### 23. Chinese and English versions are out of sync?

Please submit an Issue to report, we will fix it promptly.

#### 24. How to choose the right Skill?

Based on your needs:
- **Write test cases** → test-case-writing
- **Functional testing** → functional-testing
- **API testing** → api-testing
- **Automation testing** → automation-testing
- **Performance testing** → performance-testing
- **Security testing** → security-testing

#### 25. What are the relationships between Skills?

Check [skills-graph.md](skills-graph.md) to understand dependencies and recommended combinations between Skills.

---

### Contributing and Community

#### 26. How to contribute a new skill?

1. Fork the project
2. Create new Skill directory
3. Write SKILL.md, prompts/, etc.
4. Submit Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

#### 27. How to report bugs?

1. Search [Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues)
2. If not reported, create new Issue
3. Provide detailed information and reproduction steps

#### 28. How to request a new Skill?

1. Search existing Feature Requests
2. Create new Issue with `enhancement` label
3. Describe Skill requirements and use cases in detail

#### 29. What is the project license?

MIT License. You can freely use, modify, and distribute.

#### 30. How to get more help?

1. Check this FAQ
2. Check [README.md](README.md)
3. Search [Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues)
4. Ask in GitHub Issues

---

## 没有找到答案？ | Can't Find Your Answer?

如果您的问题未在此列出，请在 [GitHub Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues) 提问。

If your question isn't listed, please ask in [GitHub Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues).

---

**最后更新 | Last Updated**: 2024-02-09
