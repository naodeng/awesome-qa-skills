# REST Assured API 测试示例

使用 REST Assured 和 JUnit 5 进行 Java API 测试的完整示例。

## 📋 项目概述

本示例展示了如何使用 REST Assured 进行：
- RESTful API 的 CRUD 操作测试
- 请求和响应验证
- JSON 数据断言
- 响应时间测试
- 请求头和响应头验证

## 🚀 快速开始

### 前置要求

- Java 11 或更高版本
- Maven 3.6 或更高版本

### 1. 构建项目

```bash
mvn clean compile
```

### 2. 运行测试

```bash
mvn test
```

### 3. 运行特定测试类

```bash
mvn test -Dtest=UserApiTest
```

### 4. 生成测试报告

```bash
mvn surefire-report:report
```

报告位置：`target/surefire-reports/`

## 📁 项目结构

```
rest-assured-java/
├── src/
│   └── test/
│       └── java/
│           └── com/
│               └── example/
│                   └── UserApiTest.java
├── pom.xml
└── README.md
```

## 🧪 测试用例

### UserApiTest.java

| 测试方法 | 描述 | HTTP 方法 |
|---------|------|-----------|
| testGetAllUsers | 获取所有用户 | GET |
| testGetUserById | 获取单个用户 | GET |
| testGetNonExistentUser | 获取不存在的用户 | GET |
| testCreateUser | 创建新用户 | POST |
| testCreateUserWithMissingFields | 创建用户（缺少字段） | POST |
| testUpdateUser | 更新用户 | PUT |
| testPatchUser | 部分更新用户 | PATCH |
| testDeleteUser | 删除用户 | DELETE |
| testFilterUsersByUsername | 过滤用户 | GET |
| testResponseTime | 响应时间测试 | GET |
| testResponseHeaders | 响应头测试 | GET |
| testExtractResponseData | 提取响应数据 | GET |

## 📝 REST Assured 基础用法

### 1. 基本请求

```java
given()
    .contentType(ContentType.JSON)
.when()
    .get("/users")
.then()
    .statusCode(200);
```

### 2. 路径参数

```java
given()
    .pathParam("id", 1)
.when()
    .get("/users/{id}")
.then()
    .statusCode(200);
```

### 3. 查询参数

```java
given()
    .queryParam("username", "john")
    .queryParam("page", 1)
.when()
    .get("/users")
.then()
    .statusCode(200);
```

### 4. 请求体

```java
String requestBody = """
    {
        "name": "John Doe",
        "email": "john@example.com"
    }
    """;

given()
    .contentType(ContentType.JSON)
    .body(requestBody)
.when()
    .post("/users")
.then()
    .statusCode(201);
```

### 5. 请求头

```java
given()
    .header("Authorization", "Bearer token")
    .header("Accept", "application/json")
.when()
    .get("/users")
.then()
    .statusCode(200);
```

## 🎯 断言技巧

### 1. 状态码断言

```java
.then()
    .statusCode(200)
    .statusCode(anyOf(equalTo(200), equalTo(201)))
```

### 2. 响应体断言

```java
.then()
    .body("name", equalTo("John Doe"))
    .body("email", notNullValue())
    .body("id", greaterThan(0))
    .body("users.size()", equalTo(10))
```

### 3. JSON 路径断言

```java
.then()
    .body("[0].name", equalTo("John"))
    .body("users[0].email", matchesPattern("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$"))
    .body("address.city", equalTo("New York"))
```

### 4. 响应头断言

```java
.then()
    .header("Content-Type", containsString("application/json"))
    .header("Cache-Control", notNullValue())
```

### 5. 响应时间断言

```java
.then()
    .time(lessThan(2000L))  // 毫秒
```

### 6. 集合断言

```java
.then()
    .body("users", hasSize(10))
    .body("users.name", hasItems("John", "Jane"))
    .body("users.id", everyItem(greaterThan(0)))
```

## 🔧 高级功能

### 1. 提取响应数据

```java
Response response = given()
    .when()
        .get("/users/1")
    .then()
        .statusCode(200)
    .extract()
        .response();

String name = response.path("name");
int id = response.path("id");
```

### 2. JSON Schema 验证

```java
given()
.when()
    .get("/users/1")
.then()
    .body(matchesJsonSchemaInClasspath("user-schema.json"));
```

### 3. 认证

```java
// Basic Auth
given()
    .auth().basic("username", "password")
.when()
    .get("/users")
.then()
    .statusCode(200);

// Bearer Token
given()
    .auth().oauth2("token")
.when()
    .get("/users")
.then()
    .statusCode(200);
```

### 4. 文件上传

```java
given()
    .multiPart("file", new File("test.txt"))
.when()
    .post("/upload")
.then()
    .statusCode(200);
```

### 5. 日志

```java
given()
    .log().all()  // 记录所有请求信息
.when()
    .get("/users")
.then()
    .log().all()  // 记录所有响应信息
    .statusCode(200);
```

### 6. 规范重用

```java
RequestSpecification requestSpec = new RequestSpecBuilder()
    .setBaseUri("https://api.example.com")
    .setContentType(ContentType.JSON)
    .addHeader("Authorization", "Bearer token")
    .build();

ResponseSpecification responseSpec = new ResponseSpecBuilder()
    .expectStatusCode(200)
    .expectContentType(ContentType.JSON)
    .build();

given()
    .spec(requestSpec)
.when()
    .get("/users")
.then()
    .spec(responseSpec);
```

## 🐛 调试技巧

### 1. 打印请求和响应

```java
given()
    .log().all()
.when()
    .get("/users")
.then()
    .log().all();
```

### 2. 仅在失败时打印

```java
given()
    .log().ifValidationFails()
.when()
    .get("/users")
.then()
    .log().ifValidationFails();
```

### 3. 打印特定部分

```java
.log().body()      // 仅打印响应体
.log().headers()   // 仅打印响应头
.log().status()    // 仅打印状态码
```

## 📊 测试报告

### Maven Surefire 报告

```bash
mvn surefire-report:report
```

### Allure 报告

1. 添加依赖：
```xml
<dependency>
    <groupId>io.qameta.allure</groupId>
    <artifactId>allure-junit5</artifactId>
    <version>2.24.0</version>
    <scope>test</scope>
</dependency>
```

2. 生成报告：
```bash
mvn clean test
mvn allure:serve
```

## 🚨 常见问题

### 1. 连接超时

```java
given()
    .config(RestAssured.config()
        .httpClient(HttpClientConfig.httpClientConfig()
            .setParam(CoreConnectionPNames.CONNECTION_TIMEOUT, 5000)
            .setParam(CoreConnectionPNames.SO_TIMEOUT, 5000)))
.when()
    .get("/users");
```

### 2. SSL 证书问题

```java
given()
    .relaxedHTTPSValidation()
.when()
    .get("https://example.com/users");
```

### 3. 代理设置

```java
given()
    .proxy("proxy.example.com", 8080)
.when()
    .get("/users");
```

## 📚 参考资源

- [REST Assured 官方文档](https://rest-assured.io/)
- [REST Assured GitHub](https://github.com/rest-assured/rest-assured)
- [JUnit 5 文档](https://junit.org/junit5/docs/current/user-guide/)
- [Hamcrest 文档](http://hamcrest.org/JavaHamcrest/)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT

---

*最后更新: 2026-02-09*
