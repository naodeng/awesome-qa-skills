# Skill-up 驱动的 Skills 优化实施计划

> **For agentic workers:** 按 Task 并行执行；每完成一批跑 `bash scripts/check_skills_quality.sh`。步骤用 checkbox 跟踪。

**Goal:** 按 [alibaba/skill-up](https://github.com/alibaba/skill-up) 与 Agent Skills 最佳实践，让本仓库全部 QA skill 具备可触发、可执行、可评测、可演进的质量闭环。

**Architecture:** 保持现有 `SKILL.md`（激活入口）+ `prompts/`（完整规范）结构；为每个 skill 补齐 `evals/`；分批把偏模板的 prompt 深化为领域可执行规范；用仓库校验脚本守门，skill-up CLI 作可选运行时评测。

**Tech Stack:** Markdown skills、skill-up YAML evals、Python 脚手架脚本、`scripts/check_skills_quality.sh`

---

## 现状（基线）

| 项 | 状态 |
| --- | --- |
| SKILL.md 入口优化 | ✅ 58 个已升级（流程/约束/按需加载/自检） |
| description 触发词 | ✅ 弱描述已规范化 |
| 试点 evals | ✅ 5 skill × zh/en = 10 套（含定制用例） |
| 其余 evals | ❌ 约 24 zh + 对应 en 缺失 |
| prompts 深度 | ⚠️ 多数 ~57 行模板；`api-testing` 等较好 |
| skill-up 实跑 | ⏳ 本机未装 CLI / 无强制 CI |

## 目标结构

```text
skills/{zh|en}/.../<skill>/
  SKILL.md          # 瘦入口（已优化）
  prompts/*.md      # 完整执行规范（本阶段深化）
  evals/
    eval.yaml
    cases/{basic,edge-*}.yaml
  agents/openai.yaml
  references/ examples/ scripts/  # 按需
```

## 分阶段方案

### Phase A — 评测覆盖（skill-up 骨架）【并行】

为所有缺失 `evals/` 的 skill 脚手架 + **按领域定制断言**（禁止长期停留在通用电商模板）。

分组：

- **A1** 工具链 API：`api-test-bruno|pytest|restassure|supertest`（zh+en）
- **A2** 性能/安全/无障碍：`performance-testing|performance-test-gatling|security-testing|accessibility-testing|mobile-testing|manual-testing|automation-testing|ai-assisted-testing`
- **A3** 分析/策略/用例族：`requirements-analysis(-plus)|test-strategy(-plus)|test-case-reviewer(-plus)|testcase-writer-plus|test-reporting`
- **A4** 工作流：`discover-testing|daily|sprint|release-testing-workflow`

每组要求：

1. `python3 scripts/scaffold_skill_evals.py --skill <path>`（或批量后覆盖 cases）
2. 每个 skill **至少 3 个 case**：成功路径 / 信息不完整 / 领域边界或近邻误用
3. `rule_based` 关键字必须来自该 skill 的 prompt 输出结构或领域词
4. 中英双语同步；中文 skill 用中文 prompt/断言，英文 skill 用英文
5. 骨架完成后对该批 skill 重跑 `optimize_skills_skillup.py --skill ...` 以写入「按需加载 → evals」

### Phase B — Prompt 深化（抗模板）【并行，与 A 分文件不冲突时可并行】

优先加深「用户高频 + 当前过薄」的 prompt（zh 与 en 同步）：

| 优先级 | Skill | 深化重点 |
| --- | --- | --- |
| P0 | `api-test-bruno/pytest/restassure/supertest` | 输入解析顺序、默认框架约定、产物目录、脱敏、不可编造字段 |
| P0 | `performance-test-k6` / `gatling` | 场景选择决策树、阈值写法、无 SLA 时假设模板 |
| P0 | `testcase-writer-plus` / `test-case-reviewer-plus` | 追踪矩阵、评审严重级别、与基础版差异 |
| P1 | `requirements-analysis-plus` / `test-strategy-plus` | 多格式输入处理、结构化结论字段 |
| P1 | 工作流 4 个 | 阶段门禁、进出标准、与类型 skill 的交接 |
| P2 | 其余类型 skill | 补 gotchas + 1 个迷你示例输入输出 |

深化原则（agentskills）：

- 只写 Agent 不知道就会错的内容；删空话
- Prefer defaults，不摆工具菜单
- 解释 why；交付前自检与最低覆盖清单保留
- 禁止真实 token/密钥；curl 示例脱敏

### Phase C — 质量门禁与文档

- [x] `bash scripts/check_skills_quality.sh` 全绿（A/B 全部完成后复跑）
- [x] `SKILL_AUTHORING.md` 已含 skill-up / skill-upper 演进约定
- [ ] （可选）根目录注明：未安装 skill-up 时至少 `validate` 配置可由贡献者本地补跑

### Phase D — 演进闭环（人工/有 API Key 时）

- 安装 skill-up + engine，对 P0 skill `skill-up run`
- 失败归类：Skill 缺陷 vs eval 过严/过松
- 修 prompt / 补 regression case；不削弱有效断言

---

## Task 拆分（给并行 Agent）

### Task A1: API 工具 skill evals 定制 — ✅

**Files:** `skills/{zh,en}/testing-types/api-test-{bruno,pytest,restassure,supertest}/evals/**`

- [x] Scaffold 缺失 evals
- [x] 定制 3 cases/skill（生成集合/脚本、缺文档、错误格式输入）
- [x] 中英同步
- [x] 对该批重跑 optimize 入口（仅这些 skill）

### Task A2: 性能/安全/探索类 evals 定制 — ✅

**Files:** 对应 testing-types 下无 evals 的非 API-tool、非 plus/分析族 skill

- [x] 同上脚手架 + 领域断言
- [x] 中英同步

### Task A3: 分析/策略/用例/报告 evals 定制 — ✅

**Files:** requirements/strategy/reviewer/writer-plus/reporting

- [x] 同上；plus 与基础版 case 要能区分增强点

### Task A4: 工作流 evals 定制 — ✅

**Files:** `skills/{zh,en}/testing-workflows/*/evals/**`

- [x] discover 侧重路由正确性；daily/sprint/release 侧重阶段产出与门禁

### Task B1: 深化 API 工具 prompts（zh+en） — ✅

**Files:** `**/api-test-*/prompts/*.md`（及必要时 `references/` 交叉引用说明）

- [x] 按 Phase B P0 深化；保持独立安装；不链到其他 skill 内部文件

### Task B2: 深化 plus / 策略 / 工作流 prompts（zh+en） — ✅

**Files:** plus skills + workflows prompts

- [x] 写出与基础版的明确差异；工作流写出交接与 DoD

### Task C: 质量门禁 — ✅

- [x] 全量 `check_skills_quality.sh`
- [x] 修复 independence / metadata / integrity 问题
- [x] 汇总变更清单与残留风险

---

## 验收标准

1. 每个 skill 目录存在合法 `evals/eval.yaml` + ≥3 cases  
2. 弱 description 仍为 `Use this skill when...; triggers include...`  
3. `SKILL.md` 含按需加载与交付前自检；有 evals 的会提到 `evals/`  
4. P0 prompts 不再是「换标题的 57 行空壳」（有默认工具约定、gotchas、具体输出字段）  
5. `check_skills_quality.sh` 通过  
6. 未引入密钥；未破坏 skill 独立安装规则  

## 不在本计划范围

- 强制接入 GitHub Action 跑 skill-up（需密钥与 runner 镜像，另开 PR）
- 重写 `resources/` 或安装器大改
- 把 prompts 合并进 SKILL.md 导致失去 `prompts/` 校验约定
