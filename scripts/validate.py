#!/usr/bin/env python3
"""Validate the ELIPokemon dataset source files.

Checks, for every question in questions/questions.tsv:
  * both answer files exist;
  * front matter is present and its id/slug/style/question agree with the catalogue;
  * the body is non-trivial and starts with an H1;
  * serious answers contain at least one fenced ASCII diagram.

Exits non-zero if anything fails, so it can be wired straight into CI.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_dataset import ROOT, STYLES, answer_path, read_catalogue, split_front_matter  # noqa: E402

MIN_WORDS = 120


def main() -> int:
    problems: list[str] = []
    entries = read_catalogue()

    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()
    for entry in entries:
        if entry["id"] in seen_ids:
            problems.append(f"duplicate id {entry['id']}")
        if entry["slug"] in seen_slugs:
            problems.append(f"duplicate slug {entry['slug']}")
        seen_ids.add(entry["id"])
        seen_slugs.add(entry["slug"])

        for style in STYLES:
            path = answer_path(style, entry)
            rel = path.relative_to(ROOT)
            if not path.exists():
                problems.append(f"{rel}: missing")
                continue
            meta, body = split_front_matter(path.read_text(encoding="utf-8"))
            if not meta:
                problems.append(f"{rel}: missing front matter")
                continue
            for key, expected in (("id", entry["id"]), ("slug", entry["slug"]), ("style", style)):
                if meta.get(key) != expected:
                    problems.append(f"{rel}: front matter {key}={meta.get(key)!r}, expected {expected!r}")
            if meta.get("question") != entry["question"]:
                problems.append(f"{rel}: front matter question does not match the catalogue")
            if not body.startswith("# "):
                problems.append(f"{rel}: body should start with an H1 heading")
            if len(body.split()) < MIN_WORDS:
                problems.append(f"{rel}: body is only {len(body.split())} words (min {MIN_WORDS})")
            if style == "serious" and "```" not in body:
                problems.append(f"{rel}: serious answers must include a fenced ASCII diagram")

    if problems:
        print(f"FAILED: {len(problems)} problem(s)")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print(f"OK: {len(entries)} questions, {len(entries) * len(STYLES)} answer files validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
