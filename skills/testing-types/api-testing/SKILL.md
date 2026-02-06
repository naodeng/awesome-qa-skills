---
name: api-testing
version: 2.0.0
description: 默认输出 Markdown，可请求 Excel/CSV/JSON。Use for API 测试 or api-testing.
tags: [api, testing, rest, graphql, postman, newman]
difficulty: intermediate
last_updated: 2026-02-06
---

# API 测试（中文版）

**英文版：** 见技能 `api-testing-en`。

提示词见本目录 `prompts/api-testing.md`。

## 何时使用

- 用户提到「API 测试」「api-testing」
- 需要基于 Standard-version 执行该类测试或产出对应交付物
- **触发示例：**「根据以下内容生成/设计/编写…」

## 输出格式选项

默认 **Markdown**。若需 **Excel / CSV / JSON**，请在需求**末尾**说明，详见 **[output-formats.md](output-formats.md)**。

## 如何使用

1. 打开本目录 `prompts/api-testing.md`，将虚线以下内容复制到 AI 对话。
2. 附加你的具体需求。
3. 若需 Excel/CSV/JSON，在末尾加上 output-formats.md 中的请求句。

## 代码示例

### 1. Postman + Newman REST API 测试

完整的用户管理 API 测试示例，包含 10 个测试用例。

**位置：** `examples/postman-rest-api/`

**包含内容：**
- Postman 集合文件（10 个测试用例）
- 环境变量配置
- Newman 自动化运行脚本
- 详细的 README 文档

**快速开始：**
```bash
cd examples/postman-rest-api
npm install -g newman
./newman-run.sh
```

**测试覆盖：**
- 用户 CRUD 操作（创建、读取、更新、删除）
- 认证和授权测试
- 错误处理和边界条件
- 响应时间验证
- 数据格式验证

详见：[examples/postman-rest-api/README.md](examples/postman-rest-api/README.md)

## 最佳实践

### API 测试设计原则

1. **测试金字塔**
   - 单元测试：测试单个 API 端点
   - 集成测试：测试多个端点的交互
   - 端到端测试：测试完整的业务流程

2. **测试数据管理**
   - 使用环境变量管理不同环境配置
   - 使用动态变量避免硬编码
   - 测试后清理数据

3. **断言策略**
   - 验证状态码
   - 验证响应结构（Schema Validation）
   - 验证响应数据
   - 验证响应时间

4. **错误处理**
   - 测试各种错误场景（4xx, 5xx）
   - 验证错误消息格式
   - 测试边界条件

### 工具选择建议

| 工具 | 适用场景 | 优势 |
|------|---------|------|
| Postman/Newman | REST API 测试 | 易用、可视化、CI/CD 集成 |
| REST Assured | Java 项目 | 强类型、BDD 风格 |
| Pytest + Requests | Python 项目 | 灵活、生态丰富 |
| SuperTest | Node.js 项目 | 与 Express 集成好 |
| GraphQL Playground | GraphQL API | 专为 GraphQL 设计 |

## 故障排除

### 常见问题

#### 1. Newman 运行失败

**问题：** `newman: command not found`

**解决方案：**
```bash
# 全局安装 Newman
npm install -g newman

# 或使用 npx（无需全局安装）
npx newman run collection.json
```

#### 2. 环境变量未生效

**问题：** 测试中的变量显示为 `{{variable}}`

**解决方案：**
- 确保使用 `-e` 参数指定环境文件
- 检查环境文件中变量名是否正确
- 在 Postman 中验证变量是否正确设置

```bash
newman run collection.json -e environment.json
```

#### 3. 证书验证错误

**问题：** `SSL certificate problem`

**解决方案：**
```bash
# 开发环境可临时禁用 SSL 验证（不推荐生产环境）
newman run collection.json --insecure

# 或指定 CA 证书
newman run collection.json --ssl-client-cert-list cert-list.json
```

#### 4. 请求超时

**问题：** `Error: ETIMEDOUT` 或 `Error: ESOCKETTIMEDOUT`

**解决方案：**
```bash
# 增加超时时间（毫秒）
newman run collection.json --timeout-request 30000

# 添加请求延迟
newman run collection.json --delay-request 500
```

#### 5. 响应数据格式不匹配

**问题：** JSON Schema 验证失败

**解决方案：**
- 使用 Postman 的 Schema 生成功能
- 检查 API 文档确认数据结构
- 使用 `pm.response.json()` 打印实际响应

```javascript
// 在 Tests 中添加调试信息
console.log(pm.response.json());
```

#### 6. 动态数据依赖问题

**问题：** 后续请求依赖前一个请求的数据

**解决方案：**
```javascript
// 在第一个请求的 Tests 中保存数据
pm.environment.set("userId", pm.response.json().id);

// 在后续请求中使用
// URL: {{baseUrl}}/users/{{userId}}
```

#### 7. 批量运行测试失败

**问题：** 单个测试通过，批量运行失败

**解决方案：**
- 检查测试之间的数据依赖
- 确保每个测试独立可运行
- 添加适当的延迟：`--delay-request 200`
- 使用 `--bail` 在首次失败时停止

## 参考文件

- **prompts/api-testing.md** — API 测试 Standard-version 提示词
- **output-formats.md** — Markdown / Excel / CSV / JSON 请求说明
- **examples/postman-rest-api/** — Postman + Newman 完整示例
- **quick-start.md** — 5 分钟快速上手指南
