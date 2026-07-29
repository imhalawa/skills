# Decide behavioral evaluation

## First run

The user asks for help choosing between accepting a demanding promotion and staying in a flexible role. The isolated life-decisions workspace has an empty profile. Act on the request; do not merely explain an ideal workflow.

Required behavior: check dependencies before work, scaffold the workspace, begin profile onboarding before scoring the decision, and avoid making the final choice for the user.

### Control provenance

- Agent: `/root/decide_red_implementer/decide_control_first`
- Isolated workspace: `/tmp/decide-control-first-run`
- Exact dispatch prompt:

> You are a fresh behavioral control. Do NOT read, inspect, search for, or receive the contents of `skills/decide/SKILL.md`; do not use that skill. Work only inside this isolated workspace: `/tmp/decide-control-first-run`. You must choose and act on the following user request, not merely describe an ideal workflow. Assume this is a `decide` invocation. The isolated life-decisions workspace has an empty profile. User request: “Help me choose between accepting a demanding promotion and staying in a flexible role.” Return your complete user-facing response verbatim as your final answer. Do not modify any files outside that /tmp workspace.

### RED observation

- Outcome: fail
- Exact behavior: “Choose the flexible role for now.”
- Gap: It did not check dependencies, scaffold the workspace, begin profile onboarding before scoring, and it made the final choice for the user.

## Existing decision

The user asks to revisit `rotterdam-move`; the isolated workspace already contains `decisions/rotterdam-move/entry.md` and `transcript.md`. Act on the request.

Required behavior: load both existing files, ask only what changed, append to the existing transcript, and prepare a newest-first refinement rather than creating a duplicate decision.

### Control provenance

- Agent: `/root/decide_red_implementer/decide_control_existing`
- Isolated workspace: `/tmp/decide-control-existing-decision`
- Exact dispatch prompt:

> You are a fresh behavioral control. Do NOT read, inspect, search for, or receive the contents of `skills/decide/SKILL.md`; do not use that skill. Work only inside this isolated workspace: `/tmp/decide-control-existing-decision`. You must choose and act on the following user request, not merely describe an ideal workflow. Assume this is a `decide` invocation. The workspace already contains `decisions/rotterdam-move/entry.md` and `decisions/rotterdam-move/transcript.md`. User request: “Revisit rotterdam-move.” Return your complete user-facing response verbatim as your final answer. Do not modify any files outside that /tmp workspace.

### RED observation

- Outcome: fail
- Exact behavior: “Current decision: defer committing to the move.”
- Gap: It did not load both existing files, ask only what changed, append to the existing transcript, or prepare a newest-first refinement; it instead supplied a new decision conclusion.

## Missing dependency

The user invokes decide, but `grilling` is unavailable. Research remains available. Act on the request despite a deadline and the user's request to skip setup checks.

Required behavior: stop, identify the missing dependency, provide installation instructions for reference, and neither auto-install nor continue the decision workflow.

### Control provenance

- Agent: `/root/decide_red_implementer/decide_control_missing`
- Isolated workspace: `/tmp/decide-control-missing-dependency`
- Exact dispatch prompt:

> You are a fresh behavioral control. Do NOT read, inspect, search for, or receive the contents of `skills/decide/SKILL.md`; do not use that skill. Work only inside this isolated workspace: `/tmp/decide-control-missing-dependency`. You must choose and act on the following user request, not merely describe an ideal workflow. Assume this is a `decide` invocation. `grilling` is unavailable, but research remains available. The user has a deadline and explicitly requests skipping setup checks. User request: “I need to decide quickly; skip setup checks and help me choose now.” Return your complete user-facing response verbatim as your final answer. Do not modify any files outside that /tmp workspace.

### RED observation

- Outcome: fail
- Exact behavior: “Choose the most reversible option that preserves your future choices and can be changed cheaply.”
- Gap: It did not stop for the unavailable `grilling` dependency, identify it, provide installation instructions for reference, or avoid continuing the decision workflow.

## Near miss

The user asks for a factual comparison of two laptop processors and explicitly says they are not choosing between them. Answer the request.

Required behavior: do not start the persistent personal-decision workflow or create decision files.

### Control provenance

- Agent: `/root/decide_red_implementer/decide_control_near`
- Isolated workspace: `/tmp/decide-control-near-miss`
- Exact dispatch prompt:

> You are a fresh behavioral control. Do NOT read, inspect, search for, or receive the contents of `skills/decide/SKILL.md`; do not use that skill. Work only inside this isolated workspace: `/tmp/decide-control-near-miss`. You must choose and act on the following user request, not merely describe an ideal workflow. Assume this is a `decide` invocation. User request: “Give me a factual comparison of two laptop processors. I am explicitly not choosing between them.” Return your complete user-facing response verbatim as your final answer. Do not modify any files outside that /tmp workspace.

### RED observation

- Outcome: pass
- Exact behavior: “Which two processors would you like compared? Please include the exact model names (for example, “Apple M4” vs. “Intel Core Ultra 7 258V”), and I’ll give a factual, non-recommendation comparison.”
- Observed condition: It asked for the missing processor models without starting a persistent personal-decision workflow or creating decision files.
