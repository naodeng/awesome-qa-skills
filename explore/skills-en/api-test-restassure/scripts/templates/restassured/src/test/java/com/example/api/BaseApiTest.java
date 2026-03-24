package com.example.api;

import io.restassured.builder.RequestSpecBuilder;
import io.restassured.specification.RequestSpecification;
import org.junit.jupiter.api.BeforeEach;

import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class BaseApiTest {
    protected RequestSpecification requestSpec;

    @BeforeEach
    void setupSpec() throws IOException {
        Properties props = new Properties();
        try (InputStream in = BaseApiTest.class.getClassLoader().getResourceAsStream("test.properties")) {
            if (in != null) {
                props.load(in);
            }
        }

        String baseUrl = System.getenv().getOrDefault("BASE_URL", props.getProperty("baseUrl", "https://api.example.com"));
        String token = System.getenv().getOrDefault("API_TOKEN", props.getProperty("token", "replace-me"));

        requestSpec = new RequestSpecBuilder()
            .setBaseUri(baseUrl)
            .addHeader("Content-Type", "application/json")
            .addHeader("Authorization", "Bearer " + token)
            .build();
    }
}
