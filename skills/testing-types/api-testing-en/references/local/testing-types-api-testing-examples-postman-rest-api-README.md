# Local Reference

This file is an in-skill formal reference migrated from `_external`.

Original file: `testing-types__api-testing__examples__postman-rest-api__README.md`

---

# Snapshot Reference

This file is a localized snapshot for skill portability.

---
# Postman REST API 测试示例

这是一个完整的 Postman 集合示例，演示如何测试 RESTful API。

## 📋 测试覆盖

### CRUD 操作测试
- ✅ GET - 获取资源列表
- ✅ GET - 获取单个资源
- ✅ POST - 创建资源
- ✅ PUT - 更新资源
- ✅ PATCH - 部分更新资源
- ✅ DELETE - 删除资源

### 高级测试
- ✅ 认证和授权（Bearer Token, API Key）
- ✅ 查询参数和过滤
- ✅ 分页测试
- ✅ 排序测试
- ✅ 错误处理（4xx, 5xx）
- ✅ 响应时间验证
- ✅ 数据验证（Schema Validation）

## 🚀 快速开始

### 1. 导入 Postman 集合

1. 打开 Postman
2. 点击 "Import"
3. 选择 `User-API-Tests.postman_collection.json`
4. 导入环境变量 `API-Environment.postman_environment.json`

### 2. 配置环境变量

在 Postman 中选择 "API-Environment" 环境，配置以下变量：

```
baseUrl: https://jsonplaceholder.typicode.com
apiKey: your-api-key-here
token: (自动生成)
userId: (自动生成)
```

### 3. 运行测试

#### 方式 1: 在 Postman 中运行
1. 选择集合 "User API Tests"
2. 点击 "Run" 按钮
3. 选择环境和迭代次数
4. 点击 "Run User API Tests"

#### 方式 2: 使用 Newman 命令行运行
```bash
# 安装 Newman
npm install -g newman

# 运行测试
newman run User-API-Tests.postman_collection.json \
  -e API-Environment.postman_environment.json \
  --reporters cli,html \
  --reporter-html-export report.html
```

## 📁 文件说明

```
postman-rest-api/
├── User-API-Tests.postman_collection.json    # Postman 测试集合
├── API-Environment.postman_environment.json  # 环境变量配置
├── newman-run.sh                             # Newman 运行脚本
└── README.md                                 # 本文档
```

## 🎯 测试用例详解

### 1. GET /users - 获取用户列表

**测试点**:
- 状态码为 200
- 响应时间 < 500ms
- 返回数组
- 数组不为空
- 每个用户包含必需字段

**测试脚本**:
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

pm.test("Response is an array", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('array');
});

pm.test("Array is not empty", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.length).to.be.above(0);
});

pm.test("Each user has required fields", function () {
    const jsonData = pm.response.json();
    jsonData.forEach(user => {
        pm.expect(user).to.have.property('id');
        pm.expect(user).to.have.property('name');
        pm.expect(user).to.have.property('email');
    });
});
```

### 2. GET /users/:id - 获取单个用户

**测试点**:
- 状态码为 200
- 返回对象
- 包含正确的用户 ID
- Email 格式正确
- 保存用户 ID 到环境变量

**测试脚本**:
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response is an object", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.be.an('object');
});

pm.test("User ID matches request", function () {
    const jsonData = pm.response.json();
    const requestedId = pm.variables.get("userId");
    pm.expect(jsonData.id).to.eql(parseInt(requestedId));
});

pm.test("Email format is valid", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData.email).to.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/);
});

// 保存用户 ID 到环境变量
const jsonData = pm.response.json();
pm.environment.set("userId", jsonData.id);
```

### 3. POST /users - 创建用户

**测试点**:
- 状态码为 201
- 返回创建的用户对象
- 包含新生成的 ID
- 数据与请求一致

**请求体**:
```json
{
  "name": "Test User",
  "email": "test@example.com",
  "username": "testuser"
}
```

**测试脚本**:
```javascript
pm.test("Status code is 201", function () {
    pm.response.to.have.status(201);
});

pm.test("Response has id", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('id');
    pm.expect(jsonData.id).to.be.a('number');
});

pm.test("Response data matches request", function () {
    const jsonData = pm.response.json();
    const requestData = JSON.parse(pm.request.body.raw);
    
    pm.expect(jsonData.name).to.eql(requestData.name);
    pm.expect(jsonData.email).to.eql(requestData.email);
    pm.expect(jsonData.username).to.eql(requestData.username);
});

// 保存新用户 ID
const jsonData = pm.response.json();
pm.environment.set("newUserId", jsonData.id);
```

### 4. PUT /users/:id - 更新用户

**测试点**:
- 状态码为 200
- 返回更新后的用户对象
- 所有字段都已更新

**请求体**:
```json
{
  "name": "Updated User",
  "email": "updated@example.com",
  "username": "updateduser"
}
```

### 5. PATCH /users/:id - 部分更新

**测试点**:
- 状态码为 200
- 只更新指定字段
- 其他字段保持不变

**请求体**:
```json
{
  "email": "newemail@example.com"
}
```

### 6. DELETE /users/:id - 删除用户

**测试点**:
- 状态码为 200 或 204
- 响应体为空或包含确认信息

**测试脚本**:
```javascript
pm.test("Status code is 200 or 204", function () {
    pm.expect(pm.response.code).to.be.oneOf([200, 204]);
});

pm.test("Response is empty or contains confirmation", function () {
    if (pm.response.code === 200) {
        const jsonData = pm.response.json();
        pm.expect(jsonData).to.be.an('object');
    }
});
```

### 7. 错误处理测试

#### 404 - 资源不存在
```javascript
pm.test("Status code is 404", function () {
    pm.response.to.have.status(404);
});

pm.test("Error message is present", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('error');
});
```

#### 400 - 无效请求
```javascript
pm.test("Status code is 400", function () {
    pm.response.to.have.status(400);
});

pm.test("Validation errors are present", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('errors');
    pm.expect(jsonData.errors).to.be.an('array');
});
```

#### 401 - 未授权
```javascript
pm.test("Status code is 401", function () {
    pm.response.to.have.status(401);
});

pm.test("WWW-Authenticate header is present", function () {
    pm.response.to.have.header('WWW-Authenticate');
});
```

## 🔧 高级功能

### 1. 认证测试

#### Bearer Token 认证
```javascript
// Pre-request Script
const token = pm.environment.get("token");
pm.request.headers.add({
    key: 'Authorization',
    value: `Bearer ${token}`
});
```

#### API Key 认证
```javascript
// Pre-request Script
const apiKey = pm.environment.get("apiKey");
pm.request.headers.add({
    key: 'X-API-Key',
    value: apiKey
});
```

### 2. 动态数据生成

```javascript
// Pre-request Script
const randomEmail = `user${Date.now()}@example.com`;
const randomName = `User ${Math.floor(Math.random() * 1000)}`;

pm.environment.set("randomEmail", randomEmail);
pm.environment.set("randomName", randomName);
```

### 3. 链式请求

```javascript
// 在创建用户后，自动使用新 ID 进行后续请求
const jsonData = pm.response.json();
pm.environment.set("userId", jsonData.id);

// 下一个请求会自动使用这个 ID
// GET /users/{{userId}}
```

### 4. Schema 验证

```javascript
const schema = {
    type: "object",
    required: ["id", "name", "email"],
    properties: {
        id: { type: "number" },
        name: { type: "string" },
        email: { type: "string", format: "email" },
        username: { type: "string" }
    }
};

pm.test("Schema is valid", function () {
    pm.response.to.have.jsonSchema(schema);
});
```

### 5. 性能测试

```javascript
pm.test("Response time is acceptable", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});

// 记录响应时间
console.log(`Response time: ${pm.response.responseTime}ms`);
```

## 📊 测试报告

### Newman HTML 报告

运行 Newman 后会生成 HTML 报告：

```bash
newman run User-API-Tests.postman_collection.json \
  -e API-Environment.postman_environment.json \
  --reporters html \
  --reporter-html-export report.html
```

报告包含：
- 总体统计（通过/失败/跳过）
- 每个请求的详细结果
- 响应时间图表
- 失败的测试详情

### CI/CD 集成

#### GitHub Actions
```yaml
name: API Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install Newman
        run: npm install -g newman
      - name: Run API Tests
        run: |
          newman run User-API-Tests.postman_collection.json \
            -e API-Environment.postman_environment.json \
            --reporters cli,junit \
            --reporter-junit-export results.xml
      - name: Publish Test Results
        uses: EnricoMi/publish-unit-test-result-action@v2
        if: always()
        with:
          files: results.xml
```

## 🐛 故障排除

### 问题 1: 环境变量未设置

**症状**: 请求失败，显示 "baseUrl is not defined"

**解决方案**:
1. 确保已导入环境文件
2. 在 Postman 右上角选择正确的环境
3. 检查环境变量是否正确配置

### 问题 2: 认证失败

**症状**: 401 Unauthorized

**解决方案**:
1. 检查 token 或 API key 是否正确
2. 确认 token 未过期
3. 检查 Authorization header 格式

### 问题 3: Newman 运行失败

**症状**: Newman 报错或测试失败

**解决方案**:
```bash
# 检查 Newman 版本
newman --version

# 使用 --verbose 查看详细日志
newman run collection.json --verbose

# 检查集合和环境文件是否有效
newman run collection.json --bail
```

## 📚 最佳实践

1. **使用环境变量**: 不要硬编码 URL 和凭据
2. **编写可重用的测试**: 使用 Pre-request Scripts 和 Tests
3. **测试独立性**: 每个测试应该独立运行
4. **清理数据**: 测试后清理创建的数据
5. **版本控制**: 将集合和环境文件加入版本控制
6. **文档化**: 为每个请求添加描述和示例

## 🔗 相关资源

- Postman 官方文档 (https://learning.postman.com/)
- Newman 文档 (https://github.com/postmanlabs/newman)
- Postman 测试脚本指南 (https://learning.postman.com/docs/writing-scripts/test-scripts/)
- JSONPlaceholder API (https://jsonplaceholder.typicode.com/)

## 📄 许可证

MIT License
