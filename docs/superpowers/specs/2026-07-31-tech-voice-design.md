# Tech Voice Design

## Goal

Create a global, model-invoked `tech-voice` skill that makes every technical
answer simple, precise, and useful while preserving the author's genuine
personality. It must work for ephemeral answers, project artifacts, and
published writing without forcing one template onto all of them.

## Inputs

The design combines three evidence streams:

- the 18-source comparative technical-writing study in `docs/research/`;
- Matt Pocock's skill-design guidance on predictable invocation, context load,
  leading words, branching, and progressive disclosure;
- the conversation-derived user voice profile, with AI-generated material
  explicitly excluded as a voice source.

The governing rule is: use the shortest explanation that preserves the
mechanism and the decision-changing boundary.

## Architecture

Keep the always-loaded path small:

- `skills/tech-voice/SKILL.md` defines the trigger, universal writing contract,
  compact workflow, and progressive-disclosure routing.
- `skills/tech-voice/references/formats.md` contains job-specific guidance for
  chat, project artifacts, articles, tutorials, notes, and reviews.
- `skills/tech-voice/references/voice.md` contains generalized preferences
  derived from user-authored conversation. It stores no private transcript and
  does not imitate typos or chat fragments.
- `skills/tech-voice/agents/openai.yaml` provides minimal interface metadata.

Research remains a separate capability. `tech-voice` requires verification
when a claim is unstable, disputed, high-stakes, uncertain, or explicitly
requested; it does not make every stable explanation browse the web.

## Universal contract

Every technical response should:

1. lead with the answer, action, or governing idea;
2. orient before adding depth;
3. use one deliberate explanatory backbone;
4. keep exact terms stable and explain them near first consequential use;
5. make cause, state transition, or invariant inspectable;
6. place a decision-changing limitation beside the claim it qualifies;
7. use examples, code, diagrams, or tables only when they do technical work;
8. stop when the reader can understand, decide, or act.

These are checks, not mandatory sections. A factual one-liner may satisfy the
contract in one sentence.

## Voice policy

The skill is direct, concrete, compact, plain, candid, natural, and
context-aware. It keeps necessary domain vocabulary but rejects inflated
wording, throat-clearing, fake excitement, corporate fog, academic posturing,
and conspicuously AI-polished filler.

For revisions, preserve the author's argument, personality, and structure
unless they impair correctness or comprehension. Never infer authorial voice
from material the user identifies as generated. Code, commands, identifiers,
quotes, and required formats remain unchanged unless explicitly in scope.

## Format branches

The reference must cover:

- short technical answers and project updates;
- README, ADR/RFC, migration guide, PR review, comment, and docstring;
- full technical article;
- series entry;
- book note;
- short engineering note;
- tutorial;
- system-design explanation;
- reflective technical essay.

The branch is selected by the reader's job, not the filename. Hybrids retain
one primary backbone and borrow only the needed check from another branch.

## Evaluation

Behavioral evidence lives in `tests/evals/tech-voice.md`, outside the deployed
skill. RED controls run without the skill. GREEN runs use fresh contexts and
the exact candidate skill. Each run is inspected for:

- answer-first orientation;
- visible mechanism;
- stable terminology;
- nearby consequential boundary;
- proportional structure and length;
- preservation of supplied facts and genuine voice;
- absence of invented claims and AI-like filler;
- correct branch behavior.

The intensive matrix covers all listed formats plus near misses: nontechnical
conversation, code-only changes, strict templates, verbatim text, and factual
one-liners. Behavior-shaping wording receives at least five fresh-context
repetitions per variant; full format scenarios provide breadth and do not need
five repetitions each.

## Deployment

After repository tests, official validation, behavioral review, and diff
review pass, install the source skill globally for both Codex and Claude Code.
Update the plugin manifest so repository and marketplace installs include it.
Do not derive voice rules from Trace in Time.
