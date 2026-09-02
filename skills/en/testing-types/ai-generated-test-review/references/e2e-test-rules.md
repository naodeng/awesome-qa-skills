# E2E-Test Rules

- Reserve E2E tests for critical journeys, cross-system integration, and high-risk regressions; do not repeat every unit detail in the UI layer.
- Use stable, user-facing selectors; avoid styling hierarchy and volatile text.
- Wait for observable state—completed request, enabled element, or business result—not arbitrary sleeps.
- Set up and clean up independent data per run; do not depend on shared accounts, order, or leftovers.
- Preserve screenshots, logs, or key network evidence on failure without exposing sensitive data.
- Retries may mitigate a known intermittent condition but must not hide a deterministic product defect.
