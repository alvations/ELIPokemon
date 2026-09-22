---
id: "259"
slug: non-autoregressive-generation
style: pokemon
category: optimization
difficulty: advanced
question: "Non-autoregressive generation has been reinvented every few years since 2018. Why does the field keep returning to it, and why does it keep retreating?"
tags: [non-autoregressive, machine-translation, distillation, speculative-decoding, latency]
---

# Both moves, locked in before either resolves

In a Double Battle you send out two Pokémon and you choose **both** of their moves before the turn
plays. Neither choice sees the other. That is non-autoregressive generation, and it is the oldest
idea in fast decoding: stop waiting, act on every slot at once. It was born in translation, it
reported something like fifteen times the speed, and it has come back about every three years
since — each time with a better trick, each time retreating for the same two reasons. One of them
is real and lives in the game. The other is a measuring mistake.

## The real one: two good choices that are bad together

Your **Gyarados** wants **Surf**. Your **Jolteon** wants to stay in. Both are correct on their
own. Surf hits every adjacent Pokémon **including your own partner**, and Jolteon eats it.

```
  ONE AT A TIME                          BOTH AT ONCE

  pick Surf, see the field, then pick    slot 1: Surf .45  Waterfall .40  Protect .15
  the second move knowing the first      slot 2: stay .45  Protect   .40  switch  .15
                                                   |              |
  the second choice can dodge the first   each slot picks its own favourite, blind
                                                   v
       Surf, then Jolteon pivots out       Surf + stay in   <- nobody wanted this
```

It shows up the other way too: both Pokémon use **Protect** on the same turn and the whole turn is
spent doing nothing, and **Protect** used again straight after is likelier to fail. Two locally
excellent picks, one wasted turn. Nothing is wrong with either Pokémon. What is wrong is that
neither of them could see the other's move.

## Every fix, and what each one quietly admits

| Fix | What it does | What it gives up |
| --- | --- | --- |
| **Sketch the teacher** | Train the parallel team only on lines a one-at-a-time team already played | **Smeargle** can only **Sketch** a move somebody else already used |
| **Re-pick the unsure slot** | Lock in both, keep the confident one, choose the other again | Turns are back. The thing you removed is the dial again |
| **Pad the turn** | Allow extra empty slots and collapse them afterwards | Guessing how many actions the turn holds was the damage all along |
| **Edit the turn** | Insert and delete moves over several passes | It is a sequence of turns wearing one turn's costume |
| **Peek at the answer while training** | Show some correct choices during practice | Conditioning, smuggled in at the Day Care |

The first row is the tell. **Sketch is not a convenience, it is the foundation.** A parallel team
can only be taught from a serial team's chosen line, because that line has already picked one way
to win out of the many that existed. A strategy that requires **Smeargle** to have watched
**Cynthia**'s **Garchomp** first has not escaped Cynthia. It has moved her to the Day Care.

## Why it kept retreating

1. **The baseline was Youngster Joey's Rattata.** Tune the ordinary one-at-a-time team properly —
   a huge front end, a tiny finisher — and it is just as quick. Almost all of the famous speedup
   was measured against an opponent nobody had bothered to optimise.
2. **The advantage dies in the queue.** Alone in the **Pokémon Center** at midnight, going faster
   matters. With a queue out of the door, **Nurse Joy** takes a whole party at a time either way,
   and the parallel trick stops buying anything. Battling one match at a time is exactly the
   situation a real service tries never to be in.
3. **The scoreboard was forgiving.** The errors this makes — the same move twice, a missing
   action — were the errors the old scoring was softest on. Judged by anyone watching, the gap
   read wider.
4. **The teacher never left.** If you need a one-at-a-time team to train from and to check
   against, you are running two teams to avoid running one.

## What actually won

**A fast proposer with a veto behind it.** **Regieleki** has 200 base Speed, the highest in the
game, and it calls the next few actions before anyone else can move. The ace behind it checks the
call in one pass and throws out everything from the first disagreement onward. The battle log ends
up **exactly** the log the ace would have produced alone — the speed was free because the guess
was only ever a guess. That is speculative decoding (questions 033, 215, 230), and it is where
this whole line of research actually shipped: as drafting, never as the final word.

**And the wall panels in the Ruins of Alph** (question 258). "Choose every slot, keep the
confident ones, blank the rest, go round again" is the same loop, seven years older than the
diffusion models now running it with a far bigger budget. The open questions are still 2018's
questions: how long is the turn, and what happens when two slots are decided blind.

Where acting in parallel genuinely earns its slot: one battle at a time with nobody queued behind
it, interpreting live while the speaker is still talking, a handheld with no queue to exploit, and
very short answers. Every one of those is the empty **Pokémon Center** at midnight.

The games do contain one honest fix, and it is worth knowing how narrow it is. **Telepathy** makes
an ally's spread move miss you outright, and **Rock Slide** hits both opponents while sparing your
partner. Both work. Both are available to a handful of Pokémon and a handful of moves. That is the
shape of every coordination fix here: real, and not general.

## What a Gym Leader is listening for

That you ask what the other side of the stopwatch was doing. Before believing any "faster" claim,
name the opponent, name the queue length, and ask whether the fast team could have been trained at
all without the slow one.

**Citation note.** The arXiv identifiers linked in the serious half are given from working
knowledge. `arxiv.org` is blocked from the environment this was written in, so **not one of them
was resolved while writing**. Resolve every identifier before you cite it.

## Where this stands, September 2026

The history here is working knowledge of the translation literature and should be treated as
coverage. One thing is primary and I read it myself: the LLaDA chamber's own note that its
sampling is slower than going one at a time (question 258) — the 2018 story, replayed with a
bigger budget. What does not rot is the discipline. **Name the baseline, name the queue, and find
out who taught the fast one.**
