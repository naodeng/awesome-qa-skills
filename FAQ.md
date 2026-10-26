<div align="right"><strong>🇨🇳 中文</strong> | <a href="./FAQ_EN.md">🇬🇧 English</a></div>

# 常见问题

## 项目与 Skill

### 1. 这个项目包含什么？

这是面向 AI 编码 Agent 的双语 QA Agent Skills 库。每种语言有 165 个 Skill：10 个测试工作流、150 个测试类型和 5 个 Skill Engineering；中英文合计 330 个 Skill 目录。查看[完整索引](docs/catalog/skills-index.md)。

### 2. 支持哪些 AI 工具？

查看 README 的[支持工具和安装方式](README.md#支持的-ai-工具)。具体能力取决于工具的 Skill 发现方式；项目不会把未验证的工具版本标成已测试。

### 3. 如何找到适合的 Skill？

先按任务查看 [README 的 Skill 导航](README.md#按任务查找-skill)，或使用 `discover-testing` 路由 Skill；全部名称和用途见[技能索引](docs/catalog/skills-index.md)。

### 4. 中文和英文 Skill 有什么区别？

中英文使用相同的 canonical name，分别位于 `skills/zh/` 和 `skills/en/`。内容按语言维护；在同一个工具目标中通常只安装一种语言，避免同名目录冲突。

## 安装与使用

### 5. 如何安装一个 Skill？

使用 Agent Skills CLI 时，英文 Skill 可从仓库入口安装；中文 Skill 要显式指定 `skills/zh`：

```bash
npx skills add naodeng/awesome-qa-skills --skill functional-testing
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/zh --skill functional-testing
```

更多 CLI、macOS/Linux、Windows、快捷脚本和手动复制方式见[安装手册](scripts/INSTALL_SKILLS.md)。

### 6. 如何使用已安装的 Skill？

支持 Agent Skills 自动发现的工具可以直接接收自然语言任务。有些工具还支持显式调用语法，例如 `@skill functional-testing`；语法因工具而异。安装与调用范围见[支持工具说明](README.md#支持的-ai-工具)。

### 7. 多个 Skill 会自动串联吗？

不会自动编排。你可以按需逐个使用 Skill；[Composition 路由目录](docs/catalog/skills-composition.md)提供任务路线和主辅 Skill 建议，用于导航和选择。

### 8. Skill 会自动运行测试或保证代码可执行吗？

不会。Skill 可帮助设计测试或起草脚本；是否执行、能否运行以及结果是否通过，取决于所用 Agent、工具和目标项目。运行前应检查代码与目标环境，并按实际执行结果记录证据。

### 9. 可以要求输出 Excel、CSV 或其他格式吗？

Markdown 是默认格式。是否支持 Excel、CSV、JSON 等格式取决于具体 Skill；请查看该 Skill 目录里的 `output-formats.md`，或在请求中说明需要的格式。

### 10. 安装或加载失败怎么办？

检查语言来源、目标工具的 Skills 路径、Skill 目录中的 `SKILL.md`，以及是否装了同名的另一种语言版本。CLI 安装中文 Skill 时请指定 `skills/zh`。完整排查步骤见[安装手册](scripts/INSTALL_SKILLS.md)。

### 11. 社区推荐的第三方 Skill 属于本项目吗？

不属于。README 的[社区推荐列表](README.md#社区推荐的外部-skills)用于发现外部项目维护的 Skill；许可证、版本、依赖和兼容性以各自上游为准，列入列表不代表本仓库已做运行时评测。

## 贡献与许可

### 12. 如何新增或修改 Skill？

先阅读[贡献指南](CONTRIBUTING.md)和[Skill 编写指南](skills/SKILL_AUTHORING.md)。新增或修改 Skill 时需要维护中英文目录、元数据和 Eval 用例，并运行项目质量检查。

### 13. 如何报告问题或请求新 Skill？

先搜索[现有 Issues](https://github.com/naodeng/awesome-qa-skills/issues)；如果没有相同问题，再提交 Issue 并附上复现步骤、使用场景和期望结果。

### 14. 项目采用什么许可证？

本仓库采用 [PolyForm Noncommercial License 1.0.0](LICENSE)，仅允许非商业用途。第三方推荐 Skill 使用其上游各自的许可证。

---

**最后更新：2026-10-26**
