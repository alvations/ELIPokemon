# Resume state

Machine-readable-ish checkpoint so this work can be picked up by a fresh session
(or a fresh agent) without re-deriving anything. Updated and committed whenever a
unit of work finishes.

## Current position

| | |
| --- | --- |
| Improvement waves | **20 of 20 over `001–100` — target reached.** Corpus-wide mean is 58.2 across 200 answers, median 54.4, minimum 38.5. |
| Documentation | **Complete.** `README`, `CONTRIBUTING`, `TERMINOLOGY` (both halves), `DATASHEET`, `CHANGELOG`, and this directory. |
| Corpus extension | **200 of 200 — complete, documented and tagged `v0.1.0`.** |
| Open for the repo owner | The stale `claude/elipokemon-ml-interview-dataset-qibsci` branch must be deleted in the GitHub UI — delete pushes are rejected from this environment. |

## What to do next

**The dataset is complete and released as `v0.1.0`.** There is no outstanding build work.

If you are picking this up to extend or maintain it:

1. **Adding a question?** [`../CONTRIBUTING.md`](../CONTRIBUTING.md) has the loop, including the
   score-and-ground step. Ground it in the same batch if it lands under ~40 — that rule kept the
   corpus floor at 38.5 through 100 new questions.
2. **Expect scorer vocabulary gaps.** Five turned up during the build; the table in
   [`LEARNINGS.md`](LEARNINGS.md#five-scorer-vocabulary-gaps-found-across-200-questions) lists
   them. A vocabulary change moves every historical score, so it **never shares a commit with
   content**.
3. **Extend [`../TERMINOLOGY.md`](../TERMINOLOGY.md)** with any new entity, linked to its answer.
4. **Update [`../CHANGELOG.md`](../CHANGELOG.md)** and, for a release, the counts in
   [`../DATASHEET.md`](../DATASHEET.md).
5. **Do not run more waves over `001–100`.** Returns flattened to +0.6.
   See [`LEARNINGS.md`](LEARNINGS.md#the-score-is-a-search-tool-not-a-target).

### Known gaps worth closing

* **No second full-corpus Pokémon audit over 101–200.** Those were reviewed per batch, not in one
  sweep. The first sweep over 001–100 found 21 errors, so another sweep is likely to find some.
* **Category imbalance** — 45 multimodal and 38 translation against 7 transformers. Reflects the
  order of writing, not editorial judgement.
* **No external technical review.** Recorded in [`../DATASHEET.md`](../DATASHEET.md).

### Open for the repo owner

* The stale `claude/elipokemon-ml-interview-dataset-qibsci` branch must be deleted in the GitHub
  UI; delete pushes are rejected from this environment.

## How to resume

```bash
python3 scripts/validate.py                 # gate — must print OK before any commit
python3 scripts/pokemon_score.py            # regenerate LEDGER.md
python3 scripts/ledger_history.py           # every wave's mean, from git
python3 scripts/build_dataset.py            # rebuild index.json + elipokemon.jsonl

# lowest scorers in a given ID range (edit the bounds)
python3 scripts/pokemon_score.py --json \
  | python3 -c "import json,sys; rows=[r for r in json.load(sys.stdin) if 101<=int(r['id'])<=200]; rows.sort(key=lambda r:r['score']); [print(r['score'], r['id'], r['slug']) for r in rows[:15]]"
```

Take the lowest scorers, replace an abstraction with a **specific that makes the analogy
more concrete**, never invent a Pokémon fact, never keyword-stuff. Read the actual file text
immediately before composing an edit — remembered text drifts. Commit and push each wave
separately so `ledger_history.py` keeps one row per wave.

## Rules that must not be broken

* Author is `alvations` only. No `Co-Authored-By`, no mention of Claude/AI anywhere in
  commits, filenames or content.
* `python3 scripts/validate.py` must print OK before every commit.
* Only append a row to `questions/questions.tsv` in the same commit that adds both of
  its answer files, or validation breaks for everyone.
* Use targeted `git add` paths — another process may have uncommitted work in the tree.
* Everything goes to `main`. No feature branches.
