# Resume state

Machine-readable-ish checkpoint so this work can be picked up by a fresh session
(or a fresh agent) without re-deriving anything. Updated and committed after every
improvement wave.

## Current position

| | |
| --- | --- |
| Task | Pokémon-ness improvement waves over `answers/pokemon/001–100` |
| Waves completed | 18 |
| Mean (001–100) | 45.4 |
| Target | 20 waves total |
| Concurrent work | a separate agent is adding questions 101–200 (multilingual / multimodal / translation) |

## How to resume

```bash
python3 scripts/pokemon_score.py            # regenerate LEDGER.md
python3 scripts/ledger_history.py           # every wave's mean, from git
python3 scripts/pokemon_score.py --json \
  | python3 -c "import json,sys; rows=[r for r in json.load(sys.stdin) if int(r['id'])<=100]; rows.sort(key=lambda r:r['score']); [print(r['score'], r['id'], r['slug']) for r in rows[:15]]"
```

Take the lowest scorers, replace an abstraction with a **specific that makes the analogy
more concrete**, never invent a Pokémon fact, never keyword-stuff. Commit and push each
wave separately so `ledger_history.py` keeps one row per wave.

## Rules that must not be broken

* Author is `alvations` only. No `Co-Authored-By`, no mention of Claude/AI anywhere in
  commits, filenames or content.
* `python3 scripts/validate.py` must print OK before every commit.
* Only append a row to `questions/questions.tsv` in the same commit that adds both of
  its answer files, or validation breaks for everyone.
* Use targeted `git add` paths — another process may have uncommitted work in the tree.
