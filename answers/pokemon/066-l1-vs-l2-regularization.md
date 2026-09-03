---
id: "066"
slug: l1-vs-l2-regularization
style: pokemon
category: fundamentals
difficulty: core
question: "What is the difference between L1 and L2 regularization?"
tags: [l1, l2, lasso, ridge, sparsity, weight-decay]
---

# L1 vs L2: trimming the team, or trimming everyone

Your Trainer is superstitious — remember the one who tracks hat colours and days of the week. You
need to cut some of that.

Two ways to cut, and they produce **completely different Trainers.**

## ✂️ L1 — release the weak ones

> *"Every Pokémon pays the same fixed upkeep. Can't justify it? Release it."*

Flat fee, regardless of how strong they are. So your Charizard easily earns its keep — and that
Rattata you never send out **cannot**. It goes.

```
   BEFORE                    AFTER L1
   ──────                    ────────
   Charizard  ████████       Charizard  ████████
   Blastoise  ██████         Blastoise  ██████
   Pikachu    ███            Pikachu    ███
   Rattata    ▌              Rattata    ─────  ⬅ RELEASED
   Zubat      ▏              Zubat      ─────  ⬅ RELEASED
   Caterpie   ▏              Caterpie   ─────  ⬅ RELEASED
```

You end up with a **small team of genuine contributors**, and the marginal ones are *gone* — not
diminished, gone. You can point at the survivors and say "these six matter."

## 🪶 L2 — everyone slims down

> *"Upkeep is proportional to how much you're relied on."*

Heavy contributors pay more, light ones pay almost nothing. So the Rattata's fee is tiny, and it
**never quite gets released** — it shrinks toward irrelevance forever without ever arriving.

```
   BEFORE                    AFTER L2
   ──────                    ────────
   Charizard  ████████       Charizard  █████
   Blastoise  ██████         Blastoise  ████
   Pikachu    ███            Pikachu    ██
   Rattata    ▌              Rattata    ▏     ⬅ still there!
   Zubat      ▏              Zubat      ▏     ⬅ still there!
   Caterpie   ▏              Caterpie   ▏     ⬅ still there!
```

You keep **everyone**, all a bit more modest. No single Pokémon carries the whole team, and the
Trainer stops betting everything on one read.

## The key difference in one line 🔑

> **L1 fires people. L2 gives everyone a pay cut.**

Because L1's fee is *fixed*, it eventually exceeds a weak Pokémon's contribution and out they go.
Because L2's fee shrinks *with* the Pokémon, it can never quite finish the job.

## Which do you want? 🎯

**✂️ L1 when you need to know WHO matters.** *"Which of these two hundred factors actually predict a
win?"* L1 hands you a short list. That's a real answer you can act on.

**🪶 L2 when you want a robust Trainer.** No sharp answer about who matters, and a Trainer far less
likely to be caught out by one weird match.

## L1's ugly habit ⚠️

Give L1 **two Pokémon that do the same job** — say two bulky Water types — and it keeps one and
releases the other. Essentially at random.

Rerun the training on slightly different footage and it keeps the *other* one. Your "these are the
important factors" list **changes between runs**, which is deeply unhelpful if anyone's making
decisions from it.

📌 **The fix: charge both fees at once.** A flat fee to clear out genuine deadweight, plus a
proportional fee so that redundant duplicates *share* the load instead of one being arbitrarily
executed. Best of both.

## Three things worth knowing for deep training 🔧

* 🪶 **L2 is the default.** Almost universally. Cutting Pokémon outright is handled separately and
  more deliberately.
* 🐛 **There's a famous bug here.** For years everyone charged upkeep by adding it to the training
  costs — and with modern training methods, that means Pokémon with volatile performance histories
  got **charged less**, entirely by accident. The fix is to charge upkeep **directly**, separately
  from everything else. Sounds like a technicality; it measurably improved training, and it's why
  the corrected method replaced the original.
* 🚫 **Some things shouldn't pay upkeep at all.** Referees, scorekeepers, the tournament rules —
  charging *those* is meaningless and actively harmful. Standard practice exempts them.
