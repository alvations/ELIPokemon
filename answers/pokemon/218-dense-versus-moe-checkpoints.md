---
id: "218"
slug: dense-versus-moe-checkpoints
style: pokemon
category: open-weights
difficulty: advanced
question: "Qwen ships a dense 27B checkpoint and a 35B-A3B mixture-of-experts checkpoint in the same generation. When is the dense one the right answer?"
tags: [qwen, mixture-of-experts, dense-models, quantisation, fine-tuning]
---

# Starmie and Aegislash both total 520. Only one of them spends it all every turn

**Starmie** has base stats 60 / 75 / 85 / 100 / 85 / 115. **Aegislash** in Shield Forme has
60 / 50 / 150 / 50 / 150 / 60, and in Blade Forme those numbers swap sides to
60 / 150 / 50 / 150 / 50 / 60. Add either one up and you get **520**. Exactly the same total.

They are not the same Pokémon. Starmie's 520 is all live, all the time. Aegislash's 520 is a
**router**: its ability **Stance Change** flips it into Blade Forme the moment it picks a
damaging move and back to Shield Forme only when it picks **King's Shield**. Whichever half is
facing the wrong way that turn is 200-odd points of dead weight — carried in the same Poké Ball,
paid for in the same team slot, doing nothing.

Alibaba's Qwen line is the cleanest thing to reason about this with, because it ships both shapes
in the same generation, days apart. From the team's own repository: **Qwen3.5-122B-A10B,
Qwen3.5-35B-A3B and Qwen3.5-27B on 2026-02-24**. Then **35B-A3B on 2026-04-16 and a dense 27B on
2026-04-22**. Then **2.4T-A95B on 2026-08-12 and a dense 27B on 2026-08-14**. Three times, both
shapes, two days apart.

So you can hold "35B" against "27B" and ask which is bigger, and the question is broken. **`A3B`
is the Blade Forme number** — what is actually swinging this turn. The rest is what you carry.

## The arithmetic, laid out

```
   what you field               total     live this turn    what it weighs    top Speed
   ──────────────────────────   ───────   ───────────────   ───────────────   ─────────
   Starmie                       520 BST    all 520           one Ball           115
   Aegislash                     520 BST    about half        one Ball            60

   Qwen3.5-27B    (Starmie)       27 B       27 B             ~54 GB            fast
   Qwen3.5-35B-A3B (Aegislash)    35 B        3 B             ~70 GB            depends
   Qwen3.5-397B-A17B             397 B       17 B            ~794 GB            depends
   Qwen3.8-2.4T-A95B             2.4 T       95 B             ~4.8 TB           depends

   ┌─ what actually binds ────────────────────────────────────────────────┐
   │  one Poké Ball     │  both 520s fit. The team slot is not the        │
   │                    │  deciding factor at this size.                  │
   │  a Route 1 battle  │  both fine.                                     │
   │  a Power Spot      │  Dynamax only works where the venue supplies    │
   │                    │  one. The 2.4T is that: reported at ~2,325 GiB  │
   │                    │  in its light build, sixteen cards across four  │
   │                    │  trays. It is not coming to your Gym.           │
   └──────────────────────────────────────────────────────────────────────┘

   Same week. Two days apart. One goes in a bag; one needs the stadium.
```

Qwen3.8-27B and Qwen3.8-2.4T-A95B came out of the same announcement. "Qwen3.8 is open" is true of
both and tells you nothing about whether you can field it.

## Five reasons to bring Starmie

1. **Every point does honest work.** Starmie's 100 Special Attack is behind **Surf**, **Ice
   Beam**, **Thunderbolt** and **Psychic** on every single turn. Aegislash's 150 is only there on
   the turns Stance Change guessed right. Qwen's own announcement for the dense 27B claims it
   out-battled a model fifteen times its total on every coding ladder — SWE-bench Verified
   **77.2 vs 76.2**, SWE-bench Pro **53.5 vs 50.9**, Terminal-Bench 2.0 **59.3 vs 52.5**,
   SkillsBench **48.2 vs 30.0**. Those are the trainer's own numbers about his own Pokémon, so
   read them as a claim (question 212).
2. **Training it is a known route.** **Protein**, **Calcium** and **Carbos** put EVs into a named
   stat and you can see the number move. With Aegislash you never quite know which forme the
   investment is serving, and the forme you stop entering rots: Stance Change only sends it back
   to Shield when it uses King's Shield, so a Pokémon that has attacked forty turns running has a
   defensive half nobody has looked at since the **Pokémon Center**.
3. **Cutting it down cuts evenly.** Trim Starmie and it loses a little of everything. Trim
   Aegislash and you trim the half you were not watching — and nothing the opponent does puts it
   back, because only King's Shield does that. So a Blade Forme Aegislash meets **Earthquake** on
   **50** Defence, at double damage into its Steel half, and that is when you find out. Stat
   stages cap at ±6 for both; the difference is whether the half taking the hit was ever tested.
4. **One on one, the flat one moves first.** Base 115 against base 60 is not close, and getting
   back into Shield Forme costs Aegislash the King's Shield turn to do it. A single opponent
   gives you nothing to group and no saving to collect.
5. **There is less to run.** No forme to track, no King's Shield in the budget, and **Natural
   Cure** clears status the moment Starmie switches out. Nothing to monitor.

## When Aegislash is right

When the **Battle Tower** streak is long and the opponents are many. Across a whole ladder the
specialisation pays: 150 on whichever side this opponent attacks from beats 100 and 85 on both.
And coverage against the entire **Type Chart** is a total-points claim, not a per-turn one — the
same way Qwen3.5's claim of 201 languages is a claim about everything it carries, not about what
fires.

## What a Gym Leader is listening for

That you refuse the comparison as asked and split it into "what does it weigh" and "what does it
swing" before answering. Then that you name the thing that actually binds — one Ball, a training
plan, a Speed tier — instead of reciting totals. The strongest answers notice that at 520 the
argument is about **upkeep and training**, and at the 2.4T end it is entirely about **the venue**,
and that using the first argument at the second scale is the real mistake.

## Where this stands, September 2026

The release dates and the total/live splits come from the Qwen team's own repository, read
directly. The weights in gigabytes are arithmetic. The four benchmark scores are the vendor's
own, relayed through coverage because the release blog and the model card are both behind an
egress block here — those two pages are the authority and should be read before anyone quotes
them. Re-check the roster every quarter. Starmie and Aegislash will still total 520.
