---
id: "215"
slug: multi-token-prediction-and-speculation
style: pokemon
category: open-weights
difficulty: advanced
question: "Is multi-token prediction the same thing as speculative decoding?"
tags: [multi-token-prediction, speculative-decoding, training-objective, throughput, deepseek]
---

# No. Future Sight makes you a better Trainer. Sucker Punch just steals a turn.

**Future Sight**, which **Xatu** has known since it was a **Natu**, does nothing on the turn you
pick it. The message says you foresaw an attack, and two turns later 120 base power of Psychic
damage lands on whatever is standing there. To use it at all you have to hold the board two turns
out in your head — who will still be in, what they will have set up, whether the switch you are
about to make survives that long.

**Absol**'s **Sucker Punch** is a different animal entirely. 70 base power, +1 priority, and it
**fails outright if the target is not attacking that turn**. It changes nothing about how well
Absol fights. It steals a turn when you guessed right.

They are not the same thing. The confusion comes from the fact that it is the same Trainer doing
both, and the reason the guess lands is the two turns of practice Xatu made them do.

## Two different pictures

```
  RAISING IT — Future Sight changes what the Pokémon is
  ┌──────────────────────────────────────────────────────────────────────┐
  │  this turn ──► the usual attack ──────────────► lands now            │
  │      │                                                                │
  │      └──────► Future Sight, aimed at the turn after next ──► lands    │
  │               then, whatever has happened in between                  │
  │                                                                       │
  │  Two turns ahead, not five. You can leave the move off the set        │
  │  entirely and the Pokémon is exactly as strong. You cannot un-learn   │
  │  having been made to look two turns ahead while it was raised.        │
  └──────────────────────────────────────────────────────────────────────┘

  FIGHTING WITH IT — Sucker Punch changes the clock, not the Pokémon
  ┌──────────────────────────────────────────────────────────────────────┐
  │  guess: "they will attack"  ──►  throw it and find out                │
  │                              │                                         │
  │              ┌───────────────┴───────────────┐                        │
  │              ▼                               ▼                        │
  │        they attacked:                  they used Swords Dance:        │
  │        it lands, free turn             it fails, turn spent           │
  │        → two turns of work in one      → one turn, nothing gained     │
  │                                                                        │
  │  Reported: the guess is good 85–90 times in 100 → about 1.8× the work  │
  │  And note what CANNOT happen: a wrong guess never produces a           │
  │  different battle. It costs you the turn. It never changes the result. │
  └──────────────────────────────────────────────────────────────────────┘
```

## Why aiming two turns out helps at all

A Pokémon raised only to answer the turn in front of it learns to answer the turn in front of it.
Ask it for the turn after as well and it is corrected twice as often — and, more to the point, it
is punished immediately for a move that looks fine now and leaves it with nothing next turn.
The gains show up hardest where a choice now decides something later: long **Battle Tower** runs,
**Trick Room** teams, a **Dragon Dance** or a **Calm Mind** that only pays two turns after you
spend the turn. On a **Route 1** scrap against a **Youngster**'s **Rattata** you would never
notice, which is why small tests of this look like nothing.

There is a real detail worth keeping: Future Sight is *aimed*, not fired blind. It waits for the
turns in between to actually happen and then lands into whatever is really there. That is also
exactly why it can be repurposed as a guess later — it was already reasoning along the real
sequence of turns.

## Why they get confused, and what the confusion costs

You can drop the move from the set, or keep it and use it to steal turns. Elegant, and the source
of the muddle. Two ways to get it wrong:

* **Reading a stolen turn as strength.** "1.8× the turns" is a Sucker Punch result. It says
  nothing about whether the Pokémon beats **Cynthia**'s **Garchomp**. That is a different,
  smaller, much harder number to pin down.
* **Reading strength as stolen turns.** A Trainer who raised a Pokémon on Future Sight and never
  taught it Sucker Punch gets none of the speed.

## What the stolen turn actually depends on

1. **How busy you already are.** Sucker Punch pays because the turn would otherwise be spent
   waiting. In a one-on-one at the **Battle Tower** that is most turns. In **VGC** Doubles, with
   **Amoonguss** and **Incineroar** both demanding a decision every single turn, the guess costs
   more than the gap it fills. Every headline number is measured one-on-one.
2. **How readable the opponent is, which depends on the opponent.** 85–90 is against a
   **Bug Catcher** sending **Weedle** at you. Against someone running **Protect**, **Swords
   Dance** and **Substitute**, the guess collapses — and below about half the time, checking costs
   more than guessing saves.
3. **How far ahead you guess.** Two turns is deliberately cautious. Guess four and the win is
   bigger and so is the waste when you are wrong.
4. **How you check.** "Did it match what I would have picked anyway?" and "did it survive the
   proper check?" are not the same test. A **Battle Frontier** that quietly does the first while
   telling you it did the second is not showing you your own Pokémon's battles. Ask which.

## What a Gym Leader is listening for

That you split raising from fighting in the first sentence, and can say what each one buys —
being corrected twice as often against filling an idle turn. Then the part that cannot go wrong:
a bad guess costs a turn and never changes the outcome. The strongest answers raise the crowded
field unprompted, because that is why a published 1.8× turns into 1.1× at a real tournament.

## Where this stands, September 2026

The two-turn aiming, the 85–90 out of 100, and the 1.8× all come from published rulebooks and are
as solid as anything here. The claim that the newest generation kept the arrangement untouched is
**second-hand**: the sites that hold the report and the cards are blocked from where this was
written. The distinction itself — what you did while raising it against what you do with it in
the match — belongs to no generation and will outlast all of these.
