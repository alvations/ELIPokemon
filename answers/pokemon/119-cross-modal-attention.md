---
id: "119"
slug: cross-modal-attention
style: pokemon
category: multimodal
difficulty: intermediate
question: "How does cross-attention let text attend to image features?"
tags: [cross-attention, gating, grounding, attention-sinks, registers]
---

# Spotlight is a real move, and it is the whole mechanism

In a Double Battle, **Spotlight** does one thing: it picks a Pokémon on the field and makes
everything that turn aim at *that one*. Not a damage move. Not a status move. A move whose entire
effect is **deciding where the attention goes.**

That is cross-attention. One side asks; the other side is what gets looked at; and the only
question in the whole mechanism is **which of the things over there does each of the things over
here point at.**

## Your side asks. Their side gets looked at. 👁️

```
   YOUR SIDE (the question)          THEIR SIDE (the picture)
     🐦 Togekiss                        🪨 🔥 ⚡ 💧 🌿 👻   six tiles of what the lens saw
     🍄 Amoonguss
          │                                    ▲
          └──── each of yours picks ───────────┘
                where among theirs to look

   two of yours × six of theirs = twelve glances.

   NOT: everybody looking at everybody, twelve Pokémon in one free-for-all.
        that is eight-and-a-bit times the work and grows every time you add a tile.
```

📌 **This is why the Spotlight wiring wins on cost.** Your side never gets bigger. You can be
looking at a whole slate of tiles, or a whole *battle* of tiles, or six turns of footage, and the
question is still the same four words it always was. Add a hundred more tiles to their side and
your side does not lengthen by one slot.

The alternative — shoving every tile into your own party and letting the whole crowd consider
each other — grows on both sides at once, and grows *squared*.

## The dial that starts at zero 🎚️

Here is the part people get wrong when they bolt vision onto a Pokédex that already talks
perfectly well.

If you install a brand-new glancing mechanism and switch it on at full strength, its first
contribution is **noise** — an untrained eye shouting over a voice that already knew what it was
doing. You have not taught it to see. You have made it worse at talking.

So you install it holding a **Metronome**. The item that starts at plain, unmodified power and
climbs by a fifth for every consecutive turn the same move is used — never a jump, always from
×1.0 upward.

```
   turn 0:  dial at zero ─► the glance contributes NOTHING
                            the Pokédex behaves exactly as it did before you touched it

   later:   dial creeps up ─► it lets vision in, layer by layer, only as far as it earns
```

⚠️ And then **read the dial afterwards.** A Pokédex that "seems to ignore the picture" usually is
not being lazy — its dial genuinely never left zero, because the tiles it was being handed were
useless and the cheapest thing available was to answer from habit. The dial is a diagnostic. Look
at it before you blame the model.

## Where the wasted attention goes 🌀

Something has to be targeted every turn. That is a rule, not a preference — and it creates a
strange effect: when nothing on the field is worth looking at, the glances **do not stop**. They
pile onto whatever is nearest and emptiest. A blank corner of sky. A patch of grass. And that
tile, which contains nothing, ends up the most-looked-at thing on the slate.

The fix is exactly what a Doubles player would do: **give the junk somewhere harmless to go.**

* 🐦 **Togekiss with Follow Me** — steps forward and volunteers to be the target.
* 🍄 **Amoonguss with Rage Powder** — same idea, and a reminder that redirection is not universal:
  Grass types ignore the spores entirely, and so does anything wearing **Safety Goggles**.

Put a designated volunteer on the field, and the pointless targeting lands on it instead of
corrupting your reading of a real tile. Attention maps get visibly cleaner. Nothing else changes.

## Do not trust the glance as an explanation 🕵️

It is very tempting. You can *see* which tile each word looked at — surely that is the Pokédex
showing its working?

Careful. **Looking at something is not the same as being persuaded by it.** A Pokémon that
Spotlighted the Togekiss was not defeated *by* the Togekiss; it was redirected there. Ask instead
what would have changed if the tile had been different — that is a real test, and it disagrees
with the glance more often than anyone expects.

And do not average the glances together. Different heads are specialists — one tracks edges, one
tracks colour, one is a Follow Me sink absorbing junk. Averaging a specialist with a sink gives
you a number that describes neither.

## Four ways it goes wrong 🚨

* **🔒 The dial stays shut.** The tiles never became informative, so vision never got let in.
* **🎽 The eye was trained somewhere else.** Frozen tiles from a lens that learned on a different
  region: the tiles are *sharp*, they just do not separate the things you care about.
* **🔬 Too few askers.** Bottleneck the question down to a couple of scouts and it is fine for
  "is that a bird" and hopeless for *counting* the flock or reading the sign behind it.
* **🧭 The tiles forgot their coordinates.** Then the glance can find *what* — never *where*. The
  Pokédex names both legendary birds correctly and puts them on the wrong sides of the sky.
