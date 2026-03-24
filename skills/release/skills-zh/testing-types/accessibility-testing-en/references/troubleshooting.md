## Troubleshooting

### Issue 1: axe-core Reports Too Many False Positives

**Symptoms:** Automated test reports many issues, but they are actually false positives

**Solution:**
1. Configure rules to exclude known false positives:
   ```typescript
   await new AxeBuilder({ page })
     .disableRules(['color-contrast']) // Exclude specific rules
     .analyze();
   ```
2. Use tag filtering:
   ```typescript
   await new AxeBuilder({ page })
     .withTags(['wcag2a', 'wcag2aa']) // Only check WCAG 2.1 A/AA
     .analyze();
   ```
3. Manually verify suspicious issues
4. Update to latest version of axe-core

### Issue 2: Cannot Detect Accessibility Issues in Dynamic Content

**Symptoms:** Issues in modals, dropdowns, etc. are not detected

**Solution:**
1. Run tests after triggering dynamic content:
   ```typescript
   await page.click('[data-testid="open-modal"]');
   await page.waitForSelector('[role="dialog"]');
   const results = await new AxeBuilder({ page }).analyze();
   ```
2. Test specific regions:
   ```typescript
   await new AxeBuilder({ page })
     .include('[role="dialog"]')
     .analyze();
   ```
3. Test accessibility in different states

### Issue 3: Keyboard Navigation Tests Fail

**Symptoms:** Some elements cannot be accessed via keyboard

**Solution:**
1. Check tabindex attribute:
   ```html
   <!-- ✅ Recommended: Use tabindex="0" to make element focusable -->
   <div role="button" tabindex="0">Click me</div>
   
   <!-- ❌ Avoid: tabindex > 0 breaks natural Tab order -->
   <div tabindex="5">Bad practice</div>
   ```
2. Use semantic HTML:
   ```html
   <!-- ✅ Recommended: Native button is automatically focusable -->
   <button>Click me</button>
   
   <!-- ❌ Not recommended: Requires additional accessibility attributes -->
   <div onclick="...">Click me</div>
   ```
3. Add keyboard event handlers:
   ```typescript
   element.addEventListener('keydown', (e) => {
     if (e.key === 'Enter' || e.key === ' ') {
       // Handle activation
     }
   });
   ```

### Issue 4: Insufficient Color Contrast

**Symptoms:** axe-core reports color contrast issues

**Solution:**
1. Use contrast checking tools:
   - Chrome DevTools Lighthouse
   - WebAIM Contrast Checker
   - Colour Contrast Analyser
2. Ensure contrast ratio at least:
   - Normal text: 4.5:1
   - Large text (18pt+): 3:1
   - UI components: 3:1
3. Adjust color scheme:
   ```css
   /* ❌ Insufficient contrast */
   color: #999; /* Gray text */
   background: #fff; /* White background */
   
   /* ✅ Sufficient contrast */
   color: #595959; /* Dark gray text */
   background: #fff; /* White background */
   ```

### Issue 5: Screen Reader Cannot Read Content Correctly

**Symptoms:** Content is confusing or missing when using screen reader

**Solution:**
1. Use semantic HTML:
   ```html
   <!-- ✅ Recommended -->
   <nav>
     <ul>
       <li><a href="/">Home</a></li>
     </ul>
   </nav>
   
   <!-- ❌ Not recommended -->
   <div class="nav">
     <div class="item">Home</div>
   </div>
   ```
2. Use ARIA attributes correctly:
   ```html
   <!-- ✅ Recommended: Provide meaningful label -->
   <button aria-label="Close dialog">×</button>
   
   <!-- ❌ Not recommended: Screen reader only reads "times" -->
   <button>×</button>
   ```
3. Use aria-live to announce dynamic changes:
   ```html
   <div aria-live="polite" aria-atomic="true">
     <!-- Dynamic content -->
   </div>
   ```

### Issue 6: Form Accessibility Issues

**Symptoms:** Form controls lack labels or error messages are unclear

**Solution:**
1. Associate label with input:
   ```html
   <!-- ✅ Recommended: Explicit association -->
   <label for="email">Email</label>
   <input id="email" type="email" />
   
   <!-- ✅ Recommended: Implicit association -->
   <label>
     Email
     <input type="email" />
   </label>
   ```
2. Provide clear error messages:
   ```html
   <input
     id="email"
     type="email"
     aria-invalid="true"
     aria-describedby="email-error"
   />
   <span id="email-error" role="alert">
     Please enter a valid email address
   </span>
   ```
3. Use fieldset and legend for grouping:
   ```html
   <fieldset>
     <legend>Contact Information</legend>
     <!-- Form controls -->
   </fieldset>
   ```

### Issue 7: Tests Fail in CI Environment

**Symptoms:** Tests pass locally but fail in CI environment

**Solution:**
1. Ensure browsers are installed in CI environment:
   ```yaml
   - name: Install Playwright
     run: npx playwright install --with-deps
   ```
2. Check environment differences (fonts, rendering)
3. Save screenshots and reports on failure:
   ```typescript
   if (violations.length > 0) {
     await page.screenshot({ path: 'a11y-violations.png' });
     fs.writeFileSync('a11y-report.json', JSON.stringify(violations));
   }
   ```
4. Use Docker containers to ensure environment consistency

### Get More Help

If the issue persists:
1. Check [FAQ.md](local/FAQ.md)
2. Review example README.md files
3. Reference WCAG 2.1 official documentation
4. Use WebAIM resources
5. Submit a new Issue with detailed information

**Related skills:** functional-testing-en, manual-testing-en, automation-testing-en, test-case-writing-en.
