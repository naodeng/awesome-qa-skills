# Change-to-Regression Workflow

Invoke `change-to-regression` with the diff, Commit SHA, business paths, and regression inventory for a sourced test selection.

## Example

> Compare this branch with `main`; select required/deferred checks for a payment retry change, explain risk and uncovered paths, and do not run tests.

## Best practices

Provide exact base/head SHA, full diff, test runtimes, and environment limits. After execution, attach time, Commit, and run records.

## FAQ

- Without a diff, list required inputs and keep precise impact `UNKNOWN`.
- Regression does not run by default; a plan is not a pass.
- A new Commit makes the old checkpoint `STALE`; reassess affected scope.
