# Dataset card — ELIPokémon v0.3.0

Question 197 of this dataset argues that documentation should tell a reader something that
would make them **not** use the thing. This file tries to hold itself to that.

---

## At a glance

| | |
| --- | --- |
| **Version** | v0.3.0 |
| **Records** | 232 questions · 464 answer files · ~318,000 words |
| **Format** | Markdown with YAML front matter; generated `dataset/elipokemon.jsonl` (2.2 MB) |
| **Fields** | `id`, `slug`, `question`, `category`, `difficulty`, `answer_serious`, `answer_pokemon`, `tags` |
| **Language** | English |
| **Difficulty split** | 50 core · 99 intermediate · 83 advanced |
| **Licence** | Content CC BY 4.0 · code MIT |
| **Built** | 2026-09-03 → 2026-09-20 |

## What it is

Each record pairs one machine-learning or LLM interview question with two answers: a rigorous
technical one, and the same content re-expressed entirely through Pokémon. The pairing is the
artefact — the two answers are constrained to make the same claims.

## What it is for

* **Instruction tuning** on explanation and register control.
* **Style-transfer evaluation** — two texts, same propositional content, maximally different
  register, with a stated constraint that they agree.
* **Explanation-quality evaluation**: does a model's analogy preserve the technical claims?
* **Revision** — reading before an interview.

## What it is *not* for

Stated plainly, because this is the section that matters:

* **Not a source of record for technical facts.** Answers are written at the level of a strong
  interview response, not a paper. Named results, papers and figures are stated from working
  knowledge and were **not systematically fact-checked against primary sources**. Verify
  anything before citing it.
* **Not a Pokémon reference.** Pokémon facts were audited and corrected (see below), but the
  goal was analogical honesty, not completeness.
* **Not a benchmark with a held-out split.** There is no train/test division; every record is
  public. If you train on it, do not then evaluate on it.
* **Not balanced.** 45 multimodal and 38 translation questions against 7 on transformers. The
  distribution reflects the order things were written in, not an editorial judgement about
  importance.
* **Not a current reference on any product.** Questions 201–232 name real systems and quote real
  prices, parameter counts, benchmark scores and capability tiers, dated **September 2026**, and
  **nothing was verified by running the systems described**. Each answer carries a dated "where
  this stands" note separating what is primary from what is coverage. In the 213–232 arc a
  minority of sources really were read first-hand — two licence files, two technical-report PDFs,
  an inference config and a vendor repository, all via `raw.githubusercontent.com`, which the
  build environment permits — and those are marked as primary. Everything else came from search
  coverage, because `arxiv.org`, `huggingface.co` and most vendor pages are blocked. Where an
  answer links an arXiv identifier, a **citation note** states that the paper was named from
  working knowledge and not opened. Treat the arc as a snapshot of what was being said.
* **Not multilingual.** It is *about* multilingual NLP, in English only. Question 196 argues
  that a translated benchmark measures familiarity with the source culture; that criticism
  applies to any translation of this dataset.

## How it was made

Hand-authored, one pair at a time, serious answer first and the Pokémon answer written **from
it** as a translation rather than independently. The full construction sequence is in
[`for-agents/HOW-IT-WAS-BUILT.md`](for-agents/HOW-IT-WAS-BUILT.md); a prompt for reconstructing
it is in [`for-agents/RECREATE-PROMPT.md`](for-agents/RECREATE-PROMPT.md).

**Provenance note, stated because a reader could reasonably assume otherwise:**
`scripts/revise.py` and `prompts/revise-pokemon-answer.md` are LLM revision tooling checked into
this repository. **They did not generate any committed answer.** They exist so that future
revision rounds are reproducible — same prompt, same accept/reject rule, recorded in git. This
is repeated in the script's docstring.

## What was verified, and how

| Property | How it is enforced | Coverage |
| --- | --- | --- |
| Both answers exist for every question | `scripts/validate.py`, blocking before every commit | 232/232 |
| Front matter matches the catalogue exactly | `scripts/validate.py` | 464/464 |
| Serious answers contain an ASCII diagram | `scripts/validate.py` (fenced block required) | 232/232 |
| Minimum length (120 words) | `scripts/validate.py` | 464/464 |
| Pokémon factual accuracy | Manual audit of all 100 Pokémon answers after the first pass; per-batch review thereafter | See caveat below |
| Named-entity density | `scripts/pokemon_score.py`, committed to `LEDGER.md` | 232/232 |
| Technical accuracy | **Author review only. No external review.** | — |

### The Pokémon accuracy caveat

A full audit of answers 001–100 found **21 factual errors** and fixed them (commit `1540837`).
They fell into five classes — illegal movesets, invented numbers, wrong item effects, characters
given the wrong role, and mechanics that do not work as described — all catalogued in
[`for-agents/LEARNINGS.md`](for-agents/LEARNINGS.md).

Answers 101–200 were reviewed per batch rather than in one sweep, and three further errors were
caught and corrected during writing (recorded in [CHANGELOG.md](CHANGELOG.md)). **No second
full-corpus audit has been run over 101–200.** If you find an error, it is a bug; please open an
issue.

## The Pokémon-ness score

`scripts/pokemon_score.py` assigns each Pokémon answer 0–100 based on how much it leans on
**named** entities rather than generic furniture. It is deterministic, so the diff between two
commits of `LEDGER.md` *is* the change.

```
score = breadth (0-45) + density (0-35) + specificity (0-20)
```

Current: mean **62.1**, median **58.5**, minimum **39.9**, maximum **100.0**.

**This is a proxy and it is gameable.** It counts named entities; it cannot tell whether they
earn their place. It was used as a search tool for finding answers worth re-reading, not as an
optimisation target — and the dataset contains three answers (021, 038, 190) explaining exactly
what goes wrong when a proxy becomes a goal. Treat a low score as a question.

**Vocabulary caveat:** the score depends on a hand-maintained entity vocabulary. Eight gaps were
found and closed during the build — the seventh being that **the Pokédex had no entry at all**
after 212 questions, and the eighth that none of the sixteen Kanto and Hoenn **Badges** was
listed although every Gym Leader was; a term the vocabulary does not know scores zero, so
historical scores are not comparable across those commits. Each vocabulary change was committed
on its own, with no content change, so the discontinuities are identifiable in
`ledger_history.py` output.

## Known limitations

1. **English only**, and about multilingual NLP. See above.
2. **Category imbalance**, listed above.
3. **No external technical review.** One author, no peer review, no citation checking.
4. **Recency.** Written in 2026; specific architectures and benchmark names will date. The
   synthesis answers (199, 200) were written to outlive the specifics; the rest will not, and
   **questions 201–212 are the extreme case** — that arc is about named products by design.
5. **`for-agents/RECREATE-PROMPT.md` names Hugging Face dataset *families* rather than exact
   identifiers**, deliberately — Hub IDs drift, get gated and get renamed. Resolve any
   identifier against the Hub before relying on it.
6. **The glossary is complete but uneven.** `TERMINOLOGY.md` covers all three arcs; Part I
   (001–100) is more thorough per entry than Part II (101–200), where the long tail of
   single-mention species is listed rather than defined. Part III (201–212) is complete.
7. **No second full-corpus Pokémon audit** has been run over 101–232.
8. **Scores are not comparable across the wrap fix.** Until v0.3.0 the scorer matched against
   wrapped text, so a named entity split across a line break scored as a shorter term or as
   nothing — 19 such entities across 17 answers, reaching back to question 102. The matcher now
   joins single newlines first. Every score recorded before that change understates its answer by
   an unknown amount.

## Ethical notes

* **Trademark.** Pokémon is a trademark of Nintendo / Creatures Inc. / GAME FREAK inc. This is
  an unaffiliated educational work using the names nominatively. No game assets, artwork, sprites
  or text are reproduced.
* **Sensitive topics.** Four questions — sign language (155), endangered language documentation
  (163), accessibility (183), and biometrics (184) — concern real communities. In each, the
  Pokémon framing is deliberately set aside where the human stakes are discussed, and the
  guidance given (community consent, payment, the CARE principles, refusing some deployments)
  is stated directly rather than through analogy. This was a considered choice; if it reads
  wrongly to someone from those communities, that is worth an issue.
* **No personal data.** The dataset contains no user data, no scraped content, and no PII.

## Maintenance

* `scripts/validate.py` must pass before any commit.
* `LEDGER.md` is regenerated and committed alongside content changes.
* Vocabulary changes to the scorer are committed separately from content, always.
* Contribution process: [CONTRIBUTING.md](CONTRIBUTING.md).

## Citation

```bibtex
@misc{elipokemon2026,
  title  = {ELIPok\'emon: Paired Technical and Analogical Answers to
            Machine Learning Interview Questions},
  author = {alvations},
  year   = {2026},
  note   = {Version 0.3.0},
  url    = {https://github.com/alvations/ELIPokemon}
}
```
