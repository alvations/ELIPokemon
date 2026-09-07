---
id: "133"
slug: terminology-glossary-enforcement
style: pokemon
category: translation
difficulty: intermediate
question: "How do you make a translation system use the right terminology every time?"
tags: [terminology, glossary, constrained-decoding, do-not-translate, translation-memory]
---

# There is exactly one right name for a Pikachu

Most of a translated Pokédex entry can be worded a dozen ways and all of them are fine. *"It stores
electricity in its cheeks"* or *"electricity gathers in its cheek pouches"* — pick either.

**The species name is not like that.** Every region has one official name for **Pikachu**, and it
is the name, and there is no second-best option. Same for **Poké Ball**. Same for
**Thunderbolt**. Same for **Leftovers**. Get the entry beautiful and the name wrong and you have
not produced a slightly worse Pokédex — you have produced a **wrong** one.

## Why the machine will not do this by itself 🤷

A translator produces whatever wording is *most likely*. Your name list is a **decision somebody
made**, often against what is most likely. The machine was never in the room.

⚠️ And it will be inconsistent about it. The same item named three different ways across one
Pokédex, because each entry was written on its own and all three sounded fine in isolation
(question 131).

## Four ways to make it comply, gentlest first 🔧

```
   GENTLE ──────────────────────────────────────────────────────► ABSOLUTE

   hand it the        drill it until          force the name       swap the name out
   name list          the names are habit     into the sentence    for a blank, fill in later
       │                     │                        │                      │
   easy. mostly       durable, but cannot      the name WILL        guaranteed — and now the
   works. quietly     learn a name added       appear. the          grammar around the blank
   slips under load   yesterday                sentence may         is entirely your problem
                                               not survive
```

📌 **Hand it only the names that appear in this entry.** Dumping the whole Pokédex's worth of names
into every request costs a fortune and drowns out the ones that matter. Look up which species and
items this entry actually mentions, and pass those.

## The trap: the name has to bend, and a forced name will not 🪤

A name list stores the plain form. Sentences almost never want the plain form.

```
   the list says:   this item is called  ⟨Leftovers⟩

   forced in flat:  "... holding Leftovers ..."            ✓ happens to fit
                    "... the effect of Leftovers slow ..." ✗ the sentence needed a
                                                              different ending on the word

   the name is present. the sentence is broken.
```

In regions whose words change shape constantly (question 113) this is not an occasional annoyance,
it is **every sentence**. Three real answers: store the *bent* forms in the list as well as the
plain one; accept any member of the family as counting; or stop forcing it during writing and
**check compliance afterwards** instead.

## Some things must not be translated at all 🚫

**Poké Ball**. **TM42**. `{count}`. A Trainer's name. A route number. These pass through
untouched, and the classic failure is a helpful machine translating a brand name because it looked
like ordinary words.

The **Name Rater** in Lavender Town is the right model for this: he will happily rename a Pokémon
you caught, and he will not touch one you traded for. Some names are yours to change. Some belong
to somebody else.

## Check whether somebody already did this 📚

Before writing a single new sentence: **has this entry been translated before?**

A previously approved entry is free, correct, and guaranteed consistent with everything else that
used it. A *nearly* matching one is nearly as good — put it in front of the translator as an
example and compliance jumps without any machinery at all.

This is completely standard practice among people who translate for a living, and it is very often
missing from systems built by people who train models for a living.

## Counting whether it worked 🧮

**Of the names that appeared in the source, how many came out right?** Report that number **on its
own**, never folded into the general quality score.

⚠️ Because here is what happens if you fold it in: a new machine reads more smoothly, scores a
point higher overall, and has quietly started calling a **Poké Ball** three different things. The
general score says the machine improved. It did not.

Also count how often the same item keeps the same name from entry one to entry four hundred, and
keep a small pile of deliberately awkward sentences — the ones where the name lands somewhere the
grammar will fight it — because those are the ones that will break, and an average over easy
sentences will never show you.
