# 工作流所用提示词

本目录为工作流与测试类型技能所用的提示词。各 workflow 的 reference.md 与 SKILL 中的步骤→提示词对应关系与本目录一致。

## 文件与用途（中英文双版本）

| 类型 | 中文 | 英文 | 用途 | 常用阶段 |
|------|------|------|------|----------|
| 测试策略 | test-strategy.md | test-strategy_EN.md | 测试策略、风险与范围 | 规划、早晨审查、质量评估 |
| 需求分析 | requirements-analysis.md | requirements-analysis_EN.md | 需求分析、测试范围与场景 | 规划、用例前分析 |
| 测试用例编写 | test-case-writing.md | test-case-writing_EN.md | 测试用例设计与编写 | 日常/迭代 用例创建 |
| 自动化测试 | automation-testing.md | automation-testing_EN.md | 自动化方案与脚本、CI/CD | 日常自动化、环境与回归 |
| API 测试 | api-testing.md | api-testing_EN.md | API 测试策略与自动化 | API/集成测试 |
| 缺陷上报 | bug-reporting.md | bug-reporting_EN.md | 缺陷报告模板与分类 | 缺陷上报、缺陷分类 |
| 手动测试 | manual-testing.md | manual-testing_EN.md | 手动/探索性测试、章程 | 探索性测试、缺陷突击 |
| 功能测试 | functional-testing.md | functional-testing_EN.md | 功能/回归/E2E 场景 | 功能测试、回归、E2E |
| 测试报告 | test-reporting.md | test-reporting_EN.md | 测试报告与质量分析 | 下午审查、评审、发布评估 |
| 性能测试 | performance-testing.md | performance-testing_EN.md | 性能测试策略与执行 | 发布专项测试 |
| 安全测试 | security-testing.md | security-testing_EN.md | 安全测试策略与执行 | 发布专项测试 |
| 可访问性测试 | accessibility-testing.md | accessibility-testing_EN.md | 可访问性/视觉测试 | 发布专项、迭代视觉 |
| AI 辅助测试 | ai-assisted-testing.md | ai-assisted-testing_EN.md | AI 辅助测试与智能选择 | 回归选择、测试维护 |
| 测试用例评审 | test-case-reviewer.md | test-case-reviewer_EN.md | 测试用例评审、缺失场景与改进建议 | 迭代/发布前评审 |
| 移动端测试 | mobile-testing.md | mobile-testing_EN.md | 移动端（iOS/Android）测试方案与用例 | 移动端专项 |

## 使用方式

- 在 **Cursor / Claude Code / OpenCode** 的 workflow skill 中，各步骤会标明「使用 xxx 提示词」。
- 直接打开本目录下对应 **中文 `.md` 或英文 `_EN.md`** 文件，将其中 **Role、Task、执行指令** 及（按需）输出格式，作为与 AI 对话的提示词使用。
- 完整输出格式与示例见本目录各提示词文件内的 Output Format 小节。
