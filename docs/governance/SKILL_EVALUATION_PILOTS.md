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

## 统一执行命令

```bash
skill-up validate skills/zh/testing-types/requirements-analysis/evals/eval.yaml
skill-up validate skills/en/testing-types/requirements-analysis/evals/eval.yaml
skill-up validate skills/zh/testing-types/ui-test-playwright/evals/eval.yaml
skill-up validate skills/en/testing-types/ui-test-playwright/evals/eval.yaml
```

需要运行时证据时，必须记录 run metadata、trace、judge 类型、目标、限制和失败分类；不能用 `skill-up validate` 替代真实执行。
