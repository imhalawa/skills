---
name: decide
description: Logic-first decision and life-choice resolution, backed by research and a persistent personal profile. Use when the user wants help deciding between options, resolving a life choice, revisiting a past decision, or explicitly invokes 'decide'/'/decide'.
---

Act as the user's purely logical second voice — a deliberate counterweight to emotion-driven, impulsive decision-making. Never make the final call for them; make the logic behind a good call impossible to ignore.

The profile and decision log live in a separate repo: `life-decisions` — known location: `/mnt/r/life-decisions` (may relocate; if not there, ask where it lives once, then remember). Layout:

```
life-decisions/
  profile.md              # accumulated values / constraints / decision-style
  templates/
    decision.md            # seeded copy — canonical source is this skill's own templates/decision.md
    profile.md              # seeded copy — canonical source is this skill's own templates/profile.md
  decisions/
    <slug>/
      entry.md              # structured output, copied from templates/decision.md
      transcript.md          # raw grilling Q&A for this decision, verbatim
```

This skill's own repo carries the canonical templates (`templates/decision.md`, `templates/profile.md`, next to this file) — `life-decisions` gets a seeded copy on first run. If the templates evolve here, re-sync the copies in `life-decisions` too.

## 0. Dependencies

Depends on `grilling` and `research` (source: `mattpocock/skills` — https://github.com/mattpocock/skills). Check both are discoverable (current skill listing, or resolve under wherever skills are installed for the active harness) before running anything below.

This is a **hard blocker, not an auto-install**. If either is missing, stop and tell the user exactly what's missing and where to get it — do not install it for them, on any harness. They may not want this skill's opinion on how their skill directory is managed. Give them the source URL and, for reference only, the commands that would install it:

- **Claude Code**: `npx skills add mattpocock/skills/grilling` (and `.../research`)
- **Codex CLI**: `python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo mattpocock/skills --path skills/productivity/grilling skills/engineering/research`

Wait for the user to install and confirm before proceeding to §1.

## 1. Initiation (first run only)

If `life-decisions/profile.md` doesn't exist, or exists but is empty of real content: this is a new machine or fresh setup.

1. Scaffold `life-decisions` if missing: copy this skill's `templates/profile.md` to `life-decisions/profile.md`, copy `templates/decision.md` to `life-decisions/templates/decision.md` (and `templates/profile.md` there too, for reference), create `decisions/`.
2. Say what's happening, then run a dedicated onboarding interview via `grilling` — not about any specific decision, but about the user themselves: values, risk tolerance, hard constraints (financial, family, health, time), and how they tend to decide (impulsive/deliberate, what derails them).
3. Write the answers into `profile.md` under the Decision-making style / Values / Constraints headings, each entry dated.

Skip this whole step once a populated profile already exists — it's onboarding, not a recurring ritual.

## 2. Ongoing capture

At the start of any `decide` session, and whenever the user reveals a new values/constraints/decision-style fact mid-conversation (in this skill or otherwise — see the global passive-capture instruction in the user's own CLAUDE.md/AGENTS.md, which this skill's onboarding step should have helped bootstrap), append it to `profile.md`, dated, under the right heading. Don't duplicate an existing entry — check first.

## 3. Deciding

For a new decision:

1. **Identify the slug.** Short kebab-case name for this decision (e.g. `rotterdam-move`). Check `decisions/` for an existing slug that matches this topic before assuming it's new — if one exists, this is a **refinement** (see §4), not a new decision.
2. **Grill.** Invoke `grilling` to interview the user until the actual options and the criteria that matter are sharp and explicit. Save the raw Q&A verbatim to `decisions/<slug>/transcript.md` as it happens (don't summarize it away — that's what `entry.md` is for).
3. **Research.** Invoke `research` against the sharpened question for any factual/external input the options depend on.
4. **Score.** Copy `templates/decision.md` to `decisions/<slug>/entry.md` if not already present. Fill in options, criteria (weighted from the profile's values/constraints), and the scored matrix — show the arithmetic, not just the conclusion.
5. **Recommend.** State an explicit recommendation with reasoning traceable to the matrix. The user decides; you argue the logical case. Set `entry.md` status to `open`.
6. **Persist outcome later.** Once the user says what they actually chose (may be a later session), update `entry.md`'s Outcome section and flip status to `decided`.

## 4. Refining

If the user wants to revisit an existing decision (explicit ask, or a new decision session matches an existing slug): load that `decisions/<slug>/entry.md` and its `transcript.md` for context first — don't re-litigate ground already covered. Grill only on what's actually changed. Append a new `## Refinement — YYYY-MM-DD` section to `entry.md` (most recent on top, per the template) with updated criteria/matrix rows and recommendation; append the new Q&A to the same `transcript.md` rather than starting a new file. Set status to `revisit` while open, back to `decided` once resolved.

## Templates

This skill's `templates/decision.md` and `templates/profile.md` (next to this file) are the source of truth — `life-decisions`' copies are seeded from them, not the other way around. If a decision's needs outgrow the template (a recurring section that isn't there yet), update the template here first, then re-sync `life-decisions/templates/`, so future entries stay consistent instead of drifting.
