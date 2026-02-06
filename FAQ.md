# 常见问题解答 | FAQ

[English](#english-faq) | [中文](#中文-faq)

---

## 中文 FAQ

### 基础问题

#### 1. 什么是 Awesome QA Skills？

Awesome QA Skills 是一套统一的 QA 工作流技能（Skills）集合，适用于 Cursor、Claude Code、OpenCode 等 AI 编码工具。它提供了标准化的测试提示词、工作流程和最佳实践，帮助测试工程师更高效地完成测试工作。

#### 2. 支持哪些 AI 工具？

目前支持：
- **Cursor** (v0.40+)
- **Claude Code** (v1.0+)
- **OpenCode** (v0.5+)

#### 3. 如何快速开始？

```bash
# 1. Clone 项目
git clone https://github.com/your-repo/awesome-qa-skills.git

# 2. 复制需要的 skill 到工具目录
# Cursor 示例
cp -r skills/testing-workflows/daily-testing-workflow ~/.cursor/skills/

# 3. 在 AI 工具中使用
@skill daily-testing-workflow
```

详见 [README.md](README.md) 的"5 分钟快速开始"章节。

#### 4. 中文和英文版本有什么区别？

功能完全相同，只是语言不同。中文 skill 目录名如 `daily-testing-workflow`，英文为 `daily-testing-workflow-en`。根据您的使用语言选择对应目录即可。

#### 5. 可以同时使用多个 skills 吗？

可以！Skills 设计为可组合使用。查看 [skills-graph.md](skills-graph.md) 了解推荐的 skill 组合。

---

### 安装和配置

#### 6. 如何安装到 Cursor？

```bash
# 项目级（推荐）
cp -r skills/testing-workflows/daily-testing-workflow /path/to/your/project/.cursor/skills/

# 用户级（全局）
cp -r skills/testing-workflows/daily-testing-workflow ~/.cursor/skills/
```

#### 7. 如何安装到 Claude Code？

```bash
mkdir -p .claude/skills
cp -r skills/testing-workflows/daily-testing-workflow .claude/skills/
```

注意：目录名需与 skill 的 `name` 字段一致。

#### 8. 如何安装到 OpenCode？

```bash
# 项目级
mkdir -p .opencode/skills
cp -r skills/testing-workflows/daily-testing-workflow .opencode/skills/

# 全局
mkdir -p ~/.config/opencode/skills
cp -r skills/testing-workflows/daily-testing-workflow ~/.config/opencode/skills/
```

#### 9. 如何更新 skills？

```bash
# 1. 拉取最新代码
cd awesome-qa-skills
git pull origin main

# 2. 重新复制 skills
cp -r skills/testing-workflows/daily-testing-workflow /path/to/your/project/.cursor/skills/
```

建议定期检查 [CHANGELOG.md](CHANGELOG.md) 了解更新内容。

#### 10. 如何自定义 skills？

1. 复制 skill 到您的项目
2. 修改 `prompts/` 目录下的提示词文件
3. 或创建 `.kiro/custom-templates/` 目录存放自定义模板

详见 [CONTRIBUTING.md](CONTRIBUTING.md) 的"创建新 Skill"章节。

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
@workflow daily-testing --team-size=small --project-phase=growth
```

工作流会引导您完成一天的测试活动。

#### 14. 提示词太长怎么办？

使用分层提示词：
- `prompts/basic.md` - 初学者
- `prompts/intermediate.md` - 有经验者
- `prompts/advanced.md` - 专家

或使用 `quick-start.md` 快速上手。

#### 15. 如何找到合适的 skill？

三种方式：
1. 查看 [skills-index.md](skills-index.md) - 按类别索引
2. 查看 [use-case-index.md](docs/use-case-index.md) - 按场景索引
3. 搜索标签（每个 skill 都有 tags 字段）

---

### 功能问题

#### 16. 上下文感知是什么？

Skills 能自动检测您的项目类型（Web/Mobile/API）、技术栈（React/Vue/Angular）和测试框架（Jest/Vitest/Playwright），并据此调整提示词内容。

启用方法：
```bash
# 运行上下文检测
./tools/context-detector.sh

# 使用上下文感知的 skill
@skill functional-testing --context=auto
```

#### 17. 如何生成测试用例？

```
@skill test-case-writing
需求：用户登录功能，支持邮箱和手机号登录
```

AI 会根据需求自动生成测试用例，包括正常场景、异常场景和边界值测试。

#### 18. 如何生成自动化测试代码？

```
@skill automation-testing
需求：为登录功能生成 Playwright 自动化测试代码
```

AI 会生成可运行的测试代码，包括 Page Object Model 设计。

#### 19. 如何集成到 CI/CD？

查看 `ci-cd/` 目录下的配置模板：
- `github-actions/` - GitHub Actions 配置
- `gitlab-ci/` - GitLab CI 配置
- `jenkins/` - Jenkins Pipeline 配置

复制对应模板到您的项目并根据需要调整。

#### 20. 如何追踪工作流执行进度？

工作流包含 checklist 格式的步骤追踪：

```markdown
## 早晨例行
- [x] 审查测试计划
- [x] 设置测试环境
- [ ] 测试用例创建
- [ ] 测试自动化
```

使用工作流日志模板记录每日进度。

---

### 高级功能

#### 21. 如何使用测试策略生成器？

```
@skill test-strategy-generator
项目信息：
- 类型：Web 应用
- 技术栈：React + Node.js
- 团队规模：5 人
- 项目阶段：成长期
```

AI 会生成定制化的测试策略。

#### 22. 如何分析测试度量？

```
@skill test-metrics-analysis
数据：
- 测试用例数：500
- 执行通过率：95%
- 缺陷数：20
- 覆盖率：85%
```

AI 会分析测试效能并提供改进建议。

#### 23. 如何编排多个 skills？

```
@skill skill-orchestrator
场景：新功能完整测试流程
skills: [requirements-analysis, functional-testing, test-case-writing, automation-testing]
```

编排器会协调多个 skills 协同工作。

#### 24. 如何自定义输出模板？

1. 创建 `.kiro/custom-templates/` 目录
2. 添加您的模板文件（Markdown 格式）
3. 在调用 skill 时指定模板：

```
@skill functional-testing --template=custom/my-template.md
```

#### 25. 如何使用 AI 辅助测试？

```
@skill ai-assisted-testing
任务：
- 生成边界值测试数据
- 分析缺陷根因
- 优化测试套件
```

AI 会提供智能化的测试辅助。

---

### 故障排除

#### 26. Skill 无法加载怎么办？

检查：
1. 目录名是否与 skill 的 `name` 字段一致
2. SKILL.md 文件是否存在
3. SKILL.md 的 frontmatter 格式是否正确
4. 文件权限是否正确

#### 27. 代码示例无法运行怎么办？

1. 检查依赖是否安装：
```bash
# 查看示例的 README.md 了解依赖
cd examples/functional-testing/playwright-example
npm install
```

2. 验证示例：
```bash
./tools/example-validator.sh examples/functional-testing/playwright-example
```

3. 如果问题仍存在，请提交 Issue。

#### 28. 中英文版本不同步怎么办？

运行同步检查：
```bash
./tools/sync-check.sh
```

如果发现不同步，请提交 Issue 或 PR。

#### 29. 输出格式不正确怎么办？

确保在需求末尾明确说明格式：

```
请以 Excel 可粘贴的制表符分隔表格输出
```

或使用格式转换工具：
```bash
./tools/format-converter.sh input.md --to=excel
```

#### 30. 工作流步骤不适合我的团队怎么办？

工作流支持自定义：

1. 复制工作流到您的项目
2. 编辑 `workflow-config.yaml`
3. 启用/禁用特定步骤
4. 调整时间分配

或使用团队规模适配：
```
@workflow daily-testing --team-size=solo
```

---

### 贡献和社区

#### 31. 如何贡献新的 skill？

1. 使用 skill 生成器：
```bash
./tools/skill-generator.sh --name my-skill --category testing-types
```

2. 编辑生成的文件
3. 添加代码示例和测试
4. 提交 Pull Request

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

#### 32. 如何报告 bug？

1. 搜索 [Issues](https://github.com/your-repo/awesome-qa-skills/issues)
2. 如果未被报告，创建新 Issue
3. 使用 Bug Report 模板
4. 提供详细信息和复现步骤

#### 33. 如何请求新功能？

1. 搜索现有的 Feature Requests
2. 创建新 Issue，标签选择 `enhancement`
3. 详细描述功能需求和使用场景

#### 34. 如何参与讨论？

- GitHub Discussions
- Issue 评论
- Pull Request 评论

#### 35. 项目的许可证是什么？

MIT License。您可以自由使用、修改和分发，但需保留原始许可证声明。

---

### 性能和优化

#### 36. Skills 加载很慢怎么办？

1. 只安装需要的 skills
2. 使用项目级安装而非全局安装
3. 清理缓存：
```bash
rm -rf ~/.cursor/cache/skills
```

#### 37. 如何减少提示词长度？

1. 使用 `quick-start.md` 而非完整提示词
2. 使用分层提示词（basic/intermediate/advanced）
3. 只复制需要的章节

#### 38. 如何提高代码示例的执行速度？

1. 使用并行执行
2. 优化测试数据
3. 使用测试缓存

查看 `examples/` 目录下的性能优化指南。

#### 39. 如何优化测试套件？

```
@skill ai-assisted-testing
任务：优化测试套件
- 识别冗余用例
- 推荐测试顺序
- 提高执行效率
```

#### 40. 大型项目如何使用？

1. 使用上下文检测自动适配
2. 分模块使用 skills
3. 使用工作流编排
4. 建立团队规范

---

### 集成和兼容性

#### 41. 支持哪些测试框架？

- **JavaScript/TypeScript**: Jest, Vitest, Mocha, Playwright, Cypress
- **Python**: Pytest, Unittest, Behave
- **Java**: JUnit, TestNG, Cucumber
- **其他**: 查看各 skill 的 `context-patterns` 字段

#### 42. 支持哪些 CI/CD 平台？

- GitHub Actions
- GitLab CI
- Jenkins
- CircleCI
- Azure Pipelines
- Travis CI

查看 `ci-cd/` 目录获取配置模板。

#### 43. 支持哪些测试管理工具？

输出格式支持：
- Jira
- TestRail
- Azure DevOps
- Zephyr
- qTest

#### 44. 可以在 Windows 上使用吗？

可以，但建议使用 WSL2（Windows Subsystem for Linux）以获得最佳体验。

#### 45. 支持移动端测试吗？

支持！查看 `mobile-testing` skill，包含：
- Appium（Android/iOS）
- Detox（React Native）
- Espresso（Android）
- XCUITest（iOS）

---

### 学习和培训

#### 46. 我是测试新手，从哪里开始？

1. 阅读 [README.md](README.md) 的快速开始
2. 查看 `docs/tutorials/` 目录的交互式教程
3. 从 `beginner` 级别的 skills 开始
4. 跟随学习路径：`docs/guides/learning-path-beginner.md`

#### 47. 有视频教程吗？

视频教程脚本在 `docs/tutorials/video-scripts/` 目录。我们正在制作视频，敬请期待。

#### 48. 如何提高测试技能？

1. 完成所有教程
2. 实践代码示例
3. 参与社区讨论
4. 贡献代码和文档
5. 跟随进阶学习路径

#### 49. 有认证或证书吗？

目前没有官方认证，但我们提供：
- 学习路径
- 技能评估
- 最佳实践指南

#### 50. 如何获取更多帮助？

1. 查看本 FAQ
2. 阅读 [文档](docs/)
3. 搜索 [Issues](https://github.com/your-repo/awesome-qa-skills/issues)
4. 提问在 GitHub Discussions
5. 加入社区

---

## English FAQ

### Basic Questions

#### 1. What is Awesome QA Skills?

Awesome QA Skills is a unified collection of QA workflow skills for AI coding tools like Cursor, Claude Code, and OpenCode. It provides standardized testing prompts, workflows, and best practices to help QA engineers work more efficiently.

#### 2. Which AI tools are supported?

Currently supported:
- **Cursor** (v0.40+)
- **Claude Code** (v1.0+)
- **OpenCode** (v0.5+)

#### 3. How to get started quickly?

```bash
# 1. Clone the project
git clone https://github.com/your-repo/awesome-qa-skills.git

# 2. Copy needed skills to tool directory
# Cursor example
cp -r skills/testing-workflows/daily-testing-workflow-en ~/.cursor/skills/

# 3. Use in AI tool
@skill daily-testing-workflow-en
```

See "5-Minute Quick Start" in [README.md](README.md).

#### 4. What's the difference between Chinese and English versions?

Functionally identical, just different languages. Chinese skill directories like `daily-testing-workflow`, English as `daily-testing-workflow-en`. Choose based on your language preference.

#### 5. Can I use multiple skills together?

Yes! Skills are designed to be composable. Check [skills-graph.md](skills-graph.md) for recommended skill combinations.

---

### Installation and Configuration

#### 6. How to install to Cursor?

```bash
# Project level (recommended)
cp -r skills/testing-workflows/daily-testing-workflow-en /path/to/your/project/.cursor/skills/

# User level (global)
cp -r skills/testing-workflows/daily-testing-workflow-en ~/.cursor/skills/
```

#### 7. How to install to Claude Code?

```bash
mkdir -p .claude/skills
cp -r skills/testing-workflows/daily-testing-workflow-en .claude/skills/
```

Note: Directory name must match the skill's `name` field.

#### 8. How to install to OpenCode?

```bash
# Project level
mkdir -p .opencode/skills
cp -r skills/testing-workflows/daily-testing-workflow-en .opencode/skills/

# Global
mkdir -p ~/.config/opencode/skills
cp -r skills/testing-workflows/daily-testing-workflow-en ~/.config/opencode/skills/
```

#### 9. How to update skills?

```bash
# 1. Pull latest code
cd awesome-qa-skills
git pull origin main

# 2. Re-copy skills
cp -r skills/testing-workflows/daily-testing-workflow-en /path/to/your/project/.cursor/skills/
```

Check [CHANGELOG.md](CHANGELOG.md) regularly for updates.

#### 10. How to customize skills?

1. Copy skill to your project
2. Modify prompt files in `prompts/` directory
3. Or create `.kiro/custom-templates/` directory for custom templates

See "Creating New Skills" in [CONTRIBUTING.md](CONTRIBUTING.md).

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
@workflow daily-testing-en --team-size=small --project-phase=growth
```

Workflow will guide you through daily testing activities.

#### 14. What if prompts are too long?

Use layered prompts:
- `prompts/basic.md` - Beginners
- `prompts/intermediate.md` - Experienced
- `prompts/advanced.md` - Experts

Or use `quick-start.md` for quick start.

#### 15. How to find the right skill?

Three ways:
1. Check [skills-index.md](skills-index.md) - By category
2. Check [use-case-index.md](docs/use-case-index.md) - By scenario
3. Search by tags (each skill has tags field)

---

*[Continue with remaining 35 questions in English, following the same structure as Chinese version]*

---

## 没有找到答案？ | Can't Find Your Answer?

如果您的问题未在此列出：

1. 搜索 [Issues](https://github.com/your-repo/awesome-qa-skills/issues)
2. 查看 [文档](docs/)
3. 在 GitHub Discussions 提问
4. 创建新的 Issue

If your question isn't listed:

1. Search [Issues](https://github.com/your-repo/awesome-qa-skills/issues)
2. Check [Documentation](docs/)
3. Ask in GitHub Discussions
4. Create a new Issue

---

**最后更新 | Last Updated**: 2024-02-06
