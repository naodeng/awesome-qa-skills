# API 测试工作流

## 工作流概述

**适用场景**: RESTful API 的完整测试流程  
**涉及 Skills**: api-testing, automation-testing, performance-testing  
**预计时间**: 2-4 天

---

## 工作流步骤

### 1. API 测试设计

**使用 Skill**: `api-testing`

**输入**:
- API 文档（Swagger/OpenAPI）
- 接口规范
- 业务需求

**活动**:
```markdown
1. 分析 API 端点和参数
2. 设计功能测试用例
3. 设计边界和异常测试
4. 设计安全测试用例
```

**输出**:
- API 测试用例集
- 测试数据准备清单

---

### 2. 功能测试执行

**使用 Skill**: `api-testing`

**输入**:
- API 测试用例
- 测试环境

**活动**:
```markdown
1. 测试正常请求和响应
2. 测试参数验证
3. 测试错误处理
4. 测试业务逻辑
```

**测试维度**:
- ✅ 状态码验证
- ✅ 响应体验证
- ✅ 响应时间验证
- ✅ 数据格式验证
- ✅ 业务规则验证

**输出**:
- 功能测试报告
- 缺陷报告

---

### 3. 自动化测试实现

**使用 Skill**: `automation-testing`

**输入**:
- 稳定的 API 接口
- 核心测试用例

**活动**:
```markdown
1. 选择自动化工具（Postman/REST Assured/Supertest）
2. 编写自动化测试脚本
3. 实现数据驱动测试
4. 集成到 CI/CD
```

**输出**:
- 自动化测试脚本
- CI/CD 集成配置

---

### 4. 性能测试

**使用 Skill**: `performance-testing`

**输入**:
- 性能测试需求
- API 端点

**活动**:
```markdown
1. 设计性能测试场景
2. 执行负载测试
3. 执行压力测试
4. 分析性能瓶颈
```

**输出**:
- 性能测试报告
- 性能优化建议

---

## API 测试检查清单

### 功能测试
- [ ] 所有端点已测试
- [ ] 请求方法已验证（GET/POST/PUT/DELETE）
- [ ] 参数验证已测试
- [ ] 认证授权已测试
- [ ] 错误处理已测试
- [ ] 业务逻辑已验证

### 数据测试
- [ ] 数据格式验证（JSON/XML）
- [ ] 数据类型验证
- [ ] 必填字段验证
- [ ] 数据边界验证
- [ ] 特殊字符处理

### 安全测试
- [ ] 认证机制测试
- [ ] 授权控制测试
- [ ] SQL 注入测试
- [ ] XSS 攻击测试
- [ ] 敏感数据加密

### 性能测试
- [ ] 响应时间测试
- [ ] 并发测试
- [ ] 负载测试
- [ ] 压力测试
- [ ] 稳定性测试

---

## API 测试用例设计

### 1. 正向测试
```
测试用例: 创建用户 - 正常流程
请求方法: POST /api/users
请求体:
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
预期结果:
- 状态码: 201
- 响应体包含用户 ID
- 数据库中创建了用户记录
```

### 2. 边界测试
```
测试用例: 创建用户 - 年龄边界
请求方法: POST /api/users
请求体:
{
  "name": "Test User",
  "email": "test@example.com",
  "age": 0  // 边界值
}
预期结果:
- 状态码: 400
- 错误信息: "Age must be between 1 and 150"
```

### 3. 异常测试
```
测试用例: 创建用户 - 缺少必填字段
请求方法: POST /api/users
请求体:
{
  "name": "Test User"
  // 缺少 email
}
预期结果:
- 状态码: 400
- 错误信息: "Email is required"
```

---

## Postman 测试脚本示例

```javascript
// 测试状态码
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// 测试响应时间
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

// 测试响应体
pm.test("Response has user data", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('id');
    pm.expect(jsonData).to.have.property('name');
    pm.expect(jsonData.email).to.match(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/);
});

// 保存变量供后续使用
var jsonData = pm.response.json();
pm.environment.set("userId", jsonData.id);
```

---

## 最佳实践

1. **契约测试**: 使用 API 契约确保前后端一致
2. **数据隔离**: 使用独立的测试数据，避免污染生产数据
3. **环境管理**: 使用环境变量管理不同环境的配置
4. **持续集成**: 将 API 测试集成到 CI/CD 流程
5. **文档同步**: 保持测试用例与 API 文档同步

---

## 常见问题

**Q: API 测试和 UI 测试的区别？**  
A: API 测试直接测试接口逻辑，更快更稳定；UI 测试验证用户界面和交互。

**Q: 如何处理 API 依赖？**  
A: 使用 Mock Server 模拟依赖服务，或使用测试环境的真实服务。

**Q: 如何测试异步 API？**  
A: 使用轮询或 WebSocket 监听结果，设置合理的超时时间。

**Q: API 测试需要多少覆盖率？**  
A: 建议核心 API 达到 80% 以上覆盖率，包括正常和异常场景。

---

## 工具推荐

### 手工测试
- **Postman**: 功能强大的 API 测试工具
- **Insomnia**: 简洁的 REST 客户端
- **cURL**: 命令行 HTTP 工具

### 自动化测试
- **Newman**: Postman 的命令行工具
- **REST Assured**: Java API 测试框架
- **Supertest**: Node.js HTTP 测试库
- **Pytest + Requests**: Python API 测试

### 性能测试
- **K6**: 现代化性能测试工具
- **JMeter**: 经典性能测试工具
- **Gatling**: Scala 性能测试框架

---

## 相关模板

- [API 测试用例模板](../skill-templates/api-test-case-template.md)
- [API 测试报告模板](../skill-templates/api-test-report-template.md)
- [Postman Collection 模板](../output-templates/postman-collection-template.json)
