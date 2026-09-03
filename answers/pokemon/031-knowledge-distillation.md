---
id: "031"
slug: knowledge-distillation
style: pokemon
category: training
difficulty: intermediate
question: "What is knowledge distillation and why does a student sometimes beat its teacher?"
tags: [distillation, dark-knowledge, temperature, soft-targets, model-compression]
---

# Distillation: the Champion trains the rookie

You have a Champion. Enormous, brilliant, and far too expensive to field in every casual match.

You'd like a **cheap little Pokémon** that plays nearly as well. So have the Champion teach it.

## Don't just tell it the answer 🎓

The rookie could learn from the answer key: *"In this position, the right move was Thunderbolt."*
One fact per position.

But ask the **Champion** and you get something far richer:

```
   📋 THE ANSWER KEY              🏆 THE CHAMPION'S ACTUAL READ
   ─────────────────              ────────────────────────────
   Thunderbolt ✅                  Thunderbolt   85%  "clearly best"
   Thunder     ❌                  Thunder       11%  "same idea, riskier"
   Surf        ❌                  Surf           2%
   Splash      ❌                  Splash         2%

   One fact.                      A whole worldview.
```

Look at what the second one smuggles in. The Champion is telling the rookie that **Thunderbolt and
Thunder are cousins** — same plan, different risk — while Surf is a completely different idea.
It's teaching the *shape of the decision*, not just the decision.

The answer key can never teach that. All it says is "these three were wrong," as if Thunder and
Splash were equally wrong. They are not remotely equally wrong.

That structure in the near-misses is the actual gift.

## Turning up the detail 🌡️

Problem: the Champion is *so* confident that in most positions it says **99.97% Thunderbolt** and
everything else rounds to nothing. The rookie learns "Thunderbolt" and nothing else.

So you ask the Champion to **think out loud less decisively**:

> *"Don't tell me your pick. Tell me how you'd rank all the options, and be generous with the ones
> you're dismissing."*

```
   confident:  ████████████████████▏▏▏▏      rookie learns: "Thunderbolt"
   softened:   ████████████▎▎▎▎▎▎▏▏▏         rookie learns: "Thunderbolt,
                                              then Thunder, then Surf,
                                              and Splash is absurd"
```

Same knowledge. Vastly more of it transmitted.

## How it's actually done 🔧

* 📼 **Watch the Champion play.** It plays ten thousand matches, the rookie studies the replays.
  Simple, and it works even if all you can do is *watch* the Champion — you don't need to get
  inside its head.
* 🧠 **Read its full ranking**, not just its pick. More information per position, but you need real
  access to how it thinks.
* 🔄 **The rookie plays, the Champion corrects.** The best version. Instead of studying Champion
  replays — positions the rookie would never reach on its own — the **rookie** plays and the
  Champion critiques *its* turns. The rookie gets coached in the positions it actually gets itself
  into. Much more useful than admiring a Champion's flawless game.

## How the rookie ends up better than the Champion 🤯

This genuinely happens, and there are real reasons:

**🎯 Pick the Champion's best games, not its average ones.** The big one. Have the Champion play
each position **eight times**, keep the best attempt, and train the rookie only on those.

The rookie is now learning from *the Champion at its best*, every single time. But the Champion, in
any given match, plays at its average. The rookie has been raised on a highlight reel that no
single Champion match ever matched.

**🧹 The Champion filters out the noise.** The original training records contained mistakes — bad
calls, mislabelled results, typos in the tournament log. The Champion averaged over all of it and
smoothed it out. The rookie learns from that smoothed version and never inherits the errors.

**♾️ Unlimited practice material.** The Champion can generate positions forever. The rookie trains
on far more material than ever actually existed.

**👥 Many Champions, one rookie.** Have five Champions each teach the rookie. It absorbs the
consensus of all five — while costing what one small Pokémon costs.

## The ceiling ⚠️

The rookie cannot learn what the Champion never shows it. Every one of the Champion's blind spots
gets inherited, faithfully. And there's a size floor — you cannot distil a Champion into a Magikarp
and expect Champion play; at some point the rookie simply doesn't have room for what it's being
taught.
