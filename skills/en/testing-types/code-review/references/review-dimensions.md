# Extra Review Dimensions (load on demand)

Read this only when you need finer scan dimensions or severity calibration; do not dump the whole file into every review.

## 1. Logic and State

- Null/guard gaps, bounds errors, incomplete state machines
- Swallowed exceptions, silently ignored error codes
- Resource leaks (connections, handles, locks, temp files)

## 2. Concurrency and Distributed Consistency

- Races, lost updates, check-then-act
- Broken idempotency (retries causing double charge/ship/write)
- Misaligned distributed transaction boundaries; cache vs DB drift
- Bad lock granularity, deadlock risk

## 3. Financial Loss and Security

- Money/inventory precision (floats, rounding direction)
- AuthZ gaps, duplicate pay/refund, promo stacking bugs
- Injection (SQL/NoSQL/command/template), XSS
- Sensitive leakage (plaintext tokens/passwords in logs, hardcoded secrets, missing redaction)

## 4. API Contract and Compatibility

- Field add/remove/rename, type/enum changes, default-value semantics
- Breaking forward/backward compatibility, corrupting existing data
- Unexpected impact on callers, consumers, or batch jobs

## 5. Testability and Evolution

- Hard-coded time/randomness, hard-to-mock dependencies
- Missing assertion points or hard-to-build fixtures
- Long methods/classes, misplaced responsibility, magic values, high complexity, tight coupling
- Flag only high-value smells; avoid style nitpicking

## 6. Performance and Resources (high-value only)

- N+1 queries, IO/RPC inside loops, unbounded copies
- Clearly wrong pool/timeout/retry settings
- Leak or unbounded cache growth signals

## 7. Error Handling and Observability

- Whether failures are diagnosable or root cause is swallowed
- Logs with TraceID / key business ids (and redaction)
- Alertable metrics on core paths

## Severity Rubric

| Level | Merge decision | Typical impact |
| --- | --- | --- |
| P0 | Must fix before merge | Financial loss, severe security, main-path failure |
| P1 | Strongly fix this iteration | Likely edge failure, clear perf, core unobservability |
| P2 | Tech debt OK | Non-core maintainability, minor opts |
