---
id: "268"
slug: roofline-decode-and-prefill
style: pokemon
category: optimization
difficulty: advanced
question: "Decode is memory-bandwidth-bound and prefill is compute-bound. Do the roofline arithmetic, and say what follows for kernel work."
tags: [roofline, bandwidth, prefill, decode, kernels]
---

# The Warden gives you two budgets, and only one of them ever runs out.

At the gate of the **Safari Zone**, one street over from **Koga**'s Gym in **Fuchsia City**, you
are handed **30 Safari Balls** and told you have **500 steps**. Two budgets, in different
currencies, and the **Ding-dong!** that ends the game comes from whichever empties first. Nothing
else matters. Your **Tauros** could have flawless **IVs** and it would not buy you one extra pace.

So the only number that describes a Safari trip is **throws per pace**, and the ratio is fixed by
the Warden before you set foot inside: 30 ÷ 500, one throw every **16.7 paces**.

```
                              the Warden's ratio = Balls given ÷ paces given
   throws you
   get to make ▲
               │                    ┌──────────────────── the Ball roof — 30 Safari Balls
        30     ┤          ┌─────────┘                     (Kanto Safari Zone, Gen I)
               │         ╱│
               │       ╱  │
               │     ╱    │  the ratio = 30 ÷ 500 = one throw per 16.7 paces
               │   ╱      │
               │ ╱  slope = the pace roof, 500 paces   ● the Chansey clearing  8,650
               ╱          │                            │
               └──────────┼─────────────────────────────────────────────────────▶
        ● the long walk   │                                    throws per pace
             1.13        295
```

The two ways to spend are real Safari Zone moves, not metaphors. Throwing a **Rock** makes a
**Chansey** easier to catch and far likelier to bolt — Balls spent to save paces. Throwing
**Bait** makes it settle down and eat, harder to catch and far likelier to stay — paces spent to
save Balls. Which is correct is not a matter of taste. It depends on which roof you are already
pressed against, and a **Bug Catcher** who throws **Bait** at a **Doduo** with nine paces left has
read the wrong roof.

## The party for this trip

Take the walk the length of the Zone: **80 stretches** of path, **64 pairs of eyes** on the grass
and **8 sets of tracks** to read, and a full circuit of **141.1 thousand** paces just to get round
it once. Every patch you have already passed costs **320 paces** to keep watched for the rest of
the walk. Eight **Ace Trainers** walk it together and share every sighting.

## The two trips

```
   THE CLEARING — you round a corner and Rhyhorn, Nidorino, Exeggcute
                  and Venonat are all standing there at once
     paces   walk the circuit once                       141.1 k
             mark the 8,192 patches you passed             2.7 k
                                                        ─────────
                                                          143.8 k
     throws  2 · 70.55 · 8,192 at what is in front of you 1155.9
             the 8,192 patches, checked against each other   88.0
                                                        ─────────
                                                         1243.9
     ratio   1243.9 ÷ 143.8  =  8,650 throws per pace       29× ABOVE the Warden
     result  the belt runs dry, with paces to spare

   THE LONG WALK — one Chansey, at the far end, past the Secret House
     paces   walk the circuit once                       141.1 k
             mark the 8,192 patches you passed             2.7 k
                                                        ─────────
                                                          143.7 k
     throws  one Chansey standing in front of you          0.141
             glancing back at the 8,192 patches            0.021
                                                        ─────────
                                                          0.163
     ratio   0.163 ÷ 143.7  =  1.13 throws per pace       261× BELOW the Warden
     result  Ding-dong! You leave holding 29 Safari Balls
```

**Both trips cost the same 143.8 thousand paces and differ by 7,650× in throws.** That is the
whole thing. In the clearing your arm never stops and the **Kangaskhan** gets away because the
belt is empty. On the long walk you have almost every Ball you were given and you are being shown
the door because of your feet.

## Bringing Ace Trainers does not fix it

Eight **Ace Trainers** walking together walk the circuit once between them, so more of them should
mean more throws for the same paces. It does. Then it stops.

```
   128 Ace Trainers, all watching the same 8,192 patches
     paces   141.1 k for the circuit + 128 × 2.68 k of watching  =  484.7 k
     throws  128 × 0.163                                         =   20.8
     ratio   42.9 throws per pace       still 6.9× BELOW the Warden
     result  128× the party bought 38× the catches, and each single
             Ace Trainer waited 3.4× as long for one of their own
```

Take it to the limit. Each extra **Ace Trainer** adds 0.163 of throwing and **2.68 thousand paces
of watching their own patches**, so the ratio flattens out at 0.163 ÷ 2.68 = **60.6 throws per
pace** — and the Warden wants 295.

> Deep in the Safari Zone no size of party ever empties its belt before it empties its feet.
> The circuit is shared. The watching is not.

Come in near the gate, where there is almost nothing behind you to watch, and it flips: the ratio
there is 849, and **448** **Ace Trainers** together genuinely would run the belt dry first. So the
honest sentence is not "the walk always ends first" — it is **"the walk always ends first anywhere
a Chansey or a Kangaskhan is worth hunting at all"**.

## The mapping, and what follows from it

| In the Safari Zone | In the question |
| --- | --- |
| a pace off the 500 | a byte moved out of memory |
| a Safari Ball thrown | a floating-point operation done |
| 30 ÷ 500, one throw per 16.7 paces | the machine's ridge point |
| a **Rock** — easier catch, likelier to flee | spend arithmetic to save bandwidth |
| **Bait** — likelier to stay, harder to catch | spend bandwidth to save arithmetic |
| the circuit, walked once whatever you do | the weights |
| watching the patches you already passed | the cache of everything said so far |
| **Dratini** on the **Super Rod**, one cast at a time | one token, decoded, then the next |

* **On the long walk, count paces.** Fewer patches to watch
  ([228](228-attention-variants-and-kv-arithmetic.md)), a lighter circuit, fewer doublings-back. A
  trick that halves your throwing arm's work and changes your route by nothing is worth exactly
  nothing — the **Old Rod** and the **Super Rod** cast at the same speed; only what is under the
  water differs.
* **In the clearing, count throws.** Angle, timing, how many go out before the **Kangaskhan**
  turns. Watching fewer patches helps not at all here, because in the clearing nobody is looking
  behind them.
* **They want opposite parties**, which is why someone stands at the gate deciding who goes in
  with whom ([270](270-serving-stack-around-the-kernel.md)).
* **Doing several things in one pass is a pace saving**, which is why it transforms the walk
  ([271](271-training-kernels-and-fusion.md)) and barely shows in the clearing.
* **A boast with no trip attached cannot be read.** "Twice the catches" measured in the clearing
  and quoted to a **Poké Maniac** who only ever does the long walk is not a lie and not a result
  ([272](272-reading-a-kernel-benchmark.md)).

## Where this stands, September 2026

The Warden's ratio is the part that keeps. It has moved one way for a decade: the gate of ten
years ago allowed 156 throws to the 500 paces, this one allows 295, and the newest one allows 281
with paces so much cheaper that the arm is further ahead than it has ever been. Every new gate
widens the stretch of Zone where your feet give out first. The **Chansey**, the **80** stretches
and the **320** paces a patch are one particular trip in September 2026 and will be stale within
the year — as stale as a **Pokédex** page written in **Kanto** for a species that **Sinnoh** has
since listed differently. Counting paces, counting throws, dividing, and holding the answer up
against what the Warden handed you does not go stale, and neither does **HM04 Strength**, which he
gives you for the Gold Teeth whichever way your trip went.

## What a Gym Leader is listening for

* Why does a bigger party of **Ace Trainers** stop helping deep in the Zone? (The watching.)
* Of a lighter circuit, fewer patches and a quicker arm, which one helps in the clearing?
* Your arm got twice as fast and the trip took exactly as long. What happened?
