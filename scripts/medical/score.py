#!/usr/bin/env python3
"""Score the Pokemon-ness of the medical domain's Pokemon answers.

Reuses the machine-learning domain's deterministic scorer unchanged -- the measure is
"does this lean on named entities rather than generic furniture", which is a property of
the Pokemon writing and not of the subject matter. Importing rather than copying keeps a
single vocabulary, so a vocabulary fix lands in both domains at once.

Usage:
    python3 scripts/medical/score.py            # table, grouped by specialty; rewrites LEDGER.md
    python3 scripts/medical/score.py --write    # just rewrite the ledger
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

# Sections this domain *requires* and requires to be free of analogy. Scoring them
# would penalise an answer for complying: three writers independently reported the
# house pattern costing 1-4 points, which made the gate punish the behaviour the
# brief asks for. An answer is measured on its analogy-bearing body instead.
EXCLUDED_SECTIONS = (
    "## Where the metaphor stops",
    "## The human stakes, said plainly",
    "## And here the Pokémon framing stops",
    "## Where the game stops",
    "## Sources",
    "## Scope and safety",
)


def scorable_body(path: pathlib.Path) -> str:
    """The body with the mandated plain-prose sections removed."""
    body = body_of(path)
    out, skipping = [], False
    for line in body.splitlines():
        if line.startswith("## "):
            skipping = any(line.startswith(h) for h in EXCLUDED_SECTIONS)
        if not skipping:
            out.append(line)
    return "\n".join(out)


def write_ledger(rows: list[dict]) -> pathlib.Path:
    """Write the domain's ledger, so its diff is the change in Pokemon-ness.

    The machine-learning domain has had one since early on; this one had none, which
    meant no committed artefact to read a re-baselining against.
    """
    scores = sorted(r["score"] for r in rows)
    mean = sum(scores) / len(scores) if scores else 0.0
    lines = [
        "# Pokémon-ness ledger — medical domain",
        "",
        "How much each Pokémon answer leans on **named** Pokémon entities rather than generic",
        "furniture. Same deterministic scorer as the machine-learning domain, same vocabulary, so",
        "the two are comparable and a vocabulary fix moves both.",
        "",
        "**The mandated plain-prose sections are excluded from scoring** — `Where the metaphor",
        "stops`, `The human stakes, said plainly`, `Sources` and `Scope and safety`. They are",
        "required to contain no analogy, so scoring them would penalise an answer for complying.",
        "",
        "Regenerate with `python3 scripts/medical/score.py --write`.",
        "",
        f"**{len(rows)} answers · mean {mean:.1f} · median {scores[len(scores)//2]:.1f} · "
        f"min {scores[0]:.1f} · max {scores[-1]:.1f}**" if rows else "**no answers yet**",
        "",
        "| score | band | id | specialty | answer | distinct | named | generic |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in sorted(rows, key=lambda r: r["score"]):
        lines.append(
            f"| {r['score']:.1f} | {band(r['score'])} | {r['id']} | {r['specialty']} | "
            f"{r['slug']} | {r['distinct']} | {r['named_mentions']} | {r['generic_mentions']} |"
        )
    out = DOMAIN / "LEDGER.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def all_scores() -> list[dict]:
    rows = []
    for specialty in SPECIALTIES:
        folder = DOMAIN / "answers" / specialty / "pokemon"
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.md")):
            qid, slug = path.stem.split("-", 1)
            r = score_text(scorable_body(path))
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
    if "--write" in args or not args:
        out = write_ledger(rows)
        if "--write" in args:
            print(f"wrote {out.relative_to(ROOT)}")
            return 0
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
