---
id: "171"
slug: human-evaluation-translation
style: pokemon
category: translation
difficulty: intermediate
question: "How do you run a human evaluation of translation quality properly?"
tags: [mqm, human-evaluation, rater-training, agreement, statistical-power, crowd-vs-expert]
---

# The crowd and the Elite Four are watching different battles

Every scoring scheme in question 129 was calibrated against people. So the people are the
foundation of the entire structure — and they are routinely assembled in ways that produce numbers
containing no information whatsoever.

## Who is in the stands matters more than how many 👥

This is the finding that decides everything, and it is not close.

```
   a battle where the Trainer sent Charizard into Brock's Gym at Pewter

   the crowd in the stands ─► "what a display! the Flamethrower was beautiful,
                              the Charizard looked magnificent"
                              ⚠️ HIGH MARKS. They never looked at the Type Chart.

   Lorelei, from the Elite  ─► "they sent a Fire/Flying type against Onix.
   Four                        Rock hits it FOUR times over. This was decided
                               before the first turn."
                              LOW MARKS. And she can say exactly why.
```

📌 The crowd is not stupid. **They are watching what they can see** — how it looked, how it flowed,
whether it was exciting. They cannot judge whether it was *correct*, because judging that requires
the thing they were never given: **the source.** They never saw that the opponent was **Onix**,
that **Charizard** is Fire *and* Flying — so a Rock move is doubled twice over — or that **Erika**'s
Grass Gym at Celadon was where this team would have walked it.

⚠️ And here is why that ruins modern evaluation. Every machine you are comparing is **already
fluent**. Every one of them produces something that reads beautifully. So a crowd rating fluency
cannot tell any of them apart, and the one that dropped a **not** scores exactly as well as the one
that did not.

**If you take one thing from this page: the judges must see the source, and must be able to read
it.**

## Mark the mistakes, do not award a number 📝

*"Rate this battle out of a hundred"* is cheap and enormously noisy — three experts will give three
different numbers for the same battle and none of them can say why.

Instead: **point at each mistake, say what kind it was, and say how bad.** The score falls out of
the marks. This is better for reasons that are entirely practical:

* 🎯 **Pointing at a specific moment is a far steadier judgement** than picking a number.
* 🩺 **You get a diagnosis, not a verdict** — which kinds of mistake dominate, and where.
* 💀 **And "how bad" can mean it.** A clumsy flourish and a Pokémon **fainting on stage** stop being
  points on one scale (question 129). One is a deduction. The other is a disaster.
* 🤝 **You can check whether your judges agree**, moment by moment, which tells you whether the whole
  exercise is measuring anything at all.

⚠️ The cost is real: trained judges, and roughly three to five times as long per battle. **Budget
for it, or stop describing what you ran as an evaluation.**

## The details that decide whether it was worth doing 🔧

* **🎓 Train the judges together first**, on a shared set, arguing until they converge. Skipping
  this is the single commonest reason a whole evaluation ends up in the bin.
* **📏 Measure whether they agree, and publish it.** ⚠️ Low agreement does not mean "noisy result".
  It means **your instrument measured nothing**, and the honest response is to throw it away rather
  than report it.
* **🎭 Hide which machine is which**, and **interleave them within a document** rather than showing
  one machine's whole output in a block. Judges **anchor** brutally — the same effect as question
  149's draft anchoring the translator.
* **📖 Give them the whole document.** ⚠️ Judging one line at a time makes every improvement from
  question 131 **invisible**, so a system that finally got **Nidoran♀** right gets no credit for it.
* **🎣 Slip in some known-good and known-terrible items** — a battle you have salted with an
  illegal moveset, a **Splash** where a **Thunderbolt** belonged — and report how the judges did on
  those.
* **📊 And run enough battles.** Twenty cannot separate two good Trainers. Work out beforehand how
  many you need, or accept that *"no difference found"* means **nothing was measured**.
* **💰 Pay them properly.** Rushed judges produce noise, and no amount of analysis afterwards
  removes it.

## Reporting it 🏅

Say what protocol you used, who the judges were and how qualified, whether they agreed, and how
confident the difference is. **A quality claim without those is an assertion.**

📌 And publish the **breakdown by kind of mistake**, not just the total. That breakdown is the only
part anybody can act on.
