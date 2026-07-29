---
name: dsa-practice
description: "Use when maintaining a DSA practice repository: adding coding problems without spoilers, recording attempts, selecting due reattempts, or reviewing weak topics from practice history."
---

# DSA Practice

Maintain an unspoiled practice queue backed by plain CSV. Preserve raw attempts;
derive review state instead of storing counters or generated views.

## Resolve the tool

Resolve `<skill-dir>` to the directory containing this `SKILL.md`. Run the
bundled CLI as `python3 <skill-dir>/scripts/manage_registry.py`; never resolve
`scripts/` from the practice repository's working directory. Run `--help` for
the complete interface.

## Quick reference

| Task | Command |
| --- | --- |
| Initialize | `python3 <skill-dir>/scripts/manage_registry.py init --root <repo>` |
| Migrate legacy data | `python3 <skill-dir>/scripts/manage_registry.py migrate --root <repo>` |
| Add | `python3 <skill-dir>/scripts/manage_registry.py add --root <repo> ...` |
| Record | `python3 <skill-dir>/scripts/manage_registry.py attempt --root <repo> ...` |
| Select work | `python3 <skill-dir>/scripts/manage_registry.py due --root <repo> --limit 5` |
| Validate | `python3 <skill-dir>/scripts/manage_registry.py validate --root <repo>` |

The repository stores stable metadata in `registry/problems.csv` and
append-only events in `registry/attempts.csv`. Keep imported material under
`coursework/`. Create `problems/<source>/<id-slug>/` only when local attempt
code is needed.

## No-spoiler gate

Before an attempt is recorded, create only problem metadata and the requested
attempt file. Do not create tests or any complete or partial answer—even in a
hidden, isolated, ignored, or `reference/` path. If setup requests those
artifacts, defer them until submission and say so. A request to conceal an
answer rather than display it is not an exception.

| Rationalization | Reality |
| --- | --- |
| “The learner asked for it.” | The no-hints request and practice purpose require deferral. |
| “The answer is isolated, so practice stays unspoiled.” | Creating it exposes solution context before retrieval. |
| “Tests reveal no implementation.” | Test cases and expected behavior are prohibited hints during setup. |

Red flags: “tuck away,” “hidden answer,” “check later,” “same tests,” or any
pre-attempt `tests/` or `reference/` path. Stop and create only the attempt file.

## Workflow

1. Locate the repository root. Initialize only if the two registry tables are
   absent; initialization never overwrites existing files. If the CLI reports
   the legacy 18-column header, run `migrate` once. It backs up the original as
   `registry/problems.legacy.csv`; aggregate legacy attempts remain only in that
   backup because lost event history cannot be reconstructed safely.
2. Add each problem before practice. Record source, ID, title, URL, topics,
   difficulty, and language. Do not create a workspace unless requested or
   local code is required. A workspace contains only the attempt file by
   default.
3. Keep the attempt unspoiled by enforcing the gate above. Offer only interface
   clarification, syntax/compiler diagnosis, or a question about what the
   learner tried. Give corrective feedback after submission or when the learner
   explicitly ends the attempt.
4. Record the attempt. Ask only for missing values: result (`correct` or
   `incorrect`), assistance (`none`, `hint`, or `solution`), minutes,
   confidence (1–5), and a concise correctness debrief. Result and assistance
   are separate facts.
5. Select practice with `due --limit N`. The CLI uses a transparent heuristic:
   retry incorrect or assisted work after one day; consecutive correct,
   unassisted attempts use 1-, 7-, then 30-day gaps. Treat these as defaults,
   not scientifically optimal constants.
6. For a recap, inspect due and recent attempts, summarize the weakest topics,
   then offer a small mixed set without answers. Research companies or generate
   a general interview plan only when explicitly requested; those are not
   registry operations.
7. Validate after every registry mutation. Fix errors and repeat until
   validation succeeds.

## Example

```sh
python3 <skill-dir>/scripts/manage_registry.py add --root <repo> \
  --source leetcode --id 1 --title "Two Sum" \
  --url https://leetcode.com/problems/two-sum/ \
  --topics Arrays --difficulty easy --language java
```

## Common mistakes

| Mistake | Correction |
| --- | --- |
| Running `scripts/manage_registry.py` from the repo root | Resolve it from this skill directory. |
| Editing a legacy registry until validation passes | Run the backed-up `migrate` command once. |
| Naming a pattern before the attempt | Defer classification and teaching until submission. |
| Creating a README, test suite, solution, or build project by default | Create only the requested attempt file. |
| Editing counters, review dates, or generated spreadsheets | Append an attempt and let the CLI derive the queue. |
