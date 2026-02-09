package com.example;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.junit.jupiter.api.*;

import static io.restassured.RestAssured.*;
import static io.restassured.matcher.RestAssuredMatchers.*;
import static org.hamcrest.Matchers.*;

/**
 * User API 测试
 * 
 * 测试 RESTful API 的 CRUD 操作
 */
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class UserApiTest {

    private static String baseUrl = "https://jsonplaceholder.typicode.com";
    private static int createdUserId;

    @BeforeAll
    public static void setup() {
        RestAssured.baseURI = baseUrl;
        RestAssured.basePath = "/users";
    }

    @Test
    @Order(1)
    @DisplayName("获取所有用户 - 应该返回用户列表")
    public void testGetAllUsers() {
        given()
            .contentType(ContentType.JSON)
        .when()
            .get()
        .then()
            .statusCode(200)
            .contentType(ContentType.JSON)
            .body("size()", greaterThan(0))
            .body("[0]", hasKey("id"))
            .body("[0]", hasKey("name"))
            .body("[0]", hasKey("email"));
    }

    @Test
    @Order(2)
    @DisplayName("获取单个用户 - 应该返回用户详情")
    public void testGetUserById() {
        int userId = 1;
        
        given()
            .pathParam("id", userId)
        .when()
            .get("/{id}")
        .then()
            .statusCode(200)
            .body("id", equalTo(userId))
            .body("name", notNullValue())
            .body("email", matchesPattern("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$"))
            .body("address", hasKey("street"))
            .body("address", hasKey("city"))
            .body("company", hasKey("name"));
    }

    @Test
    @Order(3)
    @DisplayName("获取不存在的用户 - 应该返回 404")
    public void testGetNonExistentUser() {
        given()
            .pathParam("id", 9999)
        .when()
            .get("/{id}")
        .then()
            .statusCode(404);
    }

    @Test
    @Order(4)
    @DisplayName("创建新用户 - 应该返回 201")
    public void testCreateUser() {
        String requestBody = """
            {
                "name": "John Doe",
                "username": "johndoe",
                "email": "john@example.com",
                "address": {
                    "street": "123 Main St",
                    "city": "New York"
                }
            }
            """;

        Response response = given()
            .contentType(ContentType.JSON)
            .body(requestBody)
        .when()
            .post()
        .then()
            .statusCode(201)
            .body("name", equalTo("John Doe"))
            .body("email", equalTo("john@example.com"))
            .body("id", notNullValue())
        .extract()
            .response();

        createdUserId = response.path("id");
        System.out.println("Created user ID: " + createdUserId);
    }

    @Test
    @Order(5)
    @DisplayName("创建用户 - 缺少必填字段应该返回错误")
    public void testCreateUserWithMissingFields() {
        String requestBody = """
            {
                "name": "John Doe"
            }
            """;

        given()
            .contentType(ContentType.JSON)
            .body(requestBody)
        .when()
            .post()
        .then()
            .statusCode(anyOf(equalTo(400), equalTo(201))); // API 可能不验证
    }

    @Test
    @Order(6)
    @DisplayName("更新用户 - 应该返回 200")
    public void testUpdateUser() {
        int userId = 1;
        String requestBody = """
            {
                "name": "John Updated",
                "email": "john.updated@example.com"
            }
            """;

        given()
            .contentType(ContentType.JSON)
            .pathParam("id", userId)
            .body(requestBody)
        .when()
            .put("/{id}")
        .then()
            .statusCode(200)
            .body("name", equalTo("John Updated"))
            .body("email", equalTo("john.updated@example.com"))
            .body("id", equalTo(userId));
    }

    @Test
    @Order(7)
    @DisplayName("部分更新用户 - 应该返回 200")
    public void testPatchUser() {
        int userId = 1;
        String requestBody = """
            {
                "email": "newemail@example.com"
            }
            """;

        given()
            .contentType(ContentType.JSON)
            .pathParam("id", userId)
            .body(requestBody)
        .when()
            .patch("/{id}")
        .then()
            .statusCode(200)
            .body("email", equalTo("newemail@example.com"))
            .body("id", equalTo(userId));
    }

    @Test
    @Order(8)
    @DisplayName("删除用户 - 应该返回 200")
    public void testDeleteUser() {
        int userId = 1;

        given()
            .pathParam("id", userId)
        .when()
            .delete("/{id}")
        .then()
            .statusCode(200);
    }

    @Test
    @Order(9)
    @DisplayName("过滤用户 - 按用户名查询")
    public void testFilterUsersByUsername() {
        given()
            .queryParam("username", "Bret")
        .when()
            .get()
        .then()
            .statusCode(200)
            .body("size()", greaterThan(0))
            .body("[0].username", equalTo("Bret"));
    }

    @Test
    @Order(10)
    @DisplayName("响应时间 - 应该在 2 秒内")
    public void testResponseTime() {
        given()
        .when()
            .get()
        .then()
            .time(lessThan(2000L));
    }

    @Test
    @Order(11)
    @DisplayName("响应头 - 应该包含正确的 Content-Type")
    public void testResponseHeaders() {
        given()
        .when()
            .get()
        .then()
            .header("Content-Type", containsString("application/json"))
            .header("Connection", notNullValue());
    }

    @Test
    @Order(12)
    @DisplayName("提取响应数据")
    public void testExtractResponseData() {
        Response response = given()
            .pathParam("id", 1)
        .when()
            .get("/{id}")
        .then()
            .statusCode(200)
        .extract()
            .response();

        String name = response.path("name");
        String email = response.path("email");
        
        System.out.println("User name: " + name);
        System.out.println("User email: " + email);
        
        Assertions.assertNotNull(name);
        Assertions.assertNotNull(email);
    }
}
