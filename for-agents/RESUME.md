# Resume state

Machine-readable-ish checkpoint so this work can be picked up by a fresh session
(or a fresh agent) without re-deriving anything. Updated and committed whenever a
unit of work finishes.

## Current position

| | |
| --- | --- |
| Improvement waves | **20 of 20 over `001–100` — target reached.** Mean over that range rose 22.4 → 53.2; every zero-scoring answer eliminated; minimum 0.0 → 38.5. Corpus-wide mean is now 58.9 across 132 answers. |
| Documentation | **Done.** `README.md`, `HOW-IT-WAS-BUILT.md`, `LEARNINGS.md`, `RECREATE-PROMPT.md` committed in `a8f146c`. |
| Corpus extension | **132 of the intended 200.** 101–116 `multilingual`, 117–128 `multimodal`, 129–132 `translation`. All complete, committed and validating. |
| Open for the repo owner | The stale `claude/elipokemon-ml-interview-dataset-qibsci` branch must be deleted in the GitHub UI — delete pushes are rejected from this environment. |

## What to do next

1. **Continue the extension from `133`.** Covered so far: `multilingual` 101–116;
   `multimodal` 117–128 (VLM architectures, patches, cross-modal attention, contrastive
   pretraining, resolution, hallucination, document QA, interleaved data, ASR, video,
   charts, grounding); `translation` 129–132 (metrics beyond BLEU, low-resource,
   document-level, quality estimation).

   Still to write — roughly 34 more each of multimodal and translation:
   * **multimodal**: image generation and diffusion, audio/speech LLMs and duplex dialogue,
     multimodal safety and jailbreaks through images, multimodal RAG, embodied and GUI
     agents, 3D and depth, medical and scientific imaging, synthetic caption pipelines,
     modality imbalance in training, multimodal benchmarks and their contamination.
   * **translation**: terminology and glossary enforcement, domain adaptation, post-editing
     and human-in-the-loop, LLM translation versus classical NMT, off-target and hallucinated
     translation, formality and honorifics, gender bias in MT, speech translation and
     simultaneous interpretation, subtitle and length constraints, localisation beyond text.
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
