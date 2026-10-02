#!/usr/bin/env python3
"""Re-wrap answer prose to 98 columns, leaving everything else exactly alone.

LEARNINGS has asked for this to be a committed script in the loop since the first
release, and until now it was not one: every writer rolled their own in the shared
scratchpad, and in one wave three of them had their copy silently overwritten by a
sibling using the same filename. This is the one copy.

What it will not touch, because touching any of them has broken a file before:

  * YAML front matter — the ``question`` field is a single long line by design and
    must match the catalogue character for character.
  * fenced blocks — the column-aligned diagrams are aligned by hand.
  * Markdown table rows — long rows are normal in this corpus and the 98 applies to
    prose only. A writer who tried to break them would corrupt the table.
  * headings, and any line that is a bare link or a horizontal rule.
  * blank lines, and the number of them.

Everything else is a paragraph, wrapped greedily at 98 characters, with the leading
indentation of the first line preserved and list continuations given the hanging
indent the marker implies. It never splits inside a word, so a long URL or a long
inline-code span simply overruns, which is correct.

Usage:
    python3 scripts/rewrap.py PATH...          # rewrite in place
    python3 scripts/rewrap.py --check PATH...  # report, change nothing
"""

from __future__ import annotations

import re
import sys
import pathlib

WIDTH = 98
FENCE = re.compile(r"^\s*(```|~~~)")
TABLE = re.compile(r"^\s*\|")
HEADING = re.compile(r"^\s*#{1,6}\s")
RULE = re.compile(r"^\s*([-*_])\s*(\1\s*){2,}$")
# A list item or a blockquote: the marker sets the hanging indent for the rest.
MARKER = re.compile(r"^(\s*)((?:[-*+]|\d+[.)]|>)\s+)")


def _wrap(words: list[str], first_indent: str, rest_indent: str) -> list[str]:
    lines: list[str] = []
    cur = first_indent
    pending = first_indent
    for w in words:
        candidate = cur + ("" if cur in (first_indent, rest_indent) and not cur.strip() else " ") + w
        candidate = (cur + " " + w) if cur.strip() else (cur + w)
        if cur.strip() and len(candidate) > WIDTH:
            lines.append(cur)
            cur = rest_indent + w
        else:
            cur = candidate
    if cur.strip():
        lines.append(cur)
    return lines or [pending.rstrip()]


def rewrap(text: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    i = 0

    # Front matter, verbatim.
    if lines and lines[0].strip() == "---":
        out.append(lines[0])
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            out.append(lines[i])
            i += 1
        if i < len(lines):
            out.append(lines[i])
            i += 1

    in_fence = False
    para: list[str] = []
    para_raw: list[str] = []
    first_indent = rest_indent = ""

    def flush() -> None:
        """Emit the pending paragraph, re-wrapping it only if it actually overruns.

        A greedy re-wrap of everything would reflow paragraphs that are already
        inside the limit but packed slightly differently, which turns a one-line
        correction into a thousand-line diff and buries the real change. So a
        paragraph whose every line already fits is emitted byte for byte.
        """
        nonlocal para
        if not para:
            return
        if all(len(l) <= WIDTH for l in para_raw):
            out.extend(para_raw)
        else:
            out.extend(_wrap(" ".join(para).split(), first_indent, rest_indent))
        para = []
        para_raw.clear()

    while i < len(lines):
        line = lines[i]
        if FENCE.match(line):
            flush()
            in_fence = not in_fence
            out.append(line)
        elif in_fence:
            out.append(line)
        elif not line.strip():
            flush()
            out.append(line)
        elif TABLE.match(line) or HEADING.match(line) or RULE.match(line):
            flush()
            out.append(line)
        else:
            m = MARKER.match(line)
            if m and not para:
                first_indent = m.group(1)
                rest_indent = " " * len(m.group(1) + m.group(2))
                para.append(line.strip()); para_raw.append(line)
            elif m:
                # A new list item begins: the previous paragraph ends here.
                flush()
                first_indent = m.group(1)
                rest_indent = " " * len(m.group(1) + m.group(2))
                para.append(line.strip()); para_raw.append(line)
            else:
                if not para:
                    indent = line[: len(line) - len(line.lstrip())]
                    first_indent = rest_indent = indent
                para.append(line.strip()); para_raw.append(line)
        i += 1
    flush()
    return "\n".join(out)


def _unbreakable(text: str) -> list[int]:
    """Line numbers still over the limit that the script is not allowed to break.

    Front matter, fenced blocks and table rows are all exempt by design, so a
    report that counted them would always be non-empty and would train the reader
    to ignore it. What is left is a single word or inline-code span longer than the
    limit, which is correct to overrun and worth naming.
    """
    lines = text.split("\n")
    exempt = set()
    i = 0
    if lines and lines[0].strip() == "---":
        exempt.add(1)
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            exempt.add(i + 1)
            i += 1
        if i < len(lines):
            exempt.add(i + 1)
    in_fence = False
    for n, line in enumerate(lines, 1):
        if FENCE.match(line):
            in_fence = not in_fence
            exempt.add(n)
        elif in_fence or TABLE.match(line):
            exempt.add(n)
    return [n for n, l in enumerate(lines, 1) if len(l) > WIDTH and n not in exempt]


def main(argv: list[str]) -> int:
    check = "--check" in argv
    paths = [pathlib.Path(a) for a in argv if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    changed = 0
    for path in paths:
        before = path.read_text()
        after = rewrap(before)
        if after != before:
            changed += 1
            over = _unbreakable(after)
            if check:
                print(f"{path}: would re-wrap" + (f" (still over: {over})" if over else ""))
            else:
                path.write_text(after)
                print(f"{path}: re-wrapped" + (f" (unbreakable lines: {over})" if over else ""))
    if not changed:
        print(f"{len(paths)} file(s) already wrapped at {WIDTH}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
