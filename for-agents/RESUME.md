# Resume state

Machine-readable-ish checkpoint so this work can be picked up by a fresh session
(or a fresh agent) without re-deriving anything. Updated and committed whenever a
unit of work finishes.

## Current position

| | |
| --- | --- |
| Improvement waves | **20 of 20 over `001–100` — target reached.** Corpus-wide mean is 58.2 across 200 answers, median 54.4, minimum 38.5. |
| Documentation | **Done.** `README.md`, `HOW-IT-WAS-BUILT.md`, `LEARNINGS.md`, `RECREATE-PROMPT.md` committed in `a8f146c`. |
| Corpus extension | **200 of 200 — complete.** 001–100 core ML/LLM, 101–116 `multilingual`, 117–128 / 137–140 / 145–148 / 151–152 / 157–160 / 165–168 / 173–176 / 181–184 / 189–192 / 197–198 `multimodal`, 129–136 / 141–144 / 149–150 / 153–156 / 161–164 / 169–172 / 177–180 / 185–188 / 193–196 `translation`, 199–200 `synthesis`. |
| Open for the repo owner | The stale `claude/elipokemon-ml-interview-dataset-qibsci` branch must be deleted in the GitHub UI — delete pushes are rejected from this environment. |

## What to do next

**The dataset is complete.** 200 questions, 400 answer files, all validating. There is no
outstanding build work.

If you are picking this up to extend or maintain it:

1. **Adding a question?** Follow the loop in [`RECREATE-PROMPT.md`](RECREATE-PROMPT.md). Score it
   before committing and ground it in the same batch if it lands under ~40 — that is the rule that
   kept the corpus minimum at 38.5 through 100 new questions.
2. **Expect scorer vocabulary gaps.** Five turned up while writing 117–200 (overworld items and
   landmarks; the Nidoran line and redirection moves; vitamins and the Bottle Cap toolkit; Trainer
   Classes; four long species names). A vocabulary change moves every historical score, so it
   **never shares a commit with content**.
3. **Do not run more waves over `001–100`.** Returns flattened to +0.6.
   See [`LEARNINGS.md`](LEARNINGS.md#the-score-is-a-search-tool-not-a-target).
4. **Extend `TERMINOLOGY.md`** — it currently covers the entities used in 001–100 and needs the
   ones introduced by 101–200.
5. **Open for the repo owner:** the stale `claude/elipokemon-ml-interview-dataset-qibsci` branch
   must be deleted in the GitHub UI; delete pushes are rejected from this environment.

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
