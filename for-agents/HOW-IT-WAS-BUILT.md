# How this repository was built

Written after the fact, in the order the work actually happened. Where a decision was
reversed later, the reversal is recorded here rather than tidied away — the wrong turns
are the useful part.

---

## 0. The shape of the problem

The brief was one sentence long: host serious ML/LLM interview questions, and for each one
give two answers — a rigorous technical answer with ASCII diagrams, and the same content
explained entirely in Pokémon terms.

The non-obvious part is that this is **not** a "write 100 blog posts" task. It is a task
about *maintaining an invariant across 200 files*: every Pokémon answer must make exactly
the same technical claims as its serious twin, and must not lie about Pokémon while doing
it. Almost every structural decision below exists to make that invariant checkable by a
machine instead of by re-reading.

---

## 1. Catalogue before content

The first artefact was not an answer. It was `questions/questions.tsv`:

```
id   slug                        category      difficulty   question
001  attention-mechanism         transformers  core         How does the attention ...
```

One tab-separated row per question. This is the source of truth for the corpus: the ID
space, the slugs (which determine filenames), the categories, and the canonical wording of
every question.

Why a TSV and not a directory listing:

* **Filenames become derivable.** `answers/serious/001-attention-mechanism.md` and
  `answers/pokemon/001-attention-mechanism.md` are computed from the row, so a missing file
  is a detectable absence rather than an invisible one.
* **Coverage is greppable.** Category balance, difficulty spread and duplicate questions
  are all `cut -f3 | sort | uniq -c` away.
* **Concurrency has a merge point.** When a second worker later extended the corpus to 200
  questions, the only shared file it had to touch was this one.

Choosing the 100 questions themselves was editorial: work backwards from what modern
LLM/ML interviews actually probe — transformer internals, alignment (RLHF/DPO/GRPO),
parameter-efficient fine-tuning, inference economics (KV cache, quantisation, speculative
decoding), retrieval, agents, evaluation, safety — and keep a deliberate tail of classical
fundamentals (bias–variance, regularisation, calibration) so the set is not purely a
2020s-LLM set.

## 2. Front matter as the join key

Every answer file opens with YAML front matter:

```yaml
---
id: "001"
slug: attention-mechanism
style: serious          # or: pokemon
question: How does the attention mechanism work in transformers?
---
```

This is redundant with the TSV *on purpose*. Redundancy that a validator checks is not
duplication, it is a checksum: if a file is renamed, copied as a template and half-edited,
or edited by a worker holding a stale copy of the catalogue, the mismatch surfaces
immediately instead of silently producing a mislabelled training example.

## 3. The validator, written before the bulk of the content

`scripts/validate.py` was written early, and it is the reason the corpus stayed coherent
across hundreds of edits. It enforces:

* both `serious/` and `pokemon/` files exist for every catalogue row;
* front matter `id` / `slug` / `style` / `question` match the catalogue exactly;
* the body starts with an `#` H1;
* the body is at least 120 words (catches stubs and truncated generations);
* **every serious answer contains a fenced code block** — this is the ASCII-diagram
  requirement, made mechanical.

The rule that made it stick: *`validate.py` must print OK before any commit.* Not "should".
A commit that breaks validation poisons every later worker, because they clone a tree whose
gate is already red and lose the signal.

## 4. Writing the pairs

Answers were written one pair at a time — serious first, Pokémon second, from the serious
answer. Never the reverse, and never in parallel.

The serious answer is the source of truth. The Pokémon answer is a *translation* of it. If
the Pokémon answer is written first (or independently), it drifts: the analogy starts
generating claims that sound right in Pokémon terms and are wrong in ML terms. Writing it
as a translation forces every Pokémon paragraph to point at a specific technical paragraph.

Each pair was committed as it was finished, per the instruction to commit after each one.
That turned out to matter for a reason beyond crash-safety: a per-pair commit history means
`git log -- answers/pokemon/NNN-*.md` reads as the edit history of one idea, and later
score regressions can be bisected to a single answer.

The house style that emerged:

* Serious answers: a definition, the mechanism, an ASCII diagram of the data flow, the
  failure modes, and what an interviewer is actually listening for.
* Pokémon answers: the same skeleton, but every abstraction is bound to a *named* entity.
  Not "a Pokémon with high HP" — **Blissey**, whose 255 base HP is a genuine outlier.
* Both are wrapped at ~98 columns so diffs stay reviewable.

## 5. The glossary, and then the links

`TERMINOLOGY.md` was added for readers who know ML but not Pokémon: species, characters,
moves, items, places, and — the part that ended up mattering most — a ~200-row table of
**recurring analogy conventions** mapping each Pokémon prop to the technical concept it
consistently stands for across the corpus.

That table is a consistency device, not just a reader aid. Once "Ditto = a model that
copies the surface form of its target" is written down, the next answer that needs that
idea uses Ditto too, and the corpus develops a shared vocabulary instead of 100 unrelated
metaphors.

Every question reference in the glossary was then turned into a link to the answer file
(`[`078`](answers/pokemon/078-....md)`), making it navigable in both directions.

## 6. The accuracy audit

Feedback that some answers "made little Pokémon sense" triggered a full re-read of all 100
Pokémon answers against actual game facts. It found **21 real errors** — illegal movesets,
wrong stats, characters given the wrong role, mechanics that do not work as described.

The fix was not just the corrections. It was promoting Pokémon accuracy to a **correctness
bar**: a Pokémon that cannot legally learn the move you gave it is a defect in exactly the
same category as a wrong claim about softmax. The details are in
[`LEARNINGS.md`](LEARNINGS.md#the-21-accuracy-errors-and-what-they-have-in-common).

## 7. Measuring "Pokémon-ness"

The next request was to score how strongly each Pokémon answer leans on real Pokémon
entities rather than generic furniture ("a Trainer", "a Gym"), keep a ledger, improve the
low scorers, and commit every edit so the score movement is trackable.

`scripts/pokemon_score.py` scores 0–100, deterministically, with no model in the loop:

```
score = breadth (0-45) + density (0-35) + specificity (0-20)
        distinct named   named terms      named / (named +
        entities used    per 100 words    generic) ratio
```

Design choices worth keeping:

* **Generic terms are the denominator, not the numerator.** "Gym" and "Trainer" cannot earn
  points; they can only dilute the ratio. That is the whole point of the request.
* **Longest-first matching with masking.** Each matched term is blanked out of the working
  string before shorter terms are tried, so `Thunder Wave` does not also score as
  `Thunder`. Without this, verbose answers scored higher than precise ones.
* **Determinism.** The same text always yields the same number, so `git diff` on
  `LEDGER.md` *is* the change in Pokémon-ness — which is exactly what the ledger request
  asked for.

`LEDGER.md` is generated and committed. `scripts/ledger_history.py` replays its headline
line across git history to produce the trend table.

## 8. Twenty improvement waves

The loop, repeated 20 times:

1. `python3 scripts/pokemon_score.py` → ranked ledger.
2. Take the lowest ~8 answers.
3. For each, read the *serious* twin, find the abstraction doing the least work, and
   replace it with a named entity that is **both** technically apt and factually true.
4. `validate.py`, rebuild the dataset, rescore, commit the wave.

One wave = one commit, so `ledger_history.py` yields one row per wave:

```
10535d0  22.4  baseline
fd7e69f  24.0  scorer recalibration (not a content change)
...
5da187a  55.2  wave 20
```

The waves worked, and then they stopped working as well — the per-wave gain fell from +2.9
to +0.6. That flattening is real and was reported rather than smoothed over: the remaining
low scorers are answers whose analogy is *structural* (a pipeline, a trade-off curve) where
forcing in species names would cost clarity to buy score. See
[`LEARNINGS.md`](LEARNINGS.md#the-score-is-a-search-tool-not-a-target).

## 9. Revision tooling

The request to check in "the scorer and ledger and the LLM revision calls and prompts
scripts" met an awkward fact: **there were no LLM revision scripts.** Every revision to that
point had been hand-authored. Saying so was the only honest option, and the docstring of
`scripts/revise.py` still records it.

`revise.py` and `prompts/revise-pokemon-answer.md` were then built for future rounds. The
design is defensive, because an LLM optimising a score will keyword-stuff:

* the **serious** answer goes into the prompt as source of truth;
* the prompt forbids contradicting it, forbids inventing Pokémon facts, and forbids
  keyword-stuffing;
* after the call, the tool **reverts the edit** unless the score gain clears `--min-gain`,
  the front matter is byte-identical, *and* `validate.py` still passes.

The prompt lives in a versioned file with `---SYSTEM---` / `---USER---` sections and
`{{PLACEHOLDER}}` slots, so prompt changes show up in git history like code changes.

## 10. Generated artefacts

`scripts/build_dataset.py` reads the TSV plus the front matter and emits:

* `questions/index.json` — the catalogue as JSON;
* `dataset/elipokemon.jsonl` — one record per question carrying both answer bodies, ready
  for training or eval loading.

Markdown stays the editable surface; JSON/JSONL are build outputs, regenerated and
committed alongside content changes so a consumer can clone and load without running
anything.

## 11. Extension to 200

Questions 101–200 (multilingual, multimodal, translation) were added by a second worker
running concurrently. The coordination rules that made that safe:

* **targeted `git add` paths only** — `git add -A` from one worker swept the other's
  in-progress file into an unrelated commit, once, before this rule existed;
* **a TSV row and its two answer files land in the same commit** — a row without answers
  breaks `validate.py` for everyone;
* disjoint ID ranges, so the two workers never edit the same file.

---

## The invariant, restated

Everything above is machinery for one property: **a reader can hold the two answers side by
side and find no claim in one that the other contradicts, and no Pokémon fact in the
playful one that a player would call wrong.** Validation, the glossary conventions table,
the ledger, and the revision guard are four different fences around that same property.
