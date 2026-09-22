---
id: "271"
slug: training-kernels-and-fusion
style: pokemon
category: optimization
difficulty: advanced
question: "A fine-tuning library claims 2x faster training and 70 percent less VRAM from custom kernels. Where does that actually come from?"
tags: [triton, fusion, lora, gradient-checkpointing, moe]
---

# Pickup never costs you a step. That is the whole secret.

A **Zigzagoon** with **Pickup** in the party turns up a **Super Potion** after a fight you were
having anyway. **Linoone**, **Meowth**, **Teddiursa** and **Phanpy** do the same. The item is
free, and it is free for one reason only: **the trip had already been made.** Nobody walked out to
**Route 10** especially.

That is the entire content of a training speed-up. The heavy lifting was cut down long ago — the
**Ultra Ball** does the catching and you are no longer wrestling anything to the ground. What is
left is a long tail of errands, each of which walks the length of the party, does one small thing
and walks back. Every one of those sits at about one blow struck per pace walked
([268](268-roofline-decode-and-prefill.md)), which is to say: it is all feet. **Doing several of
them on one trip is a pace saving, and there is nothing else in the box.**

Take the route throughout: **32 stretches**, a line of **4,096** to walk past, **8,192** to see to
in a morning.

## 1. One trip past the line, not eight

The careless way is to walk out to **Rock Tunnel** for each errand separately and come back each
time — and **Flash** does not make the walk shorter, it only lets you see.

```
   the careless way, per stretch, on the way out
        turn each one around        out 67.1 + back 67.1 M paces
        hand out the first item     out 67.1 + back 67.1
        hand out the second         out 67.1 + back 67.1
        square them up              out 134.2 + back 67.1
                                    ──────────────────── ≈ 8 trips  =  537 M
        the same again for the 8 at the end          ≈ 8 trips  =  134 M
                                                                    671 M

   one trip with the whole Bag on you
        out once, back once, both groups            = 2 trips  =  168 M
                                                     ────────────────────
   saved: 503 M paces a stretch × 32 stretches × (out and back)  ≈  32 G
          which is about 9.6 counts of every single morning, spent walking
```

## 2. Three things picked up, three put down, seven errands done

The nastiest errand on the route wants seven small things doing to the same line of **14,336**.
Done one at a time that is nineteen walks past them. Done properly it is six, and — the part that
matters more than the six — **nothing new has to be carried**, because each of them is set back
down exactly where it was picked up.

```
   one at a time   sigmoid, then the multiply, then the pairing, then three more
                   ≈ 13 out + 6 back  =  19 trips × 234.9 M  =  4.46 G a stretch
   all at once     3 out + 3 back     =   6 trips            =  1.41 G a stretch

   3.05 G × 32 stretches  ≈  97 G a morning, ≈ 29 counts of pure walking
```

## 3. Do not carry what the Move Reminder will give back

**Small scale.** You keep **Outrage** and the **Heart Scale**s, and you do not keep the two big
in-between things at all. They can be rebuilt on the way home out of what you are already
carrying, by the same errand that was going to touch them anyway. Two lines of **14,336** at 234.9
M paces each, on every one of 32 stretches — **15.0 G that is never carried at all**.

**Large scale.** This is the **Move Deleter** and the **Move Reminder** playing the same trick
with the dial turned up. Have the **Move Deleter** take **Outrage** off **Dragonite** for the
season, walk lighter all summer, and buy it back from the **Move Reminder** for one **Heart
Scale** the week you need it — the **Move Reminder** will hand back anything **Dragonite** could
have learned on the way up, which is exactly why you were safe to let it go. Keep a marker only
every **√32** — about every sixth stretch — and what you are carrying drops from *all of it* to
*the square root of it*, for the price of walking one extra leg: roughly **a third more walking
for a large multiple less on your back**. It is not free, it is not clever kernel work, and it is
doing a great deal of any "70% lighter" claim.

## 4. Write the difference, never the whole Pokédex page

When **Garchomp** gains a level you do not rewrite the species' **Pokédex** entry. You note what
changed.

```
   the whole page for one stretch's line       14,336 × 4,096 = 58.7 M entries
   the difference actually worth keeping   14,336·16 + 16·4,096 = 294,912 entries
                                                             ───────────────────
                                                             199× lighter
```

And the order you do it in is the whole game: fold the small correction in **first**, and nothing
page-sized is ever written down at any point. The same discipline everywhere else — a **Rattata**
stays in its **Poké Ball** until the turn it is sent out and goes straight back in afterwards. It
is out for one turn. That is how a party that would fill 16.1 G of your bag travels in 5 or 6 —
some of them kept at full size because they would not survive being folded up, the rest folded.

## 5. Sweet Scent, and why one-at-a-time is so bad

Use **Sweet Scent** in the grass and five wild Pokémon come out at once. One **Rock Slide**, or
one **Surf**, settles all five — the **Honey** you slathered on the tree brought them, and now
they are all in front of you together. The alternative is five separate encounters, each with its
own walk out, its own opening, its own return.

Take a route where **128** different patches each need seeing to, top-8, with 1,024 to get
through:

```
   8,192 visits ÷ 128 patches  =  64 to see to per patch

   one patch at a time:  a line of 64 against a wall of 1,536
                         that is 12 hands' worth of work
                         with 132 pairs of hands standing there — 9.1% of them busy
                         and you do it 128 times in a row
                         ≈ 768 separate errands for one stretch

   all at once:          all 128 patches in one sweep = 1,536 hands' worth, ~12 passes
```

And here is the part to keep. Everything on a patch gets looked at once and then used for everyone
routed to it, so **how much work you get per pace is exactly how many turned up at that patch.**

```
   blows struck = 2 · what is on the patch · how many came to it · 128 patches
   paces walked = 2 · what is on the patch · 128 patches          (looked at once)
   ratio        = how many came to that patch                     exactly
```

At 1,024 that is 64 — deep in the region where your feet are the problem, which is where doing
things in one sweep wins hugely. At a real morning's 8,192 it is 512, which is past the 295 the
Warden asks for, and the very same sweep wins far less. **Remember that the next time somebody
quotes you a multiplier** ([272](272-reading-a-kernel-benchmark.md)).

## Where this stands, September 2026

The errands above I watched being done, not heard about. **The numbers on the poster outside are
another matter**, and they are not all measuring the same trip. "Twice as fast with 70% less to
carry" is about the morning in general. "Three times as fast and 30% lighter" bundles the one-trip
errands together with *not walking past empty spaces in the line at all* — and skipping the gaps
is not an errand, it is a different line. "Twelve times faster on the 128-patch route" is measured
against somebody doing it one patch at a time, at 1,024, on one particular morning. Every one of
those is a ratio against a specific slow way of doing it at a specific size of job.

What keeps is the three habits, none of which belong to any one route. **Do the errands in one
trip, because errands are feet.** **Rebuild what the Move Reminder will hand back, rather than
carrying it.** **Fold the small correction in first, so the whole page is never written.** Those
were true before anyone owned an **Exp. Share**, and they will be true long after the current
**Bag** has been redesigned again.

## What a Gym Leader is listening for

* Why does doing the small errands in one trip matter, when they are not the hard part?
* How much of "70% lighter" is the errands, and how much is the **Move Deleter**?
* How much work do you get per pace on the 128-patch route, and what does that say about size?
