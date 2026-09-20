---
id: "203"
slug: constrained-output-and-hallucination
style: pokemon
category: frontier
difficulty: advanced
question: "If a model can only emit options from a fixed schema, has hallucination been solved?"
tags: [hallucination, constrained-decoding, schema, type-safety, abstention]
---

# Earthquake is a legal move against Bronzong

The claim that a typed decision model **cannot hallucinate** — as a property of the machinery
rather than a result of good training — is exactly true about one thing and quietly false about
the thing that loses battles.

What it guarantees is real. A Pokémon cannot use a move it does not know. The game will never
announce an attack that is not in the game, never invent a type, never produce a move name that
looks plausible and does not exist. Everything you would otherwise build to catch that — the
parsing, the validating, the retrying — stops being necessary.

What it does not guarantee is that the move was the **right** move. Earthquake is a perfectly
legal, perfectly well-formed choice against Bronzong. Bronzong has **Levitate**. It does nothing
at all, and it took your turn.

## The two axes people collapse into one

```
                     │  WORKS on this target   │  DOES NOTHING to it
   ──────────────────┼─────────────────────────┼──────────────────────────
    A MOVE IT KNOWS  │  what you wanted        │  ◄── EARTHQUAKE INTO
    (one of the four)│                         │      LEVITATE. The four
                     │                         │      slots cannot see
                     │                         │      this column at all
   ──────────────────┼─────────────────────────┼──────────────────────────
    NOT A REAL MOVE  │  cannot happen          │  cannot happen
                     │                         │
   ──────────────────┴─────────────────────────┴──────────────────────────

   The moveset deletes the bottom row.
   Every battle anyone actually loses is lost in the top right.
```

## Three ways a legal move still loses the turn

1. **Nothing in the four fits.** Your whole team is Fighting-type and a Gengar switches in.
   Fighting does nothing to Ghost — 0×, not resisted, *nothing* — and you still have to press a
   button. The game gives you **Struggle** only when there is genuinely no move left; a decision
   schema with no null option does not even give you that, so it returns a high-confidence
   Earthquake instead.
2. **The moveset was built wrong.** Four attacks that overlap in type, no coverage for Steel, two
   moves that do nearly the same job. Jolteon cannot tell you its slots were badly chosen; it can
   only pick among them.
3. **The field is not what it looks like.** Zoroark's **Illusion** shows you the last Pokémon in
   the party. You read the matchup off a lie and choose correctly for a Pokémon that is not
   there. A closed move list does not improve your eyesight.

It is also worth saying that **being locked to a small set is not special to this Pokémon**. Any
holder of a **Choice Scarf** is locked to one move; that is an item, not a species. What is
actually interesting about a decision model is the honesty of its odds (question 202) and its
cost, not that it stays inside the rules.

## What to do about it

* **Carry the out.** Keep a null option and watch how often it fires. A team that never switches
  is not disciplined, it is stuck.
* **Read the percentage before you click.** A calibrated number exists so you can decline and
  pivot below a line, not so you can take the top move every time regardless.
* **Test against the opponents you will actually meet.** A flawless run against the Youngsters on
  Route 3 says nothing about the Elite Four.
* **Treat the moveset like a version.** Teach it a fifth thing and you have changed the meaning
  of every battle you already logged.

## What a Gym Leader is listening for

Whether you take the advertisement at its word. "Cannot use a move it does not know" is a fact
about the four slots. The strong answer names that guarantee exactly, says which loss it
prevents, and then says which loss it does not — and notices that Earthquake into Levitate is the
one that costs you the badge.

## Where this stands, September 2026

The phrasing is TypeSafe's, from Jev's launch, and has been repeated widely. The guarantee is
genuine and much narrower than the sentence sounds. Read it as "no illegal moves", which is what
the company itself says when it is being careful.
