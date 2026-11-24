# Agent Trajectory Evidence

Use a trajectory as source-attributed context about how a change was produced. It does not replace review of the code or execution artifacts.

Retain, item by item:

- Run, step, tool-call, and evidence IDs, including supplied time/order information.
- Task goal, input references, files read/changed, tool arguments, and tool results.
- Whether a result is an Agent self-report, simulated output, real local execution, or a CI-platform artifact; mark `UNKNOWN` when unclear.
- How each event maps to the final patch, test files, lockfiles, and workflow configuration.
- Missing context, calls absent from the trace, and whether independent Human review exists.

A trace claim of `PASS` does not prove a test or CI job ran. A located command/platform result with commit SHA, time, environment, and exit state is needed for corresponding run evidence. Missing tool events do not prove the Agent made no calls.
