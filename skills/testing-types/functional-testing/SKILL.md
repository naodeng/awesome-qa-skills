---
name: functional-testing
version: 2.0.0
last-updated: 2024-02-06
description: 设计功能测试方案与用例，覆盖业务功能、UI、数据、集成。默认输出 Markdown，可请求 Excel/CSV/JSON。Use for 功能测试 or functional testing.
category: testing-types
level: intermediate
tags: [functional, core, manual, ui, integration]
dependencies: []
recommended-with: [test-case-writing, requirements-analysis, automation-testing]
context-aware: true
context-patterns:
  project-types: [web, mobile, desktop, api]
  frameworks: [react, vue, angular, flutter, electron]
  test-frameworks: [playwright, cypress, selenium, appium]
output-formats: [markdown, excel, csv, json, jira, testrail]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
---

# 功能测试（中文版）

**英文版：** 见技能 `functional-testing-en`。

提示词见本目录 `prompts/functional-testing.md`。

## 何时使用

- 用户提到「功能测试」「functional testing」「功能测试用例」「功能测试方案」
- 需要根据需求或规格设计功能测试策略、测试用例、测试方案
- **触发示例：**「根据以下需求设计功能测试用例」「做一份功能测试方案」

## 输出格式选项

本技能**默认输出为 Markdown**（与 Standard-version 模板一致）。若需其他格式，请在需求**末尾**明确说明：

| 格式 | 说明 | 如何请求（示例） |
|------|------|------------------|
| **Markdown** | 默认，便于阅读与版本管理 | 无需额外说明 |
| **Excel** | 制表符分隔，可粘贴到 Excel | 「请以 Excel 可粘贴的制表符分隔表格输出」 |
| **CSV** | 逗号分隔，首行为表头 | 「请以 CSV 格式输出」 |
| **JSON** | 便于程序解析 | 「请以 JSON 形式输出」 |

详细说明与示例见本目录 **[output-formats.md](output-formats.md)**。

## 如何使用本技能中的提示词

1. 打开本目录 `prompts/functional-testing.md`，将虚线以下内容复制到 AI 对话。
2. 附加你的功能需求或系统规格。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 参考文件

- **[prompts/functional-testing.md](prompts/functional-testing.md)** — 功能测试 Standard-version 提示词
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON 请求说明

## 代码示例 | Code Examples

本技能提供以下真实代码示例：

1. **[Playwright 登录测试](examples/playwright-login/)** - 完整的登录功能测试套件
   - 14个测试用例
   - 覆盖功能、可访问性、安全性
   - 包含最佳实践和故障排除

2. **Cypress 表单测试**（即将推出）
3. **Selenium 导航测试**（即将推出）

查看 [examples/](examples/) 目录获取更多示例。

## 常见误区 | Common Pitfalls

- ❌ **跳过需求分析直接写用例** → ✅ 先使用 requirements-analysis skill 分析需求，识别测试点
- ❌ **只测试正常场景** → ✅ 同时覆盖异常场景、边界值和错误处理
- ❌ **用例描述不清晰** → ✅ 使用明确的步骤和预期结果，确保可重现
- ❌ **忽略可访问性测试** → ✅ 包含键盘导航、屏幕阅读器等可访问性验证
- ❌ **测试数据硬编码** → ✅ 使用测试数据管理策略，便于维护

## 最佳实践 | Best Practices

1. **测试设计**
   - 使用等价类划分和边界值分析
   - 遵循 AAA 模式（Arrange-Act-Assert）
   - 保持测试独立性，避免依赖

2. **元素定位**
   - 优先使用 data-testid 属性
   - 避免使用易变的 CSS 类名
   - 使用语义化的定位器

3. **断言策略**
   - 使用多个具体的断言而非单一模糊断言
   - 验证关键业务逻辑
   - 包含用户体验验证

4. **维护性**
   - 使用 Page Object Model 设计模式
   - 提取可复用的测试工具函数
   - 保持测试代码整洁

5. **执行效率**
   - 并行运行独立测试
   - 使用合适的等待策略
   - 避免不必要的延迟

## 故障排除 | Troubleshooting

### 问题1：代码示例无法运行

**症状**：运行示例时报错 `Cannot find module` 或 `Command not found`

**解决方案**：
1. 确保已安装依赖：
   ```bash
   cd examples/playwright-login
   npm install
   ```
2. 检查 Node.js 版本（需要 >= 16）：
   ```bash
   node --version
   ```
3. 如果使用 Playwright，需要安装浏览器：
   ```bash
   npx playwright install
   ```

### 问题2：测试用例设计不完整

**症状**：测试覆盖率低，遗漏重要场景

**解决方案**：
1. 先使用 requirements-analysis skill 分析需求
2. 参考提示词中的"测试覆盖维度"章节
3. 使用测试设计方法：
   - 等价类划分
   - 边界值分析
   - 决策表测试
   - 状态转换测试
4. 检查清单：
   - [ ] 正常场景
   - [ ] 异常场景
   - [ ] 边界值
   - [ ] 错误处理
   - [ ] 可访问性
   - [ ] 安全性

### 问题3：输出格式不符合预期

**症状**：生成的测试用例格式不对或缺少字段

**解决方案**：
1. 在需求末尾明确说明格式要求：
   ```
   请以 Excel 可粘贴的制表符分隔表格输出
   ```
2. 参考 [output-formats.md](output-formats.md) 中的示例
3. 使用格式转换工具（待实现）：
   ```bash
   ./tools/format-converter.sh input.md --to=excel
   ```

### 问题4：测试执行不稳定

**症状**：测试时而通过时而失败

**解决方案**：
1. 使用显式等待而非固定延迟：
   ```typescript
   // ✅ 推荐
   await expect(element).toBeVisible();
   
   // ❌ 不推荐
   await page.waitForTimeout(3000);
   ```
2. 等待网络请求完成：
   ```typescript
   await page.waitForResponse(resp => resp.url().includes('/api'));
   ```
3. 使用重试机制（Playwright 配置）：
   ```typescript
   retries: 2
   ```

### 问题5：无法定位元素

**症状**：测试报错 `Element not found` 或 `Timeout`

**解决方案**：
1. 检查元素是否在 iframe 中：
   ```typescript
   const frame = page.frameLocator('iframe');
   await frame.locator('[data-testid="element"]').click();
   ```
2. 等待元素出现：
   ```typescript
   await page.waitForSelector('[data-testid="element"]');
   ```
3. 使用更可靠的定位器：
   ```typescript
   // ✅ 推荐：data-testid
   page.locator('[data-testid="login-button"]')
   
   // ✅ 推荐：role
   page.getByRole('button', { name: '登录' })
   
   // ❌ 不推荐：CSS 类
   page.locator('.btn-primary')
   ```

### 问题6：测试运行缓慢

**症状**：测试套件执行时间过长

**解决方案**：
1. 启用并行执行：
   ```typescript
   // playwright.config.ts
   fullyParallel: true,
   workers: 4,
   ```
2. 优化等待策略，避免不必要的等待
3. 使用测试数据缓存
4. 考虑使用 API 设置测试前置条件

### 问题7：CI/CD 环境测试失败

**症状**：本地通过但 CI 失败

**解决方案**：
1. 检查环境差异（浏览器版本、屏幕分辨率）
2. 增加 CI 环境的超时时间
3. 启用失败重试：
   ```typescript
   retries: process.env.CI ? 2 : 0
   ```
4. 查看 CI 日志、截图和视频
5. 使用 Docker 容器保证环境一致性

### 获取更多帮助

如果问题仍未解决：
1. 查看 [FAQ.md](../../../FAQ.md)
2. 查看示例的 README.md 文件
3. 搜索 [GitHub Issues](https://github.com/your-repo/awesome-qa-skills/issues)
4. 提交新的 Issue 并附上详细信息

**相关技能：** api-testing、test-case-writing、test-strategy、automation-testing。
