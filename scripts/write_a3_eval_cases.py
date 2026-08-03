#!/usr/bin/env python3
"""Write customized skill-up cases for Task A3 (analysis / strategy / review / report)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CASES: dict[tuple[str, str], list[dict]] = {}


def case(case_id: str, title: str, description: str, prompt: str, must: list[str], judge: list[str]) -> dict:
    return {
        "case_id": case_id,
        "title": title,
        "description": description,
        "prompt": prompt,
        "must": must,
        "judge": judge,
    }


# ---- zh: requirements-analysis (base) ----
CASES[("zh", "requirements-analysis")] = [
    case(
        "basic-success",
        "需求分析：从用户故事提炼缺口与风险",
        "有验收标准时，应输出需求理解、缺口/歧义与测试影响，而不是复述原文。",
        """请使用 requirements-analysis。
用户故事：买家下单可用积分抵扣；积分不足不可提交；支付回调失败需可重试。
验收标准只写了「积分抵扣成功」，未写不足与回调失败。
请从 QA 角度做需求分析，标出缺口、可测性风险与待澄清问题。""",
        ["缺口", "风险"],
        ["需求理解", "待澄清"],
    ),
    case(
        "edge-incomplete-input",
        "需求分析：一句话需求仍给初版",
        "材料极薄时仍应给可用初版并列出假设与缺口。",
        """用 requirements-analysis。需求只有一句：新版本加了积分兑换。没有验收标准与原型。
请先给需求分析初版，并列出必须补齐的信息。""",
        ["假设", "缺口"],
        ["假设", "缺口"],
    ),
    case(
        "edge-risk-priority",
        "需求分析：短窗口只盯高风险缺口",
        "功能很多时必须按业务风险排缺口优先级，而不是平均分析。",
        """使用 requirements-analysis。范围含登录、搜索、下单、支付、优惠券、积分、工单、报表。
发版窗口半天。请只保留对发布阻塞影响最大的需求缺口与风险，说明其余可后置。""",
        ["P0", "风险"],
        ["优先级", "缺口"],
    ),
]

# ---- zh: requirements-analysis-plus ----
CASES[("zh", "requirements-analysis-plus")] = [
    case(
        "basic-success",
        "需求分析增强：跨文档冲突必须点出",
        "多来源材料冲突时，应做交叉对照并输出冲突/跨来源缺口（相对基础版的增强点）。",
        """请使用 requirements-analysis-plus。
材料 A（需求 Word）：积分不足时仍允许提交订单，后台事后扣减。
材料 B（接口 Markdown）：积分不足返回 400，禁止创建订单。
材料 C（Excel 范围表）：本迭代仅含「积分抵扣成功路径」。
请交叉检查来源一致性，输出冲突、可测性风险与应优先澄清的问题。""",
        ["冲突", "来源"],
        ["跨来源", "风险"],
    ),
    case(
        "edge-incomplete-input",
        "需求分析增强：多格式残缺仍给结构化初版",
        "Word/HTML/JSON 残缺时仍应产出结构化分析，并标明各来源缺口。",
        """用 requirements-analysis-plus。手头有：半页 Word 需求摘要、一段 HTML 原型说明、一份字段不全的 JSON 样例。
都未写异常与边界。请给结构化需求分析初版，并按来源列出缺口与假设。""",
        ["假设", "缺口"],
        ["来源", "缺口"],
    ),
    case(
        "edge-risk-priority",
        "需求分析增强：冲突项优先于文案润色",
        "短窗口下应优先处理跨来源冲突与交付阻塞，而不是平均总结。",
        """使用 requirements-analysis-plus。PRD 与技术文档在支付回调幂等上互相矛盾；其余模块描述完整。
半天内要决定能否提测。请按业务影响排出高优先级风险与必须先澄清的冲突项。""",
        ["冲突", "优先级"],
        ["高优先级", "澄清"],
    ),
]

# ---- zh: test-strategy ----
CASES[("zh", "test-strategy")] = [
    case(
        "basic-success",
        "测试策略：按风险给出覆盖与取舍",
        "有范围与风险时，应输出优先级、推荐方案与覆盖取舍。",
        """请使用 test-strategy。
项目：电商订单发版；核心链路下单→支付→发货；已知风险：支付回调偶发超时。
团队 2 名 QA，SIT 可用，一周窗口。请给出基于风险的测试策略，写清覆盖与取舍。""",
        ["优先级", "取舍"],
        ["风险", "覆盖"],
    ),
    case(
        "edge-incomplete-input",
        "测试策略：缺团队/环境信息仍给初版",
        "缺少资源与环境细节时仍应给策略初版并标假设。",
        """用 test-strategy。产品只说「积分兑换要测一下」，没有团队人数、环境与质量目标。
请给策略初版，并把资源/环境相关项标为假设或缺口。""",
        ["假设", "缺口"],
        ["假设", "范围"],
    ),
    case(
        "edge-risk-priority",
        "测试策略：半天窗口强制砍范围",
        "功能很多时必须明确 P0 与暂不覆盖项。",
        """使用 test-strategy。功能：登录、搜索、下单、支付、优惠券、积分、工单、报表。
发版窗口半天。请只保留最关键测试策略，并说明哪些抽样/暂不覆盖。""",
        ["P0", "覆盖"],
        ["取舍", "优先级"],
    ),
]

# ---- zh: test-strategy-plus ----
CASES[("zh", "test-strategy-plus")] = [
    case(
        "basic-success",
        "测试策略增强：必须含里程碑与质量门槛",
        "相对基础版，增强点是里程碑、质量门槛与责任安排，而不只是方法列表。",
        """请使用 test-strategy-plus。
输入材料：需求摘要、技术说明、发布计划（周五上线）。
范围：下单→支付→发货；风险：支付回调超时；QA 2 人。
请输出可执行策略，必须包含里程碑、质量门槛、资源与责任说明。""",
        ["里程碑", "质量门槛"],
        ["责任", "优先级"],
    ),
    case(
        "edge-incomplete-input",
        "测试策略增强：缺计划文档仍起草门槛假设",
        "缺发布计划时仍应起草策略，并把里程碑/门槛标为假设。",
        """用 test-strategy-plus。只有需求分析结论「积分兑换高风险」，没有项目计划与资源表。
请给增强版策略初版；凡里程碑与质量门槛数字均标为假设，并列出缺口。""",
        ["假设", "缺口"],
        ["里程碑", "假设"],
    ),
    case(
        "edge-risk-priority",
        "测试策略增强：短窗口用门槛做砍范围依据",
        "半天窗口下应用质量门槛与责任边界说明暂不覆盖项。",
        """使用 test-strategy-plus。模块很多：登录、搜索、下单、支付、优惠券、积分、工单、报表。
半天必须给出能否上线建议。请用风险优先级 + 质量门槛保留 P0，写清责任与可延后项。""",
        ["质量门槛", "P0"],
        ["责任", "里程碑"],
    ),
]

# ---- zh: test-case-reviewer ----
CASES[("zh", "test-case-reviewer")] = [
    case(
        "basic-success",
        "用例评审：指出漏测与弱预期",
        "有现成用例时，应指出高优先级发现与缺失场景，而不是只夸格式。",
        """请使用 test-case-reviewer。
需求：积分不足不可提交；支付回调失败可重试。
现有用例仅 2 条正向：① 积分足够抵扣成功 ② 订单创建成功。无异常/边界，预期只写「成功」。
请评审并给出高优先级发现、缺失场景与修改顺序。""",
        ["缺失", "优先级"],
        ["评审", "场景"],
    ),
    case(
        "edge-incomplete-input",
        "用例评审：无需求文档仍可审结构",
        "缺少完整需求时仍应评审可执行性并列出待确认项。",
        """用 test-case-reviewer。只有用例标题列表「兑换成功/失败」，没有需求与步骤详情。
请给评审初版：能指出的结构/清晰度问题，以及必须补齐才能继续审的信息。""",
        ["缺口", "确认"],
        ["评审", "缺口"],
    ),
    case(
        "edge-risk-priority",
        "用例评审：短窗口只盯阻塞级漏测",
        "时间紧时应优先支付/资金相关漏测，而不是文案问题。",
        """使用 test-case-reviewer。用例很多且格式不统一；已知支付成功但订单仍待支付的线上风险。
半天内只能改一轮。请只保留阻塞级高优先级发现，并说明其余可后置。""",
        ["支付", "优先级"],
        ["高优先级", "风险"],
    ),
]

# ---- zh: test-case-reviewer-plus ----
CASES[("zh", "test-case-reviewer-plus")] = [
    case(
        "basic-success",
        "用例评审增强：问题必须带等级与补测顺序",
        "相对基础版，增强点是严重度分级、业务影响与明确补测顺序。",
        """请使用 test-case-reviewer-plus。
材料：需求、策略摘要、现有用例。
需求要求覆盖积分不足拒绝提交与支付回调重试；用例只有正向成功路径，预期含糊。
请输出严重问题/一般问题、高风险缺失场景，以及修改优先级和补测顺序（每项带业务影响）。""",
        ["严重", "补测"],
        ["业务影响", "优先级"],
    ),
    case(
        "edge-incomplete-input",
        "用例评审增强：材料不全仍先定严重度",
        "缺技术文档时仍应按可判定证据给出问题等级，并标假设。",
        """用 test-case-reviewer-plus。只有用例表与半页需求，没有技术文档与缺陷历史。
请给增强版评审初版：能定级的先定级，无法定级的标假设/缺口，并给临时补测顺序。""",
        ["假设", "缺口"],
        ["严重", "补测"],
    ),
    case(
        "edge-risk-priority",
        "用例评审增强：用业务影响压缩修复队列",
        "短窗口下修复队列必须按严重度与业务影响排序，不能平均改。",
        """使用 test-case-reviewer-plus。发现问题包括：报表文案错、搜索无边界用例、支付回调无重试覆盖。
半天只能修最关键项。请按业务影响排出修改优先级和补测顺序，明确可延后项。""",
        ["支付", "补测"],
        ["业务影响", "严重"],
    ),
]

# ---- zh: testcase-writer-plus ----
CASES[("zh", "testcase-writer-plus")] = [
    case(
        "basic-success",
        "用例编写增强：优先级分组 + 可追踪性",
        "相对基础 test-case-writing，增强点是多来源输入下的追踪/分组与更严结构。",
        """请使用 testcase-writer-plus。
来源：需求 REQ-01（积分抵扣）、分析结论（不足须拒绝）、接口说明（回调可重试）。
请编写按优先级分组的测试用例，每条含前置条件、步骤、预期与数据；并给出追踪或分组说明（用例↔需求/风险）。""",
        ["优先级", "追踪"],
        ["前置条件", "预期"],
    ),
    case(
        "edge-incomplete-input",
        "用例编写增强：缺 AC 仍出可追踪草稿",
        "无验收标准时仍应出草稿用例，追踪项标假设，并列出缺口。",
        """用 testcase-writer-plus。只有「支持积分兑换」一句话与一张字段不全的 Excel。
请给增强版用例草稿：标出假设、可追踪性暂用临时 ID，并列出必须向产品确认的问题。""",
        ["假设", "缺口"],
        ["追踪", "优先级"],
    ),
    case(
        "edge-risk-priority",
        "用例编写增强：短窗口只保 P0 追踪集",
        "功能很多时只输出 P0 用例集，并说明追踪范围内外项。",
        """使用 testcase-writer-plus。模块：登录、搜索、下单、支付、优惠券、积分、工单、报表。
半天可执行。请只输出 P0 用例，附追踪/分组说明，并标明哪些需求点本轮不追踪。""",
        ["P0", "追踪"],
        ["优先级", "缺口"],
    ),
]

# ---- zh: test-reporting ----
CASES[("zh", "test-reporting")] = [
    case(
        "basic-success",
        "测试报告：结论与发布建议可决策",
        "有结果与缺陷时，应输出结论摘要、关键风险与明确发布建议。",
        """请使用 test-reporting。
范围：下单→支付已测；发货未测。执行 40 条，通过 36，失败 4。
阻塞缺陷：支付成功订单仍待支付（偶发）。环境：SIT。
请写测试报告，给出发布建议与下一步动作。""",
        ["发布建议", "阻塞"],
        ["风险", "结论"],
    ),
    case(
        "edge-incomplete-input",
        "测试报告：只有通过率仍要标缺口",
        "缺缺陷详情与未测范围时，不得用通过率粉饰，应标假设与缺口。",
        """用 test-reporting。同事只说「通过率 95%」，没有失败用例、缺陷单与未测范围。
请写报告初版，明确不能据此放行的原因，并列出必须补齐的信息。""",
        ["假设", "缺口"],
        ["通过率", "风险"],
    ),
    case(
        "edge-risk-priority",
        "测试报告：高通过率不能掩盖资金风险",
        "指标好看但存在支付类阻塞时，发布建议必须偏谨慎。",
        """使用 test-reporting。通过率 98%，但有 1 个支付双扣费偶发缺陷未解；报表导出慢 20s。
请写报告：区分关键风险与次要问题，给出明确发布建议（含信心说明）。""",
        ["支付", "发布建议"],
        ["风险", "阻塞"],
    ),
]

# ---- en: requirements-analysis ----
CASES[("en", "requirements-analysis")] = [
    case(
        "basic-success",
        "Requirements analysis: gaps and risks from stories",
        "With partial AC, return understanding, gaps/ambiguities, and test impact—not a restatement.",
        """Use requirements-analysis.
Story: buyers can redeem points at checkout; insufficient points must block submit; payment callback failures must be retryable.
AC only covers 'points redemption succeeds'.
Analyze from a QA lens: gaps, testability risks, and questions to resolve.""",
        ["gap", "risk"],
        ["Understanding", "Questions"],
    ),
    case(
        "edge-incomplete-input",
        "Requirements analysis: one-line requirement still drafts",
        "Thin input still yields a draft with assumptions and gaps.",
        """Use requirements-analysis. Requirement is only: new release adds points redemption. No AC or prototype.
Provide a first-draft analysis and list information that must be filled in.""",
        ["assumption", "gap"],
        ["assumption", "gap"],
    ),
    case(
        "edge-risk-priority",
        "Requirements analysis: short window focuses blocking gaps",
        "Many features require risk-ranked gaps, not equal analysis.",
        """Use requirements-analysis. Scope: login, search, checkout, payment, coupons, points, tickets, reports.
Half-day window. Keep only release-blocking requirement gaps/risks and say what can wait.""",
        ["P0", "risk"],
        ["priority", "gap"],
    ),
]

# ---- en: requirements-analysis-plus ----
CASES[("en", "requirements-analysis-plus")] = [
    case(
        "basic-success",
        "Requirements analysis plus: cross-source conflicts",
        "Plus differentiator: cross-check multi-format sources and surface conflicts/consistency.",
        """Use requirements-analysis-plus.
Source A (Word PRD): allow order submit when points are insufficient; deduct later.
Source B (API Markdown): return 400 and block order creation when points are insufficient.
Source C (Excel scope): this sprint only covers the happy-path points redemption.
Cross-check source consistency; output conflicts, testability risks, and questions to resolve first.""",
        ["conflict", "source"],
        ["Cross-Source", "risk"],
    ),
    case(
        "edge-incomplete-input",
        "Requirements analysis plus: partial multi-format inputs",
        "Incomplete Word/HTML/JSON still gets structured analysis with per-source gaps.",
        """Use requirements-analysis-plus. Materials: half-page Word summary, HTML prototype notes, incomplete JSON sample.
No exception/boundary rules. Draft a structured analysis and list gaps/assumptions by source.""",
        ["assumption", "gap"],
        ["source", "gap"],
    ),
    case(
        "edge-risk-priority",
        "Requirements analysis plus: conflicts outrank polish",
        "Short window prioritizes cross-source conflicts that block delivery.",
        """Use requirements-analysis-plus. PRD and tech docs contradict each other on payment-callback idempotency; other modules look complete.
Half a day to decide test entry. Rank high-priority risks and conflicts that must be clarified first.""",
        ["conflict", "priority"],
        ["High-Priority", "clarif"],
    ),
]

# ---- en: test-strategy ----
CASES[("en", "test-strategy")] = [
    case(
        "basic-success",
        "Test strategy: risk-based coverage and tradeoffs",
        "With scope and risks, return priorities, approach, and explicit tradeoffs.",
        """Use test-strategy.
Project: ecommerce order release; flow place order → pay → ship; known risk: intermittent payment-callback timeout.
2 QA, SIT available, one-week window. Produce a risk-based strategy with coverage and tradeoffs.""",
        ["priority", "tradeoff"],
        ["risk", "coverage"],
    ),
    case(
        "edge-incomplete-input",
        "Test strategy: draft despite missing team/env",
        "Missing resources/env still yields a draft with assumptions.",
        """Use test-strategy. Product only says 'please test points redemption' with no team size, env, or quality goals.
Draft a strategy and mark resource/env items as assumptions or gaps.""",
        ["assumption", "gap"],
        ["assumption", "scope"],
    ),
    case(
        "edge-risk-priority",
        "Test strategy: half-day forces cut scope",
        "Many features require explicit P0 vs not-covered items.",
        """Use test-strategy. Features: login, search, checkout, payment, coupons, points, tickets, reports.
Half-day window. Keep only the critical strategy and state what is sampled or deferred.""",
        ["P0", "coverage"],
        ["tradeoff", "priority"],
    ),
]

# ---- en: test-strategy-plus ----
CASES[("en", "test-strategy-plus")] = [
    case(
        "basic-success",
        "Test strategy plus: milestones and quality gates",
        "Plus differentiator: milestones, quality gates, and ownership—not method lists alone.",
        """Use test-strategy-plus.
Inputs: requirement summary, tech notes, release plan (ship Friday).
Scope: place order → pay → ship; risk: payment-callback timeout; 2 QA.
Produce an executable strategy that includes milestones, quality gates, and ownership/resource notes.""",
        ["milestone", "gate"],
        ["ownership", "priority"],
    ),
    case(
        "edge-incomplete-input",
        "Test strategy plus: draft gates as assumptions",
        "Without a project plan, still draft strategy and mark milestones/gates as assumptions.",
        """Use test-strategy-plus. Only analysis note 'points redemption is high risk'; no project plan or staffing sheet.
Draft a plus strategy; mark every milestone/gate number as an assumption and list gaps.""",
        ["assumption", "gap"],
        ["milestone", "assumption"],
    ),
    case(
        "edge-risk-priority",
        "Test strategy plus: gates justify scope cuts",
        "Half-day window uses gates and ownership to keep P0 only.",
        """Use test-strategy-plus. Modules: login, search, checkout, payment, coupons, points, tickets, reports.
Must advise go/no-go within half a day. Use risk priority + quality gates to keep P0; clarify ownership and deferrals.""",
        ["gate", "P0"],
        ["ownership", "milestone"],
    ),
]

# ---- en: test-case-reviewer ----
CASES[("en", "test-case-reviewer")] = [
    case(
        "basic-success",
        "Test case review: missing scenarios and weak expects",
        "Review existing cases for high-priority findings and missing scenarios.",
        """Use test-case-reviewer.
Requirement: block submit when points insufficient; payment callback failures must be retryable.
Existing cases: only two happy paths with expected result 'success'. No exception/boundary.
Review and return high-priority findings, missing scenarios, and fix order.""",
        ["missing", "priority"],
        ["Review", "scenario"],
    ),
    case(
        "edge-incomplete-input",
        "Test case review: titles-only still reviews structure",
        "Without full requirements, still review clarity and list confirmations needed.",
        """Use test-case-reviewer. Only case titles 'redeem success/fail'—no requirements or steps.
Draft a review: structural/clarity issues you can already see, plus info required to continue.""",
        ["gap", "confirm"],
        ["Review", "gap"],
    ),
    case(
        "edge-risk-priority",
        "Test case review: short window targets blockers",
        "Time pressure prioritizes payment/money gaps over wording nits.",
        """Use test-case-reviewer. Many inconsistent cases; known prod risk: payment succeeds but order stays pending.
Only one fix pass possible. Keep blocking high-priority findings and defer the rest.""",
        ["payment", "priority"],
        ["High-Priority", "risk"],
    ),
]

# ---- en: test-case-reviewer-plus ----
CASES[("en", "test-case-reviewer-plus")] = [
    case(
        "basic-success",
        "Test case review plus: severity grades and retest order",
        "Plus differentiator: severity levels, business impact, and explicit retest order.",
        """Use test-case-reviewer-plus.
Materials: requirements, strategy notes, existing cases.
Requirements require insufficient-points rejection and payment-callback retry; cases are happy-path only with vague expects.
Return critical/major findings, missing high-risk scenarios, plus fix priority and retest order (with business impact).""",
        ["critical", "retest"],
        ["impact", "priority"],
    ),
    case(
        "edge-incomplete-input",
        "Test case review plus: grade what evidence allows",
        "Missing tech docs still assigns severity where possible and marks assumptions.",
        """Use test-case-reviewer-plus. Only a case sheet and half-page requirements; no tech docs or defect history.
Draft a plus review: grade what you can, mark assumptions/gaps otherwise, and give a provisional retest order.""",
        ["assumption", "gap"],
        ["critical", "retest"],
    ),
    case(
        "edge-risk-priority",
        "Test case review plus: business impact compresses the queue",
        "Short window ranks the fix queue by severity and business impact.",
        """Use test-case-reviewer-plus. Findings: report typo, missing search boundary cases, no payment-callback retry coverage.
Half a day to fix. Rank fix priority and retest order by business impact; state deferrals.""",
        ["payment", "retest"],
        ["impact", "critical"],
    ),
]

# ---- en: testcase-writer-plus ----
CASES[("en", "testcase-writer-plus")] = [
    case(
        "basic-success",
        "Testcase writer plus: priority groups and traceability",
        "Plus differentiator vs test-case-writing: multi-source traceability/grouping and stricter structure.",
        """Use testcase-writer-plus.
Sources: REQ-01 (points redemption), analysis (insufficient points must reject), API note (callback retryable).
Write priority-grouped cases with preconditions, steps, expected results, and data; include traceability or grouping notes (case ↔ requirement/risk).""",
        ["priority", "trace"],
        ["precondition", "expected"],
    ),
    case(
        "edge-incomplete-input",
        "Testcase writer plus: draft traceable cases without AC",
        "Without AC, still draft cases with temporary trace IDs and list gaps.",
        """Use testcase-writer-plus. Only 'support points redemption' plus an incomplete Excel sheet.
Draft plus cases: mark assumptions, use temporary IDs for traceability, and list product questions.""",
        ["assumption", "gap"],
        ["trace", "priority"],
    ),
    case(
        "edge-risk-priority",
        "Testcase writer plus: keep P0 traced set only",
        "Many modules → only P0 cases with in/out-of-trace notes.",
        """Use testcase-writer-plus. Modules: login, search, checkout, payment, coupons, points, tickets, reports.
Half-day execution. Output only P0 cases with traceability/grouping notes and state what is out of scope this round.""",
        ["P0", "trace"],
        ["priority", "gap"],
    ),
]

# ---- en: test-reporting ----
CASES[("en", "test-reporting")] = [
    case(
        "basic-success",
        "Test reporting: actionable release recommendation",
        "With results and defects, return summary, key risks, and a clear release recommendation.",
        """Use test-reporting.
Scope: checkout→payment tested; shipping not tested. 40 cases run, 36 pass, 4 fail.
Blocker: payment succeeds but order stays pending (intermittent). Env: SIT.
Write a test report with release recommendation and next actions.""",
        ["recommendation", "blocker"],
        ["risk", "summary"],
    ),
    case(
        "edge-incomplete-input",
        "Test reporting: pass rate alone is not enough",
        "Without failures/untested scope, do not greenwash; mark assumptions and gaps.",
        """Use test-reporting. Colleague only says '95% pass rate' with no failures, defects, or untested scope.
Draft a report explaining why that is insufficient to ship, and list required follow-ups.""",
        ["assumption", "gap"],
        ["pass", "risk"],
    ),
    case(
        "edge-risk-priority",
        "Test reporting: high pass rate must not hide money risk",
        "Strong metrics with a payment blocker still require a cautious recommendation.",
        """Use test-reporting. Pass rate 98%, but one intermittent double-charge payment defect remains; report export is 20s slower.
Write the report: separate critical vs minor issues and give a clear release recommendation with confidence.""",
        ["payment", "recommendation"],
        ["risk", "blocker"],
    ),
]


def render(case_data: dict, lang: str) -> str:
    prompt_lines = "\n".join(f"    {line}" if line else "" for line in case_data["prompt"].splitlines())
    must = "\n".join(f'    - "{x}"' for x in case_data["must"])
    judge = "\n".join(f'          - "{x}"' for x in case_data["judge"])
    bad = '"我无法"' if lang == "zh" else '"I cannot"'
    return f"""id: {case_data['case_id']}
title: {case_data['title']}
description: |
  {case_data['description']}

input:
  prompt: |
{prompt_lines}

expect:
  must_contain:
{must}
  must_not_contain:
    - "TODO"
    - {bad}

judge:
  type: rule_based
  success:
    - output_contains:
        all:
{judge}
"""


def main() -> None:
    for (lang, skill), cases in CASES.items():
        base = ROOT / "skills" / lang / "testing-types" / skill / "evals" / "cases"
        if not base.exists():
            raise SystemExit(f"missing {base}")
        for c in cases:
            path = base / f"{c['case_id']}.yaml"
            path.write_text(render(c, lang), encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
