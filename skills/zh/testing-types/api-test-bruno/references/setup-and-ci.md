# 安装与 CI 指南（中文）

## 本地执行
1. 安装依赖
2. 运行一键脚本 scripts/run.sh
3. 查看结果与报告

## CI 建议
- PR：执行 smoke 子集
- 主干或夜间：执行全量
- 对 P0 失败设置阻断

## 模板
- 参考 examples/ci 目录下 GitHub Actions 与 Jenkins 模板
