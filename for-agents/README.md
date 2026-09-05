# for-agents/

Notes for whoever — human or agent — picks this repository up next.

This directory is not part of the dataset. It is the working memory of how the dataset
was built, what went wrong, and how to rebuild or extend it without relearning the same
lessons.

| File | What it is |
| --- | --- |
| [`RESUME.md`](RESUME.md) | Current checkpoint. Read this first if you are continuing in-flight work. |
| [`HOW-IT-WAS-BUILT.md`](HOW-IT-WAS-BUILT.md) | The construction sequence, in order, with the reasoning behind each structural decision. |
| [`LEARNINGS.md`](LEARNINGS.md) | What worked, what failed, and the specific mistakes — including the ones that shipped before being caught. |
| [`RECREATE-PROMPT.md`](RECREATE-PROMPT.md) | A prompt that rebuilds this dataset from nothing, plus how to seed it from public Hugging Face datasets instead of inventing questions. |

## The 60-second version

ELIPokémon pairs a serious ML interview answer with the same content re-expressed entirely
through Pokémon. Everything downstream follows from three constraints:

1. **The two answers must agree on every technical claim.** A disagreement is a bug in the
   pair, not a stylistic difference.
2. **Pokémon accuracy is a correctness bar.** A wrong typing or an illegal moveset is a
   defect, exactly like a wrong claim about attention would be.
3. **Named entities beat generic furniture.** "Brock's Onix" does analogical work that
   "a Gym Leader's Pokémon" does not. This is measured, tracked, and committed
   (see [`../LEDGER.md`](../LEDGER.md)).

## Commands you will want

```bash
python3 scripts/validate.py          # pairing, front matter, ASCII art, length — must pass before any commit
python3 scripts/build_dataset.py     # markdown -> questions/index.json + dataset/elipokemon.jsonl
python3 scripts/pokemon_score.py     # score every Pokémon answer, rewrite LEDGER.md
python3 scripts/ledger_history.py    # replay the score trend across git history
python3 scripts/revise.py --lowest 5 --dry-run   # LLM-assisted revision, no API calls
```

## Non-negotiables

* Author is `alvations`. **No `Co-Authored-By` trailer, and no mention of Claude, AI, or any
  model in commit messages, filenames, or dataset content.**
* `validate.py` must print OK before every commit.
* **Only append a row to `questions/questions.tsv` in the same commit that adds both of its
  answer files** — otherwise validation breaks for every concurrent worker.
* When another process may be working in the tree, use targeted `git add` paths. Never
  `git add -A`.
