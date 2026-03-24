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
1. Check [FAQ.md](local/FAQ.md)
2. Check example README.md files
3. Search [GitHub Issues](https://github.com/naodeng/awesome-qa-skills/issues)
4. Submit a new Issue with detailed information

**Related:** api-testing-en, test-case-writing-en, test-strategy-en, automation-testing-en.
