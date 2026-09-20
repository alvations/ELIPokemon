---
id: "220"
slug: thinking-budget-and-effort-control
style: pokemon
category: open-weights
difficulty: advanced
question: "Qwen controls reasoning with a thinking switch, a token budget and an effort level. How does that differ from a single effort dial?"
tags: [qwen, reasoning-effort, thinking-budget, latency, prompt-caching]
---

# Ember, Flamethrower, Fire Blast — and the PP that runs out underneath all three

**Ember** is 40 power, 100 accuracy, 25 PP. **Flamethrower** is 90 power, 100 accuracy, 15 PP.
**Fire Blast** is 110 power, **85** accuracy, **5 PP**. One **Charizard**, one type, three
settings — and the price of the top setting is paid twice: in how often you can use it, and in how
often it simply misses.

That is the whole shape of Qwen's reasoning controls, and Qwen has now set it up three different
ways in public.

**Round one (Qwen3, 2025).** One Pokémon, and a switch: use a Fire move or do not
(`enable_thinking`), plus an explicit allowance on how much it may burn — reported on the hosted
platform as anything from 1 to 32768, defaulting to 4000.

**Round two (the 2507 refresh, 2025).** The switch was thrown away. Qwen registered **two separate
Pokémon** instead — one raised to answer straight away, one raised to think — on the stated ground
that raising a single one to do both pulls its training in two directions and spoils both halves.

**Round three (Qwen3.6 and Qwen3.8, 2026).** Back to one Pokémon, with a named setting. The team's
own repository says it plainly: *"Reasoning depth can be tuned with `reasoning_effort`, and
reasoning context from historical messages is retained via `preserve_thinking`."* Qwen3.6 brought
the second half in under the name "Thinking Preservation".

So there are **two instruments here, not one**: which move you pick, and how much PP it has left.
Question 204 describes a family that gives you only the first. The gap matters.

```
   WHICH MOVE YOU PICK                        HOW MUCH PP IS LEFT
   ─────────────────────────────────          ──────────────────────────────────
   Ember  ·  Flamethrower  ·  Fire Blast      25  ·  15  ·  5
   "how hard should you swing"                "how many times you may swing"

   changes the whole turn:                    stops you dead:
     · how much it burns                        · mid-battle, wherever you are
     · how many moves it chains                 · and what you get instead is
     · how much it says first                     not a smaller Fire move

   comes down gently                          does NOT come down gently
   ──────────────────────────────────────────────────────────────────────────────

     setting:     Ember        Flamethrower             Fire Blast (default)
                    │               │                            │
   burn            ▏             ▎▎▎                       ████████████
   turns spent     ▏             ▎▎▎                       ████████████
                                                                  ▲
   PP runs out ────────────────────────┤                          │
                                       └─ and what waits there is │
                                          STRUGGLE: typeless, 50  │
                                          power, and a quarter of │
                                          your own max HP ────────┘
```

**Struggle** is the point. Running out of PP does not hand you a weaker Fire Blast. It hands you a
different move that hurts *you*, and it is what a truncated deliberation actually looks like.

## Three things that catch Trainers out

**1. The setting names are a per-species table, not a standard.** Hand **Charizard** the **Surf**
TM and nothing happens — Charizard cannot learn Surf, and the game does not give you a weaker
Surf, it refuses. Issue #217 on the Qwen team's own repository is exactly that refusal, written
out: the Qwen3.8-27B template answers an unknown setting with `Unexpected reasoning effort high.
Supported types are xhigh (default), medium, and low.` Three settings. **`high` is not one of
them** — and `high` is what a harness raised on a different Pokémon will hand over first.

**2. The shipped default is the 5-PP move.** `xhigh` is the top of the ladder, on by default.
Coverage of local runs reports one small errand costing over twenty-two thousand thinking tokens
and tens of minutes on a home card. That is a Charizard that has been taught to answer everything
with Fire Blast, including **Caterpie**. Five of those and you are at Struggle.

**3. Some of them have no small move at all.** The open `Qwen3.8-2.4T-A95B` is reported to reason
every single time: there is no way to ask it for a quick answer. It is a Charizard whose only
attack is **Hyper Beam** — 150 power, 90 accuracy, 5 PP, and a compulsory recharge turn every
time. The rented `qwen3.8-max` does have the small move. Same name, different Pokémon
(question 219).

## How to actually set it

1. **Work out whether you need the PP limit at all.** PP is a hard stop for a long day on the
   route. It is not how you ask for a gentler attack — that is **Ember**, and asking for it by
   letting Fire Blast run dry is how you end up at Struggle.
2. **Choose per route, not per turn.** Catching, grinding and scouting run on Ember; the
   **Elite Four** is what Fire Blast is for. Sweep it on your own opponents starting at the
   default and stepping *down*, exactly as in question 204.
3. **Count the Struggles out loud.** If any share of your battles ended on Struggle, your win rate
   is an average over two different Pokémon and the number hides which one moved.
4. **Check compatibility per species, every time.** Whether a move is on the list is a property of
   that individual, not of the type, and it changes between one and the next.
5. **Watch what carrying boosts forward costs.** **Calm Mind** on **Alakazam** is real and it
   stacks to +6 — and every stage was a turn you did not attack, and all of it is gone the moment
   it switches out. Preserving the thinking is the same bargain: continuity now, a longer setup
   each turn.

## What a Gym Leader is listening for

That you separate "how hard" from "how many times" and can say which of the two your route
actually needs. Then that you treat the list of settings as a compatibility table to be checked,
not a dial to be turned. The strongest answers notice that Qwen threw the switch away and then
built it again in a different shape, and read that as the trade-off being real rather than as
dithering: registering two Pokémon bought quality by giving up the control, and the named setting
is an attempt to win the control back without paying that again.

## Where this stands, September 2026

The `reasoning_effort` and `preserve_thinking` features and the Qwen3.6 "Thinking Preservation"
line are quoted from the Qwen team's own repository, read directly; the refusal text is from issue
#217 in that same repository. The PP allowance and its default, the `xhigh` default, the
overthinking reports and the always-reasoning behaviour of the 2.4T weights come from coverage and
community reports, because the developer docs and the model cards are behind an egress block
here — those pages are the authority. The setting names will rot before anything else above does.
Fire Blast will still be 5 PP.
