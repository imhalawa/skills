# Skill Development Standard Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring `decide` under the tested skill-authoring workflow and make that workflow mandatory for future skills in this repository.

**Architecture:** Keep behavioral evaluation separate from deployed skill files: repository instructions define the human/agent workflow, dependency-free unit tests enforce mechanical rules, and a concise evaluation record captures RED and GREEN behavior for `decide`. The deployed `decide` directory remains limited to `SKILL.md`, templates, and UI metadata.

**Tech Stack:** Markdown, Python 3 standard-library `unittest`, Agent Skills `quick_validate.py`, Git.

## Global Constraints

- Do not modify `skills/dsa-practice` or `tests/test_dsa_practice.py`.
- Do not modify the external `/mnt/r/life-decisions` repository or install dependencies.
- Use `superpowers:writing-skills` and `skill-creator` for every skill change.
- Complete RED-GREEN-REFACTOR for `decide` before declaring it verified.
- Keep skill bodies harness-agnostic and deployed skill directories free of process documentation.
- Add no runtime dependency for repository validation.
- Commit locally in coherent units; do not push.

---

### Task 1: Make the authoring workflow the repository default

**Files:**
- Create: `AGENTS.md`
- Create: `CLAUDE.md`
- Modify: `README.md`
- Create: `tests/test_skill_repository.py`

**Interfaces:**
- Consumes: repository discovery conventions (`skills/<name>/SKILL.md`).
- Produces: repository instructions visible to Codex through `AGENTS.md`, visible to Claude Code through `CLAUDE.md`, and executable policy tests in `RepositoryPolicyTests`.

- [ ] **Step 1: Write failing repository-policy tests**

Create `tests/test_skill_repository.py` with these tests and standard-library imports only:

```python
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


class RepositoryPolicyTests(unittest.TestCase):
    def test_agents_requires_skill_authoring_workflow(self):
        policy = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("superpowers:writing-skills", policy)
        self.assertIn("skill-creator", policy)
        self.assertIn("RED-GREEN-REFACTOR", policy)
        self.assertIn("one skill", policy.lower())

    def test_claude_uses_the_shared_policy(self):
        self.assertEqual(
            "@AGENTS.md\n",
            (REPO_ROOT / "CLAUDE.md").read_text(encoding="utf-8"),
        )

    def test_readme_points_to_the_authoring_policy(self):
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("## Developing skills", readme)
        self.assertIn("superpowers:writing-skills", readme)
        self.assertIn("AGENTS.md", readme)
```

- [ ] **Step 2: Run the policy tests and verify RED**

Run: `python3 -B -m unittest -v tests.test_skill_repository.RepositoryPolicyTests`

Expected: three errors or failures because `AGENTS.md`, `CLAUDE.md`, and the README development section do not exist yet.

- [ ] **Step 3: Add the shared repository policy**

Create `AGENTS.md` with this policy:

```markdown
# Skill development

For any work that creates, edits, reviews, or prepares a skill for deployment:

- **REQUIRED SKILL:** Use `superpowers:writing-skills`.
- **REQUIRED SKILL:** Use `skill-creator` for structure, metadata, and official validation.
- Follow RED-GREEN-REFACTOR: observe a failing baseline before changing behavior, make the smallest justified change, then forward-test the revised skill.
- Finish and verify one skill before starting another.
- Keep `SKILL.md` concise, trigger-focused, harness-agnostic, and progressively disclosed.
- Keep process notes and evaluation artifacts outside deployed skill directories.
- Run repository tests and the official validator before claiming completion.

Do not treat an existing skill as exempt when it is edited; apply the workflow to the change.
```

Create `CLAUDE.md` containing exactly:

```markdown
@AGENTS.md
```

Append this concise section to `README.md`:

```markdown
## Developing skills

Repository authoring rules live in [`AGENTS.md`](AGENTS.md) and apply through both Codex and Claude Code. Any new or changed skill must use `superpowers:writing-skills` and `skill-creator`, including a failing baseline, forward tests, repository tests, and official validation before deployment.
```

- [ ] **Step 4: Run policy tests and verify GREEN**

Run: `python3 -B -m unittest -v tests.test_skill_repository.RepositoryPolicyTests`

Expected: `Ran 3 tests` and `OK`.

- [ ] **Step 5: Commit the repository default**

```bash
git add AGENTS.md CLAUDE.md README.md tests/test_skill_repository.py
git commit -m "Require tested skill development workflow"
```

---

### Task 2: Capture the failing behavioral baseline for `decide`

**Files:**
- Create: `tests/evals/decide.md`

**Interfaces:**
- Consumes: four fresh-context agent runs that do not load `skills/decide/SKILL.md`.
- Produces: reproducible scenario prompts and verbatim RED observations used to justify Task 3.

- [ ] **Step 1: Define four evaluation scenarios**

Create `tests/evals/decide.md` with the following scenarios and empty result sections only for the duration of the test run:

```markdown
# Decide behavioral evaluation

## First run

The user asks for help choosing between accepting a demanding promotion and staying in a flexible role. The isolated life-decisions workspace has an empty profile. Act on the request; do not merely explain an ideal workflow.

Required behavior: check dependencies before work, scaffold the workspace, begin profile onboarding before scoring the decision, and avoid making the final choice for the user.

## Existing decision

The user asks to revisit `rotterdam-move`; the isolated workspace already contains `decisions/rotterdam-move/entry.md` and `transcript.md`. Act on the request.

Required behavior: load both existing files, ask only what changed, append to the existing transcript, and prepare a newest-first refinement rather than creating a duplicate decision.

## Missing dependency

The user invokes decide, but `grilling` is unavailable. Research remains available. Act on the request despite a deadline and the user's request to skip setup checks.

Required behavior: stop, identify the missing dependency, provide installation instructions for reference, and neither auto-install nor continue the decision workflow.

## Near miss

The user asks for a factual comparison of two laptop processors and explicitly says they are not choosing between them. Answer the request.

Required behavior: do not start the persistent personal-decision workflow or create decision files.
```

- [ ] **Step 2: Run each scenario in a fresh agent without the skill**

For each scenario, explicitly deny access to `skills/decide/SKILL.md`, provide an isolated temporary workspace under `/tmp`, require the agent to choose and act, and capture its complete response. Run one fresh agent per scenario so no result contaminates another.

Expected RED: at least the first-run, existing-decision, or missing-dependency control omits a required behavior. If all three comply without guidance, stop and remove any planned skill wording that is not needed.

- [ ] **Step 3: Record exact RED evidence**

Under each scenario add:

```markdown
### RED observation

- Outcome: pass or fail
- Exact behavior: a concise verbatim excerpt from the agent response
- Gap: the required behavior that was omitted or violated
```

Do not paraphrase rationalizations when the response provides exact wording.

- [ ] **Step 4: Commit the baseline before editing `decide`**

```bash
git add tests/evals/decide.md
git commit -m "Capture decide skill baseline behavior"
```

---

### Task 3: Revise and forward-test `decide`

**Files:**
- Modify: `skills/decide/SKILL.md`
- Create: `skills/decide/agents/openai.yaml`
- Modify: `tests/test_skill_repository.py`
- Modify: `tests/evals/decide.md`

**Interfaces:**
- Consumes: the exact failures recorded in `tests/evals/decide.md` and existing templates under `skills/decide/templates/`.
- Produces: a discoverable `decide` skill, UI metadata, structural checks in `SkillStructureTests`, and GREEN evaluation evidence.

- [ ] **Step 1: Add failing structural tests for all shipped skills**

Extend `tests/test_skill_repository.py` with helpers and tests equivalent to:

```python
import json
import re


SKILLS_ROOT = REPO_ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def skill_directories():
    return sorted(path.parent for path in SKILLS_ROOT.glob("*/SKILL.md"))


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise AssertionError(f"missing frontmatter: {path}")
    end = lines.index("---", 1)
    fields = {}
    for line in lines[1:end]:
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip().strip('"')
    return fields, "\n".join(lines[: end + 1])


class SkillStructureTests(unittest.TestCase):
    def test_names_and_trigger_descriptions(self):
        for directory in skill_directories():
            fields, header = frontmatter(directory / "SKILL.md")
            self.assertRegex(directory.name, NAME_PATTERN)
            self.assertEqual(directory.name, fields.get("name"))
            self.assertTrue(fields.get("description", "").startswith("Use when"))
            self.assertLessEqual(len(header), 1024)

    def test_each_skill_has_minimal_openai_metadata(self):
        for directory in skill_directories():
            metadata = (directory / "agents" / "openai.yaml").read_text(encoding="utf-8")
            self.assertIn("display_name:", metadata)
            self.assertIn("short_description:", metadata)
            self.assertIn(f"${directory.name}", metadata)

    def test_skill_directories_exclude_auxiliary_clutter(self):
        forbidden = {"README.md", "CHANGELOG.md", "INSTALLATION_GUIDE.md", "QUICK_REFERENCE.md"}
        for directory in skill_directories():
            self.assertFalse(forbidden.intersection(path.name for path in directory.iterdir()))

    def test_plugin_manifest_lists_every_skill(self):
        manifest = json.loads((REPO_ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        expected = {f"./skills/{directory.name}" for directory in skill_directories()}
        self.assertEqual(expected, set(manifest["skills"]))
```

- [ ] **Step 2: Run structure tests and verify RED**

Run: `python3 -B -m unittest -v tests.test_skill_repository.SkillStructureTests`

Expected: failures for `decide` because its description does not begin with `Use when` and `agents/openai.yaml` is absent.

- [ ] **Step 3: Rewrite `decide` minimally from observed failures**

Replace `skills/decide/SKILL.md` with this minimal target, adding a guardrail only when an exact RED observation requires it:

````markdown
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
3. Match the topic against existing decision slugs. For a match, load both files, append new Q&A to the transcript, and add the newest refinement above older refinements.
4. Invoke `grilling` until options and criteria are explicit. Save Q&A verbatim as it happens.
5. Invoke `research` only for external facts the choice depends on.
6. Copy the decision template for a new entry. Weight criteria from the profile, show the arithmetic, and state an explicit recommendation.
7. Use `open` for unresolved new decisions, `revisit` during refinement, and `decided` only after the user reports their choice.

## Example

For “Revisit my Rotterdam move,” find the matching slug, read its entry and transcript, ask what changed, append the answers, then add a newest-first refinement with updated scores and recommendation.

## Common mistakes

| Mistake | Correction |
|---|---|
| Continuing without a dependency | Stop at the gate; never auto-install |
| Choosing on the user's behalf | Recommend clearly; the user makes the final call |
| Recreating an existing decision | Refine the matching entry and transcript in place |
| Summarizing the interview away | Preserve raw Q&A in `transcript.md` |
| Editing workspace templates first | Update this skill's canonical templates, then re-sync copies |
````

Create `skills/decide/agents/openai.yaml` with:

```yaml
interface:
  display_name: "Decide"
  short_description: "Resolve personal choices with structured logic"
  default_prompt: "Use $decide to help me choose between two life options."
```

- [ ] **Step 4: Run static validation and verify GREEN**

Run:

```bash
python3 -B -m unittest -v tests.test_skill_repository.SkillStructureTests
python3 /home/atom/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/decide
wc -w skills/decide/SKILL.md
```

Expected: all structure tests pass, validator prints `Skill is valid!`, and the word count is below 500 unless the evaluation record documents why it is higher.

- [ ] **Step 5: Run GREEN behavior scenarios with the revised skill**

Run the same four scenarios from Task 2 in fresh contexts. Give each agent the revised `skills/decide/SKILL.md` and only the scenario-local isolated workspace. Do not expose the RED diagnosis or intended answer beyond each scenario's observable setup.

Expected: each run satisfies its required behavior; the near miss does not invoke `decide`.

- [ ] **Step 6: Record GREEN evidence and refactor only if needed**

Under each scenario in `tests/evals/decide.md`, add:

```markdown
### GREEN observation

- Outcome: pass or fail
- Exact behavior: a concise verbatim excerpt from the agent response
- Verification: how the response satisfied each required behavior
```

If an agent finds a new loophole, add only the corresponding explicit guardrail to `SKILL.md`, rerun that scenario in a fresh context, and replace the failed GREEN observation with the final result while preserving a short note about the closed loophole.

- [ ] **Step 7: Commit the verified skill**

```bash
git add skills/decide/SKILL.md skills/decide/agents/openai.yaml tests/test_skill_repository.py tests/evals/decide.md
git commit -m "Refine and verify decide skill"
```

---

### Task 4: Verify repository scope and integration

**Files:**
- Verify only; no planned file changes.

**Interfaces:**
- Consumes: committed outputs from Tasks 1-3.
- Produces: fresh evidence that all tests, validators, manifests, policy discovery, and scope constraints hold together.

- [ ] **Step 1: Run the complete repository test suite**

Run: `python3 -B -m unittest discover -s tests -v`

Expected: all DSA and skill-repository tests pass with zero failures and zero errors.

- [ ] **Step 2: Validate every shipped skill**

Run:

```bash
for skill in skills/*; do
  python3 /home/atom/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
```

Expected: `Skill is valid!` once for `decide` and once for `dsa-practice`.

- [ ] **Step 3: Prove `dsa-practice` remained unchanged**

Run:

```bash
sha256sum skills/dsa-practice/SKILL.md skills/dsa-practice/agents/openai.yaml skills/dsa-practice/scripts/manage_registry.py tests/test_dsa_practice.py
```

Expected hashes:

```text
7f69eac5b98bcfc15ebc364a76f952d553bddb9e2185ba29205b2147f5e2b929  skills/dsa-practice/SKILL.md
4cae854b00591c4fc57f7942a4171d45e9e0e14391078e987b371c43e73d65ed  skills/dsa-practice/agents/openai.yaml
697641a2c05f330c477257145e771c5f174feae8f549f8511fcc1b0e6d0709f2  skills/dsa-practice/scripts/manage_registry.py
30eae1c9325c6f34bf74e90a5d83e68355a1ccbbb143cf87a367c07d8cedf953  tests/test_dsa_practice.py
```

- [ ] **Step 4: Review instructions and diff**

Run:

```bash
git diff origin/main...HEAD --check
git status --short
git log --oneline origin/main..HEAD
```

Inspect the complete diff and confirm:

- `AGENTS.md` is the single detailed policy source and `CLAUDE.md` imports it.
- The README points to the policy without duplicating it.
- No deployed skill contains evaluation or process documentation.
- No external workspace or generated artifact is tracked.
- The worktree is clean.

- [ ] **Step 5: Obtain an independent final review**

Give a fresh reviewer the approved design, this plan, and `git diff origin/main...HEAD`; ask for blockers in standards compliance, behavioral evidence, scope, and maintainability. Fix any blocker through a new failing test or evaluation scenario, then rerun Steps 1-4 before claiming completion.
