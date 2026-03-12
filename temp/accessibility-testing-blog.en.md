# Accessibility Testing Skill: what it actually does in a JD.com promotional gift flash-sale campaign flow

A lot of testing skills have the same problem — the capability exists, but the explanation reads like a table of contents. That tells you the skill exists. It does not tell you what the skill actually does in a real business flow.

This post is about Accessibility Testing. Straight to the point. What the skill does, where it fits, where it stops, and what kind of output it can produce in a real JD.com promotional gift flash-sale campaign scenario — that is the whole point here.

## Skill Overview

The `accessibility-testing` skill has a clear job — Focuses on WCAG compliance, keyboard access, screen reader support, and semantic form behavior.

Its current description is: Use this skill when you need to design accessibility testing against WCAG, keyboard navigation, and assistive technology scenarios; triggers include 可访问性测试 and accessibility testing.

The useful part is not “it helps with testing.” That does not say much. The useful part is that it turns testing work into something executable — strategy, cases, reports, or findings that people can act on.

## Usage Scenarios and Scope

Where does this skill fit — Fits campaign pages, flash-sale entry points, gift-claim modals, countdown widgets, and order confirmation pages.

More concretely, it works well when:

- a campaign requirement just landed and the team needs structure fast
- launch timing is tight and risk-based prioritization matters
- the flow crosses pages, services, and states, so guesswork stops being acceptable
- the team needs reusable deliverables instead of one-off verbal conclusions

It does not do everything. It does its part. But that part is usually where things start to drift.

## Practical Simulation: JD.com promotional gift flash-sale campaign

Here is the scenario — JD.com runs a promotional gift flash-sale event. Users enter the campaign page, see the countdown, pass eligibility checks, purchase the item, complete payment, and then claim the gift. The flow sounds simple. The sharp edges are not simple — eligibility, inventory, concurrency, status sync, and rollback behavior can all break the event in different ways.

This simulation uses the `accessibility-testing` skill and keeps the focus exactly where that skill is supposed to focus.

### Simulated Input

- Campaign start time: 8:00 PM, 10-minute flash-sale window
- Gift inventory: 500 units
- Eligibility rule: PLUS members with spending over 199 RMB in the last 30 days
- Critical path: campaign page -> eligibility check -> flash order -> payment -> gift claim -> gift center status rendering
- Risk context: high traffic, fast inventory changes, mobile and web channels open at the same time

### Simulated Output

In the simulation, the keyboard tab order broke between “Buy Now” and “Claim Gift”, the screen reader never announced the countdown end time, and form errors missed aria-describedby. After fixes, the full claim flow worked without a mouse.

### What the deliverable looks like

A useful run of this skill should not end with “tested.” It should end with things like:

- a clear problem statement
- repeatable steps or trigger conditions
- business impact framing
- a fix direction or next testing action

That is a usable output. It is not a decorative output.

## Why this skill matters

For campaign testing, the value is practical — it helps you miss fewer cases, waste less time, and rely less on luck right before launch.

More directly, it turns vague language like “we should test this” into specific actions that can be executed, tracked, and reviewed later. That matters a lot in a flash-sale gift campaign. Problems do not wait for production to become real. They are already there.

## Closing

`accessibility-testing` is not there to sit in a catalog. It is a working skill. Put it in the right scenario and the output becomes concrete fast.

If you are testing a campaign-driven business flow right now, this is a skill worth using early. A lot of defects do not suddenly appear after launch — they were there the whole time, waiting for someone to look properly.
