---
id: "205"
slug: model-tiering-and-routing
style: pokemon
category: frontier
difficulty: intermediate
question: "Frontier families now ship three or four tiers that share a context window. What actually differs, and how do you route between them?"
tags: [routing, cascades, cost, model-selection, tiering]
---

# Bulbasaur, Ivysaur and Venusaur fight on the same field

Every evolution line is a tier ladder. Bulbasaur, Ivysaur and Venusaur are all Grass/Poison, all
face the same **Type Chart**, all get four move slots, all cap at level 100. The arena does not
change. What changes is the **Base Stat Total**: 318, then 405, then 525.

That is exactly what the current model families look like. One vendor ships three tiers that all
carry the same million-token window and the same output limit; another ships four, and only the
smallest one has a smaller window at all. The ladder is not a ladder of arenas. It is a ladder of
stats, with a price tag attached.

So the tiers differ on two things you can read off the card — **cost** and **capability** — and a
third you only learn by battling: which of your actual opponents each one loses to.

## Leading with the scout, and why it is not free

The standard plan is to send out something cheap, see what happens, and switch to the ace when it
goes badly. The arithmetic is worse than it looks, because **switching costs a turn** — and if
the opponent set **Stealth Rock**, the ace takes damage just for walking in.

```
   straight to the ace:   cost = the ace

   scout first:           cost = scout + (1 - p) × (scout wasted
                                                    + the ace
                                                    + the turn you lost)
                            │
                            └─ p = how often the scout was enough

   Against a 25-to-1 gap in what the two cost you, the scout has to be
   right well over nine times in ten before it pays — and every miss
   costs twice: once in resources, once in tempo.

   ┌──────────┬──────────┬──────────┬─────────────────────────────────┐
   │ tier     │ arena    │ rel. $   │ what it is actually for         │
   ├──────────┼──────────┼──────────┼─────────────────────────────────┤
   │ Venusaur │  same    │  25×     │ the 2% of battles that matter   │
   │ Ivysaur  │  same    │  10×     │ the everyday route              │
   │ Bulbasaur│  same    │   1×     │ scouting, catching, grinding    │
   └──────────┴──────────┴──────────┴─────────────────────────────────┘
```

## How to choose, in order of how well it works

1. **By the route, decided in advance.** Dull and effective. Catching and grinding go to the
   small one, the everyday gauntlet to the middle, and the fully evolved ace comes out for a
   named list of opponents. Most of the saving lives here.
2. **By a cheap read of the matchup before you commit.** Their lead's type, how many Pokémon they
   have left, whether this looks like a Gym you have seen before. Rough, but it costs no turns.
3. **By checking the result afterwards.** Worth it only when checking is genuinely cheaper than
   fighting — a type match-up you can verify instantly, a move that either hit or did not.
   Sending out a *second* Bulbasaur to judge the first one is not a saving.
4. **By asking the Pokémon how confident it is.** Appealing, and the weakest in practice. Most of
   them do not know, which is the entire argument for a Pokémon bred to know (question 202).

## What Trainers get wrong

* **Judging tiers by Base Stat Total instead of by their own opponents.** The published gap is an
  average over a league you are not in.
* **Forgetting setup.** Ivysaur after a Swords Dance and Venusaur with no boost are two different
  Pokémon, and which one wins depends on the matchup (question 204).
* **Switching constantly.** Every switch resets the stat boosts you spent turns earning. A plan
  that pivots every turn can lose to a plan that never pivots at all.
* **Treating speed as decoration.** The small one is not just cheap. On the routes where turns
  matter, being fast *is* the reason to use it.

## What a Gym Leader is listening for

That you notice the arena is identical and ask what is genuinely different. Then the switching
maths, including the scout you already spent and the Stealth Rock on the way in. The strongest
answers say which fraction of battles they would give to which Pokémon **and** how they would
check the split was right — how often they had to switch, how often each one lost, and the cost
per badge rather than the cost per turn.

## Where this stands, September 2026

The tier names, the prices and the windows move every few months; the figures here are from
September 2026 and should be re-read off the current card before anyone plans a budget around
them. The shape — the same arena, different stats — is the part that keeps.
