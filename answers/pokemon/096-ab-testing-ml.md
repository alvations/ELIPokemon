---
id: "096"
slug: ab-testing-ml
style: pokemon
category: mlops
difficulty: intermediate
question: "How do you A/B test a machine learning or LLM feature?"
tags: [ab-testing, experimentation, power-analysis, novelty-effect, guardrails]
---

# A/B testing: does the new Trainer actually win more?

Your new Trainer scores better in practice — it finally stops leading Magikarp. **Does it win more
real matches?**

Those are genuinely different questions. A Trainer with better practice numbers can absolutely lose
to Cynthia — and one that "looks worse" on paper can win because it decides three times faster.

**Only real matches settle it.**

## Setting it up 🎲

**👤 Split by Trainer, not by match.**

Give half your Trainers the new lead — Garchomp instead of Magikarp — and half the old one, and
**keep each Trainer on one side for the whole test.**

Split by *match* instead and the same Trainer plays some matches with the new strategy and some with
the old — they'll get confused, carry habits across, and both sides get muddied.

**📋 Decide what counts BEFORE you start.**

```
   1️⃣ THE DECIDER — pick ONE, in advance
      Win rate. That's it. That's what decides.

   2️⃣ THE EXPLAINERS
      Average turns per match. Switch frequency. How often it
      remembers Stealth Rock is up. Why did it win?

   3️⃣ THE DEAL-BREAKERS ⚠️
      Time per turn. Cost. Complaint rate. Double Team violations.
      → These must NOT get worse, even if wins go up.
```

Tier 3 is what stops you shipping a Trainer that wins 2% more matches and takes **forty seconds per
turn.** Better and unusable.

**📐 Work out how many matches you need — first.**

Chasing a **big** improvement — Garchomp instead of Magikarp? A few hundred matches will show it.
Chasing a **1%** improvement? You need **tens of thousands.**

📌 And halving the effect you want to detect **quadruples** the matches needed.

If you can't get that many, the honest conclusion is *"I can't run this test"* — **not** *"I'll run it
anyway and squint."*

## Five ways to fool yourself 🚨

**1. 👀 Peeking.**

You check every morning. Day 4, the new Trainer is ahead! **Ship it!**

No. Check often enough and **random noise will look like a win at some point**, guaranteed. You didn't
find an effect; you found the day the dice favoured you.

📌 **Pick a duration in advance and stick to it.**

**2. ✨ Everything new looks good at first.**

Trainers try harder with a new lead. They actually read the Focus Sash and the Leftovers. They're curious.

Two weeks later, the novelty's gone and so is the improvement.

📌 **Run at least a full week.** And check whether the effect is *stable* or **drifting toward zero.**

**3. 🎰 Measuring twenty things.**

Track twenty metrics at once and **one will look significant by pure chance**, every single time.

Then you write it up as the finding. 📌 **Name your one decider in advance.**

**4. ⚖️ The split isn't actually even. ← check this FIRST**

You wanted 50/50 and you got **50.4/49.6.**

That's not rounding. **Something is broken** — your assignment is biased, and every number you're
about to interpret is contaminated.

Check this before you look at anything else. It's easy to miss and it invalidates everything.

**5. 🔁 The test changes the world it's testing.** If your new strategy changes which opponents your
Trainers meet, it's changing the very thing you're measuring against.

## Testing a Trainer specifically 🤖

* 🎲 **Results are noisier**, so you need more matches than a normal test.
* 💰 **Speed and cost are DEAL-BREAKERS**, not footnotes. A Trainer can be better and unaffordable.
* 🤔 **"Was that a good turn?" is hard to score automatically.** Use proxies — did they ask it to
  redo the turn? Did they override it? Did they give up and call a human? — plus a sample reviewed
  properly.
* 🎯 **Change ONE thing.** New strategy *and* new Trainer at once, and you'll never know which one
  did it.

## When you can't run a proper test ⚡

* 🔀 **Blend both sides into one list.** For ranking Pokémon to catch, show suggestions from both
  Trainers **mixed together** and see which get caught. Far more sensitive — needs a fraction of
  the matches.
* 👻 **Run it silently.** Let the new Trainer call every turn — *"I'd Thunderbolt here"* — **without
  anyone acting on it**, and
  compare its calls to the old one's. Zero risk. Catches every speed and crash problem. Tells you
  **nothing** about whether people prefer it.
* ⏰ **Alternate by time.** Everyone gets the new strategy on odd days, the old one on even days.
  Useful when the strategies interfere with each other.
