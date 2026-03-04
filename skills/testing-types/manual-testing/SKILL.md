---
name: manual-testing
description: Use this skill when you need to plan manual or exploratory testing with charters, heuristics, and session records; triggers include 手动测试 and exploratory testing.
---

# 手动/探索性测试（中文版）

**英文版：** 见技能 `manual-testing-en`。

提示词见本目录 `prompts/manual-testing.md`。

## 何时使用

- 用户提到「手动测试」「manual testing」「探索性测试」「exploratory testing」
- 需要设计手工测试方案或探索性测试章程
- **触发示例：**「设计探索性测试章程」「制定手工测试计划」

## 输出格式选项

本技能**默认输出为 Markdown**。若需其他格式，请在需求**末尾**明确说明。

## 如何使用

1. 打开本目录 `prompts/` 下对应提示词文件，复制虚线以下内容。
2. 附加你的需求与上下文（业务流程、环境、约束、验收标准）。
3. 若需非 Markdown 输出，在末尾追加 `output-formats.md` 中的请求句。

## 参考文件

- **[prompts/manual-testing.md](prompts/manual-testing.md)** — 手动测试提示词
- **[output-formats.md](output-formats.md)** — 格式说明

## 代码示例 | Code Examples

1. **探索性测试章程模板（计划中）** - 测试章程和会话记录模板

## 常见误区 | Common Pitfalls

- ❌ **无计划的随机测试** → ✅ 使用测试章程指导探索
- ❌ **不记录测试过程** → ✅ 详细记录测试会话
- ❌ **忽略启发式方法** → ✅ 应用测试启发式
- ❌ **缺少时间盒** → ✅ 设定明确的时间限制

## 最佳实践 | Best Practices

### 1. 探索性测试章程

```markdown
## 测试章程

**目标**: 探索登录功能的安全性
**范围**: 登录页面和认证流程
**时间**: 90 分钟
**测试人员**: 张三

**探索重点**:
- SQL 注入漏洞
- XSS 攻击
- 暴力破解防护
- Session 管理

**测试数据**:
- 特殊字符
- SQL 语句
- 脚本代码
- 超长字符串
```

### 2. 测试启发式（SFDPOT）

- **Structure（结构）**: 测试系统结构
- **Function（功能）**: 测试功能实现
- **Data（数据）**: 测试数据处理
- **Platform（平台）**: 测试平台兼容性
- **Operations（操作）**: 测试操作流程
- **Time（时间）**: 测试时间相关

### 3. 测试旅程（Tours）

- **商业区旅程**: 测试核心业务功能
- **历史区旅程**: 测试遗留功能
- **娱乐区旅程**: 测试有趣的功能
- **旅游区旅程**: 测试帮助和文档
- **破坏区旅程**: 尝试破坏系统

## 故障排除 | Troubleshooting

### 问题1：不知道从哪里开始探索

**解决方案**：
使用测试章程模板：
```markdown
**探索**: [功能/区域]
**使用**: [工具/方法]
**发现**: [问题/风险]
```

### 问题2：探索测试效率低

**解决方案**：
1. 设定时间盒（60-90分钟）
2. 使用启发式方法
3. 记录测试笔记
4. 定期回顾总结

**相关技能：** functional-testing、bug-reporting、test-case-writing。
