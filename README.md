# ELIPokémon

> **E**xplain **L**ike **I** play **Pokémon** — a dataset of serious machine learning
> and LLM interview questions, each answered twice.

**200 questions · 400 answers · ~259,000 words.** Every question ships with **two** answers:

| Style | What it is | Where it lives |
| --- | --- | --- |
| 🎓 **Serious** | The answer you would give in an interview: precise, with the maths, the tradeoffs, and ASCII diagrams. | `answers/serious/` |
| ⚡ **Pokémon** | The same concept explained entirely through Pokémon battles, type charts, Gyms and PP. | `answers/pokemon/` |

The pairing is the point. One answer proves you *know* the concept; the other proves
you *understand* it well enough to re-encode it in a completely different domain. That
makes ELIPokémon useful as an instruction-tuning set, a style-transfer benchmark, an
explanation-quality eval, or just a fun way to revise before an interview.

```
                        ┌──────────────────────────────┐
                        │   "Explain attention in      │
                        │    transformer models."      │
                        └───────────────┬──────────────┘
                                        │
                        ┌───────────────┴───────────────┐
                        ▼                               ▼
          ┌──────────────────────────┐    ┌──────────────────────────┐
          │  🎓 answers/serious/     │    │  ⚡ answers/pokemon/     │
          ├──────────────────────────┤    ├──────────────────────────┤
          │  Q·Kᵀ / √d_k → softmax   │    │  Pikachu checks the type │
          │  → weighted sum of V     │    │  chart before attacking  │
          │  Multi-head = subspaces  │    │  Multi-head = 3 coaches  │
          └──────────────────────────┘    └──────────────────────────┘
                        │                               │
                        └───────────────┬───────────────┘
                                        ▼
                          dataset/elipokemon.jsonl
```

## Contents

The set is built in three arcs.

### Core ML and LLM — questions 001–100

The modern LLM stack, plus the classical fundamentals that still get asked in every loop.

| Area | Covers |
| --- | --- |
| Transformers & architecture | attention, RoPE, multi-head, pre-norm, MoE, KV cache, GQA, FlashAttention |
| Training & scaling | pretraining vs SFT vs RLHF, scaling laws, instruction tuning, distillation |
| Alignment | RLHF, reward models, PPO, DPO, GRPO, Constitutional AI |
| Fine-tuning & efficiency | LoRA, QLoRA, quantization, pruning, speculative decoding |
| RAG & retrieval | embeddings, chunking, HNSW, hybrid search, rerankers, RAG eval |
| Prompting, agents & reasoning | chain-of-thought, in-context learning, ReAct, tool calling, MCP, test-time compute |
| Evaluation & reliability | perplexity, LLM-as-judge, contamination, hallucination, calibration |
| Safety & security | prompt injection, jailbreaks, guardrails, red teaming |
| ML fundamentals | bias-variance, regularization, backprop, optimizers, PCA, boosting |
| Systems & MLOps | mixed precision, FSDP, parallelism, drift, A/B testing, serving cost |

### Multilingual — questions 101–116

Cross-lingual transfer · tokenizer fairness and the token premium · the curse of
multilinguality · language sampling · shared vocabularies · script vs language ·
code-switching · language identification · transliteration · language adapters ·
embedding alignment · byte-level and tokenizer-free models · morphology · segmentation
without spaces · Unicode normalisation · multilingual instruction tuning.

### Multimodal — 45 questions

VLM architectures and connectors · image patching · cross-modal attention · contrastive
pretraining · resolution and tiling · hallucination · document QA · interleaved data ·
speech recognition · video · charts and diagrams · grounding · diffusion · speech LLMs ·
image-borne attacks · multimodal retrieval · computer-use agents · synthetic captions ·
benchmarks and contamination · mixture balance · medical imaging · 3D and depth · video
generation · image editing · referring segmentation · multimodal CoT · serving cost ·
watermarking and provenance · preference tuning · embeddings · audio generation ·
egocentric perception · remote sensing · tool-using agents · robotics · distillation ·
accessibility · biometrics · data flywheels · aesthetics scoring · 3D generation ·
production monitoring · model documentation · evaluation suites.

### Translation — 38 questions

MT evaluation beyond BLEU · low-resource MT · document-level translation · quality
estimation · terminology enforcement · domain adaptation · LLM vs NMT · off-target and
hallucinated output · formality and honorifics · gender bias · simultaneous interpretation ·
length constraints · post-editing · localisation · speech-to-speech · dubbing and lip-sync ·
sign language · code and markup · translation memory · dialects and varieties · endangered
language documentation · participatory MT · MT security and poisoning · translationese ·
human evaluation · named entities · multilingual RAG · user-generated content · controlled
authoring · infrastructure and cost · massively multilingual claims · terminology mining ·
regulated domains · CAT tools · multilingual safety · on-device translation · multilingual
reasoning · cross-lingual evaluation design.

### Synthesis — questions 199–200

How to choose between all of the above, and what actually transfers.

## Layout

```
ELIPokemon/
├── questions/
│   ├── questions.tsv          # source of truth: id, slug, category, difficulty, question
│   └── index.json             # generated browsable index
├── answers/
│   ├── serious/001-attention-mechanisms.md
│   └── pokemon/001-attention-mechanisms.md
├── dataset/
│   └── elipokemon.jsonl       # generated: one record per question, both answers inlined
├── scripts/
│   ├── build_dataset.py       # markdown -> index.json + elipokemon.jsonl
│   ├── validate.py            # CI check: pairing, front matter, ASCII art, length
│   ├── pokemon_score.py       # deterministic Pokémon-ness score -> LEDGER.md
│   ├── ledger_history.py      # replay the score trend across git history
│   └── revise.py              # LLM-assisted revision, with a revert-unless-better guard
├── prompts/
│   └── revise-pokemon-answer.md
└── for-agents/                # how this was built, what went wrong, how to rebuild it
```

Each answer file carries YAML front matter so the markdown is self-describing:

```yaml
---
id: "001"
slug: attention-mechanisms
style: serious
category: transformers
difficulty: core
question: "Can you explain the concept of attention mechanisms in transformer models?"
tags: [attention, self-attention, transformers, qkv]
---
```

## Usage

Build the JSONL and the index from the markdown:

```bash
python3 scripts/build_dataset.py
python3 scripts/validate.py
```

Load it:

```python
import json

with open("dataset/elipokemon.jsonl", encoding="utf-8") as fh:
    rows = [json.loads(line) for line in fh]

row = rows[0]
row["question"]         # "Can you explain the concept of attention mechanisms..."
row["answer_serious"]   # markdown, with ASCII diagrams
row["answer_pokemon"]   # markdown, with Pokémon
row["category"]         # "transformers"
row["difficulty"]       # "core"
row["tags"]             # ["attention", "self-attention", ...]
```

Or with 🤗 `datasets`:

```python
from datasets import load_dataset

ds = load_dataset("json", data_files="dataset/elipokemon.jsonl", split="train")
```

## Measuring and improving Pokémon-ness

A Pokémon answer that reaches for **named** entities — real species, moves, items, abilities,
characters, places — is doing more analogy work than one leaning on generic furniture
("a Trainer", "a Gym", "a battle"). That is measurable, so it is measured.

```bash
python3 scripts/pokemon_score.py                # score all 200, rewrite LEDGER.md
python3 scripts/pokemon_score.py --detail 042   # what one answer matched
python3 scripts/ledger_history.py               # the score trend across git history
```

[`LEDGER.md`](LEDGER.md) is generated and committed, and scoring is deterministic — so the diff
between two commits of that file *is* the change in Pokémon-ness, and `ledger_history.py`
replays it.

```
score = breadth (0-45) + density (0-35) + specificity (0-20)
```

Current: **mean 58.2 · median 54.4 · minimum 38.5** across 200 answers.

### Revising with Claude

[`scripts/revise.py`](scripts/revise.py) asks Claude to raise a low-scoring answer, using the
prompt in [`prompts/revise-pokemon-answer.md`](prompts/revise-pokemon-answer.md) — versioned in
the repo so changes to the instructions are reviewable.

```bash
pip install anthropic
python3 scripts/revise.py --lowest 5 --dry-run   # build prompts, no API calls
python3 scripts/revise.py --lowest 5             # revise, keeping only improvements
python3 scripts/revise.py --id 082 --min-gain 5
```

Each revision is fed the **serious** answer as the source of truth, and is discarded unless it
raises the score, keeps the front matter byte-identical, and still passes `validate.py`.

### The score is a search tool, not a target

It counts named entities; it cannot tell whether they earn their place. That makes it a proxy,
and this dataset contains answers about what happens when you optimise against one — see
[`021`](answers/pokemon/021-reward-models.md) on Goodharting a reward model,
[`038`](answers/pokemon/038-llm-as-a-judge.md) on judges that reward surface features, and
[`190`](answers/pokemon/190-image-quality-and-aesthetics.md) on aesthetic scorers that get gamed
into a house style. Use it to *find* answers worth a human look. A low score is a question, not
a verdict.

## Conventions

* **Serious answers** open with a one-paragraph "the answer you'd actually say out loud",
  then go deep. They contain at least one ASCII diagram, name the real papers, and end
  with the follow-up questions an interviewer is likely to ask next.
* **Pokémon answers** never break the metaphor to lecture. Every technical component maps
  onto something concrete in the games — a type chart, a Poké Ball, PP, EVs, a Gym badge —
  and the mapping is stated explicitly so the analogy stays checkable.
* **Pokémon accuracy is a correctness bar**, not a style. A species that cannot legally learn
  the move it is given is a defect in the same category as a wrong claim about softmax.
* Both answers are for the *same* question and must agree on the facts.
* A small number of questions — sign language (155), endangered languages (163), accessibility
  (183), biometrics (184) — reach a point where the analogy steps aside and the human stakes
  are stated plainly. That is deliberate.
* [TERMINOLOGY.md](TERMINOLOGY.md) is the glossary: every Pokémon name, mechanic and
  recurring analogy the answers actually use, and what each one stands for. Read it if
  you know the machine learning but not the games.

## Provenance and limitations

See **[DATASHEET.md](DATASHEET.md)** for the dataset card: how it was made, what was verified,
what was not, and what it should not be used for. The short version:

* Written and reviewed as a hand-authored dataset; the revision tooling in `scripts/revise.py`
  exists for future rounds and did not generate the committed answers.
* Every pair passes `scripts/validate.py`. Technical claims are stated at the level of a strong
  interview answer, not a paper — **verify before citing**.
* Pokémon facts were audited; 21 errors were found and fixed in the first pass, and further
  corrections are recorded in [CHANGELOG.md](CHANGELOG.md).
* `for-agents/` documents the build process, the failures, and a prompt for reconstructing the
  dataset from scratch.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: add a row to `questions/questions.tsv`,
write both answers, run `python3 scripts/validate.py`, open a PR.

## License

Content (questions and answers) is released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code in `scripts/` is MIT.
Pokémon is a trademark of Nintendo / Creatures Inc. / GAME FREAK inc. This project is an
unaffiliated educational work and uses the names nominatively for teaching purposes.
