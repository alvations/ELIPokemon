---
id: "011"
slug: mixture-of-experts
style: pokemon
category: architecture
difficulty: advanced
question: "What is a Mixture-of-Experts model and what are its tradeoffs?"
tags: [moe, sparse, routing, load-balancing, switch-transformer]
---

# Mixture-of-Experts is the Gym Leader roster

A dense model is one Trainer who personally handles every single battle. Fire opponent? Them.
Water opponent? Also them. Ghost, Dragon, Fairy? Them, them, them. They're a generalist, and
they're exhausted.

MoE is a **League**. Sixty-four specialist Gym Leaders on the roster, and a receptionist at the
front desk who takes one look at each challenger and sends them to the right two Gyms.

```
                         challenger walks in
                                 │
                        ┌────────▼────────┐
                        │  🛎️ RECEPTIONIST │  "Water-type, holding a Mystic Water,
                        │                 │   probably Rain — you want Misty and Wallace."
                        └────────┬────────┘
                                 │
              ┌──────────────────┴──────────────────┐
              ▼                                     ▼
     ┌─────────────────┐                  ┌─────────────────┐
     │ 🌊 MISTY        │                  │ 🌊 WALLACE      │
     │ Water Gym       │                  │ Water Gym       │
     │ 61% of the call │                  │ 28% of the call │
     └─────────────────┘                  └─────────────────┘

     🔥 Blaine   🪨 Brock   ⚡ Surge   👻 Morty   🐉 Clair   ... 59 more
     ─────────────────────────────────────────────────────────────────
                     all at home, drinking tea, costing nothing
```

Sixty-four Leaders on the payroll. **Two** show up to any given battle.

## Why this is such a good deal 💰

Your League *knows* sixty-four Gyms worth of expertise — every matchup, every niche, every
obscure type interaction. That's what makes it strong.

But any one battle only *costs* two Gym Leaders' time. Thirty-two times the knowledge, roughly
twice the effort per challenger.

Compare the one exhausted generalist: to know as much, they'd have to be thirty-two times
better at everything, and they'd have to bring all of it to every fight, including the ones
where 90% of it is irrelevant.

## The receptionist is the whole problem 🛎️

Nobody ever gets this right the first time, because the front desk has a vicious failure mode.

**Day 1:** the receptionist doesn't really know who's good, so they send people fairly randomly.
Misty gets slightly more challengers than average by pure chance.

**Day 30:** more practice → Misty's better → the receptionist notices → sends her more →
even better → sends her *even more*.

**Day 90:** Misty handles every battle in the League. She's fighting Dragon-types now, badly.
The other sixty-three Leaders haven't seen a challenger in months and have forgotten how to
fight. You are paying sixty-four salaries for one overworked Water specialist.

Fixes, all of which real Leagues use:

* 📊 **A fairness quota.** The receptionist is graded on spreading challengers around, not just
  on picking well. Directly penalise pile-ups.
* 🚪 **A daily cap per Gym.** Misty sees at most 40 challengers a day. Number 41 gets turned
  away — they walk through the League without fighting anyone. Genuinely bad for that
  challenger, and the cost of keeping the system balanced.
* 🎲 **Deliberate randomness early on**, so unproven Leaders actually get tried.
* ⚖️ **A quiet thumb on the scale.** The newest approach: skip the fairness grade entirely and
  just nudge each Leader's ranking up or down based on how busy they've been lately. Same
  balance, less interference with the receptionist's actual judgement.

## What you give up ⚠️

**Every Leader has to be in the building.** They may be drinking tea, but they need an office.
Your League needs a *building* for sixty-four Gyms while only ever using two at a time. MoE
saves you *effort*, not *space* — which is why it's brilliant for a big stadium and terrible for
a model on your laptop.

**Turned-away challengers.** When a Gym hits its cap, someone genuinely walks out unbattled.

**Fragile training.** The receptionist can collapse, quotas need tuning, and a League is fussier
to get running than one generalist.

**Retraining is awkward.** Send the League to a specialist camp and it tends to overfit — the
receptionist latches onto the new challengers' quirks and stops generalising.

## What do the Leaders actually specialise in? 🔬

Less romantic than you'd hope. You'd like Misty to be "the Water expert" and Blaine to be "the
Fire expert." When researchers actually look, the split is often more like *"this Leader handles
punctuation"* and *"this one handles numbers."*

The receptionist finds *a* useful division of labour. It's just not always the one you'd have
written on the org chart.
