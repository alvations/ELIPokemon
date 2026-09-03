---
id: "005"
slug: layer-normalization
style: pokemon
category: transformers
difficulty: intermediate
question: "What is layer normalization, and why did LLMs move from post-norm to pre-norm?"
tags: [layernorm, rmsnorm, pre-norm, training-stability]
---

# LayerNorm is the Level 50 Flat Rule

You know how competitive tournaments run **Flat Rules**? Everybody's Pokémon gets set to
Level 50. Your lovingly EV-trained Level 100 Garchomp and your friend's Level 12 Bidoof walk
into the same stadium on the same scale.

That's LayerNorm. Before a Pokémon acts, its stats get rescaled to a sane range so the battle
is decided by *strategy* — the relationships between the stats — and not by one number having
run away to 40,000 while its teammates sit at 3.

The important bit: the rescaling looks at **that one Pokémon's own six stats**. It doesn't
peek at the rest of your team, and it doesn't care who else is in the tournament. So it works
identically in a full six-on-six and in a one-on-one exhibition match. (Compare BatchNorm,
which rescales you relative to *everyone else in the room* — great in a packed stadium,
completely lost when you show up alone.)

## Where you put the scale is a huge deal ⚖️

Every Gym in the League is a checkpoint. Your team walks in, fights, walks out, moves to the
next Gym. The question is where the Flat Rule scaler sits.

```
  POST-NORM: scaler is at the Gym EXIT       PRE-NORM: scaler is at the Gym DOOR

  ┌────────────────────────────────┐         ┌────────────────────────────────┐
  │  team ──┬─────────────┐        │         │  team ──┬───────────────┐      │
  │         ▼             │        │         │         ▼               │      │
  │      🥊 fight         │        │         │    ⚖️ rescale           │      │
  │         │             ▼        │         │         ▼               │      │
  │         └────► + ◄────┘        │         │      🥊 fight           ▼      │
  │                │               │         │         └──────► + ◄────┘      │
  │                ▼               │         │                 │              │
  │            ⚖️ rescale          │         │                 ▼              │
  │                ▼               │         │            next Gym            │
  │            next Gym            │         │   (the team itself was never   │
  │  (the TEAM ITSELF gets         │         │    touched — only the copy     │
  │   rescaled, every single Gym)  │         │    that walked into the fight) │
  └────────────────────────────────┘         └────────────────────────────────┘
```

**Post-norm** rescales your actual team on the way out of every Gym. Eight Gyms, fine. But a
League with a hundred Gyms? By the time news of the Champion's feedback travels back to your
starter, it's been squashed through a hundred rescalers and arrived as a whisper. Your
Charmander never learns anything. Deep post-norm teams just fall over.

**Pre-norm** rescales only the *copy* that steps into the arena. Your real team walks a clean
corridor from Gym 1 straight through to the Champion, untouched. Feedback from the top comes
back down that corridor at full volume, and every Gym hears it. That's why you can now run a
hundred-Gym League and it trains fine.

Pre-norm's own quirk: the team keeps *accumulating* — every Gym adds something and nobody ever
trims. By Gym 90 your team sheet is so loaded that one more Gym barely moves the needle, and
the last few Gyms end up mostly redundant. So you turn down how much each Gym is allowed to
add. Manageable. Nobody's going back to post-norm.

## RMSNorm: skip half the paperwork 📋

Full LayerNorm does two things: it recentres (subtract the team's average stat) and it
rescales (divide by the spread).

Someone eventually checked whether the recentring was doing anything. It mostly wasn't. The
**rescaling** is what keeps things sane; the recentring was ceremony.

RMSNorm just drops it. Same result, less paperwork at every one of a hundred Gyms — and when
you're running the League twice per Gym, skipping a form adds up. Every modern League runs
RMSNorm.

## What the Flat Rule is really for 🏟️

It's tempting to say "it makes the numbers nice". The real payoff is that it makes the League
**forgiving**.

Without it, one Pokémon whose Attack drifted to 40,000 dominates every calculation, the
Champion's feedback becomes wild and contradictory, and you spend all your time nursing the
training schedule instead of training. With it, doubling a Pokémon's raw stats changes nothing
— it gets scaled right back — so the whole League stops caring about the exact numbers you
started with and starts caring about the strategy. You can be sloppier about setup and still
finish the run.
