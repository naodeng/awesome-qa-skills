package com.example.api;

import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.anyOf;
import static org.hamcrest.Matchers.is;

public class HealthApiTest extends BaseApiTest {

    @Test
    void healthShouldBeReachable() {
        given()
            .spec(requestSpec)
        .when()
            .get("/health")
        .then()
            .statusCode(anyOf(is(200), is(404)));
    }
}
