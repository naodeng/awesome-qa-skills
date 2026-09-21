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

## 选择后的交接

输出路由理由、关键假设、证据缺口和下一步交接输入；组合建议是导航信息，不是强制执行链。
