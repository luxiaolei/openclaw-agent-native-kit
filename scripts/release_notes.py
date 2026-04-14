#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

CHANGELOG = Path(__file__).resolve().parents[1] / "CHANGELOG.md"
SECTION_RE = re.compile(r"^## \[(?P<version>[^\]]+)\].*$", re.MULTILINE)


def normalize(version: str) -> str:
    return version.strip().lstrip("v")


def extract_release_notes(changelog: str, version: str) -> str:
    normalized = normalize(version)
    matches = list(SECTION_RE.finditer(changelog))
    for index, match in enumerate(matches):
        if normalize(match.group("version")) != normalized:
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(changelog)
        body = changelog[start:end].strip()
        if not body:
            raise ValueError(f"No release notes body found for version {version}")
        return f"## [{normalized}]\n\n{body}\n"
    raise ValueError(f"Version {version} not found in {CHANGELOG}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/release_notes.py <tag-or-version>", file=sys.stderr)
        return 1

    version = sys.argv[1]
    changelog = CHANGELOG.read_text(encoding="utf-8")
    try:
        notes = extract_release_notes(changelog, version)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    sys.stdout.write(notes)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
