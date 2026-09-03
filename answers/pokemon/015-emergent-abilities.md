---
id: "015"
slug: emergent-abilities
style: pokemon
category: research
difficulty: intermediate
question: "What are emergent abilities of LLMs, and are they real?"
tags: [emergence, phase-transitions, metrics, grokking, induction-heads]
---

# Emergent abilities: is it evolution, or is it the badge?

Your Magikarp is useless. Level 15, useless. Level 18, useless. Level 19, useless.

**Level 20: GYARADOS.** 💥

That's the emergence story. Nothing, nothing, nothing — then a monster. And if capabilities work
like that, you genuinely cannot predict what your next Pokémon will be able to do.

## The counter-argument: check what you're measuring 📏

Suppose your only test is **"can it beat Brock's Onix?"** — pass or fail, no partial credit.

```
  Lv15 Magikarp: loses.  ❌
  Lv18 Magikarp: loses.  ❌
  Lv19 Magikarp: loses.  ❌
  Lv20 Gyarados: WINS.   ✅   ← "EMERGENCE!"
```

But now measure **how much damage it dealt** instead:

```
  Lv15: 4 damage    ▏
  Lv16: 9 damage    ▎
  Lv17: 19 damage   ▌
  Lv18: 38 damage   █
  Lv19: 71 damage   ██        ← Onix has 75 HP
  Lv20: 140 damage  ████
```

It was **doubling every level the whole time**. Perfectly smooth. Utterly predictable.

Nothing jumped. Your *scoreboard* jumped, because "beat Onix" is a cliff at 75 HP and you
happened to cross it between Levels 19 and 20.

```
   "damage dealt"                    "did you win?"
   (smooth, tells you what's         (a cliff — manufactures a
    coming)                           jump out of smooth progress)

   │           ...•••                 │              ████
   │      ..•••                       │              █
   │  ..••                            │______________█
   └─────────────────────►            └─────────────────────►
```

Swap the pass/fail scoreboard for a continuous one and most "emergence" flattens right out.
**A cliff-shaped test invents cliffs.** This is the single most useful thing to know here.

## But sometimes it really *is* evolution 🌟

Don't overcorrect. Some jumps are genuinely structural.

**Learning to copy.** At one specific point in training, a Trainer suddenly develops the knack of
*"they did X earlier, and Y followed — so if X happens again, expect Y."* Before that moment they
simply cannot do it. After, they can. And you can literally watch it happen: there's a visible
kink in the training curve at exactly that moment. That's not the scoreboard — that's a new
circuit forming, like a Pokémon actually evolving.

**Grokking.** A Trainer memorises every practice battle perfectly, then plateaus for *ages*,
looking like they've stopped learning. Then, long after everyone gave up watching, it suddenly
clicks and they can handle opponents they've never seen. Genuine reorganisation — they stopped
memorising battles and started understanding battling.

## The part that matters in practice 💼

Here's the thing: if your tournament requires beating Onix, then *"but the damage curve was
smooth!"* wins you nothing. The Pokémon couldn't do the job, and now it can.

For a **coach** planning next season, measure continuously — that's what lets you forecast.
For a **tournament entry decision**, the cliff is exactly the thing you care about.

## The honest summary 📌

* Ability usually grows **smoothly**.
* **Scoreboards** and **product requirements** are usually **cliffs**, and cliffs fake jumps.
* But a small number of **real evolutions** do happen mid-training — new circuits genuinely
  clicking into place.

If someone tells you a model "suddenly gained" an ability, the first question is always: *did the
Pokémon evolve, or did you just move the badge requirement?*
