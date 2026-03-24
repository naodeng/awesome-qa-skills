# Explore Skills 深度审计报告（中文）

- 审计日期：2026-03-24
- 审计范围：`explore/skills-zh`、`explore/skills-en`
- 审计方式：结构审计 + 一致性审计 + 可运行性验证 + 元数据规范审计

## 结论

- 总体状态：通过（可用）
- 关键阻断问题：0
- 已修复问题：3 类（文档规范、一致性、元数据规范）
- 环境相关风险：2 项（k6 外网目标不可达、Gatling CLI 缺失）

## 发现与修复

### 1. 元数据格式不统一（高）

问题：同一目录下 `agents/openai.yaml` 存在两种格式，可能影响技能展示和触发稳定性。

修复：统一 20 个 `openai.yaml` 为同一结构：
- `version`
- `metadata.key`
- `metadata.last_verified`
- `interface.display_name`
- `interface.short_description`
- `interface.default_prompt`
- `policy.allow_implicit_invocation`

### 2. 技能文档缺少可追溯验证信息（中）

问题：`SKILL.md` 缺少最近验证时间和文档版本，后续维护不可追踪。

修复：
- 中文 skills 增加 `审计信息` 段落
- 英文 skills 增加 `Review Metadata` 段落
- 全部写入 `2026-03-24` 与版本 `1.1.0`

### 3. 中英文目录总说明不一致（中）

问题：英文总说明曾保留旧同步脚本描述，不符合“独立可用”目标。

修复：重写 `skills-en/README.md` 与 `skills-en/SKILLS.md`，与中文目录保持同类结构。

## 验证结果

### A. 非性能技能实跑验证（16/16 通过）

通过项：
- 需求分析（中/英）
- 用例编写（中/英）
- 策略生成（中/英）
- 用例评审（中/英）
- API 解析与生成（Supertest/Bruno/Pytest/RestAssured，中/英）

### B. 性能技能验证

- k6（中/英）：命令可启动，因目标不可达导致阈值失败（环境问题，不是脚本结构问题）
- Gatling（中/英）：明确提示本机缺少 Gatling CLI（错误信息清晰）

## 剩余风险与建议

1. 性能脚本默认目标依赖外部可访问环境，建议增加本地 mock 基线模式。
2. Gatling 建议在 README 增加“一键安装或最小运行前检查”段落，降低新手门槛。

## 本次更新文件类型

- 更新：中英文 `SKILL.md`（20个）
- 更新：中英文 `agents/openai.yaml`（20个）
- 更新：中英文目录总说明（4个）
- 新增：本审计报告（2个）

## 2026-03-24 补充复审（本轮）

### 新发现与修复

1. 提示词跨目录引用失效（高）
- 问题：`explore` 中 18 个提示词保留了原始相对链接，点击后找不到目标文件。
- 修复：统一改为指向 `skills/testing-types/.../prompts/...` 的真实路径。
- 结果：本地 Markdown 链接检查结果 `broken 0`。

2. 性能报告目录混入历史运行产物（中）
- 问题：`performance-test-k6/reports` 中有历史 `smoke-*.json`，导致中英文目录不完全同步。
- 修复：删除历史产物并新增 `reports/.gitignore`（k6/gatling，中英各一份）避免再次混入。
- 结果：中英文目录文件集合再次一致。

3. 复审后验证时间未同步（低）
- 修复：所有 `SKILL.md` 与 `agents/openai.yaml` 的验证日期统一更新到 `2026-03-24`。
