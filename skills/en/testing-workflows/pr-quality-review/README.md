# PR Quality Review Workflow

Invoke `pr-quality-review` with a PR diff, base/head SHA, acceptance criteria, and available test/CI records. It composes existing code review, test impact, test effectiveness, and quality-gate capabilities.

## Example

> Review PR #42 for refund idempotency, check whether assertions verify behavior, and report sourced P0/P1/P2 findings and blockers. Do not write back to the PR.

## Best practices

Provide a complete diff and stable SHA; attach command, exit code, environment, time, and source to run evidence; provide team severity definitions.

## FAQ

- Without run results, a limited static review is possible; mark execution `NOT_RUN` / `UNKNOWN`.
- Installation of specialist Skills is not assumed; provide the host capability inventory.
- External comments, merge, and approval are not performed without explicit authorization.
