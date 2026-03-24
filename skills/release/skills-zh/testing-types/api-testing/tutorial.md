# API 测试教程

## 📚 学习目标

完成本教程后，你将能够：
- 理解 RESTful API 测试的核心概念
- 使用 Postman 和 Newman 进行 API 测试
- 编写自动化 API 测试脚本
- 验证 API 响应和状态码
- 实现 API 测试的最佳实践

## 🎯 前置要求

- 理解 HTTP 协议基础（GET、POST、PUT、DELETE）
- 了解 JSON 数据格式
- 基本的命令行操作
- 安装 Node.js (v16+)

## 📖 教程内容

### 第1步：理解 API 测试（10分钟）

#### 1.1 什么是 API 测试？

API 测试是验证应用程序接口的功能、可靠性、性能和安全性的过程。

**测试内容包括：**
- ✅ 状态码验证（200, 404, 500 等）
- ✅ 响应数据验证（JSON 结构、字段类型）
- ✅ 响应时间验证
- ✅ 错误处理验证
- ✅ 认证和授权验证

#### 1.2 API 测试的优势

- 🚀 快速执行（无需 UI）
- 🔄 易于自动化
- 🎯 精准定位问题
- 📊 易于集成到 CI/CD

### 第2步：使用 Postman（20分钟）

#### 2.1 安装 Postman

下载并安装 [Postman](https://www.postman.com/downloads/)

#### 2.2 创建第一个请求

1. 打开 Postman
2. 点击 "New" → "HTTP Request"
3. 输入 URL: `https://jsonplaceholder.typicode.com/users/1`
4. 选择方法: GET
5. 点击 "Send"

#### 2.3 添加测试脚本

在 "Tests" 标签页添加：

```javascript
// 验证状态码
pm.test("状态码是 200", function () {
    pm.response.to.have.status(200);
});

// 验证响应时间
pm.test("响应时间小于 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

// 验证响应数据
pm.test("响应包含用户名", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('name');
    pm.expect(jsonData.name).to.be.a('string');
});

// 验证 JSON 结构
pm.test("用户对象结构正确", function () {
    const jsonData = pm.response.json();
    pm.expect(jsonData).to.have.all.keys(
        'id', 'name', 'username', 'email', 
        'address', 'phone', 'website', 'company'
    );
});
```

#### 2.4 使用环境变量

创建环境变量：
1. 点击右上角的齿轮图标
2. 添加环境 "Development"
3. 添加变量：
   - `base_url`: `https://jsonplaceholder.typicode.com`
   - `user_id`: `1`

使用变量：
```
{{base_url}}/users/{{user_id}}
```

### 第3步：创建测试集合（25分钟）

#### 3.1 创建用户 API 测试集合

**请求1: 获取所有用户 (GET)**
```
GET {{base_url}}/users
```

测试脚本：
```javascript
pm.test("状态码是 200", () => {
    pm.response.to.have.status(200);
});

pm.test("返回用户数组", () => {
    const users = pm.response.json();
    pm.expect(users).to.be.an('array');
    pm.expect(users.length).to.be.above(0);
});

pm.test("每个用户有必需字段", () => {
    const users = pm.response.json();
    users.forEach(user => {
        pm.expect(user).to.have.property('id');
        pm.expect(user).to.have.property('name');
        pm.expect(user).to.have.property('email');
    });
});
```

**请求2: 创建用户 (POST)**
```
POST {{base_url}}/users
Content-Type: application/json

{
  "name": "测试用户",
  "username": "testuser",
  "email": "test@example.com"
}
```

测试脚本：
```javascript
pm.test("状态码是 201", () => {
    pm.response.to.have.status(201);
});

pm.test("返回创建的用户", () => {
    const user = pm.response.json();
    pm.expect(user).to.have.property('id');
    pm.expect(user.name).to.eql("测试用户");
    
    // 保存用户 ID 供后续使用
    pm.environment.set("created_user_id", user.id);
});
```

**请求3: 更新用户 (PUT)**
```
PUT {{base_url}}/users/{{created_user_id}}
Content-Type: application/json

{
  "name": "更新的用户",
  "email": "updated@example.com"
}
```

**请求4: 删除用户 (DELETE)**
```
DELETE {{base_url}}/users/{{created_user_id}}
```

测试脚本：
```javascript
pm.test("状态码是 200", () => {
    pm.response.to.have.status(200);
});
```

### 第4步：使用 Newman 自动化（15分钟）

#### 4.1 安装 Newman

```bash
npm install -g newman
```

#### 4.2 导出 Postman 集合

1. 在 Postman 中点击集合旁的 "..."
2. 选择 "Export"
3. 保存为 `user-api-tests.json`

#### 4.3 运行测试

```bash
# 基本运行
newman run user-api-tests.json

# 使用环境变量
newman run user-api-tests.json -e environment.json

# 生成 HTML 报告
newman run user-api-tests.json -r html --reporter-html-export report.html

# 生成 JSON 报告
newman run user-api-tests.json -r json --reporter-json-export report.json
```

### 第5步：使用代码编写测试（30分钟）

#### 5.1 使用 Supertest (Node.js)

安装依赖：
```bash
npm install --save-dev supertest jest
```

创建 `tests/api.test.js`：

```javascript
const request = require('supertest');

const baseURL = 'https://jsonplaceholder.typicode.com';

describe('用户 API 测试', () => {
  test('获取所有用户', async () => {
    const response = await request(baseURL)
      .get('/users')
      .expect(200)
      .expect('Content-Type', /json/);
    
    expect(Array.isArray(response.body)).toBe(true);
    expect(response.body.length).toBeGreaterThan(0);
  });

  test('获取单个用户', async () => {
    const response = await request(baseURL)
      .get('/users/1')
      .expect(200);
    
    expect(response.body).toHaveProperty('id', 1);
    expect(response.body).toHaveProperty('name');
    expect(response.body).toHaveProperty('email');
  });

  test('创建用户', async () => {
    const newUser = {
      name: '测试用户',
      username: 'testuser',
      email: 'test@example.com'
    };

    const response = await request(baseURL)
      .post('/users')
      .send(newUser)
      .expect(201)
      .expect('Content-Type', /json/);
    
    expect(response.body).toHaveProperty('id');
    expect(response.body.name).toBe(newUser.name);
  });

  test('更新用户', async () => {
    const updatedUser = {
      name: '更新的用户',
      email: 'updated@example.com'
    };

    const response = await request(baseURL)
      .put('/users/1')
      .send(updatedUser)
      .expect(200);
    
    expect(response.body.name).toBe(updatedUser.name);
  });

  test('删除用户', async () => {
    await request(baseURL)
      .delete('/users/1')
      .expect(200);
  });

  test('处理 404 错误', async () => {
    await request(baseURL)
      .get('/users/9999')
      .expect(404);
  });
});
```

运行测试：
```bash
npx jest
```

#### 5.2 使用 REST Assured (Java)

创建 `UserApiTest.java`：

```java
import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class UserApiTest {
    
    @BeforeAll
    public static void setup() {
        RestAssured.baseURI = "https://jsonplaceholder.typicode.com";
    }
    
    @Test
    public void testGetAllUsers() {
        given()
            .when()
            .get("/users")
            .then()
            .statusCode(200)
            .body("$", hasSize(greaterThan(0)))
            .body("[0]", hasKey("id"))
            .body("[0]", hasKey("name"));
    }
    
    @Test
    public void testGetSingleUser() {
        given()
            .pathParam("id", 1)
            .when()
            .get("/users/{id}")
            .then()
            .statusCode(200)
            .body("id", equalTo(1))
            .body("name", notNullValue())
            .body("email", containsString("@"));
    }
    
    @Test
    public void testCreateUser() {
        String requestBody = """
            {
                "name": "测试用户",
                "username": "testuser",
                "email": "test@example.com"
            }
            """;
        
        given()
            .contentType("application/json")
            .body(requestBody)
            .when()
            .post("/users")
            .then()
            .statusCode(201)
            .body("name", equalTo("测试用户"))
            .body("id", notNullValue());
    }
}
```

### 第6步：高级技巧（20分钟）

#### 6.1 认证测试

**Bearer Token 认证：**
```javascript
pm.test("使用 Token 认证", () => {
    pm.sendRequest({
        url: '{{base_url}}/protected',
        method: 'GET',
        header: {
            'Authorization': 'Bearer ' + pm.environment.get('access_token')
        }
    }, (err, response) => {
        pm.expect(response.code).to.equal(200);
    });
});
```

**Basic 认证：**
```javascript
const response = await request(baseURL)
  .get('/protected')
  .auth('username', 'password')
  .expect(200);
```

#### 6.2 数据驱动测试

```javascript
const testData = [
  { userId: 1, expectedName: 'Leanne Graham' },
  { userId: 2, expectedName: 'Ervin Howell' },
  { userId: 3, expectedName: 'Clementine Bauch' }
];

describe('数据驱动测试', () => {
  testData.forEach(({ userId, expectedName }) => {
    test(`验证用户 ${userId} 的名称`, async () => {
      const response = await request(baseURL)
        .get(`/users/${userId}`)
        .expect(200);
      
      expect(response.body.name).toBe(expectedName);
    });
  });
});
```

#### 6.3 链式请求

```javascript
describe('链式 API 调用', () => {
  let createdUserId;

  test('创建用户并获取详情', async () => {
    // 1. 创建用户
    const createResponse = await request(baseURL)
      .post('/users')
      .send({ name: '测试用户', email: 'test@example.com' })
      .expect(201);
    
    createdUserId = createResponse.body.id;

    // 2. 获取创建的用户
    const getResponse = await request(baseURL)
      .get(`/users/${createdUserId}`)
      .expect(200);
    
    expect(getResponse.body.name).toBe('测试用户');

    // 3. 更新用户
    await request(baseURL)
      .put(`/users/${createdUserId}`)
      .send({ name: '更新的用户' })
      .expect(200);

    // 4. 删除用户
    await request(baseURL)
      .delete(`/users/${createdUserId}`)
      .expect(200);
  });
});
```

#### 6.4 Schema 验证

```javascript
const Ajv = require('ajv');
const ajv = new Ajv();

const userSchema = {
  type: 'object',
  required: ['id', 'name', 'email'],
  properties: {
    id: { type: 'number' },
    name: { type: 'string' },
    email: { type: 'string', format: 'email' },
    phone: { type: 'string' }
  }
};

test('验证响应 Schema', async () => {
  const response = await request(baseURL)
    .get('/users/1')
    .expect(200);
  
  const valid = ajv.validate(userSchema, response.body);
  expect(valid).toBe(true);
});
```

### 第7步：性能测试（15分钟）

#### 7.1 响应时间测试

```javascript
test('API 响应时间测试', async () => {
  const start = Date.now();
  
  await request(baseURL)
    .get('/users')
    .expect(200);
  
  const duration = Date.now() - start;
  expect(duration).toBeLessThan(500); // 小于 500ms
});
```

#### 7.2 并发测试

```javascript
test('并发请求测试', async () => {
  const requests = Array(10).fill(null).map(() =>
    request(baseURL).get('/users/1')
  );
  
  const responses = await Promise.all(requests);
  
  responses.forEach(response => {
    expect(response.status).toBe(200);
  });
});
```

## 🎓 练习任务

### 初级练习
1. 测试一个公开 API（如 JSONPlaceholder）的所有端点
2. 验证不同的 HTTP 状态码（200, 201, 404, 500）
3. 测试 API 的错误处理

### 中级练习
1. 实现完整的 CRUD 测试流程
2. 使用环境变量管理不同环境的配置
3. 实现数据驱动的 API 测试

### 高级练习
1. 实现 API 认证和授权测试
2. 创建 API 性能基准测试
3. 实现 API 契约测试（Contract Testing）

## 📚 延伸阅读

- [REST API 设计最佳实践](https://restfulapi.net/)
- [HTTP 状态码详解](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status)
- [API 测试策略](https://martinfowler.com/articles/practical-test-pyramid.html#ContractTests)
- [Postman 学习中心](https://learning.postman.com/)

## 🔗 相关资源

- [Postman 示例集合](examples/)
- [Supertest 示例代码](examples/)
- [API 测试 Skill](./SKILL.md)
- [快速开始指南](./quick-start.md)

## ❓ 常见问题

### Q: 如何处理 API 认证？
A: 
- Bearer Token: 在 Header 中添加 `Authorization: Bearer <token>`
- Basic Auth: 使用 `.auth(username, password)`
- API Key: 在 Header 或 Query 参数中添加

### Q: 如何测试异步 API？
A: 
- 使用轮询机制检查状态
- 使用 WebSocket 监听事件
- 设置合理的超时时间

### Q: 如何组织大量的 API 测试？
A: 
- 按功能模块分组
- 使用 describe 嵌套组织测试
- 提取公共的 setup 和 teardown 逻辑

## 🎉 下一步

完成本教程后，你可以：
- 学习 [自动化测试教程](references/local/testing-types-automation-testing-tutorial.md)
- 探索 [性能测试教程](references/local/testing-types-performance-testing-tutorial.md)
- 查看 [安全测试教程](references/local/testing-types-security-testing-SKILL.md)

---

*预计完成时间: 2-3 小时*  
*难度级别: 初级到中级*
