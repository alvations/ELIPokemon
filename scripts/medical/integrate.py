#!/usr/bin/env python3
"""Integrate a writer's worktree into the main checkout, without hand-rolled greps.

Every integration before this one was improvised shell, and each improvisation had a
different bug:

  * A grep for ``^+m0`` to pull new catalogue rows out of a diff silently matched
    nothing from m100 upward, so five emergency pairs and one oncology pair sat in the
    tree fully written, fully valid and absent from the catalogue.
  * A ``git checkout --`` meant to undo a test reverted twenty recovered catalogue rows
    that were staged but not committed.
  * Copying a worktree's whole diff against main, rather than its own new files, would
    have reverted three commits of central fixes, because the worktree was branched from
    an older main.

So: this reads the worktree's own commits for the files *it added*, copies exactly those,
takes catalogue rows from the worktree's catalogue rather than from a diff, and merges
them by id. It never deletes and never reverts.

    python3 scripts/medical/integrate.py <worktree-path> [--base <ref>] [--dry-run]

``--base`` is the commit the writer branched from; the default is the merge-base with
HEAD, which is right whether or not they rebased.
"""

from __future__ import annotations

import csv
import subprocess
import sys
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parents[2]
CATALOGUE = ROOT / "domains" / "medical" / "questions" / "questions.tsv"
FIELDS = ("id", "slug", "category", "difficulty", "question")


def git(*args: str, cwd: pathlib.Path = ROOT) -> str:
    return subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, check=True
    ).stdout


def main(argv: list[str]) -> int:
    paths = [a for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    wt = pathlib.Path(paths[0]).resolve()
    if not (wt / ".git").exists():
        print(f"not a worktree: {wt}")
        return 1
    dry = "--dry-run" in argv
    base = argv[argv.index("--base") + 1] if "--base" in argv else None
    if base is None:
        # The merge-base of the worktree's HEAD and the main checkout's HEAD. Run from the
        # main checkout with the worktree's commit named explicitly, because `git merge-base
        # HEAD --` inside a worktree is not a valid invocation.
        wt_head = git("rev-parse", "HEAD", cwd=wt).strip()
        main_head = git("rev-parse", "HEAD").strip()
        try:
            base = git("merge-base", wt_head, main_head).strip()
        except subprocess.CalledProcessError:
            base = main_head

    # Files this worktree ADDED, across every commit it carries. Added only: a modified
    # file may be a central fix the worktree predates, and copying it would revert that.
    added = [
        line.split("\t", 1)[1]
        for line in git("diff", "--name-status", "--diff-filter=A", base, "HEAD",
                        "--", "domains/medical/answers", cwd=wt).splitlines()
        if line.startswith("A\t")
    ]
    modified = [
        line.split("\t", 1)[1]
        for line in git("diff", "--name-status", "--diff-filter=M", base, "HEAD",
                        "--", "domains/medical/answers", cwd=wt).splitlines()
        if line.startswith("M\t")
    ]

    print(f"worktree : {wt.name}")
    print(f"base     : {base[:12]}")
    print(f"added    : {len(added)} answer files")
    if modified:
        print(f"modified : {len(modified)} — NOT copied automatically, listed below")
        for m in modified:
            print(f"           {m}")
        print("           (a modified file may be a central fix this worktree predates;"
              " copy any you want by hand after reading the diff)")

    # Catalogue rows: read the worktree's own catalogue, not a diff of it.
    wt_rows = {r["id"]: r for r in csv.DictReader((wt / CATALOGUE.relative_to(ROOT)).open(), delimiter="\t")}
    main_rows = {r["id"]: r for r in csv.DictReader(CATALOGUE.open(), delimiter="\t")}
    new_ids = sorted(set(wt_rows) - set(main_rows))
    conflicts = [i for i in set(wt_rows) & set(main_rows) if wt_rows[i] != main_rows[i]]
    print(f"new rows : {len(new_ids)}  {', '.join(new_ids) if new_ids else '(none)'}")
    if conflicts:
        print(f"CONFLICT : {len(conflicts)} id(s) differ between the two catalogues: "
              f"{', '.join(sorted(conflicts))}")
        print("           refusing to merge; resolve by hand")
        return 1

    # Every added answer must have a row, and every new row two answers.
    ids_from_files = {pathlib.Path(f).name.split("-")[0] for f in added}
    missing_rows = sorted(ids_from_files - set(wt_rows))
    if missing_rows:
        print(f"REFUSING : answer files with no catalogue row in the worktree: "
              f"{', '.join(missing_rows)}")
        return 1
    for i in new_ids:
        n = sum(1 for f in added if pathlib.Path(f).name.startswith(f"{i}-"))
        if n != 2:
            print(f"REFUSING : {i} has {n} added answer file(s), expected 2")
            return 1

    if dry:
        print("\n--dry-run: nothing written")
        return 0

    for f in added:
        dst = ROOT / f
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(wt / f, dst)

    merged = dict(main_rows)
    merged.update({i: wt_rows[i] for i in new_ids})
    with CATALOGUE.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for i in sorted(merged):
            w.writerow(merged[i])

    print(f"\ncopied {len(added)} files; catalogue now {len(merged)} rows")
    print("next: validate.py, then build_dataset.py, then commit")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
