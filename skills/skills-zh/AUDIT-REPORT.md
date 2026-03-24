# skills-zh 深度审计报告

- 审计日期：2026-03-24
- 审计范围：`skills/skills-zh`（映射 `skills/testing-types`、`skills/testing-workflows` 的中文技能）
- 审计方式：结构审计 + 链接完整性审计 + 元数据校验

## 结论

- 总体状态：通过（可用）
- 关键阻断问题：0
- 已修复问题：3 类（链接断裂、目录分区缺失、示例目录缺失）

## 本轮修复

1. 新增中文分区目录  
- 新增 `skills/skills-zh/`，按中文技能建立语言分区视图（符号链接方式）。

2. 修复中文相关坏链  
- 修复中文技能提示词与工作流提示词中跨目录引用错误。
- 修复部分文档中 FAQ/贡献文档相对路径错误。

3. 补齐最小可用占位资源  
- 新增缺失的 `examples/` 占位目录与 `README.md`，避免快速开始文档指向空路径。
- 新增缺失参考文件（如 `references/troubleshooting.md`、`output-formats.md`）。

## 验证结果

- 链接完整性（排除 `node_modules`）：`broken = 0`
- 元数据校验（`agents/openai.yaml`）：`findings = 0`
- 语言分区结构：已生效（`skills-zh/testing-types/*`、`skills-zh/testing-workflows/*`）
- 独立性检查：`external = 0`（未发现跨 skill 外部依赖）

## 剩余建议

1. 示例项目中的 `node_modules` 不建议入库，可在后续清理并加入忽略规则。
2. 建议建立统一脚本，定期执行坏链扫描与路径回归校验。

## 本轮落实（修复与完善）

1. 已将跨目录文档依赖本地化到各 skill 内部（`references/_external/`）。
2. 已移除示例中的 `node_modules`，避免把外部依赖包带入 skill。
3. 新增自动检查脚本：
- `scripts/validate_skills_independence.py`
- 可一键检查：坏链数量、跨 skill 外部引用数量。
