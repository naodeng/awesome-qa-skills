# 变更到回归工作流

提供 Diff、Commit SHA、业务路径和回归清单后调用 `change-to-regression`，形成有依据的回归选择。

## 示例

> 比较当前分支和 `main`，为支付重试改动选择必测/可延后检查，说明风险和未覆盖路径；不要运行测试。

## 最佳实践

提供精确 base/head SHA、完整 Diff、测试耗时和环境限制；实际运行后附时间、Commit 和运行记录。

## FAQ

- 没有 Diff 时可列所需材料，精确影响保持 `UNKNOWN`。
- 不默认执行回归；计划不能写成通过结果。
- Commit 更新后旧 Checkpoint 标 `STALE`，重审相关范围。
