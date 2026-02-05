---
name: release-testing-workflow-en
description: Guides release testing from T-14 planning through Go/No-Go, deployment, and post-release. Covers functional, regression, performance, security, accessibility, and visual testing. Use when planning or executing release testing workflow.
---

# Release Testing Workflow

**中文版：** 见技能 `release-testing-workflow`。

End-to-end release testing (1–2 weeks before release through post-release). Prompts: see [reference.md](reference.md) and this directory's **`prompts/`**.

## When to Use

- User mentions **release testing**, **Go/No-Go**, or **release readiness**
- Need timeline: T-14 planning → T-7 feature freeze → T-5–T-4 specialized testing → T-3 RC → T-2 quality assessment → T-1 Go/No-Go → T-day release → T+1–T+7 post-release
- **Trigger:** e.g. “How do we schedule pre-release testing?” or “Go/No-Go checklist”

---

## Timeline

T-14 planning → T-10–T-8 prep → T-7 feature freeze & testing → T-5–T-4 specialized testing → T-3 RC → T-2 quality assessment → T-1 Go/No-Go → T release → T+1–T+7 post-release.

## T-14: Release Planning

Product/Engineering/QA/DevOps. Test Strategy + Requirements Analysis (risks). Deliverables: test plan, risk assessment, environment, regression scope, performance plan.

## T-10–T-8: Preparation

Pre-production environment, production-like data, monitoring, test accounts. Automation Testing (CI/CD) + Test Strategy (data). Update regression, performance, security, accessibility, visual; check critical-path automation and baselines.

## T-7: Feature Freeze & Test Acceleration

No new features, defect fixes only. Functional Testing + Test Case Writing (new/changed features, critical journeys, integration). Full regression + AI-Assisted Testing selection. Functional Testing E2E (full journeys, multi-system, third-party).

## T-5–T-4: Specialized Testing

- **Performance:** Performance Testing — load/stress/spike/endurance; P95/P99, throughput, error rate, resources.
- **Security:** Security Testing — scanning, penetration, auth/authz, encryption, security headers.
- **Accessibility:** Accessibility Testing — screen reader, keyboard, contrast, ARIA.
- **Visual:** Accessibility (visual) — visual regression, cross-browser, responsive, UI consistency.

## T-3: RC Testing

RC deploy, code freeze, tag. Smoke 1–2 h. Final regression (automation + manual + exploratory, Manual Testing). Defects: critical → fix → new RC; high → assess; medium/low → next release.

## T-2: Quality Assessment

Test Reporting + Test Strategy. Gates: critical fixed, regression 100%, performance SLA, security pass, no P1/P2, accessibility compliance. Risk assessment: known issues, load, third-party, rollback.

## T-1: Go/No-Go

Review summary, defects, performance, security, risk, rollback. GO: gates pass, no critical, performance acceptable, team confidence, rollback ready. NO-GO: otherwise. Checklist: release notes, deployment runbook, monitoring, rollback tested, support, communication.

## T-day: Release

Pre-deploy: RC smoke, checklist, on-call. During: monitor. Post 30–60 min production smoke; first 24 h monitor. Rollback conditions: critical failure, severe performance, data corruption, security vulnerability.

## T+1–T+7: Post-Release

Day 1 intensive monitoring; week 1 stabilize, feedback, hotfixes. Retro (Test Reporting): what went well/improvements, test gaps, process improvements.

## Contingency

Critical defect: assess → hotfix or rollback. Performance: isolate → impact → quick fix or rollback. Security: assess → contain → rollback if needed → incident response.

## Release Checklist

Pre-release: plan approved, environment/data, automation, training. Test phase: functional/regression/performance/security/accessibility/visual. Pre-deploy: RC, gates, Go/No-Go, deploy & rollback. Post-deploy: smoke, monitoring, on-call, communication.

## How to Use the Prompts

For each step: 1) Check [reference.md](reference.md) for the prompt file; 2) Open that file under this directory’s `prompts/`; 3) Combine the prompt with the current release context (scope, environment, gate criteria) and run with the AI.

## Common Pitfalls

- ❌ Adding features after T-7 → ✅ Feature freeze: only defect fixes; non-critical code freeze
- ❌ Releasing without Go/No-Go → ✅ Release only after gates pass, team alignment, and rollback readiness
- ❌ No post-release monitoring → ✅ T+1 intensive monitoring and fast response; follow incident procedures

## Best Practices

- T-14: use test strategy and requirements prompts for release plan and risk assessment
- T-2: use test reporting and test strategy for quality gates and known-issue assessment
- Before deploy: confirm rollback tested, communication plan and support brief ready
- **Principle:** When in doubt, delay release.

## Reference Files

- **[reference.md](reference.md)** — Step-to-prompt file mapping
- **prompts/** — English prompt files for this workflow (open the matching `.md` per step and use with context)

**Related:** daily-testing-workflow-en, sprint-testing-workflow-en.
