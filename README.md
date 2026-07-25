# skills

Personal skills, built to the open [Agent Skills](https://agentskills.io) standard — supports both **Claude Code** and **Codex CLI** by default, no per-harness fork.

## Layout

One folder per skill: `skills/<name>/SKILL.md`. Follows the same convention as other skill-source repos (e.g. `kepano/obsidian-skills`, `mattpocock/skills`).

Skill bodies must stay harness-agnostic in wording (e.g. "invoke the `X` skill", never "use the Skill tool") since Claude Code and Codex expose different tool primitives for the same concepts.

## Installing

### As individual skills

- **Claude Code** — installs under `~/.agents/skills` (symlinked into `~/.claude/skills`):
  ```
  npx skills add imhalawa/skills
  ```
- **Codex CLI** — installs under `$CODEX_HOME/skills` (default `~/.codex/skills`) via the bundled `skill-installer` skill:
  ```
  python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py --repo imhalawa/skills --path skills/<name>
  ```

### As a marketplace/plugin (installs all skills in this repo at once)

- **Claude Code**:
  ```
  claude plugin marketplace add imhalawa/skills
  claude plugin install skills@skills
  ```
  Manifests: `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`.
- **Codex CLI** (repo/team marketplace):
  ```
  codex plugin marketplace add <path-to-this-repo>/.agents/plugins/marketplace.json
  ```
  Manifests: `.agents/plugins/marketplace.json`, `plugins/skills/.codex-plugin/plugin.json` (its `skills/` is a symlink back to the repo's real `skills/`, so nothing is duplicated).

Any skill added here should document both install paths in its own SKILL.md if it declares dependencies on other skills (see `skills/decide/SKILL.md` for the pattern).
