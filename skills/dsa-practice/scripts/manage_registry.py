#!/usr/bin/env python3
"""Maintain a minimal, append-only DSA practice registry."""

import argparse
import csv
import json
import re
import shutil
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path


PROBLEM_FIELDS = [
    "source", "id", "slug", "title", "url", "topics", "difficulty", "language",
]
ATTEMPT_FIELDS = [
    "source", "id", "attempted_at", "result", "assistance", "minutes",
    "confidence", "debrief",
]
LEGACY_PROBLEM_FIELDS = [
    "source", "id", "slug", "title", "url", "topics", "patterns",
    "difficulty", "language", "status", "outcome", "attempts",
    "total_minutes", "confidence", "last_attempted", "next_review",
    "review_stage", "debrief",
]
RESULTS = {"correct", "incorrect"}
ASSISTANCE_LEVELS = {"none", "hint", "solution"}
DIFFICULTIES = {"", "easy", "medium", "hard"}
EXTENSIONS = {
    "c": "c",
    "c++": "cpp",
    "go": "go",
    "java": "java",
    "javascript": "js",
    "python": "py",
    "rust": "rs",
    "typescript": "ts",
}
SAFE_KEY = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class RegistryError(Exception):
    """A user-correctable registry error."""


def table_path(root, name):
    return root / "registry" / name


def write_table(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            newline="",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            delete=False,
        ) as file:
            temporary_path = Path(file.name)
            writer = csv.DictWriter(file, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        temporary_path.replace(path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def append_row(path, fields, row):
    with path.open("a", newline="", encoding="utf-8") as file:
        csv.DictWriter(file, fieldnames=fields, lineterminator="\n").writerow(row)


def create_table(path, fields):
    if not path.exists():
        write_table(path, fields, [])


def initialize(root):
    root.mkdir(parents=True, exist_ok=True)
    problems = table_path(root, "problems.csv")
    attempts = table_path(root, "attempts.csv")
    create_table(problems, PROBLEM_FIELDS)
    create_table(attempts, ATTEMPT_FIELDS)
    return {"problems": str(problems), "attempts": str(attempts)}


def read_table(path, expected_fields):
    if not path.exists():
        raise RegistryError(f"Missing {path}. Run init first.")
    with path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames != expected_fields:
            actual = ",".join(reader.fieldnames or [])
            expected = ",".join(expected_fields)
            raise RegistryError(
                f"Unexpected header in {path}: {actual!r}. Expected {expected!r}."
            )
        return list(reader)


def read_registry(root):
    problems = read_table(table_path(root, "problems.csv"), PROBLEM_FIELDS)
    attempts = read_table(table_path(root, "attempts.csv"), ATTEMPT_FIELDS)
    return problems, attempts


def ensure_current_registry(root):
    problems_path = table_path(root, "problems.csv")
    attempts_path = table_path(root, "attempts.csv")
    if not problems_path.exists() and not attempts_path.exists():
        initialize(root)
        return
    read_table(problems_path, PROBLEM_FIELDS)
    create_table(attempts_path, ATTEMPT_FIELDS)


def migrate_legacy(root):
    legacy_path = table_path(root, "problems.csv")
    attempts_path = table_path(root, "attempts.csv")
    backup_path = table_path(root, "problems.legacy.csv")
    if not legacy_path.exists():
        raise RegistryError(f"Missing {legacy_path}; nothing to migrate.")
    if backup_path.exists():
        raise RegistryError(f"Backup already exists: {backup_path}.")
    with legacy_path.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames == PROBLEM_FIELDS:
            raise RegistryError("Registry already uses the current schema.")
        if reader.fieldnames != LEGACY_PROBLEM_FIELDS:
            raise RegistryError("problems.csv does not match the supported legacy schema.")
        legacy_rows = list(reader)
    if attempts_path.exists():
        attempts = read_table(attempts_path, ATTEMPT_FIELDS)
        if attempts:
            raise RegistryError("Refusing migration because attempts.csv is not empty.")
    problems = []
    rows_with_attempts = 0
    for number, row in enumerate(legacy_rows, 2):
        problem = {field: row[field] for field in PROBLEM_FIELDS}
        problem["difficulty"] = problem["difficulty"].lower()
        problem["language"] = problem["language"].lower()
        problems.append(problem)
        try:
            rows_with_attempts += int(row["attempts"] or 0) > 0
        except ValueError as error:
            raise RegistryError(
                f"Invalid legacy attempts count at problems.csv row {number}."
            ) from error
    validate_rows(problems, [])
    shutil.copy2(legacy_path, backup_path)
    write_table(legacy_path, PROBLEM_FIELDS, problems)
    create_table(attempts_path, ATTEMPT_FIELDS)
    return {
        "backup": str(backup_path),
        "problems": len(problems),
        "legacy_rows_with_attempts": rows_with_attempts,
        "warning": (
            "Legacy aggregate attempt data remains in the backup; historical events "
            "cannot be reconstructed safely."
        ),
    }


def slugify(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def parse_day(value, field_name):
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise RegistryError(f"Invalid {field_name}: {value!r}; use YYYY-MM-DD.") from error


def validate_key(value, field_name):
    if not SAFE_KEY.fullmatch(value):
        raise RegistryError(
            f"Invalid {field_name}: {value!r}; use letters, numbers, dots, underscores, or hyphens."
        )


def bounded_limit(value):
    parsed = int(value)
    if parsed not in range(1, 101):
        raise argparse.ArgumentTypeError("limit must be between 1 and 100")
    return parsed


def problem_key(row):
    return row["source"], row["id"]


def find_problem(problems, source, problem_id):
    return next(
        (row for row in problems if problem_key(row) == (source, problem_id)),
        None,
    )


def workspace_path(root, problem):
    name = (
        problem["id"]
        if slugify(problem["id"]) == problem["slug"]
        else f"{problem['id']}-{problem['slug']}"
    )
    return root / "problems" / problem["source"] / name


def resolve_attempt_file(root, problem, file_name=None):
    language = problem["language"].lower()
    extension = EXTENSIONS.get(language)
    if extension is None and file_name is None:
        raise RegistryError(
            f"No default file extension for {problem['language']!r}; pass --file-name."
        )
    chosen_name = file_name or f"Solution.{extension}"
    if Path(chosen_name).name != chosen_name or chosen_name in {"", ".", ".."}:
        raise RegistryError("--file-name must be a plain file name, not a path.")
    return workspace_path(root, problem) / chosen_name


def create_attempt_file(attempt_file):
    attempt_file.parent.mkdir(parents=True, exist_ok=True)
    attempt_file.touch(exist_ok=True)
    return str(attempt_file)


def add_problem(args):
    root = Path(args.root).resolve()
    ensure_current_registry(root)
    problems, _ = read_registry(root)
    validate_key(args.source, "source")
    validate_key(args.id, "id")
    slug = args.slug or slugify(args.title)
    validate_key(slug, "slug")
    difficulty = args.difficulty.lower()
    if difficulty not in DIFFICULTIES:
        raise RegistryError("Difficulty must be easy, medium, hard, or blank.")
    row = {
        "source": args.source,
        "id": args.id,
        "slug": slug,
        "title": args.title,
        "url": args.url,
        "topics": args.topics,
        "difficulty": difficulty,
        "language": args.language.lower(),
    }
    attempt_file = (
        resolve_attempt_file(root, row, args.file_name)
        if args.workspace
        else None
    )
    existing = find_problem(problems, args.source, args.id)
    if existing is None:
        problems.append(row)
        write_table(table_path(root, "problems.csv"), PROBLEM_FIELDS, problems)
        action = "added"
    elif existing == row:
        action = "unchanged"
    else:
        raise RegistryError(
            f"Problem {args.source}/{args.id} already exists with different metadata."
        )
    output = {"action": action, "problem": row}
    if attempt_file is not None:
        output["attempt_file"] = create_attempt_file(attempt_file)
    return output


def append_attempt(args):
    root = Path(args.root).resolve()
    problems, attempts = read_registry(root)
    validate_rows(problems, attempts)
    if find_problem(problems, args.source, args.id) is None:
        raise RegistryError(f"Unknown problem: {args.source}/{args.id}.")
    attempted_at = args.on or date.today().isoformat()
    parse_day(attempted_at, "attempt date")
    if args.minutes < 0:
        raise RegistryError("Minutes must be zero or greater.")
    row = {
        "source": args.source,
        "id": args.id,
        "attempted_at": attempted_at,
        "result": args.result,
        "assistance": args.assistance,
        "minutes": str(args.minutes),
        "confidence": str(args.confidence),
        "debrief": args.debrief,
    }
    append_row(table_path(root, "attempts.csv"), ATTEMPT_FIELDS, row)
    return row


def review_interval(problem_attempts):
    latest = problem_attempts[-1]
    if latest["result"] != "correct" or latest["assistance"] != "none":
        return 1
    streak = 0
    for attempt in reversed(problem_attempts):
        if attempt["result"] == "correct" and attempt["assistance"] == "none":
            streak += 1
        else:
            break
    return (1, 7, 30)[min(streak, 3) - 1]


def due_items(args):
    root = Path(args.root).resolve()
    problems, attempts = read_registry(root)
    validate_rows(problems, attempts)
    as_of = parse_day(args.as_of or date.today().isoformat(), "as-of date")
    grouped = {}
    for attempt in attempts:
        grouped.setdefault(problem_key(attempt), []).append(attempt)
    output = []
    for problem in problems:
        history = sorted(grouped.get(problem_key(problem), []), key=lambda row: row["attempted_at"])
        if history:
            latest_day = parse_day(history[-1]["attempted_at"], "attempt date")
            due = latest_day + timedelta(days=review_interval(history))
        else:
            due = as_of
        if due <= as_of:
            output.append({
                "source": problem["source"],
                "id": problem["id"],
                "title": problem["title"],
                "topics": problem["topics"],
                "difficulty": problem["difficulty"],
                "language": problem["language"],
                "due": due.isoformat(),
                "attempts": len(history),
            })
    output.sort(key=lambda item: (item["due"], item["attempts"], item["source"], item["id"]))
    return output[:args.limit]


def validate_rows(problems, attempts):
    seen = set()
    for number, problem in enumerate(problems, 2):
        key = problem_key(problem)
        if key in seen:
            raise RegistryError(
                f"Duplicate problem at problems.csv row {number}: {key[0]}/{key[1]}."
            )
        seen.add(key)
        validate_key(problem["source"], f"source at problems.csv row {number}")
        validate_key(problem["id"], f"id at problems.csv row {number}")
        validate_key(problem["slug"], f"slug at problems.csv row {number}")
        if not problem["title"] or not problem["language"]:
            raise RegistryError(
                f"Problem at problems.csv row {number} requires title and language."
            )
        if problem["difficulty"] not in DIFFICULTIES:
            raise RegistryError(f"Invalid difficulty at problems.csv row {number}.")
    for number, attempt in enumerate(attempts, 2):
        key = problem_key(attempt)
        if key not in seen:
            raise RegistryError(
                f"Attempt at attempts.csv row {number} references unknown problem "
                f"{key[0]}/{key[1]}."
            )
        parse_day(attempt["attempted_at"], f"attempted_at at attempts.csv row {number}")
        if attempt["result"] not in RESULTS:
            raise RegistryError(f"Invalid result at attempts.csv row {number}.")
        if attempt["assistance"] not in ASSISTANCE_LEVELS:
            raise RegistryError(f"Invalid assistance at attempts.csv row {number}.")
        try:
            minutes = int(attempt["minutes"])
            confidence = int(attempt["confidence"])
        except ValueError as error:
            raise RegistryError(
                f"Minutes and confidence must be integers at attempts.csv row {number}."
            ) from error
        if minutes < 0 or confidence not in range(1, 6):
            raise RegistryError(f"Invalid minutes or confidence at attempts.csv row {number}.")
    return {"problems": len(problems), "attempts": len(attempts)}


def validate_registry(root):
    problems, attempts = read_registry(root)
    return validate_rows(problems, attempts)


def build_parser():
    parser = argparse.ArgumentParser(
        description="Maintain a plain-text DSA practice queue.",
        epilog=(
            "Example: manage_registry.py due --root ./dsa-practice --limit 5\n"
            "Run any subcommand with --help for its arguments."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="Create missing registry tables.")
    init.add_argument("--root", required=True)

    migrate = commands.add_parser("migrate", help="Migrate the legacy 18-column registry.")
    migrate.add_argument("--root", required=True)

    add = commands.add_parser("add", help="Add one problem idempotently.")
    add.add_argument("--root", required=True)
    add.add_argument("--source", required=True)
    add.add_argument("--id", required=True)
    add.add_argument("--slug")
    add.add_argument("--title", required=True)
    add.add_argument("--url", default="")
    add.add_argument("--topics", default="")
    add.add_argument("--difficulty", default="", choices=["easy", "medium", "hard"])
    add.add_argument("--language", required=True)
    add.add_argument("--workspace", action="store_true")
    add.add_argument("--file-name")

    attempt = commands.add_parser("attempt", help="Append one practice event.")
    attempt.add_argument("--root", required=True)
    attempt.add_argument("--source", required=True)
    attempt.add_argument("--id", required=True)
    attempt.add_argument("--result", required=True, choices=sorted(RESULTS))
    attempt.add_argument("--assistance", required=True, choices=sorted(ASSISTANCE_LEVELS))
    attempt.add_argument("--minutes", required=True, type=int)
    attempt.add_argument("--confidence", required=True, type=int, choices=range(1, 6))
    attempt.add_argument("--debrief", default="")
    attempt.add_argument("--on", help="Attempt date in YYYY-MM-DD; defaults to today.")

    due = commands.add_parser("due", help="Print a bounded due queue as JSON.")
    due.add_argument("--root", required=True)
    due.add_argument("--limit", type=bounded_limit, default=5, metavar="N")
    due.add_argument("--as-of", help="Queue date in YYYY-MM-DD; defaults to today.")

    check = commands.add_parser("validate", help="Validate schemas and values.")
    check.add_argument("--root", required=True)
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "init":
            output = initialize(Path(args.root).resolve())
        elif args.command == "migrate":
            output = migrate_legacy(Path(args.root).resolve())
        elif args.command == "add":
            output = add_problem(args)
        elif args.command == "attempt":
            output = append_attempt(args)
        elif args.command == "due":
            output = due_items(args)
        else:
            output = validate_registry(Path(args.root).resolve())
        print(json.dumps(output, indent=2, sort_keys=True))
    except RegistryError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
