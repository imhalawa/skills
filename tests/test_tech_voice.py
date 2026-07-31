import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL = REPO_ROOT / "skills" / "tech-voice"


class TechVoiceStructureTests(unittest.TestCase):
    def test_skill_has_minimal_progressive_disclosure_layout(self):
        self.assertTrue((SKILL / "SKILL.md").is_file())
        self.assertTrue((SKILL / "agents" / "openai.yaml").is_file())
        self.assertTrue((SKILL / "references" / "formats.md").is_file())
        self.assertTrue((SKILL / "references" / "voice.md").is_file())
        self.assertEqual(
            {"SKILL.md", "agents", "references"},
            {path.name for path in SKILL.iterdir()},
        )

    def test_skill_is_global_and_routes_all_required_formats(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("every technical", text.lower())
        self.assertIn("references/formats.md", text)
        self.assertIn("references/voice.md", text)

        formats = (SKILL / "references" / "formats.md").read_text(encoding="utf-8")
        required = {
            "full technical article",
            "series entry",
            "book note",
            "short engineering note",
            "tutorial",
            "system-design explanation",
            "reflective technical essay",
        }
        for label in required:
            with self.subTest(label=label):
                self.assertIn(label, formats.lower())

    def test_voice_contract_protects_precision_and_authorship(self):
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8").lower()
        voice = (SKILL / "references" / "voice.md").read_text(encoding="utf-8").lower()
        self.assertIn("mechanism", skill)
        self.assertIn("decision-changing", skill)
        self.assertIn("preserve", voice)
        self.assertIn("do not imitate", voice)
        self.assertIn("ai-generated", voice)

    def test_plugin_manifest_lists_tech_voice(self):
        manifest = json.loads(
            (REPO_ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
        )
        self.assertIn("./skills/tech-voice", manifest["skills"])


if __name__ == "__main__":
    unittest.main()
