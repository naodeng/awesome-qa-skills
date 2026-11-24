# AI-Generated Code Risk Checklist

Review each applicable item and leave missing evidence as a verification gap:

- **Intent and scope**: Do the task, acceptance criteria, baseline, and changed files align? Are there unrelated files, duplicate code, or unauthorized side effects?
- **Dependencies and APIs**: Can package names, APIs, fields, parameters, and versions be checked in lockfiles, repository material, source, or a trusted registry?
- **Errors and fallbacks**: Does the code swallow exceptions, return silent defaults, hide partial failure, fabricate cached/success state, or turn failure paths into success?
- **Behavior tests**: Does each critical acceptance criterion have an independent observable assertion? Does a test mock the subject, remove negative paths, or change only to fit the implementation?
- **CI integrity**: Were required jobs, coverage thresholds, lint/typecheck, or security scans deleted, weakened, conditionally skipped, or changed to `continue-on-error`?
- **Copy/paste and supply boundaries**: Is duplicate implementation, unreviewed generated code/dependency, or untrusted PR/issue/document text being sent to scripts, a shell, or Agent tools?
- **Evidence and ownership**: Are provenance, run, Human review, and adoption supported by evidence? Missing model identity is not an implementation defect by itself.

Do not mechanically turn this checklist into findings. Each formal finding needs change evidence, a trigger, impact, and a verifiable repair.
