---
id: "074"
slug: vanishing-exploding-gradients
style: pokemon
category: deep-learning
difficulty: core
question: "What are vanishing and exploding gradients, and how are they fixed?"
tags: [vanishing-gradients, exploding-gradients, clipping, initialisation, lstm]
---

# When the Champion's feedback never reaches Route 1

The Champion's advice has to travel back down the League — Elite Four, then Gym 8, Gym 7, all the way
to the tutor on Route 1 who first taught your Charmander to Scratch.

Every stop **passes the message on.** And nobody passes it on perfectly.

## 🔇 Vanishing: the message fades

Each stop relays it at 80% strength. Sounds fine!

```
   Champion:  "YOUR STARTER'S EARLY MOVES ARE THE PROBLEM"  📣
   Gym 8:     "your starter's early moves are the problem"  🗣️
   Gym 6:     "starter's moves...problem"                   💬
   Gym 4:     "something about...moves?"                    🤏
   Gym 2:     "...mumble..."                                 ·
   Route 1:   silence.                                       ⬜

   0.8 relayed 50 times = 0.000014.  Nothing arrives.
```

Your Route 1 tutor **never learns anything.** They keep teaching Scratch exactly as they always have,
and your entire team is built on that foundation.

📌 **The nasty part: this looks like it's working.** Your team does improve — the last few Gyms are
getting the message loud and clear. It just improves **far less than it should**, and nothing in your
dashboard tells you why.

## 💥 Exploding: the message amplifies

Each stop adds a little emphasis. 120%.

```
   Champion:  "your starter could be a bit stronger"     🗣️
   Gym 8:     "your starter should be stronger"          📣
   Gym 6:     "YOUR STARTER IS WEAK"                     📢
   Gym 4:     "YOUR STARTER IS A DISASTER"               🚨
   Route 1:   "BURN EVERYTHING AND START AGAIN"          💥

   1.2 relayed 50 times = 9,100×.
```

Your Route 1 tutor panics and rebuilds from scratch. Your team is destroyed in one afternoon.

**This one is at least obvious.** Everything visibly breaks. The fading version quietly wastes months.

## The old problem 📉

For a long time, every relay in the League **whispered by design** — the best any of them could
manage was passing on a quarter of what they heard. Ten stops and the message was one in a million.

This is why nobody could run a League with more than a handful of Gyms. Not a lack of ideas — the
message physically couldn't reach the bottom.

## The fixes 🛠️

**1. 🗣️ Relays that pass the message on at full volume.** Change who's doing the relaying so the
message arrives at 100%, not 25%. **The single biggest fix** — it's what made deep Leagues possible
at all. (Its own quirk: a relay can go permanently silent if it stops hearing anything, which is why
modern relays always pass on at least a little.)

**2. 🛣️ Build a direct road.** Don't relay at all — run a **clean corridor** from the Champion to
Route 1 that bypasses every Gym. The message arrives **at full volume, guaranteed**, no matter what
the Gyms do.

This is the structural fix, and it's why a hundred-Gym League works.

**3. ⚖️ Keep everything on the same scale** so no Gym is shouting or whispering relative to its
neighbours.

**4. 🎚️ Set the volume correctly on day one.** Get the initial levels wrong and the message is
already fading or amplifying **before you've trained anything.** There's a specific right answer for
each kind of relay, and using the wrong one dooms the run from step zero.

**5. 🔊 Cap the volume.**

The standard fix for the exploding case. If the message exceeds a set volume, **turn the whole thing
down proportionally.**

📌 Crucially: turn *everything* down together, not each word individually. The message says *"more
Speed, less Attack, slightly more Defence"* — you want that **balance** preserved, just quieter.
Clip each word separately and you'd distort the advice itself.

Essentially every serious training run does this.

## How to actually catch it 🔍

**Log the message volume at every Gym.**

* 📉 Volumes decaying by orders of magnitude toward Route 1 → **fading.**
* 📈 Sudden spikes right before everything breaks → **exploding.**

One line of instrumentation. Diagnoses both instantly. **Almost nobody has it in their training
script**, and then spends a week guessing.
