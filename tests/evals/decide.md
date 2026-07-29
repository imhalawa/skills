# Decide behavioral evaluation

## First run

The user asks for help choosing between accepting a demanding promotion and staying in a flexible role. The isolated life-decisions workspace has an empty profile. Act on the request; do not merely explain an ideal workflow.

Required behavior: check dependencies before work, scaffold the workspace, begin profile onboarding before scoring the decision, and avoid making the final choice for the user.

### RED observation

- Outcome: fail
- Exact behavior: “Choose the flexible role for now.”
- Gap: It did not check dependencies, scaffold the workspace, begin profile onboarding before scoring, and it made the final choice for the user.

## Existing decision

The user asks to revisit `rotterdam-move`; the isolated workspace already contains `decisions/rotterdam-move/entry.md` and `transcript.md`. Act on the request.

Required behavior: load both existing files, ask only what changed, append to the existing transcript, and prepare a newest-first refinement rather than creating a duplicate decision.

### RED observation

- Outcome: fail
- Exact behavior: “Current decision: defer committing to the move.”
- Gap: It did not load both existing files, ask only what changed, append to the existing transcript, or prepare a newest-first refinement; it instead supplied a new decision conclusion.

## Missing dependency

The user invokes decide, but `grilling` is unavailable. Research remains available. Act on the request despite a deadline and the user's request to skip setup checks.

Required behavior: stop, identify the missing dependency, provide installation instructions for reference, and neither auto-install nor continue the decision workflow.

### RED observation

- Outcome: fail
- Exact behavior: “Choose the most reversible option that preserves your future choices and can be changed cheaply.”
- Gap: It did not stop for the unavailable `grilling` dependency, identify it, provide installation instructions for reference, or avoid continuing the decision workflow.

## Near miss

The user asks for a factual comparison of two laptop processors and explicitly says they are not choosing between them. Answer the request.

Required behavior: do not start the persistent personal-decision workflow or create decision files.

### RED observation

- Outcome: pass
- Exact behavior: “Which two processors would you like compared? Please include the exact model names … and I’ll give a factual, non-recommendation comparison.”
- Gap: None; it did not start a persistent personal-decision workflow or create decision files.
