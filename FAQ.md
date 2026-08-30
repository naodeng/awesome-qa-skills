<div align="right"><strong>🇨🇳 中文</strong> | <a href="./FAQ_EN.md">🇬🇧 English</a></div>

# 常见问题解答

### 基础问题

#### 1. 什么是 AI 测试辅助技能合集？

这是一套面向 AI 编码助手的质量工程 Skills 库。每种语言目前包含 **78 个 Skill**：65 个测试类型、10 个跨阶段工作流和 3 个 Skill Engineering 治理能力；中英文共 156 个可独立安装的目录。

#### 2. 支持哪些 AI 工具？

- **Cursor** (v0.40+)
- **Claude Code** (v1.0+)
- **Kiro** (v0.5+)

#### 3. 如何快速开始？

```bash
# 1. Clone 项目
git clone https://github.com/naodeng/awesome-qa-skills.git

# 2. 复制需要的 skill
cp -r skills/zh/testing-types/functional-testing ~/.cursor/skills/

# 3. 在 AI 工具中使用
@skill functional-testing
帮我为用户登录功能生成测试用例
```

#### 4. 中文和英文版本有什么区别？

功能完全相同，只是语言不同。中文 skill 目录名如 `functional-testing`，英文为 `functional-testing`。

#### 5. 可以同时使用多个 skills 吗？

可以！Skills 设计为可组合使用。查看 [skills-graph.md](docs/catalog/skills-graph.md) 了解推荐的 skill 组合。

---

### 安装和配置

#### 6. 如何安装到 Cursor？

```bash
# 项目级（推荐）
cp -r skills/zh/testing-types/functional-testing /path/to/your/project/.cursor/skills/

# 用户级（全局）
cp -r skills/zh/testing-types/functional-testing ~/.cursor/skills/
```

#### 7. 如何安装到 Claude Code？

```bash
mkdir -p .claude/skills
cp -r skills/zh/testing-types/functional-testing .claude/skills/
```

#### 8. 如何安装到 Kiro？

```bash
# 项目级
mkdir -p .kiro/skills
cp -r skills/zh/testing-types/functional-testing .kiro/skills/

# 全局
mkdir -p ~/.kiro/skills
cp -r skills/zh/testing-types/functional-testing ~/.kiro/skills/
```

#### 9. 如何更新 skills？

```bash
# 1. 拉取最新代码
cd ai-testing-assistant-skills
git pull origin main

# 2. 重新复制 skills
cp -r skills/zh/testing-types/functional-testing /path/to/your/project/.cursor/skills/
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
2. 查看 [skills-index.md](docs/catalog/skills-index.md) - 按类别索引
3. 查看 [skills-graph.md](docs/catalog/skills-graph.md) - Skills 关系图

#### 15. 有哪些测试类型 Skills？

当前有 65 个测试类型，覆盖 Core QA、Engineering QA、Production Quality 和 AI Native QA。请查看 [全量索引](docs/catalog/skills-index.md) 按研发与测试阶段选择。

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

参考 [skills-graph.md](docs/catalog/skills-graph.md) 中的推荐组合，例如：

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

查看 [skills-graph.md](docs/catalog/skills-graph.md) 了解 Skills 之间的依赖关系和推荐组合。

---

### 贡献和社区

#### 26. 如何贡献新的 skill？

1. Fork 项目
2. 创建新 Skill 目录
3. 编写 SKILL.md、prompts/ 等文件
4. 提交 Pull Request

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

#### 27. 如何报告 bug？

1. 搜索 [Issues](https://github.com/naodeng/awesome-qa-skills/issues)
2. 如果未被报告，创建新 Issue
3. 提供详细信息和复现步骤

#### 28. 如何请求新 Skill？

1. 搜索现有的 Feature Requests
2. 创建新 Issue，标签选择 `enhancement`
3. 详细描述 Skill 需求和使用场景

#### 29. 项目的许可证是什么？

PolyForm Noncommercial License 1.0.0。允许自由使用、修改和分发，但仅限非商业用途。

#### 30. 如何获取更多帮助？

1. 查看本 FAQ
2. 查看 [README.md](README.md)
3. 搜索 [Issues](https://github.com/naodeng/awesome-qa-skills/issues)
4. 提问在 GitHub Issues
