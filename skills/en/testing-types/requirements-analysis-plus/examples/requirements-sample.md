# Flash-Sale Gift Campaign: Draft Requirements

## Background
- The campaign runs from 20:00 to 20:10 on 2026-03-20.
- Total gift inventory is 500 units.

## Business rules
- A user must be a PLUS member and have spent at least 199 CNY in the past 30 days.
- Each user may claim one gift only.
- The gift-center status must update within three seconds of a successful payment.
- When inventory reaches zero, the UI must show that the gifts are sold out.

## Non-functional requirements
- The service must sustain 50,000 QPS at peak, with API response time below 300 ms.
- The system must prevent replay attacks and validate request signatures.
- Inventory replenishment must be supported when necessary.

## Open questions
- Do enterprise and personal accounts share the same claim limit? (TBD)
- Is the polling interval fixed under poor-network conditions? (TBD)
