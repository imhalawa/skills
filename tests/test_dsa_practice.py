import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "skills" / "dsa-practice" / "scripts" / "manage_registry.py"
LEGACY_FIELDS = [
    "source", "id", "slug", "title", "url", "topics", "patterns",
    "difficulty", "language", "status", "outcome", "attempts",
    "total_minutes", "confidence", "last_attempted", "next_review",
    "review_stage", "debrief",
]


class RegistryCliTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_cli(self, *arguments, expected_code=0):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *arguments, "--root", str(self.root)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            expected_code,
            result.returncode,
            msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}",
        )
        return result

    def read_csv(self, name):
        with (self.root / "registry" / name).open(newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    def add_two_sum(self, workspace=False):
        arguments = [
            "add",
            "--source", "leetcode",
            "--id", "1",
            "--title", "Two Sum",
            "--url", "https://leetcode.com/problems/two-sum/",
            "--topics", "Arrays",
            "--difficulty", "easy",
            "--language", "java",
        ]
        if workspace:
            arguments.append("--workspace")
        return self.run_cli(*arguments)

    def record_attempt(self, attempted_at, result, assistance):
        return self.run_cli(
            "attempt",
            "--source", "leetcode",
            "--id", "1",
            "--result", result,
            "--assistance", assistance,
            "--minutes", "35",
            "--confidence", "2",
            "--debrief", "Explain why every returned pair is valid.",
            "--on", attempted_at,
        )

    def test_init_creates_two_narrow_source_tables(self):
        self.run_cli("init")

        with (self.root / "registry" / "problems.csv").open(newline="", encoding="utf-8") as file:
            self.assertEqual(
                ["source", "id", "slug", "title", "url", "topics", "difficulty", "language"],
                next(csv.reader(file)),
            )
        with (self.root / "registry" / "attempts.csv").open(newline="", encoding="utf-8") as file:
            self.assertEqual(
                [
                    "source", "id", "attempted_at", "result", "assistance",
                    "minutes", "confidence", "debrief",
                ],
                next(csv.reader(file)),
            )

    def test_add_is_idempotent_and_workspace_contains_only_attempt_file(self):
        self.add_two_sum(workspace=True)
        self.add_two_sum(workspace=True)

        self.assertEqual(1, len(self.read_csv("problems.csv")))
        workspace = self.root / "problems" / "leetcode" / "1-two-sum"
        self.assertEqual(["Solution.java"], sorted(path.name for path in workspace.iterdir()))

    def test_attempts_are_append_only_and_due_output_is_bounded_json(self):
        self.add_two_sum()
        self.record_attempt("2026-07-29", "incorrect", "hint")
        self.record_attempt("2026-07-30", "correct", "none")

        attempts = self.read_csv("attempts.csv")
        self.assertEqual(2, len(attempts))
        self.assertEqual(["incorrect", "correct"], [row["result"] for row in attempts])

        result = self.run_cli("due", "--as-of", "2026-07-31", "--limit", "1")
        payload = json.loads(result.stdout)
        self.assertEqual(1, len(payload))
        self.assertEqual("leetcode", payload[0]["source"])
        self.assertEqual("1", payload[0]["id"])
        self.assertEqual("2026-07-31", payload[0]["due"])

    def test_successive_unassisted_successes_lengthen_review_interval(self):
        self.add_two_sum()
        self.record_attempt("2026-07-29", "incorrect", "hint")
        self.record_attempt("2026-07-30", "correct", "none")
        self.record_attempt("2026-07-31", "correct", "none")
        self.record_attempt("2026-08-07", "correct", "none")

        result = self.run_cli("due", "--as-of", "2026-09-06", "--limit", "10")
        payload = json.loads(result.stdout)
        self.assertEqual("2026-09-06", payload[0]["due"])

    def test_validate_rejects_attempt_for_unknown_problem(self):
        self.run_cli("init")
        attempts_path = self.root / "registry" / "attempts.csv"
        with attempts_path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["leetcode", "404", "2026-07-29", "correct", "none", "20", "4", "ok"])

        result = self.run_cli("validate", expected_code=1)
        self.assertIn("unknown problem", result.stderr.lower())

    def test_due_help_stays_concise(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "due", "--help"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(0, result.returncode)
        self.assertLess(max(map(len, result.stdout.splitlines())), 120)

    def test_migrate_backs_up_legacy_registry_and_keeps_stable_metadata(self):
        registry = self.root / "registry"
        registry.mkdir()
        with (registry / "problems.csv").open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=LEGACY_FIELDS)
            writer.writeheader()
            writer.writerow({
                "source": "leetcode",
                "id": "1",
                "slug": "two-sum",
                "title": "Two Sum",
                "url": "https://leetcode.com/problems/two-sum/",
                "topics": "Arrays",
                "patterns": "Hash map",
                "difficulty": "Easy",
                "language": "java",
                "status": "review",
                "outcome": "hint",
                "attempts": "2",
                "total_minutes": "70",
                "confidence": "2",
                "last_attempted": "2026-07-29",
                "next_review": "2026-07-30",
                "review_stage": "1",
                "debrief": "legacy",
            })

        result = self.run_cli("migrate")

        payload = json.loads(result.stdout)
        self.assertEqual(1, payload["problems"])
        self.assertEqual(1, payload["legacy_rows_with_attempts"])
        self.assertTrue((registry / "problems.legacy.csv").is_file())
        self.assertEqual([], self.read_csv("attempts.csv"))
        migrated = self.read_csv("problems.csv")[0]
        self.assertEqual("Two Sum", migrated["title"])
        self.assertEqual("easy", migrated["difficulty"])
        self.run_cli("validate")

    def test_migrate_rejects_bad_counter_before_changing_files(self):
        registry = self.root / "registry"
        registry.mkdir()
        legacy_path = registry / "problems.csv"
        with legacy_path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=LEGACY_FIELDS)
            writer.writeheader()
            writer.writerow({
                "source": "leetcode",
                "id": "1",
                "slug": "two-sum",
                "title": "Two Sum",
                "difficulty": "easy",
                "language": "java",
                "attempts": "many",
            })
        original = legacy_path.read_text(encoding="utf-8")

        result = self.run_cli("migrate", expected_code=1)

        self.assertIn("legacy attempts", result.stderr.lower())
        self.assertEqual(original, legacy_path.read_text(encoding="utf-8"))
        self.assertFalse((registry / "problems.legacy.csv").exists())
        self.assertFalse((registry / "attempts.csv").exists())

    def test_add_rejects_legacy_registry_without_partial_initialization(self):
        registry = self.root / "registry"
        registry.mkdir()
        with (registry / "problems.csv").open("w", newline="", encoding="utf-8") as file:
            csv.DictWriter(file, fieldnames=LEGACY_FIELDS).writeheader()

        result = self.run_cli(
            "add",
            "--source", "leetcode",
            "--id", "1",
            "--title", "Two Sum",
            "--language", "java",
            expected_code=1,
        )

        self.assertIn("unexpected header", result.stderr.lower())
        self.assertFalse((registry / "attempts.csv").exists())

    def test_failed_workspace_validation_does_not_add_problem(self):
        result = self.run_cli(
            "add",
            "--source", "leetcode",
            "--id", "1",
            "--title", "Two Sum",
            "--language", "unknown-language",
            "--workspace",
            expected_code=1,
        )

        self.assertIn("file extension", result.stderr)
        self.assertEqual([], self.read_csv("problems.csv"))
        self.assertFalse((self.root / "problems").exists())

    def test_due_rejects_corrupt_attempt_values(self):
        self.add_two_sum()
        attempts_path = self.root / "registry" / "attempts.csv"
        with attempts_path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["leetcode", "1", "2026-07-29", "maybe", "none", "20", "4", "bad"])

        result = self.run_cli("due", "--as-of", "2026-07-30", expected_code=1)
        self.assertIn("invalid result", result.stderr.lower())


if __name__ == "__main__":
    unittest.main()
