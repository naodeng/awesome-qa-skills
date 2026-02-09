---
name: functional-testing-en
version: 2.0.0
last-updated: 2026-02-09
description: Design functional test plans and cases (business, UI, data, integration). Default output Markdown; can request Excel, CSV, or JSON. Use for functional testing.
---

# Functional Testing (English)

**中文版：** See skill `functional-testing`.

Prompt: this directory’s `prompts/functional-testing_EN.md`.

## When to Use

- User mentions **functional testing**, **functional test cases**, **functional test plan**
- Need to design functional test strategy, cases, or plan from requirements/specs
- **Trigger:** e.g. “Design functional test cases for the following requirements” or “Create a functional test plan”

## Output Format Options

This skill **defaults to Markdown** (Standard-version template). To get another format, add one of the following at the **end** of your request:

| Format | Description | How to request (example) |
|--------|-------------|--------------------------|
| **Markdown** | Default; good for reading and version control | No extra instruction |
| **Excel** | Tab-separated, paste into Excel | “Please output as tab-separated table for pasting into Excel” |
| **CSV** | Comma-separated, header row first | “Please output as CSV” |
| **JSON** | For tooling/parsing | “Please output as JSON” |

Details and examples: **[output-formats.md](output-formats.md)** in this directory.

## How to Use the Prompt

1. Open `prompts/functional-testing_EN.md`, copy everything below the dashed line into the AI chat.
2. Append your functional requirements or system spec.
3. If you want Excel/CSV/JSON, append the relevant line from output-formats.md.

## Reference Files

- **[prompts/functional-testing_EN.md](prompts/functional-testing_EN.md)** — Functional testing Standard-version prompt
- **[output-formats.md](output-formats.md)** — Markdown / Excel / CSV / JSON request instructions

## Code Examples

This skill provides the following real-world code examples:

1. **[Playwright Login Testing](examples/playwright-login/)** - Complete login functionality test suite
   - 14 test cases
   - Coverage: functionality, accessibility, security
   - Includes best practices and troubleshooting

2. **Cypress Form Testing** (Coming soon)
3. **Selenium Navigation Testing** (Coming soon)

See [examples/](examples/) directory for more examples.

## Common Pitfalls

- ❌ **Skip requirements analysis and write cases directly** → ✅ Use requirements-analysis skill first to analyze requirements and identify test points
- ❌ **Only test normal scenarios** → ✅ Cover exception scenarios, boundary values, and error handling
- ❌ **Unclear case descriptions** → ✅ Use clear steps and expected results to ensure reproducibility
- ❌ **Ignore accessibility testing** → ✅ Include keyboard navigation, screen reader validation
- ❌ **Hardcode test data** → ✅ Use test data management strategy for maintainability

## Best Practices

1. **Test Design**
   - Use equivalence partitioning and boundary value analysis
   - Follow AAA pattern (Arrange-Act-Assert)
   - Keep tests independent, avoid dependencies

2. **Element Location**
   - Prioritize data-testid attributes
   - Avoid volatile CSS class names
   - Use semantic locators

3. **Assertion Strategy**
   - Use multiple specific assertions rather than single vague assertion
   - Verify key business logic
   - Include user experience validation

4. **Maintainability**
   - Use Page Object Model design pattern
   - Extract reusable test utility functions
   - Keep test code clean

5. **Execution Efficiency**
   - Run independent tests in parallel
   - Use appropriate wait strategies
   - Avoid unnecessary delays

## Troubleshooting

### Issue 1: Code Examples Won't Run

**Symptoms:** Error `Cannot find module` or `Command not found` when running examples

**Solution:**
1. Ensure dependencies are installed:
   ```bash
   cd examples/playwright-login
   npm install
   ```
2. Check Node.js version (requires >= 16):
   ```bash
   node --version
   ```
3. If using Playwright, install browsers:
   ```bash
   npx playwright install
   ```

### Issue 2: Incomplete Test Case Design

**Symptoms:** Low test coverage, missing important scenarios

**Solution:**
1. Use requirements-analysis skill first to analyze requirements
2. Refer to "Test Coverage Dimensions" section in the prompt
3. Use test design methods:
   - Equivalence partitioning
   - Boundary value analysis
   - Decision table testing
   - State transition testing
4. Checklist:
   - [ ] Normal scenarios
   - [ ] Exception scenarios
   - [ ] Boundary values
   - [ ] Error handling
   - [ ] Accessibility
   - [ ] Security

### Issue 3: Output Format Not as Expected

**Symptoms:** Generated test cases have wrong format or missing fields

**Solution:**
1. Clearly specify format requirements at the end of request:
   ```
   Please output as tab-separated table for pasting into Excel
   ```
2. Refer to examples in [output-formats.md](output-formats.md)
3. Use format conversion tool (to be implemented):
   ```bash
   ./tools/format-converter.sh input.md --to=excel
   ```

### Issue 4: Unstable Test Execution

**Symptoms:** Tests sometimes pass, sometimes fail

**Solution:**
1. Use explicit waits instead of fixed delays:
   ```typescript
   // ✅ Recommended
   await expect(element).toBeVisible();
   
   // ❌ Not recommended
   await page.waitForTimeout(3000);
   ```
2. Wait for network requests to complete:
   ```typescript
   await page.waitForResponse(resp => resp.url().includes('/api'));
   ```
3. Use retry mechanism (Playwright config):
   ```typescript
   retries: 2
   ```

### Issue 5: Cannot Locate Element

**Symptoms:** Test error `Element not found` or `Timeout`

**Solution:**
1. Check if element is in iframe:
   ```typescript
   const frame = page.frameLocator('iframe');
   await frame.locator('[data-testid="element"]').click();
   ```
2. Wait for element to appear:
   ```typescript
   await page.waitForSelector('[data-testid="element"]');
   ```
3. Use more reliable locators:
   ```typescript
   // ✅ Recommended: data-testid
   page.locator('[data-testid="login-button"]')
   
   // ✅ Recommended: role
   page.getByRole('button', { name: 'Login' })
   
   // ❌ Not recommended: CSS class
   page.locator('.btn-primary')
   ```

### Issue 6: Slow Test Execution

**Symptoms:** Test suite takes too long to execute

**Solution:**
1. Enable parallel execution:
   ```typescript
   // playwright.config.ts
   fullyParallel: true,
   workers: 4,
   ```
2. Optimize wait strategies, avoid unnecessary waits
3. Use test data caching
4. Consider using API to set up test preconditions

### Issue 7: CI/CD Environment Test Failures

**Symptoms:** Tests pass locally but fail in CI

**Solution:**
1. Check environment differences (browser version, screen resolution)
2. Increase timeout for CI environment
3. Enable failure retry:
   ```typescript
   retries: process.env.CI ? 2 : 0
   ```
4. Review CI logs, screenshots, and videos
5. Use Docker containers to ensure environment consistency

### Get More Help

If the issue persists:
1. Check [FAQ.md](../../../FAQ.md)
2. Check example README.md files
3. Search [GitHub Issues](https://github.com/your-repo/awesome-qa-skills/issues)
4. Submit a new Issue with detailed information

**Related:** api-testing-en, test-case-writing-en, test-strategy-en, automation-testing-en.
