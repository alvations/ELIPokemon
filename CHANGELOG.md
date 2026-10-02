# Changelog

All notable changes to ELIPokémon. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/); versions follow
[Semantic Versioning](https://semver.org/) applied to the dataset — a **minor** bump adds
questions, a **major** bump changes the schema or removes records.

Every entry below is traceable to a commit. Score movements are reproducible with
`python3 scripts/ledger_history.py`.

---

## [0.5.0] — 2026-10-02

**272 questions in the machine-learning domain, 70 in the medical one — 684 answers in all.**
The medical domain went from a scaffold with 35 questions to seven specialties of ten apiece.

### Added

**Medical waves one completion and two — m036–m070** (`70feba4`, `609b2d7`)

Fifty-five new pairs across all seven specialties. Domain mean 88.4, median 89.0, floor 62.6,
validator passing on all 140 files. Every specialty now holds exactly ten.

**`domains/medical/for-agents/CONVENTIONS.md`** (`c41b0fc`, `d863c67`)

The shared analogy registry. `BRIEF.md` step 5 had told every writer since the domain opened to
read it and it did not exist; two writers went looking, failed, and said so. It is extracted from
the pairs that exist rather than invented, every mapping names the pair that established it, and
it carries eleven house devices, the per-specialty tables, the mappings that are **not** available
with the reason from `SAFETY.md`, and nine mechanical claims that competent writers got wrong from
memory and that were caught against the disassemblies.

**`TERMINOLOGY.md` Part VI** (this release)

The twenty-seven Pokémon mechanics the medical domain brought into the corpus for the first time,
each with the exact mechanic and the generation it belongs to. Seven writers asked for this and
the brief holds that they report and integration adds, because seven people editing one glossary
in seven worktrees is a guaranteed conflict.

**`scripts/rewrap.py`** (`769bab3`)

The 98-column re-wrapper `LEARNINGS.md` has asked for since the first release. It was never a
committed script, so every writer rolled their own in the shared scratchpad — and in one wave
three of them had their copy silently overwritten mid-task by a sibling using the same filename.
It is surgical rather than a reflow tool: a paragraph already inside the limit is emitted byte for
byte, so the sweep it enabled is a readable 310-file commit instead of an unreadable one.

### Changed

**Vocabulary batch eleven, 1,820 → 1,928 terms** (`4a056e5`)

Every addition was reported by a writer as an exact string that was load-bearing and scored zero.
ML mean 69.0 → 69.1, medical 85.7 → 86.4, nothing below the floor.

The case the batch exists for is m039. `Stockpile`, `Swallow` and `Spit Up` carry its entire
central device and all three were invisible; the writer named them fourteen times for nothing and
wrote *"adding species names to lift the number would have made it a worse answer; the honest fix
is a vocabulary commit."* It was. **m039 goes 68.1 → 82.0 with not one word of the answer
changed.**

Four gaps were costing answers that had already shipped: `Magic Coat` and `Snatch` both appear in
the committed m031; `Reversal` was absent while `Flail` is present despite being the same
`EFFECT_FLAIL`; `Ho-Oh` was absent while nine comparable legendaries were present; and `Rock
Blast`, `Bullet Seed`, `Fury Swipes` and `Icicle Spear` are the whole multi-hit class.

`Parlyz Heal` is added **alongside** `Paralyze Heal` because `Parlyz Heal` is what
`src/data/items.h` calls it, and a writer kept the game's own spelling knowing it would score
nothing rather than silently correct the data file.

**The nine brief defects seven writers reported are settled** (`d863c67`)

Section order, the 98-character rule not applying to table rows, the basis-marker vocabulary and
form, whether `Sources` points at the standing list or repeats it, what the do-not-edit line means
about the medical ledger, the `TERMINOLOGY.md`/`CONTRIBUTING.md` conflict, scratchpad filename
collisions, and a `BrokenPipeError` that made `score.py --detail | head` look like a failure.

**The validator now enforces the house section it already claimed to** (`7745e49`)

`BRIEF.md` marked the plain-prose stakes section "the validator checks for it". It did not. Three
writers diagnosed that independently, and one named the consequence exactly: it is why five pairs
shipped under five bespoke headings, and why `m001`'s serious half had no such section at all for
seventy questions. The check is style-keyed and matches on a line prefix; verified by breaking it
on purpose.

### Fixed

**`answers/pokemon/260` — four claims, one root cause** (`3916d23`)

The encounter tables were written from memory. Route 1 does not have Pidgey as the commoner of two
species: Pidgey holds six slots and Rattata four, and the weights make them **exactly 128 each**.
Six rows against four coming out dead even is a sharper opening than the error was, because it is
the first lesson the table teaches — the count of slots is not the probability.

That error then propagated into three arguments built on a lopsided Route 1 that does not exist,
including a nucleus-cut paragraph claiming the rule "narrows to almost nothing" there when at 50
and 50 it cannot stop until it has taken both rows. The flattest table is the one the rule leaves
completely untouched, and the three-table comparison the paragraph now makes is the point it was
reaching for and failing to make. Score 100.0 → 99.5, and that trade is not close.

**310 over-wide paragraphs** (`4fbffb7`)

Mechanical, verified by differencing the whole diff's token multisets to zero and by both ledgers
being byte-identical before and after.

### The writers were right and the briefs were wrong, again

This remains the most useful section in any release. Across one wave of seven:

* **Two corrections I ordered had false premises.** The oncology five already carried the
  counterpart section under five bespoke headings, so renaming was right and adding would have
  duplicated correct prose — except `m030`, which argued overdiagnosis as a decision problem and
  never named it as a harm. The emergency five were in the same position. Both writers renamed
  instead of adding, and both said so.
* **A writer refused a mechanism rather than invent one.** Asked for the resistance mechanism that
  makes stewardship a collective-action problem, m045 supplies the *transfer* half from code and
  declines the *selection* half, naming the real competitive-play phenomenon and marking it as
  not-from-code, because inventing a selection mechanic would have been the dishonest version.
* **A writer argued the schema, not the answer.** Declining supportive and palliative care:
  a Pokémon half with no Pokémon in it is not a low-scoring pair, it is a **degenerate record**
  for a dataset whose premise is two registers of the same content. That argument is now a rule.
* **A writer predicted its successor's mistake.** Declining frailty: *"the next writer will reach
  for Shedinja too."* They will, so `CONVENTIONS.md` Part III says so.
* **Thirty-odd Pokémon claims were corrected against the disassemblies rather than written from
  memory**, among them: `Curse` costs half the bar only for a Ghost, so Snorlax as the user would
  have been an outright error; `Rapid Spin` clears exactly one thing per use; `Future Sight`
  computes damage at the moment of use; `Light Ball` doubles Special Attack only; Sandstorm's
  Rock-type Special Defence boost is a fourth-generation change and does not exist in Emerald;
  all three vending-machine drinks cost ¥200 whatever the sign says; the Safari Zone counter is
  set to 502; and *"most moves use `EFFECT_HIT`"* is false — it is 24 of 355, which killed a
  device and produced a better one.
* **A writer caught itself.** One answer's Sources paragraph claimed reads that belonged to two
  other answers in the same block. It was rewritten to name only what that answer uses, and the
  writer flagged it as exactly the failure mode `LEARNINGS.md` describes for parallel streams.

---

## [0.4.0] — 2026-10-02

**272 questions, 544 answers**, plus a **second domain** scaffolded under `domains/medical/`.

### Added

**More open weights — questions 233–252** (`038a135`, `fef079a`, `8666255`, `59ed46e`)

Gemma 4, Inkling, DeepSpeed-and-DeepSeek, and the Qwen line from 3.6 to 3.8. Each block was
written in an isolated checkout and integrated centrally.

**Optimisation — questions 253–272** (`86b040e`, `1842841`, `d5cd5ae`, `5b19496`)

Speculative decoding, decoding strategies and non-autoregressive generation, quantisation, and
kernels.

**A second domain** (`b6598f0`, `9e82719`, `395817c`) — seven clinical specialties, with the gate
and the safety framing written before any content, as this repository's own build notes prescribe.
See `domains/medical/SAFETY.md`.

**Glossary Part V** (`7767d8d`) — 432 distinct entities across the forty new questions, 26 defined
and 194 listed with links. The closing note states that this is the least thorough part of the
glossary per entry and why.

### Fixed

**Scorer bug 5 — a plural was a double penalty** (`a0ea301`)

A plural did not match its vocabulary entry, so it scored nothing as a named entity — and then,
where the singular's last word sits in the generic set, it scored *against* the answer as
furniture. 51 such mentions across 34 of 272 answers.

Fixed in the matcher and **scoped deliberately**: an optional trailing `s` on multi-word terms and
proper nouns only. The uncounted plurals included `Cuts`, `Transforms`, `Protects` and
`Earthquakes` — single-word moves that pluralise into ordinary English verbs — so a blanket rule
would have traded this under-count for an over-count, the defect already observed when `Cut`
matched as a move inside a fenced block. Both directions are tested.

### Changed — scorer vocabulary

| Commit | What | Corpus mean |
| --- | --- | --- |
| `acb30c8` | Ninth batch, 93 terms. The seventeen type-resist Berries, which carry the whole central device of 235 and scored nothing for fourteen mentions; `Drill Peck`, on which 243's contrast entirely rests; the Repel and Lure families; `Safari Ball` and `Potion` while ten other Ball types and three Potion tiers were already listed; five evolution-line holes of the Nidoran shape | 67.8 → 68.4 |

Five declined on the `Gym Leader` precedent: `Characteristic` (collides with an ordinary English
word exactly as `Nature` does, and `Nature` is already excluded), `Bait` and `Rock` (argued
against by the worker who proposed them), `Bag` and `IV Judge`.

### What the writing found that the briefs had wrong

Eight workers wrote these forty questions, and **six of them corrected the brief they were
given**. Recording this because it is the most useful thing in the release:

* **Inkling is not a base model.** The brief said it was; the reference implementation that
  shipped on release day documents a chat template and a seven-level effort dial. 238 became
  "the word *base* is doing two jobs", which is a better question.
* **MatFormer is not in Gemma 4**, and **attention logit soft-capping is gone** — both verified by
  grepping the reference library rather than trusting a summary.
* **The small Gemma mixture is faster than the comparable dense model on a consumer card**, not
  slower as the brief claimed. The genuine slow result is an offload path, which made 235 a better
  question about residency rather than FLOPs.
* **DeepSpeed is no longer Microsoft-governed**, and its version number promises nothing: the
  release script auto-increments the patch digit after every upload.
* **FlashInfer's JIT cache key is not per-shape** — it is compile-time traits only, which is the
  difference between warm-up costing a minute at boot and warm-up never ending.
* **Flash-Next is not in the Qwen 3.8 repository**, and the widely repeated total for it is an
  on-disk figure including a prediction module.
* **Tree verification is not settled practice**, and **linear attention was walked back** by the
  lab most associated with it.

### Known limitations at this release

Everything at 0.3.0 still applies. Two are added: the medical domain is governed separately and
more strictly, and scores are not comparable across the plural fix. Both are in
[DATASHEET.md](DATASHEET.md).

## [0.3.0] — 2026-09-20

**232 questions, 464 answers.** Adds a sixth arc on open weights, and fixes a scorer bug that had
been quietly under-counting the corpus since the beginning.

### Added

**Open weights — questions 213–232** (`e770d62`, `864e2f1`, `068c032`, `a95888d`)

Four detailed architecture walkthroughs, written in four parallel streams — one per family, each
in an isolated checkout, integrated and audited centrally.

| Questions | Family | Central material |
| --- | --- | --- |
| 213–217 | DeepSeek | MLA against GQA and MQA · fine-grained plus shared experts · multi-token prediction · FP8 training and cost figures · GRPO and MIT weights |
| 218–222 | Qwen | dense against MoE · hosted tiers against downloadable checkpoints · thinking budgets · context extension against trained context · the licence patchwork |
| 223–227 | Kimi | trillion-scale sparsity · Muon and MuonClip · agentic post-training and human-preference Elo · hosting 1M multimodal weights · two licences from one lab |
| 228–232 | Mechanisms | attention variants with real byte counts · expert routing · MTP and drafting · linear and hybrid attention · reading a model card into a serving stack |

**The arithmetic is reproduced, not asserted.** DeepSeek's inference config was read directly and
three independent checks reconcile with the published figures to the byte: 576 cached values over
61 layers gives 70,272 B per token; the Llama-3.1-405B and Qwen-2.5-72B comparisons come out at
516,096 B and 327,680 B; the expert arithmetic totals 670.9B parameters with 36.5B active.

**Source discipline, recorded per claim.** `arxiv.org`, `huggingface.co` and most vendor pages are
blocked from the build environment; `raw.githubusercontent.com` and the GitHub API are not. Both
Kimi licence files and both Kimi technical-report PDFs, DeepSeek's inference config, and Qwen's
own repository were therefore read **first-hand** and are marked primary. Everything else is
marked as coverage. Two Qwen model cards and the Max licence were read through verbatim
third-party reproductions — two of them, agreeing word for word — and the answers say so.

Where an answer links an arXiv identifier it now carries a **citation note** stating that the
paper was named from working knowledge and **not opened**, because the host is blocked. This was
added during integration: the first drafts described figures as coming "from the technical
report", which overstated the provenance.

**Two questions were rewritten against their own brief**, and both are better for it. 231 was
commissioned on linear-attention stacks; the lab most associated with them has since returned to
full attention over multi-hop reasoning deficits, so the question is built on the retraction
instead. 225 qualifies a leading arena placement on the merits — it is blind human-preference
Elo, which is question 202's Contest-appeal axis rather than a verifiable reward.

### Fixed

**Scorer bug 4 — a line wrap split multi-word entities** (`c4b9c91`)

Prose wraps at 98 columns, so an entity could straddle a line break. `Trick\nRoom` matched as the
move **Trick**; `Stealth\nRock` matched as nothing. An audit found **19 split entities across 17
of 232 answers**, reaching back to question 102 — every one of them a named entity the scorer
could not see, in an answer whose score had been treated as a measurement ever since.

Fixed in the matcher rather than by re-wrapping the 17 files: single newlines are joined before
matching, so the scorer sees what a reader sees. Paragraph breaks are untouched and the word
count is still taken from the original text.

### Changed — scorer vocabulary

| Commit | What | Corpus mean |
| --- | --- | --- |
| `813a4c1` | Eighth batch. The six Generation III Battle Frontier facilities and the seven Frontier Brains; all sixteen Kanto and Hoenn Badges, none of which were listed although every Gym Leader was; the delayed-damage moves; Reflect, whose partners Light Screen and Aurora Veil were already present; Starly and Staravia, where Staraptor was already listed; the rest of the Power items; Pokérus | 64.0 → 64.2 |

Three proposals were **declined** on the `Gym Leader` precedent — a term barely more specific than
the furniture it sits beside inflates every score without any answer naming something real:
`Doubles`, `Singles` and `Priority`. Three Frontier Brains (`Lucy`, `Brandon`, `Tucker`) are
listed and then excluded through `AMBIGUOUS`, as the file already does for `Karen` and `James`:
they collide with ordinary given names and no answer uses them.

### Grinding

One answer first drafted below the floor and was ground in the same batch: **222 at 43.2 → 92.3**,
by binding abstractions to specifics rather than adding vocabulary.

### Known limitations at this release

Everything at 0.2.0 still applies, and the recency warning now covers **201–232**. One is added:
**scores recorded before `c4b9c91` are not comparable with scores after it.** The wrap fix
changes the meaning of every historical score, as a vocabulary change does, and the discontinuity
is identifiable in `ledger_history.py` output.

## [0.2.0] — 2026-09-20

**212 questions, 424 answers.** Adds a fifth arc and closes two scorer vocabulary gaps.

### Added

**Frontier systems — questions 201–212** (`4bedcce`, `37e8bcc`, `4ae2d15`)

Twelve questions anchored on named systems as they stood in September 2026: TypeSafe AI's Jev
and the System One model class, training against proper scoring rules, what a constrained output
space does and does not guarantee, the `effort` dial on the Claude 5 family, tier routing across
GPT-5.6 Sol/Terra/Luna and the Claude lineup, million-token context windows, sparse
mixture-of-experts serving anchored on Upstage's Solar Open 2, open-weight equivalence across the
DeepSeek/Qwen/Kimi/GLM/Llama/Gemma field, distillation lineage from Gemini to Gemma 4, model name
collisions, capability thresholds and staged release, and how to read a model announcement.

Every answer in the arc ends with a dated **"where this stands"** note. The material was
assembled from public documentation and coverage rather than first-hand testing, and this is
stated in the answers themselves, in [README.md](README.md), in [DATASHEET.md](DATASHEET.md) and
in the glossary. Question 212 is explicitly reflexive about it: the brief that produced the arc
named a "lunar" model that does not exist, treated "Astra" as one product when two organisations
ship one, and placed Upstage's Solar beside OpenAI's Sol as though they were related. Those
errors are written up in the answer rather than quietly corrected.

**Glossary Part III** — 57 entities used in 201–212 had no entry. Added with the same rule as
Parts I and II: every term listed actually appears in an answer, and each is linked to the
answers that use it. 83 new links, all verified to resolve.

### Changed — scorer recalibrations

Committed separately from content, as always, with no content change in either.

| Commit | What | Corpus mean |
| --- | --- | --- |
| `3feab37` | Sixth gap. Focus Blast, Zap Cannon and Dynamic Punch were unknown to the scorer, as were No Guard, Illusion, the Contest system and the breeding items | 58.2 → 58.6 |
| `4a1342c` | Seventh gap, and the largest. **The Pokédex itself had no entry after 212 questions**, nor did Bill's PC, the S.S. Anne, the Hall of Fame, the regional storage developers, the terrains, Missingno., Truant or Slow Start | 59.0 → 62.1 |

`Bill` was deliberately **not** added as a character: the word collides with an ordinary English
noun, so it went into the `AMBIGUOUS` set and `Bill's PC` is counted instead. `Brier` was added
to the mechanics list by mistake during the first of these and removed before the commit — a
machine-learning term scoring as a Pokémon entity would have corrupted every score in the file.

### Grinding

Two answers first drafted below the corpus floor and were ground in the same batch, per the rule
in [CONTRIBUTING.md](CONTRIBUTING.md): **206 at 22.8 → 83.8** and **207 at 10.3 → 89.1**. Both had
leaned on storage and party language that the scorer treats as generic furniture by design; the
fix was binding them to named entities, not adding more words.

Corpus figures at this release: mean **62.1**, median **58.5**, minimum **39.9**, maximum
**100.0** across 212 answers.

### Known limitations at this release

Everything listed at 0.1.0 still applies. One is added: **the frontier arc is dated**. It names
products, prices, parameter counts and capability-framework tiers that were accurate in
September 2026 and are the fastest-moving facts in the dataset.

## [0.1.0] — 2026-09-09

First tagged release. **200 questions, 400 answers, all validating.**

### Added

**Core ML and LLM set — questions 001–100** (`6004c2b` … `d712c1d`)
The modern LLM stack plus classical fundamentals: transformers, alignment, fine-tuning,
inference, RAG, agents, evaluation, safety, systems.

**Multilingual — questions 101–116** (`45dd5cc`, `d94d7d1`)
Cross-lingual transfer, tokenizer fairness, the curse of multilinguality, script vs language,
code-switching, transliteration, adapters, Unicode normalisation.

**Multimodal — 45 questions** (`a2c0c57` … `70c68c8`)
VLM connectors, image patching, cross-modal attention, contrastive pretraining, resolution,
hallucination, document QA, ASR, video, charts, grounding, diffusion, speech LLMs, image-borne
attacks, retrieval, computer-use agents, synthetic captions, benchmarks, mixture balance,
medical imaging, 3D, editing, segmentation, serving, watermarking, preference tuning,
embeddings, audio generation, egocentric perception, remote sensing, tool use, robotics,
distillation, accessibility, biometrics, data flywheels, aesthetics, monitoring, documentation,
evaluation design.

**Translation — 38 questions** (`13e884e` … `ed189bc`)
MT evaluation, low-resource, document-level, quality estimation, terminology, domain
adaptation, LLM vs NMT, off-target output, formality, gender bias, simultaneous interpretation,
length constraints, post-editing, localisation, speech-to-speech, dubbing, sign language,
markup, translation memory, dialects, endangered languages, participatory MT, security,
translationese, human evaluation, named entities, multilingual RAG, UGC, controlled authoring,
infrastructure, coverage claims, terminology mining, regulated domains, CAT tools, multilingual
safety, on-device, multilingual reasoning, evaluation design.

**Synthesis — questions 199–200.** How to choose between the techniques, and what transfers.

**Tooling**
* `scripts/validate.py` — pairing, front matter, ASCII diagram and length gate. Written before
  the bulk of the content, and blocking before every commit.
* `scripts/build_dataset.py` — markdown → `questions/index.json` + `dataset/elipokemon.jsonl`.
* `scripts/pokemon_score.py` (`10535d0`) — deterministic named-entity score → `LEDGER.md`.
* `scripts/ledger_history.py` (`d4de87f`) — replays the score trend from git history.
* `scripts/revise.py` + `prompts/revise-pokemon-answer.md` (`d4de87f`) — LLM revision tooling
  with a revert-unless-better guard. **Did not generate any committed answer**; recorded in the
  script's docstring and in [DATASHEET.md](DATASHEET.md).

**Documentation**
* `TERMINOLOGY.md` (`cdc22d3`, `a29c0fe`, `4a9050a`) — glossary, every reference linked to its
  answer file. Extended to cover 101–200 at v0.1.0.
* `for-agents/` (`a8f146c`) — build history, learnings, a recreation prompt, and a resume
  checkpoint.
* `DATASHEET.md`, `CHANGELOG.md` — added at v0.1.0.

### Fixed

**21 Pokémon factual errors across 23 answers** (`1540837`). Five classes:

| Class | Example |
| --- | --- |
| Illegal movesets | Splash listed alongside Thunderbolt; Charizard given Surf |
| Invented numbers | Focus Sash described as leaving 8% HP (it leaves 1); Brock's Onix given 75 HP (41); a "Level 280" Pokémon |
| Wrong item effects | Damp Rock described as boosting Water moves (it extends rain) |
| Wrong character roles | Agatha and Lance used as Gym Leaders (both are Elite Four) |
| Mechanics that do not work | Targeting a fainted Pokémon; Swords Dance used six times past the +6 cap |

The most instructive: **Q040 used Flareon's Hidden Ability as an example of hallucination — but
the stated ability, Guts, is correct.** An answer *about* hallucination was demonstrating
nothing. Rewritten around a genuinely false claim.

Three further errors caught during the 101–200 batches:

* Volt Tackle described as a level-up move (Q145) — it is a bred Egg Move requiring a Light Ball.
* Water called 4× on Charizard (Q171) — it is 2×; the example was moved to Brock's Onix, where
  Rock genuinely is 4×.
* Regulation G described as banning restricted legendaries (Q187) — it permits one per team.

**Line-wrap regression** (`deb16b2`). String-replacement edits had joined prose past the
98-column limit. Fixed with a fenced-block-aware re-wrapper, committed separately.

### Changed — scorer recalibrations

Each of these changes the **meaning** of every historical score, so each was committed on its
own with **no content change**. They are the discontinuities in `ledger_history.py` output.

| Commit | What | Corpus mean |
| --- | --- | --- |
| `fd7e69f` | Count capitalised move names; mask overlapping terms so `Thunder Wave` does not also score as `Thunder`; restore ~40 accidentally dropped moves | 22.4 → 24.0 |
| `233ca23` | Kanto and Johto were missing from PLACES entirely; added landmarks, overworld items, regional Professors, villainous teams | 57.4 → 58.2 |
| `9214120` | The Nidoran line was missing from SPECIES; added Follow Me, Rage Powder, Spotlight, Egg Move, Egg Group | 57.7 → 58.4 |
| `9607240` | Trainer Classes. **Deliberately excluded** Gym Leader — barely more specific than the generic "Gym" it sits beside | 58.9 → 58.7 |
| `b8319c3` | The stat vitamins; the Bottle Cap / Ability Capsule / Heart Scale toolkit; Name Rater, Move Deleter, Move Reminder | 58.0 → 59.0 |

### Improvement waves

Twenty waves over answers 001–100 (`40c7e1f` … `5da187a`), one commit each so
`ledger_history.py` yields one row per wave. Mean over that range: **22.4 → 53.2**; answers
scoring zero: **16 → 0**; minimum: **0.0 → 38.5**.

Per-wave gains, in order — the flattening is reported rather than smoothed:

```
+2.9  +3.7  +2.9  +2.2  +2.7  +1.6  +1.8  +1.8  +1.8  +1.5
+0.9  +1.0  +0.8  +1.3  +1.0  +1.1  +1.0  +0.6  +0.6
```

Answers 101–200 were scored as written and ground in the same batch when they landed below the
corpus floor of 38.5, rather than deferred to a wave. **Twenty-five are recorded in the commit
messages with their before-and-after scores** (the lowest first-write was Q188 at 8.4, ground to
52.6); several more were lifted above the floor by the scorer vocabulary fixes above. The corpus
minimum never moved off 38.5.

### Known limitations at this release

Listed in full in [DATASHEET.md](DATASHEET.md). In short: technical claims are not
externally reviewed or citation-checked; no second full-corpus Pokémon audit has been run over
101–200; the category distribution is unbalanced; the dataset is English-only; and the
Pokémon-ness score is an acknowledged gameable proxy.

### Outstanding

* The stale `claude/elipokemon-ml-interview-dataset-qibsci` branch needs deleting in the GitHub
  UI — delete pushes were rejected from the build environment.
