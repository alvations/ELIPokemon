---
id: "148"
slug: modality-balance-training-recipes
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you balance modalities when training a multimodal model?"
tags: [data-mixture, curriculum, forgetting, stage-training, ablation, loss-weighting]
---

# Five hundred and ten points, and six stats to spend them on

Every Pokémon gets a fixed training budget: **510 effort points in total, and no more than 252 into
any single stat.** That is the whole game. Feed it **Protein** until Attack is capped and
**Carbos** until Speed is capped, and you have six points left — for HP, for Defence, for Special
Defence, for the rest of its life. There is no **Calcium** or **Zinc** or **HP Up** in the budget
any more. You spent it.

This is the multimodal training mixture exactly. Not "how much training" — **what you spent it on,
and what you therefore did not.**

## Do it in stages, in order 📶

```
   STAGE 1  THE WIRE ONLY      lens frozen, voice frozen. Only the translator learns.
                               material: pictures with captions
                               goal: teach the translator to speak the voice's language

   STAGE 2  BROAD TRAINING     let the voice learn too, and the top of the lens
                               material: journals, captions, price boards, plain writing
                               goal: general competence

   STAGE 3  INSTRUCTIONS       a small, clean, carefully chosen pile
                               material: real requests, with and without pictures
                               goal: doing what it is told, not merely describing
```

⚠️ Collapsing these into one is the classic mistake. Let the voice learn **while** the translator
is still gibberish and the voice adapts itself to gibberish. Both end up worse than if you had
simply gone in order (question 117).

## What breaks if you leave each one out 🧩

| What goes in the budget | What collapses without it |
| --- | --- |
| 📸 Well-written captions (question 146) | knowing *which* Pokémon is the red one |
| 📓 Field journals (question 124) | holding several at once, learning from the page |
| 📜 **Plain writing, no pictures** | **its ability to talk. Measurably.** |
| 🏷️ Price boards, charts, small print | anything with writing in the picture |
| 👉 Pointing practice | left, right, and which slot |

📌 **The plain writing is the one people cut, and the one they regret.** Drop it and every
picture-related number goes up while its ordinary conversation quietly degrades — and nobody
notices, because nobody was testing conversation during the picture training.

That is the **Four-Move Limit** again (question 134): four slots, and the fifth thing you teach it
costs you one of the first four. Published recipes spend somewhere between a fifth and a half of
the budget on plain writing. That range is wide because it depends how hard you are pushing.
**Test it. Do not copy somebody else's spread.**

## Train against weak opponents first 🪜

Nobody takes a **Level 5 Charmander** straight to **Lorelei**. You work up **Route 1** on
**Pidgey** and **Rattata** first, where battles are cheap, and you meet **Brock** before you meet
**Agatha**.

Same here: **train at a distance first, walk up close later.** Looking closely costs enormously
(question 121), and almost everything — what Pokémon are, how they relate, following an
instruction — is learnable from across the clearing. Save the expensive close-up stage for the end,
and for the material that genuinely needs it: the price boards and the charts.

The same holds for battle recordings and for cries. Short first. Long last.

## Two ways the budget leaks 🕳️

* **📏 The long battles drown out the short ones.** A forty-turn match against **Lance**'s team
  teaches forty times as much as one **Pidgey** on Route 1 — *by lasting longer*, not by being more
  valuable. If you are counting turns rather than battles, you have quietly decided that long
  documents matter forty times more than short ones. Decide that **on purpose** or not at all.
  An **Exp. Share** spreads the gain across the whole party; a per-turn tally hands it all to
  whoever was on the field longest.
* **🖼️ Do not drill it on reciting what it saw.** In the design where the picture is spliced into
  the sentence, there is a real temptation to train it to predict the picture-shaped pieces too.
  That is capacity spent teaching a Pokémon to describe its own eyesight back to itself. Skip those
  positions.

And the shortcut worth naming: **Rare Candy** raises a level instantly and grants **no effort
points at all**. It looks like progress. The Pokémon arrives at the League underneath its own
level, and you find out in the worst possible place.

## Test the spread cheaply, then commit 🧪

📌 Mixture decisions are the **highest-leverage and cheapest** thing to test: no rebuilding, no new
architecture, and a small Pokémon ranks the spreads about the way a big one does. Run the whole
sweep at low levels before spending a season's training on a guess.

⚠️ **And check the entire type chart after every change.** A spread that improves your headline
number and quietly costs three points of ordinary conversation is a bad trade — and you will
discover it months later, in front of somebody who asked a question with no picture attached.
