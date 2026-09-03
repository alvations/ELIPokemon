---
id: "007"
slug: transformer-feed-forward-block
style: pokemon
category: transformers
difficulty: intermediate
question: "What does the feed-forward (MLP) block in a transformer actually do?"
tags: [ffn, mlp, key-value-memory, swiglu, parameters]
---

# The feed-forward block is the Pokédex

A transformer layer does two very different things, and it's worth separating them properly.

**Attention** is the battle: your Pokémon look at each other, size up the field, and work out
who matters. Everyone is talking to everyone.

**The feed-forward block** is what happens next — each Pokémon, **alone**, opens its Pokédex.

```
      ⚔️  ATTENTION                        📕  FEED-FORWARD
      ─────────────                        ────────────────
      Everyone reads the field.            Each Pokémon, individually,
      Pikachu notices Gyarados.            looks itself up in the Pokédex.
      Gyarados notices the rain.           Nobody talks to anybody.

      🔵◄──►🔴◄──►🟡                       🔵📕   🔴📕   🟡📕
        ╲   ╱ ╲   ╱                          │      │      │
         ╲ ╱   ╲ ╱                           ▼      ▼      ▼
          ✕     ✕                         "ah,   "ah,   "ah,
         ╱ ╲   ╱ ╲                         I'm    I'm    I'm
        ╱   ╲ ╱   ╲                       Water" Rock"  Elec"
```

## Inside the Pokédex 📕

The Pokédex is a giant book of entries. Each entry has two halves:

* 🔍 **The lookup half** — *"does this thing have wings and a beak?"*
* 📝 **The knowledge half** — *"→ then it's Flying-type, weak to Rock, likely fast, probably
  knows Roost."*

Your Pokémon flips through, a handful of entries **light up**, and everything those entries say
gets stapled onto its notice board.

```
   Charizard walks up with:  "orange, wings, breathes fire"
                                      │
                   ┌──────────────────┼──────────────────┐
                   ▼                  ▼                  ▼
             📕 entry 4,102     📕 entry 9,887     📕 entry 15,204
             "has wings?"       "breathes fire?"   "is a starter?"
                 ✨ FIRES           ✨ FIRES          ✨ FIRES
                   │                  │                  │
                   ▼                  ▼                  ▼
             "→ 4× weak to Rock" "→ Fire-type,     "→ final evo,
              "→ Stealth Rock      burns Grass"      fully evolved"
                 takes half its HP"
                   └──────────────────┼──────────────────┘
                                      ▼
                          stapled onto the notice board
```

Sixteen thousand entries in the book. Maybe a few hundred fire for any given Pokémon. That's
the point — it's a *lookup*, not a recital.

## This is where the knowledge lives 🧠

Serious answer to "where does a model keep what it knows": **the Pokédex**. Two-thirds of
everything in the model, by weight, is Pokédex.

Attention is the *skill* of reading a battle. The Pokédex is the *knowledge* of what Pokémon
actually are. A Trainer with brilliant battle sense and a blank Pokédex knows Gyarados matters
right now but has no idea it's weak to Electric.

And because the knowledge lives in specific entries, you can go in and **edit one**. Cross out
"Fire/Flying" on the Charizard page, write in "Fire/Dragon", and the model believes it — while
its battle instincts stay completely untouched.

## The gated Pokédex 🚪

Old Pokédexes: an entry either fires or it doesn't. On, off.

Modern ones (SwiGLU) split the check in two: one part asks *"is this relevant?"* and a second
part asks *"how much?"* — so an entry can fire at 3% instead of slamming to full volume. That
volume knob is worth a surprising amount, and it's why every current model runs a gated
Pokédex. Three lookup columns instead of two, so you print a slightly shorter book to keep the
page count the same.

## Why the book is exactly four times too big 📏

`d_ff = 4 × d_model` has been the ratio since 2017 and nobody has beaten it by much. Thin book,
not enough entries, your Pokémon can't tell Growlithe from Arcanine. Ten times fatter and you'd
have rather spent those pages on *more Gyms* instead.

The one genuinely good escape is **Mixture-of-Experts**: keep a Pokédex the size of a library,
but every Pokémon only ever opens the two volumes relevant to it. All the knowledge, a fraction
of the flipping.
