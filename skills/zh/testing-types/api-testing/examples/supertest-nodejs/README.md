# Supertest API 测试示例

使用 Supertest 和 Jest 进行 Node.js API 测试的完整示例。

## 📋 项目概述

本示例展示了如何使用 Supertest 进行：
- RESTful API 的 CRUD 操作测试
- 请求和响应验证
- 查询参数和请求头测试
- 错误处理测试
- 响应时间测试

## 🚀 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 运行测试

```bash
npm test
```

### 3. 监听模式

```bash
npm run test:watch
```

### 4. 生成覆盖率报告

```bash
npm run test:coverage
```

## 📁 项目结构

```
supertest-nodejs/
├── tests/
│   └── users.test.js       # 用户 API 测试
├── package.json
└── README.md
```

## 🧪 测试用例

### User API Tests

| 测试组 | 测试数量 | 描述 |
|--------|---------|------|
| GET /users | 2 | 获取所有用户 |
| GET /users/:id | 3 | 获取单个用户 |
| POST /users | 3 | 创建新用户 |
| PUT /users/:id | 2 | 更新用户 |
| PATCH /users/:id | 1 | 部分更新用户 |
| DELETE /users/:id | 2 | 删除用户 |
| Query Parameters | 2 | 查询参数测试 |
| Headers | 2 | 请求头和响应头 |
| Error Handling | 2 | 错误处理 |
| Response Validation | 2 | 响应验证 |

### Posts API Tests

| 测试组 | 测试数量 | 描述 |
|--------|---------|------|
| GET /posts | 2 | 获取文章列表 |
| GET /users/:id/posts | 1 | 获取用户文章 |

## 📝 Supertest 基础用法

### 1. 基本 GET 请求

```javascript
const response = await request(baseURL)
  .get('/users')
  .expect(200)
  .expect('Content-Type', /json/);
```

### 2. POST 请求

```javascript
const response = await request(baseURL)
  .post('/users')
  .send({ name: 'John', email: 'john@example.com' })
  .set('Content-Type', 'application/json')
  .expect(201);
```

### 3. PUT 请求

```javascript
const response = await request(baseURL)
  .put('/users/1')
  .send({ name: 'John Updated' })
  .expect(200);
```

### 4. DELETE 请求

```javascript
await request(baseURL)
  .delete('/users/1')
  .expect(200);
```

### 5. 查询参数

```javascript
const response = await request(baseURL)
  .get('/users')
  .query({ username: 'john', page: 1 })
  .expect(200);
```

### 6. 自定义请求头

```javascript
const response = await request(baseURL)
  .get('/users')
  .set('Authorization', 'Bearer token')
  .set('Accept', 'application/json')
  .expect(200);
```

## 🎯 断言技巧

### 1. 状态码断言

```javascript
await request(baseURL)
  .get('/users')
  .expect(200);

// 或使用 Jest 断言
const response = await request(baseURL).get('/users');
expect(response.status).toBe(200);
```

### 2. 响应头断言

```javascript
await request(baseURL)
  .get('/users')
  .expect('Content-Type', /json/)
  .expect('Cache-Control', 'no-cache');

// 或使用 Jest 断言
const response = await request(baseURL).get('/users');
expect(response.headers['content-type']).toMatch(/json/);
```

### 3. 响应体断言

```javascript
const response = await request(baseURL)
  .get('/users/1')
  .expect(200);

// Jest 断言
expect(response.body).toHaveProperty('id', 1);
expect(response.body).toHaveProperty('name');
expect(response.body.email).toMatch(/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/);
```

### 4. 数组断言

```javascript
const response = await request(baseURL)
  .get('/users')
  .expect(200);

expect(response.body).toBeInstanceOf(Array);
expect(response.body.length).toBeGreaterThan(0);
expect(response.body[0]).toHaveProperty('id');
```

### 5. 嵌套对象断言

```javascript
const response = await request(baseURL)
  .get('/users/1')
  .expect(200);

expect(response.body).toHaveProperty('address');
expect(response.body.address).toHaveProperty('city');
expect(response.body.address.city).toBe('New York');
```

## 🔧 高级功能

### 1. 响应时间测试

```javascript
const startTime = Date.now();

await request(baseURL)
  .get('/users')
  .expect(200);

const endTime = Date.now();
const responseTime = endTime - startTime;

expect(responseTime).toBeLessThan(2000); // 2秒内
```

### 2. 超时设置

```javascript
await request(baseURL)
  .get('/users')
  .timeout(5000)  // 5秒超时
  .expect(200);
```

### 3. 重定向

```javascript
await request(baseURL)
  .get('/redirect')
  .redirects(5)  // 最多跟随5次重定向
  .expect(200);
```

### 4. 文件上传

```javascript
await request(baseURL)
  .post('/upload')
  .attach('file', 'path/to/file.txt')
  .expect(200);
```

### 5. 表单数据

```javascript
await request(baseURL)
  .post('/form')
  .field('name', 'John')
  .field('email', 'john@example.com')
  .expect(200);
```

### 6. 认证

```javascript
// Bearer Token
await request(baseURL)
  .get('/users')
  .set('Authorization', 'Bearer your-token')
  .expect(200);

// Basic Auth
await request(baseURL)
  .get('/users')
  .auth('username', 'password')
  .expect(200);
```

## 🧩 与 Jest 集成

### 1. 测试套件组织

```javascript
describe('User API', () => {
  describe('GET /users', () => {
    it('should return all users', async () => {
      // 测试代码
    });
  });

  describe('POST /users', () => {
    it('should create a new user', async () => {
      // 测试代码
    });
  });
});
```

### 2. 测试钩子

```javascript
describe('User API', () => {
  let userId;

  beforeAll(async () => {
    // 所有测试前执行一次
  });

  afterAll(async () => {
    // 所有测试后执行一次
  });

  beforeEach(async () => {
    // 每个测试前执行
  });

  afterEach(async () => {
    // 每个测试后执行
  });

  it('test case', async () => {
    // 测试代码
  });
});
```

### 3. 测试数据准备

```javascript
const testUser = {
  name: 'Test User',
  email: 'test@example.com'
};

beforeEach(() => {
  // 重置测试数据
});
```

## 🐛 调试技巧

### 1. 打印响应

```javascript
const response = await request(baseURL)
  .get('/users/1')
  .expect(200);

console.log('Response:', response.body);
console.log('Headers:', response.headers);
console.log('Status:', response.status);
```

### 2. 使用 Jest 的 --verbose

```bash
npm test -- --verbose
```

### 3. 运行单个测试

```bash
npm test -- --testNamePattern="should return all users"
```

### 4. 调试模式

```bash
node --inspect-brk node_modules/.bin/jest --runInBand
```

## 📊 测试报告

### Jest 内置报告

```bash
npm test
```

### 覆盖率报告

```bash
npm run test:coverage
```

报告位置：`coverage/lcov-report/index.html`

### HTML 报告

安装 jest-html-reporter:

```bash
npm install --save-dev jest-html-reporter
```

配置 package.json:

```json
{
  "jest": {
    "reporters": [
      "default",
      ["jest-html-reporter", {
        "pageTitle": "API Test Report",
        "outputPath": "test-report.html"
      }]
    ]
  }
}
```

## 🚨 常见问题

### 1. 超时错误

**问题**: `Timeout - Async callback was not invoked within the 5000ms timeout`

**解决方案**:
```javascript
it('test case', async () => {
  // 测试代码
}, 10000); // 增加超时时间到10秒
```

### 2. 异步测试

**问题**: 测试提前结束

**解决方案**: 使用 async/await 或返回 Promise
```javascript
it('test case', async () => {
  await request(baseURL).get('/users');
});
```

### 3. 连接错误

**问题**: `ECONNREFUSED`

**解决方案**: 确保 API 服务器正在运行，或使用正确的 URL

## 📚 参考资源

- [Supertest GitHub](https://github.com/visionmedia/supertest)
- [Jest 官方文档](https://jestjs.io/)
- [Node.js HTTP 模块](https://nodejs.org/api/http.html)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT

---

*最后更新: 2026-02-09*
