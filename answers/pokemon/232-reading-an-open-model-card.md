---
id: "232"
slug: reading-an-open-model-card
style: pokemon
category: open-weights
difficulty: intermediate
question: "You have downloaded an open model's weights. What do you read before you try to serve it?"
tags: [model-card, licensing, tokenizer, quantisation, vllm]
---

# The trade came through. That is step one of about seven.

The gap between "it is in my box" and "it is on my team at **Regulation G**" is five screens and
one compatibility question, and every one of them has ruined somebody's weekend. Read them in
this order, because each one decides whether the next one matters at all.

```
   the summary, page by page
   ├── species, Ability, Nature  ← read first. decides everything below it.
   ├── level, the six stats      ← what it actually weighs
   ├── the four moves            ← must be moves it can legally know
   ├── the held item             ← the settings the previous Trainer left on
   ├── Original Trainer, ID No. ─┐
   ├── where it was met          ├── three different lines, three different meanings
   └── the ribbons and marks    ─┘
```

## 1. The top of the summary, and the one line that outranks the rest

**Species** is the line that decides whether any of this works. If the game you are actually
playing does not have that species in its **Pokédex**, no amount of correct everything-else helps,
and **Pokémon HOME** will simply refuse to send it: a **Sylveon** does not go back to **Kanto**,
and a **Garchomp** raised in **Sinnoh** only travels forward. Check against the cartridge in your
hand, not the newest one you have read about.

Then the numbers, which give you the arithmetic from
[228](228-attention-variants-and-kv-arithmetic.md) and [207](207-sparse-moe-serving.md):

```
   level · the six stats · Nature · Ability · whether it is one of a line
        → what it costs you to carry and what it costs you to use

   registered versus on the field
        → the whole team's weight against the one that acts

   the Nature and the EVs         → how much of the stat line is real
   what it was met at, and where  → whether it obeys you at the level printed
   its moves                      → must match what the species can legally learn
```

Two traps live here. **The level printed is not the level it will obey at**: a traded Pokémon
ignores you above a ceiling set by how many badges you hold, and only with all eight does it obey
completely. And **a Singles six is not a Doubles four**: **VGC** registers six, brings four and
puts two out at a time, and a team assembled for one format does not re-slice into the other,
which is the kind of thing you discover at the registration desk.

## 2. Weigh it before you count on it

Look at the actual stat line, not the species' reputation. That number — after the Nature, the
**EVs** and whatever **Hyper Training** has been done — is what walks onto the field, and it
already reflects whatever the previous Trainer did. If you want the Nature pinned, an
**Everstone** on the parent does it; hoping does not. A Pokémon whose history you can see is what
you want. Something handed to you by a stranger at the **Global Trade Station** — a **Smeargle**
carrying a move it never **Sketch**ed — is asking you to take its word for everything else too.

## 3. The Original Trainer, which is three questions not one

*May I use it, do conditions travel with it, and can those conditions change?*

| Where it came from | Ceiling | What travels | Can it change |
| --- | --- | --- | --- |
| You raised it | none | nothing | no |
| Traded, common terms | high, but there | naming, pass-through, limits on offspring | amendable |
| Traded, house rules | set by the house | an acceptable-use note | the house sets it |
| Event-distributed | varies | varies — read the ribbon, it is short | varies |

As of September 2026 the easy end is crowded: DeepSeek, Mistral Large 3 (reported 675 registered,
41 on the field, fully open terms), GLM-5.3 and GLM-5.3-Flash (the same), and Meta's Muse Glimmer
(30, open, August 2026) are all Pokémon you may simply use. Llama 4 still carries its house rules,
with a size threshold and a requirement that anything bred from it keeps the family name; many of
the smaller Qwen releases are unconditional while the flagships are not. **The question for
whoever checks your registration is not "is it tradeable" — it is whether a conduct note travels
with it and whether the house can rewrite that note without telling you.**

## 4. The moveset, and how it answers you

This is where the silent failures live.

* **The moves must be legal for the species.** An illegal moveset does not throw you out at the
  door; it gets you quietly turned away later, at the one facility you cared about.
* **How you address it matters.** The previous Trainer taught it in a particular order and a
  particular style, and calling the moves differently costs you real damage that nothing on the
  screen will report.
* **Knowing when to stop is a move property, not a Trainer property.** **Outrage** locks
  **Dragonite** in for two or three turns whether you like it or not and leaves it confused
  afterwards. **Thrash** and Petal Dance do the same. If your Pokémon never stops attacking, look
  at the move before you look at the Pokémon.
* **Some of them have a second phase.** **Solar Beam** charges for a turn first; **Hyper Beam**
  and **Giga Impact** leave you standing there afterwards. If you have not accounted for it your
  opponent sees the wind-up and switches in **Blissey**.
* The moveset also sets what a turn *costs* you — see [206](206-million-token-context.md). Two
  Pokémon with the same **Speed** do not get the same amount done.

## 5. What actually reaches the other games, and when

```
   day 0        usable in the game it was caught in, immediately
   day 0–3      Hyper Training with a Bottle Cap, or a Gold Bottle Cap for all six
   day 3–21     Pokémon HOME learns the new species and will move it forward
   later        the older services, if anyone still bothers
   newest       new kinds of Bottle Cap, only just reaching the handheld games
```

The order is not arbitrary. The game it came from already knows the species. **Pokémon HOME** has
to be taught each new one by hand, so a genuinely new species — a new Ability, a new type
combination — arrives there weeks later or not at all. **"Has HOME got it yet" is a proxy for
"has anyone outside the studio implemented this."**

And be clear about what **Hyper Training** is. A **Bottle Cap** makes a stat *behave* as though it
were perfect without making it perfect, and the improvement is not passed to the offspring through
a **Destiny Knot**. It is an excellent thing to do to a Pokémon you are going to battle with, and
a useless thing to do to one you are going to breed from.

## 6. The compatibility question, asked properly

Do not ask "is it allowed". Ask, of the exact bracket you are entering: is the species in the
Dex; is this build legal under the **Regulation G** list the **VGC** season is actually running;
does the **Battle Tower** recognise a **Choice Scarf** here and the **Battle Maison** not; does
anyone know how it was taught to answer; and does your six divide into the format. Five yeses is
a team. Four is a weekend.

## Where this stands, September 2026

The transfer services move: one kind of **Bottle Cap** is standard now, another is fading, and a
third is only just arriving. The house rules move less, but they do move, and the amendable
conduct note is exactly why you re-read rather than remember. The noticeboards themselves were
behind a gate I could not pass, so the terms and formats above come from write-ups — read the
actual line on the actual summary screen of the actual Pokémon you are registering, every time.
The reading order is the part that keeps: species, weight, Original Trainer, moveset, transfer,
bracket. It has not changed in three generations and it will not change next year.

## What a Gym Leader is listening for

* Why might the level printed on the screen not be the level it obeys at?
* It will not stop attacking. What do you look at first?
* Why does **Pokémon HOME** lag the game a new species debuted in?
