---
id: "204"
slug: effort-and-adaptive-thinking
style: pokemon
category: frontier
difficulty: intermediate
question: "Modern reasoning models expose an effort dial instead of a thinking-token budget. How do you tune it?"
tags: [effort, adaptive-thinking, inference-cost, prompt-caching, latency]
---

# How many turns will you spend setting up?

The old interface was a Trainer counting turns out loud: thinking on, *this many* turns of
Calm Mind, then attack. The current one is **Speed Boost**. Ninjask's ability raises its Speed a
stage at the end of every turn without spending a turn on it — the Pokémon decides, and what you
set is the posture, not the schedule.

That posture has five settings, and they read like setup moves. Clicking the attack straight
away. One **Dragon Dance**. The default. A long **Swords Dance** chain. And **Belly Drum**, which
maxes Attack to +6 and costs half your HP to do it — absolute capability, no constraint on what
it spends. Gyarados, Scizor and Snorlax take the dial; some Pokémon do not have it at all.

Three things about it catch Trainers out.

**It is a posture, not a limit.** Setting the dial low does not forbid setup. Against something
genuinely threatening the Pokémon will still take a boosting turn — just fewer than it would
have. The real ceiling is the **turn count**, and setup turns and attacking turns come out of the
same pool. Spend them all on Swords Dance and the battle ends with your Attack at +6 and nothing
landed.

**It moves everything, not just the setup.** Switching, item use, pivoting — all of it. At a low
setting a Trainer commits early, switches less and says nothing; at a high one they scout, pivot,
and explain the plan. In a long battle that switching is most of what you are paying for.

**It is not a dial for how long the attack animation runs.** Belly Drum does not make Body Slam
*longer*. If you want a shorter turn, ask for a shorter turn.

```
    setting:   attack      Dragon      default     Swords       Belly
               at once      Dance                  Dance chain   Drum
                 │            │            │            │           │
   setup turns   ▏           ▎▎           ▍▍▍▍        ▊▊▊▊▊▊▊     ████████
   switches      ▏▏          ▎▎▎          ▍▍▍▍▍       ▊▊▊▊▊▊      ███████
   clock         ▏           ▎▎           ▍▍▍         ▊▊▊▊▊       ███████
   payoff        ▔▔▔▔▔▔▔▔▁▁▁▁▁▁▁▁▔▔▔▔▔▔▔▔▁▁▁▁▁▁▁▁▔▔▔▔▔▔▔▔▁▁▁▁▁▁▁▁▔
                 ╰── matchup-dependent. Boosts stop at +6 no matter
                     what, and the flat part arrives well before that

   turn count ───────────────────────────────────────► hard ceiling on
                                                       setup AND attacks
```

## How to actually tune it

1. **Test it against your own ladder.** Start at the default and step down until you start
   losing, rather than starting low and hoping. A setting that worked on your last team does not
   carry over to this one.
2. **Split by format, not by turn.** A long Battle Tower run sits high; sweeping Route 3 does
   not. The scout Pokémon you send in first is the classic low setting.
3. **Mind the switch-out.** Stat boosts vanish the moment a Pokémon leaves the field. Changing
   the dial between requests is that switch — everything accumulated is gone. **Baton Pass** is
   the exception: Ninjask passes its boosts to the Pokémon coming in, which is exactly what a
   mid-conversation change on a supporting model does. Without it, pick a posture and stay in.
4. **Raise the dial instead of shouting at the Pokémon.** If it is playing shallow against a hard
   opponent, that is a setting, not a motivation problem.
5. **At the top settings, give it room.** A long battle needs turns on the clock. And a Pokémon
   with Speed Boost cannot switch the ability off, which is the point of having it.

## Failure modes

* **Belly Drum against a Rattata.** You halved your HP to one-shot something you would have
  one-shot anyway, and the next Pokémon revenge-kills you. Maximum is occasionally worse than
  default, not just dearer.
* **Dropping the dial everywhere to save turns.** Looks like a faster run. Shows up as losses
  nobody connects back to it.
* **Confusing the ability with the item.** Speed Boost is an ability; it is not something you
  hand the Pokémon to hold. Passing one where the other belongs is simply rejected.

## What a Gym Leader is listening for

That you treat setup as **a real axis with a real cost**, tested against your own opponents,
rather than a habit. The strongest answer connects it to the switch-out and to how much pivoting
you are doing — in a long battle, those two eat the clock long before the boosting does.

## Where this stands, September 2026

The names of the settings, and which Pokémon have which, change generation to generation. Check
the current chart rather than a remembered one. The idea — one dial over how much you spend
before acting, tuned against your own record — is older than any of them.
