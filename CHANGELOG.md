# Changelog

All notable changes to ELIPokémon. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/); versions follow
[Semantic Versioning](https://semver.org/) applied to the dataset — a **minor** bump adds
questions, a **major** bump changes the schema or removes records.

Every entry below is traceable to a commit. Score movements are reproducible with
`python3 scripts/ledger_history.py`.

---

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
