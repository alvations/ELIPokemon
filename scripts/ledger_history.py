#!/usr/bin/env python3
"""Replay the Pokémon-ness ledger across git history.

    python3 scripts/ledger_history.py

Reads the headline line out of every committed version of LEDGER.md, so the
score trend is recoverable from the repository itself rather than from anyone's
notes. Commits made before the ledger existed are skipped.
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
HEADLINE = re.compile(
    r"\*\*(\d+) answers · mean ([\d.]+) · median ([\d.]+) · min ([\d.]+)"
)


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True
    ).stdout


def main() -> int:
    commits = git("log", "--reverse", "--format=%h\t%s", "--", "LEDGER.md").splitlines()
    if not commits:
        print("No committed LEDGER.md yet — run scripts/pokemon_score.py and commit it.")
        return 1

    print(f"{'commit':<9} {'mean':>6} {'median':>7} {'min':>6}  subject")
    print("-" * 78)
    previous = None
    for line in commits:
        sha, subject = line.split("\t", 1)
        try:
            blob = git("show", f"{sha}:LEDGER.md")
        except subprocess.CalledProcessError:
            continue
        match = HEADLINE.search(blob)
        if not match:
            continue
        _, mean, median, low = (float(g) for g in match.groups()[0:1] + match.groups()[1:])
        delta = f"  ({mean - previous:+.1f})" if previous is not None else ""
        print(f"{sha:<9} {mean:>6.1f} {median:>7.1f} {low:>6.1f}  {subject[:44]}{delta}")
        previous = mean
    return 0


if __name__ == "__main__":
    sys.exit(main())
