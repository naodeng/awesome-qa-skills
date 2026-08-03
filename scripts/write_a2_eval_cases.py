#!/usr/bin/env python3
"""Write skill-specific skill-up cases for Task A2 (perf/security/exploratory set)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CASES: dict[tuple[str, str], list[dict]] = {}

EVAL_YAML = """\
schema_version: v1alpha1

environment:
  type: none

skills:
  - source: local_path
    path: .

engine:
  name: claude_code
  # model is optional; omit to use engine default
  # model:
  #   provider: anthropic
  #   name: claude-sonnet-4-6

cases:
  files:
    - evals/cases/basic-success.yaml
    - evals/cases/edge-incomplete-input.yaml
    - evals/cases/edge-domain-boundary.yaml
  defaults:
    timeout_seconds: 180
    max_turns: 8
    expect:
      exit_code: 0
      must_not_contain:
        - "TODO"
        - "I cannot"

report:
  formats: [json]
"""


def case(case_id: str, title: str, description: str, prompt: str, must: list[str], judge: list[str]) -> dict:
    return {
        "case_id": case_id,
        "title": title,
        "description": description,
        "prompt": prompt,
        "must": must,
        "judge": judge,
    }


# ---- zh ----
CASES[("zh", "performance-testing")] = [
    case(
        "basic-success",
        "性能测试：按风险选测试类型与阈值",
        "有流量目标与关键交易时，应给出场景方案与退出标准。",
        """请使用 performance-testing。
系统：订单查询与下单。促销峰值约 800 RPS，目标 P95 < 500ms，错误率 < 0.1%。
已知风险：支付回调排队导致延迟。环境：SIT，有 APM。
请给出性能测试方案（基线/负载等按需选择），标明假设。""",
        ["场景", "阈值"],
        ["任务理解", "性能风险"],
    ),
    case(
        "edge-incomplete-input",
        "性能测试：无 SLA/流量仍给初版",
        "缺少基线数据时不能编造容量结论，必须标假设与缺口。",
        """用 performance-testing。产品只说「测一下性能」，没有 SLA、没有历史流量。
系统是积分兑换。请给初版方案，并把数字目标标成假设，列出缺口。""",
        ["假设", "缺口"],
        ["假设", "缺口"],
    ),
    case(
        "edge-domain-boundary",
        "性能测试：不要做成安全渗透清单",
        "用户混入安全诉求时，应坚持性能视角并澄清边界。",
        """使用 performance-testing。老板说：既要压测，也顺便扫一下 SQL 注入和弱口令。
窗口半天。请只给可执行的性能测试范围，并明确哪些属于安全测试、不应塞进本方案。""",
        ["性能", "安全"],
        ["场景", "范围"],
    ),
]

CASES[("zh", "performance-test-gatling")] = [
    case(
        "basic-success",
        "Gatling：贴合工具的场景与负载模型",
        "应给出 Gatling 场景、负载模型与阈值，而非通用空话。",
        """请使用 performance-test-gatling。
目标：促销期保护下单 POST /orders。期望 P95 < 400ms，错误率 < 0.1%。
当前峰值约 300 RPS，促销可能 1000 RPS。请给 Gatling 场景方案（不必长代码），标假设。""",
        ["Gatling", "阈值"],
        ["场景", "负载模型"],
    ),
    case(
        "edge-incomplete-input",
        "Gatling：无流量数据时写清假设",
        "缺少 feeder/流量数据时仍给初版并标缺口。",
        """用 performance-test-gatling。只有「要做 Gatling 压测」，没有 SLA、没有历史 RPS、没有现有工程。
链路：积分兑换。请给初版，数字目标标假设，并列出待确认问题。""",
        ["假设", "缺口"],
        ["假设", "Gatling"],
    ),
    case(
        "edge-domain-boundary",
        "Gatling：拒绝写成 k6 脚本方案",
        "用户要 k6 时，应说明本 skill 面向 Gatling，并给出 Gatling 等价结构。",
        """使用 performance-test-gatling。同事说「直接给我一份 k6 script，VU 和 thresholds 都写好」。
目标接口 GET /orders/{id}。请用 Gatling 视角给可落地场景与负载模型，并说明为何不按 k6 产出。""",
        ["Gatling", "k6"],
        ["负载模型", "阈值"],
    ),
]

CASES[("zh", "security-testing")] = [
    case(
        "basic-success",
        "安全测试：按资产与攻击面排优先级",
        "有认证与敏感数据流时，应给出高风险与优先检查项。",
        """请使用 security-testing。
系统：订单 API + 买家后台。认证：Bearer token（示例用 ${TOKEN} 占位）。
敏感数据：支付状态、收货地址。已知关注：越权读他人订单。
请给出安全测试方案，区分已确认风险与待验证项，勿给利用教程。""",
        ["鉴权", "风险"],
        ["任务理解", "优先检查"],
    ),
    case(
        "edge-incomplete-input",
        "安全测试：范围不清仍给初版",
        "无架构图时仍产出初版并列出缺口，不夸大覆盖。",
        """用 security-testing。产品说「积分兑换要做安全测试」，没有架构、没有鉴权说明、没有数据流。
请给可用初版，并明确信息缺口与假设。""",
        ["假设", "缺口"],
        ["假设", "缺口"],
    ),
    case(
        "edge-domain-boundary",
        "安全测试：不要做成性能测试",
        "用户要压测 RPS 时，应澄清安全边界并坚持安全检查项。",
        """使用 security-testing。需求写成：测一下支付回调能不能扛住 2000 RPS，顺便看看权限。
请以安全测试为主给出优先检查项，并说明纯负载/容量验证不属于本 skill 范围。""",
        ["安全", "权限"],
        ["优先检查", "范围"],
    ),
]

CASES[("zh", "accessibility-testing")] = [
    case(
        "basic-success",
        "无障碍：关键流程障碍与修复优先级",
        "应围绕键盘/读屏等给出检查项与优先级，而非标准科普。",
        """请使用 accessibility-testing。
页面：结算页（地址表单 + 支付按钮）。目标：键盘与读屏可用；参考 WCAG 思路但不做标准课。
平台：Web Chrome/Safari。请给出无障碍测试方案与修复优先级。""",
        ["键盘", "读屏"],
        ["任务理解", "修复优先级"],
    ),
    case(
        "edge-incomplete-input",
        "无障碍：无原型时仍列缺口与初版",
        "只有一句话时仍给初版检查方向并标信息缺口。",
        """用 accessibility-testing。只有一句：新活动页要过无障碍。没有设计稿、没有辅助技术范围。
请给初版检查清单，并列出必须补齐的信息。""",
        ["缺口", "假设"],
        ["信息缺口", "假设"],
    ),
    case(
        "edge-domain-boundary",
        "无障碍：不等于功能回归清单",
        "用户要功能用例时，应坚持无障碍视角并澄清边界。",
        """使用 accessibility-testing。测试同学把需求写成「把结算页所有功能点回归一遍，顺便看看无障碍」。
请只产出无障碍高风险检查与修复优先级，并说明哪些属于功能测试、不应混进本方案。""",
        ["无障碍", "功能"],
        ["键盘", "修复优先级"],
    ),
]

CASES[("zh", "mobile-testing")] = [
    case(
        "basic-success",
        "移动端：设备矩阵与高风险检查",
        "应给出设备矩阵、中断/网络等移动端特有风险。",
        """请使用 mobile-testing。
App：买家下单；平台 iOS/Android。已知风险：弱网下支付回调后状态不同步；deeplink 从推送打开偶发丢参。
请给移动端测试方案：设备矩阵、高风险检查与执行顺序。""",
        ["设备", "deeplink"],
        ["任务理解", "设备矩阵"],
    ),
    case(
        "edge-incomplete-input",
        "移动端：无设备清单仍给初版",
        "缺少机型/系统版本时标假设与缺口。",
        """用 mobile-testing。产品说「新版本要测手机端积分兑换」，没有机型列表、没有系统版本、没有权限说明。
请给初版，并列出必须确认的设备与环境信息。""",
        ["假设", "缺口"],
        ["假设", "设备"],
    ),
    case(
        "edge-domain-boundary",
        "移动端：不要只按桌面 Web 功能测",
        "用户按桌面清单测 App 时，应强调移动端特有风险。",
        """使用 mobile-testing。同事给了一份桌面 Web 功能用例，要求原样在 App 上跑一遍就交差。
请说明为何不够，并给出必须补的移动端高风险检查（网络中断、权限、推送/deeplink 等）。""",
        ["移动", "网络"],
        ["设备矩阵", "高风险"],
    ),
]

CASES[("zh", "manual-testing")] = [
    case(
        "basic-success",
        "手工测试：可执行清单与探索重点",
        "应给出优先级、执行清单与探索性重点。",
        """请使用 manual-testing。
范围：SIT 下单→支付→发货。已知风险：支付成功订单仍待支付（偶发）。
账号：buyer_sit_01（无真实密码）。请给手工测试优先级、执行清单与探索重点。""",
        ["手工", "探索"],
        ["任务理解", "执行清单"],
    ),
    case(
        "edge-incomplete-input",
        "手工测试：需求一句仍给清单草稿",
        "信息不足时给初版清单并标待确认。",
        """用 manual-testing。需求：支持积分兑换。没有用例、没有环境说明。
请先给可执行的手工清单草稿，并列出待确认问题。""",
        ["假设", "待确认"],
        ["假设", "缺口"],
    ),
    case(
        "edge-domain-boundary",
        "手工测试：不要改写成全面自动化方案",
        "用户要立刻全自动时，应坚持手工会话价值并划清边界。",
        """使用 manual-testing。经理说：别手工了，直接把所有检查写成自动化脚本一夜上线。
发版窗口半天，且支付偶发问题需要探索。请给本轮手工优先级与探索重点，并说明哪些暂不适合自动化。""",
        ["手工", "自动化"],
        ["探索", "优先级"],
    ),
]

CASES[("zh", "automation-testing")] = [
    case(
        "basic-success",
        "自动化：先自动化什么/暂不自动化",
        "应区分优先自动化与暂不自动化，并给方案与风险。",
        """请使用 automation-testing。
现状：有 Playwright，CI 可跑冒烟。候选：登录、搜索、下单、支付回调校验、后台报表导出。
目标：两周内稳定冒烟。请给出优先自动化范围、暂不自动化范围与防护建议。""",
        ["自动化", "暂不"],
        ["任务理解", "优先自动化"],
    ),
    case(
        "edge-incomplete-input",
        "自动化：无框架信息仍给初版",
        "缺少框架/CI 细节时标假设与缺口。",
        """用 automation-testing。只说「想把回归自动化」，不知道现有框架、语言、CI。
业务是积分兑换。请给初版建议，并列出必须确认的信息。""",
        ["假设", "缺口"],
        ["假设", "缺口"],
    ),
    case(
        "edge-domain-boundary",
        "自动化：禁止建议全部自动化",
        "探索性/不稳定路径应进入暂不自动化，而不是全覆盖口号。",
        """使用 automation-testing。干系人要求：登录到报表「全部场景 100% 自动化」，含偶发支付状态与探索性体验。
请明确优先自动化与暂不自动化，并解释为何不能全部自动化。""",
        ["暂不自动化", "风险"],
        ["优先自动化", "防护"],
    ),
]

CASES[("zh", "ai-assisted-testing")] = [
    case(
        "basic-success",
        "AI 辅助：分工与人工把关点",
        "应给出 AI/人工分工、高风险人工点与使用前检查。",
        """请使用 ai-assisted-testing。
任务：两天内完成积分兑换相关用例草稿 + 一轮探索清单；团队可用 AI 生成草稿。
请给出 AI 与人工分工、必须人工把关的高风险点、建议草稿产物与正式使用前检查项。""",
        ["人工", "复核"],
        ["任务理解", "高风险"],
    ),
    case(
        "edge-incomplete-input",
        "AI 辅助：目标不清仍给分工初版",
        "范围模糊时仍给初版分工并标限制与假设。",
        """用 ai-assisted-testing。同事说「用 AI 把测试都做了」，没有具体模块、没有质量门槛。
请给可用初版分工建议，并列出限制、假设与必须确认的信息。""",
        ["假设", "限制"],
        ["人工", "假设"],
    ),
    case(
        "edge-domain-boundary",
        "AI 辅助：AI 不能替代验证结论",
        "用户想让 AI 直接签发布时，应坚持人工把关边界。",
        """使用 ai-assisted-testing。负责人说：AI 生成用例并执行后，可以直接签发布，人工不用看。
请纠正边界：哪些可由 AI 起草，哪些必须人工把关，并给出正式使用前检查项。""",
        ["人工", "AI"],
        ["高风险", "检查"],
    ),
]

# ---- en ----
CASES[("en", "performance-testing")] = [
    case(
        "basic-success",
        "Performance testing: choose types and thresholds by risk",
        "With traffic targets and critical transactions, return scenarios and exit criteria.",
        """Use performance-testing.
System: order query and checkout. Promo peak ~800 RPS; target P95 < 500ms; error rate < 0.1%.
Known risk: payment-callback queueing adds latency. Env: SIT with APM.
Propose a performance plan (baseline/load as needed) and mark assumptions.""",
        ["scenario", "threshold"],
        ["Task Understanding", "Performance Risk"],
    ),
    case(
        "edge-incomplete-input",
        "Performance testing: draft without SLA/traffic",
        "Without baselines, do not invent capacity certainty; mark assumptions and gaps.",
        """Use performance-testing. Product only says 'please performance test' with no SLA or traffic history.
System: points redemption. Draft a plan; mark numeric targets as assumptions; list gaps.""",
        ["assumption", "gap"],
        ["assumption", "gap"],
    ),
    case(
        "edge-domain-boundary",
        "Performance testing: not a security penetration list",
        "When security asks are mixed in, stay performance-focused and clarify boundaries.",
        """Use performance-testing. Leadership wants load testing and also SQL injection / weak-password scans.
Half-day window. Deliver an executable performance scope and explicitly call out what belongs to security testing.""",
        ["performance", "security"],
        ["scenario", "scope"],
    ),
]

CASES[("en", "performance-test-gatling")] = [
    case(
        "basic-success",
        "Gatling: tool-fit scenarios and load model",
        "Return Gatling scenarios, load model, and thresholds—not generic fluff.",
        """Use performance-test-gatling.
Goal: protect checkout POST /orders in a promo. Target P95 < 400ms; error rate < 0.1%.
Peak ~300 RPS now, maybe 1000 RPS in promo. Propose a Gatling scenario plan (no long code) and mark assumptions.""",
        ["Gatling", "threshold"],
        ["Scenario", "Load Model"],
    ),
    case(
        "edge-incomplete-input",
        "Gatling: mark assumptions without traffic data",
        "Missing feeder/traffic data still yields a draft with gaps.",
        """Use performance-test-gatling. Only ask: 'do Gatling load testing'—no SLA, no historical RPS, no existing project.
Flow: points redemption. Draft a plan; mark numeric goals as assumptions; list open questions.""",
        ["assumption", "gap"],
        ["assumption", "Gatling"],
    ),
    case(
        "edge-domain-boundary",
        "Gatling: do not deliver a k6 script plan",
        "If the user asks for k6, stay Gatling-oriented and explain the mismatch.",
        """Use performance-test-gatling. A teammate asks for 'a ready k6 script with VUs and thresholds'.
Endpoint: GET /orders/{id}. Provide a Gatling-ready scenario and load model, and explain why this skill does not output k6.""",
        ["Gatling", "k6"],
        ["Load Model", "threshold"],
    ),
]

CASES[("en", "security-testing")] = [
    case(
        "basic-success",
        "Security testing: prioritize assets and attack surface",
        "With auth and sensitive flows, return top risks and priority checks.",
        """Use security-testing.
System: order API + buyer admin. Auth: Bearer token (use ${TOKEN} placeholder only).
Sensitive data: payment status, shipping address. Concern: IDOR reading others' orders.
Produce a security plan; separate confirmed risks vs needs-validation; no exploit how-to.""",
        ["auth", "risk"],
        ["Task Understanding", "Priority"],
    ),
    case(
        "edge-incomplete-input",
        "Security testing: draft when scope is thin",
        "Without architecture, still draft and list gaps; do not overclaim coverage.",
        """Use security-testing. Product says 'security-test points redemption' with no architecture, auth model, or data flow.
Give a usable draft and explicitly list gaps and assumptions.""",
        ["assumption", "gap"],
        ["assumption", "gap"],
    ),
    case(
        "edge-domain-boundary",
        "Security testing: not a performance load plan",
        "When the ask is RPS soak, clarify security boundaries and keep security checks.",
        """Use security-testing. The ask: see if payment callback survives 2000 RPS, and also check permissions.
Lead with security priority checks and state that pure load/capacity validation is out of this skill's scope.""",
        ["security", "permission"],
        ["Priority", "scope"],
    ),
]

CASES[("en", "accessibility-testing")] = [
    case(
        "basic-success",
        "Accessibility: barriers and fix priority on critical journeys",
        "Return keyboard/screen-reader focused checks and fix priority—not a WCAG lecture.",
        """Use accessibility-testing.
Page: checkout (address form + pay button). Goal: keyboard and screen-reader usable; WCAG-minded but practical.
Platform: Web Chrome/Safari. Produce an a11y plan with fix priority.""",
        ["keyboard", "screen reader"],
        ["Task Understanding", "Priority"],
    ),
    case(
        "edge-incomplete-input",
        "Accessibility: draft gaps without prototypes",
        "One-line asks still get a draft checklist plus information gaps.",
        """Use accessibility-testing. Only sentence: new campaign page needs accessibility. No designs, no AT scope.
Give a first-pass checklist and list must-have information.""",
        ["gap", "assumption"],
        ["Information Gaps", "assumption"],
    ),
    case(
        "edge-domain-boundary",
        "Accessibility: not a functional regression suite",
        "When asked for full functional cases, stay a11y-focused and clarify the boundary.",
        """Use accessibility-testing. A tester rewrote the ask as 'regress every checkout functional point, and glance at a11y'.
Deliver only high-risk accessibility checks and fix priority; call out what belongs to functional testing.""",
        ["accessibility", "functional"],
        ["keyboard", "Priority"],
    ),
]

CASES[("en", "mobile-testing")] = [
    case(
        "basic-success",
        "Mobile: device matrix and high-risk checks",
        "Return device matrix and mobile-specific risks (network, deeplink, etc.).",
        """Use mobile-testing.
App: buyer checkout on iOS/Android. Risks: weak-network payment status drift; push deeplink sometimes drops params.
Produce a mobile plan: device matrix, high-risk checks, execution order.""",
        ["device", "deeplink"],
        ["Task Understanding", "Device Matrix"],
    ),
    case(
        "edge-incomplete-input",
        "Mobile: draft without a device list",
        "Missing models/OS versions must be marked as assumptions/gaps.",
        """Use mobile-testing. Product says 'test points redemption on mobile' with no device list, OS versions, or permissions.
Draft a plan and list device/environment questions to confirm.""",
        ["assumption", "gap"],
        ["assumption", "device"],
    ),
    case(
        "edge-domain-boundary",
        "Mobile: not desktop-web cases copy-pasted",
        "If given a desktop suite, emphasize mobile-only risks that must be added.",
        """Use mobile-testing. A teammate hands a desktop web functional suite and says run it as-is on the app.
Explain why that is insufficient and list must-add mobile high-risk checks (network interrupt, permissions, push/deeplink).""",
        ["mobile", "network"],
        ["Device Matrix", "High-Risk"],
    ),
]

CASES[("en", "manual-testing")] = [
    case(
        "basic-success",
        "Manual testing: executable checklist and exploration",
        "Return priorities, session checklist, and exploratory focus.",
        """Use manual-testing.
Scope: SIT place-order → pay → ship. Risk: paid orders sometimes stay Pending Payment.
Account: buyer_sit_01 (no real password). Provide manual priorities, checklist, and exploratory focus.""",
        ["Manual", "Exploratory"],
        ["Task Understanding", "Checklist"],
    ),
    case(
        "edge-incomplete-input",
        "Manual testing: draft checklist from one line",
        "Thin requirements still get a draft checklist plus open questions.",
        """Use manual-testing. Requirement: support points redemption. No cases, no environment notes.
Provide a draft manual checklist and list open questions.""",
        ["assumption", "Open Question"],
        ["assumption", "gap"],
    ),
    case(
        "edge-domain-boundary",
        "Manual testing: not an overnight full-automation rewrite",
        "When asked to automate everything now, keep manual session value and boundaries.",
        """Use manual-testing. Manager says skip manual work and automate every check overnight.
Half-day release window; payment flake needs exploration. Give this round's manual priorities and exploratory focus, and what should not be automated yet.""",
        ["Manual", "automat"],
        ["Exploratory", "priority"],
    ),
]

CASES[("en", "automation-testing")] = [
    case(
        "basic-success",
        "Automation: what first vs not yet",
        "Separate automate-first vs not-yet; include approach and guardrails.",
        """Use automation-testing.
Current: Playwright; CI can run smoke. Candidates: login, search, checkout, payment-callback checks, admin report export.
Goal: stable smoke in two weeks. Return automate-first scope, not-yet scope, and guardrails.""",
        ["Automate First", "Not to Automate"],
        ["Task Understanding", "What to Automate"],
    ),
    case(
        "edge-incomplete-input",
        "Automation: draft without framework details",
        "Missing framework/CI details still yield a draft with gaps.",
        """Use automation-testing. Ask is only 'automate regression' with unknown framework, language, and CI.
Domain: points redemption. Draft recommendations and list must-confirm information.""",
        ["assumption", "gap"],
        ["assumption", "gap"],
    ),
    case(
        "edge-domain-boundary",
        "Automation: never recommend 100% automation",
        "Flaky/exploratory paths belong in not-yet—not a full-coverage slogan.",
        """Use automation-testing. Stakeholders demand 100% automation from login to reports, including flaky payment state and exploratory UX.
Explicitly separate automate-first vs not-yet and explain why full automation is wrong.""",
        ["Not to Automate", "risk"],
        ["What to Automate", "Guardrail"],
    ),
]

CASES[("en", "ai-assisted-testing")] = [
    case(
        "basic-success",
        "AI-assisted: split work and human gates",
        "Return AI/human split, high-risk human gates, and pre-use checks.",
        """Use ai-assisted-testing.
Task: in two days, draft points-redemption cases plus an exploration checklist; team may use AI drafts.
Provide AI vs human split, high-risk human gates, suggested draft artifacts, and checks before final use.""",
        ["human", "review"],
        ["Task Understanding", "High-Risk"],
    ),
    case(
        "edge-incomplete-input",
        "AI-assisted: draft split when goals are vague",
        "Vague scope still gets a draft split with limits and assumptions.",
        """Use ai-assisted-testing. Teammate says 'let AI do all the testing' with no module or quality bar.
Give a usable first split, and list limits, assumptions, and must-confirm items.""",
        ["assumption", "limit"],
        ["human", "assumption"],
    ),
    case(
        "edge-domain-boundary",
        "AI-assisted: AI cannot sign off release",
        "If AI is treated as a release authority, reinforce human-gate boundaries.",
        """Use ai-assisted-testing. Lead says: after AI generates and runs cases, ship without human review.
Correct the boundary: what AI may draft vs what humans must gate; include checks before final use.""",
        ["human", "AI"],
        ["High-Risk", "Check"],
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
        base = ROOT / "skills" / lang / "testing-types" / skill / "evals"
        cases_dir = base / "cases"
        if not cases_dir.exists():
            raise SystemExit(f"missing {cases_dir}")

        # drop scaffold third case if renamed
        old = cases_dir / "edge-risk-priority.yaml"
        if old.exists():
            old.unlink()

        for c in cases:
            path = cases_dir / f"{c['case_id']}.yaml"
            path.write_text(render(c, lang), encoding="utf-8")
            print(f"wrote {path.relative_to(ROOT)}")

        (base / "eval.yaml").write_text(EVAL_YAML, encoding="utf-8")
        print(f"updated { (base / 'eval.yaml').relative_to(ROOT) }")


if __name__ == "__main__":
    main()
