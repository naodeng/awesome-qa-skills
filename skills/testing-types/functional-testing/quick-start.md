# 功能测试 - 快速开始 | Functional Testing - Quick Start

5 分钟快速上手功能测试 skill。

---

## 1. 这是什么？ | What is it?

功能测试 skill 帮助你设计全面的功能测试方案和测试用例，覆盖业务功能、UI、数据处理和系统集成。

## 2. 何时使用？ | When to use?

- ✅ 新功能开发完成，需要设计测试用例
- ✅ 需要验证业务逻辑的正确性
- ✅ 需要测试用户界面交互
- ✅ 需要验证数据处理流程
- ✅ 需要测试系统集成功能

## 3. 快速示例 | Quick Example

### 输入

```
@skill functional-testing

需求：用户登录功能

功能描述：
- 用户可以使用邮箱和密码登录
- 支持"记住我"功能
- 登录失败5次后锁定账户30分钟
- 密码可以显示/隐藏
```

### 预期输出

AI 会生成包含以下内容的功能测试方案：

1. **测试概述**
   - 测试目标、范围、方法、环境、周期

2. **功能测试用例**
   - 正常登录场景（有效凭据）
   - 异常场景（无效用户名、错误密码）
   - 边界值测试（空字段、特殊字符）
   - 记住我功能验证
   - 密码可见性切换
   - 账户锁定机制
   - 键盘导航测试

3. **验证点**
   - 输入验证、处理验证、输出验证
   - 状态验证、数据验证

4. **测试执行计划**
   - 阶段划分、资源需求、风险控制

5. **验收标准**
   - 通过标准、缺陷标准、覆盖率标准

## 4. 关键要点 | Key Points

### 测试设计方法
- **等价类划分**: 将输入分为有效和无效类
- **边界值分析**: 重点测试边界条件
- **决策表测试**: 处理复杂业务规则
- **状态转换测试**: 验证状态变化
- **场景测试**: 端到端用户场景

### 测试覆盖维度
- **功能覆盖**: 需求、用例、路径、条件
- **数据覆盖**: 有效、无效、边界、特殊数据
- **用户角色覆盖**: 不同权限和角色
- **环境覆盖**: 不同操作系统、浏览器、设备

### 输出格式选项
- **Markdown** (默认): 便于阅读和版本管理
- **Excel**: 制表符分隔，可粘贴到 Excel
- **CSV**: 逗号分隔，便于导入
- **JSON**: 便于程序解析
- **Jira/TestRail**: 直接导入测试管理工具

## 5. 实战技巧 | Practical Tips

### 技巧 1: 先分析需求
```
# 第一步：使用需求分析 skill
@skill requirements-analysis
[粘贴需求文档]

# 第二步：基于分析结果设计测试
@skill functional-testing
基于上述需求分析，设计功能测试用例
```

### 技巧 2: 使用代码示例
```bash
# 查看 Playwright 登录测试示例
cd skills/testing-types/functional-testing/examples/playwright-login
npm install
npm test
```

### 技巧 3: 指定输出格式
```
@skill functional-testing
需求：[你的需求]

请以 Excel 可粘贴的制表符分隔表格输出
```

### 技巧 4: 结合其他 skills
```
# 完整的测试流程
1. @skill requirements-analysis  # 分析需求
2. @skill test-strategy          # 制定策略
3. @skill functional-testing     # 设计测试
4. @skill automation-testing     # 自动化实现
5. @skill test-reporting         # 生成报告
```

## 6. 常见场景 | Common Scenarios

### 场景 1: Web 应用功能测试
```
@skill functional-testing
项目类型：Web 应用
技术栈：React + Node.js
需求：[具体功能需求]
```

### 场景 2: API 功能测试
```
@skill functional-testing
项目类型：RESTful API
需求：[API 端点和功能]
重点：数据验证、错误处理、状态码
```

### 场景 3: 移动应用功能测试
```
@skill functional-testing
项目类型：移动应用 (iOS/Android)
需求：[移动端功能]
重点：触摸交互、屏幕适配、离线功能
```

## 7. 下一步 | Next Steps

### 学习更多
- 📖 阅读完整文档：[SKILL.md](SKILL.md)
- 💻 尝试代码示例：[examples/](examples/)
- 📝 查看提示词：[prompts/functional-testing.md](prompts/functional-testing.md)

### 进阶学习
- 🎯 学习高级技巧：[prompts/advanced.md](prompts/advanced.md)
- 🔗 了解相关 skills：
  - [test-case-writing](../test-case-writing/) - 测试用例编写
  - [requirements-analysis](../requirements-analysis/) - 需求分析
  - [automation-testing](../automation-testing/) - 自动化测试
  - [test-strategy](../test-strategy/) - 测试策略

### 获取帮助
- ❓ 查看 [FAQ.md](../../../FAQ.md)
- 🐛 遇到问题？查看 SKILL.md 的"故障排除"章节
- 💬 提交 Issue 或参与讨论

## 8. 快速检查清单 | Quick Checklist

使用功能测试 skill 前，确保：

- [ ] 已充分理解功能需求
- [ ] 已识别核心业务逻辑
- [ ] 已明确用户角色和权限
- [ ] 已了解系统依赖和集成点
- [ ] 已准备好测试环境

设计测试用例时，确保覆盖：

- [ ] 正常场景（Happy Path）
- [ ] 异常场景（Error Handling）
- [ ] 边界值（Boundary Values）
- [ ] 特殊数据（Special Characters, Null, Empty）
- [ ] 用户体验（UX/UI）
- [ ] 可访问性（Accessibility）
- [ ] 安全性（Security）

---

**预计时间**: 5 分钟上手，30-60 分钟完成一个功能的测试设计

**难度级别**: 中级（Intermediate）

**推荐组合**: requirements-analysis → functional-testing → test-case-writing → automation-testing

---

**开始使用**:
```
@skill functional-testing
需求：[在此粘贴你的功能需求]
```

祝测试顺利！🚀
