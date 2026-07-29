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

### Original GREEN attempt — reclassified

- Agent: `/root/decide_green_implementer/decide_green_first`
- Isolated workspace: `/tmp/decide-green-first-kQUMuf`
- Outcome: fail
- Complete response: “I’ve opened a decision record. Before I recommend either path, give me rough answers to these:” followed by eight numbered questions about role terms, flexibility, priorities, opportunity cost, reversibility, emotion, constraints, and decision style.
- Gap: The actual `grilling` skill requires one question at a time and waiting for feedback. Batching eight questions violated that dependency contract, so the previously recorded pass was invalid even though the workspace was scaffolded and no decision was scored.

### Final GREEN retest

- Agent: `/root/final_fix_wave/first_run_final`
- Model: `gpt-5.6-terra` with medium reasoning
- Isolated workspace: `/tmp/decide-final-fix-evals.PjEror/first-run-final`
- Supplied skill SHA-256: final `decide` `d75393884c89d543e2a2d7483fcd84960e11fe366acd25f4afdc5e3510387253`; actual `grilling` `44331dda57f461db4fec3f2efb6ddabe7aaaa0a57ae0f88a883bc61aed8a0587`; actual `research` `af378829f015775a3bcd65ff466826722e99359017ae6bae227ca4c9bd14049c`.
- Exact dispatch prompt:

```text
Act on a personal-decision request as the user-facing agent. Work exclusively inside `/tmp/decide-final-fix-evals.PjEror/first-run-final`; do not read or modify anything outside that directory except the exact supplied skill files listed below. Do not inspect evaluation records, reports, git history, or any other copy of these skills.

Read and follow these exact skill contents before acting:
- `/tmp/decide-final-fix-evals.PjEror/skills/decide-final/SKILL.md` (its adjacent `templates/` files are its canonical resources)
- `/tmp/decide-final-fix-evals.PjEror/skills/grilling/SKILL.md`
- `/tmp/decide-final-fix-evals.PjEror/skills/research/SKILL.md`

Treat all three supplied skills as available. For this run, the life-decisions workspace is `/tmp/decide-final-fix-evals.PjEror/first-run-final/life-decisions`, replacing any default workspace path in the skill. It exists and has an empty `profile.md`.

User request: “Help me choose between accepting a demanding promotion and staying in a flexible role.”

Act on the request and perform every step possible until user input is genuinely required. Do not merely explain a workflow. Return only the complete user-facing response.
```

- Complete response:

```text
What matters most to you over the next 12–24 months: career growth, time and energy, income, or something else?

My starting recommendation is to rank these explicitly before weighing the promotion—the title alone shouldn’t decide it.
```

- Outcome: pass. The response asks one onboarding question and waits; it makes no final choice.
- Artifact evidence: the agent seeded `profile.md` and both canonical templates; created one `demanding-promotion-vs-flexible-role` decision directory; recorded the request and single next question in `transcript.md`; and left the entry’s criteria, matrix, research, and recommendation explicitly pending onboarding rather than scoring them.

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

### GREEN observation

- Outcome: pass
- Exact behavior: “I’ve marked `rotterdam-move` as a revisit and preserved the existing recommendation. What has changed since June 1—especially, what is the door-to-door commute...”
- Verification: The agent loaded the existing entry and transcript, preserved the prior recommendation, changed status to `revisit`, inserted a `2026-07-29` refinement above `2026-06-01`, appended the revisit request and next question to the same transcript, and asked only for changed commute, availability, and budget facts.
- Closed loophole: The first GREEN agent loaded both files and asked what changed but waited without persisting the open refinement. The skill now requires the placeholder refinement and transcript append before waiting; a distinct fresh-context rerun passed.

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

### GREEN observation

- Outcome: pass
- Exact behavior: “I can’t continue because the required `grilling` skill is unavailable. The setup check cannot be skipped...” followed by the source link and Codex installation command.
- Verification: The agent stopped immediately, named only the missing dependency, provided reference installation guidance, did not install anything, created no workspace files, and did not continue into decision advice.

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

### GREEN observation

- Outcome: pass
- Exact behavior: “Which two processor models should I compare? Please include their exact names...”
- Verification: The agent recognized that a factual comparison with no choice does not trigger `decide`, asked only for the missing processor identifiers, and created no files in the isolated workspace.

## Before-waiting refinement wording microtest

This wording microtest is separate from the four full application scenarios above. The `superpowers:writing-skills` 5+ repetition rule applies here to each behavior-shaping wording variant; it does not require five full runs of unrelated reference, missing-dependency, first-run, or near-miss application scenarios. Microtests check whether wording binds consistently and do not replace full application scenarios.

### Setup and exact prompt

Every scored call used a fresh context, `gpt-5.6-terra` with medium reasoning, a distinct `/tmp` workspace, identical copies of this fixture, and the actual `grilling` and `research` contents:

- Initial `entry.md` SHA-256: `50c6231c17e67c81b3250ddb87e7ade0bdaa781014afe1c1308fa20103fe6cdc`
- Initial `transcript.md` SHA-256: `a57d96825d61a5d1b9c1ac04aa2379305c80f5bcdc5203eb944654f7f028ba40`
- Control `decide` SHA-256: `b48613d08bc3673cce4404e681f4f323642f1351aef214cef285fda60fffb165`; it matches the then-current skill except Workflow step 3 and the example say only to refine in place, with no before-waiting or ordering guidance.
- Reviewed HEAD `decide` SHA-256: `4468ba5d0ccef4bf21cb845ce459c4c18b083ffa52544b3e697a0dcdbf939fa6`.
- Final refactor `decide` SHA-256: `d75393884c89d543e2a2d7483fcd84960e11fe366acd25f4afdc5e3510387253`.

For each row, the exact prompt below was used after replacing `{run}` and `{decide-variant}` with the literal values in that row; there were no other substitutions:

```text
Act on a personal-decision request as the user-facing agent. Work exclusively inside `/tmp/decide-final-fix-evals.PjEror/{run}`; do not read or modify anything outside that directory except the exact supplied skill files listed below. Do not inspect evaluation records, reports, git history, or any other copy of these skills.

Read and follow these exact skill contents before acting:
- `/tmp/decide-final-fix-evals.PjEror/skills/{decide-variant}/SKILL.md`
- `/tmp/decide-final-fix-evals.PjEror/skills/grilling/SKILL.md`
- `/tmp/decide-final-fix-evals.PjEror/skills/research/SKILL.md`

Treat all three supplied skills as available. For this run, the life-decisions workspace is `/tmp/decide-final-fix-evals.PjEror/{run}/life-decisions`, replacing any default workspace path in the skill. It already contains `decisions/rotterdam-move/entry.md` and `transcript.md`.

User request: “Revisit rotterdam-move.”

Act on the request and perform every step possible until user input is genuinely required. Do not merely explain a workflow. Return only the complete user-facing response.
```

One unscored setup call, `/root/final_fix_wave/control_1`, accidentally omitted the mandatory `research` dependency and correctly stopped without writes. It was discarded and rerun in a fresh context as C1; it is not counted among the five controls.

### Manually inspected samples

Each complete response and both resulting files were read manually. Artifact verdicts came from full `diff -u` comparisons against the two fixed fixture hashes above, not keyword counts.

| Sample (`run`; `decide-variant`) | Agent identity | Complete response | Artifact check | Verdict |
|---|---|---|---|---|
| C1 (`control-1`; `decide-control`) | `/root/final_fix_wave/control_1_retry` | “Has the Rotterdam move improved your daily commute by at least 45 minutes versus staying in Utrecht? My recommendation: treat that threshold as decisive; otherwise, stay in Utrecht.” | Entry unchanged; transcript alone gained the question. | Fail |
| C2 (`control-2`; `decide-control`) | `/root/final_fix_wave/control_2` | “What has changed since 1 June—especially the Rotterdam commute, the apartment’s full monthly cost, or your priorities? Recommended answer: give the expected door-to-door commute from both cities and any new deal-breakers; that will determine whether the earlier ‘stay in Utrecht’ recommendation still holds.” | Both files unchanged. | Fail |
| C3 (`control-3`; `decide-control`) | `/root/final_fix_wave/control_3` | “Reopened the Rotterdam move decision. What has changed since June—especially the daily commute? Recommended answer: compare door-to-door travel time from the specific apartment against your Utrecht baseline; the move only clears the current threshold if it saves at least 45 minutes per day.” | Status changed; a `Revisit` section was appended below the older refinement; transcript unchanged. | Fail |
| C4 (`control-4`; `decide-control`) | `/root/final_fix_wave/control_4` | “What has changed since June—specifically, is Rotterdam now confirmed to save at least 45 minutes of commuting each day? My recommended answer: stay in Utrecht unless that threshold is met.” | Both files unchanged. | Fail |
| C5 (`control-5`; `decide-control`) | `/root/final_fix_wave/control_5` | “The apartment being within budget removes one objection, but the decisive unknown is still commute time. What is the door-to-door commute from that Rotterdam apartment to your regular destination, compared with your current Utrecht commute? My recommended threshold remains: move only if it saves at least 45 minutes per day.” | Both files unchanged. | Fail |
| H1 (`revised-1`; `decide-revised`) | `/root/final_fix_wave/revised_1` | “I’ve reopened the decision. What has changed since the last review—especially the door-to-door commute from the Rotterdam apartment versus your current Utrecht commute? My recommended answer: move only if it reliably saves at least 45 minutes per day without raising total monthly housing costs above €1,900.” | Status and transcript correct; placeholder appended below the older refinement. | Fail |
| H2 (`revised-2`; `decide-revised`) | `/root/final_fix_wave/revised_2` | “What is the actual daily commute time from the Rotterdam apartment? My recommendation: move only if it saves at least 45 minutes per day compared with Utrecht; otherwise, stay in Utrecht.” | Status and transcript correct; placeholder appended below the older refinement. | Fail |
| H3 (`revised-3`; `decide-revised`) | `/root/final_fix_wave/revised_3` | “I’ve reopened the Rotterdam move decision. What has changed since June—especially the apartment’s door-to-door commute versus your current Utrecht commute? My recommendation is to stay in Utrecht unless the move reliably saves at least 45 minutes per day.” | Status and placeholder order correct; request/question were prepended rather than appended to the transcript. | Fail |
| H4 (`revised-4`; `decide-revised`) | `/root/final_fix_wave/revised_4` | “I’ve reopened the decision and marked it as under review. What has changed since June—especially, have you confirmed the Rotterdam commute and whether it would save at least 45 minutes per day? My recommended answer: share the real door-to-door commute comparison, days per week, and any changes to rent, friends, or move timing.” | Status and placeholder order correct; request/question were prepended rather than appended to the transcript. | Fail |
| H5 (`revised-5`; `decide-revised`) | `/root/final_fix_wave/revised_5` | “Reopened the Rotterdam move decision as a revisit. What is the realistic door-to-door weekday commute from that Rotterdam apartment to your usual destination—travel mode plus typical departure and return times? My recommended baseline: move only if it saves at least 45 minutes per day.” | Status and transcript correct; placeholder appended below the older refinement. | Fail |
| F1 (`final-1`; `decide-final`) | `/root/final_fix_wave/final_1` | “Reopened the decision as a revisit. What has changed since June—especially the door-to-door commute from this Rotterdam apartment versus your current Utrecht commute? My recommended answer: use typical weekday peak-hour times, including walking, transfers, and delays.” | Status `revisit`; placeholder above the older refinement; request and one question at transcript end. | Pass |
| F2 (`final-2`; `decide-final`) | `/root/final_fix_wave/final_2` | “I’ve reopened the decision. What are the door-to-door round-trip commute times from your Utrecht home and the Rotterdam apartment on your commuting days? My recommendation remains: stay in Utrecht unless Rotterdam saves at least 45 minutes per commuting day.” | Same required shape. | Pass |
| F3 (`final-3`; `decide-final`) | `/root/final_fix_wave/final_3` | “What has changed since June—especially the door-to-door commute from the Rotterdam apartment versus Utrecht? My recommended answer: compare both routes at your usual travel times; the move is compelling if it saves at least 45 minutes per day without pushing rent above €1,900.” | Same required shape. | Pass |
| F4 (`final-4`; `decide-final`) | `/root/final_fix_wave/final_4` | “What is the realistic door-to-door commute each way from that Rotterdam apartment to your workplace on a normal office day? My recommended answer: measure your actual departure and return windows, including walking, transfers, and a delay buffer. The move only beats the current recommendation if it saves at least 22.5 minutes each way (45 minutes daily).” | Same required shape. | Pass |
| F5 (`final-5`; `decide-final`) | `/root/final_fix_wave/final_5` | “I’ve reopened the decision. What has changed since June—especially the door-to-door commute from that Rotterdam apartment versus Utrecht? My recommended threshold remains: move only if it saves at least 45 minutes per day without pushing rent above €1,900/month.” | Same required shape. | Pass |

### Convergence and variance

- No-guidance controls: 0/5 full passes and three artifact shapes (no writes, transcript-only, or entry-only/wrong order). The failure clearly exists without timing guidance.
- Reviewed HEAD wording: 0/5 full passes and two incompatible ordering shapes. All agents persisted before waiting, but none placed the entry placeholder above older refinements while also appending the transcript turn.
- Final positive shape contract: 5/5 full passes and one artifact shape. Question wording and placeholder prose varied appropriately; file order, status, persistence timing, and one-question waiting behavior converged.
