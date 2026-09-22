---
id: "237"
slug: shipping-open-weights-on-device
style: pokemon
category: open-weights
difficulty: intermediate
question: "You want to ship an open-weight model inside a phone application. What does the memory envelope really look like, and what does an Apache-2.0 licence let you do that a custom one does not?"
tags: [on-device, quantisation, apache-2, licensing, memory]
---

# A **Snorlax** weighs 460.0 kg and clips to your belt. The **HM** in your bag is the heavy thing

Two questions, one shape. **Snorlax** weighs 460.0 kilograms and has 160 base HP and none of that
is why you might not be able to take it with you — a **Poké Ball** handles the four hundred and
sixty kilos without comment. And "I own **HM03**" is not the same sentence as "I can use
**Surf**", because the **HM** has conditions stapled to it that the word *own* does not cover.

Both halves go wrong the same way: somebody quotes one number where three or four bind. For what
fits, the three are what has to be awake, what the battle has piled up so far, and what can sit on
a shelf. For what you are allowed to do, the parts that bite are the ones nobody reads: what
happens if you sue, what you have to print on the case, and whose name you may not use.

## What actually has to fit

Taking Gemma 4's E4B, whose numbers question 233 works through — the part that fights, and the
**Pokédex** that never does:

```
   E4B — 7.52 B on the cartridge, 4.67 B that has to be awake

   how tightly packed     the download      awake in the Ball     Pokédex on the shelf
   ──────────────────     ────────────      ─────────────────     ────────────────────
   loose                    15.04 GB            9.34 GB                 5.64 GB
   packed (int4)             3.76 GB            2.34 GB                 1.41 GB
   E2B, packed               2.33 GB            1.14 GB                 1.18 GB

   then the field, which nobody budgets for and which fills up as you play:

   turns elapsed   the windowed layers (512)   the hazard layers (4)    total
   ─────────────   ─────────────────────────   ──────────────────────   ─────
       8,192              20.97 MB                   134.2 MB          155 MB
      32,768              20.97 MB                   536.9 MB          558 MB
     131,072              20.97 MB                     2.15 GB        2.17 GB

   ┌─ an honest packed-E4B belt, for an 8,192-turn battle ─────────────┐
   │   awake in the Ball            2.34 GB                            │
   │   Spikes still on the field    0.16 GB                            │
   │   camera and the rest         ~0.15 GB                            │
   │                              ─────────                            │
   │   on the belt                 ~2.65 GB  ← this decides it         │
   │   on the shelf                ~1.41 GB  ← this does not           │
   │   what they downloaded         3.76 GB  ← this is what they feel  │
   └───────────────────────────────────────────────────────────────────┘
```

Three things there survive the particular model. **The field is the term that grows with play** —
**Snorlax** weighs 460.0 kg at the start of the battle and 460.0 kg at the end, but the **Spikes**
pile up, and a long battle is what pushes you over, not the Pokémon. **The download is not the
belt**: 3.76 GB fetched against 2.65 GB carried, and it is the fetch a player sees. And **the
512-step window flattens one whole column to a constant** — 20.97 MB whether the battle has run
8,192 turns or 131,072 — which is question 234's architecture, stated in megabytes.

## Packing: not whether, but who did the packing

On a phone it is packed or it is nothing, so the only question is how it got packed. Leave a
Pokémon at the **Day Care** and it will level up and learn its new moves and **throw out whatever
was in the first slot to make room, without asking you**. That is packing after the fact: it
works, it is cheap, and you find out what it cost when you reach for a move that is gone. Standing
there yourself while it levels — deciding which move goes — is packing done during the raising.
Google ships the second kind for Gemma 4 in several shapes: an unpacked checkpoint you pack
yourself, a 4-bit build, a phone build, and a 4-bit-weights build that keeps the working numbers
wide. Reported savings run about 60–66% on the big dense ones and visibly less on E4B, which is
what you would expect when a large share of E4B is **Pokédex** that does not pack the same way.
Treat those percentages as hearsay and weigh your own.

Two rules hold anyway. **Pack the fighters, go carefully with the book** — the **Pokédex** is read
one page at a time, and damage there shows up as one strange entry rather than a general dulling,
which is exactly the kind of fault nobody's benchmark catches. And **pack the field separately and
on purpose**: halving what each turn on the field costs you halves the biggest growing term in the
table, and it is a different decision from how tightly the Pokémon is packed.

## What a TM gives you that an HM does not

Assume the weights come as a **TM** rather than an **HM**. Four things change for someone putting
them on somebody else's device.

1. **You get covered if somebody comes after you — and it cuts both ways.** The grant is real, and
   it is **Destiny Bond**: the moment you turn round and attack the people who gave it to you, the
   protection goes down with you. A custom licence usually hands you the move and says nothing at
   all about who might object, which leaves the question open.
2. **What you owe is mechanical, and it is a printing job.** Keep the case, keep the number, say
   which ones you altered. **TM26** is **Earthquake** and the case says TM26; you do not get to
   file the number off. In practice that means the licence text goes on your acknowledgements
   screen. It is not catching: your version, your wrapper and your product can all stay shut, and
   you may hand them on under your own terms.
3. **There is no badge gate.** This is the real difference from the older terms. **HM03** is
   **Surf** and you cannot use Surf outside a battle without the **Soul Badge** in hand — and in
   those games the HM cannot be tossed, cannot be sold, and cannot even be forgotten without a
   trip to the **Move Deleter**. Conditions that travel with the disc, that the person who wrote
   them can change, and that you have to pass to everyone downstream. A **TM** has none of that,
   and since it stopped being single-use it does not run out either.
4. **You get the move, not the name.** You may teach **Earthquake** to anything that can learn it.
   You may not print **Silph Co.** on your own box, and you may not imply they made it.

And what it does *not* do, because this is where teams get hurt. It says nothing about where the
move came from or who else might have a claim on it. It makes no promise about the outcome: the
case prints **Focus Blast** at 70% and then you miss, and that is not a defect. And it has nothing
to say about the door you are walking through — **Flat Rules**, **VGC**, whatever **Regulation G**
says this season. Those attach to *entering*, not *owning*, and no TM description mentions them.

## What a Gym Leader is listening for

That you answer the fitting question with a sum and a turn count, not a weight. Then, on the disc,
that you go straight to **Destiny Bond**, the number printed on the case, and the name you may not
use — rather than saying "it's a TM, it's fine". The strongest answers close the loop: the disc
matters precisely because you are putting it in somebody else's bag, and handing it on is the one
act the conditions actually attach to.

## Where this stands, September 2026

The splits behind the table are **primary** — read from the published definitions in
`google-deepmind/gemma` — and the gigabytes are my arithmetic over them, not quotes. The terms of
the **TM** I read first-hand too, but in a narrower sense than it looks: I read the licence
sitting in that repository, which covers the *tools*. The **weights**' own disc I could not read,
because the pages that hold it are behind an egress block here; several independent write-ups
report Gemma 4's weights as shipping as a **TM** where the earlier generations shipped as an
**HM** with a use policy attached, and that is **coverage**. Do not take a licence claim from
anybody, this one included — open the file in the folder you actually downloaded, for the exact
checkpoint you actually shipped. The packing formats and the reported percentages are hearsay too.
The arithmetic and the four points survive. **Snorlax** has weighed 460.0 kg throughout.
