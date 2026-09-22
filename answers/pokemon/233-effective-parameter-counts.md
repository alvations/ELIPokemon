---
id: "233"
slug: effective-parameter-counts
style: pokemon
category: open-weights
difficulty: intermediate
question: "Gemma 4 ships checkpoints called E2B and E4B whose effective parameter count is not their parameter count. What is that label actually telling you?"
tags: [gemma, per-layer-embeddings, on-device, parameter-counts, memory]
---

# The Pokédex holds 151 entries. Chansey takes the hits. Only one of those is a weight you carry

**Professor Oak** hands you two things in **Pallet Town** and they are not the same kind of thing.
One is a **Pokédex** with room for all 151 **Kanto** entries. The other is a **Poké Ball** with a
Pokémon in it. Add them up and you can say you have "152 Pokémon" if you want to, and the sentence
will be useless, because the Pokédex has never taken a hit in its life and never will. It is a
book you flip open at **Pewter City** to check that **Brock**'s **Onix** is Rock and Ground before
you pick who goes first, and then it goes back in the bag.

E4B is **7.52B of weights on the cartridge and 4.67B that has to be awake at once**. The gap is a
second table, indexed rather than fought with — a Pokédex. The `E` is telling you which number
decides whether the thing fits on the device in your pocket. It is not telling you it battles like
a 4B model, and reading it that way is the mistake the label invites.

## The arithmetic, off the printed lines

```
   what Oak hands you in Pallet Town        what walks into the Pewter Gym
   ──────────────────────────────────       ───────────────────────────────
   Pokédex, 151 Kanto entries               Chansey, 250 / 5 / 5 / 35 / 105 / 50
   never battles, never faints              takes every hit Onix throws
   you read ONE entry at a time             all 450 points are awake all the time

   E2B  35 layers · width 1536              E4B  42 layers · width 2560
   ───────────────────────────────          ───────────────────────────────
   the part that fights      1.88 B         the part that fights      4.00 B
   the first table           0.40 B         the first table           0.67 B
                            ───────                                  ───────
   AWAKE                     2.28 B         AWAKE                     4.67 B
   the Pokédex 262,144×35×256  2.36 B       the Pokédex 262,144×42×256  2.82 B
                            ───────                                  ───────
   ON THE CARTRIDGE          4.65 B         ON THE CARTRIDGE          7.52 B
                                            (printed as ~2.3B / ~4.5B awake,
                                             ~5B / ~8B on the cartridge)

   what one turn costs you out of that book:

        262,144 entries                  ┌─ one entry ─┐
        ┌────────────────────────────────┴─────────────┴─────────┐
        │  ...                                                   │
        │  entry 18,422  →  [256 numbers]  ← you read this one    │
        │  ...                                                   │
        └────────────────────────────────────────────────────────┘
          1.41 GB of book on the shelf      42 × 256 = 10,752 numbers read
                                            = 5.25 KB of turn

          You keep 1.41 GB to read 5 KB. That gap is the whole reason the
          book is allowed to sit somewhere slow.
```

Chansey has to **be there**. Every point of that 250 HP is standing in front of **Rock Slide**
whether you wanted it to or not — you cannot leave a third of Chansey at home and bring it back
when the move connects. A Pokédex entry is the opposite: you know which page you want before the
turn starts, so the book can live in the bag, on the shelf, in the PC at the **Pokémon Center** —
anywhere at all, so long as you can flip to page 18,422 in time. That is why those 4.67B are the
number that has to fit and the 2.82B are not.

## What this is not: an evolution line

Do not read E2B and E4B as **Happiny** into **Chansey** into **Blissey**. That line is real — a
Happiny holding an **Oval Stone** and levelling up during the day becomes a Chansey, and a Chansey
with high friendship becomes a Blissey — and it is *not* what these two are. Thirty-five layers at
width 1536 and forty-two at 2560 are two separate species that happen to carry the same held item.
The older generation of this design did nest the small model inside the big one and bolted two
more tricks on beside it; this one kept the book and dropped the rest. Anyone who read the old
write-up and assumed the nesting carried forward has the wrong family tree.

It is also not a claim about how hard it hits, and here is the honest tension. **Eviolite** raises
Defence and Sp. Def by half on anything that can still evolve, so an Eviolite **Chansey** sits at
an effective 157.5 Sp. Def where **Blissey** — fully evolved, so the item does nothing for it at
all — sits at 135. Chansey's printed 450 total is *lower* than Blissey's 540 and
Chansey is the specially bulkier of the two: 250 × 157.5 against 255 × 135. One label, two
readings. "E4B" is an honest answer to *will it fit*; read as an answer to *how well does it
battle*, it is a 7.52B Pokémon wearing a 4.67B name tag, and the flattering reading is the one
that travels.

## Three places it bites

1. **The cartridge is sized by the big number.** You ship all 7.52B. "E4B" does not warn anyone
   downloading it that the Pokédex is coming too.
2. **The saving only happens if your game reads the book from the shelf.** A **Pokémon Center**
   that insists on healing the Pokédex along with the party gets nothing from any of this and just
   carries 7.52B around. Check what yours does before you budget for 4.67B.
3. **It does not scale up.** The 31B and the 26B-A4B carry no Pokédex at all. On a machine with
   room, the book was never the problem, and hauling it out to a shelf costs more than it saves.

## What a Gym Leader is listening for

That you split *what has to be awake* from *what merely has to exist* before you answer anything
at all. Then that you can say why a page you can look up is allowed to live somewhere slow and a
Pokémon standing in front of Onix is not. The strongest answers volunteer the reading failure
unprompted: a name like E4B answers a question about the **Poké Ball** and will be heard as an
answer about the battle.

## Where this stands, September 2026

The layer counts, the widths, the 262,144-entry table and the 256 numbers per page were read
straight off the published model definitions in `google-deepmind/gemma`, and cross-checked against
the same settings in `huggingface/transformers` — **primary**, both of them. The totals are my own
arithmetic over those settings, not quoted figures; they land within rounding of the published
"awake" counts, which is how you know the arithmetic is right. The published counts themselves are
**coverage**: the report and the model cards are behind an egress block here and were not read.
Those are the authority. Chansey's 250 / 5 / 5 / 35 / 105 / 50 has not moved in thirty years, and
neither has the point: a Pokédex is not a party member.
