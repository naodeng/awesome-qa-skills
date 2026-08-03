#!/usr/bin/env python3
"""Write skill-specific skill-up cases for the pilot skill set."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (lang, skill) -> list of cases
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


# ---- zh ----
CASES[("zh", "functional-testing")] = [
    case(
        "basic-success",
        "功能测试：完整上下文产出可执行方案",
        "有业务流程与角色时，应输出带优先级的功能覆盖与场景。",
        """请使用 functional-testing 技能。
背景：电商「下单→支付→发货」即将发版。
环境：SIT；角色：买家、卖家运营、仓配。
已知风险：支付回调偶发超时。
请给出聚焦高风险路径的功能测试方案，并标明假设与信息缺口。""",
        ["优先级", "支付"],
        ["任务理解", "风险"],
    ),
    case(
        "edge-incomplete-input",
        "功能测试：信息不全仍给初版",
        "只有一句话需求时仍应给可用初版并列出缺口。",
        """用 functional-testing 帮我设计测试。
需求只有一句：新版本加了积分兑换。没有原型和接口文档。
请先给可用初版，并列出必须补齐的信息。""",
        ["假设", "缺口"],
        ["假设", "缺口"],
    ),
    case(
        "edge-risk-priority",
        "功能测试：发版窗口短必须砍范围",
        "功能很多但窗口很短时，必须突出 P0 并说明可降级项。",
        """使用 functional-testing。功能包含：登录、搜索、下单、支付、优惠券、积分、客服工单、后台报表。
发版窗口只有半天。请只保留最关键路径，并说明为什么其他项可降级。""",
        ["P0", "优先级"],
        ["P0", "降级"],
    ),
]

CASES[("zh", "api-testing")] = [
    case(
        "basic-success",
        "API 测试：按风险设计接口方案",
        "有核心接口与已知风险时，应给出优先级与鉴权/异常覆盖。",
        """请使用 api-testing。
系统：订单 REST API。关键接口：POST /orders、POST /payments/callback、GET /orders/{id}。
已知风险：支付回调重试与幂等。
环境：SIT。请给出可执行 API 测试方案，标出冒烟与发布阻塞项。""",
        ["优先级", "幂等"],
        ["任务理解", "风险"],
    ),
    case(
        "edge-incomplete-input",
        "API 测试：无 OpenAPI 时仍给初版",
        "缺少完整文档时仍应产出初版并列出缺口。",
        """用 api-testing。我只知道有一个「积分兑换」接口，路径和字段都不清楚。
请给可用初版方案，并列出必须补齐的信息。""",
        ["假设", "缺口"],
        ["假设", "缺口"],
    ),
    case(
        "edge-risk-priority",
        "API 测试：半天窗口只保核心链路",
        "接口很多时必须按业务风险排序，而不是平均覆盖。",
        """使用 api-testing。接口很多：登录、搜索、下单、支付回调、优惠券、积分、工单、报表导出。
发版窗口半天。请只保留 P0 API 检查，并说明其余如何降级。""",
        ["P0", "支付"],
        ["P0", "降级"],
    ),
]

CASES[("zh", "bug-reporting")] = [
    case(
        "basic-success",
        "缺陷报告：可复现的完整缺陷单",
        "有现象与环境时，应写出可复现步骤、实际/预期与优先级依据。",
        """请使用 bug-reporting 写缺陷报告。
现象：SIT 环境，买家用 Chrome 支付成功后订单仍显示「待支付」。
账号：buyer_sit_01。大约 3 次里出现 1 次。
请写出可复现缺陷报告，事实与猜测分开，并给出严重程度依据。""",
        ["复现", "预期"],
        ["实际", "严重"],
    ),
    case(
        "edge-incomplete-input",
        "缺陷报告：证据不全时标明不确定性",
        "信息不完整时仍应结构化描述，并标明待确认项。",
        """用 bug-reporting。用户只说：积分兑换有时候会失败。没有截图、日志、环境。
请先写一版缺陷报告草稿，并明确列出待确认信息。""",
        ["待确认", "复现"],
        ["待确认", "假设"],
    ),
    case(
        "edge-risk-priority",
        "缺陷报告：严重程度必须有业务依据",
        "避免情绪化定级；严重程度/优先级要写清影响。",
        """使用 bug-reporting。
问题：后台报表导出比平时慢约 20 秒，业务仍能导出成功。
同时另有：支付成功但扣款翻倍（偶发）。
请分别给出两份简版缺陷摘要，并解释严重程度为何不同。""",
        ["严重", "支付"],
        ["优先级", "影响"],
    ),
]

CASES[("zh", "performance-test-k6")] = [
    case(
        "basic-success",
        "k6：按目标选择场景而非全做",
        "应给出贴合 k6 的场景、阈值与假设。",
        """请使用 performance-test-k6。
目标：订单查询 GET /orders/{id} 在促销期保活。
期望：P95 < 300ms，错误率 < 0.1%。当前峰值约 200 RPS，促销可能到 800 RPS。
请给出 k6 场景方案（不必输出完整脚本），并标明假设。""",
        ["k6", "P95"],
        ["场景", "假设"],
    ),
    case(
        "edge-incomplete-input",
        "k6：无流量数据时写清假设",
        "缺少基线数据时不能编造精确容量结论。",
        """用 performance-test-k6。产品说「要测一下性能」，没有 SLA、没有历史流量。
系统是积分兑换接口。请给初版方案，并把所有数字目标标成假设。""",
        ["假设", "缺口"],
        ["假设", "k6"],
    ),
    case(
        "edge-risk-priority",
        "k6：窗口短时只做关键负载",
        "不要默认基线+负载+压力+尖峰+稳定性全做。",
        """使用 performance-test-k6。半天内要给出发版建议。
链路：浏览、搜索、下单、支付回调、报表导出。
请只选最关键的 1-2 个 k6 场景，并说明为什么其他可延后。""",
        ["场景", "延后"],
        ["支付", "优先级"],
    ),
]

CASES[("zh", "test-case-writing")] = [
    case(
        "basic-success",
        "用例编写：高风险路径优先",
        "应输出具体用例并带优先级，而不是空泛清单。",
        """请使用 test-case-writing。
需求：下单后可用积分抵扣；积分不足时不能提交；支付回调失败要可重试。
请编写聚焦高风险的测试用例，并标明优先级与待确认项。""",
        ["优先级", "积分"],
        ["用例", "风险"],
    ),
    case(
        "edge-incomplete-input",
        "用例编写：需求一句时仍给草稿",
        "信息不足时给草稿用例并列出缺口。",
        """用 test-case-writing。需求：支持积分兑换。无验收标准。
请先给用例草稿，并列出必须向产品确认的问题。""",
        ["假设", "确认"],
        ["缺口", "用例"],
    ),
    case(
        "edge-risk-priority",
        "用例编写：时间不够时砍非关键用例",
        "用例很多时必须标 P0 与可延后。",
        """使用 test-case-writing。模块：登录、搜索、下单、支付、优惠券、积分、工单、报表。
只有半天测试时间。请只保留 P0 用例清单，并说明其余如何降级。""",
        ["P0", "优先级"],
        ["P0", "降级"],
    ),
]

# ---- en ----
CASES[("en", "functional-testing")] = [
    case(
        "basic-success",
        "Functional testing: executable plan with context",
        "With flows and roles, return prioritized functional coverage.",
        """Use the functional-testing skill.
Context: ecommerce place-order → pay → ship release.
Env: SIT; roles: buyer, seller ops, warehouse.
Known risk: payment callback timeouts.
Produce a risk-focused functional test plan and mark assumptions/gaps.""",
        ["priority", "payment"],
        ["Task Understanding", "Risk"],
    ),
    case(
        "edge-incomplete-input",
        "Functional testing: draft despite missing docs",
        "One-line requirements should still yield a draft with gaps.",
        """Use functional-testing.
Requirement: new release adds points redemption. No prototype or API docs.
Give a usable first draft and list must-have information.""",
        ["assumption", "gap"],
        ["assumption", "gap"],
    ),
    case(
        "edge-risk-priority",
        "Functional testing: cut scope for a short window",
        "Many features + short window => P0 focus and deferrals.",
        """Use functional-testing. Features: login, search, checkout, payment, coupons, points, tickets, admin reports.
Half-day release window. Keep only critical paths and explain what can be deferred.""",
        ["P0", "priority"],
        ["P0", "defer"],
    ),
]

CASES[("en", "api-testing")] = [
    case(
        "basic-success",
        "API testing: risk-ranked interface plan",
        "With key endpoints and known risks, cover auth/errors/priority.",
        """Use api-testing.
System: order REST API. Endpoints: POST /orders, POST /payments/callback, GET /orders/{id}.
Risk: callback retries and idempotency. Env: SIT.
Produce an executable API plan with smoke and release blockers.""",
        ["priority", "idempotency"],
        ["Task Understanding", "Risk"],
    ),
    case(
        "edge-incomplete-input",
        "API testing: draft without OpenAPI",
        "Missing docs should still yield a draft and gaps.",
        """Use api-testing. I only know there is a points-redemption API; path and fields unknown.
Give a usable draft plan and list missing information.""",
        ["assumption", "gap"],
        ["assumption", "gap"],
    ),
    case(
        "edge-risk-priority",
        "API testing: half-day window keeps core chain",
        "Many endpoints must be ranked by business risk.",
        """Use api-testing. Endpoints span login, search, checkout, payment callback, coupons, points, tickets, report export.
Half-day window. Keep only P0 API checks and explain deferrals.""",
        ["P0", "payment"],
        ["P0", "defer"],
    ),
]

CASES[("en", "bug-reporting")] = [
    case(
        "basic-success",
        "Bug reporting: reproducible defect report",
        "With symptoms and env, write steps, actual/expected, severity rationale.",
        """Use bug-reporting.
Symptom: on SIT, Chrome buyer pays successfully but order stays Pending Payment.
Account: buyer_sit_01. Happens about 1 of 3 times.
Write a reproducible bug report; separate facts from guesses; justify severity.""",
        ["Steps", "Expected"],
        ["Actual", "Severity"],
    ),
    case(
        "edge-incomplete-input",
        "Bug reporting: mark uncertainty when evidence is thin",
        "Incomplete info still gets a structured draft with open questions.",
        """Use bug-reporting. User says: points redemption sometimes fails. No screenshot, logs, or environment.
Write a draft bug report and explicitly list what must be confirmed.""",
        ["confirm", "Steps"],
        ["confirm", "assumption"],
    ),
    case(
        "edge-risk-priority",
        "Bug reporting: severity needs business impact",
        "Severity/priority must be justified, not emotional.",
        """Use bug-reporting.
Issue A: admin report export is ~20s slower but still succeeds.
Issue B: payment succeeds but double-charges (intermittent).
Give two short bug summaries and explain why severity differs.""",
        ["severity", "payment"],
        ["priority", "impact"],
    ),
]

CASES[("en", "performance-test-k6")] = [
    case(
        "basic-success",
        "k6: choose scenarios intentionally",
        "Return k6-fit scenarios, thresholds, and assumptions.",
        """Use performance-test-k6.
Goal: keep GET /orders/{id} healthy in a promo.
Target: P95 < 300ms, error rate < 0.1%. Peak ~200 RPS now, maybe 800 RPS in promo.
Propose k6 scenarios (full scripts not required) and mark assumptions.""",
        ["k6", "P95"],
        ["scenario", "assumption"],
    ),
    case(
        "edge-incomplete-input",
        "k6: mark numeric goals as assumptions",
        "Without baselines, do not invent capacity certainty.",
        """Use performance-test-k6. Product says 'please performance test' with no SLA or traffic history.
System: points redemption API. Draft a plan and mark every numeric target as an assumption.""",
        ["assumption", "gap"],
        ["assumption", "k6"],
    ),
    case(
        "edge-risk-priority",
        "k6: short window keeps critical load only",
        "Do not default to baseline+load+stress+spike+soak.",
        """Use performance-test-k6. Need a release recommendation within half a day.
Flows: browse, search, checkout, payment callback, report export.
Pick only the most critical 1-2 k6 scenarios and explain what can wait.""",
        ["scenario", "defer"],
        ["payment", "priority"],
    ),
]

CASES[("en", "test-case-writing")] = [
    case(
        "basic-success",
        "Test case writing: prioritize high-risk paths",
        "Return concrete cases with priority, not vague lists.",
        """Use test-case-writing.
Requirement: orders can use points; cannot submit if points insufficient; payment callback failure must be retryable.
Write risk-focused test cases with priorities and open questions.""",
        ["priority", "points"],
        ["Priority", "risk"],
    ),
    case(
        "edge-incomplete-input",
        "Test case writing: draft from one-line requirement",
        "Thin requirements still get draft cases plus confirmation questions.",
        """Use test-case-writing. Requirement: support points redemption. No acceptance criteria.
Provide draft cases and list questions for product.""",
        ["assumption", "confirm"],
        ["gap", "Priority"],
    ),
    case(
        "edge-risk-priority",
        "Test case writing: cut non-critical cases",
        "Mark P0 vs deferrable when time is short.",
        """Use test-case-writing. Modules: login, search, checkout, payment, coupons, points, tickets, reports.
Only half a day to test. Keep a P0 case list and explain deferrals.""",
        ["P0", "priority"],
        ["P0", "defer"],
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
