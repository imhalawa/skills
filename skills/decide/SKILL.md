---
name: decide
description: Use when the user wants help choosing between life options, resolving or revisiting a personal decision, or explicitly invokes decide or /decide.
---

# Decide

## Overview

Act as the user's logical second voice: make an explicit, evidence-backed recommendation while leaving the final choice to the user. Preserve relevant context so later decisions improve instead of restarting from scratch.

## Dependency gate

Require the `grilling` and `research` skills before doing any decision work. If either is unavailable, stop, name what is missing, and reference `https://github.com/mattpocock/skills`. Do not install it or continue the workflow.

Reference installation commands:

- Claude Code: `npx skills add mattpocock/skills/grilling` and `npx skills add mattpocock/skills/research`
- Codex CLI: `python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo mattpocock/skills --path skills/productivity/grilling skills/engineering/research`

## Workspace

Use `/mnt/r/life-decisions`; if absent, ask for its new location once. This skill's `templates/decision.md` and `templates/profile.md` are canonical. Seed copies into the workspace only when missing.

```text
life-decisions/
  profile.md
  templates/{decision.md,profile.md}
  decisions/<slug>/{entry.md,transcript.md}
```

## Quick reference

| Situation | Action |
|---|---|
| Empty profile | Scaffold, invoke `grilling` for onboarding, then record dated values, constraints, and decision style |
| New decision | Create a kebab-case slug, grill, research factual dependencies, score, recommend, persist |
| Matching slug | Load `entry.md` and `transcript.md`; ask only what changed; refine in place |
| User reports outcome | Record the choice and date; set status to `decided` |
| New personal fact | Append it to the matching profile section unless already present |

## Workflow

1. Pass the dependency gate and load the profile.
2. If the profile has no real content, complete onboarding before scoring a decision.
3. Match topics to existing slugs. For a match, load both files; before waiting for answers, set status `revisit`, add a dated newest-first refinement placeholder, and append the revisit request and next question to the existing transcript. Replace placeholders as new Q&A arrives.
4. Invoke `grilling` until options and criteria are explicit. Save Q&A verbatim as it happens.
5. Invoke `research` only for external facts the choice depends on.
6. Copy the decision template for a new entry. Weight criteria from the profile, show the arithmetic, and state an explicit recommendation.
7. Use `open` for unresolved new decisions, `revisit` during refinement, and `decided` only after the user reports their choice.

## Example

For “Revisit my Rotterdam move,” load the matching entry and transcript, mark `revisit`, add a newest-first placeholder, append the request and next question, then ask what changed; replace the placeholder as answers arrive.

## Common mistakes

| Mistake | Correction |
|---|---|
| Continuing without a dependency | Stop at the gate; never auto-install |
| Choosing on the user's behalf | Recommend clearly; the user makes the final call |
| Recreating an existing decision | Refine the matching entry and transcript in place |
| Summarizing the interview away | Preserve raw Q&A in `transcript.md` |
| Editing workspace templates first | Update this skill's canonical templates, then re-sync copies |
