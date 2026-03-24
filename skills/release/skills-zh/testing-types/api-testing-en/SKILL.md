---
name: api-testing-en
description: Use this skill when you need to design API test plans or cases for REST, GraphQL, or gRPC interfaces; triggers include API testing and API test cases.
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

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

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

See: [examples/postman-rest-api/README.md](references/local/testing-types-api-testing-examples-postman-rest-api-README.md)

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

## Common Pitfalls

- ❌ Testing only happy paths → ✅ Cover validation, error handling, auth failures, and edge cases
- ❌ Weak contract checks → ✅ Assert status, schema, business fields, and backward compatibility
- ❌ Not isolating test data → ✅ Use deterministic seed data and clear teardown rules
- ❌ Ignoring environment parity → ✅ Validate base URL, auth config, and dependency versions per environment

## Troubleshooting

Detailed troubleshooting steps were moved to [references/troubleshooting.md](references/troubleshooting.md).
Load it on demand to keep the main skill concise.
## Reference Files

- **prompts/api-testing_EN.md** — API testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/postman-rest-api/** — Complete Postman + Newman example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** automation-testing-en, performance-testing-en, security-testing-en, functional-testing-en.

## Target Audience

- QA engineers and developers executing this testing domain in real projects
- Team leads who need structured, reproducible testing outputs
- AI users who need fast, format-ready deliverables for execution and reporting

## Not Recommended For

- Pure production incident response without test scope/context
- Decisions requiring legal/compliance sign-off without expert review
- Requests lacking minimum inputs (scope, environment, expected behavior)

## Critical Success Factors

- Provide clear scope, environment, and acceptance criteria before generation
- Validate generated outputs against real system constraints before execution
- Keep artifacts traceable (requirements -> test points -> defects -> decisions)

## Output Templates and Parsing Scripts

- Template directory: `output-templates/`
  - `template-word.md` (Word-friendly structure)
  - `template-excel.tsv` (Excel paste-ready)
  - `template-xmind.md` (XMind-friendly outline)
  - `template-json.json`
  - `template-csv.csv`
  - `template-markdown.md`
- Parser scripts directory: `scripts/`
  - Parse (generic): `parse_output_formats.py`
  - Parse (per-format): `parse_word.py`, `parse_excel.py`, `parse_xmind.py`, `parse_json.py`, `parse_csv.py`, `parse_markdown.py`
  - Convert (generic): `convert_output_formats.py`
  - Convert (per-format): `convert_to_word.py`, `convert_to_excel.py`, `convert_to_xmind.py`, `convert_to_json.py`, `convert_to_csv.py`, `convert_to_markdown.py`
  - Batch convert: `batch_convert_templates.py` (outputs into `artifacts/`)

Examples:
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/parse_markdown.py output-templates/template-markdown.md
python3 scripts/convert_to_json.py output-templates/template-markdown.md
python3 scripts/convert_output_formats.py output-templates/template-json.json --to csv
python3 scripts/batch_convert_templates.py --skip-same
```
