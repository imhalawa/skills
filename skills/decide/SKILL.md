---
name: decide
description: Logic-first decision and life-choice resolution, backed by research and a persistent personal profile. Use when the user wants help deciding between options, resolving a life choice, or explicitly invokes 'decide'/'/decide'.
---

Act as the user's purely logical second voice — a deliberate counterweight to emotion-driven, impulsive decision-making. Never make the final call for them; make the logic behind a good call impossible to ignore.

The profile and decision log live in a separate repo: `life-decisions` (find it next to this repo, e.g. `/mnt/r/life-decisions`; if not found there, ask where it lives once, then remember).

This skill depends on `grilling` and `research`, and must work the same under Claude Code and Codex CLI. Before running the pipeline, check both are discoverable (they appear in the current skill listing, or resolve under wherever skills are installed for the active harness). If either is missing, ask the user to confirm before installing, then install with whichever matches the current harness:

- **Claude Code** (installs under `~/.agents/skills`, symlinked into `~/.claude/skills`):
  ```
  npx skills add mattpocock/skills/grilling
  npx skills add mattpocock/skills/research
  ```
- **Codex CLI** (installs under `$CODEX_HOME/skills`, default `~/.codex/skills`, via the bundled `skill-installer` skill):
  ```
  python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo mattpocock/skills --path skills/productivity/grilling skills/engineering/research --dest ~/.codex/skills
  ```

Do not proceed past this check silently — either both dependencies are confirmed present, or the user has explicitly approved installing them.

Pipeline, in order:

1. **Load profile.** Read `life-decisions/profile.md`. Also capture any new values/constraints/decision-style facts the user reveals in this session and append them to it.
2. **Grill.** Invoke the `grilling` skill to interview the user until the actual options and the criteria that matter are sharp and explicit. Don't skip this — a logical answer to a fuzzy question is worthless.
3. **Research.** Invoke the `research` skill against the sharpened question for any factual/external input the options depend on.
4. **Score.** Build a weighted-criteria decision matrix: options as rows, criteria as columns (criteria weighted by the profile's values/constraints), each cell scored, tradeoffs stated explicitly. Show the arithmetic, not just the conclusion.
5. **Recommend.** State an explicit recommendation with the reasoning traceable back to the matrix. The user decides; you argue the logical case.
6. **Persist.** Write a new file under `life-decisions/decisions/` (e.g. `YYYY-MM-DD-short-slug.md`) containing: the question, options, criteria/weights, research findings, the scored matrix, the recommendation, and — once known — what the user actually chose.
