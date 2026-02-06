# 测试类型技能（Testing Type Skills）

本目录下各技能按测试类型单独封装，**中英文分目录**，并支持多种输出格式。

- **默认输出**：Markdown。
- **可选输出**：在向 AI 提交需求时**在末尾说明**即可获得 **Excel**（制表符分隔，可粘贴到 Excel）、**CSV** 或 **JSON** 格式。详见各技能目录下的 **output-formats.md** 及根目录 `_output-formats-template-zh.md` / `_output-formats-template-en.md`。

## 测试类型列表

| 类型（中文） | 目录名（中文） | 目录名（英文） |
|-------------|----------------|----------------|
| 功能测试 | functional-testing | functional-testing-en |
| API 测试 | api-testing | api-testing-en |
| 自动化测试 | automation-testing | automation-testing-en |
| 缺陷上报 | bug-reporting | bug-reporting-en |
| 手动/探索性测试 | manual-testing | manual-testing-en |
| 测试用例编写 | test-case-writing | test-case-writing-en |
| 测试报告 | test-reporting | test-reporting-en |
| 测试策略 | test-strategy | test-strategy-en |
| 需求分析 | requirements-analysis | requirements-analysis-en |
| 性能测试 | performance-testing | performance-testing-en |
| 安全测试 | security-testing | security-testing-en |
| 可访问性测试 | accessibility-testing | accessibility-testing-en |
| AI 辅助测试 | ai-assisted-testing | ai-assisted-testing-en |
| 测试用例评审 | test-case-reviewer | test-case-reviewer-en |
| 移动端测试 | mobile-testing | mobile-testing-en |

以上类型的提示词已内置在各技能目录的 `prompts/` 中。

## 输出格式选项

各技能**默认输出为 Markdown**。若需其他格式，请在对话中明确说明：

- **Excel**：请以「Excel 可粘贴的制表符分隔表格」或「可直接复制到 Excel 的表格」形式输出。
- **CSV**：请以 CSV（逗号分隔，首行为表头）形式输出。
- **JSON**：请以 JSON 结构输出（具体字段见各技能 `output-formats.md`）。

详见各技能目录下的 **output-formats.md**（中文技能为中文说明，英文技能为英文说明）。

## 使用方式

复制对应语言目录到你的 AI 工具 skills 目录即可，与工作流技能用法相同（Cursor `.cursor/skills/`、Claude Code `.claude/skills/`、OpenCode `.opencode/skills/`）。
