---
id: "262"
slug: grammar-constrained-decoding
style: pokemon
category: optimization
difficulty: advanced
question: "How does grammar-constrained decoding work at the logit level, and what does it cost when the grammar fights the model?"
tags: [constrained-decoding, grammar, structured-output, json-schema, masking]
---

# The game greys the button out before you can press it

**Taunt** lands. Look at your move screen: **Recover** and **Toxic** have gone grey. You cannot
select them. The game did not let you choose and then tell you off — it removed the option from
the menu before your thumb got there.

That is grammar-constrained decoding, exactly. A rule is watching the field, and every turn it
recomputes which buttons are pressable and blanks the rest. The guarantee is absolute and easy to
state: whatever comes out is legal. Everything difficult is in three places — recomputing the
menu fast enough, the fact that a rule written about *moves* is enforced on *buttons*, and what
happens when the only legal buttons are ones your Pokémon hates.

```
  this turn                                   your four slots + everything else
  ─────────                    ┌────────────────────────────────────────────────┐
  field state: Taunt active    │  Recover  Toxic  Scald  Baneful Bunker  switch │
        │                      └────────────────────────────────────────────────┘
        ▼                                        │
  ┌──────────────┐   menu mask   ┌───────────────▼────────────────────────────────┐
  │ what the     │─────────────► │  grey    grey   OK     grey           OK       │
  │ clause allows│               └───────────────┬────────────────────────────────┘
  └──────────────┘                               ▼
        ▲                             press one of what is left
        └───────── update on what you pressed ◄──┘

  The greying happens BEFORE any of question 260's odds are consulted.
  Whatever you were weighing up is re-weighed over what survived.
```

## Flat clauses, and clauses with a memory

**Taunt** is flat: a whole category is out for a few turns and nothing about your history matters.
So is **Heal Block**, and so is the **Assault Vest**, which raises Special Defence by half and
forbids every status move for as long as it is held.

Others need memory. **Torment** forbids the move you used *last turn*, so the menu depends on one
turn of history. **Disable** blanks the specific move the target last used. **Encore** goes the
other way and forces the repeat. A **Choice Scarf** locks you to the first move you pick after
switching in, so the menu depends on a decision made turns ago. **Imprison** removes every move
the *opponent* knows, so the menu depends on somebody else's four slots. **Gravity** takes away
**Fly** and **Bounce** by grounding the whole field — a rule that names a property, not a list.

That ladder is the real dividing line. A clause with no memory is cheap. A clause that needs one
turn of history is more machinery. A clause that needs the whole battle needs a stack, and that is
why the fast implementations keep one per battle rather than a single number.

**And the menu is recomputed instantly.** That is not free — somebody paid for it. The trick is to
work out in advance which buttons are grey in which situations and keep the table, so the game is
doing a lookup rather than re-reading the rulebook every turn.

## Why the rule and the button do not line up

Clauses are written about **moves**. What you press is a **slot**, and one is not one.

In the generations where **Hidden Power**'s type came from a Pokémon's IVs, that button was Grass
on one Pokémon and Ice on another, with the same name on both screens. A clause about Ice moves
has to see past the label to what the button will actually be. A clause about status moves has to
resolve every button the same way, every turn, before it can grey anything — and two different
games do not always resolve them identically, which is why the same restriction behaves
differently in two places.

## What the greying costs you

1. **What is left may be nothing you wanted.** Taunt your **Toxapex** and it must attack. It has
   **Regenerator**, **Recover**, **Toxic** and a plan that needed all three, and now it is
   clicking **Scald** into a **Blissey**. Every legal button is legal. None of them was the point.
2. **The Choice lock, which is the big one.** You switch in with a **Choice Scarf** and pick **Ice
   Beam**. The opponent sends out a Water-type. You are now locked into Ice Beam and you cannot
   take it back. The first choice was legal, and it walked you into a position where every legal
   continuation is bad. Switching out clears the lock — and costs you a turn. That is what
   backtracking is: the fix exists, and you pay for it. Keeping several lines alive under a
   restriction is one of the few places the old search still earns its keep (question 261).
3. **You may have greyed out the setup.** An **Assault Vest** on a Pokémon that only ever attacked
   costs it nothing at all. The same Vest on one whose whole plan was **Calm Mind** first, then
   attack, has removed the plan and left the attacks. The argument about whether restrictions make
   models worse is this argument: it depends entirely on whether the thing you took away was the
   turn they needed before they could act. Leave the setup move in the schema and most of the loss
   goes away.
4. **A legal move is still not the right move.** Question 203 is that whole fight and nothing here
   changes it. Earthquake is a legal, well-formed choice against a **Bronzong** with **Levitate**.
   Greying the menu removed the moves you never knew. It did not remove the ones that do nothing.

And when the menu greys out completely, the game does not invent a fifth move. It gives you
**Struggle**, which takes a quarter of your maximum HP. That is the dead end at the bottom of
every restriction: sometimes the only legal continuation is one that hurts you.

## What to do instead of fighting it

* **Bring a Pokémon that was built for the restriction.** A special attacker that never wanted a
  status move loses nothing to the **Assault Vest**. A constraint that agrees with the Pokémon
  costs nothing, and that is the entire difference between a restriction imposed on a model and a
  restriction it was trained under.
* Keep the clause shallow, put the setup turn first, and ask for moves it would have picked
  anyway.
* **Do not stack a Torment on top of a Choice lock.** The penalties of question 260 and a strict
  menu fight each other: structure needs the same button again and again, and a rule against
  repeating is a rule against finishing.
* Check what the clause silently fails to cover. A restriction you believe in and the game does
  not enforce is worse than no restriction, because you stopped watching.

## What a Gym Leader is listening for

That you can name the guarantee precisely — no move it does not know, no button that is not there
— and then name the price: you are choosing from a menu that may hold almost nothing your Pokémon
wanted, and how much that hurts is exactly how far the clause sits from how it wanted to play.

**Citation note.** The arXiv identifiers linked in the serious half are given from working
knowledge. `arxiv.org` is blocked from the environment this was written in, so **not one of them
was resolved while writing**. Resolve every identifier before you cite it.

## Where this stands, September 2026

Primary, read first-hand this session: the XGrammar repository's own claims of complete structural
correctness and near-zero overhead, which engines it is the default backend for, and the dates on
those integrations. Coverage: the papers, and the whole argument about whether being greyed down
makes a model worse — that one is live, not settled, and both sides are worth reading. What will
not rot: **a mask buys a guarantee about form and charges you in how far the clause sits from what
the Pokémon wanted to do.**
