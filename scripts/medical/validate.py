#!/usr/bin/env python3
"""Validate the medical domain's source files. Blocking: run before every commit.

Carries the machine-learning domain's checks:
  * both answer files exist;
  * front matter id/slug/style/question agree with the catalogue;
  * the body starts with an H1 and is non-trivial;
  * serious answers contain at least one fenced diagram.

And three the medical domain adds, because the failure modes here are different:
  * the specialty must be one of the seven this domain covers, so a typo creates a
    validation error rather than a silent eighth folder;
  * EVERY answer, both halves, must carry a "## Scope and safety" section. An
    answer about clinical material that does not say what it is not for is a
    defect, and this is the only way to guarantee none ships without one;
  * no answer may address the reader as their clinician -- the second person
    paired with an imperative about their own treatment. Teaching material
    explains what is done and why; it does not instruct a reader about their own
    care. The check is deliberately crude and over-flags.

And two about sourcing, because no medical authority is reachable from the build
environment and the only honest response to that is to say so in every answer:
  * every answer must carry a "## Sources" section naming the documents that would
    settle its claims, headed by the verbatim statement that none was retrieved;
  * nothing may read as a quotation from a source that was not opened -- no
    "the guideline states \u2018...\u2019", no DOIs, no author-year citations, no
    guideline reference codes. A fabricated medical citation is the most damaging
    single defect this dataset could contain.
"""

from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_dataset import (  # noqa: E402
    DOMAIN,
    ROOT,
    SPECIALTIES,
    STYLES,
    answer_path,
    read_catalogue,
    split_front_matter,
)

MIN_WORDS = 120
SAFETY_HEADING = "## Scope and safety"
SOURCES_HEADING = "## Sources"

# No medical authority is reachable from the build environment -- who.int, cdc.gov,
# nice.org.uk, pubmed, the formularies and the resuscitation councils are all refused
# by the egress proxy. So every answer must name the documents that would settle its
# claims AND state plainly that none of them was opened. An answer that cited a source
# it could not read would be worse than one that cited nothing.
NOT_RETRIEVED = "**None of the sources below was retrieved.**"

# The house pattern: every pair carries one section with the analogy dropped, where the
# stakes are stated plainly. The Pokemon half announces that the metaphor stops; the
# serious half says what is at stake for a person. BRIEF.md has always claimed the
# validator enforced this and until now it did not, which is how five pairs shipped under
# five bespoke headings and one shipped with no such section at all.
# Relative links inside an answer. Five writers in one wave pointed at
# SOURCES-<specialty>.md two levels up instead of three and produced fifty broken
# links, because the brief named the file without giving the path from an answer.
# The brief says the path now; this makes a wrong one impossible to ship.
# CommonMark fence rules, not a loose prefix match. The first version of this check used
# r"^\s*(```|~~~)" and immediately reported two false positives, because a diagram line of
# ASCII art -- "   ~~~~~~~~ stratum corneum ~~~~~~~~" inside a backtick fence -- matched the
# tilde alternative and was read as a closing fence at the wrong indent. A fence closer is
# the same character as its opener, at least as long, and alone on its line.
FENCE_OPEN = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([^`]*)$")
FENCE_SHUT = re.compile(r"^(\s*)(`{3,}|~{3,})\s*$")
LINK = re.compile(r"\]\((?!https?:)([^)#\s]+)")

STAKES_HEADING = {
    "pokemon": "## Where the metaphor stops",
    "serious": "## The human stakes, said plainly",
}

# Anything that presents un-retrieved source text as a quotation. These are the
# fabrication shapes, and in medical content a fabricated citation is the most
# damaging single defect available.
FABRICATED_CITATION = re.compile(
    r"(guideline|guidance|monograph|formulary|standard|consensus|statement|review)\s+"
    r"(?:states|says|reads|notes|recommends)\s*[:,]?\s*[\"\u201c]"
    r"|\bdoi:\s*10\."
    r"|\bet al\.\s*\(?\d{4}"
    r"|\b(?:NG|CG|QS|TA|DG)\d{2,4}\b",
    re.IGNORECASE,
)

# Phrases that would make the text read as direction to a patient rather than
# explanation to a student. Matched case-insensitively against the body.
PATIENT_DIRECTIVE = re.compile(
    r"\b(you should (?:take|stop|start|inject|apply|double)|"
    r"take \d+\s*(?:mg|mcg|g|ml|units)|"
    r"your dose (?:is|should be)|"
    r"stop taking your)\b",
    re.IGNORECASE,
)


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

        if entry["category"] not in SPECIALTIES:
            problems.append(
                f"{entry['id']}: specialty {entry['category']!r} is not one of {', '.join(SPECIALTIES)}"
            )
            continue

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
                problems.append(f"{rel}: serious answers must include a fenced diagram")
            # A fenced block that opens at column 0 and closes indented renders as an
            # indented literal. rewrap.py tolerates it, because its FENCE regex allows
            # leading whitespace, so nothing in the gate caught it until a writer found one
            # in its own file late enough to mention it in a hand-back.
            open_indent = open_marker = None
            for n, line in enumerate(body.splitlines(), 1):
                if open_marker is None:
                    m = FENCE_OPEN.match(line)
                    if m:
                        open_indent, open_marker = len(m.group(1)), m.group(2)
                    continue
                m = FENCE_SHUT.match(line)
                if m and m.group(2)[0] == open_marker[0] and len(m.group(2)) >= len(open_marker):
                    if len(m.group(1)) != open_indent:
                        problems.append(
                            f"{rel}: fence opened at column {open_indent} closes at "
                            f"column {len(m.group(1))} (line {n}); it renders as a literal"
                        )
                    open_indent = open_marker = None
            if open_marker is not None:
                problems.append(f"{rel}: a fenced block is never closed")

            for target in LINK.findall(body):
                if not (path.parent / target).resolve().exists():
                    problems.append(f"{rel}: relative link does not resolve: {target}")
            stakes = STAKES_HEADING[style]
            if not any(line.startswith(stakes) for line in body.splitlines()):
                problems.append(f"{rel}: missing a '{stakes}' section")
            if SAFETY_HEADING not in body:
                problems.append(f"{rel}: missing a '{SAFETY_HEADING}' section")
            if SOURCES_HEADING not in body:
                problems.append(f"{rel}: missing a '{SOURCES_HEADING}' section")
            elif NOT_RETRIEVED not in body:
                problems.append(
                    f"{rel}: the '{SOURCES_HEADING}' section must carry the "
                    f"not-retrieved statement verbatim"
                )
            cite = FABRICATED_CITATION.search(body)
            if cite:
                problems.append(f"{rel}: reads as a quotation from an unread source: {cite.group(0)!r}")
            hit = PATIENT_DIRECTIVE.search(body)
            if hit:
                problems.append(f"{rel}: reads as direction to a patient: {hit.group(0)!r}")

    # Every answer file must have a catalogue row, not only the other way round. The
    # loop above walks the catalogue and checks its files exist, which cannot see a file
    # with no row. Six of those sat in the tree undetected: an integration script
    # extracted new rows with a grep for "^+m0", which silently matched nothing from
    # m100 upwards, so five emergency pairs and one oncology pair were fully written,
    # fully valid and absent from the catalogue -- invisible to this gate and to the
    # dataset build, while the scorer counted them.
    catalogued = {e["id"] for e in entries}
    for style in STYLES:
        for path in sorted((DOMAIN / "answers").glob(f"*/{style}/m*.md")):
            mid = path.name.split("-")[0]
            if mid not in catalogued:
                rel = path.relative_to(ROOT)
                problems.append(f"{rel}: answer file has no row in the catalogue")

    if problems:
        print(f"FAILED: {len(problems)} problem(s)")
        for problem in problems:
            print(f"  - {problem}")
        return 1
    print(f"OK: {len(entries)} questions, {len(entries) * len(STYLES)} answer files validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
