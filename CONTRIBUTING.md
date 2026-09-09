# Contributing to ELIPokémon

## Adding a question

1. **Add a row to `questions/questions.tsv`** (tab separated, keep it sorted by id):

   ```
   201	continuous-batching	inference	advanced	What is continuous batching and how does it differ from static batching?
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

5. **Score the Pokémon answer and ground it if it is low:**

   ```bash
   python3 scripts/pokemon_score.py --detail 201
   ```

   The corpus minimum is **38.5**. If your answer lands below it, the fix is not to sprinkle
   species names in — it is to find the place where an abstraction is doing work a *real*
   Pokémon fact would do better. That substitution is the whole technique, and it is worked
   through in [`for-agents/LEARNINGS.md`](for-agents/LEARNINGS.md). Do it before you open the
   PR, not in a follow-up.

6. **Extend [`TERMINOLOGY.md`](TERMINOLOGY.md)** if you introduced a Pokémon entity the glossary
   does not already list, with a link to your answer.

7. Commit the regenerated `questions/index.json`, `dataset/elipokemon.jsonl` and `LEDGER.md`
   alongside your markdown.

## Two rules that are not negotiable

* **`python3 scripts/validate.py` must print OK before every commit.** A commit that breaks the
  gate poisons everyone who clones after it, because they inherit a red tree and lose the signal.
* **A `questions.tsv` row and its two answer files go in the same commit.** A row without answers
  breaks validation for every concurrent contributor.

## Changing the scorer

If `scripts/pokemon_score.py` needs a new vocabulary entry — and it will; five gaps were found
during the build — **commit the vocabulary change on its own, with no content change.**

A vocabulary change alters the meaning of every historical score. Keeping it in a separate
commit is what makes `ledger_history.py` readable and what lets a reader tell a real improvement
from a re-baselining. Say the before-and-after corpus mean in the commit message.

And apply the line the existing vocabulary draws: a term only marginally more specific than the
generic furniture it sits beside (`Gym Leader` next to `Gym`) does not go in. Counting it
inflates every score without any answer naming something real.

## Front matter

Every answer file starts with front matter. `id`, `slug`, `style` and `question` must match
`questions.tsv` exactly — `validate.py` enforces it.

```yaml
---
id: "201"
slug: continuous-batching
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
* **Prefer the fact that fits.** The strongest analogies in this dataset are the ones where
  Pokémon *already contains* the structure — Kanto's Gym order is a pipeline, EV spreads are a
  fixed budget, Blissey's 255 HP is a genuine outlier. If you are straining to make a species
  fit, the abstraction was probably the honest choice.
* **Do not lie to be cute.** A wrong analogy is worse than a boring one. The Pokémon answer
  must be consistent with the serious answer.
* Emoji are welcome as signposts; they are not a substitute for structure.

## Accuracy

Both answers describe the same reality. If a reviewer finds the two disagreeing, that is a
bug in the pair, not a stylistic difference. Fix both.

**Pokémon accuracy is a correctness bar.** A species that cannot legally learn the move you gave
it is a defect in exactly the same category as a wrong claim about softmax — not a lesser one.
The first audit of this dataset found 21 such errors, and they fell into five repeatable classes:
illegal movesets, invented numbers, wrong item effects, characters given the wrong role, and
mechanics that do not work as described. All five are the analogy exerting pressure on the facts.
If a fact would make your metaphor land better, that is exactly when to go and check it.

## Sensitive topics

A few questions concern real communities — sign language (155), endangered language documentation
(163), accessibility (183), biometrics (184). In those, the Pokémon framing is deliberately set
aside where the human stakes are discussed, and the guidance is given directly. If you write in
that territory, do the same, and say plainly what you are unsure of.
