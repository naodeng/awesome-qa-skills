# QA Skills 项目评审报告

**评审日期**：2026-08-07
**项目**：awesome-qa-skills
**范围**：仓库结构、skill 双语对齐、eval 覆盖、质量脚本、文档治理

---

## 当前状态

- 当前仓库包含 76 个 skill 目录：中文 38 个、英文 38 个。
- 单语技能包含 34 个测试类型与 4 个测试工作流。
- `skills/zh` 与 `skills/en` 的 skill 目录名保持成对一致。
- 每个 skill 均配置 `evals/eval.yaml` 与 `evals/cases/*.yaml`。
- 本地质量门禁 `bash scripts/check_skills_quality.sh` 当前可通过。

## 已完成优化

1. 核心 8 个测试类型 skill 的 eval 断言已增强：
   - `functional-testing`
   - `api-testing`
   - `automation-testing`
   - `manual-testing`
   - `performance-testing`
   - `security-testing`
   - `mobile-testing`
   - `accessibility-testing`

2. 完整性校验规则已与项目文档对齐：
   - `SKILL.md`、`prompts/`、`agents/openai.yaml`、`evals/` 继续作为必需项。
   - `scripts/`、`output-templates/` 作为支持目录，不再被当作所有 skill 的硬性必需项。
   - 已新增回归测试覆盖该规则。

3. 旧版 2026-02-10 评审报告已归档到：
   - `docs/archive/SKILLS_REVIEW_REPORT-2026-02-10.md`

## 后续建议

### P1：把质量门禁搬到 CI

当前 `.github` 目录没有质量 workflow，本地 pre-commit 需要开发者主动安装。建议新增 GitHub Actions，至少运行：

```bash
bash scripts/check_skills_quality.sh
pytest tests/test_validate_skills_integrity.py -q
```

### P1：让 skill-up eval 校验在 CI 中强制执行

当前 `skill-up` 不在 PATH 时，`scripts/validate_skill_evals.sh` 会提示跳过并返回成功。建议增加 CI 模式：

```bash
REQUIRE_SKILL_UP=1 bash scripts/validate_skill_evals.sh
```

当 `REQUIRE_SKILL_UP=1` 且 `skill-up` 缺失时应返回失败。

### P2：继续提升 eval 质量

核心 8 个 skill 已增强关键词断言。下一步建议把同样方法推广到工具专项 skill，并补充更接近真实产物质量的规则，例如：

- 是否区分确认事实、假设与信息缺口。
- 是否避免编造接口、字段、环境和根因。
- 是否给出优先级、范围边界和可交付物。
- 是否覆盖边界、异常、安全、性能、兼容性等关键测试维度。

### P2：治理生成物漂移

`installers/` 下存在大量由脚本生成的安装器文件。建议在 CI 中加入生成物漂移检查：

```bash
bash scripts/generate-install-shortcuts.sh
git diff --exit-code installers/
```

这样可以避免手工修改生成文件后忘记同步生成脚本。
