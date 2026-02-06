# Changelog

All notable changes to the Awesome QA Skills project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-02-06

### Added

#### 架构层面
- 新增 `templates/` 目录，包含输出格式模板、工作流模板和 skill 模板
- 新增 `examples/` 目录，包含各测试类型的真实代码示例
- 新增 `docs/` 目录，包含教程、指南、API 文档和 FAQ
- 新增 `tools/` 目录，包含各种辅助工具脚本
- 新增 `ci-cd/` 目录，包含主流 CI/CD 平台的配置模板
- 新增 `tests/` 目录，包含 skill 测试用例和集成测试
- 新增 `skills/advanced/` 目录，包含高级 skills

#### 核心文档
- 新增 `CHANGELOG.md` - 项目更新日志
- 新增 `CONTRIBUTING.md` - 贡献指南
- 新增 `FAQ.md` - 常见问题解答
- 新增 `skills-index.md` - Skills 索引（按类别/场景/标签）
- 新增 `skills-graph.md` - Skills 依赖关系图（Mermaid 格式）

#### Skills 增强
- 所有测试类型 skills 新增 3-5 个真实代码示例
- 所有 skills 新增 `troubleshooting` 章节
- 所有 skills 新增分层提示词（basic/intermediate/advanced）
- 所有 skills 新增 `quick-start.md` 快速上手指南
- 所有 skills 新增版本号和最后更新日期

#### 工作流增强
- 工作流新增 checklist 格式的步骤追踪
- 工作流新增执行日志模板
- 工作流新增健康度评分机制
- 工作流新增团队规模适配指南（solo/small/large）
- 工作流新增项目阶段适配指南（mvp/growth/mature）

#### 智能化功能
- 新增上下文检测系统，自动识别项目类型、技术栈和测试框架
- 新增智能测试用例生成功能
- 新增 AI 辅助的缺陷根因分析
- 新增测试优先级自动排序
- 新增对话式测试设计流程

#### 输出格式
- 新增 Jira 格式输出模板
- 新增 TestRail 格式输出模板
- 新增 Azure DevOps 格式输出模板
- 新增自动格式检测功能
- 支持自定义输出模板

#### CI/CD 集成
- 新增 GitHub Actions 工作流模板
- 新增 GitLab CI 配置模板
- 新增 Jenkins Pipeline 模板
- 新增测试报告自动发布到 Slack/Teams 的配置
- 工作流新增 CI/CD 监控与响应步骤

#### 工具脚本
- 新增 `skill-generator.sh` - Skill 生成器
- 新增 `context-detector.sh` - 上下文检测器
- 新增 `sync-check.sh` - 中英文同步检查
- 新增 `quality-check.sh` - 质量检查
- 新增 `format-converter.sh` - 格式转换器
- 新增 `example-validator.sh` - 代码示例验证器

#### 高级 Skills
- 新增 `test-strategy-generator` - 测试策略生成器
- 新增 `test-metrics-analysis` - 测试度量分析
- 新增 `skill-orchestrator` - Skills 编排器

#### 文档和学习资源
- 新增交互式教程（每个主要 skill）
- 新增学习路径（初学者/中级/高级）
- 新增 50+ 常见问题解答
- README 新增 "5 分钟快速开始" 章节
- 新增视频教程脚本

### Changed

#### Skills 元数据
- 所有 skills 的 SKILL.md 新增以下字段：
  - `version` - 版本号
  - `last-updated` - 最后更新日期
  - `level` - 难度级别（beginner/intermediate/expert）
  - `tags` - 标签
  - `dependencies` - 依赖的其他 skills
  - `recommended-with` - 推荐组合使用的 skills
  - `context-aware` - 是否支持上下文感知
  - `context-patterns` - 上下文匹配模式
  - `examples-count` - 代码示例数量
  - `has-tutorial` - 是否有教程
  - `has-troubleshooting` - 是否有故障排除指南

#### 提示词优化
- 功能测试提示词新增 Playwright/Cypress 代码示例
- API 测试提示词新增 Postman/REST Assured/Supertest 示例
- 自动化测试提示词新增 Page Object Model 完整示例
- 性能测试提示词新增 JMeter/K6 示例
- 安全测试提示词新增 OWASP 检查清单
- 可访问性测试提示词新增 WCAG 检查清单
- 移动端测试提示词新增 Appium 示例

#### 工作流优化
- 日常测试工作流新增 CI/CD 监控步骤
- 迭代测试工作流新增 Sprint 规划检查清单
- 发布测试工作流新增 Go/No-Go 决策矩阵

#### 文档改进
- README 重构，新增快速开始章节
- 所有 skills 的 SKILL.md 新增 "何时使用" 章节
- 所有 skills 新增 "常见误区" 和 "最佳实践" 章节
- reference.md 新增更详细的步骤说明

### Fixed
- 修复中英文版本不同步的问题
- 修复部分代码示例无法运行的问题
- 修复文档链接失效的问题
- 修复格式不一致的问题

### Deprecated
- 无

### Removed
- 无

### Security
- 所有脚本新增输入验证，防止命令注入
- 配置文件新增权限控制
- 日志新增脱敏处理

---

## [1.0.0] - 2024-01-01

### Added
- 初始版本发布
- 3 个工作流 skills（日常/迭代/发布）
- 15 个测试类型 skills
- 中英文双语支持
- 基础文档和 README

---

## 版本说明

### 版本号规则
- **主版本号（Major）**: 不兼容的 API 变更
- **次版本号（Minor）**: 向后兼容的功能新增
- **修订号（Patch）**: 向后兼容的问题修正

### 发布周期
- **主版本**: 每 6-12 个月
- **次版本**: 每 1-2 个月
- **修订版**: 根据需要随时发布

### 支持策略
- 当前主版本：完全支持
- 上一个主版本：安全更新和关键 bug 修复
- 更早版本：不再支持

---

## 贡献者

感谢所有为本项目做出贡献的开发者！

查看完整的贡献者列表：[Contributors](https://github.com/your-repo/awesome-qa-skills/graphs/contributors)

---

## 反馈和建议

如果您有任何问题、建议或发现了 bug，请：
1. 查看 [FAQ.md](FAQ.md)
2. 搜索 [Issues](https://github.com/your-repo/awesome-qa-skills/issues)
3. 如果问题未被报告，请创建新的 Issue

---

[2.0.0]: https://github.com/your-repo/awesome-qa-skills/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/your-repo/awesome-qa-skills/releases/tag/v1.0.0
