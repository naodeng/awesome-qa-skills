# Unit-Test Rules

- Each test should focus on one observable behavior; name its condition and expected result.
- Prefer lightweight real dependencies; mock only uncontrollable, expensive, or side-effecting boundaries.
- A mock can verify collaboration at a boundary, but must not replace a domain-result assertion.
- Cover normal, failure, and boundary inputs, including nulls, error mapping, state changes, and idempotency where relevant.
- Tests must be independent of order, wall clock, shared globals, and data created by other tests.
- If a test locks private functions, call order, or internal structures, require an externally relevant risk; otherwise prefer behavior assertions.
