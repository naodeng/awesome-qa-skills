---
name: requirement-consistency-analysis
description: Use this skill when multiple requirement artifacts may disagree on terminology, identifiers, formats, states, rules, or behavior; triggers include 需求一致性分析, requirement consistency, and cross-document consistency.
---

# 需求一致性分析

比较用户提供的多份需求、契约、设计或规则材料，判断术语、标识、格式、状态、规则和行为描述是否在同一适用范围内一致。它保留来源和版本边界，不静默合并互斥约束。

## 何时使用

- PRD、用户故事、API 契约、原型、技术说明或验收标准使用了不同名称或状态。
- 需要核对多份材料是否对同一角色、字段、流程和结果给出一致描述。
- 同一流程在不同版本、时间或平台的规则可能不同，需要先区分适用范围。

不适用于只有一个来源且只需要通用需求分析的任务，也不用于替业务裁决显式冲突。

## 工作方式

1. 阅读并遵循 `prompts/requirement-consistency-analysis.md`。
2. 建立来源、版本、时间、角色、平台和适用范围清单；没有比较对象时标明限制。
3. 用稳定比较键对照术语、标识、格式、状态、规则和行为；逐项保留证据和关系。
4. 将关系区分为 `aligned`、`inconsistent` 和 `conflict`，将证据状态区分为 `assessed`、`missing`、`stale` 和 `unassessed`；不静默合并互斥规则。
5. 当任务要求 `business-rule` 模式时，使用稳定规则键和 `BR-##` 规则级证据比较主体、触发、适用范围、优先级/覆盖关系、动作、结果和例外；保留通用 `RC-##` 发现。
6. 给出影响、优先级、责任角色、待确认问题、关闭条件和验证方式。

## 核心约束

- 使用 `RC-##` 标识发现；每行至少有 source pair、comparison key、关系、状态、evidence、scope/version、impact 和 action。关系只能使用 `aligned`、`inconsistent` 或 `conflict`；状态只能使用 `assessed`、`missing`、`stale` 或 `unassessed`。
- `business-rule` 模式额外使用 `BR-##` 记录规则级证据、主体/对象、触发、适用范围、优先级/覆盖关系、动作、结果和例外；不把“更严格”自动当作更高优先级。
- 不把相似名称直接当成同义，不把缺少第二来源当成一致。
- 不跨版本或不同适用范围判定同一事实；范围不明时保留 `stale`/`unassessed`。
- 显式互斥规则建议使用 `requirement-conflict-detection`，只写 Skill 名称，不链接内部文件。
- 不补造状态迁移、字段含义、平台支持或最终规范。

## 按需加载

- 每次产出前必须阅读 `prompts/requirement-consistency-analysis.md`。
- 需要回归本 Skill 时使用 `evals/eval.yaml` 和 `evals/cases/`；结构门禁不证明跨来源语义正确。
- 需要验证发现行为时，使用 `evals/trigger-prompts.csv` 与 `evals/local-rules.json` 运行仓库的 `scripts/run_skill_trace_eval.py`；缺少 `skill.selection` 证据时必须报告 `BLOCKED`，不能推断触发成功。
- 以上是仓库根目录下的开发验证步骤；独立安装的 Skill 包不包含仓库级 runner，运行时不依赖该脚本。
- 需要验证 `business-rule` 模式时，使用 `business-rule-*` Eval 和带业务规则短语的本地触发样本；目录仍是本 Skill 的物理目录，不创建别名目录。

## 交付前自检

- [ ] 每个比较结论都列出来源、版本/范围和最小证据
- [ ] 已分别区分关系 `aligned`、`inconsistent`、`conflict` 与状态 `assessed`、`missing`、`stale`、`unassessed`
- [ ] 明确冲突没有被静默合并或被错误降级为普通不一致
- [ ] P0/P1 问题有责任角色、待决策问题和验证方式
- [ ] 没有把名称匹配、文档存在或静态表格写成运行结果

## 常见误区

- 看到两个术语相近就直接判定为同一个对象。
- 忽略文档版本、发布日期、平台或租户范围。
- 用一份材料的缺省内容填补另一份材料。
- 把冲突双方改写成一个未经批准的折中规则。
