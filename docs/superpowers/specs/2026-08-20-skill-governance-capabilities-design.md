# Skill Governance Capabilities Design

## Goal

吸收 `deepseek-harness/.agents/skills` 中与当前仓库最匹配的治理思想，新增三组可独立安装的双语 QA Skill：文案契约审查、变更验证选择、过程性内容清理。

## Scope

### Included

1. `skill-prose-review`
   - 审查 SKILL.md、Prompt、元数据、示例、输出格式和文档中的契约完整性。
   - 检查触发条件、输入、输出、约束、拒绝条件、证据要求和交付检查。
   - 识别重复、装饰性背景、实现叙述和无法验证的承诺。

2. `skill-change-verification`
   - 根据变更范围选择最小但足够的验证集合。
   - 明确区分静态完整性、结构/独立性检查、Evals、运行时 Skill 执行和人工审阅。
   - 输出变更范围、验证命令、结果、未覆盖风险和证据等级。

3. `skill-prose-trim`
   - 清理“本次修改”“审查者认为”“之前版本”“设计阶段编号”等过程性残留。
   - 保留当前状态、真实约束、反事实风险和可解析的外部引用。
   - 不删除有价值的契约、负向保证、测量结果或正式决策依据。

### Excluded

- VitePress/站点投影同步。
- GitHub stacked PR 合并流程。
- 浏览器 GIF 录制。
- Agent Notes 的归档数据模型。
- 自动修改既有 Skill 内容；本轮只新增能力并验证其可用性。

## Repository fit

每项 Skill 在 `skills/zh/skill-engineering/` 与 `skills/en/skill-engineering/` 下建立同名目录，至少包含。它们属于 Skill 工程与治理能力，不属于 QA 测试类型或测试工作流；`.agents/skills/` 仅作为后续可选的本仓库 Agent 运行时投影目录，不作为正式源目录：

- `SKILL.md`
- `prompts/<skill-name>.md`
- `agents/openai.yaml`
- `evals/eval.yaml`
- `evals/cases/` 下的成功路径、信息不完整、范围/风险边界用例

Skill 不引用其他 Skill 的内部文件，不依赖当前仓库路径或运行时数据库；三项能力都可以在复制单个目录后独立使用。

## Shared output contract

三个 Skill 默认输出 Markdown，并使用以下证据分类：

| Evidence level | Meaning |
| --- | --- |
| Static | 文件、frontmatter、目录和格式检查 |
| Structural | 双语配对、独立性、索引和 Evals 结构检查 |
| Evaluation | `skill-up validate` 或等价评测结果 |
| Runtime | 实际执行 Skill/Prompt 后得到的行为证据 |
| Human review | 对语义、术语、风险和可用性的人工判断 |

任何未执行的验证必须标记为未验证，不能用较低等级证据替代较高等级结论。

## Component design

### skill-prose-review

输入是一个 Skill、Prompt 或相关文档目录，以及审查目标。流程先识别文档角色，再建立“触发条件 → 输入 → 执行规则 → 输出 → 约束 → 验证”的契约链，最后按阻塞问题、重要建议、低优先级建议输出结果。缺少上下文时不得臆测代码行为，应列出缺失信息并降低结论等级。

### skill-change-verification

输入是变更文件列表、变更类型和可用工具。流程先按内容、元数据、目录、脚本、Evals 和运行时影响分类，再选择最小验证集合。输出必须包含已运行命令和原始结果摘要、未运行项目及原因、残余风险，以及“可以声称什么/不能声称什么”。

### skill-prose-trim

输入是明确限定的文案范围。流程先逐段识别事实、契约、历史、推理过程和审查对话，再只删除或改写无法在当前仓库语境中解析的内容。对双语文件必须保持语义同步；对记录型 fixture、归档历史和正式变更记录默认只审查不改写，除非用户明确扩大范围。

## Evaluation design

每个语言版本至少覆盖：

1. 成功路径：输入完整且能产出结构化结果。
2. 信息不完整：缺少目标、输入或验证环境时明确列出缺口，不虚构结论。
3. 范围/风险边界：遇到跨 Skill 依赖、敏感信息、历史归档或运行时证据缺失时拒绝越权或降低证据等级。

Evals 只验证可观察输出契约；静态 `skill-up validate` 不代表已经验证运行时语义，运行时验证需单独报告。

## Quality gates

实现后运行：

```bash
bash scripts/check_skills_quality.sh
git diff --check
rg -n 'TBD|TODO|<[^>]+>' skills/zh/skill-engineering skills/en/skill-engineering
```

新增 Skill 的 Evals 运行结果单独记录；如果没有执行 `skill-up run`，交付报告必须明确说明“未验证运行时语义”。

## Risks and decisions

- 三项 Skill 可能与既有 `code-review`、`test-report-review` 或文档类 Skill 重叠；实现前需搜索其边界，避免复制完整内容，只保留治理层能力。
- `skill-prose-trim` 不能成为无差别文案重写器；必须以当前状态可验证性和契约完整性为判断标准。
- `skill-change-verification` 不能承诺自动知道所有项目命令；命令不可发现时必须输出待确认项，而不是猜测。
- 本轮不修改索引和安装器，除非质量门禁证明新增 Skill 必须登记；对外入口同步作为后续独立任务。
