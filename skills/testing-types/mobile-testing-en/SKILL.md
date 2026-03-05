---
name: mobile-testing-en
description: Use this skill when you need to design mobile test plans for iOS or Android covering functionality, compatibility, performance, network, and security; triggers include mobile testing and app testing.
---

# Mobile Testing (English)

**中文版:** See skill `mobile-testing`.

Prompt: this directory's `prompts/mobile-testing_EN.md`.

## When to Use

- User mentions **mobile testing**, **APP testing**, **iOS/Android testing**
- Need to design or execute mobile test plans and cases (device matrix, OS versions, network, lifecycle, etc.)
- **Trigger examples:** "Design mobile test plan for the following requirements" or "Output mobile test cases"

## Output Format Options

**Markdown** by default. For **Excel / CSV / JSON**, add at the **end** of your request; see **[output-formats.md](output-formats.md)**.

## How to Use

1. Open the relevant file in this directory's `prompts/` and copy the content below the dashed line.
2. Append your requirements and context (business flow, environment, constraints, acceptance criteria).
3. If you need non-Markdown output, append the request sentence from `output-formats.md` at the end.

## Code Examples

### 1. Appium Android Automation Testing

Complete Appium + Python Android testing example.

**Location:** `../mobile-testing/examples/appium-android/`

**Includes:**
- Page Object Model architecture
- Login and navigation tests
- Gesture operation examples
- Pytest configuration

**Quick Start:**
```bash
cd examples/appium-android
pip install -r requirements.txt
appium &
pytest
```

See: [examples/appium-android/README.md](../mobile-testing/examples/appium-android/README.md)

## Best Practices

### Mobile Testing Strategy

1. **Device Coverage**
   - Mainstream device models
   - Different screen sizes
   - Different OS versions

2. **Test Types**
   - Functional testing
   - Compatibility testing
   - Performance testing
   - Network testing
   - Security testing

3. **Automation Strategy**
   - Automate core flows
   - Automate regression tests
   - Supplement with manual testing

## Common Pitfalls

- ❌ Testing on a single device model only → ✅ Validate representative device/OS/network matrix
- ❌ Ignoring lifecycle interruptions → ✅ Cover calls, background/foreground switches, and permission prompts
- ❌ Not testing degraded networks → ✅ Verify behavior under weak, unstable, and offline conditions
- ❌ Overfocusing on UI flow → ✅ Include install/update, crash, battery, and performance checks

## Troubleshooting

### Common Issues

#### 1. Appium Connection Failed

**Solution**:
```bash
appium --version
adb devices
pkill -f appium && appium
```

#### 2. Element Location Failed

**Solution**:
- Use Appium Inspector
- Increase wait time
- Check locators

#### 3. App Installation Failed

**Solution**:
```bash
adb install app.apk
adb uninstall com.example.app
```

## Reference Files

- **prompts/mobile-testing_EN.md** — Mobile testing Standard-version prompt
- **output-formats.md** — Markdown / Excel / CSV / JSON request instructions
- **examples/appium-android/** — Complete Appium Android example
- **quick-start.md** — 5-minute quick start guide

**Related skills:** functional-testing-en, automation-testing-en, performance-testing-en, accessibility-testing-en.

## Target Audience

- QA engineers and developers executing this testing domain in real projects
- Team leads who need structured, reproducible testing outputs
- AI users who need fast, format-ready deliverables for execution and reporting

## Not Recommended For

- Pure production incident response without test scope/context
- Decisions requiring legal/compliance sign-off without expert review
- Requests lacking minimum inputs (scope, environment, expected behavior)

## Critical Success Factors

- Provide clear scope, environment, and acceptance criteria before generation
- Validate generated outputs against real system constraints before execution
- Keep artifacts traceable (requirements -> test points -> defects -> decisions)

## Output Templates and Parsing Scripts

- Template directory: `output-templates/`
  - `template-word.md` (Word-friendly structure)
  - `template-excel.tsv` (Excel paste-ready)
  - `template-xmind.md` (XMind-friendly outline)
  - `template-json.json`
  - `template-csv.csv`
  - `template-markdown.md`
- Parser scripts directory: `scripts/`
  - Parse (generic): `parse_output_formats.py`
  - Parse (per-format): `parse_word.py`, `parse_excel.py`, `parse_xmind.py`, `parse_json.py`, `parse_csv.py`, `parse_markdown.py`
  - Convert (generic): `convert_output_formats.py`
  - Convert (per-format): `convert_to_word.py`, `convert_to_excel.py`, `convert_to_xmind.py`, `convert_to_json.py`, `convert_to_csv.py`, `convert_to_markdown.py`
  - Batch convert: `batch_convert_templates.py` (outputs into `artifacts/`)

Examples:
```bash
python3 scripts/parse_json.py output-templates/template-json.json
python3 scripts/parse_markdown.py output-templates/template-markdown.md
python3 scripts/convert_to_json.py output-templates/template-markdown.md
python3 scripts/convert_output_formats.py output-templates/template-json.json --to csv
python3 scripts/batch_convert_templates.py --skip-same
```
