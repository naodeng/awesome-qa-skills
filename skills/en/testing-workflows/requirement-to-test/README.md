# Requirement-to-Test Workflow

Invoke `requirement-to-test` with requirements, user stories, or acceptance criteria to produce strategy, cases, and traceability.

## Example

> Analyze R-17: “A frozen account must not be refunded.” Check testability, list unresolved rules, then propose positive/negative cases, a risk strategy, and traceability to R-17.

## Best practices

Preserve requirement IDs; ask about missing thresholds; state each case source and method; explain uncovered areas.

## FAQ

- For vague acceptance criteria, ask only about scope, verdict, or priority.
- Tests are not run by default; execution remains `NOT_RUN`, with real run evidence cited separately.
- A changed requirement fingerprint/spec version makes old checkpoints `STALE` and requires reassessment.
