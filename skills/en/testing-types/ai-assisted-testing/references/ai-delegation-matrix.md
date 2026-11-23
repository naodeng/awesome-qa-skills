# AI Delegation Matrix

Use this matrix to assign draft work while keeping human ownership and acceptance evidence clear. AI capability does not grant installation, invocation, data-use, or release authorization.

| Artifact | Stage | AI may do | Human must do | Minimum evidence |
| --- | --- | --- | --- | --- |
| Requirements and risks | Clarification, analysis | Summarize, locate conflicts, draft questions | Confirm business rules, priority, and scope | Source requirement version, confirmer, decision record |
| Strategy and test cases | Design | Draft scenarios/boundaries and suggest trace links | Verify business oracles, assertions, and risk coverage | Source requirements, draft ID, review decision |
| Test data and scripts | Preparation, implementation | Draft sanitized samples/scripts and static-check suggestions | Confirm data permission, execution safety, and assertions | Data classification, script version, review, run evidence |
| Defects and reports | Analysis, communication | Cluster, summarize, index evidence, draft trends | Verify raw logs, reproduction, severity, and conclusions | Defect ID, raw execution record, report version |
| Release or high-risk decision | Gate, approval | Summarize verified evidence and gaps | Accept risk, make Go/No-Go, approve release | Gate record, owner, traceable evidence |

Track `source_snapshot_id`, `assistant/model`, `prompt/instruction_version`, `draft_id`, `reviewer`, `review_decision`, `adopted_version_id`, and `execution_evidence` for each draft. Mark missing fields `UNKNOWN`; never promote work to a formal asset without human adoption.
