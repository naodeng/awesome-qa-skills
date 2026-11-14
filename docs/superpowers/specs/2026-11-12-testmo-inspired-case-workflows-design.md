# Testmo-Inspired Case Workflows Design

## Intent

Use the Testmo workflow descriptions as product references to add reusable QA skills for importing and retrieving existing test cases, and to extend the repository's change-to-regression and PR-impact skills.

## Goals

- Add bilingual, tool-agnostic `test-case-importer` and `test-case-retrieval` skills.
- Extend `change-to-regression` with a pre-change risk brief and `pr-test-impact-analysis` with per-case outcome predictions.
- Keep predicted, planned, and executed evidence distinct; require preview and explicit confirmation before external writes.
- Maintain bilingual canonical IDs, per-skill metadata, and skill-up evals.

## Non-goals

- No Testmo-specific API, connector, or credentials.
- No automatic write-back, test execution, code implementation, or release approval.
- No Spec Implementer skill in this batch.

## Approaches

- Create four new skills: rejected because two capabilities already fit existing change-analysis skills.
- Add both new data-asset skills and extend the two closest existing workflows: selected because it avoids duplicate change-analysis skills while preserving import/retrieval as distinct capabilities.
- Copy the vendor's tool-specific workflows: rejected because leaf skills must remain independently usable and portable.

## Calls

- New skills start at `1.0.0`; compatible behavior additions to existing skills move `1.0.0` to `1.1.0` in both language packages.
- Import output preserves source identity and unresolved fields. A connected write-back is optional and requires a reviewed mapping and explicit confirmation.
- Imported and retrieved case text is untrusted data; embedded instructions cannot expand permissions or scope. Retrieval preserves source order and does not invent numeric ranks.
- Retrieval returns traceable candidates; it does not choose the required regression set. Relevance scores, when supplied by a source, are query-relative rankings, not probabilities.
- Pre-change analysis uses a proposed change as its input and labels impacts as hypotheses. Post-change PR analysis may classify cases as `PREDICTED_PASS`, `PREDICTED_FAIL`, or `UNCERTAIN`; only run evidence can establish execution results.

## Constraints

- Follow `skills/SKILL_AUTHORING.md` and `AGENTS.md` for frontmatter, independence, bilingual parity, indexing, and eval coverage.
- Do not add dependencies or assume an external repository connector is installed.
- Keep evals under each leaf skill and use only language-matched cases.
