# Skill Development Standard

## Goal

Bring every authored skill in this repository under the `superpowers:writing-skills` development workflow, excluding the already-completed `dsa-practice` skill, and make that workflow the default for future skill work.

The repository currently contains one remaining skill in scope: `decide`.

## Scope

In scope:

- Evaluate and, where tests expose a gap, revise `skills/decide`.
- Preserve `decide`'s existing purpose, persistent data model, and cross-harness behavior.
- Add repository instructions that require the same workflow for future skill creation and edits.
- Add lightweight automated structural checks that apply to every shipped skill.
- Keep the existing README as the only contributor-facing overview.

Out of scope:

- Reworking or retesting `dsa-practice`.
- Vendoring or duplicating `superpowers:writing-skills` in this repository.
- Changing the external `life-decisions` repository or installing dependencies.
- Publishing, pushing, or opening a pull request.

## Skill Evaluation

Treat `decide` as a workflow skill with persistent-state and dependency guardrails. Apply RED-GREEN-REFACTOR before changing its behavior:

1. Run realistic baseline scenarios without loading `decide` and capture concrete failures.
2. Cover first-run onboarding, refinement of an existing decision, missing dependencies, and a near-miss that should not invoke the workflow.
3. Revise only what the observed failures justify.
4. Re-run equivalent scenarios with the revised skill loaded.
5. Close any newly exposed loopholes and re-test.

Keep test artifacts outside the deployed skill directory. The deployed directory should contain only its instructions and resources.

## Repository Default

Add a root `AGENTS.md` that makes `superpowers:writing-skills` and `skill-creator` mandatory whenever a skill is created, edited, reviewed, or prepared for deployment. It will require:

- A failing baseline before behavioral changes.
- One skill completed and verified before starting another.
- Minimal, trigger-focused metadata and progressive disclosure.
- Forward tests appropriate to the skill type.
- Fresh structural and behavioral verification before completion claims.

Add a minimal root `CLAUDE.md` that imports the shared repository policy so Claude Code and Codex receive the same rules without maintaining two copies.

Add a short development section to `README.md` that points contributors to the repository instructions and states the required authoring skills. The README will not duplicate the detailed checklist.

## Automated Checks

Add dependency-free repository tests that discover `skills/*/SKILL.md` and check stable, mechanically enforceable requirements:

- Directory and frontmatter names match and use lowercase kebab-case.
- Required `name` and `description` fields exist.
- Descriptions start with `Use when` and remain within the supported metadata limit.
- Every skill passes the official `skill-creator` validator when it is available.
- Shipped skill directories avoid known auxiliary clutter such as per-skill README or changelog files.
- Plugin manifests continue to list every shipped skill where required.

Behavioral quality remains an agent-evaluation concern; static tests must not pretend to prove that a workflow is effective.

## Verification

Before completion:

1. Run the `decide` forward-test scenarios and inspect each result.
2. Run the repository test suite.
3. Run the official validator against every skill.
4. Confirm `dsa-practice` is unchanged.
5. Check repository instructions are discoverable from both supported harnesses.
6. Review the complete diff for scope, concision, and accidental generated files.
7. Run `git diff --check` and confirm the worktree state.

Commit locally in coherent units. Do not push without separate authorization.
