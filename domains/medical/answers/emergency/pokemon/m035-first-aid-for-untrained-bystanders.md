---
id: "m035"
slug: first-aid-for-untrained-bystanders
style: pokemon
category: emergency
difficulty: intermediate
question: "Why is first-aid guidance for untrained bystanders different in kind from clinical guidance, rather than just simpler?"
tags: [first-aid, bystander, guidance-design, simplification, dispatcher]
---

# Focus Energy told you it raised your critical-hit rate. In Red and Blue it quartered it.

The critical-hit routine in Red and Blue has a comment in the decompilation written by the people
who read the machine code, and it is the single best example in the games of advice that did the
opposite of what its own text promised:

```
   CriticalHitTest:                               engine/battle/core.asm
     ...
     bit GETTING_PUMPED, a        ; test for focus energy
     jr nz, .focusEnergyUsed      ; bug: using focus energy causes a shift to
                                  ; the right instead of left, resulting in
                                  ; 1/4 the usual crit chance
     sla b                        ; (the intended path: double it)
     ...
   .focusEnergyUsed
     srl b                        ; halve it. Then it is halved again below.
```

**Focus Energy**'s in-game text says it gets the user pumped up for critical hits. The
implementation shifts the wrong way and makes them four times rarer. A new player who did the
obvious thing — read the description, believe it, use the move — was worse off than a player who
ignored it, and had no way whatsoever to find out. It was corrected in later generations. That is
what it looks like when guidance written for someone who cannot check it turns out to be harmful,
and it is why the test for such guidance is never *is this right in principle* but *what happens
to everybody who follows it*.

## Four consequences of writing for a reader who cannot check

```
   assumption about the reader           a competitive rules post   the game's own tutorial
   ────────────────────────────────────────────────────────────────────────────────────────
   knows which case applies              yes                        no
   can tell when they have it wrong      yes                        no
   can undo a mistake                    usually                    often not
   will do this many times               yes                        maybe once
   has anyone to correct them            yes                        no
   ────────────────────────────────────────────────────────────────────────────────────────
   therefore: conditions are             cheap, so state them       expensive, so collapse them
              what is optimised          the best line              every attempt, including bad ones
```

* **Collapse the branches.** The top-level choice Red and Blue puts in front of a new player is
  four options wide — the FIGHT menu and its three neighbours — and no more. Everything
  conditional lives underneath, discovered later. A game that opened on the damage formula would
  be correct and unusable.
* **Prefer things whose failure mode is cheap.** A new player never needs the catch-rate formula,
  because the names carry the ordering: **Poké Ball**, then **Great Ball**, then **Ultra Ball**,
  then **Master Ball**. Getting it wrong costs one ball. Compare an instruction whose failure
  cannot be taken back: a **TM** in Red and Blue was consumed on use, and an **HM** move, once
  taught, could not be removed at all — the games added a **Move Deleter** later precisely because
  an irreversible action had been handed to inexperienced players.
* **Accept a lower ceiling to raise the floor.** *Lower its HP, then try a Ball* is not the
  optimal line and never was. It is approximately right in almost every case, it is robust to
  being done badly, and it is impossible to turn into a disaster. That is the trade, taken
  deliberately.
* **Bias toward acting.** The game's unconditional, unbranched, repeated instruction is to go to a
  **Pokémon Center**. It is free, it is always available, and it is never the wrong answer, which
  is exactly why it can be given with no conditions attached to a player who cannot evaluate
  conditions.

## The printed number has to be true, or the reader has nothing

Red and Blue also broke the other half of the contract. `MoveHitTest` carries its own comment:
*note that this means that even the highest accuracy is still just a 255/256 chance, not 100%.* A
move printed at 100 missed one time in 256. The text was right and the implementation was not, and
no player could have discovered the gap.

Emerald fixed it where it had to be fixed — in the implementation, not the text.
`Cmd_accuracycheck` ends with `(Random() % 100 + 1) > calc`, so a printed 100 is genuinely 100,
and a reader who cannot inspect anything can rely on what is written. **Zap Cannon** and **Dynamic
Punch** are printed at 50 in Emerald's own move table, **Blizzard** at 70 and **Hypnosis** at 60,
and every one of those is honest: the whole value of printing a number is that it is checkable and
coachable, and a number the reader cannot trust is worse than no number at all.

Which is also why the games print numbers at all instead of saying *usually hits*. PP is a count,
not a feeling. Base Power is a number. A vague instruction cannot be taught, rehearsed, counted
along with, or corrected halfway through; a specified one can.

## Where the game stops

Plain prose from here. This section is about people and the metaphor is set down.

Bystander first-aid guidance has a reader who is untrained, frightened, acting once, with no
feedback and no way to detect that the branch they chose was the wrong one. So what it optimises
is not the outcome achievable by someone who applies it correctly but the expected outcome across
everybody who will attempt it, misreadings included. That makes it a different document from
clinical guidance rather than a shortened one: branches get collapsed even at a real cost in
accuracy, actions are chosen for having benign failure modes rather than for being best when done
right, a lower ceiling is accepted to raise the floor, and the recognition step is deliberately
biased toward acting because not starting when something was needed is far worse than starting
when it was not. All **mechanism**, checkable by reasoning.

The removals are the clearest evidence of the discipline. Butter, oil or ice straight onto a burn.
Inducing vomiting after a swallowed poison. Cutting, heating or sucking a snake bite. Tilting the
head backwards for a nosebleed. Alcohol as a stimulant for someone cold or collapsed. And the lay
pulse check, removed because pulse checks are unreliable even among trained rescuers and the delay
costs more than the error it was supposed to prevent. Each had a plausible mechanism, a failure
mode that sounded benign and was not, and a reader with no way to tell. **(Consensus** that each
was removed; **council-dependent** in how each council words things now.**)** One has gone the
other way: tourniquet guidance moved away from lay use and then substantially back toward it for
life-threatening limb bleeding as evidence accumulated — so *removed* does not mean *wrong
forever*, it means the balance of harms went the other way at that revision.

The branching that the written document could not carry did not disappear. It went to a person on
the telephone, who can assess, adapt and correct in real time. That is why **calling the local
emergency number is not merely a request for an ambulance** — it is how the reader obtains the
branch logic the document had to leave out, from someone who can see which branch they are
actually in. If a call handler is giving instructions, those instructions are the ones to follow.

Some instructions carry a specified rate rather than an instruction to use judgement, for the
reason in the section above: self-paced attempts are far too fast or far too slow, and a named
target can be coached, rehearsed and counted. **The number is not stated anywhere in this answer,
deliberately.** It differs between national councils, it is revised on a cycle, and a
misremembered number acted on is the exact harm all of this exists to prevent. It belongs in the
reader's own council's current document and nowhere else.

## What a Gym Leader is listening for

* What did Focus Energy's description promise in Red and Blue, what did the code do, and why could
  no player have found out?
* Why was the 1/256 miss fixed in the implementation rather than by rewording the move
  descriptions?
* Why is the Great Ball through Master Ball naming a better piece of beginner guidance than the
  catch formula would be, even though it is less accurate?
* Why is *go to a Pokémon Center* safe to give with no conditions attached?
* What does a TM being consumed, or an HM move being unremovable, illustrate about exposing an
  irreversible action to someone who cannot evaluate it?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The current first-aid and basic life support guidance for the public issued by **the national
  resuscitation council for the country the reader is in**. This is the authority on every
  specific this answer declines to state, including any rate. The councils differ from one another
  and each revises on its own cycle.
* The current consensus on science with treatment recommendations issued by **the International
  Liaison Committee on Resuscitation**, including its first-aid material, which is the evidence
  synthesis the national councils write their public guidance from and where removals are argued
  rather than announced.
* **The reader's national or regional poisons information service**, which is the authority on
  ingestion and envenomation advice and on why the older advice was withdrawn.
* **The reader's own national ambulance service or equivalent**, for how dispatcher-assisted
  instruction is actually delivered where they are, which varies considerably.
* The first-aid manual published by **whichever voluntary first-aid organisation runs training in
  the reader's country**, for the public-facing wording as that country's trainers teach it.

No rate, depth, ratio, dose or setting is stated anywhere; nothing is quoted; and no guideline
number, document title or identifier is given, because none was opened. The Pokémon side is in the
opposite position and is sourced file by file in the closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all. If a call handler is giving instructions, those instructions are the ones to follow — they
come from someone who can assess the actual situation, which no written document can.

This is revision material about *how bystander guidance is designed and why*, written for someone
already trained, and the Pokémon framing covers the design problem only — nothing here stands for
a person. It is deliberately not first-aid guidance and is not usable as any: no sequence of
actions, no rates, no depths, no ratios, no doses, no settings, and the removed items are named as
history rather than as instruction. First-aid and resuscitation guidance **differs between
national councils and is revised on a cycle**. The reader's own national council, poisons service
and ambulance service are the authority; this is not, and it has had no clinical review. Nothing
here describes any real person, case or institution.

## Where this stands, October 2026

The Pokémon facts pinned to source are the Focus Energy shift bug and the 255/256 accuracy
ceiling, both from `engine/battle/core.asm` in the Red decompilation and both carrying the
decompilation's own comments quoted above as code; the FIGHT menu from the same file; and
Emerald's corrected accuracy comparison from `Cmd_accuracycheck` in
`src/battle_script_commands.c`, with the printed accuracies of Zap Cannon, Dynamic Punch, Blizzard
and Hypnosis from `src/data/battle_moves.h`. **The Move Deleter's history, and HM moves being
unremovable in Red and Blue, are stated from working knowledge rather than read from either
decompilation**, as is the general claim about what later generations fixed. On the clinical side
the design argument is **mechanism** and stable, each removal is **consensus** as of writing, and
everything else — current wording, recognition cues, every number, and how prominently
dispatcher-assisted instruction is foregrounded — is **council-dependent** and revised on cycles
the councils do not synchronise. The tourniquet example is here specifically because it shows this
material changes direction; a reader taking the direction of travel from this answer rather than
from their own council's current document has misread it. Dated October 2026.
