---
id: "224"
slug: muon-optimizer-and-training-stability
style: pokemon
category: open-weights
difficulty: advanced
question: "A lab trains its trillion-parameter models with Muon instead of AdamW. What should a practitioner take from that?"
tags: [optimizers, muon, training-stability, pretraining, attention]
---

# Every battle gives you something. What it gives you is a choice.

Most Trainers treat **Effort Values** as weather. You walk **Route 1**, you win, numbers happen.
They do not. **EVs** are the rule by which a battle is converted into stat, and the rule has
settings — a held item, an opponent chosen on purpose, a bottle bought at the
**Celadon Department Store**. Changing the rule changes how much stat the same number of battles
buys you, and that is the whole argument.

The arithmetic underneath: four **EVs** are one point of a stat at level 100. A stat caps at 252
**EVs**, and the whole Pokémon caps at 510. So there is a fixed budget, a fixed exchange rate, and
a very wide gap between spending it well and spending it at all.

## What deliberate training does differently

The default is per-battle and undirected. Beat whatever walks into you on **Route 1** and the
yield lands wherever the opponent happened to put it: a bit of Attack from a **Machop**, a bit of
Defence from a **Geodude**, some Special Attack from a **Gastly**, some Special Defence from a
**Tentacool**. Every battle moves something. Almost none of it moves what you meant.

The deliberate version fixes the direction before the battle starts. Hold a **Power Bracer** and
every battle adds a fixed block of Attack **EVs** on top of whatever the opponent yields — eight
of them, from **Alola** onward, four before that. Hold a **Macho Brace** instead and the whole
yield doubles. Pick the opponent to match: a route of **Starly** for Speed, a cave of **Geodude**
for Defence. Same number of battles. Far more of the 510 lands where you aimed it.

The claim worth quoting is the ratio: **roughly half the battles for the same finished Pokémon.**
And the honest caveat is that the comparison depends entirely on how well the undirected Trainer
was doing — someone who was already picking their routes carefully is not getting a free doubling.

## The cost the efficiency bought

**Both the Macho Brace and every Power item halve the holder's Speed while it is held.** That is
not a footnote. A Pokémon trained this way is slower than it looks for the entire time it is being
trained, loses turn order it would otherwise win, and has to have the item taken off before it is
worth anything in a real fight. The efficiency is real and it is paid for every single turn.

And the two obvious ways out are both closed. Fixing it later costs the turns you were saving. And
you cannot simply hold something steadying instead — **a Pokémon holds one item**, and the slot is
already spent. No **Leftovers**, no **Choice Band**. The way the Pokémon is built removed the
standard answer, so the answer had to come from somewhere else.

## The cap the game applies itself

```
   the runaway that never happens:

   Swords Dance  +2      ██                Attack stage
   Swords Dance  +4      ████
   Swords Dance  +6      ██████   ◄── the ceiling
   Swords Dance  +6      ██████   "Attack won't go higher!"  (PP still spent)

   Belly Drum    +6      ██████   ◄── straight to the ceiling, for half of max HP

   stage
     +6 ┤──────────────────────────────────────  hard wall, every game, every stat
      0 ┤╭─╯
     -6 ┤──────────────────────────────────────  and the same wall downward
        └──────────────────────────────────────►  turns
```

**Swords Dance** raises Attack two stages. Use it three times and you are at +6, and the fourth
use fails outright — the move happens, the PP goes, the stat does not move. **Belly Drum** jumps
straight to +6 and charges half the Pokémon's maximum HP for the privilege. **Nasty Plot**,
**Calm Mind** and **Bulk Up** all run into the same wall.

Three things make that wall good design rather than a nuisance:

1. **It belongs to the individual, not the team.** The Pokémon at +6 is capped; its partner across
   the field keeps every stage it had. Nothing healthy is punished for one runaway.
2. **It does not undo the turn.** The move still resolves, the PP is still spent. The ceiling is a
   limit on where you end up, not a rewind of how you got there.
3. **It mostly stops mattering.** Only a setup sweeper ever reaches +6, and only in the opening
   turns. For the rest of the battle the wall is there and touches nothing.

The same shape appears one layer down. **Hyper Training** with a **Bottle Cap** raises what a stat
*behaves* as, right to the top, while leaving the **IVs** underneath exactly as they were — a
correction applied at the surface, not a rewrite of the Pokémon.

## What a Trainer should take from this

* **The training rule is a real choice.** It was treated as scenery for years. It is not.
* **Every efficiency comes attached to a cost you were not watching.** Halved Speed is the one
  here. Watch the number the shortcut moves, not only the number it improves.
* **What you can do depends on what you are holding.** One item slot. Pick the fix and you have
  spent it.
* **Do not carry a pretraining result into a quick top-up.** Ten **Protein** and ten **Carbos**
  bought at the counter move the same stat, and none of the above applies to them. And a
  **Rare Candy** raises the level while giving no **EVs** at all — the fastest way up is not the
  same thing as the best way up.

## What a Gym Leader is listening for

That you can say in one line what the rule actually changes — where the yield lands — and then
name its price in the same breath rather than quoting the doubling as if it were free. The
strongest
answers volunteer that the ceiling is per Pokémon and that it stops binding once setup is over,
because that is the part you only know from having used it.

## Where this stands, September 2026

The caps, the item effects and the ceiling are from the games and do not rot. What does rot is any
particular claim about how much a training rule buys: it depends on who was being compared and how
carefully they were already playing. Re-check that the doubling survives against a Trainer who was
choosing their routes properly in the first place. That is the comparison most likely to move.
