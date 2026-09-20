# Resume state

Machine-readable-ish checkpoint so this work can be picked up by a fresh session
(or a fresh agent) without re-deriving anything. Updated and committed whenever a
unit of work finishes.

## Current position

| | |
| --- | --- |
| Corpus | **232 questions, 464 answers, all validating.** Mean 64.4, median 60.5, minimum 39.9. |
| Arcs | 001–100 core ML/LLM · 101–116 multilingual · 45 multimodal · 38 translation · 199–200 synthesis · 201–212 frontier systems · **213–232 open weights**. |
| Documentation | **Complete.** `README`, `CONTRIBUTING`, `TERMINOLOGY` (all four parts), `DATASHEET`, `CHANGELOG`, and this directory. |
| Release | 0.3.0 documented in [`../CHANGELOG.md`](../CHANGELOG.md). |
| Open for the repo owner | Two items, both below — neither can be done from this environment. |

## What to do next

There is no outstanding build work. If you are picking this up to extend or maintain it:

1. **Adding a question?** [`../CONTRIBUTING.md`](../CONTRIBUTING.md) has the loop, including the
   score-and-ground step. Ground it in the same batch if it lands under ~40 — that rule has held
   the corpus floor through 112 new questions.
2. **Expect scorer vocabulary gaps.** Eight batches have turned up; the table in
   [`LEARNINGS.md`](LEARNINGS.md#seven-scorer-vocabulary-gaps-found-across-212-questions) lists
   the first seven. A vocabulary change moves every historical score, so it **never shares a
   commit with content** — and neither does a change to the matcher, of which there have now
   been four.
3. **A low score is not always a bad answer.** Terms in the scorer's `GENERIC` set are generic on
   purpose, so an analogy built on the PC, the party or the battle itself can score near zero
   while being the best analogy available. Run `--detail` before concluding anything.
4. **Extend [`../TERMINOLOGY.md`](../TERMINOLOGY.md)** with any new entity, linked to its answer.
5. **Update [`../CHANGELOG.md`](../CHANGELOG.md)** and, for a release, the counts in
   [`../DATASHEET.md`](../DATASHEET.md).
6. **Do not run more waves over `001–100`.** Returns flattened to +0.6.
   See [`LEARNINGS.md`](LEARNINGS.md#the-score-is-a-search-tool-not-a-target).

### If you touch questions 201–232

Those arcs name real products and quote real figures, dated **September 2026**. Before editing
any of it, re-read the primary source — the model card, the licence file, the config, the system
card — rather than the answer. `arxiv.org`, `huggingface.co` and most vendor pages are blocked
from this environment; `raw.githubusercontent.com` and the GitHub API are not, which is how the
licence files, the inference config and two technical-report PDFs were read first-hand. Each
answer says which of its claims are primary and which are coverage, and every answer linking an
arXiv identifier carries a citation note saying the paper was **not opened**. If a figure has
moved, update the answer *and* its "where this stands" note, and record it in the changelog.

### Known gaps worth closing

* **No second full-corpus Pokémon audit** over 101–232. Those were reviewed per batch, not in one
  sweep. The first sweep over 001–100 found 21 errors, so another sweep is likely to find some.
* **Category imbalance** — 45 multimodal and 38 translation against 7 transformers, 20
  open-weights and 12 frontier. Reflects the order of writing, not editorial judgement.
* **Scores before `c4b9c91` understate their answers.** The wrap fix changed what the matcher can
  see, so the ledger has a discontinuity there as well as at each vocabulary commit.
* **The scorer is now slow** — a full run over 232 answers takes a couple of minutes, because
  matching is linear in vocabulary size. Fine as a gate, annoying in a loop.
* **No external technical review.** Recorded in [`../DATASHEET.md`](../DATASHEET.md).

### Open for the repo owner

* The **`v0.1.0` tag exists locally only**. Tag pushes are rejected from this environment
  (HTTP 403 from the proxy, while branch pushes to `main` succeed in the same breath). From a
  clone with push rights:

  ```bash
  git fetch origin && git checkout main && git pull
  git tag -a v0.1.0 99d8bb4 -m "ELIPokemon v0.1.0 — 200 questions, 400 answers"
  git tag -a v0.2.0 43442cc -m "ELIPokemon v0.2.0 — 212 questions, 424 answers"
  git tag -a v0.3.0 -m "ELIPokemon v0.3.0 — 232 questions, 464 answers"
  git push origin v0.1.0 v0.2.0 v0.3.0
  ```
* The stale `claude/elipokemon-ml-interview-dataset-qibsci` branch must be deleted in the GitHub
  UI; delete pushes are rejected from this environment too.

## How to resume

```bash
python3 scripts/validate.py                 # gate — must print OK before any commit
python3 scripts/pokemon_score.py            # regenerate LEDGER.md
python3 scripts/ledger_history.py           # every wave's mean, from git
python3 scripts/build_dataset.py            # rebuild index.json + elipokemon.jsonl

# lowest scorers in a given ID range (edit the bounds)
python3 scripts/pokemon_score.py --json \
  | python3 -c "import json,sys; rows=[r for r in json.load(sys.stdin) if 101<=int(r['id'])<=232]; rows.sort(key=lambda r:r['score']); [print(r['score'], r['id'], r['slug']) for r in rows[:15]]"
```

Take the lowest scorers, replace an abstraction with a **specific that makes the analogy
more concrete**, never invent a Pokémon fact, never keyword-stuff. Read the actual file text
immediately before composing an edit — remembered text drifts. Commit and push each batch
separately so `ledger_history.py` keeps one row per change.

## Rules that must not be broken

* Author is `alvations` only. No `Co-Authored-By`, no mention of Claude/AI anywhere in
  commits, filenames or content.
* `python3 scripts/validate.py` must print OK before every commit.
* Only append a row to `questions/questions.tsv` in the same commit that adds both of
  its answer files, or validation breaks for everyone.
* Use targeted `git add` paths — another process may have uncommitted work in the tree.
* Everything goes to `main`. No feature branches.
