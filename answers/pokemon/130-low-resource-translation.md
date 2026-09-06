---
id: "130"
slug: low-resource-translation
style: pokemon
category: translation
difficulty: advanced
question: "How do you translate a language with almost no parallel data?"
tags: [low-resource, back-translation, transfer, pivot, bitext-mining, flores]
---

# Teaching a move nobody in the family can learn

Your Pokémon needs a move. It does not learn it by levelling up. There is no **TM** for it. No
**Move Tutor** in any town will teach it.

This is the low-resource problem exactly. Not "the data is bad" — **the data does not exist**, and
every technique below is a way of manufacturing a lesson nobody ever wrote down.

## 1. Find a relative who already knows it 🥚

The highest-value move, and it is the oldest trick Trainers have. **Egg Groups.** If some other
species in the same Egg Group knows the move, breed for it and the child is born already knowing
what its parent knew.

That is transfer from a related language. Spanish carries you a long way into Galician. Indonesian
carries you a long way into Malay. **Not because someone wrote a phrasebook — because the families
overlap**, and a Pokémon born into the right Egg Group inherits far more than a stranger could ever
be taught.

⚠️ But the family has to actually be shared. A relative who **writes in a completely different
alphabet** (question 106) passes on much less than the family tree suggests — the kinship is real
and the surface is unrecognisable. Rewriting both into the same script first (question 109) can
recover a startling amount of it.

## 2. When there is no partner at all, breed with Ditto 🫧

Here is the technique that carries the whole field, and Ditto is the exact analogy for it.

You have a Pokémon and **no compatible partner anywhere.** So you breed it with a **Ditto** —
which is not really a partner, it is a *copy of one*, manufactured on the spot.

📌 And this is the crucial part: **the egg does not hatch into a Ditto.** It hatches into a genuine,
real member of the other parent's species. The fake half was only ever the *input*. What comes out
is real.

```
   you have:  no pairs at all — but plenty of genuine writing in the rare language

   step 1   real rare-language text ──[ run the machine BACKWARDS ]──►  invented source text
   step 2   now drill on ( invented source , REAL rare-language target )
                              ▲                        ▲
                        the Ditto side          the genuine offspring
                        — made up, and fine     — what it actually learns to produce
   step 3   the machine is better now. Make better Dittos. Go again.
```

The errors all land on the side the Pokémon only has to *understand*. The side it learns to
**produce** is real human writing, every time.

🚫 Do it the other way round — drill it on sentences *it* produced — and you have a Pokémon that
only ever spars with itself. It gets very good at its own bad habits and nothing else.

## 3. Go looking for pairs that already exist 🔎

Nobody wrote a parallel corpus. But two regions have both written up **the same species** in their
own Pokédexes, in their own words, without ever coordinating. Line those entries up and you have
pairs that nobody made on purpose.

Match them by meaning rather than by wording, keep only the confident matches, and throw out
anything where the two entries turn out to be about different Pokémon. ⚠️ The catch is circular:
the matching tool is weakest for exactly the rare languages you are mining for.

## 4. Trade through a third Trainer 🔁

You and the other Trainer cannot connect directly, so you both connect to somebody who can reach
you both, and pass the Pokémon along in two hops.

It always works and it always costs. Anything the middle Trainer's language cannot carry —
politeness levels, whether the speaker saw it themselves, **Nidoran♀ versus Nidoran♂** — is
**gone at the halfway point** and no amount of care in the second hop brings it back.

## 5. The rest of the kit 🧰

* 💿 **A disc per language** (question 110) — new capacity for the new language, everything else
  untouched.
* 🔤 **Teach it the alphabet first.** If the machine shreds the language into unrecognisable
  fragments before it starts (questions 102, 112), fixing *that* beats every clever idea
  downstream, and people skip it because it is boring.
* 📖 **Hand it a dictionary and a page of grammar.** For a language with almost nothing at all, a
  strong general Pokédex reading a phrasebook can beat a system trained from scratch on the scraps.

## And then: how would you even know it worked? 🧭

This is the hardest part and it is the part that gets skipped.

There is a standard test set covering a great many languages, and it is genuinely useful. It is
also one narrow style of writing, it is all over the web where models train, and **a good score on
it does not mean a single speaker can use the thing.**

👥 **Ask the region's own Trainers.** A system that scores beautifully and produces sentences no
native speaker would ever write is common, and no scoring scheme will ever tell you. Ask them what
they actually want translated, too — it is very often not the news.
