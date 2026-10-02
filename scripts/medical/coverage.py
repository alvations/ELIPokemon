#!/usr/bin/env python3
"""Print what a specialty already covers, as its questions, for writing a wave brief.

This exists because of a specific, reproducible mistake. A wave brief told a nursing
writer that eight topics were available, and three of them were already written —
pressure ulcers in m004, fluid balance in m005, medicines administration in m003.
The brief's summary of existing coverage had been assembled from the *device* column
of ``CONVENTIONS.md`` Part II rather than from the *question* column of
``questions.tsv``. Part II is indexed by device because that is what a writer needs
for reuse, and reading it as a topic index reliably under-reports coverage: m004
alone absorbs two of the eight offered topics and Part II renders it as "Something
that extends a state rather than causing it — Damp Rock".

The writer caught it, declined all three, and noted that an eight-for-five list with
three dead entries leaves a writer no slack if they also need to decline one on
taste grounds. So: never write a territory list from the devices. Run this.

    python3 scripts/medical/coverage.py                # every specialty
    python3 scripts/medical/coverage.py nursing        # one
    python3 scripts/medical/coverage.py --next nursing # and the next free ID block
"""

from __future__ import annotations

import csv
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
CATALOGUE = ROOT / "domains" / "medical" / "questions" / "questions.tsv"
SPECIALTIES = (
    "nursing",
    "pharmacology",
    "general-practice",
    "dermatology",
    "endocrinology",
    "oncology",
    "emergency",
)


def rows() -> list[dict[str, str]]:
    with CATALOGUE.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main(argv: list[str]) -> int:
    want_next = "--next" in argv
    names = [a for a in argv if not a.startswith("--")] or list(SPECIALTIES)
    all_rows = rows()
    taken = sorted(int(r["id"][1:]) for r in all_rows)
    for name in names:
        group = [r for r in all_rows if r["category"] == name]
        print(f"\n=== {name} — {len(group)} of 100 written\n")
        for r in sorted(group, key=lambda r: r["id"]):
            print(f"  {r['id']}  {r['slug']}")
            print(f"        {r['question']}")
        if want_next:
            n = 1
            while n in taken:
                n += 1
            block = []
            while len(block) < 5:
                if n not in taken:
                    block.append(n)
                n += 1
            print(f"\n  next free IDs: {', '.join('m%03d' % i for i in block)}")
    print(
        f"\ntotal {len(all_rows)} of 700. "
        "Read the question text, not the device, before offering a topic as new."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
