"""Shared contracts for the v3-v4 two-batch Skill rollout.

This module is deliberately data-only.  It records the reviewed Project card
IDs, the Capability Match decision, and the static package contract used by
the batch tests.  It does not call GitHub, invoke a model, or execute a real
target.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LANGUAGES = ("zh", "en")
PROJECT_NUMBER = 4
PROJECT_TITLE_PREFIX = "v3-v4 P2｜候选 Skill｜"
TARGET_SECTION = "testing-types"
CASES = (
    "basic-success.yaml",
    "edge-incomplete-input.yaml",
    "edge-scope-boundary.yaml",
)
REQUIRED_PACKAGE_FILES = (
    "SKILL.md",
    "prompts/{slug}.md",
    "agents/openai.yaml",
    "evals/eval.yaml",
    "evals/cases/basic-success.yaml",
    "evals/cases/edge-incomplete-input.yaml",
    "evals/cases/edge-scope-boundary.yaml",
    "evals/trigger-prompts.csv",
    "evals/local-rules.json",
)
SHARED_AUDIT_TERMS = (
    "known",
    "missing",
    "conflicting",
    "stale",
    "out_of_scope",
    "assumptions",
)


BATCH_1 = {
    "reliability-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc5w",
    "resilience-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc68",
    "chaos-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc8M",
    "failover-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc90",
    "recovery-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sc_w",
    "retry-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdAw",
    "timeout-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdCU",
    "circuit-breaker-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdEM",
    "dependency-failure-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdFo",
    "disaster-recovery-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdHI",
    "authentication-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdJA",
    "authorization-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdLg",
    "session-security-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdNI",
    "api-security-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdPY",
    "security-requirement-review": "PVTI_lAHOAHP1as4BjBhVzg6SdQ0",
    "threat-modeling": "PVTI_lAHOAHP1as4BjBhVzg6SdSk",
    "secrets-exposure-review": "PVTI_lAHOAHP1as4BjBhVzg6SdUg",
}

BATCH_2 = {
    "quality-gate-design": "PVTI_lAHOAHP1as4BjBhVzg6SdWc",
    "quality-metrics-design": "PVTI_lAHOAHP1as4BjBhVzg6SdY4",
    "quality-dashboard-design": "PVTI_lAHOAHP1as4BjBhVzg6SdaY",
    "quality-debt-analysis": "PVTI_lAHOAHP1as4BjBhVzg6SdcE",
    "quality-maturity-assessment": "PVTI_lAHOAHP1as4BjBhVzg6Sddo",
    "test-effectiveness-analysis": "PVTI_lAHOAHP1as4BjBhVzg6SdfA",
    "automation-roi-analysis": "PVTI_lAHOAHP1as4BjBhVzg6Sdg8",
    "testing-bottleneck-analysis": "PVTI_lAHOAHP1as4BjBhVzg6Sdig",
    "regression-optimization": "PVTI_lAHOAHP1as4BjBhVzg6SdkQ",
    "ci-test-optimization": "PVTI_lAHOAHP1as4BjBhVzg6SdnA",
    "test-runtime-optimization": "PVTI_lAHOAHP1as4BjBhVzg6Sdo4",
    "test-maintenance-cost-analysis": "PVTI_lAHOAHP1as4BjBhVzg6Sdqc",
    "quality-productivity-metrics": "PVTI_lAHOAHP1as4BjBhVzg6SdsA",
    "prompt-regression-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdtI",
    "rag-quality-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sdus",
    "rag-retrieval-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sdwg",
    "agent-loop-testing": "PVTI_lAHOAHP1as4BjBhVzg6SdyQ",
    "agent-memory-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sdzo",
    "agent-permission-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd1E",
    "agent-failure-recovery-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd2I",
    "agent-long-running-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd3w",
    "multi-agent-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd5g",
    "llm-hallucination-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd7Q",
    "llm-consistency-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd8Q",
    "ai-safety-testing": "PVTI_lAHOAHP1as4BjBhVzg6Sd9w",
}

CARD_IDS = {**BATCH_1, **BATCH_2}

PREFIXES = {
    "reliability-testing": "RLT-",
    "resilience-testing": "RES-",
    "chaos-testing": "CHS-",
    "failover-testing": "FOV-",
    "recovery-testing": "RCV-",
    "retry-testing": "RTY-",
    "timeout-testing": "TMO-",
    "circuit-breaker-testing": "CBR-",
    "dependency-failure-testing": "DPF-",
    "disaster-recovery-testing": "DRT-",
    "authentication-testing": "AUT-",
    "authorization-testing": "AZT-",
    "session-security-testing": "SST-",
    "api-security-testing": "AST-",
    "security-requirement-review": "SRR-",
    "threat-modeling": "THM-",
    "secrets-exposure-review": "SER-",
    "quality-gate-design": "QGD-",
    "quality-metrics-design": "QMD-",
    "quality-dashboard-design": "QDD-",
    "quality-debt-analysis": "QDA-",
    "quality-maturity-assessment": "QMA-",
    "test-effectiveness-analysis": "TEA-",
    "automation-roi-analysis": "ARO-",
    "testing-bottleneck-analysis": "TBA-",
    "regression-optimization": "RGO-",
    "ci-test-optimization": "CTO-",
    "test-runtime-optimization": "TRO-",
    "test-maintenance-cost-analysis": "TMC-",
    "quality-productivity-metrics": "QPM-",
    "prompt-regression-testing": "PRT-",
    "rag-quality-testing": "RAGQ-",
    "rag-retrieval-testing": "RAGT-",
    "agent-loop-testing": "ALT-",
    "agent-memory-testing": "AMT-",
    "agent-permission-testing": "AGP-",
    "agent-failure-recovery-testing": "AFR-",
    "agent-long-running-testing": "ALR-",
    "multi-agent-testing": "MAT-",
    "llm-hallucination-testing": "LHT-",
    "llm-consistency-testing": "LCT-",
    "ai-safety-testing": "AIS-",
}

DOMAIN_MARKERS = {
    "reliability-testing": {"zh": "可靠性目标", "en": "reliability objective"},
    "resilience-testing": {"zh": "韧性目标", "en": "resilience objective"},
    "chaos-testing": {"zh": "故障注入假设", "en": "fault-injection hypothesis"},
    "failover-testing": {"zh": "切换路径", "en": "failover path"},
    "recovery-testing": {"zh": "恢复目标", "en": "recovery objective"},
    "retry-testing": {"zh": "重试策略", "en": "retry policy"},
    "timeout-testing": {"zh": "超时策略", "en": "timeout policy"},
    "circuit-breaker-testing": {"zh": "熔断状态", "en": "circuit-breaker state"},
    "dependency-failure-testing": {"zh": "依赖故障", "en": "dependency failure"},
    "disaster-recovery-testing": {"zh": "灾备目标", "en": "disaster-recovery objective"},
    "authentication-testing": {"zh": "身份认证", "en": "authentication"},
    "authorization-testing": {"zh": "授权决策", "en": "authorization decision"},
    "session-security-testing": {"zh": "会话安全", "en": "session security"},
    "api-security-testing": {"zh": "API 安全", "en": "API security"},
    "security-requirement-review": {"zh": "安全需求", "en": "security requirement"},
    "threat-modeling": {"zh": "威胁场景", "en": "threat scenario"},
    "secrets-exposure-review": {"zh": "敏感信息暴露", "en": "secrets exposure"},
    "quality-gate-design": {"zh": "质量门禁", "en": "quality gate"},
    "quality-metrics-design": {"zh": "质量指标", "en": "quality metric"},
    "quality-dashboard-design": {"zh": "质量仪表盘", "en": "quality dashboard"},
    "quality-debt-analysis": {"zh": "质量债务", "en": "quality debt"},
    "quality-maturity-assessment": {"zh": "质量成熟度", "en": "quality maturity"},
    "test-effectiveness-analysis": {"zh": "测试有效性", "en": "test effectiveness"},
    "automation-roi-analysis": {"zh": "自动化投资回报", "en": "automation ROI"},
    "testing-bottleneck-analysis": {"zh": "测试瓶颈", "en": "testing bottleneck"},
    "regression-optimization": {"zh": "回归范围", "en": "regression scope"},
    "ci-test-optimization": {"zh": "CI 测试流水线", "en": "CI test pipeline"},
    "test-runtime-optimization": {"zh": "测试运行时间", "en": "test runtime"},
    "test-maintenance-cost-analysis": {"zh": "维护成本", "en": "maintenance cost"},
    "quality-productivity-metrics": {"zh": "质量生产力", "en": "quality productivity"},
    "rag-quality-testing": {"zh": "RAG 质量", "en": "RAG quality"},
    "rag-retrieval-testing": {"zh": "检索结果", "en": "retrieval result"},
    "agent-loop-testing": {"zh": "Agent 循环", "en": "Agent loop"},
    "agent-memory-testing": {"zh": "Agent 记忆", "en": "Agent memory"},
    "agent-permission-testing": {"zh": "Agent 权限", "en": "Agent permission"},
    "agent-failure-recovery-testing": {"zh": "Agent 故障恢复", "en": "Agent failure recovery"},
    "agent-long-running-testing": {"zh": "长运行 Agent", "en": "long-running Agent"},
    "multi-agent-testing": {"zh": "多 Agent 协作", "en": "multi-agent coordination"},
    "llm-hallucination-testing": {"zh": "LLM 幻觉", "en": "LLM hallucination"},
    "llm-consistency-testing": {"zh": "LLM 一致性", "en": "LLM consistency"},
    "ai-safety-testing": {"zh": "AI 安全", "en": "AI safety"},
}

NEW_SKILLS = tuple(slug for slug in CARD_IDS if slug != "prompt-regression-testing")

ENHANCEMENTS = {
    "prompt-regression-testing": {
        "target": "prompt-testing",
        "target_section": TARGET_SECTION,
        "mode": "prompt-regression",
        "prefix": "PRT-",
    }
}


def _targets(*slugs):
    return [
        path
        for slug in slugs
        for path in (
            f"skills/zh/{TARGET_SECTION}/{slug}/SKILL.md",
            f"skills/en/{TARGET_SECTION}/{slug}/SKILL.md",
        )
    ]


def _record(slug, conclusion, existing_targets, difference, *, target=None):
    return {
        "slug": slug,
        "target_section": TARGET_SECTION,
        "target": target or slug,
        "conclusion": conclusion,
        "existing_targets": existing_targets,
        "difference": difference,
    }


MATCH_RECORDS = {
    "reliability-testing": _record(
        "reliability-testing",
        "NEW",
        _targets("performance-testing", "production-incident-analysis"),
        "Adds a reliability-objective ledger covering availability, failure modes, and evidence readiness instead of generic performance or incident analysis.",
    ),
    "resilience-testing": _record(
        "resilience-testing",
        "NEW",
        _targets("performance-testing", "quality-risk-analysis"),
        "Adds resilience degradation and bounded recovery analysis; adjacent performance and risk Skills do not own the failure-mode contract.",
    ),
    "chaos-testing": _record(
        "chaos-testing",
        "NEW",
        _targets("performance-testing"),
        "Adds a controlled fault-injection hypothesis and safety boundary without injecting faults or claiming a chaos run.",
    ),
    "failover-testing": _record(
        "failover-testing",
        "NEW",
        _targets("production-incident-analysis", "quality-risk-analysis"),
        "Isolates primary-to-secondary failover paths, triggers, and recovery evidence rather than post-incident analysis.",
    ),
    "recovery-testing": _record(
        "recovery-testing",
        "NEW",
        _targets("production-incident-analysis"),
        "Defines recovery objectives, evidence gaps, and validation preparation; it does not execute recovery procedures.",
    ),
    "retry-testing": _record(
        "retry-testing",
        "NEW",
        _targets("api-testing", "api-negative-testing"),
        "Adds retry safety, idempotency, backoff, and exhaustion analysis beyond generic API test design.",
    ),
    "timeout-testing": _record(
        "timeout-testing",
        "NEW",
        _targets("api-testing", "performance-testing"),
        "Adds timeout budget, cancellation, and downstream-boundary analysis rather than general API or performance coverage.",
    ),
    "circuit-breaker-testing": _record(
        "circuit-breaker-testing",
        "NEW",
        _targets("api-testing", "production-incident-analysis"),
        "Adds closed, open, half-open, and fallback state evidence for circuit breakers; adjacent Skills do not model the state machine.",
    ),
    "dependency-failure-testing": _record(
        "dependency-failure-testing",
        "NEW",
        _targets("api-testing", "production-incident-analysis"),
        "Adds dependency fault taxonomy, isolation, and fallback analysis rather than API behavior or incident retrospectives.",
    ),
    "disaster-recovery-testing": _record(
        "disaster-recovery-testing",
        "NEW",
        _targets("production-incident-analysis", "capacity-planning-analysis"),
        "Adds disaster-recovery objectives, runbook evidence, and restore validation preparation without performing a drill.",
    ),
    "authentication-testing": _record(
        "authentication-testing",
        "NEW",
        _targets("security-testing", "api-testing"),
        "Narrows security analysis to identity proof, credential lifecycle, and authentication failure evidence.",
    ),
    "authorization-testing": _record(
        "authorization-testing",
        "NEW",
        _targets("security-testing", "api-testing"),
        "Narrows security analysis to subject-resource-action decisions, privilege boundaries, and authorization evidence.",
    ),
    "session-security-testing": _record(
        "session-security-testing",
        "NEW",
        _targets("security-testing"),
        "Adds session lifecycle, fixation, expiry, and revocation analysis beyond generic security review.",
    ),
    "api-security-testing": _record(
        "api-security-testing",
        "NEW",
        _targets("security-testing", "api-contract-testing"),
        "Combines API-specific attack surface and security contract review; generic security and schema contracts do not provide this boundary.",
    ),
    "security-requirement-review": _record(
        "security-requirement-review",
        "NEW",
        _targets("requirement-quality-review", "security-testing"),
        "Adds security requirement traceability and testability review rather than general requirement quality or vulnerability review.",
    ),
    "threat-modeling": _record(
        "threat-modeling",
        "NEW",
        _targets("security-testing", "technical-design-quality-review"),
        "Adds asset, trust-boundary, threat, and mitigation modeling with explicit assumptions; adjacent reviews do not own the model.",
    ),
    "secrets-exposure-review": _record(
        "secrets-exposure-review",
        "NEW",
        _targets("security-testing", "requirement-quality-review"),
        "Adds secret-location, lifecycle, and exposure evidence review without reading live credentials or declaring a clean scan.",
    ),
    "quality-gate-design": _record(
        "quality-gate-design",
        "NEW",
        _targets("test-reporting", "quality-risk-analysis"),
        "Defines evidence-based pass, block, and escalation rules rather than reporting results or ranking risk.",
    ),
    "quality-metrics-design": _record(
        "quality-metrics-design",
        "NEW",
        _targets("test-reporting", "metrics-anomaly-analysis"),
        "Defines metric contracts, denominator, freshness, and interpretation boundaries rather than reviewing a report or anomaly.",
    ),
    "quality-dashboard-design": _record(
        "quality-dashboard-design",
        "NEW",
        _targets("test-reporting", "metrics-anomaly-analysis"),
        "Defines dashboard evidence layout and drill-down semantics rather than producing a report or diagnosing an anomaly.",
    ),
    "quality-debt-analysis": _record(
        "quality-debt-analysis",
        "NEW",
        _targets("quality-risk-analysis", "production-incident-analysis"),
        "Adds quality-debt inventory, cost, risk, and repayment evidence instead of generic risk or incident analysis.",
    ),
    "quality-maturity-assessment": _record(
        "quality-maturity-assessment",
        "NEW",
        _targets("quality-risk-analysis", "requirement-quality-review"),
        "Adds maturity dimensions, evidence levels, and progression options without assigning unsupported scores or rankings.",
    ),
    "test-effectiveness-analysis": _record(
        "test-effectiveness-analysis",
        "NEW",
        _targets("test-reporting", "quality-risk-analysis"),
        "Adds effectiveness hypotheses and evidence mapping rather than treating test counts or reports as effectiveness proof.",
    ),
    "automation-roi-analysis": _record(
        "automation-roi-analysis",
        "NEW",
        _targets("automation-testing", "quality-risk-analysis"),
        "Adds cost, benefit, uncertainty, and decision boundaries for automation investment beyond automation design.",
    ),
    "testing-bottleneck-analysis": _record(
        "testing-bottleneck-analysis",
        "NEW",
        _targets("performance-bottleneck-analysis", "quality-risk-analysis"),
        "Adds testing-flow bottleneck evidence and intervention hypotheses rather than application performance diagnosis.",
    ),
    "regression-optimization": _record(
        "regression-optimization",
        "NEW",
        _targets("regression-scope-analysis", "regression-test-selection"),
        "Adds a full regression optimization trade-off across risk, feedback time, maintenance, and evidence; adjacent Skills cover only scope or selection.",
    ),
    "ci-test-optimization": _record(
        "ci-test-optimization",
        "NEW",
        _targets("automation-testing", "test-reporting"),
        "Adds CI stage, feedback, flake, artifact, and isolation optimization rather than generic automation or reporting.",
    ),
    "test-runtime-optimization": _record(
        "test-runtime-optimization",
        "NEW",
        _targets("performance-bottleneck-analysis", "automation-testing"),
        "Narrows optimization to test runtime evidence, queueing, parallelism, and reproducibility rather than product performance.",
    ),
    "test-maintenance-cost-analysis": _record(
        "test-maintenance-cost-analysis",
        "NEW",
        _targets("automation-testing", "quality-risk-analysis"),
        "Adds maintenance-cost evidence and prioritization for test assets rather than automation implementation or generic risk.",
    ),
    "quality-productivity-metrics": _record(
        "quality-productivity-metrics",
        "NEW",
        _targets("test-reporting", "metrics-anomaly-analysis"),
        "Defines quality-productivity measures without converting them into individual performance rankings or unsupported productivity claims.",
    ),
    "prompt-regression-testing": _record(
        "prompt-regression-testing",
        "ENHANCE",
        _targets("prompt-testing"),
        "Adds a prompt-testing regression mode for baseline, version, drift, and comparison evidence; the existing prompt-testing package can carry the mode, so no alias directory is created.",
        target="prompt-testing",
    ),
    "rag-quality-testing": _record(
        "rag-quality-testing",
        "NEW",
        _targets("llm-testing", "llm-evaluation-design"),
        "Adds end-to-end RAG quality evidence across grounding, answer utility, and retrieval dependencies rather than generic LLM evaluation.",
    ),
    "rag-retrieval-testing": _record(
        "rag-retrieval-testing",
        "NEW",
        _targets("llm-testing", "llm-evaluation-design"),
        "Isolates retrieval quality, query transformation, ranking, and evidence provenance from broader LLM testing.",
    ),
    "agent-loop-testing": _record(
        "agent-loop-testing",
        "NEW",
        _targets("ai-agent-testing", "agent-tool-testing"),
        "Adds loop termination, planning-act-observe transitions, and repeatability evidence beyond generic Agent or tool-call review.",
    ),
    "agent-memory-testing": _record(
        "agent-memory-testing",
        "NEW",
        _targets("ai-agent-testing"),
        "Adds memory write, retrieval, isolation, expiry, and contamination analysis beyond general Agent behavior.",
    ),
    "agent-permission-testing": _record(
        "agent-permission-testing",
        "NEW",
        _targets("agent-tool-testing", "security-testing"),
        "Adds Agent-specific authorization, least privilege, delegation, and side-effect evidence beyond generic tool or security review.",
    ),
    "agent-failure-recovery-testing": _record(
        "agent-failure-recovery-testing",
        "NEW",
        _targets("ai-agent-testing", "production-incident-analysis"),
        "Adds Agent failure classification, recovery policy, and safe resume evidence instead of generic Agent goals or incident review.",
    ),
    "agent-long-running-testing": _record(
        "agent-long-running-testing",
        "NEW",
        _targets("ai-agent-testing", "performance-testing"),
        "Adds long-running state, budget, checkpoint, and degradation analysis rather than generic Agent testing or product performance testing.",
    ),
    "multi-agent-testing": _record(
        "multi-agent-testing",
        "NEW",
        _targets("ai-agent-testing", "agent-tool-testing"),
        "Adds multi-Agent coordination, message ownership, conflict, and shared-state evidence beyond single-Agent and tool contracts.",
    ),
    "llm-hallucination-testing": _record(
        "llm-hallucination-testing",
        "NEW",
        _targets("llm-testing", "llm-evaluation-design"),
        "Adds claim verification, unsupported assertion, abstention, and source-grounding analysis rather than generic LLM evaluation.",
    ),
    "llm-consistency-testing": _record(
        "llm-consistency-testing",
        "NEW",
        _targets("llm-testing", "llm-evaluation-design"),
        "Adds repeat, perturbation, and invariant consistency analysis with explicit sampling limits beyond generic LLM testing.",
    ),
    "ai-safety-testing": _record(
        "ai-safety-testing",
        "NEW",
        _targets("ai-agent-testing", "security-testing"),
        "Adds AI safety hazard, refusal, misuse, and escalation evidence without claiming safety certification or universal coverage.",
    ),
}
