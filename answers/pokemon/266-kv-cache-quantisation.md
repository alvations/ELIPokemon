---
id: "266"
slug: kv-cache-quantisation
style: pokemon
category: optimization
difficulty: advanced
question: "At what context length does the KV cache cost more than the weights, and what does quantising the cache cost you?"
tags: [kv-cache, quantisation, long-context, serving, memory]
---

# Your six are a fixed cost. Everything you caught on the way is a bill that grows.

Everybody worries about the six. **Charizard**, **Snorlax**, **Lapras**, **Alakazam**, **Tauros**,
**Dragonite** — six on **Route 1**, still six at the **Indigo Plateau**, and you pay for them
once. What nobody watches is the pile behind you: every **Pidgey** out of the **Tall Grass**,
every **Zubat** in **Mt. Moon**, every **Magikarp** the salesman in the **Route 4** **Pokémon
Center** talked you into, every **Caterpie** in **Viridian Forest**. That bill grows with every
step, and somewhere on every journey it becomes the bigger number.

In **Kanto** that point arrives absurdly early, and you can prove it to the byte.

## The arithmetic, on two real save files

```
   ONE TRAINER'S BOXES  —  Kanto, the numbers the cartridge actually uses
   ──────────────────────────────────────────────────────────────────────
   a party Pokémon   44 B record + 11 B nickname + 11 B OT name  =  66 B
   a boxed Pokémon   33 B record + 11 B nickname + 11 B OT name  =  55 B

   your whole team   6 × 66                                      = 396 B
   ──────────────────────────────────────────────────────────────────────
   396 / 55 = 7.2      → THE EIGHTH POKEMON YOU BOX OUTWEIGHS YOUR TEAM

   one full box      20 × 55  =  1,100 B  =  2.8 teams
   all twelve boxes 240 × 55  = 13,200 B  =  33  teams
```

```
   THE HALL OF FAME  —  Indigo Plateau, past Lance and the Champion behind him
   ──────────────────────────────────────────────────────────────────────
   one Pokémon recorded there     16 B      (species, level, name)
   one team                        6 × 16 =    96 B
   room for                       50 teams
   ──────────────────────────────────────────────────────────────────────
   total                          50 × 96 = 4,800 B  =  12 teams

   Twelve times your party, to record clears you will never look at again.
   And there is room for exactly fifty. Not fifty-one.
```

Two things fall out that surprise people. **The eighth Pokémon you ever box outweighs your whole
six** — **Charizard**, **Snorlax**, **Lapras**, **Alakazam**, **Tauros** and **Dragonite** put
together — and eight is nothing, you have caught eight before **Mt. Moon**. And the boxes run out at 240
long before anything else gives way, so the real question was never "is the pile bigger than the
six". It was "how many more **Caterpie** can I keep", and only the pile moves that number.

## Three ways to write less down, in increasing order of loss

```
   1. DROP WHAT YOU CAN WORK OUT AGAIN                     nothing is lost
      A boxed Pokémon's record is 33 B; a party one is 44.
      The missing 11 B are the LEVEL and the five computed
      stats — and the game recomputes all six from the
      species, the potential and the stat experience the
      moment you withdraw it. Storing them would be
      storing an answer you can always redo.  → 228

   2. WRITE EVERY ONE DOWN, IN LESS DETAIL                 lossy, evenly
      The Hall of Fame's 16 B: species, level, name. The
      potential, the stat experience, the moves, the item,
      the Original Trainer — gone, and gone for good. You
      cannot get the Pokémon back out of that entry.

   3. KEEP FEWER OF THEM                                   lossy, unevenly
      Fifty teams and no more. Twelve boxes and no more.
      Release a Pokémon and it is not written down worse,
      it is not written down. And two Trainers who caught
      the same things no longer have the same boxes, so
      nothing either of them learned transfers to the other.
```

The order is the point. Most people jump straight to (2) and never notice that (1) was already
done for them by whoever built the game, or that (3) is a different kind of promise — (2) makes
every record a little worse, (3) makes some records not exist.

## Some fields tolerate rounding and some never do

This is what separates a Trainer who has actually filled a storage system from one who has read
about it.

```
                    THE POTENTIAL                 THE CURRENT HP
   ───────────────────────────────────────────────────────────────────
   how it is used   multiplied by the level       read as itself, once
                    inside the stat formula
   an error there   grows with the level — the    washes out — a Pokémon
                    same wrong nibble costs one   Center or a Full Restore
                    point at Lv. 20 and five at   sets it right on the way
                    Lv. 100                       past
   where it sits    the SAME two bytes, the       different for every
                    same four nibbles, in every   Pokémon and every moment
                    record ever written
   so measure it    down the COLUMN — which       one record at a time,
                    fights you, because you       which is the natural way,
                    catch them ONE AT A TIME      done as you catch them
                    and the column is not
                    finished until the journey is
   ───────────────────────────────────────────────────────────────────
   the sensible budget:  potential in full, current HP rounded. Not both.
```

That column problem is real and it is the whole difficulty. To rule the Attack-potential column
finely you would have to have already seen every **Pidgey**, **Zubat** and **Dratini** you are
ever going to catch — and you are on **Route 3** with four of them and a **Rattata**. So the
practical answer is to keep the awkward field exact and be coarse about the easy one, which is
exactly what a **Pokémon Center** lets you get away with: **Nurse Joy** restores HP, so an
approximate HP on a **Zubat** costs you nothing by the next town.

Two details that bite. **Writing down how you rounded costs bytes too** — a note on every single
boxed **Pidgey** saying which ruler you used is itself a pile, and at the coarsest settings those
notes are a real fraction of what you saved. And **the ends of the journey are not like the
middle**: **Charizard** and the **Dratini** you caught ten seconds ago in the **Safari Zone** get
looked at constantly, so they stay in full. Only the settled middle of box four — twenty
**Rattata** nobody has looked at since **Cerulean City** — gets trimmed.

## What breaks, and why your test will not find it

Trimming the pile never makes you forget *which* Pokémon is which — a **Nidoking** is still a
**Nidoking**. What it breaks is every question needing an exact number from a long way back: the
**Nidoking** you caught before the **Cascade Badge** and want the potential of now, the long chain
of arithmetic where one early figure has to survive to the **Elite Four**, anything where you must
quote rather than remember the gist.

And it gets **worse the longer the journey**. Which produces the trap: you trimmed the records,
tested with two boxes filled somewhere around **Vermilion City**, saw nothing wrong, carried on.
The failure is waiting in box eleven beside the **Dratini**, and your test never went past box
two. **Test the trimming at the number you will have caught by Victory Road**, not at the number
you happened to have when you started testing ([267](267-evaluating-a-quantised-model.md)).

## What a Gym Leader is listening for

* At how many caught does trimming the pile beat trimming the team? Do the division out loud.
* Why does the potential need more care than the current HP — give both reasons.
* Why does ruling a column fight against catching them one at a time?
* When would you release instead of trimming, and what do you lose that never comes back?

## Where this stands, September 2026

Every byte count here is from **Kanto**'s own code, which I read: 44 for a party record, 33 for a
boxed one, 11 each for the nickname and the **Original Trainer**'s name, 16 for a **Hall of Fame**
entry, 20 to a box, 12 boxes, and room for exactly 50 teams. The 11-byte difference between the
two records really is the level and the five computed stats, and the game really does work them
out again on withdrawal rather than carrying them around. Later generations changed every one of
those numbers and none of the reasoning: the team is a cost you pay once, the pile is a cost you
pay per Pokémon, and dividing one by the other tells you when the bill flips. That number has been
getting smaller every generation, because the boxes keep getting bigger and the team is still six.
