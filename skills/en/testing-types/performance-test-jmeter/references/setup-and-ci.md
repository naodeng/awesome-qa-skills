# Performance Test JMeter Setup and CI Notes

## Local Setup

- Confirm the tool version and runtime before proposing commands.
- Keep secrets, tokens, and environment-specific values outside committed test files.
- Store generated reports under a reports or build-artifacts folder ignored by version control.

## Suggested Run Command

```bash
jmeter -n -t "${TEST_PLAN:-test-plan.jmx}" -l "$REPORT_DIR/results.jtl" -e -o "$REPORT_DIR/html"
```

## CI Guidance

- Run smoke coverage on pull requests.
- Run broader regression on release branches or scheduled jobs.
- Preserve reports, logs, screenshots, traces, or result files as CI artifacts when the tool produces them.
- Fail the pipeline on clear assertion failures, not on missing optional artifacts.
