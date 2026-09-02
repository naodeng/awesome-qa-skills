# API-Test Rules

- Assert status, key response fields, error contract, and necessary side effects; never HTTP 200 alone.
- Cover applicable authentication/authorization, validation, missing resources, conflicts, idempotency, pagination, and sorting.
- Keep request data minimal and traceable; never hard-code production identifiers or credentials.
- Check schema, field type, optionality, and compatibility, especially fields guessed by AI.
- For writes, verify creation, update, rollback, or cleanup and isolate data.
- For asynchronous APIs, wait for observable completion rather than hiding timing issues with fixed sleeps.
