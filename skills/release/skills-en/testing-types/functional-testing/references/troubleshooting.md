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
1. 查看 [FAQ.md](local/FAQ.md)
2. 查看示例的 README.md 文件
3. 搜索 [GitHub Issues](https://github.com/naodeng/awesome-qa-skills/issues)
4. 提交新的 Issue 并附上详细信息

**相关技能：** api-testing、test-case-writing、test-strategy、automation-testing。
