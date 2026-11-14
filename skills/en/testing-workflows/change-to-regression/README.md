# Change-to-Regression Workflow

Before coding, provide the proposal and existing cases for candidate guardrails. After coding, provide the diff, Commit SHA, business paths, and regression inventory for a sourced test selection.

## Example

> Compare this branch with `main`; select required/deferred checks for a payment retry change, explain risk and uncovered paths, and do not run tests.

> I plan to change discount stacking, but implementation has not started. Use these existing cases to identify behavior to preserve, candidate guardrails, and the smallest post-code verification. Label impacts as hypotheses and do not run tests.

## Best practices

Before coding, state the proposed behavior and constraints. After coding, provide exact base/head SHA, full diff, test runtimes, and environment limits. After execution, attach time, Commit, and run records.

## FAQ

- For an implemented change, without a diff or inspectable source, list required inputs and keep precise impact `UNKNOWN`; proposals may use `PRE_CHANGE` with hypothesis labels.
- Regression does not run by default; a plan is not a pass.
- A new Commit makes the old checkpoint `STALE`; reassess affected scope.
