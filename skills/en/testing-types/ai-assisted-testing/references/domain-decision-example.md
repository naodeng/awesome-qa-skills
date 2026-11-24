# Domain Decision Example

This sanitized synthetic fixture checks provenance, decisions, and cost calculations. It is not a project run or business acceptance record.

## Input and Expected Decisions

The same 10 checkout cases have a 60-minute manual baseline. The AI-assisted workflow takes 10 minutes to generate, 25 to review, 35 to rework, and 10 to accept, for 80 minutes total. Input is sanitized. QA reviewer R1 checks D1 assertions and adopts them as V2; raw evidence for run R7 shows 10/10 passing. Review also finds one false-green assertion and the work is reworked. D2 has not been reviewed and cannot be called adopted. No token counts or billing evidence are available.

| ID | DECISION | Evidence |
| --- | --- | --- |
| AIA-01 | ACCEPTED | D1 is reviewed by R1; V2 and run R7 are traceable. 10/10 applies only to this fixture. |
| AIA-02 | DRAFT | Human review and an adopted version are missing. |
| AIA-03 | UNSUPPORTED | Ten minutes of generation does not represent total cost; token cost has no source. |

## Cost Recalculation

| METRIC | VALUE | Evidence |
| --- | --- | --- |
| human_baseline_minutes | 60 | Same scope and complexity manual baseline |
| generate_minutes | 10 | Time record |
| review_minutes | 25 | Time record |
| rework_minutes | 35 | Time record |
| acceptance_minutes | 10 | Time record |
| total_minutes | 80 | 10 + 25 + 35 + 10 |
| token_cost | UNSUPPORTED | No token counts or billing evidence |
| defects_found | 1 | One false-green assertion found in review |
| rework_count | 1 | One rework record |
| false_green_count | 1 | Original assertion did not validate the target behavior |

`total_minutes=80` exceeds the manual baseline of `60`; this example does not support an AI productivity claim. Do not generalize fixture IDs, versions, times, or pass counts to real projects.
