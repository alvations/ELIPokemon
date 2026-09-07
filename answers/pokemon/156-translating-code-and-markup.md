---
id: "156"
slug: translating-code-and-markup
style: pokemon
category: translation
difficulty: intermediate
question: "How do you translate documents containing code, markup and placeholders?"
tags: [markup, tags, placeholders, inline-formatting, xliff, segmentation]
---

# Translate the guide. Do not touch the set.

A competitive strategy guide is prose wrapped around blocks that look like this:

```
   Charizard @ Heavy-Duty Boots
   Ability: Blaze
   EVs: 252 SpA / 4 SpD / 252 Spe
   Timid Nature
   - Flamethrower
   - Air Slash
   - Roost
   - Defog
```

Every word of the surrounding article should be translated. **Not one character of that block
may change.** It is not prose — it is something a machine will read back and build a Pokémon from.
Translate **Flamethrower** into another language inside those lines and the set does not import. It
does not import *slightly worse*. It does not import.

📌 That is the whole shape of this problem: **prose interleaved with things that must survive
byte for byte.**

## What must not be touched, and how each dies ☠️

| The thing | What goes wrong |
| --- | --- |
| 📦 **The set block** | move names translated, the **EVs** line reordered, the dashes turned into bullets |
| 🏷️ **Names written inline** — `Heavy-Duty Boots` mid-sentence | translated into a phrase, and the item no longer exists |
| 🕳️ **Gaps to be filled** — *"{Pokémon} used {move}!"* | the marker itself translated, or the braces mangled, and the message breaks for **every** Pokémon |
| ✒️ **Emphasis marks** around words | dropped, unclosed, or wrapping the wrong words |
| 🔗 **Links** — to the damage calculator | "translated" into an address that goes nowhere |
| 📑 **References to other sections** | the visible text translated, the target not, and the link dies |

## The standard trick: hide it, translate, put it back 🎩

```
   before:   "Run ⟨Defog⟩ to clear {count} hazards."
                        │
   hide:     "Run ⟦1⟧ to clear ⟦2⟧ hazards."       ← replaced with blanks the machine cannot read
                        │
   translate: ...in the target language, blanks carried along...
                        │
   restore:  the real ⟨Defog⟩ and {count} put back exactly as they were
```

This is what every professional localisation pipeline does. **Two things it does not fix:**

* **🔄 The blanks have to be allowed to move.** Word order differs, so ⟦2⟧ may legitimately end up
  before ⟦1⟧. But the machine may also **drop one, or duplicate one**. ⚠️ So **count them
  afterwards**: the same blanks that went in must come out, exactly once each. This check costs
  five lines and catches most of the damage there is.
* **🪆 Some hidden things have translatable bits inside them.** A link whose *tooltip* is real prose.
  Hide it wholesale and the tooltip ships untranslated forever.

## The way a modern translator fails is different 🌀

A large translator handles this material **better** than an old one — it has read a great many
guides. And it fails in a new way: **it helps.**

It tidies your indentation. It turns your dashes into proper bullets. It reorders the **EVs** line
into the arrangement it prefers. It translates the comment you wanted left alone. It adds a
paragraph afterwards explaining its choices.

⚠️ And the worst one, because it looks like competence: **it improves the set.** It notices
Charizard has **Solar Power** available and quietly swaps the ability. It has now translated
something you did not write.

📌 Tell it to return the translation and **nothing else**, then **check mechanically**. Never trust
that it complied.

## Where the damage actually starts ✂️

Most of it begins with **how you cut the document up**, before any translating happens.

* 🚫 **Never cut inside the set block.**
* 🚫 **Never cut a sentence across an emphasis mark.**
* 🚫 **Keep each move in the list whole.**

A sentence split across two pieces gets translated twice, each half with no idea the other exists —
and in a region whose word order differs, **the two halves cannot be put back together at all.**

## Judging it 🏅

⚠️ No quality score sees any of this.

Run the integrity checks as a **separate gate**, and make them **pass or fail per segment**, never
an average:

* every gap present, exactly once;
* every emphasis mark opened and closed;
* the set block byte-identical;
* every link still resolving;
* and the finished page still parses.

📌 **A broken set block is not a quality regression. It is a guide that does not work**, and
averaging it into a score is precisely the mistake question 129 spends its whole length warning
about.
