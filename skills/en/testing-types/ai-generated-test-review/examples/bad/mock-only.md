# Bad Example: Mock Only

Runnable example: [mock-only.test.mjs](mock-only.test.mjs). Run `node --test mock-only.test.mjs`; it passes while intentionally not verifying real order logic.

It does not prove saved content, business result, or an error path; an invalid order might still pass.
