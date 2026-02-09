---
name: api-testing-en
version: 2.0.0
last-updated: 2024-02-06
description: Design API test plans and cases for REST/GraphQL/gRPC interfaces. Default output Markdown; can request Excel, CSV, or JSON. Use for API testing.
category: testing-types
level: intermediate
tags: [api, rest, graphql, grpc, postman, newman, integration]
dependencies: []
recommended-with: [automation-testing-en, performance-testing-en, security-testing-en]
context-aware: true
context-patterns:
  project-types: [api, web, mobile]
  frameworks: [express, nestjs, django, flask, fastapi, spring-boot, gin]
  test-frameworks: [postman, rest-assured, supertest, pytest, junit]
output-formats: [markdown, excel, csv, json, jira, testrail]
examples-count: 3
has-tutorial: false
has-troubleshooting: true
---

# API Testing (English)

**中文版：** See skill `api-testing`.

Prompt: this directory's `prompts/api-testing_EN.md`.

## When to Use

- User mentions **API testing**, **api-testing**
- Need to execute this testing type or produce deliverables per Standard-version
- **Trigger examples:** "Generate/design/write API test cases for the following"

## Output Format Options

**Markdown** by default. For **Excel / CSV / JSON**, add at the **end** of your request; see **[output-formats.md](output-formats.md)**.

## How to Use

1. Open `prompts/api-testing_EN.md`, copy everything below the dashed line into the AI chat.
2. Append your specific input.
3. For Excel/CSV/JSON, append the request line from output-formats.md.

## Code Examples

### 1. Postman + Newman REST API Testing

Complete user management API test example with 10 test cases.

**Location:** `examples/postman-rest-api/`

**Includes:**
- Postman collection file (10 test cases)
- Environment variable configuration
- Newman automation run script
- Detailed README documentation

**Quick Start:**
```bash
cd examples/postman-rest-api
npm install -g newman
./newman-run.sh
```

**Test Coverage:**
- User CRUD operations (Create, Read, Update, Delete)
- Authentication and authorization testing
- Error handling and boundary conditions
- Response time validation
- Data format validation

See: [examples/postman-rest-api/README.md](examples/postman-rest-api/README.md)

### 2. REST Assured (Java)

Coming soon - Java-based REST API testing with REST Assured framework.

**Location:** `examples/rest-assured-java/`

### 3. SuperTest (Node.js)

Coming soon - Node.js API testing with SuperTest framework.

**Location:** `examples/supertest-nodejs/`

## Best Practices

### API Test Design Principles

1. **Test Pyramid**
   - Unit tests: Test individual API endpoints
   - Integration tests: Test interactions between multiple endpoints
   - End-to-end tests: Test complete business workflows

2. **Test Data Management**
   - Use environment variables for different environment configurations
   - Use dynamic variables to avoid hardcoding
   - Clean up data after tests

3. **Assertion Strategy**
   - Verify status codes
   - Verify response structure (Schema Validation)
   - Verify response data
   - Verify response time

4. **Error Handling**
   - Test various error scenarios (4xx, 5xx)
   - Verify error message format
   - Test boundary conditions

### Tool Selection Guide

| Tool | Use Case | Advantages |
|------|----------|------------|
| Postman/Newman | REST API testing | Easy to use, visual, CI/CD integration |
| REST Assured | Java projects | Strong typing, BDD style |
| Pytest + Requests | Python projects | Flexible, rich ecosystem |
| SuperTest | Node.js projects | Good integration with Express |
| GraphQL Playground | GraphQL API | Designed specifically for GraphQL |

## Troubleshooting

### Common Issues

#### 1. Newman Run Failure

**Problem:** `newman: command not found`

**Solution:**
```bash
# Install Newman globally
npm install -g newman

# Or use npx (no global installation needed)
npx newman run collection.json
```

#### 2. Environment Variables Not Working

**Problem:** Variables in tests show as `{{variable}}`

**Solution:**
- Ensure using `-e` parameter to specify environment file
- Check if variable names in environment file are correct
- Verify variables are correctly set in Postman

```bash
newman run collection.json -e environment.json
```

#### 3. Certificate Verification Error

**Problem:** `SSL certificate problem`

**Solution:**
```bash
# Temporarily disable SSL verification for dev environment (not recommended for production)
newman run collection.json --insecure

# Or specify CA certificate
newman run collection.json --ssl-client-cert-list cert-list.json
```

#### 4. Request Timeout

**Problem:** `Error: ETIMEDOUT` or `Error: ESOCKETTIMEDOUT`

**Solution:**
```bash
# Increase timeout (milliseconds)
newman run collection.json --timeout-request 30000

# Add request delay
newman run collection.json --delay-request 500
```

#### 5. Response Data Format Mismatch

**Problem:** JSON Schema validation fails

**Solution:**
- Use Postman's Schema generation feature
- Check API documentation to confirm data structure
- Use `pm.response.json()` to print actual response

```javascript
// Add debug info in Tests
console.log(pm.response.json());
```

#### 6. Dynamic Data Dependency Issues

**Problem:** Subsequent requests depend on data from previous request

**Solution:**
```javascript
// Save data in first request's Tests
pm.environment.set("userId", pm.response.json().id);

// Use in subsequent requests
// URL: {{baseUrl}}/users/{{userId}}
```

#### 7. Batch Test Run Failures

**Problem:** Individual tests pass, batch run fails

**Solution:**
- Check data dependencies between tests
- Ensure each test can run independently
- Add appropriate delays: `--delay-request 200`
- Use `--bail` to stop on first failure

## Reference Files

- **prompts/api-testing_EN.md** — API testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/postman-rest-api/** — Complete Postman + Newman example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** automation-testing-en, performance-testing-en, security-testing-en, functional-testing-en.
