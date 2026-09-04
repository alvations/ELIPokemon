# ELIPokémon

> **E**xplain **L**ike **I** play **Pokémon** — a dataset of serious machine learning
> and LLM interview questions, each answered twice.

Every question in this dataset ships with **two** answers:

| Style | What it is | Where it lives |
| --- | --- | --- |
| 🎓 **Serious** | The answer you would give in an interview: precise, with the maths, the tradeoffs, and ASCII diagrams. | `answers/serious/` |
| ⚡ **Pokémon** | The same concept explained entirely through Pokémon battles, type charts, Gyms, and PP. | `answers/pokemon/` |

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

**100 questions** spanning the modern LLM stack and the classical ML fundamentals that
still get asked in every interview loop:

| Area | Questions |
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
└── scripts/
    ├── build_dataset.py       # markdown -> index.json + elipokemon.jsonl
    └── validate.py            # CI check: pairing, front matter, ASCII art, length
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
python3 scripts/pokemon_score.py            # score all 100, rewrite LEDGER.md
python3 scripts/pokemon_score.py --detail 042   # what one answer matched
python3 scripts/ledger_history.py           # the score trend across git history
```

[`LEDGER.md`](LEDGER.md) is generated and committed, and scoring is deterministic — so the diff
between two commits of that file *is* the change in Pokémon-ness, and `ledger_history.py`
replays it.

```
score = breadth (0-45) + density (0-35) + specificity (0-20)
```

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
[`021`](answers/pokemon/021-reward-models.md) on Goodharting a reward model and
[`038`](answers/pokemon/038-llm-as-a-judge.md) on judges that reward surface features. Use it to
*find* answers worth a human look. A low score is a question, not a verdict.

## Conventions

* **Serious answers** open with a one-paragraph "the answer you'd actually say out loud",
  then go deep. They contain at least one ASCII diagram, name the real papers, and end
  with the follow-up questions an interviewer is likely to ask next.
* **Pokémon answers** never break the metaphor to lecture. Every technical component maps
  onto something concrete in the games — a type chart, a Poké Ball, PP, EVs, a Gym badge —
  and the mapping is stated explicitly so the analogy stays checkable.
* Both answers are for the *same* question and must agree on the facts.
* [TERMINOLOGY.md](TERMINOLOGY.md) is the glossary: every Pokémon name, mechanic and
  recurring analogy the answers actually use, and what each one stands for. Read it if
  you know the machine learning but not the games.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: add a row to `questions/questions.tsv`,
write both answers, run `python3 scripts/validate.py`, open a PR.

## License

Content (questions and answers) is released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code in `scripts/` is MIT.
Pokémon is a trademark of Nintendo / Creatures Inc. / GAME FREAK inc. This project is an
unaffiliated educational work and uses the names nominatively for teaching purposes.
