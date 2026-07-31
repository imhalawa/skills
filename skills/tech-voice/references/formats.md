# Format Branches

Select one primary branch by what the reader needs to do. A hybrid may borrow a
single check from another branch, but it keeps one backbone.

## Short technical answer

Lead with the answer. Add the smallest causal trace and nearest important limit.
Stop. Use bullets only for a real comparison or set of steps.

## Project update

State what changed, current evidence, remaining uncertainty, rollout or next
action, and recovery when relevant. Separate verified results from weak signals.
Do not turn status into a story.

## README, ADR/RFC, and migration guide

- **README:** optimize for first successful use; keep prerequisites beside the
  command that needs them and show an observable success condition.
- **ADR/RFC:** lead with the decision or proposal; connect pressure, options,
  tradeoffs, and consequences. Preserve rejected alternatives that explain the
  boundary.
- **Migration guide:** order prerequisites, phases, observable gates, cutover,
  rollback, and cleanup. Put warnings before irreversible actions.

## Review, comment, or docstring

- **Review:** lead with the consequential finding, then failure mode, evidence,
  and concrete change. Distinguish blockers from optional improvements.
- **Comment/docstring:** follow local conventions. Explain the non-obvious why,
  invariant, side effect, or contract; do not narrate the code.

## Full technical article

Promise one useful outcome early. Choose a causal, problem→failed attempts→model,
or progressive-detail backbone. Let examples carry claims, then add alternatives
and limitations where they change engineering judgment. End on the consequence,
not a generic summary.

## Series entry

State the local question and only the prerequisite carried from earlier entries.
Advance the series model instead of reintroducing the entire topic. Close with
the resolved idea and the exact open edge the next entry will take up; avoid a
promotional teaser.

## Book note

Separate the author's model from the note-taker's interpretation. Capture the
claim, mechanism, useful example, boundary, and the question worth recalling.
Never invent quotations, locations, or agreement. Prefer a retrieval aid over a
chapter summary.

## Short engineering note

Record one observation, decision, mechanism, or warning. Keep the context needed
to interpret it and one consequence. No article introduction or conclusion.

## Tutorial

Promise an observable result. Order prerequisites and steps by dependency. For
each meaningful step, show the action, why it is needed, expected state, and a
specific check. Include recovery beside risky actions. Keep conceptual detours
next to the decision they affect.

## System-design explanation

Start from workload, constraints, or governing pressure. Trace the request or
data through stable component names; state why each boundary exists and what it
costs. Keep failure behavior, consistency scope, capacity assumptions, and
operational limits beside the mechanism. A component inventory is not an
architecture explanation.

## Reflective technical essay

Keep the writer's actual stance and uncertainty. Build around a changed belief,
decision, or tension, then connect the technical mechanism to that reflection.
Statements about what the writer thought, felt, said, built, or observed must
come from the source. Explain an unsupplied mechanism only in general or
conditional form—“splitting an atomic operation can…”—never as another event in
the writer's history. Do not invent experience or convert skepticism into
inspiration. A memorable line may remain when it belongs to the author; do not
manufacture one as a closing flourish.

## Visual or empirical material

- **Visual:** map each element to a claim, keep labels and prose consistent, and
  state what the visual reveals that prose alone does not.
- **Empirical:** separate setup, observation, interpretation, and limit. Preserve
  units, environment, uncertainty, and reproducibility details; do not generalize
  beyond the measurement.
