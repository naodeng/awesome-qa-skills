# Functional-Test Rules

- Review from user goals, business rules, and state transitions—not only UI actions.
- For every critical journey, verify the successful outcome plus a failure or boundary path that changes a business decision.
- Check roles, permissions, prerequisite state, data lifecycle, duplicate submission, and recovery.
- Expected results must include a user-visible or persisted business outcome, not merely element existence.
- For external services, state whether the boundary is stubbed, sandboxed, or real and what integration risk remains.
- Raise severity for missing cancellation, rollback, timeout, retry, or inconsistent-state coverage when business impact warrants it.
