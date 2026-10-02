#!/usr/bin/env python3
"""Build the medical-domain artifacts from the markdown source of truth.

Reads:
    domains/medical/questions/questions.tsv
    domains/medical/answers/<specialty>/serious/<id>-<slug>.md
    domains/medical/answers/<specialty>/pokemon/<id>-<slug>.md

Writes:
    domains/medical/questions/index.json
    domains/medical/dataset/elipokemon-medical.jsonl

The record schema is deliberately identical to the machine-learning domain's, so
the two JSONL files can be concatenated and loaded as one set.
"""

from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DOMAIN = ROOT / "domains" / "medical"
CATALOGUE = DOMAIN / "questions" / "questions.tsv"
STYLES = ("serious", "pokemon")

# Fixed on purpose. A specialty outside this set is a validation failure, not a
# new folder: the domain's scope is a decision, not a side effect of a typo.
SPECIALTIES = (
    "nursing",
    "pharmacology",
    "general-practice",
    "dermatology",
    "endocrinology",
    "oncology",
    "emergency",
)


def read_catalogue() -> list[dict]:
    rows = CATALOGUE.read_text(encoding="utf-8").splitlines()
    header = rows[0].split("\t")
    entries = []
    for line in rows[1:]:
        if not line.strip():
            continue
        entries.append(dict(zip(header, line.split("\t"))))
    return entries


def split_front_matter(text: str) -> tuple[dict, str]:
    """Return (front matter dict, body). Front matter is a flat YAML subset."""
    if not text.startswith("---\n"):
        return {}, text
    _, raw, body = text.split("---\n", 2)
    meta: dict = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            meta[key.strip()] = [v.strip().strip("\"'") for v in inner.split(",") if v.strip()]
        else:
            meta[key.strip()] = value.strip("\"'")
    return meta, body.lstrip("\n")


def answer_path(style: str, entry: dict) -> pathlib.Path:
    return DOMAIN / "answers" / entry["category"] / style / f"{entry['id']}-{entry['slug']}.md"


def main() -> int:
    entries = read_catalogue()
    index, records, missing = [], [], []

    for entry in entries:
        record = {
            "id": entry["id"],
            "slug": entry["slug"],
            "question": entry["question"],
            "category": entry["category"],
            "difficulty": entry["difficulty"],
            "domain": "medical",
        }
        item = dict(record)
        tags: list[str] = []
        for style in STYLES:
            path = answer_path(style, entry)
            if not path.exists():
                missing.append(str(path.relative_to(ROOT)))
                continue
            meta, body = split_front_matter(path.read_text(encoding="utf-8"))
            tags = meta.get("tags", tags) or tags
            record[f"answer_{style}"] = body.rstrip() + "\n"
            item[f"{style}_path"] = str(path.relative_to(ROOT))
        record["tags"] = tags
        item["tags"] = tags
        index.append(item)
        if all(f"answer_{style}" in record for style in STYLES):
            records.append(record)

    (DOMAIN / "questions" / "index.json").write_text(
        json.dumps({"count": len(index), "questions": index}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (DOMAIN / "dataset").mkdir(exist_ok=True)
    out = DOMAIN / "dataset" / "elipokemon-medical.jsonl"
    with out.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")

    print(f"catalogue : {len(entries)} questions")
    print(f"complete  : {len(records)} question/answer pairs written to {out.relative_to(ROOT)}")
    if missing:
        print(f"missing   : {len(missing)} answer files")
        for path in missing[:10]:
            print(f"            - {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
