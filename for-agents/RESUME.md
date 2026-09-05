# Resume state

Machine-readable-ish checkpoint so this work can be picked up by a fresh session
(or a fresh agent) without re-deriving anything. Updated and committed whenever a
unit of work finishes.

## Current position

| | |
| --- | --- |
| Improvement waves | **20 of 20 — target reached.** Mean over `001–100` rose 22.4 → 53.2; every zero-scoring answer eliminated; minimum 0.0 → 38.5. |
| Documentation | **Done.** `README.md`, `HOW-IT-WAS-BUILT.md`, `LEARNINGS.md`, `RECREATE-PROMPT.md` committed in `a8f146c`. |
| Corpus extension | **In progress.** A separate agent is adding questions 101–200 (multilingual / multimodal / translation). Last seen through Q109. |
| Open for the repo owner | The stale `claude/elipokemon-ml-interview-dataset-qibsci` branch must be deleted in the GitHub UI — delete pushes are rejected from this environment. |

## What to do next

1. **If 101–200 is still landing:** leave `questions/questions.tsv` alone except to append
   your own rows, and use targeted `git add` paths. Two workers, disjoint ID ranges.
2. **Once 101–200 is complete:** run the same wave loop over the new answers. They start at
   the same baseline the original 100 did, so the first few waves should give the large
   gains (+2 to +4) rather than the +0.6 the original set is now down to.
3. **Do not run more waves over `001–100`.** Returns flattened to +0.6 and the remaining low
   scorers are structural analogies where forcing in species names trades clarity for score.
   See [`LEARNINGS.md`](LEARNINGS.md#the-score-is-a-search-tool-not-a-target).

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
