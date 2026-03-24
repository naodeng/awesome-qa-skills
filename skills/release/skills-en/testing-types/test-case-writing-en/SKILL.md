---
name: test-case-writing-en
description: Use this skill when you need to create high-quality test cases with normal, exception, and boundary scenarios; triggers include test case writing and test design.
---

# Test Case Writing (English)

**中文版：** See skill `test-case-writing`.

Prompt: this directory's `prompts/test-case-writing_EN.md`.

## When to Use

- User mentions **test case writing**, **test case design**, **case design**
- Need to design test cases based on requirements
- **Trigger examples:** "Write test cases for the following requirements" or "Design test cases for login functionality"

## Output Format Options

This skill **defaults to Markdown** (Standard-version template). To get another format, add one of the following at the **end** of your request:

| Format | Description | How to request (example) |
|--------|-------------|--------------------------|
| **Markdown** | Default; good for reading and version control | No extra instruction |
| **Excel** | Tab-separated, paste into Excel | "Please output as tab-separated table for pasting into Excel" |
| **CSV** | Comma-separated, header row first | "Please output as CSV" |
| **JSON** | For tooling/parsing | "Please output as JSON" |
| **TestRail** | TestRail import format | "Please output in TestRail format" |

Details and examples: **[output-formats.md](output-formats.md)** in this directory.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Reference Files

- **[prompts/test-case-writing_EN.md](prompts/test-case-writing_EN.md)** — Test case writing Standard-version prompt
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON request instructions

## Code Examples

This skill provides the following real-world code examples:

1. **Test Case Design Patterns (Planned)** - Complete test case design examples
   - Equivalence partitioning examples (10+)
   - Boundary value analysis examples (8+)
   - Decision table testing examples (5+)
   - State transition testing examples (3+)
   - Real project test case sets (50+)

2. **Test Case Generation Tool** (Coming soon)
3. **Test Case Quality Checker** (Coming soon)

Additional examples are planned in a future update.

## Common Pitfalls

- ❌ **Only testing happy paths** → ✅ Cover normal, exception, and boundary scenarios
- ❌ **Unclear test case descriptions** → ✅ Use explicit steps and expected results
- ❌ **Missing test data** → ✅ Provide specific test data
- ❌ **Inappropriate granularity** → ✅ Maintain appropriate granularity, not too coarse or too fine
- ❌ **Ignoring preconditions** → ✅ Clearly state preconditions and environment requirements
- ❌ **No priority** → ✅ Mark test case priority (P0/P1/P2/P3)
- ❌ **Dependencies between cases** → ✅ Keep test cases independent

## Best Practices

### 1. Test Case Structure

**Standard test case format**:

```markdown
## TC-001: Test Case Title

**Priority**: P0 / P1 / P2 / P3
**Type**: Functional / UI / Performance / Security / Compatibility
**Preconditions**:
- Condition 1
- Condition 2

**Test Steps**:
1. Step 1
2. Step 2
3. Step 3

**Test Data**:
- Data item 1: Value
- Data item 2: Value

**Expected Results**:
- Result 1
- Result 2

**Actual Results**: [Fill during execution]
**Status**: Pass / Fail / Blocked / Skip
**Notes**: [Optional]
```

### 2. Test Design Methods

#### Equivalence Partitioning

Divide input domain into equivalence classes, select representative data from each class:

**Example: Age input (valid range 18-65)**

| Equivalence Class | Type | Test Value | Expected Result |
|-------------------|------|------------|-----------------|
| < 18 | Invalid | 10, 17 | Reject |
| 18-65 | Valid | 18, 30, 65 | Accept |
| > 65 | Invalid | 66, 100 | Reject |

#### Boundary Value Analysis

Test boundary values and values near boundaries:

**Example: Age input (valid range 18-65)**

| Test Value | Type | Expected Result |
|------------|------|-----------------|
| 17 | Lower boundary-1 | Reject |
| 18 | Lower boundary | Accept |
| 19 | Lower boundary+1 | Accept |
| 64 | Upper boundary-1 | Accept |
| 65 | Upper boundary | Accept |
| 66 | Upper boundary+1 | Reject |

#### Decision Table

Handle scenarios with multiple condition combinations:

**Example: Login validation**

| Condition | Rule 1 | Rule 2 | Rule 3 | Rule 4 |
|-----------|--------|--------|--------|--------|
| Username correct | ✓ | ✓ | ✗ | ✗ |
| Password correct | ✓ | ✗ | ✓ | ✗ |
| **Result** | **Login success** | **Password error** | **Username error** | **Both error** |

#### State Transition

Test object transitions between different states:

```
[Not logged in] --Login--> [Logged in] --Logout--> [Not logged in]
                 |                      |
                 +----Login failed------+
```

### 3. Test Case Priority

**P0 (Critical)**:
- Core business processes
- Blocking issues
- Must execute before each release

**P1 (High)**:
- Important features
- Common scenarios
- Should execute before each release

**P2 (Medium)**:
- General features
- Non-core scenarios
- Can be selectively executed

**P3 (Low)**:
- Edge cases
- Rarely used features
- Execute when time permits

### 4. Test Case Writing Principles

**SMART Principles**:
- **Specific**: Steps and results are clear
- **Measurable**: Results are verifiable
- **Achievable**: Can be actually executed
- **Relevant**: Related to requirements
- **Time-bound**: Execution time is reasonable

**3C Principles**:
- **Clear**: Anyone can understand
- **Concise**: Not redundant
- **Complete**: Contains all necessary information

### 5. Coverage Goals

- **Requirements coverage**: 100% (all requirements have corresponding test cases)
- **Code coverage**: 80%+ (automated tests)
- **Scenario coverage**: Cover normal, exception, and boundary cases
- **Priority distribution**: P0(20%) + P1(30%) + P2(30%) + P3(20%)

## Troubleshooting

### Issue 1: Don't Know How to Start Writing Test Cases

**Symptoms:** Facing requirements document, don't know where to start

**Solution:**

Use 5W1H analysis method:

1. **What (What to test)**: Identify functional points
2. **Who (Who uses)**: Identify user roles
3. **When (When)**: Identify trigger conditions
4. **Where (Where)**: Identify usage scenarios
5. **Why (Why)**: Understand business goals
6. **How (How)**: Design test steps

**Example**:

```markdown
## Requirement: User login functionality

### 5W1H Analysis

**What**: 
- Username password validation
- Remember me feature
- Forgot password link

**Who**:
- Registered users
- Unregistered users
- Administrators

**When**:
- First visit
- After session expires
- After active logout

**Where**:
- Web
- Mobile
- Different browsers

**Why**:
- Protect user data
- Personalized experience
- Permission control

**How**:
- Enter username and password
- Click login button
- Validate and redirect

### Test Case Design

Based on above analysis, design following test cases:
1. Normal login (P0)
2. Username error (P1)
3. Password error (P1)
4. Remember me feature (P2)
5. Forgot password flow (P2)
...
```

### Issue 2: Incomplete Test Coverage

**Symptoms:** Many missed scenarios found after testing

**Solution:**

Use test coverage checklist:

```markdown
## Test Coverage Checklist

### Functional Dimension
- [ ] Normal flow
- [ ] Exception flow
- [ ] Boundary conditions
- [ ] Error handling

### Data Dimension
- [ ] Valid data
- [ ] Invalid data
- [ ] Empty/null values
- [ ] Special characters
- [ ] Oversized data
- [ ] Wrong data types

### User Dimension
- [ ] Different roles
- [ ] Different permissions
- [ ] Not logged in users
- [ ] Logged in users

### Environment Dimension
- [ ] Different browsers
- [ ] Different operating systems
- [ ] Different screen sizes
- [ ] Different network conditions

### State Dimension
- [ ] Initial state
- [ ] Intermediate state
- [ ] Final state
- [ ] Exception state

### Time Dimension
- [ ] First use
- [ ] Repeated use
- [ ] Timeout scenarios
- [ ] Concurrent scenarios
```

### Issue 3: Too Many Test Cases, Can't Execute All

**Symptoms:** Huge number of test cases, not enough testing time

**Solution:**

1. **Priority sorting**:
   - Execute P0 and P1 test cases first
   - P2 and P3 selectively based on time

2. **Risk assessment**:
   - Increase test cases in high-risk areas
   - Reduce test cases in low-risk areas

3. **Automation**:
   - Automate repetitive test cases
   - Manual testing focuses on exploratory testing

4. **Test case merging**:
   - Merge similar test cases
   - One test case validates multiple checkpoints

**Example**:

```markdown
## Before optimization (5 test cases)

TC-001: Login success
TC-002: Display username after login
TC-003: Display avatar after login
TC-004: Display menu after login
TC-005: Redirect to homepage after login

## After optimization (1 test case)

TC-001: Login success and verify user information

**Test Steps**:
1. Enter correct username and password
2. Click login button

**Expected Results**:
- ✓ Login successful
- ✓ Display username
- ✓ Display user avatar
- ✓ Display navigation menu
- ✓ Redirect to homepage
```

### Issue 4: Unclear Test Case Description

**Symptoms:** Others have difficulty understanding when executing test cases

**Solution:**

Use **Given-When-Then** format:

```markdown
## TC-001: Add product to shopping cart

**Given (Preconditions)**:
- User is logged in
- Product stock is sufficient (> 10 items)
- Shopping cart is empty

**When (Test Steps)**:
1. Visit product detail page
2. Select quantity: 2
3. Click "Add to Cart" button

**Then (Expected Results)**:
- Display "Added successfully" message
- Shopping cart icon shows number 2
- Product appears in shopping cart list
- Product quantity shows 2
- Total price = Unit price × 2
```

### Issue 5: Difficult Test Data Preparation

**Symptoms:** Spend a lot of time preparing data for each test case execution

**Solution:**

1. **Create test data sets**:

```markdown
## Test Data Sets

### User Data
| Username | Password | Role | Status | Purpose |
|----------|----------|------|--------|---------|
| admin@test.com | Admin123! | Admin | Normal | Admin function testing |
| user1@test.com | User123! | User | Normal | Normal flow testing |
| user2@test.com | User123! | User | Locked | Exception state testing |

### Product Data
| Product ID | Name | Price | Stock | Purpose |
|------------|------|-------|-------|---------|
| P001 | Product A | 100 | 999 | Normal purchase testing |
| P002 | Product B | 200 | 1 | Insufficient stock testing |
| P003 | Product C | 0 | 100 | Free product testing |
```

2. **Use data generation tools**:
   - Faker.js (JavaScript)
   - Faker (Python)
   - Custom data generation scripts

3. **Database snapshots**:
   - Save test database snapshots
   - Restore snapshots before each test

### Issue 6: High Test Case Maintenance Cost

**Symptoms:** Need to update many test cases after requirement changes

**Solution:**

1. **Modular design**:

```markdown
## Common Steps Library

### Login Steps
**Step ID**: COMMON-LOGIN
**Steps**:
1. Visit login page
2. Enter username: {username}
3. Enter password: {password}
4. Click login button

### Add Product to Cart
**Step ID**: COMMON-ADD-TO-CART
**Steps**:
1. Visit product detail page: {product_id}
2. Select quantity: {quantity}
3. Click "Add to Cart"

## Test Cases

### TC-001: Purchase product flow
**Steps**:
1. Execute COMMON-LOGIN (username=user1, password=User123!)
2. Execute COMMON-ADD-TO-CART (product_id=P001, quantity=2)
3. Click shopping cart icon
4. Click "Checkout" button
...
```

2. **Parameterized test cases**:

```markdown
## TC-001: Login validation (Parameterized)

| Case ID | Username | Password | Expected Result |
|---------|----------|----------|-----------------|
| TC-001-1 | valid@test.com | Valid123! | Login success |
| TC-001-2 | invalid@test.com | Valid123! | Username error |
| TC-001-3 | valid@test.com | Invalid | Password error |
| TC-001-4 | | Valid123! | Username empty |
| TC-001-5 | valid@test.com | | Password empty |
```

### Issue 7: Don't Know How to Verify Complex Expected Results

**Symptoms:** Expected results involve multiple systems or complex calculations

**Solution:**

Break down verification points:

```markdown
## TC-001: Order submission

**Expected Results**:

### 1. Frontend Display
- [ ] Display "Order submitted successfully" message
- [ ] Redirect to order detail page
- [ ] Order number format correct (ORD-YYYYMMDD-XXXXX)
- [ ] Order status shows "Pending payment"

### 2. Database Verification
- [ ] New record added to orders table
- [ ] Corresponding product records added to order_items table
- [ ] Product stock decreased by corresponding quantity
- [ ] User points increased

### 3. Third-party Systems
- [ ] Send order confirmation email
- [ ] Push order notification to mobile
- [ ] Sync order to ERP system

### 4. Log Verification
- [ ] Record order creation log
- [ ] Record stock change log
- [ ] Record points change log
```

### Get More Help

If the issue persists:
1. Check [FAQ.md](references/local/FAQ.md)
2. Review example README.md files
3. Refer to test case templates
4. Consult team's test lead

**Related skills:** requirements-analysis-en, functional-testing-en, test-case-reviewer-en, test-strategy-en.

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
