---
id: "m009"
slug: drug-interactions-mechanisms
style: pokemon
category: pharmacology
difficulty: advanced
question: "Compare enzyme induction and enzyme inhibition mechanistically, and explain why protein-binding displacement usually matters less than it sounds."
tags: [interactions, induction, inhibition, protein-binding, cytochrome-p450]
---

# An Ability stops the moment it leaves. Drizzle keeps raining after it has gone.

Three kinds of interference cover almost everything, and the way to hold them apart is **when they
start and when they stop**, not which mechanic has which name.

* An **Ability** interferes only while its owner is standing there. **Pressure** doubles what
  every move used against it costs in PP; **Air Lock** switches the weather's effects off
  entirely. Both stop the instant the Pokémon leaves. Nothing was destroyed; something was
  occupied.
* **Drizzle** is the other shape. In the Game Boy Advance games it sets rain with **no duration at
  all** — it goes on raining after the Pokémon that set it has been switched out, and it takes
  another weather move to stop it. The cause has gone and the effect has not.
* And some interference needs no mechanism in common at all: **Spikes**, **Sandstorm** and **Leech
  Seed** take the same bar down by three routes that never touch one another.

Plus the one that looks dramatic and usually is not: **Whirlwind**, dragging a Pokémon off the
field. It changes which of six is standing there and it changes nothing about the six.

## Pressure: on while present, off when gone

**Pressure** does not destroy a move. It makes each use cost two PP instead of one, for as long as
its owner is on the field. **Aerodactyl** carries it; so does the Pokémon your plan was built
around not meeting.

```
   THUNDERBOLT, 15 PP as printed

   normally          15 uses
   against Pressure  uses 1-7 cost 2 each = 14 PP spent, 1 left
                     use 8 spends the last point (the extra deduction is skipped
                     at zero, which the games check for explicitly)
                     ────────────────────────────────────────────────────────
                     8 USES, not 15

   with three PP Ups:  15 + (15 × 20 × 3)/100  =  15 + 9  =  24 PP
   normally          24 uses
   against Pressure  12 uses

   Raising the maximum buys back uses. It does not change the ratio, and it does not
   change the moment you find out: you reach for the ninth Thunderbolt, and what comes
   out is STRUGGLE.
```

And the consequence is not immediate even though the interference is. The supply drains at the new
rate, and the failure arrives several turns after the Pokémon with Pressure walked in. **Air
Lock** makes the same point in the opposite direction: while **Rayquaza** is out, a sandstorm does
no damage and rain boosts nothing, and the moment it switches out all of that resumes exactly
where it was. The weather was never gone. It was overruled.

**Knock Off is the asymmetric one.** One action, and the target's held item is gone for the rest
of the battle. The Pokémon that used it can leave immediately; the item does not come back. Fast
to start, and it does not stop — which is the shape of the next section, arriving from the wrong
family.

## Drizzle and Toxic: slow to arrive, slow to leave

**Toxic** is the gradual one. Badly poisoned damage is a sixteenth of maximum HP multiplied by a
counter that rises every turn it stays in.

```
   400 maximum HP, so a sixteenth is 25

   turn            1     2     3     4     5     6
   counter         1     2     3     4     5     6
   damage         25    50    75   100   125   150
   running total  25    75   150   250   375   525   ◄ past 400 on turn six

   Turn one is a rounding error. Turn six is the battle. Nothing about the poison
   changed; the amount of it that has built up did.
```

**Future Sight** is the one that outlasts its cause, and the games are unusually explicit about
it. The damage is calculated **at the moment the move is used** and stored; a counter is set to
three and ticks down at the end of each turn, so it lands two turns later. It lands on whatever is
standing in that slot when it arrives — which need not be the Pokémon that was there — and the
user may have been switched out a turn and a half earlier. You cannot stop it by leaving. You
could not have stopped it by leaving.

**Drizzle** is the one that does not wear off at all. In the Game Boy Advance games it sets
permanent rain: no counter, no expiry. Switch the Pokémon out and it is still raining. **Sunny
Day** will end it, and **Air Lock** will overrule it, but nothing about time will.

**And the direction is not always worse for you.** The same rain that halves every Fire move
multiplies every Water move by 1.5 and makes **Thunder** unable to miss. Harsh sunlight reverses
all three — Fire up, Water down, and Thunder's accuracy cut to 50 — and it lets **Solar Beam**
fire on the turn it is chosen instead of charging for one. One induced condition, consequences
pointing in several different directions at once. The rule is about what the weather does to the
*rate*, not about whether you like the result.

```
   WHEN EACH ONE IS AT FULL SIZE

   ABILITY (Pressure, Air Lock)
       starts   the turn it walks in                         immediately
       then     the supply drains at the new rate            several turns
       stops    the turn it walks out                        immediately
       ─────────────────────────────────────────────────────────────────────────
   KNOCK OFF (one action, permanent loss)
       starts   the turn it is used                          immediately
       stops    it does not                                  never, this battle
       ─────────────────────────────────────────────────────────────────────────
   TOXIC, DRIZZLE (built up, or simply left behind)
       starts   turn by turn, as the counter climbs          gradual
       stops    Toxic only when cured; rain only when another
                weather move replaces it                     not by waiting
       ─────────────────────────────────────────────────────────────────────────
   SPIKES + SANDSTORM + LEECH SEED (no shared mechanism)
       starts   as soon as both are in play                  as fast as the faster
       stops    as soon as either is gone                    as fast as the faster

   The Knock Off row is the one worth remembering: it behaves like an Ability when it
   starts and like Drizzle when it stops.
```

## Whirlwind, and why dragging someone out disappoints

```
   A team of six. One on the field, five in reserve.
   The share standing there is 1 in 6, and the FORMAT fixed that, not the battle.

   Whirlwind drags out whoever is in front.
        the six                 unchanged
        the share on the field  still 1 in 6
        next turn               you can send the same one straight back

   So what does it cost?

        on a clean field                              0
        over one layer of Spikes (maxHP / 8)          50 on every entry

   400 maximum HP, dragged out and brought back three times:
        3 × 50  =  150  =  more than a third of the bar, and none of it from Whirlwind

   The dragging was free. THE TAX ON THE DOORWAY WAS NOT.
```

So the lasting consequence of being dragged out is usually a misleading impression of chaos rather
than a changed position, and the classic error is to respond to the rearrangement itself — to burn
turns re-establishing exactly what you had — which does change the position, for the worse.

Being dragged out *does* matter in three situations, and they are the real ones. Transiently, in
the turn or two before you can rotate back. When the doorway is taxed, as above, because then the
rotation has a price and the price compounds. And when you have **nobody left to rotate to**, at
which point it stops being a rearrangement and becomes the whole battle. **Spikes** plus
**Whirlwind** is the pairing always cited for exactly that reason — two mechanics at once, and the
Whirlwind is the less important of them.

## Interference with nothing in common

**Spikes**, **Sandstorm** and **Leech Seed** share no mechanism whatsoever. They share a bar.

```
   400 maximum HP, grounded, not Rock, Ground or Steel, and seeded

   on entry      Spikes, one layer      400 / 8   =  50
   every turn    Sandstorm              400 / 16  =  25
   every turn    Leech Seed             400 / 8   =  50
                 ───────────────────────────────────────
                 per turn                            75

   turn           1     2     3     4     5
   taken         125   200   275   350   425   ◄ past 400 on turn five

   No part of that interacts with any other part. They add because they arrive at the
   same place, and nothing you could measure about any one of them would predict it.
```

And the antagonistic version, in the same weather: a Pokémon with **Sand Veil** in a sandstorm
takes no sandstorm damage *and* has incoming accuracy cut, so one condition helps it twice while
hurting everything else. Opposite signs, same cause, decided by who is standing in it.

**Finally, the interaction the brief calls for by name: one thing changing what another thing
does.** A **Thick Club** doubles Attack for **Cubone** and **Marowak** and is an inert rock in the
hands of anything else. A **Light Ball** doubles **Pikachu**'s Special Attack and nobody else's.
**Metal Powder** doubles **Ditto**'s Defence only. **Deep Sea Tooth** and **Deep Sea Scale** work
for **Clamperl** and for nothing in the game besides. Same item, different body, completely
different effect or none at all — and no amount of studying the item tells you that.

The sharpest one is an Ability rewriting a status condition. A burn normally halves the physical
damage you deal. The damage calculation checks the attacker's ability and **skips the halving
entirely if that ability is Guts** — which also raises Attack while statused. So a burn is a
penalty in one Pokémon and a bonus in another, and the burn did not change.

## Where the metaphor stops

Everything above is mechanism, and mechanism is what the analogy is for. Here it stops.

An interaction that harms someone was not bad luck. Two medicines were prescribed, dispensed or
bought, and the combination was not caught — which makes the harm iatrogenic, caused by the care
rather than by the illness. The person who comes to harm did nothing wrong, and the contributing
factors are usually structural: more medicines than one prescriber can hold in mind, care split
across services, one drug started by one team and another by a second, and a record that is
complete nowhere.

Two things follow that matter more than any mechanic named above. Harm suspected to come from an
interaction is a suspected adverse drug reaction and is reportable through the national scheme, by
professionals and in many countries by patients directly; reporting it is how the next person is
protected. And stopping a medicine because of something read in a revision answer carries its own
risk, sometimes a serious one. That decision belongs with the prescriber or pharmacist who can see
the whole list, and anyone worried about a combination they are taking should raise it with them.

## What a Gym Leader is listening for

* The failure shows up four turns after a switch. **Pressure**, or something that was already
  there?
* Why does **Knock Off** stop behaving like an Ability the moment the user leaves?
* The team looks scrambled and the position is unchanged. What is the most likely explanation?
* Why would no measurement of **Sandstorm** have predicted the turn-five faint above?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* Your national formulary's appendix on interactions, and the monograph for each drug the
  technical twin of this answer names — in the United Kingdom the British National Formulary,
  published by NICE with the pharmaceutical press; elsewhere the equivalent national formulary.
  Authority for whether an interaction is clinically significant and what is done about it.
* A dedicated drug interactions reference maintained by a recognised body and used in your own
  institution, for the magnitude of any individual interaction. Magnitudes are deliberately absent
  from both halves of this answer because they cannot be generalised.
* The summary of product characteristics, or the regulator-approved prescribing information, for
  each product, which lists the interactions the licence holder has characterised.
* Your national medicines regulator's guidance on drug interaction studies, for how inducer and
  inhibitor classifications are assigned. The thresholds are regulatory and differ by
  jurisdiction.
* A standard clinical pharmacology textbook for the nuclear receptor pathways and for the
  restrictive-clearance argument about protein-binding displacement.

The Pokémon figures are a different matter and were checked: Thunderbolt's 15 PP and the PP Up
formula of twenty per cent of base per use to a maximum of three; Pressure deducting one extra PP
and skipping that deduction at zero; Struggle being what a Pokémon with no usable move does;
Drizzle setting permanent rain in these games; Air Lock and Cloud Nine negating weather effects;
rain halving Fire and multiplying Water by 1.5; Thunder being unable to miss in rain and dropping
to 50 accuracy in sun; Solar Beam skipping its charge turn in sun and being halved in any other
weather; badly poisoned damage being a sixteenth of maximum HP times a rising counter; Future
Sight storing its damage on use and landing on the third end-of-turn; one layer of Spikes costing
an eighth of maximum HP; sandstorm costing a sixteenth and sparing Rock, Ground, Steel and Sand
Veil; Leech Seed costing an eighth; the species locks on Thick Club, Light Ball, Metal Powder,
Deep Sea Tooth and Deep Sea Scale; and the damage calculation skipping the burn penalty for Guts —
all come from the public decompilation of the Game Boy Advance games, read directly.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in it are the Pokémon ones.** No interaction
magnitude appears in either half, deliberately, and the binding percentages in the technical twin
are illustrative figures invented to show arithmetic. Whether any given combination of medicines
is acceptable is a decision for someone with the full record in front of them. Practice differs
between countries, formularies and institutions. Nothing here should be used to make a decision
about anyone's treatment, including your own. Anyone with a question about a combination of
medicines they are taking should raise it with their own prescriber or pharmacist.

## Where this stands, October 2026

The mechanisms and their time courses are stable, and the game mechanics cited are fixed in
released software — though the series has changed several of them between generations, permanent
weather from Drizzle among them, and this answer names the version it is describing. What moves on
the clinical side is the catalogue: which drugs count as strong, moderate or weak inducers and
inhibitors, which interactions are flagged, and what the recommended management is. That changes
with every formulary edition and differs between countries. Check the current interactions
reference.
