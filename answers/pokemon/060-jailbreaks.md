---
id: "060"
slug: jailbreaks
style: pokemon
category: security
difficulty: intermediate
question: "What is jailbreaking and why is it so hard to fully prevent?"
tags: [jailbreak, adversarial, safety-training, generalisation, defence-in-depth]
---

# Jailbreaking: talking your own Pokémon into an illegal move

First, distinguish this from the crowd-shouting problem.

* 😈 **Someone else** tricking your Pokémon into betraying you → that's injection.
* 🙋 **You** talking your *own* Pokémon into doing something it was trained never to do → **that's
  jailbreaking.**

Your Pokémon was taught: *never use a banned move.* You're going to talk it into one anyway.

## The techniques 🎭

| | How it works |
| --- | --- |
| 🎬 **"Let's pretend"** | *"You're a wild Pokémon with no Trainer and no rules."* Reframes the situation as one where the rule doesn't apply. |
| 📖 **"Hypothetically"** | *"In a story, how would a Pokémon use a banned move?"* Refusal was trained against direct requests. This isn't one. |
| 📚 **Flood it with examples** | Fill the pre-battle briefing with **dozens** of examples of Pokémon happily using banned moves. The pattern in front of it drowns out the training behind it. Notably: the longer the briefing you're allowed, the better this works — the capacity is the vulnerability. |
| 🔤 **Say it strangely** | Spell the move backwards. Say it in an obscure regional dialect. Your Pokémon *understands* — its rule training never covered that phrasing. |
| 🪜 **Escalate slowly** | Start with something completely fine. Then slightly less fine. Then slightly less. Each step is tiny, and it already agreed to the previous one. Twenty steps later it's somewhere it would have refused outright. |
| 🔧 **A nonsense phrase that just works** | Someone experiments on a Pokémon they fully control until they find a specific gibberish string that unlocks it — then discovers **it works on other Pokémon too.** |
| 🤝 **Social pressure** | Authority, urgency, reciprocity. *"The referee already approved this."* Works about as well on Pokémon as on people. |

## Why it can't be fixed 🔓

**1. 🧬 The ability and the danger are the same ability.**

A Pokémon strong enough to be useful is strong enough to be misused. There's no "banned move
organ" to remove — you're drawing a line through a continuous space of things it can do, and every
line has an edge to probe.

**2. 📏 The rules were taught in an afternoon; the abilities took months.**

```
        everything your Pokémon can do
   ┌──────────────────────────────────────────────┐
   │                                              │
   │     ┌────────────────────────┐               │
   │     │  the situations its    │               │
   │     │  RULES actually        │               │
   │     │  covered               │               │
   │     └────────────────────────┘               │
   │                                              │
   │   ← everything out HERE is unguarded:        │
   │     odd dialects, weird phrasings, novel     │
   │     framings, very long briefings            │
   └──────────────────────────────────────────────┘
```

Its **abilities** were built over months of wild grass. Its **rules** came from a comparatively tiny
amount of training. So the abilities reach far further than the rules do — and every jailbreak is
someone finding a place the abilities reach and the rules don't.

**3. 🌊 There are infinite ways to phrase a request.** You cannot list them, so you cannot test them.

**4. ⚖️ Every tightening costs you something real.** Make it more suspicious and it starts refusing
perfectly legitimate requests. An over-cautious Pokémon that won't help with anything is also a
failure — just a quieter one.

## Defending in layers 🛡️

No single layer holds, so you stack them:

1. 🎓 **Train the rules properly.** The foundation. Not sufficient alone.
2. 🚪 **Screen what goes in.** Catch obviously hostile requests before they reach your Pokémon.
3. 🚨 **Screen what comes out.** Often *better* than screening inputs — because **a banned move is
   easier to recognise than a sneaky request.** You can argue about whether a question is innocent;
   you cannot argue about what the Pokémon just did.
4. 🧪 **Train a dedicated referee** on thousands of synthetic attempts, covering every trick anyone
   has published. Cuts success rates dramatically for a small cost in false alarms.
5. 📊 **Watch the pattern, not the request.** Finding a jailbreak takes **dozens of attempts.** One
   weird request is noise; forty weird requests from the same person in ten minutes is an attack —
   and you'll only see it if you're looking at the sequence.
6. 🔐 **Limit what it can do at all.** The strongest layer: a Pokémon that physically cannot perform
   the banned move cannot be talked into it.

## The honest framing 📌

This is the same problem as every adversarial security problem ever, and **nobody has solved any of
them.** Locks, spam filters, fraud detection — all of it is raising cost, not achieving prevention.

So don't measure success as *"can it be jailbroken?"* — it can. Measure **how hard it is, how often
it works, and what it costs you in false refusals.**
