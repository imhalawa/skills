#!/usr/bin/env python3
"""Maintain the dsa-practice CSV registry and its Excel view."""

import argparse
import csv
import re
from collections import Counter
from datetime import date, timedelta
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile


FIELDS = [
    "source", "id", "slug", "title", "url", "topics", "patterns", "difficulty",
    "language", "status", "outcome", "attempts", "total_minutes", "confidence",
    "last_attempted", "next_review", "review_stage", "debrief",
]
EXTENSIONS = {"java": "java", "python": "py", "javascript": "js", "typescript": "ts", "go": "go", "rust": "rs", "c++": "cpp", "c": "c"}


def registry_path(root):
    return root / "registry" / "problems.csv"


def read_rows(root):
    path = registry_path(root)
    if not path.exists():
        raise SystemExit(f"Registry not found: {path}. Run init first.")
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def write_rows(root, rows):
    path = registry_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)


def initialize(root):
    root.mkdir(parents=True, exist_ok=True)
    path = registry_path(root)
    if not path.exists():
        write_rows(root, [])
    print(path)


def slugify(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def add_problem(args):
    root = Path(args.root).resolve()
    initialize(root)
    rows = read_rows(root)
    if any(row["source"] == args.source and row["id"] == args.id for row in rows):
        raise SystemExit(f"Problem already exists: {args.source}/{args.id}")
    row = {field: "" for field in FIELDS}
    row.update({
        "source": args.source,
        "id": args.id,
        "slug": args.slug or slugify(args.title),
        "title": args.title,
        "url": args.url,
        "topics": args.topics,
        "patterns": args.patterns,
        "difficulty": args.difficulty,
        "language": args.language,
        "status": "in-progress",
        "attempts": "0",
        "total_minutes": "0",
    })
    rows.append(row)
    write_rows(root, rows)
    if args.workspace:
        extension = EXTENSIONS.get(args.language.lower(), args.language.lower())
        file_name = args.file_name or f"Solution.{extension}"
        workspace_name = args.id if slugify(args.id) == row["slug"] else f"{args.id}-{row['slug']}"
        workspace = root / "problems" / args.source / workspace_name
        workspace.mkdir(parents=True, exist_ok=False)
        (workspace / file_name).touch()
        print(workspace)


def record_attempt(args):
    root = Path(args.root).resolve()
    rows = read_rows(root)
    row = next((item for item in rows if item["source"] == args.source and item["id"] == args.id), None)
    if row is None:
        raise SystemExit(f"Unknown problem: {args.source}/{args.id}")
    today = date.today()
    attempts = int(row["attempts"] or 0) + 1
    total_minutes = int(row["total_minutes"] or 0) + args.minutes
    needs_review = args.outcome != "independent" or args.confidence < 4
    stage = int(row["review_stage"] or 0)
    if needs_review:
        stage = min(stage + 1, 3)
        days = (1, 7, 30)[stage - 1]
        next_review = (today + timedelta(days=days)).isoformat()
    else:
        stage = 0
        next_review = ""
    row.update({
        "status": "solved" if args.outcome == "independent" else "review",
        "outcome": args.outcome,
        "attempts": str(attempts),
        "total_minutes": str(total_minutes),
        "confidence": str(args.confidence),
        "last_attempted": today.isoformat(),
        "next_review": next_review,
        "review_stage": str(stage),
        "debrief": args.debrief,
    })
    write_rows(root, rows)


def inline_cell(reference, value, style=None):
    style_attribute = f' s="{style}"' if style is not None else ""
    if value == "":
        return f'<c r="{reference}"{style_attribute}/>'
    return f'<c r="{reference}" t="inlineStr"{style_attribute}><is><t>{escape(str(value))}</t></is></c>'


def row_xml(number, cells):
    return f'<row r="{number}">{"".join(cells)}</row>'


def sheet_xml(headers, values):
    letters = [chr(ord("A") + index) for index in range(len(headers))]
    rows = [row_xml(1, [inline_cell(f"{letter}1", value, 1) for letter, value in zip(letters, headers)])]
    for number, values_row in enumerate(values, 2):
        rows.append(row_xml(number, [inline_cell(f"{letter}{number}", value, 2) for letter, value in zip(letters, values_row)]))
    last = f"{letters[-1]}{max(2, len(values) + 1)}"
    columns = "".join(f'<col min="{index}" max="{index}" width="20" customWidth="1"/>' for index in range(1, len(headers) + 1))
    return f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">
<dimension ref="A1:{last}"/><sheetViews><sheetView workbookViewId="0"><pane ySplit="1" topLeftCell="A2" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>
<sheetFormatPr defaultRowHeight="15"/><cols>{columns}</cols><sheetData>{"".join(rows)}</sheetData><autoFilter ref="A1:{last}"/></worksheet>'''


def export_xlsx(args):
    root = Path(args.root).resolve()
    rows = read_rows(root)
    problem_values = [[item[field] for field in FIELDS] for item in rows]
    topics = Counter()
    for item in rows:
        for topic in filter(None, (value.strip() for value in item["topics"].split(","))):
            topics[topic] += 1
    output = root / "registry" / "dsa-problem-tracker.xlsx"
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/><Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override PartName="/xl/worksheets/sheet2.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/><Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/></Types>'''
    root_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>'''
    workbook = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Problems" sheetId="1" r:id="rId1"/><sheet name="Topics" sheetId="2" r:id="rId2"/></sheets></workbook>'''
    workbook_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/><Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"/><Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>'''
    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><fonts count="2"><font><sz val="11"/><name val="Calibri"/></font><font><b/><color rgb="FFFFFFFF"/><sz val="11"/><name val="Calibri"/></font></fonts><fills count="3"><fill><patternFill patternType="none"/></fill><fill><patternFill patternType="gray125"/></fill><fill><patternFill patternType="solid"><fgColor rgb="FF1F4E78"/><bgColor indexed="64"/></patternFill></fill></fills><borders count="1"><border><left/><right/><top/><bottom/><diagonal/></border></borders><cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs><cellXfs count="3"><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/><xf numFmtId="0" fontId="1" fillId="2" borderId="0" xfId="0" applyFont="1" applyFill="1"/><xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0" applyAlignment="1"><alignment wrapText="1" vertical="top"/></xf></cellXfs></styleSheet>'''
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", root_rels)
        archive.writestr("xl/workbook.xml", workbook)
        archive.writestr("xl/_rels/workbook.xml.rels", workbook_rels)
        archive.writestr("xl/worksheets/sheet1.xml", sheet_xml(FIELDS, problem_values))
        archive.writestr("xl/worksheets/sheet2.xml", sheet_xml(["topic", "problems"], [[topic, str(count)] for topic, count in sorted(topics.items())]))
        archive.writestr("xl/styles.xml", styles)
    print(output)


def validate(root):
    rows = read_rows(root)
    duplicates = [(row["source"], row["id"]) for row in rows]
    if len(duplicates) != len(set(duplicates)):
        raise SystemExit("Duplicate source/id entries in registry.")
    for row in rows:
        if not row["source"] or not row["id"] or not row["language"]:
            raise SystemExit("Each row requires source, id, and language.")
    print(f"Validated {len(rows)} problem records.")


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init")
    init.add_argument("--root", required=True)
    add = commands.add_parser("add")
    add.add_argument("--root", required=True)
    add.add_argument("--source", required=True)
    add.add_argument("--id", required=True)
    add.add_argument("--slug")
    add.add_argument("--title", required=True)
    add.add_argument("--url", default="")
    add.add_argument("--topics", default="")
    add.add_argument("--patterns", default="")
    add.add_argument("--difficulty", default="")
    add.add_argument("--language", required=True)
    add.add_argument("--workspace", action="store_true")
    add.add_argument("--file-name")
    attempt = commands.add_parser("attempt")
    attempt.add_argument("--root", required=True)
    attempt.add_argument("--source", required=True)
    attempt.add_argument("--id", required=True)
    attempt.add_argument("--outcome", required=True, choices=["independent", "hint", "studied-solution"])
    attempt.add_argument("--minutes", required=True, type=int)
    attempt.add_argument("--confidence", required=True, type=int, choices=range(1, 6))
    attempt.add_argument("--debrief", default="")
    export = commands.add_parser("export-xlsx")
    export.add_argument("--root", required=True)
    check = commands.add_parser("validate")
    check.add_argument("--root", required=True)
    args = parser.parse_args()
    if args.command == "init":
        initialize(Path(args.root).resolve())
    elif args.command == "add":
        add_problem(args)
    elif args.command == "attempt":
        record_attempt(args)
    elif args.command == "export-xlsx":
        export_xlsx(args)
    else:
        validate(Path(args.root).resolve())


if __name__ == "__main__":
    main()
