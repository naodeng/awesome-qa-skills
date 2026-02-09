# 测试工作流模板库

本目录包含常见测试场景的工作流模板，帮助团队快速建立标准化的测试流程。

---

## 📋 工作流列表

### 1. [新功能开发测试工作流](01-new-feature-testing.md)
**适用场景**: 开发新功能时的完整测试流程  
**涉及 Skills**: requirements-analysis, test-case-writing, functional-testing, automation-testing  
**预计时间**: 2-5 天

**关键步骤**:
1. 需求分析阶段
2. 测试设计阶段
3. 功能测试阶段
4. 自动化测试阶段

---

### 2. [Bug 修复验证工作流](02-bug-fix-verification.md)
**适用场景**: 验证 Bug 修复的完整流程  
**涉及 Skills**: bug-reporting, functional-testing, test-case-reviewer  
**预计时间**: 0.5-2 天

**关键步骤**:
1. Bug 分析阶段
2. 验证测试设计
3. Bug 验证执行
4. 测试用例评审

---

### 3. [回归测试工作流](03-regression-testing.md)
**适用场景**: 版本发布前的回归测试  
**涉及 Skills**: test-strategy, automation-testing, test-reporting  
**预计时间**: 1-3 天

**关键步骤**:
1. 回归测试计划
2. 测试环境准备
3. 回归测试执行
4. 测试报告和决策

---

### 4. [API 测试工作流](04-api-testing-workflow.md)
**适用场景**: RESTful API 的完整测试流程  
**涉及 Skills**: api-testing, automation-testing, performance-testing  
**预计时间**: 2-4 天

**关键步骤**:
1. API 测试设计
2. 功能测试执行
3. 自动化测试实现
4. 性能测试

---

### 5. [探索性测试工作流](05-exploratory-testing.md)
**适用场景**: 快速探索和发现未知问题  
**涉及 Skills**: manual-testing, bug-reporting, test-case-writing  
**预计时间**: 2-4 小时/会话

**关键步骤**:
1. 测试章程制定
2. 探索性测试执行
3. 问题记录和报告
4. 测试总结和用例提取

---

## 🎯 如何选择工作流

### 按项目阶段选择

| 阶段 | 推荐工作流 |
|------|-----------|
| 需求阶段 | 新功能开发测试工作流 |
| 开发阶段 | API 测试工作流、探索性测试工作流 |
| 测试阶段 | 回归测试工作流、Bug 修复验证工作流 |
| 发布阶段 | 回归测试工作流 |

### 按测试类型选择

| 测试类型 | 推荐工作流 |
|----------|-----------|
| 功能测试 | 新功能开发测试工作流 |
| API 测试 | API 测试工作流 |
| 回归测试 | 回归测试工作流 |
| 探索性测试 | 探索性测试工作流 |
| Bug 验证 | Bug 修复验证工作流 |

### 按团队规模选择

| 团队规模 | 推荐策略 |
|----------|----------|
| 1-2 人 | 简化流程，重点关注核心步骤 |
| 3-5 人 | 标准流程，适当分工 |
| 6+ 人 | 完整流程，明确角色分工 |

---

## 🔧 工作流定制

每个工作流都可以根据团队实际情况进行定制：

### 1. 调整步骤
- 根据项目复杂度增减步骤
- 合并或拆分某些阶段
- 调整步骤顺序

### 2. 调整时间
- 根据项目紧急程度调整时间盒
- 并行执行某些步骤
- 优先执行高风险区域

### 3. 调整工具
- 选择适合团队的工具
- 集成现有工具链
- 自动化重复性工作

---

## 📚 相关资源

### Skills 文档
- [Requirements Analysis](../../skills/testing-types/requirements-analysis/SKILL.md)
- [Test Case Writing](../../skills/testing-types/test-case-writing/SKILL.md)
- [Functional Testing](../../skills/testing-types/functional-testing/SKILL.md)
- [API Testing](../../skills/testing-types/api-testing/SKILL.md)
- [Automation Testing](../../skills/testing-types/automation-testing/SKILL.md)
- [Manual Testing](../../skills/testing-types/manual-testing/SKILL.md)
- [Bug Reporting](../../skills/testing-types/bug-reporting/SKILL.md)

### 模板文档
- [Skill Templates](../skill-templates/)
- [Output Templates](../output-templates/)

---

## 💡 最佳实践

1. **选择合适的工作流**: 根据项目特点选择最适合的工作流
2. **灵活调整**: 不要生搬硬套，根据实际情况调整
3. **持续改进**: 定期回顾和优化工作流
4. **团队共识**: 确保团队成员理解和认同工作流
5. **文档记录**: 记录工作流执行过程和改进点

---

## 🤝 贡献

欢迎贡献新的工作流模板！请参考 [贡献指南](../../CONTRIBUTING.md)。

---

*最后更新: 2026-02-09*
