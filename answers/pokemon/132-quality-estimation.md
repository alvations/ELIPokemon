---
id: "132"
slug: quality-estimation
style: pokemon
category: translation
difficulty: advanced
question: "How do you tell whether a translation is good without a reference?"
tags: [quality-estimation, comet-qe, calibration, routing, critical-errors, mqm]
---

# Nurse Joy has no reference Pokémon to compare against

Every scoring scheme in question 129 needs somebody's model answer to compare with. Out in the
world there is no model answer — **that is the entire reason you needed the translation.**

So this is **Nurse Joy**'s job, not a judge's. A Pokémon walks into the **Pokémon Center**, and she
and her **Chansey** have to decide, right there, from the Pokémon in front of them: **is this one
fit to go back out?**

And notice that the decision is not a number. It is *which shelf you reach for*. A **Potion** and a
**Revive** are not two points on one scale — one is for a Pokémon that is scuffed, the other is for
a Pokémon that has already fainted, and no amount of Potion has ever substituted for the other.

## Why it is worth doing 🏥

This is not paperwork. It is triage, and triage is what makes the whole operation affordable.

```
   the source ─► the machine ─► a translation ─► 🏥 Nurse Joy looks it over
                                                        │
                        ┌───────────────────────────────┼───────────────────────────────┐
                     ✅ fine                        ⚠️ scuffed                      🚨 not fit
                        │                              │                               │
                 send it straight out          hand it to a person             send it to a stronger
                                                 to patch up                    Trainer — or hold it
                                                                                back entirely
```

📌 **The middle lane is where the money is.** Having a person check every translation is ruinously
expensive. Having a person check the one-in-five that needs it is a business. And the right-hand
lane is why anyone does this at all in medicine or law: some things must not go out.

## How she actually judges 🩺

* **🩹 An overall verdict.** Look at the source and the translation together and produce one number.
  This is the standard tool: something taught by watching thousands of translations that people
  graded, then asked to grade a fresh one with no answer sheet.
* **📍 Or point at where it hurts.** Mark the specific words that are wrong, not just "this one is
  unwell". Far harder to teach, and **far** more useful to the person doing the repair — they want
  to know where to look, not that something, somewhere, is off.
* **🧑‍🏫 Or ask a very experienced Trainer** to read it and list what is wrong with it. Works
  surprisingly well. Inherits every problem from question 038 — it prefers its own phrasing, it
  favours whatever it read first — plus one that stings here: it is **weakest on exactly the rare
  languages you most needed help with.**
* **🌀 And the tempting one: just ask the Pokémon how it feels.** Free. Almost worthless. A Pokémon
  under **Confusion** will tell you with total conviction that it is about to land a perfect hit,
  and then strike itself. ⚠️ **A confident translation is not a correct one**, and the fluent,
  self-assured, entirely invented sentence is precisely the case you built the whole system to
  catch.

## "Fine" has to mean the same thing everywhere 📏

A Nurse Joy who ranks Pokémon perfectly but whose *"fine"* means something different in **Cerulean
City** than it does in **Blackthorn City** cannot be used to set a rule. The **Audino** on the desk
in one town and the **Blissey** on the desk in the other have to agree on where the line is, or the
line is not a line.

* 🎚️ **Set the bar separately for each language and each subject.** One global bar will wave
  through the pairs it flatters and drag every good translation in another pair back to the ward.
* 🔄 **Re-check the bar whenever the machine changes.** She was calibrated against the old machine's
  output. New machine, new distribution, stale bar.
* 📊 **And report what actually happened at the bar you chose** — of everything you sent straight
  out, how much should not have gone. That is the question the Centre is judged on. "How well she
  ranks Pokémon in general" does not answer it.

## The rare, terrible ones are their own job 🚨

A dropped **not**. A dosage doubled. One Trainer's name swapped for another's.

These are rare — so rare they barely register in any average — and **they are the whole reason
anyone deployed a triage in the first place.**

So do not treat them as the bad tail of a general score. Treat them as their own question, with
their own target: *what fraction of dropped negations does she catch?* Build the test deliberately
— flip the negations, swap the numbers, swap the names, delete a whole clause — and measure the
catch rate directly.

📌 A Nurse Joy who is broadly excellent and catches **two in five** dropped negations is not fit to
run a hospital, and her broadly-excellent number will never once tell you that.

The shape to keep in mind is a **Focus Sash**: a Pokémon left standing on exactly 1 HP is, by any
reasonable summary, *alive*. It is also one hit — one turn of **Sandstorm**, one tick of **Toxic** —
away from gone. A triage that reports the average is reporting that it is standing.

## What she is bad at 🩻

* **✨ She over-rewards a Pokémon that looks well.** A translation that reads smoothly beats a
  clumsy one that is actually right — the same way a Pokémon fresh from being groomed and brushed
  looks magnificent and may be **badly poisoned** underneath, where **Toxic** takes a little more
  each turn and shows nothing at all on the first one. Glossy is not healthy.
* **📏 Very short ones fool her.** A single word, a menu label, a name. Not enough to go on.
* **👻 Wholesale invention slips past** unless she was specifically taught to look for it.
* **🌏 And the rarest species get the worst care**, because she has seen the fewest of them — which
  is, once again, exactly backwards from where the need is.
