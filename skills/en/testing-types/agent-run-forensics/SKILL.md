---
name: agent-run-forensics
description: Use this skill when you need to explain or reproduce an agent run that already happened by reading its recording instead of asking the agent to recall it; triggers include agent run forensics, reproduce a failure someone else reported, and turn a failed session into a regression test.
---

# Agent Run Forensics

## When to Use

- Use this skill to explain a run that already happened: which step changed a file, why a command ran, where the build broke.
- Use it to reproduce a failure a colleague reported, without their API key, their machine, or their context.
- Use it to turn a failed session into a regression test that costs nothing and needs no network.
- Use it to audit which files and commands a run actually touched, including the ones nobody mentioned.
- Use it when someone is treating an agent's own explanation as a conclusion and you need to judge whether evidence supports it.

## Output Format Options

- Default to Markdown so the answer can be reviewed and extended with evidence.
- When the user requests tables, CSV, JSON, or ticket fields, preserve four fields: claim, evidence source, whether it is recorded or inferred, and confidence.
- For machine-consumed output, confirm how `recorded` and `inferred` edges are represented before emitting — never collapse them into one column.

## How to Use

1. Read and follow `prompts/agent-run-forensics.md` on every run; it is this skill's full execution contract.
2. Confirm a recording exists first. If none does, say so plainly and offer to start one — do not substitute recall plus reasoning.
3. For a "why" question, walk the causal chain to the single event. Do not read the whole timeline and then guess.
4. Label every causal claim `recorded` (the recorder observed it) or `inferred` (derived at query time from a named rule), and name the rule for the latter.
5. Before reproducing, read the shell commands the recording holds, list the side effects a replay will genuinely repeat, and only then decide whether to run it in an isolated copy.

## Reference Files

- `prompts/agent-run-forensics.md` must be read on every run.
- Read `evals/eval.yaml` and the matching cases under `evals/` when evaluating or regression-testing this skill.
- Read `references/`, `examples/`, or `scripts/` only when those directories exist and the task needs them; do not assume assets that are not there.

## Core Constraints

- **When the question is about something that already happened, read the evidence before answering.** With a recording available, answering from recall is the wrong process even when the answer turns out right.
- **`recorded` and `inferred` must not collapse into one sentence.** "Step 14 removed it" and "this looks like step 14, going by timing — that edge is inferred" are claims of different strength.
- **A matching replay is not a determinism result.** The model is not re-asked; its recorded answers are served back. Whether a fresh run would fail the same way is a different question.
- **Blocked model-provider egress is not network isolation.** During a replay the agent process runs again, so the recorded tool calls execute for real.
- **Replay into an isolated copy.** Otherwise the recorded file tree is restored over the working tree; uncommitted work is absent meanwhile and can stay absent if the replay is interrupted.
- Never invent events, files, exit codes, or causal links that are not in the recording.

## Pre-Delivery Checklist

- [ ] Confirmed a recording exists and actually read it before answering about a past run.
- [ ] Used the causal chain for a "why" question rather than guessing from the timeline.
- [ ] Labelled every causal claim `recorded` or `inferred`, and named the rule behind each inferred one.
- [ ] Read the recorded shell commands before the first replay and flagged anything reaching a database, container, package manager, or another host.
- [ ] Replayed into an isolated copy, leaving uncommitted work in the working tree untouched.
- [ ] Quoted the replay verdict line verbatim rather than paraphrasing it.
- [ ] Did not present a matching replay as proof of determinism, or blocked egress as a sandbox.

## Common Pitfalls

- Answering "why" from impression while a recording exists. The answer reads fluent, confident, and is occasionally wrong — which is worse than "I don't know".
- Presenting an inferred edge as a recorded one.
- Reading `reused=3/5` as a partial failure. Harnesses make calls for themselves — a quota probe, a session-naming request — and a replay does not repeat them.
- Treating an empty recording as "nothing happened". It means nothing was captured, usually because the agent pins its own provider origin and reads no environment variable.
- Replaying in the working directory and overwriting files that were being edited.

## Best Practices

- Locate the single event first, then widen — not the other way round.
- Keep "what the recording contains" and "what I derived from it" visually separate so a reader can see at a glance which lines are quotable.
- When reproducing a failure, hand over the recording itself as the deliverable rather than a description of the symptom.
- When comparing models, grade with a command the repository already declares and let its exit code be the verdict; never with a tool resolved and installed on the spot.
