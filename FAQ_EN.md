# Frequently Asked Questions (FAQ)

[中文](FAQ.md) | [English](#english-faq)

---

## English FAQ

### Basic Questions

#### 1. What is AI Testing Assistant Skills?

A testing skills library designed specifically for AI coding assistants, containing **18 carefully designed testing Skills** (15 testing types + 3 workflows) to help Cursor, Claude Code, Kiro, and other AI tools become your professional testing assistant.

#### 2. Which AI tools are supported?

- **Cursor** (v0.40+)
- **Claude Code** (v1.0+)
- **Kiro** (v0.5+)

#### 3. How to get started quickly?

```bash
# 1. Clone the project
git clone https://github.com/your-repo/ai-testing-assistant-skills.git

# 2. Copy needed skill
cp -r skills/testing-types/functional-testing-en ~/.cursor/skills/

# 3. Use in AI tool
@skill functional-testing-en
Help me generate test cases for user login functionality
```

#### 4. What's the difference between Chinese and English versions?

Functionally identical, just different languages. Chinese skill directories like `functional-testing`, English as `functional-testing-en`.

#### 5. Can I use multiple skills together?

Yes! Skills are designed to be composable. Check [skills-graph.md](skills-graph.md) for recommended skill combinations.

---

### Installation and Configuration

#### 6. How to install to Cursor?

```bash
# Project level (recommended)
cp -r skills/testing-types/functional-testing-en /path/to/your/project/.cursor/skills/

# User level (global)
cp -r skills/testing-types/functional-testing-en ~/.cursor/skills/
```

#### 7. How to install to Claude Code?

```bash
mkdir -p .claude/skills
cp -r skills/testing-types/functional-testing-en .claude/skills/
```

#### 8. How to install to Kiro?

```bash
# Project level
mkdir -p .kiro/skills
cp -r skills/testing-types/functional-testing-en .kiro/skills/

# Global
mkdir -p ~/.kiro/skills
cp -r skills/testing-types/functional-testing-en ~/.kiro/skills/
```

#### 9. How to update skills?

```bash
# 1. Pull latest code
cd ai-testing-assistant-skills
git pull origin main

# 2. Re-copy skills
cp -r skills/testing-types/functional-testing-en /path/to/your/project/.cursor/skills/
```

#### 10. How to customize skills?

1. Copy skill to your project
2. Modify prompt files in `prompts/` directory
3. Adjust content as needed

---

### Usage Questions

#### 11. How to invoke a skill?

In AI tool's chat:

```
@skill functional-testing-en
Requirement: User login functionality
```

#### 12. How to specify output format?

Specify at the end of requirement:

```
@skill functional-testing-en
Requirement: User login functionality
Please output as tab-separated table for Excel
```

Supported formats: Markdown (default), Excel, CSV, JSON, Jira, TestRail.

#### 13. How to use workflows?

```
@skill daily-testing-workflow-en
Today I need to test user login and registration features
```

Workflow will guide you through daily testing activities.

#### 14. How to find the right skill?

Three ways:
1. Check [README_EN.md](README_EN.md) - Skills list
2. Check [skills-index.md](skills-index.md) - By category
3. Check [skills-graph.md](skills-graph.md) - Skills relationships

#### 15. What testing type Skills are available?

15 testing type Skills:
- Functional Testing, API Testing, Automation Testing
- Performance Testing, Security Testing, Mobile Testing, Accessibility Testing
- Bug Reporting, Test Case Writing, Test Case Review
- Test Reporting, Test Strategy, Requirements Analysis
- Manual Testing, AI-Assisted Testing

---

### Feature Questions

#### 16. How to generate test cases?

```
@skill test-case-writing-en
Requirement: User login functionality, support email and phone login
```

AI will automatically generate test cases including normal, exception, and boundary value scenarios.

#### 17. How to generate automation test code?

```
@skill automation-testing-en
Requirement: Generate Playwright automation test code for login functionality
```

AI will generate runnable test code.

#### 18. How to analyze requirements?

```
@skill requirements-analysis-en
Requirement: Users can login to the system via email or phone number
```

AI will analyze requirements and extract test points.

#### 19. How to create test strategy?

```
@skill test-strategy-en
Project info:
- Type: Web application
- Tech stack: React + Node.js
- Team size: 5 people
```

AI will generate customized test strategy.

#### 20. How to use multiple Skills together?

Refer to recommended combinations in [skills-graph.md](skills-graph.md), for example:

**New Feature Testing Flow**:
```
1. @skill requirements-analysis-en
2. @skill test-strategy-en
3. @skill test-case-writing-en
4. @skill functional-testing-en
5. @skill automation-testing-en
```

---

### Troubleshooting

#### 21. Skill cannot be loaded?

Check:
1. Directory name is correct
2. SKILL.md file exists
3. File permissions are correct
4. AI tool version supports Skills

#### 22. Output format is incorrect?

Ensure you specify format at the end of requirement:

```
Please output as tab-separated table for Excel
```

#### 23. Chinese and English versions are out of sync?

Please submit an Issue to report, we will fix it promptly.

#### 24. How to choose the right Skill?

Based on your needs:
- **Write test cases** → test-case-writing-en
- **Functional testing** → functional-testing-en
- **API testing** → api-testing-en
- **Automation testing** → automation-testing-en
- **Performance testing** → performance-testing-en
- **Security testing** → security-testing-en

#### 25. What are the relationships between Skills?

Check [skills-graph.md](skills-graph.md) to understand dependencies and recommended combinations between Skills.

---

### Contributing and Community

#### 26. How to contribute a new skill?

1. Fork the project
2. Create new Skill directory
3. Write SKILL.md, prompts/, etc.
4. Submit Pull Request

See [CONTRIBUTING_EN.md](CONTRIBUTING_EN.md) for details.

#### 27. How to report bugs?

1. Search [Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues)
2. If not reported, create new Issue
3. Provide detailed information and reproduction steps

#### 28. How to request a new Skill?

1. Search existing Feature Requests
2. Create new Issue with `enhancement` label
3. Describe Skill requirements and use cases in detail

#### 29. What is the project license?

MIT License. You can freely use, modify, and distribute.

#### 30. How to get more help?

1. Check this FAQ
2. Check [README_EN.md](README_EN.md)
3. Search [Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues)
4. Ask in GitHub Issues

---

## Can't Find Your Answer?

If your question isn't listed, please ask in [GitHub Issues](https://github.com/your-repo/ai-testing-assistant-skills/issues).

---

**Last Updated**: 2024-02-09
