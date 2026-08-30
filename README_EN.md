<div align="right"><strong><a href="./README.md">🇨🇳中文</a></strong> | <strong>🇬🇧English</strong></div>

# Awesome QA Skills

A language-partitioned **AI testing skills library** (Agent Skills) for Codex, Cursor, Claude Code, Kiro, OpenCode, Trae, and similar tools. It ships independently installable, composable skills for testing workflows and testing types.

[![License: PolyForm Noncommercial 1.0.0](https://img.shields.io/badge/License-PolyForm%20Noncommercial%201.0.0-blue.svg)](./LICENSE)
[![Skills](https://img.shields.io/badge/skills-156%20(zh%2Ben)-0A7EA4)](./docs/catalog/skills-index.md)
[![Workflows](https://img.shields.io/badge/workflows-10-informational)](./skills/en/testing-workflows/)
[![Testing types](https://img.shields.io/badge/testing%20types-65-informational)](./skills/en/testing-types/)
[![Skill engineering](https://img.shields.io/badge/skill%20engineering-3-informational)](./skills/en/skill-engineering/)
[![skills.sh](https://skills.sh/b/naodeng/awesome-qa-skills)](https://skills.sh/naodeng/awesome-qa-skills)

**Online site:** [https://inaodeng.com/qaskills/](https://inaodeng.com/qaskills/)

---

## Why this repository

| Capability | Description |
| --- | --- |
| Bilingual parity | `skills/zh` and `skills/en` share the same folder names and layout |
| Full testing chain | From requirements and strategy through cases, execution, defects, and reporting |
| Workflows + type skills | Daily / sprint / release, role-quality perspective, and multi-role synthesis workflows, composed with 65 specialized type skills |
| Ready to install | One-click installers plus per-skill shortcut scripts |
| Evaluable & evolvable | Every skill includes `evals/`; validate and run with [skill-up](https://github.com/alibaba/skill-up) |

Each skill directory is meant to be self-contained when copied out: `SKILL.md`, primary prompts, tool metadata, plus optional examples, templates, scripts, and eval cases.

## Choose Skills by Category

Start with the delivery or testing stage you are in, then install or invoke a Skill from that section. Use the routing workflow when you are unsure. The [complete Skills index](docs/catalog/skills-index_EN.md) remains available when you already know a name.

| What are you trying to do? | Choose a category | Typical stages / capabilities | Entry point |
| --- | --- | --- | --- |
| Build a quality foundation across requirements, strategy, cases, execution, and reporting | Core QA Skills | Discovery, strategy, design, execution, defects, and reporting | [View Core QA Skills](#core-qa-skills--quality-foundation) |
| Shift quality left, assess change, implement automation, or make performance decisions | Engineering QA Skills | Requirements shift left, development / CI, regression, performance, and continuous improvement | [View Engineering QA Skills](#engineering-qa-skills--quality-engineering) |
| Make quality decisions from release and production evidence | Production Quality Skills | Release verification, incident response, trace, and metrics analysis | [View Production Quality Skills](#production-quality-skills--production-quality) |
| Test AI features, LLMs, prompts, agents, and safety boundaries | AI Native QA Skills | AI requirements and risk, evaluation, tool use, and injection defense | [View AI Native QA Skills](#ai-native-qa-skills--ai-native-quality) |
| Orchestrate stages, collaborate by role, or decide where to begin | Cross-phase workflows | Routing, daily / sprint / release workflows, quality perspectives, and synthesis | [View workflows](#cross-phase-workflows) |
| You already know the Skill name | Complete index | All 78 capabilities and Chinese/English paths | [Open the complete Skills index](docs/catalog/skills-index_EN.md) |

**Recommended path:** start with [`discover-testing`](skills/en/testing-workflows/discover-testing/) when uncertain, select the matching capability layer once the stage is clear, or go directly to the complete index when you know the name.

## Capability evolution map

The repository uses stable directories for installation and capability stages for navigation and evolution:

```text
Core QA Skills → Engineering QA Skills → Production Quality Skills → AI Native QA Skills
```

| Stage | Question | Current entry points | Direction |
| --- | --- | --- | --- |
| Core QA Skills | How do requirements, strategy, cases, execution, and reporting form a quality foundation? | `requirements-analysis`, `test-strategy`, `functional-testing`, `test-reporting` | Preserve a complete foundation without duplicate packages |
| Engineering QA Skills | How do we shift quality left, assess change, diagnose issues, and make performance decisions? | `code-review`, `automation-testing`, `performance-testing` | Shift Left, change/execution intelligence, performance engineering |
| Production Quality Skills | How do we make quality decisions from release and production evidence? | `release-testing-workflow`, `test-reporting` | Production verification, incidents, and observability |
| AI Native QA Skills | How do we test AI features, LLMs, prompts, agents, and safety boundaries? | AI feature, LLM, prompt, agent, and safety Skills are available | Testing-for-AI specialized Skills |

`ai-assisted-testing` is cross-cutting **AI for QA**, not the Testing-for-AI scope of AI Native QA. The six-iteration roadmap, 29 added Skills, and Prompt Baseline mapping are in the [evolution roadmap](docs/governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md).

## Supported AI tools

| Tool | Typical install target |
| --- | --- |
| Codex | `~/.codex/skills/` |
| Cursor | `~/.cursor/skills/` |
| Claude Code | Claude skills directory (see install guide) |
| Kiro / OpenCode / Trae | See [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) |

You can also `cp -r` a single skill folder into the tool’s skills path.

## 5-minute start

### 1. Clone the repository

```bash
git clone https://github.com/naodeng/awesome-qa-skills.git
cd awesome-qa-skills
```

### 2. Install skills (pick one)

```bash
# One-click: all tools × both languages
bash ./install-skills-mac.sh --tool all --lang all

# Codex + English only
bash ./install-skills-mac.sh --tool codex --lang en

# Single skill (example: functional-testing → Codex)
bash installers/en/functional-testing/mac/codex.sh
```

You can also use `npx skills` to install skills into a supported AI tool (Node.js required):

```bash
# Install all English skills into Codex
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/en -g -a codex -y

# Install one skill only
npx skills add https://github.com/naodeng/awesome-qa-skills/tree/main/skills/en/testing-types/functional-testing -g -a codex -y
```

For Chinese skills, replace `skills/en` in the URL with `skills/zh`. Install one language at a time to avoid same-named skills overwriting each other.

Windows:

```powershell
powershell -ExecutionPolicy Bypass -File .\install-skills-windows.ps1 -Tool all -Lang all
```

Manual copy:

```bash
cp -r skills/en/testing-types/functional-testing ~/.cursor/skills/
```

Full options and tool paths: [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md)

### 3. Invoke in your AI tool

```text
@skill functional-testing
Help me generate test cases for user login
```

Unsure which skill to use? Start with the router:

```text
@skill discover-testing
I need a pre-release regression — which skills should I use?
```

---

## Skill catalog

Each language provides **78** Skills: 10 workflows, 65 testing types, and 3 Skill Engineering packages; **156** bilingual directories in total. Physical directories remain stable; the catalog below is logical navigation only.

### Cross-phase workflows

Workflows orchestrate lifecycle phases and do not form a fifth capability stage.

#### Discovery

| Skill | Directory | Primary use |
| --- | --- | --- |
| Testing Skill Discovery | [`discover-testing`](skills/en/testing-workflows/discover-testing/) | Use this skill when you need to route a request to the right testing skill before execution; triggers include discover testing, testing skill router, and which… |
| Product Quality Perspective | [`product-quality-perspective`](skills/en/testing-workflows/product-quality-perspective/) | Identify user value, business rules, acceptance gaps, and decision risks across product quality stages. |
| QA quality perspective | [`qa-quality-perspective`](skills/en/testing-workflows/qa-quality-perspective/) | Assesses testability, risk-based coverage, defect risk, and evidence-bound quality conclusions across QA stages. |
| UX Quality Perspective | [`ux-quality-perspective`](skills/en/testing-workflows/ux-quality-perspective/) | Identify information architecture, interaction-state, consistency, responsive, and accessibility risks across quality stages. |
| Technical quality perspective | [`technical-quality-perspective`](skills/en/testing-workflows/technical-quality-perspective/) | Produces evidence-backed technical quality findings for a selected delivery stage. |

#### Development

| Skill | Directory | Primary use |
| --- | --- | --- |
| Daily Testing Workflow | [`daily-testing-workflow`](skills/en/testing-workflows/daily-testing-workflow/) | Use this skill when you need a day-by-day QA routine including planning, execution, bug reporting, and end-of-day wrap-up; triggers include daily testing workf… |
| Sprint Testing Workflow | [`sprint-testing-workflow`](skills/en/testing-workflows/sprint-testing-workflow/) | Use this skill when you need a sprint-based QA workflow from planning through review and retrospective; triggers include sprint testing workflow and sprint QA… |
| Project Delivery Perspective | [`project-delivery-perspective`](skills/en/testing-workflows/project-delivery-perspective/) | Capture attributable delivery constraints and actions for supported strategy and report-review stages without changing quality facts. |

#### Release

| Skill | Directory | Primary use |
| --- | --- | --- |
| Release Testing Workflow | [`release-testing-workflow`](skills/en/testing-workflows/release-testing-workflow/) | Use this skill when you need release-phase QA workflow from T-14 planning to go/no-go and post-release monitoring; triggers include release testing workflow an… |
| Multi-Role Quality Synthesis | [`multi-role-quality-synthesis`](skills/en/testing-workflows/multi-role-quality-synthesis/) | Combine role reports into a source-preserving quality synthesis |

### Four capability stages by R&D and testing phase

Each testing-type Skill appears once; routers and workflows cover cross-phase composition.

#### Core QA Skills — Quality foundation

##### Discovery and Requirements Analysis

| Skill | Directory | Primary use |
| --- | --- | --- |
| Requirements Analysis (English) <!-- data-skill:requirements-analysis --> | [`requirements-analysis`](skills/en/testing-types/requirements-analysis/) | Use this skill when you need to analyze requirements, identify test points, boundaries, dependencies, and risks before test design; triggers include requiremen… |
| Requirements Analysis Plus <!-- data-skill:requirements-analysis-plus --> | [`requirements-analysis-plus`](skills/en/testing-types/requirements-analysis-plus/) | Use this skill when you need to parse Word/HTML/JSON/Markdown/Excel requirements and produce a structured analysis; triggers include requirements analysis plus… |

##### Solution Design and Test Strategy

| Skill | Directory | Primary use |
| --- | --- | --- |
| Test Strategy <!-- data-skill:test-strategy --> | [`test-strategy`](skills/en/testing-types/test-strategy/) | Use this skill when you need to define a test strategy covering scope, methods, resources, risks, and quality gates; triggers include test strategy and QA plan… |
| Test Strategy Plus <!-- data-skill:test-strategy-plus --> | [`test-strategy-plus`](skills/en/testing-types/test-strategy-plus/) | Use this skill when you need a structured test strategy from requirement, analysis, tech, and plan docs; triggers include test strategy plus and advanced test… |
| Test Strategy Review <!-- data-skill:test-strategy-review --> | [`test-strategy-review`](skills/en/testing-types/test-strategy-review/) | Review test strategy evidence, separate blockers from conditions, and leave the final decision to a Human |

##### Test Design and Preparation

| Skill | Directory | Primary use |
| --- | --- | --- |
| Test Case Writing (English) <!-- data-skill:test-case-writing --> | [`test-case-writing`](skills/en/testing-types/test-case-writing/) | Use this skill when you need to create high-quality test cases with normal, exception, and boundary scenarios; triggers include test case writing and test desi… |
| Testcase Writer Plus <!-- data-skill:testcase-writer-plus --> | [`testcase-writer-plus`](skills/en/testing-types/testcase-writer-plus/) | Use this skill when you need high-quality test cases from requirements and analysis artifacts; triggers include testcase writer plus and advanced test case wri… |
| Test Case Review <!-- data-skill:test-case-reviewer --> | [`test-case-reviewer`](skills/en/testing-types/test-case-reviewer/) | Use this skill when you need to review test cases for completeness, clarity, maintainability, and missing scenarios; triggers include test case review and test… |
| Test Case Reviewer Plus <!-- data-skill:test-case-reviewer-plus --> | [`test-case-reviewer-plus`](skills/en/testing-types/test-case-reviewer-plus/) | Use this skill when you need structured test-case review findings from requirements, strategy, and case docs; triggers include test case reviewer plus and adva… |

##### Test Execution and Analysis

| Skill | Directory | Primary use |
| --- | --- | --- |
| Functional Testing (English) <!-- data-skill:functional-testing --> | [`functional-testing`](skills/en/testing-types/functional-testing/) | Use this skill when you need to design functional test plans or cases for business flows, UI, data, and integrations; triggers include functional testing and f… |
| API Testing (English) <!-- data-skill:api-testing --> | [`api-testing`](skills/en/testing-types/api-testing/) | Use this skill when you need to design API test plans or cases for REST, GraphQL, or gRPC interfaces; triggers include API testing and API test cases. |
| Manual/Exploratory Testing <!-- data-skill:manual-testing --> | [`manual-testing`](skills/en/testing-types/manual-testing/) | Use this skill when you need to plan manual or exploratory testing with charters, heuristics, and session records; triggers include manual testing and explorat… |
| Mobile Testing (English) <!-- data-skill:mobile-testing --> | [`mobile-testing`](skills/en/testing-types/mobile-testing/) | Use this skill when you need to design mobile test plans for iOS or Android covering functionality, compatibility, performance, network, and security; triggers… |
| Accessibility Testing (English) <!-- data-skill:accessibility-testing --> | [`accessibility-testing`](skills/en/testing-types/accessibility-testing/) | Use this skill when you need to design accessibility testing against WCAG, keyboard navigation, and assistive technology scenarios; triggers include accessibil… |
| Security Testing (English) <!-- data-skill:security-testing --> | [`security-testing`](skills/en/testing-types/security-testing/) | Use this skill when you need to design security testing around OWASP risks, vulnerability scanning, and penetration scenarios; triggers include security testin… |

##### Release, Defects, and Reporting

| Skill | Directory | Primary use |
| --- | --- | --- |
| Bug Reporting <!-- data-skill:bug-reporting --> | [`bug-reporting`](skills/en/testing-types/bug-reporting/) | Use this skill when you need to write clear, reproducible bug reports with steps, environment details, and evidence; triggers include bug reporting and defect… |
| Test Reporting <!-- data-skill:test-reporting --> | [`test-reporting`](skills/en/testing-types/test-reporting/) | Use this skill when you need to generate test reports with summary, metrics, defect analysis, and risk assessment; triggers include test reporting and QA statu… |
| Test Report Review <!-- data-skill:test-report-review --> | [`test-report-review`](skills/en/testing-types/test-report-review/) | Check report claims against execution, defect, and scope evidence while preserving Human authority |

#### Engineering QA Skills — Quality engineering

##### Requirements and Shift Left

| Skill | Directory | Primary use |
| --- | --- | --- |
| Acceptance Criteria Review <!-- data-skill:acceptance-criteria-review --> | [`acceptance-criteria-review`](skills/en/testing-types/acceptance-criteria-review/) | Review acceptance-criteria gaps and verifiability |
| Requirement Gap Analysis <!-- data-skill:requirement-gap-analysis --> | [`requirement-gap-analysis`](skills/en/testing-types/requirement-gap-analysis/) | Identify requirement gaps, conflicts, and impact |
| Quality Risk Analysis <!-- data-skill:quality-risk-analysis --> | [`quality-risk-analysis`](skills/en/testing-types/quality-risk-analysis/) | Identify and rank evidence-based quality risks |
| Testability Analysis <!-- data-skill:testability-analysis --> | [`testability-analysis`](skills/en/testing-types/testability-analysis/) | Assess testability and prioritized blockers |

##### Development and Continuous Integration

| Skill | Directory | Primary use |
| --- | --- | --- |
| Code Review <!-- data-skill:code-review --> | [`code-review`](skills/en/testing-types/code-review/) | Risk-driven PR/diff code review with P0/P1/P2 findings and actionable fixes; triggers include code review and PR review. |
| Change Impact Analysis <!-- data-skill:change-impact-analysis --> | [`change-impact-analysis`](skills/en/testing-types/change-impact-analysis/) | Analyze quality impact scope and risk from change |
| PR Test Impact Analysis <!-- data-skill:pr-test-impact-analysis --> | [`pr-test-impact-analysis`](skills/en/testing-types/pr-test-impact-analysis/) | Analyze test impact from a PR or diff |
| API Contract Testing <!-- data-skill:api-contract-testing --> | [`api-contract-testing`](skills/en/testing-types/api-contract-testing/) | Verify API contract compatibility and change risk |
| Automation Testing (English) <!-- data-skill:automation-testing --> | [`automation-testing`](skills/en/testing-types/automation-testing/) | Use this skill when you need to design automation testing approaches using patterns like POM, data-driven testing, or BDD; triggers include automation testing… |

##### Test Data and Automation Implementation

| Skill | Directory | Primary use |
| --- | --- | --- |
| Test Data Generation <!-- data-skill:test-data-generation --> | [`test-data-generation`](skills/en/testing-types/test-data-generation/) | Design safe and representative test data |
| API Test Bruno <!-- data-skill:api-test-bruno --> | [`api-test-bruno`](skills/en/testing-types/api-test-bruno/) | Use this skill when you need to parse multi-format API definitions and generate Bruno collections for executable regression; triggers include Bruno collections… |
| Postman API Testing <!-- data-skill:api-test-postman --> | [`api-test-postman`](skills/en/testing-types/api-test-postman/) | Design Postman collections, environments, scripts, and Newman-ready API regression plans. |
| API Test Pytest <!-- data-skill:api-test-pytest --> | [`api-test-pytest`](skills/en/testing-types/api-test-pytest/) | Use this skill when you need to parse multi-format API definitions and generate Pytest API automation; triggers include Pytest API tests and API automation wit… |
| API Test RestAssure <!-- data-skill:api-test-restassure --> | [`api-test-restassure`](skills/en/testing-types/api-test-restassure/) | Use this skill when you need to parse multi-format API definitions and generate Rest Assured Java test classes; triggers include Rest Assured, RestAssured, and… |
| API Test Supertest <!-- data-skill:api-test-supertest --> | [`api-test-supertest`](skills/en/testing-types/api-test-supertest/) | Use this skill when you need to parse multi-format API definitions and generate executable Supertest scripts; triggers include Supertest, Node.js API testing,… |
| Selenium UI Testing <!-- data-skill:ui-test-selenium --> | [`ui-test-selenium`](skills/en/testing-types/ui-test-selenium/) | Design Selenium WebDriver UI automation plans with stable locators, waits, Page Objects, Grid, and CI execution. |
| Playwright UI Testing <!-- data-skill:ui-test-playwright --> | [`ui-test-playwright`](skills/en/testing-types/ui-test-playwright/) | Design Playwright Test suites with fixtures, projects, traces, screenshots, API plus UI coverage, and CI reporting. |
| TestCafe UI Testing <!-- data-skill:ui-test-testcafe --> | [`ui-test-testcafe`](skills/en/testing-types/ui-test-testcafe/) | Design TestCafe UI automation with fixtures, selectors, roles, browser matrix execution, and reports. |
| Cypress UI Testing <!-- data-skill:ui-test-cypress --> | [`ui-test-cypress`](skills/en/testing-types/ui-test-cypress/) | Design Cypress e2e and component testing plans with commands, fixtures, network stubbing, and CI reporting. |
| Puppeteer UI Testing <!-- data-skill:ui-test-puppeteer --> | [`ui-test-puppeteer`](skills/en/testing-types/ui-test-puppeteer/) | Design Puppeteer automation for Chromium-driven checks, screenshots, PDFs, network interception, and CDP use cases. |
| WebdriverIO UI Testing <!-- data-skill:ui-test-webdriverio --> | [`ui-test-webdriverio`](skills/en/testing-types/ui-test-webdriverio/) | Design WebdriverIO suites with config, services, runner behavior, Page Objects, capabilities, and reporters. |

##### Test Execution and Regression Intelligence

| Skill | Directory | Primary use |
| --- | --- | --- |
| Flaky Test Analysis <!-- data-skill:flaky-test-analysis --> | [`flaky-test-analysis`](skills/en/testing-types/flaky-test-analysis/) | Analyze intermittent test failures from evidence |
| Regression Scope Analysis <!-- data-skill:regression-scope-analysis --> | [`regression-scope-analysis`](skills/en/testing-types/regression-scope-analysis/) | Define risk-based regression scope and exclusions |
| Regression Test Selection <!-- data-skill:regression-test-selection --> | [`regression-test-selection`](skills/en/testing-types/regression-test-selection/) | Select a minimum risk-covering regression set |
| AI-Assisted Testing <!-- data-skill:ai-assisted-testing --> | [`ai-assisted-testing`](skills/en/testing-types/ai-assisted-testing/) | Use this skill when you need AI-assisted testing workflows such as test data generation, root-cause analysis, and prioritization; triggers include AI-assisted… |

##### Performance Engineering and Capacity Decisions

| Skill | Directory | Primary use |
| --- | --- | --- |
| Performance Testing (English) <!-- data-skill:performance-testing --> | [`performance-testing`](skills/en/testing-types/performance-testing/) | Use this skill when you need to design performance testing for load, stress, spike, endurance, or capacity objectives; triggers include performance testing and… |
| Performance Test k6 <!-- data-skill:performance-test-k6 --> | [`performance-test-k6`](skills/en/testing-types/performance-test-k6/) | Use this skill when you need k6 load/stress/spike/soak scope, scripts, or runnable entry points; triggers include k6, k6 scripts, and k6 performance testing. |
| Performance Test Gatling <!-- data-skill:performance-test-gatling --> | [`performance-test-gatling`](skills/en/testing-types/performance-test-gatling/) | Use this skill when you need Gatling performance scope, simulations, or runnable entry points; triggers include Gatling, Gatling simulations, and Gatling perfo… |
| JMeter Performance Testing <!-- data-skill:performance-test-jmeter --> | [`performance-test-jmeter`](skills/en/testing-types/performance-test-jmeter/) | Design JMeter test plans with Thread Groups, samplers, data sets, assertions, timers, CLI runs, and HTML reports. |
| Performance Workload Modeling <!-- data-skill:performance-workload-modeling --> | [`performance-workload-modeling`](skills/en/testing-types/performance-workload-modeling/) | Build evidence-based performance workload models |
| Performance Result Analysis <!-- data-skill:performance-result-analysis --> | [`performance-result-analysis`](skills/en/testing-types/performance-result-analysis/) | Interpret performance results, evidence, and risk |
| Performance Bottleneck Analysis <!-- data-skill:performance-bottleneck-analysis --> | [`performance-bottleneck-analysis`](skills/en/testing-types/performance-bottleneck-analysis/) | Form verifiable performance bottleneck hypotheses |
| Performance Regression Analysis <!-- data-skill:performance-regression-analysis --> | [`performance-regression-analysis`](skills/en/testing-types/performance-regression-analysis/) | Compare version evidence and assess performance regression risk |
| Capacity Planning Analysis <!-- data-skill:capacity-planning-analysis --> | [`capacity-planning-analysis`](skills/en/testing-types/capacity-planning-analysis/) | Assess capacity demand, headroom, and planning risk |

##### Retrospective and Continuous Improvement

| Skill | Directory | Primary use |
| --- | --- | --- |
| Root Cause Analysis <!-- data-skill:root-cause-analysis --> | [`root-cause-analysis`](skills/en/testing-types/root-cause-analysis/) | Form and verify evidence-based root-cause hypotheses |
| Log Analysis <!-- data-skill:log-analysis --> | [`log-analysis`](skills/en/testing-types/log-analysis/) | Extract timelines, anomalies, and evidence from logs |

#### Production Quality Skills — Production quality

##### Release and Production Verification

| Skill | Directory | Primary use |
| --- | --- | --- |
| Production Verification <!-- data-skill:production-verification --> | [`production-verification`](skills/en/testing-types/production-verification/) | Plan or assess evidence-based production verification |

##### Production Operations and Incident Response

| Skill | Directory | Primary use |
| --- | --- | --- |
| Production Incident Analysis <!-- data-skill:production-incident-analysis --> | [`production-incident-analysis`](skills/en/testing-types/production-incident-analysis/) | Analyze production incident evidence, impact, and follow-up |
| Distributed Trace Analysis <!-- data-skill:distributed-trace-analysis --> | [`distributed-trace-analysis`](skills/en/testing-types/distributed-trace-analysis/) | Correlate call paths and evidence from distributed traces |
| Metrics Anomaly Analysis <!-- data-skill:metrics-anomaly-analysis --> | [`metrics-anomaly-analysis`](skills/en/testing-types/metrics-anomaly-analysis/) | Identify metric anomalies, baselines, and investigation evidence |

#### AI Native QA Skills — AI-native quality

##### AI Feature Requirements and Risk

| Skill | Directory | Primary use |
| --- | --- | --- |
| AI Feature Testing <!-- data-skill:ai-feature-testing --> | [`ai-feature-testing`](skills/en/testing-types/ai-feature-testing/) | Design AI feature behavior, risk, and boundary tests |

##### LLM and Prompt Evaluation Design

| Skill | Directory | Primary use |
| --- | --- | --- |
| LLM Evaluation Design <!-- data-skill:llm-evaluation-design --> | [`llm-evaluation-design`](skills/en/testing-types/llm-evaluation-design/) | Design LLM evaluations, judges, and human-review boundaries |
| LLM Testing <!-- data-skill:llm-testing --> | [`llm-testing`](skills/en/testing-types/llm-testing/) | Test LLM behavior, failure modes, and quality boundaries |
| Prompt Testing <!-- data-skill:prompt-testing --> | [`prompt-testing`](skills/en/testing-types/prompt-testing/) | Test prompt behavior, boundaries, and version regressions |

##### Agent, Tool, and Safety Testing

| Skill | Directory | Primary use |
| --- | --- | --- |
| AI Agent Testing <!-- data-skill:ai-agent-testing --> | [`ai-agent-testing`](skills/en/testing-types/ai-agent-testing/) | Test AI agent goals, state, recovery, and safety boundaries |
| Agent Tool Testing <!-- data-skill:agent-tool-testing --> | [`agent-tool-testing`](skills/en/testing-types/agent-tool-testing/) | Verify agent tool-call contracts, authorization, and side effects |
| Prompt Injection Testing <!-- data-skill:prompt-injection-testing --> | [`prompt-injection-testing`](skills/en/testing-types/prompt-injection-testing/) | Design AI prompt-injection defense tests |

### Skill Engineering (cross-cutting governance)

| Skill | Directory | Primary use |
| --- | --- | --- |
| Skill Change Verification | [`skill-change-verification`](skills/en/skill-engineering/skill-change-verification/) | Select evidence by change scope and distinguish static, evaluation, and runtime claims. |
| Skill Prose Contract Review | [`skill-prose-review`](skills/en/skill-engineering/skill-prose-review/) | Audit executable contracts, boundaries, and evidence requirements in Skills and Prompts. |
| Process Prose Trimming | [`skill-prose-trim`](skills/en/skill-engineering/skill-prose-trim/) | Remove review and design residue while preserving current-state contracts. |

Skill Engineering supports every capability stage without changing product-capability classification. Chinese Skills use the same folder names; switch languages at the top of the page.

## Repository layout

```text
awesome-qa-skills/
├── skills/
│   ├── zh/                      # Chinese skills
│   │   ├── testing-workflows/
│   │   ├── testing-types/
│   │   └── skill-engineering/
│   └── en/                      # English skills (same shape)
├── scripts/                     # Install, validate, and eval helpers
├── installers/                  # Generated per-skill / per-tool shortcuts
├── resources/                   # Shared reference materials, not an install source
├── legacy-prompts/              # Legacy root prompts; official prompts live inside skills
├── AGENTS.md                    # Conventions for coding agents
├── docs/catalog/                # Full index and relationship graph
├── README.md / README_EN.md
└── LICENSE                      # PolyForm Noncommercial 1.0.0
```

### Per-skill layout

```text
skills/{zh|en}/{testing-types|testing-workflows|skill-engineering}/<skill-name>/
├── SKILL.md                 # Entry + YAML frontmatter (required)
├── prompts/                 # Primary prompts (required)
├── agents/openai.yaml       # OpenAI / Codex metadata (required)
├── evals/                   # skill-up eval cases (present for all skills here)
├── output-formats.md        # Optional multi-format output notes
├── quick-start.md           # Optional shortest path
├── references/ · examples/ · scripts/
└── ...
```

Details: [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md) · [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)

## Design principles

- **Language partition, name parity:** zh/en share skill folder names; no `-en` suffix; English prompt filenames do not use `_EN`.
- **Independently installable:** do not hard-link skill A to skill B internals; cross-skill advice stays in prose.
- **Progressive disclosure:** keep `SKILL.md` lean; put depth in `prompts/`, `references/`, and `examples/`.
- **Actionable outputs:** Markdown by default; switch via `output-formats.md` for Excel/CSV/JSON/Word.
- **Secure by default:** never hard-code real tokens, passwords, or private keys in examples or docs.

## Quality and evaluation

Before submitting changes, run from the repo root:

```bash
bash scripts/check_skills_quality.sh
```

This gate covers directory hygiene, agents metadata, install independence, integrity checks, and skill-up evals YAML validation.

Optional validate / run with [skill-up](https://github.com/alibaba/skill-up):

```bash
curl -fsSL https://raw.githubusercontent.com/alibaba/skill-up/main/install.sh | bash
bash scripts/validate_skill_evals.sh
bash scripts/run_skill_eval.sh skills/en/testing-types/functional-testing/evals/eval.yaml
```

Suggested pilots: `functional-testing`, `api-testing`, `api-test-bruno`, `bug-reporting`, `performance-test-k6`. See [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md).

## Documentation map

| Document | Purpose |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Coding-agent conventions and quality checks |
| [skills-index.md](docs/catalog/skills-index.md) | Full skill index |
| [QA_SKILLS_EVOLUTION_ROADMAP_EN.md](docs/governance/QA_SKILLS_EVOLUTION_ROADMAP_EN.md) | Four-stage capability evolution and R&D/testing lifecycle map |
| [DOCUMENTATION_POLICY_EN.md](docs/governance/DOCUMENTATION_POLICY_EN.md) | Chinese-first bilingual documentation policy |
| [skills/DIRECTORY_GUIDE.md](skills/DIRECTORY_GUIDE.md) | Directory and naming rules |
| [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md) | Authoring and skill-up eval conventions |
| [scripts/INSTALL_SKILLS.md](scripts/INSTALL_SKILLS.md) | Install options and tool paths |
| [FAQ_EN.md](FAQ_EN.md) | FAQ (English) |
| [CONTRIBUTING_EN.md](CONTRIBUTING_EN.md) | Contribution guide (English) |
| [skills-graph.md](docs/catalog/skills-graph.md) | Skill relationship graph (reference) |

## Contributing

Issues and PRs are welcome: new skills, bilingual parity, prompt/evals improvements, installers, and docs.

1. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [skills/SKILL_AUTHORING.md](skills/SKILL_AUTHORING.md)
2. Update zh and en together unless the change is intentionally single-language
3. Run `bash scripts/check_skills_quality.sh` before opening a PR

## License

This repository is licensed under the [PolyForm Noncommercial License 1.0.0](./LICENSE). You may use, modify, and distribute the software for noncommercial purposes only (e.g. personal study, research, experimentation, charitable organizations, educational institutions, public research organizations, or government institutions).
