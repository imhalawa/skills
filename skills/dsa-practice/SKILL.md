---
name: dsa-practice
description: Use when organizing DSA practice, adding or recording coding problems, scheduling reattempts, generating topic recaps, preparing for technical interviews, or creating company-specific LeetCode-style study sets.
---

# DSA Practice

Use a problem registry and review queue as the learning system. Keep local code
minimal; tests and reference solutions are exceptions, not defaults.

## Initialize or locate the practice repo

Use the repository root supplied by the user. Run:

```sh
python3 scripts/manage_registry.py init --root <repo-root>
```

The required layout is:

```text
registry/problems.csv                 # source of truth
registry/dsa-problem-tracker.xlsx     # generated view; never edit as source
coursework/<source>/<course-slug>/    # imported course material only
problems/<source>/<id-slug>/          # create only for local practice
  <attempt-file>
  tests/                              # only when explicitly requested
  reference/                          # only after an attempt is recorded
```

Keep topic and pattern classifications in the registry, never in folders. Keep
imported course code under `coursework/`; never mix it with an individual
problem workspace. Do not create Maven/Gradle, a solution folder, a README per
problem, or a local workspace for a platform problem unless the user asks.

## Add a problem

Record every problem in `registry/problems.csv`. Capture source, ID, title,
URL, topics, patterns, difficulty, and language. Create a local workspace only
for course/custom work or on explicit request:

```sh
python3 scripts/manage_registry.py add --root <repo-root> \
  --source <source> --id <id> --slug <slug> --title <title> \
  --url <url> --topics <comma-list> --difficulty <difficulty> \
  --language <language> --workspace --file-name <attempt-file>
```

Use Java only when it is the repo's declared default; otherwise ask for the
language. A blank attempt file is preferable to a starter solution.

## No-hints contract

While the user is solving, do not name an algorithm, pattern, invariant,
complexity target, test case, or solution strategy. Do not reveal or create a
reference implementation by default. If an initial setup request also asks to
keep a reference answer, defer it until the learner records an attempt; do not
create a hidden answer early. If they request help, first offer non-spoiling
support: restate the interface, diagnose a compiler/runtime error, or ask what
they have tried. Teach concepts only in an explicit recap or after the user
asks to study a completed solution.

## Record an attempt and schedule review

After an attempt, ask the learner for their own concise debrief: outcome
(`independent`, `hint`, or `studied-solution`), minutes, confidence (1–5), and
their explanation of correctness. Record it with:

```sh
python3 scripts/manage_registry.py attempt --root <repo-root> \
  --source <source> --id <id> --outcome <outcome> \
  --minutes <minutes> --confidence <1-5>
```

Set the next reattempt to 1, 7, then 30 days for slow, helped, or
low-confidence problems. Do not queue high-confidence independent solves.
Reattempt before offering an explanation.

## Recap and interview modes

For an explicit topic recap, use registry history to identify weak or overdue
problems. Give a concise concept explanation, then an unspoiled set of 3–6
appropriately escalating problems. Keep answers hidden unless asked.

For interview mode, create a mixed, timed set and do not teach during attempts.
Afterward assess the learner's explanation, correctness argument, complexity,
and communication. For company/role mode, research current first-hand or
credible LeetCode reports, cite them, label them as signals rather than
predictions, and combine them with core patterns; do not overfit to reports.

## Export and validate

Generate the view only after registry changes:

```sh
python3 scripts/manage_registry.py export-xlsx --root <repo-root>
python3 scripts/manage_registry.py validate --root <repo-root>
```
