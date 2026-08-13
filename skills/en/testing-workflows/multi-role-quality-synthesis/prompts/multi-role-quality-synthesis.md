# Multi-Role Quality Synthesis

This Prompt combines one or more role reports for the same quality stage into a traceable synthesis. It runs independently and does not require loading, invoking, or knowing any specific role Skill.

## Input contract

Input consists of one or more role reports. Each report should provide:

- `source_id`: unique report source identifier;
- `stage`: quality stage covered by the report;
- `source_role`: originating role;
- `facts`: facts confirmed by the source;
- `evidence`: evidence supporting facts or findings;
- `findings`: quality findings and source-provided severity, if any;
- `risks`, `gaps`, `questions`, `actions`, and `confidence`.

If `source_id` is missing, assign `report-1`, `report-2`, and so on in input order. Declare each as a synthesis-only locator under Information Gaps and Source Register; it is not a fabricated external source. Mark any other missing field as Not supplied and do not infer its content.

## Input validation

1. Require at least one identifiable role report. With no report, stop and output the blocker and required input; create no synthesized finding.
2. Validate every `stage`. A missing stage is a blocking input gap. When reports have different stages, do not combine them into one conclusion; list the stage conflict and ask the caller to split inputs by stage.
3. Record every input source, role, field completeness, and original confidence. A missing role does not erase the source; retain the source and label its role Unknown.
4. An absent optional role does not block synthesis of available reports. State only that the perspective was not supplied and how that limits coverage or confidence; do not infer what the role would have found.

## Classification rules

Classify before merging:

- **Quality facts**: supplied requirement, implementation, test-execution, defect, evidence, and quality states. Preserve their original statement, evidence, and sources.
- **Project constraints**: supplied schedules, capacity, dependencies, milestones, owners, action status, and stakeholder requests. Preserve sources, but never treat a request as a state change that already happened.
- **Analysis items**: findings, risks, gaps, questions, and actions. They must not masquerade as facts.

When one input sentence mixes a project request with a quality state, split it into two traceable items. No project constraint, deadline, resource pressure, PM/delivery opinion, or stakeholder request may rewrite, close, pass, approve, weaken, or override a quality fact.

## Deterministic merge rules

Apply these rules in order:

1. **Build the source register**: Bind every input item to its `source_id` and `source_role`; retain evidence, severity, and confidence.
2. **Normalize equivalent findings**: Merge findings only when they have the same target, the same condition or scope, and the same core problem or outcome. Wording, plurality, and synonym differences may be normalized. Different targets, conditions, states, impacts, or recommendations must remain separate.
3. **Union sources**: Write one neutral normalized statement that does not expand meaning. Its `sources` is the deduplicated union of every contributing `source_id`; `source_roles` is the deduplicated union of contributors; preserve evidence by source.
4. **Handle possible duplicates**: When equivalence is uncertain, keep findings separate and add an Open Question asking whether they are the same issue. Never guess merely to reduce the item count.
5. **Identify consensus**: Record Consensus only when at least two distinct sources explicitly support the same fact or conclusion, and list all supporting sources. A single-source finding is not consensus.
6. **Identify disagreements**: When facts contradict, conclusions oppose, severities differ, risk-acceptance positions differ, or actions are mutually exclusive, preserve every statement, evidence, and source under Disagreements. Never select one silently.
7. **Merge gaps, questions, and actions**: Merge only semantic equivalents and union their sources. Include owner, date, status, or dependency only when explicitly supplied.

## Severity rules

- Always preserve every source's original severity. Never generate a new severity through averaging, voting, or majority override.
- When all sources for an equivalent finding use the same severity, that value may be the synthesized severity, with its sources listed.
- When equivalent findings use different values on the same scale, preserve every source severity and record a disagreement. If a ranked output requires one severity, select the highest urgency supplied using `P0 > P1 > P2 > P3`, explicitly label the rule as conservative highest-input urgency, and show all original values. This is not averaging and does not remove the disagreement.
- When scales are incompatible or undefined, create no synthesized severity. List the original values and add an Open Question.
- Every P0/P1 from any source remains visible under Synthesized Findings. If its source explicitly calls it blocking, also include it under Blockers. Minority status never permits hiding, downgrading, or deletion.

## No-new-facts rule

Only reorganize, deduplicate, and label input content. Do not infer an unsupplied fact, evidence, root cause, production impact, owner, date, status, test result, defect disposition, severity, or quality/release conclusion from correlation, common knowledge, role identity, or project pressure.

Turn speculation only into a sourced Open Question or explicitly unverified risk hypothesis; never place it under Quality Facts. Synthesis cannot replace a Human or authorized decision-maker with an approval absent from the inputs.

## Output format

Output Markdown in this order:

1. **Stage and Input Coverage**: stage, received sources/roles, missing or incomplete role reports, and whether synthesis can proceed.
2. **Quality Facts**: each fact, evidence if supplied, and `sources`.
3. **Project Constraints**: each constraint/request, its status nature, and `sources`, physically separated from Quality Facts.
4. **Synthesized Findings**: for each item include `finding_id`, normalized statement, severity and rule explanation, `sources`, `source_roles`, evidence by source, risk, and confidence limits. Every item has at least one `sources` entry.
5. **Consensus**: agreed item and all supporting sources; write None when there is no consensus.
6. **Disagreements**: topic, each position/severity/evidence/source, unresolved reason, and required clarification. Always include this section and write None when no disagreement exists.
7. **Blockers**: only input-declared blockers or input gaps that prevent reliable synthesis, with sources. Write None when there are no blockers.
8. **Information Gaps**: deduplicated gap, impact, and sources. Record optional-role absence here.
9. **Open Questions**: question, triggering sources, and who must answer only if supplied.
10. **Actions**: action, sources, owner/date/status only if supplied, and related findings.
11. **Confidence and Limitations**: retain source confidence without arithmetic averaging; explain how input coverage, evidence, and conflict limit the synthesis.
12. **Source Register**: `source_id`, `source_role`, `stage`, and supplied/missing fields.

## Mandatory pre-output self-check

Check and correct every item before delivery:

- Does every Synthesized Finding cite at least one real input `source_id` or declared temporary locator?
- Does each equivalent finding retain every contributing source and role rather than one representative?
- Is Disagreements always present, explicitly stating None when no conflict exists?
- Are all original severities preserved, with no unexplained average, vote, downgrade, or override?
- Does every minority P0/P1 remain visible, and does a source-declared blocker also appear under Blockers?
- Are Project Constraints separate from Quality Facts, with no project/PM input incorrectly changing quality status?
- Is there any fact, evidence, root cause, impact, owner, date, status, or conclusion unsupported by the inputs? Delete it or convert it into an explicitly unverified Open Question.
- Is optional-role absence recorded only as a coverage/confidence limitation, with no invented content for that role?
