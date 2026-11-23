# discover-testing 路由参考

> 此文件由 `scripts/generate_skill_composition_views.py` 生成。它是 Router Skill 的本地、自包含参考，不依赖仓库外部文件，也不把组合关系变成安装依赖。

## 使用边界

- 先根据用户目标选择一条最匹配的路线。
- 每条路线只给一个主 Skill，可选 Skill 最多一个；不要输出菜单式候选列表。
- 信息不足时保留假设和证据缺口；本参考不证明模型、运行时或业务效果。

## Routes

### 新功能质量准备 (`new-feature-quality`)

- 触发意图: 从新需求和验收目标开始建立可测试的质量准备
- 适用阶段: 需求分析 / 测试设计
- 主 Skill: `requirements-analysis`
- 可选 Skill: `test-strategy`
- 交接: 交接已确认的风险、验收条件和测试范围，供后续测试设计使用
- 不适用:
  - 不替代具体测试类型或测试工具的执行
  - 不在输入不足时捏造验收标准

### API 交付 (`api-delivery`)

- 触发意图: 为 API 变更或新接口选择契约与行为验证的起点
- 适用阶段: API 设计 / 实现 / 验证
- 主 Skill: `api-testing`
- 可选 Skill: `api-contract-testing`
- 交接: 交接接口清单、输入输出约束、异常路径和待验证的契约风险
- 不适用:
  - 不替代具体 API 客户端或测试框架的执行
  - 不把契约检查结果当作完整业务验收

### 变更与回归 (`change-regression`)

- 触发意图: 从代码或需求变更识别影响面并收敛回归范围
- 适用阶段: 变更分析 / 回归规划
- 主 Skill: `change-impact-analysis`
- 可选 Skill: `regression-test-selection`
- 交接: 交接受影响组件、风险优先级、回归候选和未覆盖证据
- 不适用:
  - 不声称已经执行回归测试
  - 不在没有变更证据时给出精确影响结论

### 性能决策 (`performance-decision`)

- 触发意图: 把性能目标和工作负载转化为可解释的验证与分析路径
- 适用阶段: 性能建模 / 结果分析
- 主 Skill: `performance-workload-modeling`
- 可选 Skill: `performance-result-analysis`
- 交接: 交接负载假设、指标定义、环境前提和结果分析问题
- 不适用:
  - 不替代压测工具或目标环境的实际运行
  - 不把静态工作负载模型当作运行结果

### AI 功能验证 (`ai-feature-validation`)

- 触发意图: 为 AI 功能区分功能行为、模型输出和风险边界的验证入口
- 适用阶段: AI 功能设计 / 评测规划
- 主 Skill: `ai-feature-testing`
- 可选 Skill: `llm-testing`
- 交接: 交接功能目标、输入输出样本、风险维度、评测数据和未运行项
- 不适用:
  - 不在没有模型、数据和目标环境时声称模型效果
  - 不把提示词建议当作业务验收或安全结论

### PR 质量审查 (`pr-quality-review`)

- 触发意图: 审查 Pull Request 代码变更、测试影响、测试有效性并汇总质量证据
- 适用阶段: 代码审查 / 测试影响 / 质量门禁
- 主 Skill: `pr-quality-review`
- 可选 Skill: 无
- 交接: 交接 PR ID、base/head SHA、Diff、验收标准、可用测试证据和权限范围
- 不适用:
  - 只需单项代码审查时不要强行进入完整工作流
  - 不能代替授权者评论或批准合并

### 需求到测试设计 (`requirement-to-test`)

- 触发意图: 用户明确要求从需求分析走到测试策略、用例与追踪矩阵
- 适用阶段: 需求质量 / 可测试性 / 测试设计
- 主 Skill: `requirement-to-test`
- 可选 Skill: 无
- 交接: 交接需求 ID/原文、验收标准、业务约束、已确认风险和测试执行边界
- 不适用:
  - 只需澄清单条需求时优先单步需求分析
  - 不替业务方补写未确认规则

### 变更到回归计划 (`change-to-regression`)

- 触发意图: 用户明确要求从代码变更完成影响分析、回归选择和风险汇总
- 适用阶段: 变更影响 / 回归规划
- 主 Skill: `change-to-regression`
- 可选 Skill: 无
- 交接: 交接 Diff、base/head SHA、模块/业务路径、测试清单、时间与环境限制
- 不适用:
  - 只需识别受影响模块时使用单步变更影响分析
  - 不声称回归已执行

### 缺陷修复验证 (`bugfix-verification`)

- 触发意图: 从缺陷、复现步骤、基线与修复版本出发，建立复现、修复验证和回归证据
- 适用阶段: 缺陷复现 / 修复验证 / 回归
- 主 Skill: `root-cause-analysis`
- 可选 Skill: `regression-test-selection`
- 交接: 交接缺陷 ID、复现输入、基线与目标 SHA、修复 diff、回归候选、执行状态和证据路径
- 不适用:
  - 不在无基线证据时声称已复现
  - 不把测试通过单独当作缺陷已修，也不替代发布批准

### AI 评测门禁 (`ai-eval-gate`)

- 触发意图: 为 AI 功能、Prompt 或模型变更定义评测门禁、样本量与放行证据
- 适用阶段: 评测设计 / 发布门禁
- 主 Skill: `quality-gate-design`
- 可选 Skill: `llm-evaluation-design`
- 交接: 交接评测目标、数据集及版本、judge、阈值、样本量、回归基线和未运行项
- 不适用:
  - 不设计数据集与 judge 的细节；这部分交给 llm-evaluation-design
  - 不代替发布批准

### AI 生成代码验证 (`ai-code-verification`)

- 触发意图: 评审 Agent 编写或修改的生产代码，核对意图、变更范围、依赖、测试和 CI 证据
- 适用阶段: 实现评审 / 变更验证
- 主 Skill: `ai-generated-code-review`
- 可选 Skill: 无
- 交接: 交接目标/验收条件、base/head SHA、生成来源、完整 diff、依赖与测试/CI 原始结果、未验证项
- 不适用:
  - 不代替完整 PR 质量流程
  - 不因测试通过就认定实现正确或代码已执行验证

### AI 特性发布闭环 (`ai-feature-release`)

- 触发意图: 从 AI 评测资产与门禁连接到灰度/影子、线上质量观察和回滚准备
- 适用阶段: 评测 / 发布门禁 / 线上观察
- 主 Skill: `ai-feature-release-workflow`
- 可选 Skill: 无
- 交接: 交接模型/Prompt/数据集/judge/run 版本、门槛与样本、灰度 cohort、监控 Owner、停止/回滚条件和待批准决定
- 不适用:
  - 不代替评测引擎、CI Runner 或生产监控系统
  - 不执行发布、流量切换、风险接受或人工批准

## 选择后的交接

输出路由理由、关键假设、证据缺口和下一步交接输入；组合建议是导航信息，不是强制执行链。
