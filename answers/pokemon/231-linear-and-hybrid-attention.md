---
id: "231"
slug: linear-and-hybrid-attention
style: pokemon
category: open-weights
difficulty: advanced
question: "Linear and hybrid attention promise to kill the quadratic term. What do they actually give up?"
tags: [linear-attention, hybrid, minimax, long-context, sparse-attention]
---

# Stop keeping the tape. Keep the slate. It never gets any bigger — and it never gets any bigger.

A full recording compares this turn against every turn that has happened. A **slate** does not.
The slate says **+6 Attack**, **Sandstorm** for three more turns — five is the normal count, eight
if somebody is holding a **Smooth Rock** — **Light Screen** and **Reflect** for two more, eight
had there been a **Light Clay**, **Electric Terrain** on the floor, **Stealth Rock** up,
**Spikes** at two layers of a possible three. And that is the whole of it, at turn five or turn
five thousand. It never grows, which is the entire appeal, and it cannot be interrogated, which is
the entire price.

Hybrids exist because that trade is unbearable at 100% and perfectly comfortable at 25%.

## The arithmetic, on one stand

Take a stand of 64 tiers, 8 recorders to a tier, 128 entries a reading, the ordinary arrangement
from [228](228-attention-variants-and-kv-arithmetic.md). Now let the battle run to a million
turns.

```
   a tier that keeps the tape
        per turn = 2 · 8 · 128 · 2                      =       4,096 pg
        × 64 tiers                                      =     262,144 pg per turn
        at a million turns                              =         262 crates
        setting the whole thing up costs  ∝  turns²     ← the part that hurts

   a tier that keeps the slate (32 readers · 128 · 128, four pages an entry)
        slate per tier                                  =   2,097,152 pg
        × 48 tiers                                      =     101 million pg
        …and that number does not move when the battle does.
        each turn costs the same whether it is turn 9 or turn 900,000

   crossover:   4,096 · turns  =  2,097,152   →   turns ≈ 512
                past turn 512 the slate is smaller than the tape
```

Put them together three slates to every tape — the schedule Qwen and Moonshot both settled on —
and:

```
   16 tiers on tape × 4,096 pg = 65,536 pg a turn   → 65.5 crates at a million
   48 tiers on the slate, fixed                     →  0.1 crates, ever
   ──────────────────────────────────────────────────────────────────────────
   total ≈ 65.6 crates   against 262 for all-tape   →  4.0× less
```

That 4× is the schedule and nothing else. Keep one tier in eight on tape — what MiniMax first
shipped — and you get 8×. You cannot reach 20× this way without going to one in twenty, and that
is the point where the stand stops being able to see.

## What the slate actually gives up

The slate is one surface that everything writes onto, and reading it back is a guess, not a
lookup. Three things go wrong, in this order:

1. **It saturates, and it saturates fast.** **Swords Dance** raises Attack two stages. One use is
   ×2, two is ×3, three is ×4 — and the fourth does nothing at all, because **+6 is the ceiling**
   and the game says so. **Nasty Plot**, **Calm Mind** and **Dragon Dance** all hit the same wall.
   A fixed slate has a fixed ceiling, and no amount of training raises it.
2. **It cannot tell you *which*.** The slate reads +2 Attack. It cannot tell you whether that was
   a single **Swords Dance**, or two Swords Dances answered by two **Intimidate** switch-ins, or
   three Swords Dances against four of them — all three land on exactly +2, and the slate keeps
   only the +2. It cannot tell you who did it, or in what order. For one fact that barely matters.
   For a chain of three facts held
   at once — which one is holding the **Choice Scarf**, whether **Mimikyu**'s **Disguise** has
   already been broken, which one the **Toxic Spikes** landed on — it matters enormously, and that
   is the failure people actually hit. Finding one thing is easy. Holding three precise things at
   once is the job.
3. **You cannot rejoin.** **Baton Pass** hands over the stat stages and only the stat stages; the
   incoming **Ninjask** inherits a +6 and no idea how it got there. And a single **Haze** wipes
   every stage on the field to zero with nothing to rebuild from, because nobody kept the tape.
   Coming back to a battle in the middle is a thing you can do with a recording and cannot do with
   a slate.

**Clear Smog**, per-stat gating, deliberate forgetting — every improvement in this area is an
attempt to make the slate forget *on purpose* instead of by smudging. They help. None of them
makes it bigger.

## The field argued about this in public, which is the useful part

```
   MiniMax-01   Jan 2025   7 slates : 1 tape              the bet
   MiniMax-M1   2025       kept it                        the bet, scaled up
   MiniMax-M2   2025/26    tape on every tier             the retraction
   MiniMax-M3   Jun 2026   tape, but only the blocks
                           worth reading                  a different bet
        ──────────────────────────────────────────────────────────────────
   Qwen3-Next / Qwen3.5    3 slates : 1 tape              stayed hybrid
   Kimi Linear / K3        about 3 : 1                    stayed hybrid
   DeepSeek-V3.2           tape, top 2,048 turns only     went selective
   Llama 4 Scout           one tier in four sees all of
                           it, the rest see 8,192 turns   a third arrangement
```

MiniMax wrote down why they went back, and it is the most useful paragraph in this whole area: no
cheaper arrangement reliably matched the full tape across reasoning, coding and long errands; the
hybrid looked equal in short exhibition battles and showed clear gaps, at scale, on exactly the
multi-step reads described above. That is failure number two, found by the Trainer who had
shipped the alternative twice.

Then M3 came back with something different. It does **not** keep a slate. It keeps the real tape,
cuts it into blocks, has a cheap reader score which blocks matter for this turn, and then watches
those blocks properly — like checking the three exchanges where **Cynthia**'s **Garchomp**
actually came in and ate the **Ice Beam**, rather than re-watching the whole **Battle Tower** run.
Reported: level with the ordinary
arrangement on a 109-billion build, attention work per turn down 28.4× at a million turns, and
14.2× faster to set up and 7.6× faster to play out. M3 itself is reported at 428 registered, about
23 on the field, a million turns, under MiniMax's own community terms.

So the 2026 shape is: **the flagships kept the tape and got choosier about it; the hybrids kept
slates as a floor, not as the whole stand.** Choosing which blocks to watch still leaves exact
recall available for the blocks you chose. A slate leaves it available for nothing.

## Telling whether it lands for you

* Find out how long your battles actually run. A **Blissey** and a **Shuckle** can stall for
  hundreds of turns; a **Choice Band** team is over in six. Under a few thousand turns none of
  this matters and the slate's own overhead makes it *slower*.
* Test it on holding three facts at once over your own record — not on a single **Rare Candy**
  hidden in a cave. The gap only shows where several precise things must be live together.
* Check your own **Battle Maison** supports slates and mid-battle resumption at the version you
  are actually on, not in principle.
* Time setting up and playing out separately. Slates help both; choosing blocks mostly helps the
  setting up, until the choosing is cheap on every turn too.

## Where this stands, September 2026

The names will go stale fastest, the ratios next, the mechanism not at all. MiniMax's own
retraction notice, the block-selection write-up and the Qwen and Moonshot paperwork are the
authorities, and I could reach none of them from here — every figure above about M1, M2, M3, Qwen
and Kimi came from write-ups, so check before you quote. What transfers: a slate buys you a cost
that never grows and charges you the ability to look anything up; choosing blocks buys you a cost
that grows slowly and charges you whatever you did not choose. Different bills. Know which one you
are paying.

## What a Gym Leader is listening for

* Why does holding three facts break before finding one does?
* What does a slate do to your ability to come back to a battle halfway through?
* Why is choosing which blocks to watch not the same thing as keeping a slate?
