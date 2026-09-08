---
id: "186"
slug: terminology-mining
style: pokemon
category: translation
difficulty: intermediate
question: "How do you build a bilingual glossary without writing it by hand?"
tags: [term-extraction, bilingual-alignment, validation, glossary-maintenance, precision]
---

# Nobody hands you the name list

Question 133 assumed the list of official names already existed. Usually it does not — or it is a
sheet somebody kept up to date until three regions ago.

You need to know that **Poké Ball**, **Great Ball**, **Ultra Ball** and **Master Ball** are four
distinct things with four fixed names in every region; that **Full Restore** is not **Full Heal**;
that **TM26** is one specific TM. Somewhere in your archive, every one of those pairings already
exists. Nobody has written them down.

You can build the list out of that archive. There is exactly one hard constraint, and everything
below follows from it:

⚠️ **A wrong entry is worse than a missing one — because a wrong entry gets *enforced*.** A name
that is absent gets translated a bit inconsistently. A name that is present and wrong gets stamped
onto four hundred pages, correctly, every time.

## The pipeline 🏭

```
   1. 🔍 FIND THE CANDIDATE NAMES on one side
        things shaped like names — and, crucially, things that are common HERE
        and rare in ordinary writing

   2. 🔗 PAIR THEM UP with the other side
        for each one, find what it became in the aligned entries

   3. 🧹 THROW MOST OF THEM OUT
        too rare, too uncertain, rendered differently every time

   4. 👤 A PERSON CHECKS THEM            ← the step nobody gets to skip
        accept, reject, or correct. THIS is the deliverable.

   5. 🗓️ AND SOMEBODY OWNS IT afterwards
```

## Where each step goes wrong 🚨

* **📢 Step one finds boilerplate, not names.** *"Please select"*, *"in accordance with"*. Counting
  how often something appears finds the phrases your documents are made of. 📌 What separates a
  **name** from a common phrase is being **common here and rare everywhere else** — the way
  **Leftovers** is a word you meet constantly in competitive writing and almost never outside it.
* **🎯 Step two misses exactly the entries you wanted.** A name that becomes **several words** in the
  other region. One that becomes a completely different kind of word. One that is **correctly left
  alone** — **Poké Ball**, untouched, in every region. ⚠️ Those are the valuable ones, and automatic
  pairing is systematically worst on all three.
* **🎲 And where your archive was inconsistent, you get a coin flip.** If the **Poké Ball** was
  rendered three ways across three projects (question 161), the miner picks **the most common one**
  — which may be the one your style guide **bans**.
* **📚 Over-collecting is the default failure.** Five thousand entries of which twelve hundred are
  wrong is **far worse** than three hundred correct ones, because question 133's machinery will
  faithfully stamp **Full Heal** onto four hundred pages that meant **Full Restore**, and never
  once hesitate.

📌 **So tune it to catch fewer and be right**, not to catch everything. Fewer candidates, higher
bar, and a person in front of them.

## Making the checking affordable 👤

Expert time is the bottleneck, so spend it where it counts:

* **📈 Sort by how much it matters**: how often the name actually appears × how bad it would be to
  get wrong. **Poké Ball** appears on every page and **Lucky Punch** appears twice — and confusing
  **Full Restore** with **Full Heal** costs somebody the match. Checking the top two hundred covers
  most of the benefit.
* **📄 Show three real sentences with it in place.** ⚠️ Validating a bare pair of words is guesswork
  even for somebody who knows the subject — the same reason question 156 keeps the sentence around
  its placeholder.
* **🔀 Offer the alternatives you found**, so the expert is **choosing** rather than saying yes or no
  to whichever one you happened to surface first.
* **🚫 And write down what they rejected.** A **do-not-use** list is worth as much as the approved
  one (question 133), and it is thrown away almost every time.

## Where name lists die 🪦

Every entry needs **an owner, a date, and a status.** Names get added when things change, retired
when things are renamed, and the list has to be **versioned alongside the content** — so that a
translation can be traced back to the rules that were actually in force when somebody made it.

⚠️ A list without that history rots into exactly the same untrustworthy state as an abandoned
Pokédex (question 161): full, impressive, and impossible to clean.
