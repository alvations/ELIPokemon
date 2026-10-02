---
id: "m010"
slug: adverse-drug-reactions
style: pokemon
category: pharmacology
difficulty: intermediate
question: "How are adverse drug reactions classified, why do dose-dependent and idiosyncratic reactions need different responses, and why do spontaneous reporting schemes exist despite their known biases?"
tags: [adverse-reactions, pharmacovigilance, idiosyncrasy, reporting, causality]
---

# Hyper Beam always makes you recharge. Rough Skin only ever happens to someone else.

There is a difference between a move that costs you something every time you use it properly, and
a move that costs you nothing in a thousand battles and then takes a bite out of you because of
who was standing opposite. And there is a third thing, different again: picking the wrong move.
The first two are the subject of this answer. The third is an error, it is investigated
differently, and conflating it with the other two is how the wrong thing gets fixed.

A classification is only worth learning if it changes what you do next. This one does, because its
first two rows demand opposite responses.

| Type | In the games | Amount-related? | Predictable from the move? | How often | What you do |
| --- | --- | --- | --- | --- | --- |
| A | **Hyper Beam**'s recharge turn | yes | yes | every time | use it at a better moment, not never |
| B | **Rough Skin** taking a sixteenth of your bar | no | no | rarely | stop making contact at all |
| C | **Macho Brace** halving Speed for the whole journey | by duration | partly | while held | reconsider how long you hold it |
| D | **Rare Candy** and the Effort Values you never got | sometimes | no | at the end | recognise it is attributable at all |
| E | **Substitute** breaking, **Light Screen** expiring | — | partly | on ending | plan the ending, do not just stop |
| F | **Struggle** | often | yes | common | find out what drained the PP |

**Type A is the move's own printed cost arriving where you did not want it.** **Hyper Beam** is
150 power and 5 PP and the user spends the next turn recharging. Every Pokémon, every time,
strictly because you used it. There is nothing mysterious about it, nothing host-specific, and it
is on the data sheet.

**Type B is not an extension of the move at all.** **Rough Skin** takes a sixteenth of the
*attacker's* maximum HP whenever a contact move connects. The move did not change. Nothing you
could read about the move would have told you. Only who you hit decided it.

**Pokérus** is the other face of type B, and the starker one: three values out of 65,536 at the
end of a battle, and nothing you did made it more or less likely. It is worth saying where that
example diverges — Pokérus is *good* for you, doubling what every battle teaches ever afterwards,
while an idiosyncratic reaction in a person is usually harm. The structure is the same and the
sign is not.

**The three axes worth asking about** are the amount, the timing and who it happened to. **Hyper
Beam** is pure amount: use it more, pay more, always. **Rare Candy** is pure timing: nothing
visible on the day, everything visible at level 100. **Rough Skin** is pure susceptibility: the
amount is irrelevant and the timing is immediate, and the only variable that matters is the
opponent. Naming the third axis out loud is what turns an unexplained bite into a question with a
findable answer.

## Why the first two rows need different answers

For **Hyper Beam** the response is quantitative. Use it when the recharge turn is affordable — to
finish a battle rather than to open one — or find out why you needed it, which usually means
something about the matchup rather than the move. Using it again at a better moment is perfectly
reasonable. The recharge was evidence about the timing, not about you.

For **Rough Skin** reducing the amount is not a smaller version of the right answer; it is the
wrong kind of answer. You stop making contact and reach for something that does not: the move list
is full of alternatives and the whole point is that the mechanism, not the magnitude, is what has
to change. Then three things follow that **Hyper Beam** never requires.

* **Write it down accurately rather than defensively.** There is an enormous difference between
  recording *this species carries Rough Skin* and recording *contact moves are dangerous*. The
  first costs you nothing. The second costs you a third of the move list for the rest of the game,
  on the strength of one encounter, and you will lose battles to that note that you would not have
  lost to the ability.
* **Decide about the class, not just the individual**, but only where there is a reason to. Rough
  Skin runs in a family; most contact moves against most Pokémon never do anything of the kind.
* **Look it up, because it is knowable.** An ability is a property of the species, printed and
  checkable before the battle rather than discovered during it. Susceptibility that can be read in
  advance is not idiosyncrasy any more; it is just information somebody did not consult.

And both need **working out whether it was really that at all**: did the bar drop on the turn
contact was made, did it stop when you switched to a non-contact move, did it come back when you
switched back, and does something else fit equally well? Because something does. A held **Rocky
Helmet** punishes contact in much the same way, a **Sandstorm** turn takes a slice of the bar for
entirely unrelated reasons, and the bar does not say which. The honest verdict is usually
*probably* rather than *certainly*, and a system built on it had better be designed for that.

## Why you keep a register that cannot measure anything

```
   THE RULE OF THREE -- arithmetic, not lore

   P(it has not happened in N battles)  =  (1 - p)^N   ≈   e^(-pN)

   for about a 95 % chance of having seen it at least once:
        pN ≥ 3,   so   N ≈ 3 / p        because e^(-3) ≈ 0.05

   event                                p                 battles needed
   ──────────────────────────────────────────────────────────────────────
   a critical hit at stage 0            1 / 16                      48
   Pokérus, rolled at the end
   of every battle                      3 / 65,536              65,536
   ──────────────────────────────────────────────────────────────────────

   3 ÷ (3/65,536) = 65,536 exactly, which is a tidy coincidence and also
   the entire point.

   A whole playthrough is a few hundred battles. Over 500:
        expected number of times      =  500 × 3/65,536  =  0.0229
        chance of seeing it at all    =  1 - e^(-0.0229)  ≈  2.3 %

   So ninety-eight playthroughs in a hundred finish having seen nothing.
   Not because Pokérus is not real -- it is three exact values out of 65,536,
   sitting in the code -- but because one player is not a big enough trial.
```

Which is why **Missingno.** matters more than it looks. The Kanto games contain index numbers with
no Pokémon assigned to them, and when asked for one the game builds something anyway. No manual
described it. No testing plan would have found it, because it is reached only by sequences nobody
was ever told to perform. It is real, it is in the software, and it carries a real harm:
encountering it is well known to corrupt the Hall of Fame record.

It was found because an enormous number of players, independently, reported the same anomaly. That
is a register with every defect a register can have.

* **Almost nobody reports.** For every player who wrote in there were many who shrugged, and
  nobody knows the ratio, and it was never the same ratio twice.
* **No denominator.** The reports count sightings, not attempts. A rise in reports could mean more
  glitches, more players, or more attention — and there is no way to tell from the reports which.
* **Attention multiplies reports without anything changing.** Once it was printed in magazines the
  reports multiplied, and the software had not moved a byte.
* **Reports fell away over the years** while the games were still being played, so the newest
  thing always looks like the most eventful thing, for reasons that are about people and not about
  software.
* **The spectacular gets written up and the dull does not**, the same sighting arrives by three
  routes, and confident wrong explanations get attached to perfectly real observations.

And it is kept anyway, because it does the one thing nothing else does: **it can find what nobody
was looking for.** Every method with a denominator — count how many players did X, count how many
saw Y — has to be told what to count before it can count it. The **Pokédex** is the same shape: it
records what somebody caught and registered, so a rare species is under-registered exactly as a
rare event is under-reported, and the register still tells you the species exists. It generates
the question. Something with a denominator answers it. A register that cannot produce a rate can
still be the only thing that notices there is something to count.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. Here it stops, and the
plain version is short.

An adverse drug reaction is harm done to a person by treatment. That is a different thing from an
illness getting worse, and the difference is not academic.

The person it happened to did nothing wrong. They took a medicine as intended and the medicine
harmed them, which is why the language of blame has no place in it and why any phrasing that
implies the patient failed is both inaccurate and corrosive. The reactions that are not
amount-related can be severe and can be fatal, and they arrive without warning in people who were
doing everything asked of them. None of that is a bar going down on a screen, and treating it as
one would be grotesque.

Three practical things follow. Reporting a suspected reaction is a professional duty rather than a
courtesy, and in many countries patients can report directly; the point of it is that it protects
somebody else. An allergy or intolerance recorded carelessly follows a person for life and can
cost them the best treatment for a later illness, so being precise at the moment of recording is
itself a safety intervention — which is the one place where the note-taking paragraph above is not
a metaphor at all. And stopping a medicine on the strength of something read in a revision answer
carries its own risk, sometimes a serious one; that decision belongs with the prescriber or
pharmacist who can see the whole record. Anyone who thinks a medicine may be harming them should
contact their prescriber or pharmacist, and in an emergency contact emergency services.

## What a Gym Leader is listening for

* Something happens to one Trainer in several thousand. Why would no amount of testing have found
  it?
* Why is using **Hyper Beam** more carefully the wrong response to **Rough Skin**?
* What is wrong with working out how common something is from how often it gets reported?
* Why is a note saying *contact moves are dangerous* worse than no note at all?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* Your national pharmacovigilance scheme's own guidance on what to report and how — in the United
  Kingdom the Yellow Card Scheme operated by the Medicines and Healthcare products Regulatory
  Agency; in the United States the Food and Drug Administration's MedWatch programme; in the
  European Union EudraVigilance at the European Medicines Agency. Reporting criteria differ
  between countries.
* The Uppsala Monitoring Centre, for the World Health Organization international drug monitoring
  programme and its causality assessment categories.
* Your national formulary's guidance on adverse reactions and on reporting — in the United Kingdom
  the British National Formulary, published by NICE with the pharmaceutical press.
* The summary of product characteristics, or the regulator-approved prescribing information, for
  the product in question, for its characterised adverse reactions and their frequency categories.
* A standard clinical pharmacology textbook for the Rawlins–Thompson classification and for the
  DoTS framework described by Aronson and Ferner, both of which the table above dramatises.
* Your national or local guidance on recording and verifying drug allergy.
* Your national pharmacogenomic testing guidance for any genetic association, including allele
  nomenclature, which should be checked rather than recalled.

The Pokémon figures are a different matter and were checked: Hyper Beam's 150 power, 5 PP and
recharge effect; Rough Skin costing the attacker a sixteenth of its maximum HP on contact moves
only; Pokérus being granted when a sixteen-bit random value matches one of exactly three values,
and permanently doubling effort-point yield; the critical hit chance of one in sixteen at the
lowest stage; Macho Brace halving Speed and doubling effort-point gain; effort points coming from
defeating Pokémon and not from a Rare Candy; Substitute costing a quarter of maximum HP and
failing at or below it; Light Screen lasting five turns; sandstorm costing a sixteenth of maximum
HP; and Struggle being what a Pokémon with no usable move does — all come from the public
decompilation of the Game Boy Advance games, read directly. The account of Missingno. is from the
Kanto games and from the long public record of it, not from the decompilation.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in it are the Pokémon ones and the rule-of-three
arithmetic**, which is statistics rather than clinical data; no frequency, dose or threshold in
either half of this answer describes any real drug. Reporting criteria, allergy documentation
standards and pharmacogenomic testing practice differ between countries. Nothing here should be
used to make a decision about anyone's treatment, including your own. Anyone who thinks a medicine
may be harming them should contact their own prescriber or pharmacist, and in an emergency contact
emergency services.

## Where this stands, October 2026

The classifications and the arithmetic do not date, and the game mechanics cited are fixed in
released software. The surveillance landscape does date: schemes get renamed and merged, patient
reporting has expanded in several countries and not others, additional monitoring lists change
continuously, and pharmacogenomic testing recommendations move faster than most of pharmacology.
Check your own regulator's current guidance.
