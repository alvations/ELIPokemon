---
id: "102"
slug: tokenizer-fairness-token-premium
style: pokemon
category: multilingual
difficulty: core
question: "Why do non-Latin scripts consume more tokens, and what does that token premium cost?"
tags: [tokenization, fairness, fertility, byte-fallback, cost]
---

# Some Trainers pay more PP for the exact same order

Two Trainers, same battle, same plan: *knock out the Gyarados with an Electric attack.*

Trainer A's Pikachu has **Thunderbolt**: 15 PP. Fifteen goes at it.

Trainer B has to spell the identical instruction out one syllable at a time, and every syllable
burns a PP. Same order, same result, **eight times the PP**.

That is not a story. That is what a tokenizer does to a language it barely saw.

## Where the bill comes from 💸

The Move Tutor only bundles up the moves it has seen a lot. Drill in Kanto and *Thunderbolt*
becomes one clean move — one button, 15 PP. Bring a language the tutor met twice and there is no
bundled move for it, so you are stuck spelling:

```
   😌 THE CHEAP LANGUAGE                    😰 THE EXPENSIVE LANGUAGE
   ─────────────────────                    ────────────────────────
   "Thunderbolt"     ► 1 slot               "Thun-der-bo-lt"   ► 4 slots
   15 PP, one press                         and if the tutor has never seen
                                            the letters either, each letter
                                            splits again ► 12 slots

   Same order. Same Gyarados. Twelve times the cost.
```

Worst case is a script the tutor has no entry for at all — the Unown alphabet in the Ruins of
Alph, or the Braille on the Sealed Chamber walls. Then every single character gets broken into
three, because the tutor is spelling out marks it cannot read.

## The names that survive the trip 🌍

Some things the tutor bundles everywhere. **Pikachu** is Pikachu in Kanto, in Kalos, in Galar,
in every region there is — one entry in every tutor's book, one slot, always.

Bulbasaur is not so lucky. In Japan that same Pokémon is **Fushigidane**; in Germany
**Bisasam**; in France **Bulbizarre**. Charmander is **Hitokage**, **Glumanda**, **Salamèche**.
The Kanto tutor bundled exactly one of those spellings. Every other region's Trainer spells
their own starter out by hand, letter by letter, every single time they mention it.

The luckiest word in the language costs one slot. The name of your own Bulbasaur costs nine.

## It is Pressure, permanently 👻

You know this mechanic. Dusknoir and Articuno have **Pressure**: every move you aim at them
costs **2 PP instead of 1**. Your fifteen Thunderbolts become seven.

Now imagine a Trainer whose every opponent, every battle, forever, has Pressure — and worse
odds than double. That is what writing in Telugu, Amharic or Burmese costs against a tokenizer
trained mostly on English.

## Four things that breaks 🧨

**1. 💰 The bill.** You are charged by the PP, not by the plan. The Trainers charged the most are
usually the ones with the least to spend.

**2. 🎒 The bag shrinks.** Everyone is told they get the same enormous bag. But the bag holds
*PP*, not *ideas*. If your ideas cost five PP each, your bag is a fifth the size — and the long
Pokédex entry that fits comfortably for one Trainer gets cut off halfway for another.

**3. 🐌 It is slower.** Each PP is a turn. More PP per order means more turns per order, and
your opponent is not waiting.

**4. 🎯 It aims worse.** This is the one people forget. A Pokémon executing *"Thunderbolt"* as one
clean move hits hard. One executing *"Thun... der... bo... lt"* across twelve fumbling turns has
to remember at turn twelve what it started at turn one. **Spelling it out does not just cost
more. It lands worse.**

## Patching it up 🩹

* 🍎 **Leppa Berries.** Restore some PP to one move. Real relief, one move at a time, and you
  cannot carry enough of them to fix a whole journey.
* 📖 **Send the tutor back to school on a fairer mix of regions.** The proper fix. Teach it the
  Paldean and Alolan and Hisuian material properly and those orders bundle up too.
* 🎓 **Teach it a bundle of new moves just for one region.** Targeted, effective — and the new
  moves arrive with zero practice behind them, so they need drilling before they are worth
  their slot.
* 🧱 **Refuse to bundle anything for anybody.** Everyone spells everything out, letter by letter.
  Perfectly fair. Perfectly slow. Nobody gets a Thunderbolt button.

📌 The move list is not neutral furniture. **Whoever the tutor practised on gets the cheap
buttons**, and everyone else pays the difference in PP, in bag space, in speed and in accuracy.
