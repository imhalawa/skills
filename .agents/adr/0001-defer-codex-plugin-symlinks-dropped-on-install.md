# Defer a native Codex plugin/marketplace; ship only the Claude Code one

We ship a native **Claude Code plugin** (`.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json`) and **defer** a native Codex plugin, for the same reason [`mattpocock/skills` documented in their own ADR](https://github.com/mattpocock/skills/blob/main/.agents/adr/0002-ship-as-a-claude-code-plugin.md) — a repo we depend on directly (`grilling`, `research`).

A first pass here scaffolded `.agents/plugins/marketplace.json` + `plugins/skills/.codex-plugin/plugin.json` via Codex's own bundled `plugin-creator` skill, with `plugins/skills/skills` as a symlink back to this repo's real `skills/` (to avoid duplicating skill content). It validated cleanly with `scripts/validate_plugin.py` — but validation only checks manifest shape, not install behavior.

**The actual problem, found in mattpocock's ADR, not by testing here:** Codex copies a plugin's tree into its install cache and **drops symlinks** during that copy. A symlinked `skills/` inside a Codex plugin arrives empty on real install — the plugin would silently ship broken. `.codex-plugin/plugin.json`'s `skills` field also only accepts a single path string (not an array), so even without the symlink problem there's no way to point it at content living outside the plugin's own directory tree.

The only robust fixes are the same two mattpocock rejected: physically duplicate skill content under the plugin directory (sync burden, second source of truth), or restructure so the promoted skill set already lives at a path Codex can reference directly and exclusively. Neither is worth doing for a one-skill repo.

## Decision

- Ship the Claude Code plugin/marketplace now.
- Do not ship a Codex plugin/marketplace. Codex users install via the universal installer instead (`npx skills add imhalawa/skills` with `-a codex`, or the `skill-installer` system skill's `install-skill-from-github.py` — both already documented in `README.md`), which copies real files, not symlinks, so it isn't affected by this problem.
- Revisit if Codex starts preserving symlinks on plugin install, or accepts an array/include-list for `skills` in `plugin.json`.
