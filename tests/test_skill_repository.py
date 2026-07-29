import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
QUICK_VALIDATE = Path(
    "/home/atom/.codex/skills/.system/skill-creator/scripts/quick_validate.py"
)
REPOSITORY_TEST_COMMAND = "python3 -B -m unittest discover -s tests -v"
ZERO_TEST_COMMAND = "python3 -B -m unittest -v"
CLAUDE_DEPENDENCY_COMMAND = (
    "npx skills add mattpocock/skills --skill grilling research"
)
OPENAI_INTERFACE_FIELDS = {
    "display_name",
    "short_description",
    "default_prompt",
}
OPENAI_INTERFACE_LINE = re.compile(
    r'^  (?P<key>[a-z][a-z0-9_]*): (?P<value>"(?:[^"\\]|\\.)*")$'
)


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


def openai_interface(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    meaningful = [
        (line_number, line)
        for line_number, line in enumerate(lines, start=1)
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if not meaningful or meaningful[0][1] != "interface:":
        raise AssertionError(f"missing top-level interface mapping: {path}")

    fields = {}
    for line_number, line in meaningful[1:]:
        match = OPENAI_INTERFACE_LINE.fullmatch(line)
        if not match:
            raise AssertionError(
                f"malformed interface line {line_number} in {path}: {line!r}"
            )
        key = match.group("key")
        if key in fields:
            raise AssertionError(f"duplicate interface field {key!r}: {path}")
        value = json.loads(match.group("value"))
        if not value.strip():
            raise AssertionError(f"empty interface field {key!r}: {path}")
        fields[key] = value

    if set(fields) != OPENAI_INTERFACE_FIELDS:
        raise AssertionError(
            f"interface fields must be exactly {sorted(OPENAI_INTERFACE_FIELDS)}: {path}"
        )
    if not 25 <= len(fields["short_description"]) <= 64:
        raise AssertionError(
            f"short_description must contain 25-64 characters: {path}"
        )
    return fields


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
            metadata = openai_interface(directory / "agents" / "openai.yaml")
            self.assertRegex(
                metadata["default_prompt"],
                rf"\${re.escape(directory.name)}(?![a-z0-9-])",
            )

    def test_openai_metadata_rejects_malformed_structures(self):
        invalid_documents = {
            "comments only": """\
# display_name:
# short_description:
# $demo-skill
""",
            "empty strings": """\
interface:
  display_name: ""
  short_description: ""
  default_prompt: "$demo-skill"
""",
            "missing interface indentation": """\
interface:
display_name: "Demo Skill"
short_description: "A sufficiently long description"
default_prompt: "Use $demo-skill for this task."
""",
            "malformed simple key line": """\
interface:
  display_name: "Demo Skill"
  short_description: "A sufficiently long description"
  default_prompt: "Use $demo-skill for this task."
  malformed line
""",
            "skill name only in comment": """\
interface:
  display_name: "Demo Skill"
  short_description: "A sufficiently long description"
  default_prompt: "Use this skill for the task."
# $demo-skill
""",
            "short description below minimum": """\
interface:
  display_name: "Demo Skill"
  short_description: "Too short"
  default_prompt: "Use $demo-skill for this task."
""",
            "extra interface field": """\
interface:
  display_name: "Demo Skill"
  short_description: "A sufficiently long description"
  default_prompt: "Use $demo-skill for this task."
  extra_field: "Not part of the minimal interface"
""",
        }

        for label, metadata in invalid_documents.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as temporary:
                directory = Path(temporary) / "demo-skill"
                agents = directory / "agents"
                agents.mkdir(parents=True)
                (agents / "openai.yaml").write_text(metadata, encoding="utf-8")
                result = unittest.TestResult()
                with patch(__name__ + ".skill_directories", return_value=[directory]):
                    SkillStructureTests(
                        "test_each_skill_has_minimal_openai_metadata"
                    ).run(result)
                self.assertFalse(
                    result.wasSuccessful(),
                    f"malformed openai.yaml was accepted: {label}",
                )

    def test_each_skill_passes_official_validator_when_available(self):
        if not QUICK_VALIDATE.is_file():
            self.skipTest(f"official validator unavailable: {QUICK_VALIDATE}")

        for directory in skill_directories():
            with self.subTest(skill=directory.name):
                completed = subprocess.run(
                    [sys.executable, str(QUICK_VALIDATE), str(directory)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(
                    0,
                    completed.returncode,
                    "official validator failed for "
                    f"{directory.name}\nstdout:\n{completed.stdout}\n"
                    f"stderr:\n{completed.stderr}",
                )

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

    def test_agents_documents_the_repository_test_command(self):
        policy = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn(REPOSITORY_TEST_COMMAND, policy)
        self.assertNotIn(ZERO_TEST_COMMAND, policy)

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

    def test_readme_documents_the_repository_test_command(self):
        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(REPOSITORY_TEST_COMMAND, readme)
        self.assertNotIn(ZERO_TEST_COMMAND, readme)

    def test_decide_documents_supported_claude_dependency_command(self):
        skill = (REPO_ROOT / "skills" / "decide" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertIn(CLAUDE_DEPENDENCY_COMMAND, skill)
        self.assertNotIn("mattpocock/skills/grilling", skill)
        self.assertNotIn("mattpocock/skills/research", skill)
