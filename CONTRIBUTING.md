# Contributing to ELIPokémon

## Adding a question

1. **Add a row to `questions/questions.tsv`** (tab separated, keep it sorted by id):

   ```
   101	speculative-batching	inference	advanced	What is continuous batching and how does it differ from static batching?
   ```

   * `id` — zero-padded, three digits, never reused.
   * `slug` — lowercase, hyphenated, stable. It is part of the filename forever.
   * `category` — reuse an existing one where you can (`git`-grep column 3).
   * `difficulty` — `core`, `intermediate`, or `advanced`.

2. **Write `answers/serious/<id>-<slug>.md`.**

3. **Write `answers/pokemon/<id>-<slug>.md`.**

4. **Run the checks:**

   ```bash
   python3 scripts/validate.py && python3 scripts/build_dataset.py
   ```

5. Commit the regenerated `questions/index.json` and `dataset/elipokemon.jsonl` alongside
   your markdown.

## Front matter

Every answer file starts with front matter. `id`, `slug`, `style` and `question` must match
`questions.tsv` exactly — `validate.py` enforces it.

```yaml
---
id: "101"
slug: speculative-batching
style: serious        # or: pokemon
category: inference
difficulty: advanced
question: "What is continuous batching and how does it differ from static batching?"
tags: [batching, throughput, serving]
---
```

## Style guide — serious answers

* Open with a **lead paragraph** you could say out loud in an interview in 30 seconds.
* Then go deeper: mechanism, maths where it clarifies, and the **tradeoffs**. Interviewers
  are buying judgement, not recall.
* Include **at least one ASCII diagram** in a fenced code block. `validate.py` requires it.
  Box drawing characters (`┌ ─ ┐ │ └ ┘ ▼ ▲ ├ ┤`) are fine and render everywhere.
* Cite the real paper with a link the first time you name a technique.
* Close with a short **"What an interviewer digs into next"** list.
* Be honest about uncertainty. If the field disagrees, say the field disagrees.

## Style guide — Pokémon answers

* **Stay in the metaphor.** No "in other words, the softmax normalises the logits" escape
  hatches. If the Pokémon version cannot express it, find a better mapping.
* **Make the mapping explicit.** A short table or bullet list pinning each technical piece
  to its Pokémon counterpart keeps the analogy checkable instead of merely cute.
* **Use the real games.** Type effectiveness, PP, EVs/IVs, Poké Balls, Gym badges, HMs,
  the Day Care, Rare Candy, the Elite Four. Accurate details make the analogy land.
* **Do not lie to be cute.** A wrong analogy is worse than a boring one. The Pokémon answer
  must be consistent with the serious answer.
* Emoji are welcome as signposts; they are not a substitute for structure.

## Accuracy

Both answers describe the same reality. If a reviewer finds the two disagreeing, that is a
bug in the pair, not a stylistic difference. Fix both.
