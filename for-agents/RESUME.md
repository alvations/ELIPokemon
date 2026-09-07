# Resume state

Machine-readable-ish checkpoint so this work can be picked up by a fresh session
(or a fresh agent) without re-deriving anything. Updated and committed whenever a
unit of work finishes.

## Current position

| | |
| --- | --- |
| Improvement waves | **20 of 20 over `001–100` — target reached.** Mean over that range rose 22.4 → 53.2; every zero-scoring answer eliminated. Corpus-wide mean is now 59.3 across 152 answers. |
| Documentation | **Done.** `README.md`, `HOW-IT-WAS-BUILT.md`, `LEARNINGS.md`, `RECREATE-PROMPT.md` committed in `a8f146c`. |
| Corpus extension | **152 of the intended 200.** 101–116 `multilingual`, 117–128 and 137–140 and 145–148 and 151–152 `multimodal`, 129–136 and 141–144 and 149–150 `translation`. All complete, committed and validating. |
| Open for the repo owner | The stale `claude/elipokemon-ml-interview-dataset-qibsci` branch must be deleted in the GitHub UI — delete pushes are rejected from this environment. |

## What to do next

1. **Continue the extension from `153`.** Covered so far: `multilingual` 101–116;
   `multimodal` 117–128, 137–140, 145–148, 151–152; `translation` 129–136, 141–144,
   149–150.

   Still to write — 48 more to reach 200. Candidate topics not yet covered:
   * **multimodal**: video generation, audio/music generation, image editing and
     inpainting, referring segmentation, egocentric video, sign language, remote
     sensing, multimodal agents with tools, watermarking and provenance, efficient
     VLM serving, streaming perception, multimodal chain-of-thought.
   * **translation**: speech-to-speech translation, dubbing and lip-sync constraints,
     sign language translation, code and markup translation, translation memory
     systems, MT for accessibility, dialect and non-standard varieties, endangered
     language documentation, community and participatory MT, MT security and
     poisoning, translationese in training corpora, evaluation with professional
     translators.

2. **Work in batches of ~6–10 pairs and commit each batch.** The last worker lost nothing
   only because its finished files were on disk when it stopped; a batch that is committed
   cannot be lost at all. A TSV row and its two answer files go in the same commit.
3. **Score each new answer as you write it and ground it before committing.** New answers
   written with the named-entity lesson already learned land around 45–85 unaided, so the
   old wave loop is mostly unnecessary — but check, because a structural analogy can still
   come in near 27 (Q130 and Q132 both did, and a single grounding pass took them to 82.6
   and 54.9). Ground it in the same batch rather than deferring it to a wave.
4. **Expect scorer vocabulary gaps, and fix them in their own commit.** Two turned up while
   writing 117–132: the whole overworld-item and landmark vocabulary, and then the Nidoran
   line, Follow Me, Rage Powder and Egg Move. A vocabulary change moves every historical
   score, so it never shares a commit with content.
5. **Do not run more waves over `001–100`.** Returns flattened to +0.6 and the remaining low
   scorers are structural analogies where forcing in species names trades clarity for score.
   See [`LEARNINGS.md`](LEARNINGS.md#the-score-is-a-search-tool-not-a-target).
6. **Extend `TERMINOLOGY.md`** to cover any new Pokémon entities 101+ introduce, and link
   each new question reference to its answer file.

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
