## 故障排除 | Troubleshooting

### 问题1：axe-core 报告过多误报

**症状**：自动化测试报告大量问题，但实际上是误报

**解决方案**：
1. 配置规则排除已知误报：
   ```typescript
   await new AxeBuilder({ page })
     .disableRules(['color-contrast']) // 排除特定规则
     .analyze();
   ```
2. 使用标签过滤：
   ```typescript
   await new AxeBuilder({ page })
     .withTags(['wcag2a', 'wcag2aa']) // 只检查 WCAG 2.1 A/AA
     .analyze();
   ```
3. 手工验证可疑问题
4. 更新到最新版本的 axe-core

### 问题2：无法检测动态内容的可访问性问题

**症状**：模态框、下拉菜单等动态内容的问题未被检测

**解决方案**：
1. 在触发动态内容后再运行测试：
   ```typescript
   await page.click('[data-testid="open-modal"]');
   await page.waitForSelector('[role="dialog"]');
   const results = await new AxeBuilder({ page }).analyze();
   ```
2. 针对特定区域测试：
   ```typescript
   await new AxeBuilder({ page })
     .include('[role="dialog"]')
     .analyze();
   ```
3. 测试不同状态下的可访问性

### 问题3：键盘导航测试不通过

**症状**：某些元素无法通过键盘访问

**解决方案**：
1. 检查 tabindex 属性：
   ```html
   <!-- ✅ 推荐：使用 tabindex="0" 使元素可聚焦 -->
   <div role="button" tabindex="0">Click me</div>
   
   <!-- ❌ 避免：tabindex > 0 会破坏自然的 Tab 顺序 -->
   <div tabindex="5">Bad practice</div>
   ```
2. 使用语义化 HTML：
   ```html
   <!-- ✅ 推荐：原生按钮自动可聚焦 -->
   <button>Click me</button>
   
   <!-- ❌ 不推荐：需要额外的可访问性属性 -->
   <div onclick="...">Click me</div>
   ```
3. 添加键盘事件处理：
   ```typescript
   element.addEventListener('keydown', (e) => {
     if (e.key === 'Enter' || e.key === ' ') {
       // 处理激活
     }
   });
   ```

### 问题4：颜色对比度不足

**症状**：axe-core 报告颜色对比度问题

**解决方案**：
1. 使用对比度检查工具：
   - Chrome DevTools Lighthouse
   - WebAIM Contrast Checker
   - Colour Contrast Analyser
2. 确保对比度至少：
   - 正常文本：4.5:1
   - 大文本（18pt+）：3:1
   - UI 组件：3:1
3. 调整颜色方案：
   ```css
   /* ❌ 对比度不足 */
   color: #999; /* 灰色文本 */
   background: #fff; /* 白色背景 */
   
   /* ✅ 对比度充足 */
   color: #595959; /* 深灰色文本 */
   background: #fff; /* 白色背景 */
   ```

### 问题5：屏幕阅读器无法正确读取内容

**症状**：使用屏幕阅读器时内容混乱或缺失

**解决方案**：
1. 使用语义化 HTML：
   ```html
   <!-- ✅ 推荐 -->
   <nav>
     <ul>
       <li><a href="/">Home</a></li>
     </ul>
   </nav>
   
   <!-- ❌ 不推荐 -->
   <div class="nav">
     <div class="item">Home</div>
   </div>
   ```
2. 正确使用 ARIA 属性：
   ```html
   <!-- ✅ 推荐：提供有意义的标签 -->
   <button aria-label="关闭对话框">×</button>
   
   <!-- ❌ 不推荐：屏幕阅读器只会读"乘号" -->
   <button>×</button>
   ```
3. 使用 aria-live 通知动态变化：
   ```html
   <div aria-live="polite" aria-atomic="true">
     <!-- 动态内容 -->
   </div>
   ```

### 问题6：表单可访问性问题

**症状**：表单控件缺少标签或错误提示不清晰

**解决方案**：
1. 关联 label 和 input：
   ```html
   <!-- ✅ 推荐：显式关联 -->
   <label for="email">邮箱</label>
   <input id="email" type="email" />
   
   <!-- ✅ 推荐：隐式关联 -->
   <label>
     邮箱
     <input type="email" />
   </label>
   ```
2. 提供清晰的错误提示：
   ```html
   <input
     id="email"
     type="email"
     aria-invalid="true"
     aria-describedby="email-error"
   />
   <span id="email-error" role="alert">
     请输入有效的邮箱地址
   </span>
   ```
3. 使用 fieldset 和 legend 分组：
   ```html
   <fieldset>
     <legend>联系方式</legend>
     <!-- 表单控件 -->
   </fieldset>
   ```

### 问题7：CI 环境中测试失败

**症状**：本地通过但 CI 环境中可访问性测试失败

**解决方案**：
1. 确保 CI 环境安装了浏览器：
   ```yaml
   - name: Install Playwright
     run: npx playwright install --with-deps
   ```
2. 检查环境差异（字体、渲染）
3. 保存失败时的截图和报告：
   ```typescript
   if (violations.length > 0) {
     await page.screenshot({ path: 'a11y-violations.png' });
     fs.writeFileSync('a11y-report.json', JSON.stringify(violations));
   }
   ```
4. 使用 Docker 容器保证环境一致性

### 获取更多帮助

如果问题仍未解决：
1. 查看 [FAQ.md](../../../FAQ.md)
2. 查看示例的 README.md 文件
3. 参考 WCAG 2.1 官方文档
4. 使用 WebAIM 资源
5. 提交新的 Issue 并附上详细信息

**相关技能：** functional-testing、manual-testing、automation-testing、test-case-writing。
