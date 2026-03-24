# API 测试快速上手指南

5 分钟快速掌握 API 测试技能的使用方法。

## 📋 前置条件

- 了解基本的 HTTP 协议知识
- 熟悉 REST API 概念
- 安装 Postman（可选，用于可视化测试）

## 🚀 快速开始

### 步骤 1：选择测试工具

根据你的项目技术栈选择合适的工具：

| 场景 | 推荐工具 | 安装命令 |
|------|---------|---------|
| 快速手动测试 | Postman | [下载安装](https://www.postman.com/downloads/) |
| 自动化测试 | Newman | `npm install -g newman` |
| Python 项目 | Pytest + Requests | `pip install pytest requests` |
| Java 项目 | REST Assured | Maven/Gradle 依赖 |
| Node.js 项目 | SuperTest | `npm install supertest` |

### 步骤 2：运行示例测试

我们提供了一个完整的 Postman + Newman 示例：

```bash
# 1. 进入示例目录
cd skills/testing-types/api-testing/examples/postman-rest-api

# 2. 安装 Newman（如果还没安装）
npm install -g newman

# 3. 运行测试
./newman-run.sh

# 或者手动运行
newman run User-API-Tests.postman_collection.json \
  -e API-Environment.postman_environment.json
```

**预期输出：**
```
┌─────────────────────────┬──────────┬──────────┐
│                         │ executed │   failed │
├─────────────────────────┼──────────┼──────────┤
│              iterations │        1 │        0 │
├─────────────────────────┼──────────┼──────────┤
│                requests │       10 │        0 │
├─────────────────────────┼──────────┼──────────┤
│            test-scripts │       10 │        0 │
├─────────────────────────┼──────────┼──────────┤
│      prerequest-scripts │        0 │        0 │
├─────────────────────────┼──────────┼──────────┤
│              assertions │       35 │        0 │
└─────────────────────────┴──────────┴──────────┘
```

### 步骤 3：使用 AI 生成测试用例

1. **打开提示词文件**
   ```bash
   cat prompts/api-testing.md
   ```

2. **复制虚线以下的内容到 AI 对话**

3. **附加你的需求**，例如：
   ```
   为以下 API 生成测试用例：
   
   POST /api/v1/orders
   请求体：
   {
     "userId": "string",
     "items": [
       {
         "productId": "string",
         "quantity": number
       }
     ],
     "totalAmount": number
   }
   
   响应：
   - 201: 订单创建成功
   - 400: 请求参数错误
   - 401: 未授权
   ```

4. **AI 将生成**：
   - 完整的测试用例列表
   - 测试数据
   - 预期结果
   - 可选：Postman 集合 JSON

### 步骤 4：自定义输出格式

如果需要 Excel、CSV 或 JSON 格式，在需求末尾添加：

```
请以 Excel 格式输出，包含以下列：
- 用例编号
- 用例标题
- 前置条件
- 测试步骤
- 预期结果
- 优先级
```

详见 [output-formats.md](output-formats.md)

## 📝 实战示例

### 示例 1：测试用户注册 API

**需求：**
```
为用户注册 API 生成测试用例

API 端点：POST /api/v1/users/register
请求参数：
- username: 字符串，3-20 字符
- email: 邮箱格式
- password: 字符串，8-32 字符，需包含大小写字母和数字

响应：
- 201: 注册成功，返回用户信息
- 400: 参数验证失败
- 409: 用户名或邮箱已存在
```

**AI 输出：** 包含正常场景、边界值、异常场景等 15+ 个测试用例

### 示例 2：测试分页查询 API

**需求：**
```
为商品列表查询 API 生成测试用例

API 端点：GET /api/v1/products
查询参数：
- page: 页码，默认 1
- pageSize: 每页数量，默认 10，最大 100
- category: 分类 ID（可选）
- sortBy: 排序字段（可选）

需要测试分页逻辑、排序、过滤等功能
```

**AI 输出：** 包含分页边界、排序验证、过滤条件等测试用例

## 🎯 核心测试点

每个 API 测试应该覆盖：

### 1. 功能测试
- ✅ 正常场景：有效输入，验证正确响应
- ✅ 边界值：最小值、最大值、空值
- ✅ 异常场景：无效输入、缺失参数

### 2. 状态码验证
```javascript
// Postman Tests 示例
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

### 3. 响应结构验证
```javascript
pm.test("Response has correct structure", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property('id');
    pm.expect(jsonData).to.have.property('username');
    pm.expect(jsonData).to.have.property('email');
});
```

### 4. 响应数据验证
```javascript
pm.test("Username is correct", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.username).to.eql("testuser");
});
```

### 5. 响应时间验证
```javascript
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});
```

## 🔧 常用命令速查

### Newman 命令

```bash
# 基本运行
newman run collection.json

# 使用环境变量
newman run collection.json -e environment.json

# 生成 HTML 报告
newman run collection.json -r html --reporter-html-export report.html

# 运行特定文件夹
newman run collection.json --folder "User Management"

# 设置迭代次数
newman run collection.json -n 3

# 添加延迟（毫秒）
newman run collection.json --delay-request 500

# 首次失败时停止
newman run collection.json --bail

# 禁用 SSL 验证（仅开发环境）
newman run collection.json --insecure
```

### Postman 快捷键

| 快捷键 | 功能 |
|--------|------|
| `Ctrl/Cmd + Enter` | 发送请求 |
| `Ctrl/Cmd + S` | 保存请求 |
| `Ctrl/Cmd + N` | 新建请求 |
| `Ctrl/Cmd + E` | 导出集合 |
| `Ctrl/Cmd + ,` | 打开设置 |

## 📚 进阶学习

### 1. 学习 Postman 脚本

```javascript
// Pre-request Script：请求前执行
pm.environment.set("timestamp", Date.now());

// Tests：请求后执行
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});

// 保存响应数据供后续使用
var jsonData = pm.response.json();
pm.environment.set("userId", jsonData.id);
```

### 2. 使用动态变量

Postman 内置动态变量：
- `{{$guid}}` - 生成 GUID
- `{{$timestamp}}` - 当前时间戳
- `{{$randomInt}}` - 随机整数
- `{{$randomEmail}}` - 随机邮箱
- `{{$randomFirstName}}` - 随机名字

### 3. 集成到 CI/CD

```yaml
# GitHub Actions 示例
- name: Run API Tests
  run: |
    npm install -g newman
    newman run collection.json -e environment.json --reporters cli,json
```

### 4. 探索更多示例

查看 `examples/` 目录下的完整示例：
- REST API 测试
- GraphQL API 测试（即将推出）
- 认证和授权测试（即将推出）

## ❓ 遇到问题？

1. **查看故障排除章节**：[SKILL.md#故障排除](SKILL.md#故障排除)
2. **查看示例文档**：[examples/postman-rest-api/README.md](examples/postman-rest-api/README.md)
3. **参考官方文档**：
   - [Postman 文档](https://learning.postman.com/)
   - [Newman 文档](https://github.com/postmanlabs/newman)

## 🎓 下一步

- ✅ 完成快速上手
- 📖 阅读完整的 [SKILL.md](SKILL.md)
- 🔨 运行示例项目
- 🚀 为你的项目创建测试集合
- 🤖 使用 AI 提示词生成更多测试用例

---

**预计学习时间：** 5-10 分钟  
**难度级别：** 初级到中级  
**最后更新：** 2026-02-06
