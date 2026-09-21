<div align="right"><strong>🇨🇳 中文</strong> | <a href="./SKILL_EVALUATION_PILOTS_EN.md">🇬🇧 English</a></div>

# Skill Evaluation 双 Pilot

本记录把设计中的 analysis Pilot 与 executable Pilot 绑定到已有 Skill，不创建新的全局用例仓库。

## Analysis Pilot

- Skill：`requirements-analysis`
- 关注：触发、需求缺口、风险相关性、假设控制和 `agent_judge` rubric。
- 现有配置：`skills/{zh,en}/testing-types/requirements-analysis/evals/eval.yaml`。
- 最低覆盖：成功、信息不足、风险优先级；邻近边界通过 `testability-analysis` 等相邻 Skill 另行记录。
- Judge 配置：`edge-semantic-agent-judge` 使用 `agent_judge`，其余基础用例保留 `rule_based`。
- 当前证据：结构和 `skill-up validate` 可执行；真实模型 replay、judge calibration 和 semantic effectiveness 为 `NOT_RUN`。

## Executable Pilot

- Skill：`ui-test-playwright`
- 关注：测试工件结构、脚本可执行性、JavaScript 语法、测试声明发现和 `script` judge；浏览器/runtime smoke 仍属于独立层。
- 现有配置：`skills/{zh,en}/testing-types/ui-test-playwright/evals/eval.yaml`，启用 benchmark 配置。
- Judge 配置：`basic-script-artifact` 使用 `script` judge 提取 JavaScript 代码块，验证语法并检查 Playwright 测试、导航和断言声明。
- 当前证据：配置、工件提取、语法和声明检查可验证；没有授权目标应用和真实模型运行时，浏览器/runtime 执行与 benchmark 结果为 `NOT_RUN`。

## Router Composition Pilot（v1.5.2）

- Skill：`discover-testing`
- 关注：`new-feature-quality`、`api-delivery`、`change-regression`、`performance-decision` 和 `ai-feature-validation` 的 route intent、主/辅唯一性、信息不足、负向控制与交接可执行性。
- Eval cases：双语配置各包含 `route-new-feature-quality`、`route-api-delivery`、`route-change-regression`、`route-performance-decision`、`route-ai-feature`；配置与 `skill-up validate` 可验证。
- 选择证据：case 的 `expected_selection` 声明 expected route/primary/optional；observed 选择必须由带有 `route`、`primary`、`optional`、`selected_skills` 的 `skill.selection` trace 或明确的 trace adapter 输出支持。`selected_skills` 严格限制为唯一主 Skill 加至多一个辅助 Skill；缺字段为 `BLOCKED`，不匹配或多选为 `FAIL`，不能按 negative control 或 `PASS` 解释。
- 当前证据：Manifest、生成视图、双语 case、唯一性和离线 trace 合同可静态/结构化验证；真实模型选择、跨模型一致性、目标执行、业务路由效果和 Quality Score 均为 `NOT_RUN` / `NOT_SCORED`。
- 边界：Composition Recipe 是导航元数据，不是自动调用链；本 Pilot 不新增第二套 Engine、Judge、Benchmark 或 Quality Score。

## 统一执行命令

```bash
skill-up validate skills/zh/testing-types/requirements-analysis/evals/eval.yaml
skill-up validate skills/en/testing-types/requirements-analysis/evals/eval.yaml
skill-up validate skills/zh/testing-types/ui-test-playwright/evals/eval.yaml
skill-up validate skills/en/testing-types/ui-test-playwright/evals/eval.yaml
skill-up validate skills/zh/testing-workflows/discover-testing/evals/eval.yaml
skill-up validate skills/en/testing-workflows/discover-testing/evals/eval.yaml
```

需要运行时证据时，必须记录 run metadata、trace、judge 类型、目标、限制和失败分类；不能用 `skill-up validate` 替代真实执行。
