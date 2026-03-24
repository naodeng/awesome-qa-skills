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

