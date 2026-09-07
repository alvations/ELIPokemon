---
id: "147"
slug: multimodal-benchmarks-contamination
style: pokemon
category: multimodal
difficulty: intermediate
question: "Why are multimodal benchmark scores so unreliable?"
tags: [benchmarks, contamination, blind-baseline, saturation, mmmu, evaluation-design]
---

# Beating the Elite Four proves less than you think

**Lorelei**, then **Bruno**, then **Agatha**, then **Lance**. Fixed teams. Fixed order. The same
Pokémon in the same slots every single time, forever.

A Trainer who clears all four is impressive. A Trainer who clears all four **having watched a
recording of that exact run beforehand** has demonstrated a good memory.

Both get the same badge, and the badge does not distinguish them.

## Run the blindfold test first 🙈

Before believing any score at all, ask the one question that settles most of it:

**How well does it do without looking?**

```
   the score everyone quotes:          68%
   the same Pokédex, screen covered:   54%    ← this "looking" test was mostly not looking
   pure guessing between four options: 25%

   what it can actually SEE is the gap. Fourteen points. Not sixty-eight.
```

📌 An alarming share of "look at this and answer" questions never needed the picture. *"What colour
is a **Charizard**?"* is answerable from having heard of Charizard. *"Which of these four is a
Water type?"* is answerable if three of the options are obviously not Pokémon at all. And sometimes
only one option is even grammatical.

⚠️ **Run this on your own numbers, not just other people's.** It costs one extra run with the screen
covered.

## The rest of what goes wrong 🧨

* **📼 It has seen the test.** The famous battles are on every recording in circulation, and
  everything trains on everything. And you **cannot check this the way you check written material**
  — the same photograph crops up cropped, resized and recoloured, so you have to match on **how it
  looks**, not on the filename. Almost nobody says they did.
* **🅰️ It just likes the first option.** Pokédexes have position habits. **Shuffle the four answers
  and score it again** — real ability does not care what order they are in, a habit does. This
  catches far more than it ought to.
* **🖼️ In battle recordings, one still is usually enough** (question 126). Same disease, different
  sense.
* **🎰 At the top, it is all luck.** Once something clears the League nine times in ten, the last
  tenth is a **Focus Blast** missing and a critical hit landing — not skill. Movement up there is
  weather, and a chunk of the remaining "failures" are questions whose official answers are simply
  wrong.
* **📋 It matters how you asked.** Where the picture sits relative to the question, whether the
  options are lettered, whether you asked it to think first — several points, on formatting alone.
  Two Pokédexes compared under different prompts have not been compared.
* **🧑‍⚖️ And the judge often cannot see either.** Grading an open answer by having somebody read a
  *description* of the battle rather than watching it means you are grading **plausibility**
  (question 038). A beautifully argued wrong answer wins.

## What to do instead 🛠️

**Build a small League of your own.** A hundred battles from the format you actually play, judged by
somebody who knows it. Nobody has trained on it, it measures the thing you care about, and you can
look at every single loss.

For public numbers, report defensively:

* 🙈 the score **and** the blindfolded score;
* 📝 exactly how you asked, and where the picture went;
* 🔀 the shuffled-options result;
* 📅 which Pokédex, and when;
* 🗂️ **and the breakdown by type.** An overall number averages together reading small print,
  counting, telling left from right, and general knowledge — which have **nothing to do with each
  other**. A Trainer superb against Water and hopeless against Ghost averages to "fine", and "fine"
  describes neither half.

## The uncomfortable part 😬

A Pokédex can climb to the top of the League table, genuinely be better **at that table**, and be
**no better at looking at anything** — if what improved was its general knowledge, its taste in
lettered options, or the fact that it had already seen the fights.

📌 That is not a rare failure of testing. **It is what happens by default unless somebody checks.**
And the check is one run with the screen covered.
