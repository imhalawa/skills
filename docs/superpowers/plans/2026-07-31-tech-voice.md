# Tech Voice Implementation Plan

**Goal:** Build and globally install a minimal, intensively tested technical
communication skill for answers, project work, and publishing.

## Constraints

- Use `superpowers:writing-skills` and `skill-creator`.
- Complete RED-GREEN-REFACTOR before deployment.
- Keep evaluation records outside `skills/tech-voice/`.
- Do not use `traceintime.com` as voice evidence.
- Preserve unrelated worktree changes.

## Tasks

### 1. Lock the evidence and contract

- [x] Complete the multi-source technical-writing census and comparison.
- [x] Derive a conversation-only user voice profile.
- [x] Record the approved architecture and intensive format matrix.
- [x] Remove the superseded preliminary research report.

### 2. Capture RED

- [x] Add failing structural tests for the absent skill.
- [x] Run fresh no-skill controls for the core behavior contract.
- [x] Record exact prompts, outputs, and manually inspected failures.

### 3. Implement GREEN

- [x] Add concise `SKILL.md` and minimal OpenAI metadata.
- [x] Add conditional format and voice references.
- [x] Update the Claude plugin manifest.
- [x] Make only changes justified by observed failures.

### 4. Test intensively

- [x] Re-run core controls with the skill in fresh contexts.
- [x] Run the seven Trace in Time format scenarios.
- [x] Run project-artifact, DSA-teaching, and near-miss scenarios.
- [x] Run five-repetition wording microtests and inspect variance.
- [x] Record failures, refinements, and final evidence.

### 5. Verify and deploy

- [x] Run the repository unit tests.
- [x] Run the official skill validator.
- [x] Run `git diff --check` and review the complete diff.
- [x] Install globally for Codex and Claude Code.
- [x] Verify installed copies match the reviewed source.
- [x] Commit coherently and push the current branch.
