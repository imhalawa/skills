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
