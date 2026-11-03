<div align="right"><strong>🇨🇳 中文</strong> | <a href="./WORKFLOW_STATE_RUNTIME_EN.md">🇬🇧 English</a></div>

# 本地 Workflow Run State CLI

`scripts/workflow_run_state.py` 为工作流契约提供一个可选的、本地 JSON 状态账本。它保存 Run ID、Workflow 包指纹、输入指纹、Commit SHA、阶段状态、证据引用、Checkpoint 和幂等键。它不调用 Agent、不调度 Skill，也不执行任何写入或发布操作。

## 建立状态与输入指纹

`fingerprint` 对指定文件或目录中的内容和 Commit SHA 计算稳定摘要。`create` 另外记录 workflow package 指纹，所以本地 Workflow/Prompt 改动也会使旧 Run 失效。

```bash
COMMIT_SHA="$(git rev-parse HEAD)"
python3 scripts/workflow_run_state.py fingerprint \
  --base-dir . \
  --input skills/en/testing-workflows/pr-quality-review \
  --input path/to/review-input.md \
  --commit-sha "$COMMIT_SHA"

python3 scripts/workflow_run_state.py create \
  --workflow-file skills/en/testing-workflows/pr-quality-review/workflow.yaml \
  --state-dir /tmp/qa-workflow-state \
  --input-fingerprint <上一步输出的 SHA-256> \
  --commit-sha "$COMMIT_SHA"
```

Run 状态文件是新建的独立 JSON 文件；状态目录应位于 Skill 包之外。创建同一个 Run ID 两次会失败。

## 阶段与 Checkpoint

`start-stage` 重新核对输入指纹、Commit SHA 和 Workflow 包。依赖阶段未完成时不能启动；同一 Run 中已启动或已结束的阶段不能再次启动。阶段完成需附至少一个证据引用；失败、阻塞和跳过都需要显式记录。

```bash
python3 scripts/workflow_run_state.py start-stage \
  --state-file /tmp/qa-workflow-state/pr-quality-review/<run-id>.json \
  --workflow-file skills/en/testing-workflows/pr-quality-review/workflow.yaml \
  --stage-id scope \
  --expected-input-fingerprint <SHA-256> \
  --expected-commit-sha "$COMMIT_SHA"

python3 scripts/workflow_run_state.py complete-stage \
  --state-file /tmp/qa-workflow-state/pr-quality-review/<run-id>.json \
  --stage-id scope \
  --evidence-ref evidence/scope-review.json \
  --checkpoint-ref checkpoints/scope.json
```

## 恢复与权限

```bash
python3 scripts/workflow_run_state.py resume \
  --state-file /tmp/qa-workflow-state/pr-quality-review/<run-id>.json \
  --workflow-file skills/en/testing-workflows/pr-quality-review/workflow.yaml \
  --expected-input-fingerprint <当前 SHA-256> \
  --expected-commit-sha "$(git rev-parse HEAD)"
```

- 任一指纹或 Commit SHA 改变时，Run 与未完成阶段变为 `STALE`。
- 进程中断时仍处于 `RUNNING` 的阶段会变为 `BLOCKED`，要求检查是否已经产生副作用；CLI 不会自动重放。
- `resume` 只报告检查点是否仍匹配及可开始的未执行阶段，不会调用 Skill 或重试阶段。
- `permission: write` 或 `approval_required: true` 的阶段必须显式传入 `--confirm --approved-by <标识>`。这会在状态中记录时间、范围和操作者填写的标识。
- `--approved-by` 是审计文本，不是已验证身份。外部写入、删除、发布和正式放行仍必须由 Agent Host 通过可信的人类确认实施；本地 CLI 本身不是安全授权边界。

详细字段约束见 [Workflow Contract](./WORKFLOW_CONTRACT.md) 和 [Run State Schema](../../resources/workflows/schemas/run-state.schema.json)。本工具是 Python 标准库脚本，无需新增 Skill 安装依赖。

## 验证

```bash
python3 -m unittest scripts.tests.test_workflow_run_state -v
python3 scripts/validate_workflow_contracts.py --repo-root .
```
