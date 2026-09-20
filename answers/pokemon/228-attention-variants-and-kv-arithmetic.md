---
id: "228"
slug: attention-variants-and-kv-arithmetic
style: pokemon
category: open-weights
difficulty: advanced
question: "Walk me through MHA, MQA, GQA and multi-head latent attention with real shapes. What does each one actually divide?"
tags: [attention, kv-cache, gqa, mla, deepseek]
---

# Everyone in the stands brought a Vs. Recorder. That is the whole problem.

Picture the stand above the field: **126 tiers**, and **128 Trainers to a tier**, each one
watching for a different thing. One is watching for **Stealth Rock** going up. One is watching
whether **Cynthia**'s **Garchomp** has taken an **Ice Beam** yet. One is counting how much
**Draco Meteor** has left. One is watching the **Leftovers** tick. Every tier watches the tier
below it and passes its reading upward.

They all need the past. The only question — the whole question — is **how many separate
recordings of that past the tier has to keep**.

```
   pages kept per turn per tier  =  2  ×  recorders  ×  128 entries  ×  2 pages
                                    ▲        ▲              ▲             ▲
                               what was   the only     how wide a    how thick
                               used, and  thing that   reading is    the paper is
                               what it    changes
                               did
```

## One stand, four ways to film it

```
                   recorders   per tier, per turn          × 126 tiers          ratio
   ──────────────────────────────────────────────────────────────────────────────────
   one each            128     2·128·128·2 = 65,536 pg   8,257,536 pg = 8.26 M    1×
   eight to a tier       8     2·  8·128·2 =  4,096 pg     516,096 pg =  516 K   16×
   one to a tier         1     2·  1·128·2 =    512 pg      64,512 pg = 64.5 K  128×
   ──────────────────────────────────────────────────────────────────────────────────

   the Battle Video   (61 tiers instead of 126)

                       512 entries of replay code + 64 entries of turn order = 576
                       2 pages each  →   1,152 pg per tier per turn
                       × 61 tiers    →     70,272 pg
```

**One recorder each** is the honest, expensive way. Nobody shares, every Trainer keeps a complete
personal record, and the stand drowns in paper.

**One to a tier** is the **Vs. Recorder** on the railing that everybody crowds around. It divides
by 128 and it is the only one of the four that visibly costs you something: 128 Trainers reading
one tape start seeing the same battle, and the one who was counting **Draco Meteor** stops
noticing **Draco Meteor** at all.

**Eight to a tier** — sixteen Trainers to a recorder — is the arrangement almost every stand
actually uses. 16× less paper, and the Trainers in a group are close enough in what they want
that a shared tape still serves them. If you started with one each, you can re-seat everyone into
eights and re-train them in about a twentieth of the time it took to train them the first time.

**The Battle Video** is the clever one, and it is not "even more sharing". A Battle Video is not
footage. It is a short record the game **replays the battle from** — you keep the code, not the
pictures, and you regenerate whatever view a Trainer asks for when they ask for it. 512 entries
of code, and the regeneration folds into the asking, so nobody ever writes out the full picture.

The 64 extra entries are the part people skip, and they are the whole craft:

```
   what the Battle Video keeps

        [ replay code : 512 ]      [ turn order : 64 ]    ← one copy for all 128 Trainers
                  │                         │
       folds into the asking ───┘            └─── has to be kept as-is
                  ▼
        reading it costs like one very wide recorder, not 128 narrow ones

        paper  ↓ 57× against one-each   work per turn ↑
        (65,536 pg → 1,152 pg a tier)   (one very wide reading)
```

You cannot fold **turn order** into the code, because turn order is not a summary — it is the
thing that decides the battle. **Fake Out** moves at +3 and only on the turn it comes out.
**Extreme Speed** moves at +2. **Quick Attack** and **Sucker Punch** move at +1. **Regieleki**
has the highest base Speed in the game at 200 and still eats the **Fake Out** first.
**Trick Room** turns the ordering upside down inside every one of those brackets for five turns,
a **Choice Scarf** multiplies Speed by 1.5 and locks you into the move you picked, and a genuine
Speed tie is settled by a coin flip. A record that compressed away *when* would be a record of a
different battle. So those 64 entries ride along uncompressed, and that is why the number is 576
and not 512.

## What the paper saving actually buys

Paper is not the point. **How many battles the Battle Tower can run at once** is the point.

```
   The record room holds 640 crates. The registered team's own paperwork takes 405.
   Left for the recordings: ~235 crates, at a billion pages a crate.

                per turn       turns that fit       a 32,768-turn streak
   ────────────────────────────────────────────────────────────────────────
   one each      8.26 M pg        ~28,400             0.9 streaks   ← not a Tower
   eight/tier     516 K pg       ~455,000            13.9 streaks
   one/tier      64.5 K pg     ~3,640,000             111 streaks
   ────────────────────────────────────────────────────────────────────────

   The same 235 crates. The only thing that changed was the number of recorders.
```

And note what did **not** change. All 128 Trainers still have to watch. Sharing a recorder means
fewer tapes, not fewer eyes — so if your battles are long to set up and short to finish, this
buys you more battles at once and almost nothing on the clock of any one of them.

## Where this stands, September 2026

The tier counts and widths will change with the next stand that gets built; the counting will
not. The 61-tier, 576-entry figures are from the builder's own posted plans, which I read
directly; the crate totals are from the write-ups, because the notice board itself was behind a
gate I could not get through — check the plans before you quote them. Everything newer —
picking which turns are even worth consulting, or carrying a running slate instead of a record
([231](231-linear-and-hybrid-attention.md)) — changes *which* turns you keep. It does not change
this sum for the ones you do.

## What a Gym Leader is listening for

* Why can turn order not be folded into the replay code, and what are those 64 entries?
* Does sharing recorders make the opening any faster? (No. Say why.)
* When would you still put one recorder on the whole tier?
