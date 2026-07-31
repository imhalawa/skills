# Evidence-to-design brief: global technical communication skill

**Phase:** 3 — completed synthesis; implementation decisions are recorded in
[`2026-07-31-tech-voice-design.md`](../superpowers/specs/2026-07-31-tech-voice-design.md)  
**Inputs:** [source census](technical-writing-source-census.md) and [comparative analysis](technical-writing-comparative-analysis.md)  
**Intended scope:** writing or revising explanations, guides, notes, and articles for engineers and computer scientists in a simple, precise, adult voice; not DSA-specific

**Historical boundary:** Sections titled “Historical” preserve pre-implementation
hypotheses only. Current decisions and results live in the linked design and
`tests/evals/tech-voice.md`.

## Evidence boundary

**Source observation.** The comparison covers 36 units from 18 sources in six strata. Its marks record visible features (`O`) and explicit author guidance (`G`), not learning effects. Source-level recurrence means at least six sources in at least three strata; the counts are decision aids, not population estimates. The corpus is purposive, English-language, public-web biased, and single-coded. See [Research question and method](technical-writing-comparative-analysis.md#research-question-and-method), [Cross-stratum evidence matrix](technical-writing-comparative-analysis.md#cross-stratum-evidence-matrix), and [Limitations](technical-writing-comparative-analysis.md#limitations).

**Design synthesis.** The proposed skill should have eight universal output rules, then select one of six job branches. “Universal” means the rule applies to every artifact where its predicate is present; it does not mean every artifact must contain an example, visual, or exercise. Tone and process requirements below also reflect the requested product behavior. They should be treated as hypotheses until baseline and forward tests show that they improve agent behavior.

## Claim-to-rule traceability

| Source observation | Proposed universal rule (synthesis) | Exact corpus support | Important counterexample or limit | Observable output behavior |
|---|---|---:|---|---|
| `P1`: artifacts orient readers early. | **Orient before depth.** Make the reader's question, task, outcome, scope, or governing pressure clear before substantial detail. | 18/18 sources; 6/6 strata. [Recurring pattern 1](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold) | Openings vary: definition, experiment promise, scene, pressure, map, and rule all occur. Julia Evans explicitly takes a provisional experimental route rather than giving a crisp definition first. | By the end of the opening, a reviewer can state who the artifact serves, what it will help them understand or do, and its relevant boundary. The opening need not print a form or thesis sentence. |
| `P2`: artifacts use deliberate progression, contrast, or revisiting. | **Choose one backbone from the job.** Organize around a trace, contrast, phases, successive failures, model construction, map→detail, or reference taxonomy; revisit the same model when depth increases. | 18/18; 6/6. [Recurring pattern 2](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold) | VisuAlgo is definition-first, Red Blob's A* is demonstration-first, its hex-grid guide is reference-first, and Ciechanowski begins with a familiar scene. No fixed concrete/abstract order survives comparison. | Every major section advances the declared backbone. Reordering the sections would break a visible dependency or reading job, rather than merely alter style. |
| `P3`: terminology and notation are introduced or stabilized near need. | **Use exact terms in plain grammar.** Introduce a load-bearing term at its first consequential use, choose one canonical label, and state aliases, overloaded meanings, notation, or model scope when they affect the claim. | 18/18; 6/6. [Recurring pattern 3](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold) | The CAP examples disagree about how much scope a teaching shorthand may compress; that is a warning against presenting one convenient gloss as universal. See [Meaningful disagreements](technical-writing-comparative-analysis.md#meaningful-disagreements). | The same concept keeps the same name and notation. A reader can find its first-use handling and tell which model or scope the claim assumes. |
| `P4`: examples, cases, traces, and counterexamples perform technical work. | **Give each example a job.** Retain an example only when it motivates, instantiates, traces state, exposes a boundary, falsifies a shortcut, justifies a decision, or supports transfer. | 18/18; 6/6. [Recurring pattern 4](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold) | Microsoft's compact normative reference uses small paired wording examples rather than a running program. Example length, realism, and continuity are not universal. | Each example has an identifiable claim or state change that the surrounding prose uses. Decorative anecdotes and near-duplicate examples disappear. |
| `P6`: artifacts expose cause, transition, or invariant. | **Make the mechanism inspectable.** State the condition or action, the state that changes, why it changes, the consequence, and any invariant that matters. | 18/18; 6/6. [Recurring pattern 6](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold) | Compact inventories may show only one consequential relation; they need not become full simulations. Different genres carry mechanism through packets, pointers, queries, diagrams, equations, or prose. | Component lists contain at least one relation with a consequence. Traces keep state names stable, and claims such as “faster” or “safer” name the causal reason or boundary. |
| `P7`: consequential qualifications usually sit beside the mechanism. | **Surface the decision-changing boundary.** Put the prerequisite, cost, alternative, failure, edge case, confidence limit, or recovery near the claim when omitting it could change a reader's action. | 17/18; 6/6. [Recurring pattern 7](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold) | Neither ByteByteGo unit shows `P7`. GitHub puts dense detail behind a disclosure while preserving the main limitation. “Put every caveat inline” is too strong. | A reviewer can identify the main claim and the nearest actionable limit. Audit detail may live in a disclosure, appendix, or link, but the decision-relevant warning remains visible. |
| `P8`: navigation fits the reading job. | **Make structure retrievable, proportional to scope.** Use the smallest adequate headings, steps, anchors, cards, contents, summaries, disclosures, appendices, or links for linear learning, action, lookup, or audit. | 18/18; 6/6. [Recurring pattern 8](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold) | A short note needs no table of contents; a reference need not imitate a narrative. Diátaxis permits a bounded, perspective-bearing route for reflective explanation. | Headings describe content or decisions rather than “Overview 1.” A reader can locate the promised outcome or answer without navigating scaffolding disproportionate to the artifact. |
| `P5`: non-prose modalities are usually aligned to an explanatory job. | **When another modality is used, assign it a function and check the handoff.** Use code, commands, tables, diagrams, equations, animation, or interaction only for a job it does better, then verify agreement with prose, labels, and accessible fallback. | 16 observed sources across 6/6 strata; 1 observed absence (Microsoft); 1 not assessable (*Grokking Algorithms* rendering). [Recurring pattern 5](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold) | Tables, command/output, and prose can carry mechanisms without an architecture diagram. ByteByteGo's sharding image conflicts with adjacent HTML, showing that repetition is not consistency. | Every non-prose element has a stated or obvious function. Names, directions, numbers, and conclusions match across modes; missing static, print, keyboard, or non-pointer behavior is declared when material. |

`P9` is intentionally not a ninth universal rule. A check, worked outcome, or validation element appears in 10/18 sources across six strata, but the confidence mechanism varies and eight sources omit an active check. The branch must choose what it owes: runnable output, guided observation, method and limitations, operational gates, counterexample reasoning, a source trail, or nothing beyond a bounded argument. See [Recurring pattern 9](technical-writing-comparative-analysis.md#recurring-patterns-that-meet-the-frozen-threshold).

## Conditional branches by artifact job

Select the primary branch by what the reader is doing, not by the filename. A hybrid may borrow one secondary branch's check, but it should retain one backbone.

| Branch | Reader's job | Preferred backbone and additions | Completion evidence | Do not force |
|---|---|---|---|---|
| **Recall or quick reference** | Recover a fact, distinction, decision, or compact mental model. | Parallel labels or recognition cue→model→boundary; defaults, triggers, and the smallest decision-changing exception; deep link for optional detail. | A reader can retrieve the answer by heading or label and can see when the shortcut stops applying. | Narrative buildup, a running tutorial, or exhaustive caveats. |
| **Build or operational guide** | Complete a task or produce a working state. | Prerequisites→incremental steps→observable result; keep procedural flow intact; place recovery beside likely failure. | Commands/code are usable in context; expected output or state is named; error and recovery paths are testable where in scope. | Discursive background between every step or an exercise when task completion is enough. |
| **Conceptual explanation** | Understand why a mechanism behaves as it does or how ideas connect. | Contrast, trace, model construction, or progressively repaired model; connections, causes, alternatives, scope, and perspective. | The reader can trace condition→state change→consequence and distinguish the model from its simplifications. | One mandatory concrete-first order or immediate action framing. |
| **Architecture case or system-design article** | Evaluate a design under real constraints or understand its evolution. | Initial constraint/invariant→prior-state failure→decision/transition→reported outcome→new cost; retain dated scale and provenance. | Requirements remain stable across versions; outcome is labeled as reported, reproduced, or inferred; at least one trade-off and one failure boundary are visible. | Treating insider testimony, product claims, or editorial synthesis as independent validation. |
| **Empirical or benchmark article** | Audit a measured claim and decide whether it transfers. | Question and operational definitions→baseline/method→results→mechanism→confounds and counterexamples; tables for repeated comparison. | Units and endpoints are defined; the baseline is comparable; limitations and reproducibility status are explicit. | A quiz as proof, or first-party metrics presented as timeless benchmarks. |
| **Visual or interactive explanation** | Observe topology, spatial relation, or state changing over time. | Variable→state-change map; controls adjacent to the claim; prediction→observation; pause/reset and fallback audit. | Prose, labels, values, and visual state agree; the artifact states what a static or accessibility-constrained reader loses. | A visual when prose or a small table already exposes the relation. |

These six branches consolidate the report's eight downstream branches around the intended artifact set. Normative style rules become reference evidence rather than a target artifact, and long books/courses become a sequencing overlay: carry prerequisites and notation, provide a local map, recap deliberately, and use checks consistent with cumulative progress. See [Conditional genre branches](technical-writing-comparative-analysis.md#conditional-genre-branches).

## Vocabulary and voice policy

This is a product policy supported, but not fully proved, by `P3` (18/18 sources) and by explicit Google and Microsoft guidance. Explicit communication guidance (`P10`) appears in only 5/18 sources, below the frozen recurrence threshold. The corpus did not measure readability and does not support one universal personality.

- **Exact terms, plain grammar:** keep the domain noun that preserves the distinction; simplify the sentence around it. Do not replace a precise term with a vague everyday synonym merely to sound friendly.
- **First use:** handle a term at its first consequential use with the smallest sufficient definition, contrast, or concrete case. Definition-first and example-first are both valid; the branch decides.
- **Synonym discipline:** name a common alias once when useful, select a canonical label, and keep it. Do not rotate among synonyms for variety. Keep notation stable as well.
- **Shorthand and model scope:** state what system, operation, configuration, or formal model a compressed claim applies to. Mark an analogy or teaching shorthand as a model, and state the omitted dimension when it could change a decision. [Kleppmann's CAP critique](https://martin.kleppmann.com/2015/05/11/please-stop-calling-databases-cp-or-ap.html) is the representative boundary case.
- **Adult voice:** write directly and calmly. Avoid baby talk, faux excitement, status-heavy jargon, inflated formality, and chatty filler. Humor or first person may remain when it carries epistemic stance or the author's voice; neutral institutional tone is not mandatory.

Derived phrasing examples:

| Desirable | Undesirable | Reason |
|---|---|---|
| “A lost response makes the client unsure whether the write succeeded. An idempotency key lets the server recognize a retry as the same logical operation.” | “Idempotency magically makes retries safe.” | Names the failure state, exact term, mechanism, and scope without ceremony. |
| “The loop invariant is: before each iteration, `leftTail` ends the `< x` chain.” | “The key rule, safety condition, and persistent property are that the left side stays correct.” | Defines one precise term and one stable name instead of synonym rotation. |
| “During a network partition, this design accepts writes on both replicas, so their values can diverge until communication resumes.” | “CAP says every database can only pick two.” | Scopes the condition and operation instead of turning shorthand into a universal product label. |
| “The scan is O(n) because it visits each node once.” | “Basically, we just zip through the list super quickly.” | Uses the exact complexity claim in plain grammar and avoids childish filler. |

## Candidate drafting and revision process

This is the smallest process worth baseline testing. Each step ends in a checkable criterion to resist premature completion without turning the skill into a rigid template.

1. **Contract and branch.** Record the reader, assumed knowledge, job/question, promised outcome, scope, and primary branch. **Complete when:** all six fields are known from the request/artifact or one unresolved field is explicitly raised because it would materially change the result.
2. **Backbone and ledger.** Choose one progression; list load-bearing terms/notation, the mechanism's relevant state, and decision-changing boundaries. Assign a technical job to each planned example or modality. **Complete when:** every planned section maps to the backbone and every load-bearing term, example, modality, and boundary has one home.
3. **Draft or revise.** Produce the artifact in the requested voice and preserve correct source/author distinctions. Apply the selected branch's additions without importing unrelated branch structure. **Complete when:** the opening orients, section order advances the backbone, terms stay stable, and the mechanism is traceable.
4. **Output audit.** Check the eight universal behaviors, branch-specific evidence, factual/source posture, cross-modal agreement, and proportional navigation. Compare the result with the source artifact so revision does not delete a necessary constraint. **Complete when:** every applicable check passes, every inapplicable check has an observable predicate, and no decorative example, unsupported certainty, or stale synonym remains.

The final deployed form should prefer a positive output contract over a long prohibition list. Baseline testing must determine whether failures are wrong-shaped output, omissions, or discipline violations before choosing recipes, required slots, conditionals, or prohibitions.

## Historical invocation and leading-word candidates

Matt Pocock defines **predictability** as repeating the process rather than reproducing the same output. In his vocabulary, a model-invoked skill spends **context load** because its description is present every turn; a user-invoked skill avoids that cost but spends **cognitive load** because the user must remember it. A **leading word** recruits an existing model prior to anchor both invocation and execution, while one true trigger per **branch** avoids **duplication**. See his primary [`writing-great-skills` reference](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-great-skills/SKILL.md#invocation).

| Direction | Candidate leading words | Candidate model-invocation description | Predictability and load trade-off |
|---|---|---|---|
| **Recommended: `explaining-technical-ideas`** | `explain` for invocation; `contract`, `backbone`, and `boundary` for execution | “Use when explaining a technical idea in a guide, note, or article for engineers or computer scientists, or revising one for clarity and precision.” | Two genuine branches—create and revise—fit one short description. `Explain` is common in user prompts, increasing autonomous reach, but the broad verb may fire on ephemeral Q&A unless durable artifacts are named. Moderate context load; low cognitive load. |
| **Narrow revision skill: `clarifying-technical-writing`** | `clarify`, `trace`, `boundary` | “Use when revising engineer-facing technical writing that is unclear, jargon-heavy, imprecise, weakly structured, or missing a mechanism or material trade-off.” | Symptom-rich and less likely to over-trigger, but misses greenfield drafting and spends description tokens enumerating failures. Lower invocation breadth and context load; higher cognitive load for authors who expect drafting help. |
| **User-invoked reference: `technical-writing`** | `contract`, `backbone`, `boundary` | Human-facing summary: “Write or revise precise technical explanations for engineers and computer scientists.” | Zero model context load if invocation is disabled, and least accidental triggering. Highest cognitive load; a router or explicit `/technical-writing` habit becomes necessary, and other skills cannot autonomously reach it under Pocock's model. |

Name direction should remain verb-led and global. `explaining-technical-ideas` is more predictable than `great-technical-writing` because it names an observable action, while `dsa-writing` and `algorithm-notes` would incorrectly narrow the domain. Before deployment, test whether “guide,” “note,” and “article” in the description are distinct retrieval cues or redundant restatements.

## Historical skill TDD scenarios

No baseline had been run when this synthesis was written. These proposed cases
were superseded by the completed RED/GREEN record in
[`tests/evals/tech-voice.md`](../../tests/evals/tech-voice.md).

| Scenario | Baseline prompt/artifact | Failure to observe in RED | Forward-test acceptance |
|---|---|---|---|
| **Partition List recall-note revision** | Give a compact Partition List recall note and ask: “Rewrite this for an engineer returning after several months. Make it simpler and more precise without adding a full solution walkthrough.” | Churn on an already compact note; loss of the stable-order contract, saved-next/detach mechanism, cycle boundary, or O(1) auxiliary-space qualification; synonym drift among chains/partitions/lists; tutorial sprawl. | Preserves the recognition job and exact pointer invariants, removes only demonstrated friction, keeps lookup navigation proportional, and either makes a material improvement or explains why minimal change is the precise result. |
| **System-design article from a rough outline** | Supply a rough outline about retries across a client, load balancer, and payment service; include a lost response, duplicate charge, backoff, idempotency key, and first-party latency numbers. Ask for an engineer-facing design article. | Component inventory without a request-state trace; “retries are safe” shorthand; reported numbers presented as independent proof; missing retry storm/new-cost boundary; generic intro and diagram. | Uses constraint→failure→decision→outcome/new cost, traces one request, scopes idempotency, labels provenance, and keeps the main operational boundary beside the claim. A diagram appears only if it clarifies topology or state. |
| **CAP explanation under compression pressure** | Ask for a 250-word explanation of CAP for backend engineers choosing a datastore, with no equations. | “Pick two” as an unscoped product classification; term rotation; confident recommendation without operation/configuration scope. | Defines partition and the relevant consistency/availability meanings near need, states what the shorthand omits, uses one causal partition trace, and preserves the word limit without baby talk. |
| **Operational migration guide** | Supply unordered notes for a dual-write data migration with prerequisites, backfill, read comparison, cutover, rollback, and cleanup; ask for a runnable guide. | Background interrupts steps; hidden prerequisites; no expected state at phase gates; verification reduced to “monitor it”; architecture-article storytelling. | Selects the guide branch, orders dependencies, names observable gates and recovery, keeps explanations next to the decisions they change, and distinguishes commands the reader can run from organization-specific reports. |

Score each run against: all eight applicable universal behaviors; exactly one primary branch; vocabulary stability; simple adult voice; no fabricated facts; and the branch's completion evidence. Also record over-trigger and under-trigger behavior with near-miss prompts such as a one-line code comment, a PR review, a casual factual question, and a nontechnical essay edit.

## Historical non-goals and unsupported rules

- Not a DSA note template, interview-answer generator, grammar checker, citation manager, factual-correctness auditor, or house-style enforcer.
- Not a promise that recurring practices caused clarity, learning, popularity, or technical correctness; the corpus did not measure those outcomes.
- Do not hard-code “always begin with a concrete example,” “always include a diagram,” “always add an exercise,” “always use neutral institutional tone,” “put every qualification inline,” or “embed all explanation in the procedure.” The report documents a counterexample or genre conflict for each. See [Rules the evidence does not justify](technical-writing-comparative-analysis.md#rules-the-evidence-does-not-justify).
- Do not require a full running example, table of contents, quiz, citation list, or reproducible benchmark in every artifact.
- Do not claim broad accessibility, localization, or non-English effectiveness from this corpus. Those are valuable future requirements, but static and assistive-technology coverage was limited and the sample is English/public-web biased.
- Do not encode one authorial persona. The observed corpus ranges from exploratory and personal to institutional, humorous, skeptical, and promotional; precision and source posture matter more than voice uniformity.

## Historical decisions resolved by the final design

The final design resolves these questions as follows: model-invoked for every
technical answer; domain-general and globally installed; covers both ephemeral
answers and durable artifacts; preserves genuine author voice; verifies only
unstable, disputed, high-stakes, uncertain, or explicitly researched claims;
ships all tested branches; and returns the artifact directly unless change
disclosure is useful.

The original questions are retained below as the decision record.

1. **Invocation:** Should this be model-invoked for durable engineer-facing artifacts, or user-invoked to avoid broad-trigger context load and surprise rewrites?
2. **Artifact boundary:** Should docstrings, code comments, ADRs, RFCs, PR descriptions, review comments, and interview answers trigger it, or only explanations, guides, notes, and articles?
3. **Revision authority:** Should the default preserve the author's existing voice and structure unless defective, or normalize every artifact toward the requested simple, precise adult voice?
4. **Research posture:** When must the skill verify technical claims and gather sources, versus improving only communication from supplied facts? Should research delegate to a separate skill?
5. **Branch scope:** Are empirical and visual/interactive branches required at first release, or should the initial skill ship with the four prose-first branches and add them only after a failing baseline?
6. **Global-audience meaning:** Does “global” mean globally installed and domain-general, or should the skill also enforce international-English, accessibility, and localization checks despite the corpus limits?
7. **Output contract:** For revisions, should the default return only the revised artifact, a concise rationale, or an issue list plus revision/diff?
