---
id: "002"
slug: positional-encodings-rope
style: pokemon
category: transformers
difficulty: core
question: "Why do transformers need positional encodings, and how does RoPE work?"
tags: [positional-encoding, rope, alibi, extrapolation]
---

# Positional encodings, or: which slot is that Pokémon in?

Attention sees your team as a **PC box**, not a party. A box is just a pile of six Pokémon —
it has no idea who leads and who is the ace in the back. But battle order is everything:
sending Magikarp out first and Charizard last is a completely different match from the
reverse, and a box cannot tell those two teams apart.

Positional encoding is how you stamp a slot number onto each Pokémon so the model knows it is
looking at a **party**, in order, and not a shoebox of monsters.

## Three ways to stamp the slot

```
  ┌────────────────────────────────────────────────────────────────────┐
  │ ABSOLUTE — the numbered Poké Ball                                  │
  │   Paint "1" through "6" on each ball before the match.             │
  │   ✗ Bring a 7th Pokémon and you have no ball for it.               │
  ├────────────────────────────────────────────────────────────────────┤
  │ RELATIVE — "how many switches ago?"                                │
  │   Don't number anyone; just track distance. ALiBi says the further  │
  │   back a Pokémon is, the less you care.                            │
  │   ✓ Works for any team size  ✗ Always biased toward whoever's out  │
  ├────────────────────────────────────────────────────────────────────┤
  │ ROTARY (RoPE) — the spinning Poké Ball                             │
  │   Give every ball a spin proportional to its slot number.          │
  │   ✓ Stamped individually, but only the *difference* in spin        │
  │     ever matters when two Pokémon interact.                        │
  └────────────────────────────────────────────────────────────────────┘
```

## RoPE: spin the ball 🌀

Instead of writing a number on the Poké Ball, you **spin** it. The lead ball gets no spin at
all, slot 2 gets one click, slot 4 gets three, slot 8 gets seven.

```
      slot 0            slot 3              slot 7
        ●                  ●                   ●
       ╱│╲               ╲ │                   │ ╱
      ╱ │ ╲               ╲│                   │╱
        │                  │                   │
     no spin          3 clicks           7 clicks
```

Here is why that is clever. When two Pokémon size each other up, what matters is the **angle
between their balls**, not either ball's own angle. Slot 3 vs slot 7 shows a gap of four
clicks. Slot 13 vs slot 17? Also four clicks. The Trainer never has to memorise which slots
exist — only *"you're four switches after me"*.

So you stamp each ball **individually** (cheap, do it once, keep it in the box) but the
Pokémon experience the stamp **relatively** (that's what actually decides the fight).

## Fast clicks and slow clicks 🕰️

Not every part of the ball spins at the same rate:

* ⚡ **Fast-spinning grooves** flip wildly between neighbouring slots. These tell you *"you're
  the one right before me"* — precise, short-range ordering. Lead vs second slot.
* 🐢 **Slow-spinning grooves** barely move between adjacent slots but drift steadily over a
  whole team. These tell you *"you're way back in the reserves"* — coarse, long-range position.

Together they give both fine local order and a sense of far-away structure.

## Bringing more than six 🎒

Your model trained on parties of six. Now you want a battle with sixty.

* 🔧 **Interpolation** — spin more slowly, so all sixty Pokémon fit into the range of spin the
  Trainer already recognises. Works, but now slots 3 and 4 look nearly identical, and you
  start confusing adjacent teammates.
* 🎯 **NTK / YaRN scaling** — slow down only the **slow** grooves (the long-range ones) and
  leave the fast grooves at full speed. You keep sharp neighbour-ordering while stretching the
  overall range. This is the good version.
* 🧭 **Bigger base** — rebuild the balls from the start to spin gently enough that sixty slots
  fit naturally, then train a little at that size. What serious long-context teams do.

Just handing a six-party Trainer sixty Pokémon with no adjustment is a disaster: the balls
spin to angles they have literally never seen, and the Trainer starts targeting nonsense.

## The one rule people get wrong

You spin the **Query** and the **Key** — what you're looking for, and what each Pokémon
advertises. You never spin the **Value**. A Pokémon's actual HP and stats don't change because
it's in slot 5 instead of slot 2. Only *who notices whom* depends on position.
