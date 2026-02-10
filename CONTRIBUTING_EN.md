# Contributing Guide

[中文](CONTRIBUTING.md) | [English](#english)

---

## English

Thank you for your interest in contributing to AI Testing Assistant Skills! We welcome all forms of contributions.

### How to Contribute

#### 1. Report Issues

If you find a bug or have suggestions:

1. Search [Issues](https://github.com/naodeng/awesome-qa-skills/issues) first
2. Create a new Issue
3. Provide detailed description, reproduction steps, and environment info

#### 2. Feature Requests

If you have ideas for new Skills:

1. Search existing Feature Requests
2. Create a new Issue with `enhancement` label
3. Describe the Skill requirements, use cases, and expected behavior

#### 3. Contribute New Skills

##### 3.1 Skill Directory Structure

```
skills/testing-types/your-skill/
├── SKILL.md              # Skill metadata and description
├── quick-start.md        # Quick start guide
├── output-formats.md     # Output format documentation
├── prompts/              # Prompts directory
│   ├── basic.md          # Basic level prompts
│   ├── intermediate.md   # Intermediate level prompts
│   └── advanced.md       # Advanced level prompts
└── reference.md          # Reference documentation (optional)
```

##### 3.2 SKILL.md Metadata Standards

```yaml
---
name: your-skill-name
version: 1.0.0
last-updated: 2024-02-06
description: Brief description (one sentence)
category: testing-types | testing-workflows
level: beginner | intermediate | advanced
tags: [tag1, tag2, tag3]
dependencies: []
recommended-with: [skill1, skill2]
output-formats: [markdown, excel, csv, json]
---
```

##### 3.3 Commit Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>
```

**Types**:
- `feat`: New Skill or feature
- `fix`: Bug fix
- `docs`: Documentation update
- `refactor`: Refactoring

**Example**:
```
feat(functional-testing): add boundary value testing prompts

- Add boundary value analysis section
- Update quick-start.md
- Optimize output formats

Closes #123
```

#### 4. Documentation Contributions

Documentation contributions are equally important! You can:

- Fix typos and grammar
- Improve structure and readability
- Add usage examples
- Translate documentation

### Quality Checklist

Before submitting, check:

- [ ] Skill follows directory structure standards
- [ ] SKILL.md metadata is complete
- [ ] Chinese and English versions are in sync (if applicable)
- [ ] Prompts are clear and understandable
- [ ] Documentation links are valid
- [ ] No spelling errors

### Code of Conduct

- Respect all contributors
- Be friendly and professional
- Accept constructive criticism
- Focus on project goals: providing high-quality testing Skills

### License

Contributed content will be licensed under the project's license.

### Getting Help

If you have questions:

1. Check [FAQ_EN.md](FAQ_EN.md)
2. Ask in Issues
3. Review existing Skills as reference

---

## Thank You

Thank you for your contributions! Every contribution makes this project better.
