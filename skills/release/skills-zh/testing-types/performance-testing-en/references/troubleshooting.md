## Troubleshooting

### Common Issues

#### 1. Connection Timeout

**Problem:** `request timeout` or `connection timeout`

**Solution:**
```javascript
// K6 example
export const options = {
  timeout: '60s',  // Increase timeout
};

// Or check network connection and server status
```

#### 2. Out of Memory

**Problem:** K6 or JMeter consuming too much memory

**Solution:**
- Reduce virtual users
- Use SharedArray to share data (K6)
- Distributed testing
- Increase test machine memory

#### 3. Certificate Verification Error

**Problem:** SSL certificate verification failed

**Solution:**
```javascript
// K6 example
export const options = {
  insecureSkipTLSVerify: true,  // Skip certificate verification (test environment only)
};
```

#### 4. Rate Limiting

**Problem:** Rate limited by server (429 Too Many Requests)

**Solution:**
- Increase think time (sleep)
- Use random delays
- Gradually increase load
- Coordinate test time with server team

#### 5. Unstable Results

**Problem:** Test results vary greatly each time

**Solution:**
- Ensure stable test environment
- Run multiple times and average
- Check network conditions
- Isolate other interference factors

#### 6. Cannot Reach Target Load

**Problem:** Actual RPS much lower than expected

**Solution:**
- Check client resources (CPU, network)
- Use distributed testing
- Optimize test scripts
- Reduce unnecessary wait times

#### 7. Abnormal Report Data

**Problem:** Performance metrics abnormally high or low

**Solution:**
- Check test script logic
- Verify threshold settings
- Review detailed logs
- Compare with historical data

