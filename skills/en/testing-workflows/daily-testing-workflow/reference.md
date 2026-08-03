# Daily Testing Workflow — Stage Handoff Map

Orchestration prompt: `prompts/daily-testing-workflow.md` (stage goals, gates, handoffs).  
For stage deep-dives, hand off to the matching **type skill** (skill names only—no relative-path links to other skill internals).

| Step | Handoff skill | Use |
|------|---------------|-----|
| Morning review | `requirements-analysis`, `test-strategy` | Today's stories & high-risk areas |
| Set up environment | `automation-testing`, `test-strategy` | Pipeline & test data |
| Test case creation | `test-case-writing`, `requirements-analysis`, `functional-testing` | New/fix scenarios |
| Test automation | `automation-testing`, `api-testing`, `ai-assisted-testing` | Write & maintain automation |
| Exploratory testing | `manual-testing` | Charters & sessions |
| Bug reporting | `bug-reporting` | Bug reports |
| Visual / E2E | `accessibility-testing`, `functional-testing` | Visual & end-to-end |
| Afternoon review | `test-reporting`, `test-strategy` | Coverage & quality metrics |
