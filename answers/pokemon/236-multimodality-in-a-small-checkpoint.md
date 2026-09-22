---
id: "236"
slug: multimodality-in-a-small-checkpoint
style: pokemon
category: open-weights
difficulty: advanced
question: "What has to give when you put vision and audio into a checkpoint that has to fit on one card?"
tags: [multimodal, vision-encoder, token-budget, on-device, gemma]
---

# The entry fee is 500. What it actually costs you is every Pokémon you own

Walking into the **Safari Zone** at **Fuchsia City** gets you **Kangaskhan**, **Tauros**,
**Chansey**, **Scyther**, **Pinsir** and a **Dratini** out of the pond — species you will not meet
in the tall grass anywhere else in **Kanto**. The fee is ¥500, which is nothing. What you actually
hand over at the gate is your whole team: inside, you cannot send out a single Pokémon. The menu
is BALL, BAIT, ROCK, RUN, and nothing else. You are handed thirty **Safari Ball**s and a counter
that starts at **500 steps**, and when it reaches zero you are escorted out whether or not you got
what you came for.

Bolting a camera onto a small model is that gate. The parts cost about 1–3% of the model, which
is the ¥500. What it actually costs is **steps** — and in an architecture where five layers in
six are only allowed to walk 512 of them, one picture at the standard budget spends more than
half the walk.

## The numbers, off the published definitions

From `gemma/gm/nn/gemma4/` in `google-deepmind/gemma`:

```
   what is at the gate

     E2B / E4B camera   width 768, 16 layers, 12 heads, FFW 3,072    ≈ 0.11 B
     31B / 26B-A4B      width 1,152, 27 layers, 16 heads, FFW 4,304  ≈ 0.41 B
     E2B / E4B rod      12 layers, width 1,024, 13 behind, 0 ahead
     31B / 26B-A4B      — no rod in the bag at all —

     the camera as a share of what you already own:
        E4B  0.11 / 4.67 = 2.4%        31B  0.41 / 30.7 = 1.3%      the ¥500

   what a single encounter costs

     one picture (any shape)
       │  16-pixel patches
       ▼
     up to 2,520 sightings ──────── padded to 2,520 whatever you actually met
       │  nine sightings collapse into one step
       ▼
     280 steps of the walk   ← the standard issue; 70 / 140 / 280 / 560 / 1,120
       │
       ▼
     mixed into the rest of the walk

   280 measured against each budget

     against the full 131,072-step journey :  0.21%    ~468 pictures would fill it
     against E4B's 512-step window         : 54.7%     █████████████·············
     against the 31B's 1,024-step window   : 27.3%     ███████···················

     at the 560 issue on E4B, and 1,120 on the 31B, ONE PICTURE IS LONGER THAN
     THE WHOLE WALK. No sliding layer ever sees the whole of it.
```

## What gives, in the order it hurts

**1. Detail, before anyone gets a look.** Nine sightings collapse into one step. Eight ninths of
what the camera saw is pooled away between the gate and the walk — which is why small text, dense
tables and fine chart labels are the first things to go, and why the step count is a dial you can
turn up when the job is *reading* and down when the job is *describing*. It is **Bait and Rock**
in one decision: a Rock makes the catch easier and the flee likelier, more steps buy detail and
spend the walk.

**2. The walk, which is the expensive one.** The standard 280 eats 55% of every sliding layer's
entire 512 steps on E4B. Two pictures and the text around them is gone from those layers
altogether; anything that ties the two pictures together has to travel through the seven layers
that remember the whole journey, which question 234 already identified as the lossy road.
Multimodality and the sliding window are two separately sensible decisions that ruin each other,
and neither description mentions the other.

**3. A step is a step.** A public engineering report on one serving stack measures the gate at a
flat price: every picture is padded out to the full 2,520 sightings, so a 192-pixel thumbnail and
a 768-pixel photograph cost exactly the same — 3.7× the 144-sighting case — and trimming to a
576-sighting ladder would give back about 3.5× on the small ones. Walking past a **Magikarp**
costs the same step as walking past a **Kangaskhan**. On a phone, a per-picture toll you cannot
dodge by sending something smaller is a product decision, not a tuning knob.

**4. Which direction you are allowed to walk, and it differs by size.** In the 31B and 26B-A4B
configs the picture's own steps may look at each other in both directions inside the sliding
layers, staying one-way in the layers that remember everything. E2B and E4B are one-way
everywhere. The **Safari Zone**'s areas connect in every direction and you wander them as you
like; **Route 1** you walk north. A picture has no reading order, so forcing one on it is a real
handicap, and the two smallest checkpoints wear it. The small one does not get a smaller version
of the big one's deal. It gets a different deal.

**5. The steps you did not spend on Victory Road.** This one is in no config and it is the one
that matters most. Every step spent learning pictures is a step not spent on words, and in a
4.5B-effective model there is no slack in the counter. You cannot read this off the gate. You read
it off a comparison the **Warden** may never have published.

## The inversion worth noticing

The rod is in `Gemma4_E2B` and `Gemma4_E4B` and **not** in `Gemma4_31B` or `Gemma4_26B_A4B`. The
ladder does not run smallest to largest; it runs by where you are standing when you use it. The
rod has thirteen behind it and **nothing** ahead — you cast, and you take what comes, with no
peeking at what is further out — which is exactly the shape you want for something listening in
real time on a device in a pocket. The **Super Rod** is not in the big bags because the big bags
are not standing by the water. Anyone choosing a checkpoint by "bigger catches more" has just
walked past **Dratini**.

## What a Gym Leader is listening for

That your first question is "how many steps per picture", not "how big is the camera". Then that
you hold that number up against the **512-step window** rather than the 131,072-step journey —
that is the step that separates someone who has run one from someone who has read about one. The
strongest answers raise the steps-not-spent-on-**Victory Road** cost unprompted and admit it is
the hardest of the five to check.

## Where this stands, September 2026

The camera dimensions, the 16-pixel patches, the nine-into-one pooling, the 280 standard issue,
the one-way-or-both-ways settings, the rod's thirteen-behind-and-nothing-ahead, and which
checkpoints carry a rod at all were read first-hand from `google-deepmind/gemma` — **primary**.
The parameter estimates and the percentages are mine, not quotes. The 70 / 140 / 280 / 560 / 1,120
ladder is **coverage**, though the 2,520 it implies is confirmed independently by the serving
report. The 3.7× figures come from one public thread on one machine, read first-hand: one team's
measurement, not a general law. The model cards and the documentation are the authority and both
are behind an egress block here. Step counts and pooling factors will move; **Kangaskhan** has
been Safari-only in **Kanto** since 1996, and steps-against-the-window is the part that transfers.
