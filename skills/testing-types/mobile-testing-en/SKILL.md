---
name: mobile-testing-en
version: 2.0.0
last-updated: 2024-02-06
description: Design mobile (iOS/Android) test plans and cases covering functionality, compatibility, performance, network, security. Default output Markdown; can request Excel/CSV/JSON. Use for mobile testing.
category: testing-types
level: advanced
tags: [mobile, android, ios, appium, detox, espresso, xcuitest, automation]
dependencies: [functional-testing-en]
recommended-with: [automation-testing-en, performance-testing-en, accessibility-testing-en]
context-aware: true
context-patterns:
  project-types: [mobile]
  platforms: [android, ios, react-native, flutter, hybrid]
  test-frameworks: [appium, detox, espresso, xcuitest, flutter-test]
  test-types: [functional, compatibility, performance, network, battery, security]
output-formats: [markdown, excel, csv, json, jira, testrail]
examples-count: 1
has-tutorial: false
has-troubleshooting: true
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

1. Open `prompts/mobile-testing_EN.md`, copy everything below the dashed line into the AI chat.
2. Append mobile app requirements, platform features, or test objectives.
3. For Excel/CSV/JSON, append the request line from output-formats.md.

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
