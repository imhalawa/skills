import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
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
