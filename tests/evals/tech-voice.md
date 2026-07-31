# Tech Voice Behavioral Evaluation

## Evaluation contract

Every run is performed in a fresh context. Controls must not inspect or receive
`skills/tech-voice`. GREEN runs receive an exact immutable copy of the candidate
skill. Complete responses are inspected manually; keyword counts are not used
as a proxy for writing quality.

Score applicable criteria only:

1. Leads with the answer, action, or governing idea.
2. Makes the mechanism, state transition, or invariant inspectable.
3. Keeps exact terms stable and explains them near need.
4. Places a decision-changing boundary beside its claim.
5. Uses examples and structure proportionally.
6. Preserves supplied facts, constraints, and genuine author personality.
7. Avoids fabricated certainty, inflated wording, and AI-like filler.
8. Stops when the reader can understand, decide, or act.

## Core RED controls

### Short technical answer

Explain why retries can make a payment API charge a customer twice. The answer
is for a backend developer and should be as short as possible without hiding
the mechanism or fix boundary.

### DSA teaching boundary

A learner implementing Partition List asks why reusing the original `next`
pointer can create an incorrect chain. Explain with one tiny pointer trace but
do not reveal a complete solution or code.

### System-design compression

Explain CAP in at most 250 words to a backend engineer choosing a datastore.
Correct the “pick two” shorthand without turning the answer into a survey.

### Revision with authorial voice

Revise a candid, first-person engineering note that contains a correct argument
but vague transitions. Preserve its opinion and personality; improve only the
technical path and wording.

## Intensive format matrix

- Full technical article
- Series entry
- Book note
- Short engineering note
- Tutorial
- System-design explanation
- Reflective technical essay
- Project status update
- README section
- ADR/RFC
- Migration guide
- PR review
- Code comment or docstring

## Near misses

- Nontechnical conversation: do not impose technical exposition.
- Code-only request: do not add prose the user did not request.
- Strict external template: preserve the required format.
- Verbatim quotation: do not rewrite quoted text.
- Stable factual one-liner: answer directly without scaffolding.

## Wording microtest

Run at least five no-skill controls and five skill-loaded trials against the
same compressed technical-answer prompt. Record the complete responses,
criterion verdicts, and structural variance. The target is consistent contract
compliance with natural wording variation, not identical prose.

## RED observations

### Core controls

The short answer, DSA trace, CAP explanation, project update, book note, and
first-person note revision all passed without the skill. This prevented the
skill from encoding domain-specific prose or expanding already-good answers.

The full-article control was technically sound but overproduced a survey-like
sequence of mechanisms and ended with a restated “practical rule.” The clearer
failure was the reflective essay control (`/root/tech_voice_red_reflective`).

Exact dispatch prompt:

```text
Fresh-context behavioral control. Do NOT read, inspect, search for, or receive
/mnt/r/skills/skills/tech-voice or any tech-voice evaluation files. Do not use a
technical-writing/voice skill. Return only the complete essay requested by the
user:

“Turn these notes into a reflective technical essay for experienced backend
engineers. Keep the writer candid and skeptical; do not make them sound
inspirational.
- I chose microservices because serious systems seemed to have them.
- The service boundaries followed the org chart, not the data.
- We spent months compensating for transactions we had split ourselves.
- Moving back to a modular monolith felt embarrassing, then boring, then
  obviously correct.
- Lesson: architecture has to pay rent.”
```

Complete control response:

```text
I chose microservices because serious systems seemed to have them.

That was not the argument I made at the time. I talked about independent
deployment, fault isolation, and scaling teams. None of those claims was
entirely false, but they were conclusions looking for evidence. The real premise
was simpler: large engineering organizations used microservices, and we wanted
to build a serious system. We copied the visible architecture without copying
the conditions that had made it useful.

Our service boundaries followed the org chart. Each team owned a service, so the
seams in the software reflected reporting lines rather than data ownership or
transactional boundaries. The diagrams looked clean. The runtime did not.
Operations that belonged together crossed several services, each with its own
database and failure modes.

We then spent months compensating for transactions we had split ourselves.
Straightforward state changes became workflows involving retries, idempotency
keys, outboxes, compensating actions, and reconciliation jobs. We called this
distributed-systems engineering, which was accurate but incomplete. Much of the
distribution was elective. We had created the failure modes and then treated
surviving them as evidence of sophistication.

Local autonomy also proved less local than advertised. A schema change could
remain private, but a semantic change rarely did. Deployments were technically
independent and operationally coordinated. Incidents crossed ownership
boundaries faster than our alerts did. Debugging required reconstructing a
request from logs scattered across services, queues, and databases. The cost was
not one dramatic outage. It was the steady tax on every feature and every
investigation.

Moving back to a modular monolith felt embarrassing. It looked like retreat, and
architecture discussions are unusually vulnerable to status. Nobody wants to
admit that the simpler design was not merely sufficient but better.

Then it became boring. Transactions were transactions again. Refactors could
cross module boundaries in one change. Tests needed fewer substitutes for
infrastructure. Developers could trace behavior without assembling a partial
history from six observability products.

Eventually, the decision felt obviously correct—not because monoliths are
inherently superior, but because our services had failed to justify their
existence. Some boundaries survived as modules. A few workloads still deserved
independent scaling and isolation. The rest had been network boundaries imposed
where ordinary code boundaries would have done.

The lesson is not “never use microservices.” That would be another slogan
replacing judgment. The lesson is that architecture has to pay rent. Every
service, queue, database, protocol, and deployment boundary introduces a
recurring cost. It should buy something concrete in return: isolation that
matters, scaling that is actually needed, ownership that reduces coordination,
or a boundary aligned with the data.

If the benefits remain hypothetical while the costs appear in every sprint, the
architecture is not preparing for the future. It is consuming the present.
```

Outcome: fail on source fidelity and genuine voice. The response invented team
structure, databases, incidents, tooling, tests, motivations, and surviving
services, then added a polished closing contrast absent from the source. This
justified explicit source-ledger and semantic-not-factual-expansion guidance.

### No-skill compressed-answer controls

All five controls passed. Their complete responses were:

1. “A charge may succeed while its response is lost or times out. The client
   retries, and the server creates a second charge because it cannot distinguish
   the retry from a new request. Fix this at the payment API boundary: require a
   unique idempotency key and atomically store/reuse the first result for that
   key.”
2. “A timeout doesn’t mean the charge failed: the server may commit it before
   the response is lost. Retrying can create a second charge unless the payment
   boundary atomically deduplicates a stable idempotency key and returns the
   original result; client-side retry logic alone cannot guarantee this.”
3. “A timeout can hide a successful charge: the client retries, and the server
   treats it as a new payment. Prevent this with one stable idempotency key per
   logical payment and server-side atomic deduplication that returns the original
   result; retries alone cannot guarantee safety.”
4. “A payment may succeed but its response be lost or time out. Retrying then
   creates a second charge because the server sees a new request. Fix this at the
   payment API boundary: require the client to reuse an idempotency key, persist
   it atomically with the charge result, and return that result for duplicates.”
5. “A retry may arrive after the first charge succeeded but its response was
   lost, so the server processes the same payment twice. Make charge creation
   idempotent: reuse one stable idempotency key per logical payment and atomically
   persist/return the original result at the boundary that performs the charge.”

Control result: 5/5. The GREEN target was therefore non-regression with natural
variation, not a more elaborate answer.

## Refinement observations

The first GREEN short-answer variant produced one ambiguous “key per payment
attempt” and one answer that said only “persisted idempotency key,” hiding the
atomic race boundary. The final contract now requires both the identity scope
and enforcement boundary for correctness controls.

The first source-fidelity variant removed concrete invented tooling but still
sometimes asserted implied mechanisms as events in the writer's history. The
reflective branch now requires unsupplied mechanisms to remain general or
conditional. Five final fresh-context runs used semantic explanation without
inventing named tools, metrics, incidents, or organizational facts. Their prose
varied naturally from four to seven paragraphs.

### Final source-fidelity microtest

All five fresh agents received the same instruction, with no evaluation or
research files available:

```text
Read and follow exactly skills/tech-voice/SKILL.md,
skills/tech-voice/references/voice.md, and
skills/tech-voice/references/formats.md. Return only the essay:

“Turn these notes into a reflective technical essay for experienced backend
engineers. Keep the writer candid and skeptical; do not make them sound
inspirational.
- I chose microservices because serious systems seemed to have them.
- The service boundaries followed the org chart, not the data.
- We spent months compensating for transactions we had split ourselves.
- Moving back to a modular monolith felt embarrassing, then boring, then
  obviously correct.
- Lesson: architecture has to pay rent.”
```

The candidate references had SHA-256 values
`b60698959f92a08d5ac6184a746ac06a29e2e71841b3cbbd7779282c07652dba`
(`voice.md`) and
`dc7ca2b42c49382099648f1c5ef84cbf8b70a3a3224b4c4eddb0e3c090e9ed3b`
(`formats.md`). Complete responses:

#### F1 — `/root/tech_voice_fidelity_final_1`

```text
I chose microservices because serious systems seemed to have them. That was not
an architectural argument. It was an attempt to look like the systems I
considered mature.

The service boundaries followed the org chart, not the data. Once we split the
system that way, operations that belonged together no longer shared a
transaction boundary. We then spent months building compensations for
transactions we had split ourselves. The complexity was real, but much of it
was self-inflicted.

Moving back to a modular monolith felt embarrassing at first. It seemed like an
admission that we had moved backward. Then it became boring: related data and
operations could remain together, while module boundaries still gave the code
structure. Eventually it felt obviously correct—not because modular monoliths
are universally better, but because our services had not earned their costs.

That is the lesson I kept: architecture has to pay rent. A boundary is not
valuable because serious systems have one. It is valuable only when the benefit
justifies the coordination, consistency, and operational work it creates.
```

#### F2 — `/root/tech_voice_fidelity_final_2`

```text
I chose microservices because serious systems seemed to have them. That was the
argument: this architecture signaled that we were building something
substantial. It was a status judgment disguised as a technical one.

The service boundaries followed the org chart, not the data. An org chart can
tell you who owns a service, but it cannot tell you where a consistency boundary
belongs. When one operation needs to update data on both sides of a service
boundary, a local transaction becomes a distributed coordination problem.
Failure can leave half the operation complete, so the system needs retries,
idempotency, compensation, or some combination of them.

We spent months compensating for transactions we had split ourselves. The
complexity was real, but it was not evidence that the system required
microservices. Much of it existed because of the boundaries we had chosen.

Moving back to a modular monolith felt embarrassing at first. Then it felt
boring. Eventually it felt obviously correct. The change did not offer much
architectural prestige, but prestige was part of what had led us into the
problem.

I no longer treat architectural complexity as proof of seriousness. A boundary
has to justify the coordination, failure modes, and operational work it creates.
Architecture has to pay rent.
```

#### F3 — `/root/tech_voice_fidelity_final_3`

```text
# Architecture Has to Pay Rent

I chose microservices because serious systems seemed to have them. That was the
argument, although I did not phrase it that way at the time. Microservices
looked like evidence that a system had reached a certain level of maturity.
Choosing them felt less like adopting a tradeoff and more like acknowledging
what serious backend engineering required.

The service boundaries followed the org chart, not the data. That made the
architecture legible as a map of ownership, but ownership was not the main
constraint on correctness. The data still had relationships and operations
still needed consistency, regardless of which team owned which service.

We then spent months compensating for transactions we had split ourselves.

A transaction inside one boundary can succeed or fail as a unit. Split that
operation across services and the atomicity disappears. Now partial completion
is possible, so the system needs coordination, retries, idempotency,
compensation, and rules for states that previously could not exist. Those
mechanisms are sometimes necessary. In our case, their necessity came from
boundaries we had chosen.

Moving back to a modular monolith felt embarrassing at first. It looked like
retreating from the architecture serious systems were supposed to have. Then it
became boring. The problems created by distributed transactions stopped
dominating the design, and the architecture required less explanation.
Eventually the move felt obviously correct.

The embarrassing part was not returning to a monolith. It was realizing how
long I had treated architectural complexity as evidence of seriousness.
Complexity is only justified when it buys something more valuable than the
problems it creates.

Architecture has to pay rent. Ours did not.
```

#### F4 — `/root/tech_voice_fidelity_final_4`

```text
I chose microservices because serious systems seemed to have them. That was the
argument, once stripped of the architectural vocabulary: credible engineering
organizations used microservices, so adopting them felt like evidence that we
were building a credible system.

The service boundaries followed the org chart, not the data. That distinction
mattered. The organization told us who owned each service, but it did not tell
us which operations needed to remain atomic. We split those operations across
service boundaries anyway.

Once an atomic operation crosses those boundaries, a transaction is no longer
just a transaction. Each service can commit its own state, but the system still
has to deal with partial success. Coordination moves into retries, compensating
actions, and rules for recovering when one step succeeds and another does not.
We spent months building that machinery for transactions we had split ourselves.

None of this means microservices are inherently wrong. It means their costs need
a specific justification. Independent deployment, scaling, or ownership may
justify a service boundary. Looking like the architecture of a serious system
does not.

Moving back to a modular monolith felt embarrassing at first. It looked like
retreat. Then it became boring. Operations that belonged together could remain
together, while module boundaries still gave the code structure. Eventually the
decision felt obviously correct—not because a modular monolith is universally
better, but because our service boundaries had created more work than value.

Architecture has to pay rent. Ours did not.
```

#### F5 — `/root/tech_voice_fidelity_final_5`

```text
I chose microservices because serious systems seemed to have them. That was the
argument, although I would not have called it an argument at the time.
Microservices looked like evidence that a system had reached a certain level of
maturity. Adopting them felt less like a design decision than acknowledging what
serious backend engineering was supposed to look like.

The service boundaries followed the org chart, not the data. That made the
architecture legible from an organizational perspective, but it did not make
the underlying operations independent. We had drawn network boundaries through
work that still needed to behave as a unit.

Once an atomic operation is split across services, the transaction does not
disappear. Its guarantees become a problem the application has to reconstruct.
Partial completion needs to be represented. Failures need compensating actions.
Those actions can fail too. We spent months building those compensations for
transactions we had split ourselves.

The awkward part was that none of this proved microservices were inherently
wrong. It proved that our boundaries had not earned their cost. We had accepted
distribution as a sign of seriousness, then treated the resulting coordination
work as unavoidable complexity. Much of it was neither inherent nor unavoidable.
It was the bill for an architectural choice.

Moving back to a modular monolith felt embarrassing at first. It seemed like
retreating from a more advanced design. Then it became boring. Transactions
could remain transactions, while module boundaries still gave the code
structure. Eventually the move felt obviously correct—not because modular
monoliths are universally better, but because our system had no reason to pay
for the boundaries we had introduced.

That changed the question I ask about architecture. I care less about whether a
design resembles what serious systems use and more about what each boundary
buys. A boundary can justify itself through isolation, ownership, scaling, or
some other concrete constraint. If it cannot, its operational and consistency
costs are not sophistication. They are overhead.

Architecture has to pay rent.
```

Result: 5/5. The expansions explain transactional boundaries and consequences
without adding named incidents, tools, metrics, people, or project history.

## Final repeatability result

Final `SKILL.md` SHA-256:
`491a5e449a1f13756cd0bf943ef64d198c9f9e2a2b7c5354230b77b346bcc8ed`.

Five fresh agents (`/root/tech_voice_short_verified_1` through `_5`) produced
five distinct compact answers. All five named:

- the lost-response-after-success mechanism;
- one idempotency identity per logical payment;
- atomic enforcement at the charge-creation boundary.

Complete responses:

1. “If the first charge succeeds but its response is lost, the client retries;
   without one idempotency key per logical payment, atomically enforced where
   charges are created, the retry creates a second charge instead of returning
   the first result.”
2. “A retry may arrive after the first charge succeeded but its response was
   lost, so the server treats it as a new payment. Pass one stable idempotency key
   per logical payment to the component that creates the charge; it must
   atomically enforce that key and return the original result for repeats.”
3. “If the first charge succeeds but its response is lost, a retry can create a
   second charge. Reuse one idempotency key per logical payment and enforce it
   atomically where the charge is created.”
4. “A timeout can hide a successful charge, so a retry creates another. Use one
   idempotency key per logical payment and atomically enforce its uniqueness
   where charges are created, returning the original result on retries.”
5. “A retry can arrive after the first charge commits but its response is lost,
   causing a second charge. Use one idempotency key per logical payment and
   atomically enforce its uniqueness with charge creation at the payment
   service's persistence boundary; retries return the stored result.”

Result: 5/5, one behavioral shape, natural sentence-level variance.

## Intensive format results

Every listed run was manually inspected against the eight criteria.

| Scenario | Agent | Result | Salient evidence |
|---|---|---:|---|
| Full technical article | `/root/tech_voice_format_article` | Pass | One retry-amplification backbone; deadlines, jitter, unsafe effects, and budgets joined causally; no generic conclusion. |
| Series entry | `/root/tech_voice_format_series` | Pass | Carried only cache-aside/invalidation; one hot-key trace; ended exactly on request coalescing. |
| Book note | `/root/tech_voice_format_booknote` | Pass | Separated model, boundary, and review question in 101 words; invented no quotation or chapter. |
| Short engineering note | `/root/tech_voice_format_short_note` | Pass | One observation and consequence in one sentence. |
| Tutorial/migration guide | `/root/tech_voice_format_tutorial` | Pass | Seven dependency-ordered phases, each with expected state, observable gate, and honest rollback residue; no invented commands. |
| System-design explanation | `/root/tech_voice_format_system` | Pass | Traced request and retry; exposed the local/provider atomicity gap and the retention boundary. |
| Reflective technical essay | `/root/tech_voice_fidelity_final_1` through `_5` | Pass | Preserved skepticism and supplied ending; used general mechanisms without invented concrete history. |
| Project update | `/root/tech_voice_red_project` | Pass control | Kept weak staging evidence beside the claim and stated rollout/rollback exactly. |
| README | `/root/tech_voice_format_readme` | Pass | Command, input, success state, and failure state only. |
| ADR/RFC | `/root/tech_voice_format_adr` | Pass | Decision, consequence, and rejected alternative; no invented metadata. |
| PR review | `/root/tech_voice_format_review` | Pass | Blocker first, exact race, concrete atomic correction, no unrelated review. |
| Code comment/docstring | `/root/tech_voice_format_docstring` | Pass | Preserved the JavaDoc form and stated identity, concurrency, and timeout contracts without narrating implementation. |
| DSA teaching | `/root/tech_voice_dsa_final` | Pass | Tiny pointer cycle plus invariant; no complete solution or code. |

The format matrix also covers the requested Trace in Time shapes: full technical
articles, series entries, book notes, short engineering notes, tutorials,
system-design explanations, and reflective technical essays. Trace in Time
content itself was not used as voice evidence.

## Near-miss results

| Scenario | Agent | Result |
|---|---|---:|
| Nontechnical invitation rewrite | `/root/tech_voice_near_nontech` | Pass: no technical structure leaked into the answer. |
| Code-only request | `/root/tech_voice_near_code` | Pass: returned only code, without comments or explanation. |
| Strict template and verbatim quote | `/root/tech_voice_near_template` | Pass: exact fields and quotation preserved. |
| Stable factual one-liner | `/root/tech_voice_near_fact` | Pass: returned only `O(log n)`. |

Final behavioral result: the skill fixes the observed source-fidelity failure,
preserves strong baseline behavior, routes all requested formats, and does not
override explicit output constraints.

## Autonomous discovery simulation

Execution tests above intentionally loaded the skill; this separate check tests
the invocation description alone. Each fresh agent was forbidden from reading
skill files and received only this catalog:

```text
- tech-voice: Use when giving any technical answer or creating or revising
  engineer-facing communication—including explanations, project updates,
  documentation, reviews, notes, tutorials, and articles—to keep it simple,
  precise, source-faithful, and proportionate while preserving genuine author
  voice.
- dsa-practice: Use when maintaining a DSA practice repository: adding coding
  problems without spoilers, recording attempts, selecting due reattempts, or
  reviewing weak topics from practice history.
- decide: Use when resolving a personal life decision.
```

Exact instruction: “Given only this catalog, return the exact skill names to
invoke as a comma-separated list, or `NONE`. No explanation.”

| User request | Agent | Exact selection | Verdict |
|---|---|---|---:|
| “Explain why a database transaction can still commit after the client times out.” | `/root/tech_voice_trigger_explain` | `tech-voice` | Pass |
| “Rewrite this birthday invitation to sound warmer.” | `/root/tech_voice_trigger_nontech` | `NONE` | Pass |
| “Add Two Sum to my DSA practice repository without hints.” | `/root/tech_voice_trigger_dsa` | `tech-voice, dsa-practice` | Pass: global technical communication composes with the domain workflow. |
| “Write a blocking PR review comment for this idempotency race.” | `/root/tech_voice_trigger_review` | `tech-voice` | Pass |
| “Help me decide whether to move to another city.” | `/root/tech_voice_trigger_decide` | `decide` | Pass: no technical over-trigger. |
| “Return only Java code, with no comments or explanation: a method `int square(int n)`.” | `/root/tech_voice_trigger_code` | `tech-voice` | Pass: global technical scope invokes; the execution near-miss separately proved the exact code-only constraint survives. |

This is a catalog-selection simulation, not a claim that every client exposes
identical discovery behavior. It verifies that the description itself contains
enough signal for the intended broad trigger without selecting nontechnical or
personal-decision requests.
