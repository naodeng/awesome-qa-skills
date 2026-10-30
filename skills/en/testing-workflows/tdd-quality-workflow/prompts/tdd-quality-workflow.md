# TDD Quality Workflow Contract

## Inputs and scope

Establish observable behavior and acceptance criteria, project test conventions, change scope, user authorization, and existing run records. Mark missing information `UNKNOWN`; identify provenance (direct observation, inspectable CI/report, or user recollection) and limitations. For a review-only request, do not execute tests or edit files. For an implementation request, use project tools within authorization and retain actual commands and outcomes. Commits, pushes, and external actions follow user authorization.

## Phase evidence

For one observable behavior at a time, record the phase, target test, command, run time, exit code, result, test count, source revision, and evidence location where available. The revision must identify the content actually tested; for a dirty worktree, record its state and a traceable diff or snapshot instead of treating HEAD alone as complete.

| Phase | Verified condition | Other outcomes |
| --- | --- | --- |
| Red | `VERIFIED_RED`: before implementation the target test actually ran and the intended behavior assertion failed for the expected reason; test, cause, and source revision are inspectable. | Unexpected dependency, compilation, collection, or environment failure is `INCONCLUSIVE`; known non-execution is `NOT_EXECUTED`. |
| Green | `VERIFIED_GREEN`: the target test actually ran and passed on the corresponding implementation revision; verify count, result, and exit code. | Zero tests, all skipped, failure, or insufficient evidence is `INCONCLUSIVE`; known non-execution is `NOT_EXECUTED`. |
| Refactor | `VERIFIED_REFACTOR`: relevant tests and required regression actually ran and passed after the refactor on the corresponding revision. | No refactor or no post-refactor run is `NOT_EXECUTED`; an unexpected run or insufficient evidence is `INCONCLUSIVE`. |

Missing logs do not prove non-execution: if execution is unknown or rests on unverified recollection, mark `INCONCLUSIVE` and identify the gap. An inspectable CI record can support conclusions within its scope; say when it was not run in this session. Assess phases independently, and claim a verified full cycle only if order and revision linkage are also supported. Do not fabricate an earlier Red from a later Green.

## Test effectiveness and optional gates

Inspect visible tests for business assertions, boundaries and negative paths, mocks that hide real behavior, side effects, and plausible missed defects. Static review is a risk signal; it does not establish runtime results, coverage, or defect detection. A passing test alone does not establish effectiveness. When useful, recommend project-appropriate mutation testing and distinguish a recommendation from an actual run.

Complexity, duplication, and mutation checks are optional and policy-dependent. For executed checks, record tool/version, input snapshot, command, result, and limitations. Evaluate a gate only against a project-defined threshold. Missing thresholds do not erase observed results, but they cannot justify a gate-pass claim. Use `INCONCLUSIVE` when an executed result or provenance cannot be checked and `NOT_EXECUTED` for known non-execution. For mutation tests report available killed, survived, and timed-out counts; do not count timeouts as killed.

External audit reports are supplementary evidence with attribution; static reports do not prove test execution. Do not assume that a particular Auditor version or evidence contract exists, and do not change its classifications or exit codes.

## Exceptions and output

For documentation and other appropriate non-TDD work, record the exception reason, existing authorization or decision source, alternative verification, and risks; mark missing approvers or material `UNKNOWN`. Never present the exception as a completed Red.

Deliver the behavior scope, three phase states with their own evidence, test effectiveness and optional checks, exceptions, risks, and next actions. State the scope of supported conclusions and leave unverified behavior, gates, and business acceptance unverified.
