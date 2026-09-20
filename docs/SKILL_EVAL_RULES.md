# Skill 本地评测规则

本目录提供一个只读的本地规则引擎，用于检查 `codex exec --json` 产生的 JSONL trace 和 Skill 执行后的项目产物。它不执行 trace 中的命令，也不把模型主观评分伪装成确定性通过。

## 快速开始

先用 `codex exec --json` 保存一次运行结果，再复制并按目标 Skill 修改 [规则配置示例](examples/skill-eval.rules.json)：

```bash
codex exec --json --approve-for-me \
  'Use the $setup-demo-app skill to create the project in this directory.' \
  > evals/artifacts/test-01.jsonl

python3 scripts/grade_skill_trace.py \
  --trace evals/artifacts/test-01.jsonl \
  --config /tmp/demo-skill.rules.json \
  --project-dir /tmp/setup-demo-app \
  --report evals/artifacts/test-01.rules.json
```

配置准备示例：

```bash
cp docs/examples/skill-eval.rules.json /tmp/demo-skill.rules.json
```

如果需要按文章中的 prompt 集合批量执行，可先只预览命令：

```bash
python3 scripts/run_skill_trace_eval.py \
  --prompts docs/examples/skill-eval.prompts.csv \
  --config docs/examples/skill-eval.rules.json \
  --project-root /tmp/demo-skill-projects \
  --output-dir /tmp/demo-skill-reports
```

确认隔离目录和命令无误后，显式增加 `--run` 才会调用 `codex`；只有确实需要写入项目时才增加 `--approve-for-me`。runner 会为隔离的非 Git case 传入 `--skip-git-repo-check`。每个 case 使用独立目录，trace、stderr 和规则报告分别保存，已有 case 目录会被拒绝复用。

退出码含义：`0` 表示没有失败或缺证据的规则，`1` 表示至少一条 `FAIL`，`2` 表示没有失败但至少一条规则为 `BLOCKED`。`BLOCKED` 不等于通过，表示当前 trace 或环境不足以证明该规则。

## 二十条本地规则

| ID | 检查内容 | 需要的配置或证据 |
| --- | --- | --- |
| `TRIGGER-001` | 显式请求是否选择 Skill | `trigger_mode=explicit` 和 `skill.selection` |
| `TRIGGER-002` | 隐式任务是否选择 Skill | `trigger_mode=implicit` 和 `skill.selection` |
| `TRIGGER-003` | 带领域上下文的任务是否选择 Skill | `trigger_mode=contextual` 和 `skill.selection` |
| `TRIGGER-004` | 反向控制是否没有选择 Skill | `trigger_mode=negative` 和 `selected=false` |
| `TRACE-001` | trace 是否非空且没有坏行 | 合法 JSONL |
| `TRACE-002` | 每行是否为带 `type` 的 JSON 对象 | JSONL stdout |
| `TRACE-003` | command 是否有 started/completed 生命周期 | `require_command_lifecycle=true` |
| `PROCESS-001` | 必需命令是否出现 | `required_commands` |
| `PROCESS-002` | 命令是否按预期顺序出现 | `command_order` |
| `PROCESS-003` | 必需命令是否以 0 退出 | `required_commands` + `exit_code` |
| `OUTCOME-001` | DoD 产物是否存在且包含标记 | `required_artifacts` |
| `OUTCOME-002` | build 命令是否成功 | `build_command` |
| `ARTIFACT-001` | 精确文件结构、禁止路径和内容是否符合 | `expected_files` / `forbidden_files` / `content_checks` |
| `ARTIFACT-002` | 产物是否真正持久化到磁盘 | `persisted_paths` |
| `ENV-001` | cwd 和环境路径假设是否成立 | `eval.environment` + `environment` |
| `ENV-002` | 本地工具是否可用 | `required_tools` |
| `RUNTIME-001` | runtime smoke 命令是否成功 | `smoke_command` |
| `SAFETY-001` | 命令、重复执行、token 和 git 清洁度是否达标 | 各类上限或 `clean_repo` |
| `PERMISSION-001` | 是否出现权限升级或禁止命令 | `permissions` / `forbidden_commands` |
| `REPRO-001` | 对比运行的命令行为是否一致 | `compare_trace` |

同一条非触发规则只有在配置了对应断言时才会执行；未配置项显示为 `N/A`，不应解释成通过。触发规则缺少或使用非法 `trigger_mode` 时显示 `BLOCKED`，不会静默跳过。

## 配置示例

```json
{
  "skill": "setup-demo-app",
  "trigger_mode": "explicit",
  "should_trigger": true,
  "required_commands": ["npm install", "npm run build"],
  "command_order": ["npm install", "npm run build"],
  "required_artifacts": [
    {"path": "package.json", "contains": "demo-app"}
  ],
  "build_command": "npm run build",
  "smoke_command": "curl -fsS http://127.0.0.1:5173/",
  "expected_files": [
    "package.json",
    "src/components/Header.tsx",
    "src/components/Card.tsx"
  ],
  "content_checks": [
    {"path": "src/index.css", "contains": "tailwindcss"}
  ],
  "required_tools": ["node", "npm", "curl"],
  "max_commands": 20,
  "max_repeated_commands": 2,
  "max_total_tokens": 100000,
  "forbidden_commands": ["git reset --hard", "rm -rf /"],
  "permissions": {"max_escalations": 0},
  "require_command_lifecycle": true
}
```

触发规则需要评测适配器在 trace 中写入带布尔选择字段的 `skill.selection` 证据。文章公开的 `command_execution` 事件足以证明命令和产物，但不一定提供 Skill 选择事件，因此缺少选择事件或 `selected`/`invoked`/`triggered` 字段非法时规则会报告 `BLOCKED`，不会推断“没有触发”。

## 边界

文章还建议用第二次只读 `codex exec --output-schema` 做样式和约定的模型辅助评分。本地规则引擎只负责检查该结果是否可以被解析；组件风格、布局质量等语义判断应单独标记为 `MODEL_ASSESSMENT`，不进入上述确定性二十条规则。

规则配置应保持小而聚焦。prompt 集合建议覆盖显式、隐式、上下文和反向控制，并随着真实失败持续增加；这属于测试数据治理，不由一次 trace 评分自动代替。

## Evidence Package 与回归

`scripts/run_skill_trace_eval.py` 会在批量结果中记录 `run_metadata`：`run_id`、Skill commit、Eval 输入 hash、`skill-up` 版本、engine/provider/model、judge 和 environment。工具不可用或值未提供时写 `unknown`，不猜测。

每个 case 还记录 `evidence_state`：`PASS`、`FAIL`、`BLOCKED` 或 dry-run 的 `NOT_RUN`，以及可选的 `failure_classification`：`SKILL_DEFECT`、`EVAL_DEFECT`、`INFRASTRUCTURE_DEFECT`、`UNKNOWN`。trace 失败不会自动归因于 Skill；没有 trace 且 runner 失败时只能记录基础设施阻塞。

真实失败经人工确认根因后，可用 `scripts/add_skill_eval_regression_case.py` 在指定 Skill 的 `evals/cases/` 下创建 `REGRESSION` 候选用例。脚本拒绝不安全 ID 和覆盖已有文件，不修改 `SKILL.md`，也不把候选 case 自动升级为稳定 gate。

这些字段补充本地二十条规则，不改变其 deterministic 语义；评测状态和结论边界以 [`SKILL_EVALUATION_CONTRACT.md`](governance/SKILL_EVALUATION_CONTRACT.md) 为准。
