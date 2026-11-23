# False Confidence Catalog

Check for these patterns when reviewing AI-assisted test work. Preserve the real state and gather evidence; do not change acceptance rules to hide the problem.

1. **Invalid assertion, all green:** An assertion does not validate the target behavior or checks only a status code/non-empty value.
2. **Failure removal:** A failing check is deleted, skipped, weakened, or masked to pass a gate.
3. **Invented interface:** Output cites an API, field, configuration, or business rule that does not exist.
4. **Generation time only:** Productivity is claimed from generation minutes while review, rework, acceptance, and token cost are omitted.
5. **Adopted without review:** A draft is made a formal asset without a `reviewer` and `ACCEPTED` record.
6. **Coverage in place of quality:** Coverage is treated as proof of defect detection, a correct oracle, or business acceptance.
7. **Hidden failure path:** Failed cases, retries, environment limits, or counterexamples are omitted while only a final green result is reported.
8. **Summary in place of raw evidence:** An AI summary, explanation, or screenshot description is treated as logs, a run ID, or an execution report.

Record source and impact for each finding. Missing execution evidence is `NOT_RUN` or `BLOCKED`; an unconfirmed conclusion is `UNKNOWN`; an unreviewed draft is `DRAFT`. Name an owner and the smallest evidence-gathering action.
