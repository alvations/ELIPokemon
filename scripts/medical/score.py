#!/usr/bin/env python3
"""Score the Pokemon-ness of the medical domain's Pokemon answers.

Reuses the machine-learning domain's deterministic scorer unchanged -- the measure is
"does this lean on named entities rather than generic furniture", which is a property of
the Pokemon writing and not of the subject matter. Importing rather than copying keeps a
single vocabulary, so a vocabulary fix lands in both domains at once.

Usage:
    python3 scripts/medical/score.py            # table, grouped by specialty
    python3 scripts/medical/score.py --json
    python3 scripts/medical/score.py --detail m001
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from pokemon_score import band, body_of, score_text  # noqa: E402
from build_dataset import DOMAIN, SPECIALTIES  # noqa: E402


def all_scores() -> list[dict]:
    rows = []
    for specialty in SPECIALTIES:
        folder = DOMAIN / "answers" / specialty / "pokemon"
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            qid, slug = path.stem.split("-", 1)
            r = score_text(body_of(path))
            r.update({"id": qid, "slug": slug, "specialty": specialty})
            rows.append(r)
    return sorted(rows, key=lambda r: r["id"])


def main() -> int:
    args = sys.argv[1:]
    if "--detail" in args:
        qid = args[args.index("--detail") + 1]
        for r in all_scores():
            if r["id"] == qid:
                print(json.dumps(r, indent=2, ensure_ascii=False))
                return 0
        print(f"no answer with id {qid}")
        return 1
    rows = all_scores()
    if "--json" in args:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0
    if not rows:
        print("no Pokemon answers yet")
        return 0
    for specialty in SPECIALTIES:
        group = [r for r in rows if r["specialty"] == specialty]
        if not group:
            continue
        mean = sum(r["score"] for r in group) / len(group)
        print(f"\n{specialty}  ({len(group)} answers, mean {mean:.1f})")
        for r in group:
            print(f"  {r['score']:>5.1f}  {band(r['score']):<10}  {r['id']}  {r['slug']}")
    scores = sorted(r["score"] for r in rows)
    mean = sum(scores) / len(scores)
    print(
        f"\nmedical domain: {len(scores)} answers, mean {mean:.1f}, "
        f"median {scores[len(scores) // 2]:.1f}, min {scores[0]:.1f}, max {scores[-1]:.1f}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
