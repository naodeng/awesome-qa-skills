# 领域判定示例

以下为脱敏合成 fixture，用于核对来源、决策和成本计算；不是项目执行或业务验收记录。

## 输入与预期

同一批 10 个结账用例的人工基线为 60 分钟。AI 辅助流程耗时：生成 10 分钟、复核 25 分钟、返工 35 分钟、验收 10 分钟。合计 80 分钟。输入已脱敏；D1 的断言经 QA R1 复核并采纳为 V2，执行 run R7 的原始证据显示 10/10 通过；复核还发现一项断言假绿并完成返工。D2 未经复核，不得标记采纳。没有 token 计数或计费记录。

| ID | DECISION | 依据 |
| --- | --- | --- |
| AIA-01 | ACCEPTED | D1 经 R1 复核，版本 V2 与 run R7 可追溯；10/10 只代表此 fixture 的执行结果 |
| AIA-02 | DRAFT | 缺少人工复核与采纳版本 |
| AIA-03 | UNSUPPORTED | 生成耗时 10 分钟不能代表总成本，token 费用无来源 |

## 成本复算

| METRIC | VALUE | 依据 |
| --- | --- | --- |
| human_baseline_minutes | 60 | 同一范围与复杂度的人工基线 |
| generate_minutes | 10 | 计时记录 |
| review_minutes | 25 | 计时记录 |
| rework_minutes | 35 | 计时记录 |
| acceptance_minutes | 10 | 计时记录 |
| total_minutes | 80 | 10 + 25 + 35 + 10 |
| token_cost | UNSUPPORTED | 无 token 计数或费用来源 |
| defects_found | 1 | 复核发现的一项断言假绿 |
| rework_count | 1 | 一次返工记录 |
| false_green_count | 1 | 原断言未验证目标行为 |

`total_minutes=80` 大于人工基线 `60`；本例不支持“AI 已提效”的结论。fixture 中的 ID、版本、时长和通过数不得外推到真实项目。
