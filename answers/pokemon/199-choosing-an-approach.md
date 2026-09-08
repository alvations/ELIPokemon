---
id: "199"
slug: choosing-an-approach
style: pokemon
category: synthesis
difficulty: advanced
question: "Given all these techniques, how do you decide which one your problem needs?"
tags: [decision-framework, prioritisation, cost, synthesis, diagnosis]
---

# Read the Type Chart before you pick the Pokémon

Almost every page in this dataset hands you **a Pokémon**. This one is about **not sending the wrong
one out**, which is where the losses actually happen.

📌 A Trainer who owns every Pokémon and never checks the matchup loses to a Trainer who owns six and
does.

## Diagnose first 🔍

Nearly every failure in this whole dataset falls into **one of five buckets**, and each has a
different cheapest answer. Working out which takes an afternoon. **Skipping it costs a season.**

```
   ┌─ Was the information even in the picture? ─────────────────────────────┐
   │  Hand it a perfect written description instead. Does it answer now?    │
   │      YES ─► 👁️ IT COULD NOT SEE. Walk closer. Panel it. Read the print │
   │             (q121, q123, q127). ⚠️ More thinking will not help (q160).  │
   │      NO  ─► keep going                                                 │
   ├─ Does it get it right in Kanto, or on the easy half? ──────────────────┤
   │      YES ─► 🌏 IT HAS NEVER BEEN THERE. Data, discs, per-region work    │
   │             (q103, q110, q162, q185). Not an architecture problem.     │
   │      NO  ─► keep going                                                 │
   ├─ Is the answer fluent, confident, and wrong? ──────────────────────────┤
   │      YES ─► 👻 IT IS RECITING, NOT LOOKING. Grounding, citations,       │
   │             cap the lens and subtract (q122, q136, q140, q167).        │
   │      NO  ─► keep going                                                 │
   ├─ Does it know the answer and give it in the wrong SHAPE? ──────────────┤
   │      YES ─► 📏 IT NEEDS A RULE, NOT A BRAIN. Name list, length limit,   │
   │             mechanical checks (q133, q144, q156). Cheap. DO THIS FIRST. │
   │      NO  ─► keep going                                                 │
   └─ Only now: 🧠 it genuinely cannot work it out. Tools. A bigger Pokémon. ┘
```

⚠️ **The order is deliberate.** That last bucket is the one everybody reaches for **first**, and it
is the **rarest and most expensive.** It is buying a **Mewtwo** because you kept losing to Brock
without ever checking that your team was full of Fire types.

## Cheapest first, always 🪜

1. **🔭 Fix what goes in.** Walk closer, write the source better, clean the picture, settle the
   spelling (questions 121, 179, 115). ⚠️ **Consistently the biggest lever and the least glamorous** —
   which is exactly why it gets skipped.
2. **📖 Give it the context it was missing.** The whole document, the previous entries, the name list
   (questions 131, 133, 140).
3. **✅ Check the output mechanically** instead of hoping (questions 156, 136).
4. **🚦 Route.** Send the hard one-in-twenty somewhere better rather than upgrading everything
   (questions 132, 180). Do not send **Mewtwo** to fight a **Rattata**.
5. **🎓 And only then train something.** A **disc** before re-raising it, re-raising it before
   starting from an egg.

## Five questions before you build anything 🎯

* **⚖️ What does being wrong cost — and is it the same both ways?** If one kind of mistake is
  **categorically** worse, your score has to say so (questions 132, 187).
* **↩️ Can it be undone?** ⚠️ If not, **no accuracy number substitutes for a stop-and-confirm.** You
  cannot walk back up the ledge (questions 145, 181).
* **🙈 Who cannot check the answer?** If the person receiving it has no way to verify, invention
  becomes a **different class of problem** entirely (questions 183, 155).
* **📊 How many times a day?** At high volume, the small specialist's arithmetic wins (question 182).
  At low volume it never pays back.
* **🔒 What is not allowed to leave?** ⚠️ This constrains the architecture **before quality does**
  (questions 174, 187, 194).

## And the honest default 🏅

For most problems: **a good general Pokémon, standing close enough, with the name list, the relevant
pages retrieved, mechanical checks on the way out, hard cases routed elsewhere, and a small
hand-built gauntlet** (question 198).

📌 That combination beats a cleverer architecture **almost every time** — and it is boring enough
that teams walk straight past it on their way to the interesting problem.
