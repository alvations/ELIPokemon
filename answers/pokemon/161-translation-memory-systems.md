---
id: "161"
slug: translation-memory-systems
style: pokemon
category: translation
difficulty: intermediate
question: "What is a translation memory, and how does it fit alongside MT?"
tags: [translation-memory, fuzzy-match, leverage, cat-tools, retrieval, maintenance]
---

# Check the Pokédex before you go looking

**Professor Oak**'s device does something very dull and very valuable: it remembers every Pokémon
you have already seen and every one you have already caught.

So before you spend a whole afternoon in the **Tall Grass**, you check. **Have I already got this
one?**

That is a translation memory. A drawer of segments somebody has already translated **and signed
off**, consulted *before* any machine is asked to do anything. It is older than every technique in
this dataset, it is what professional translators actually work inside all day, and ML teams
rebuild a worse version of it by accident all the time.

## Already caught, nearly caught, or new 🎣

```
   the segment coming in:  "Click Save to store your changes."

   check the Pokédex ─┬─ 💯 caught it       ─► exactly this, already approved. Free. Done.
                      ├─ 🟢 nearly          ─► "...store your settings." One word to fix
                      ├─ 🟡 related         ─► "Press Save to keep..." A useful hint
                      └─ 🔴 barely          ─► ⚠️ do NOT show this one
```

📌 That last line matters. A **Rattata** when you needed a **Raticate** is helpful. A **Rattata**
when you needed a **Gyarados** is worse than nothing — it **anchors** the translator (question 149)
into shaping their answer around something irrelevant. Below a threshold, showing the match makes
the work worse, not faster.

And how much of the job the Pokédex already covers is **the number the whole business runs on**:
already-caught segments are charged at a fraction, near-matches at a discount, brand-new ones at
full price. ⚠️ Which is why keeping the Pokédex clean is a **money** question, not a tidiness one.

There is a second thing translators use constantly and pipelines always forget: **look up a
phrase, anywhere.** Not "find this whole segment" but *"show me every time anyone has ever
translated **Poké Ball** in this product"*. That is the concordance, and it is how consistency
actually gets maintained by hand.

## It works *with* the machine, not instead of it 🤝

| What you found | What to do |
| --- | --- |
| 💯 Exact | Use it. Approved, consistent, free |
| 🟢 Very close | Hand the entry over to be edited |
| 🟡 Loosely related | **Give it to the machine as an example** (question 134) |
| ⬜ Nothing at all | Machine translate it, with the name list (question 133) and Nurse Joy watching (question 132) |

📌 The third row is where modern systems find real gains. A Pokédex full of approved work **is** a
retrieval corpus for exactly your subject — and putting the nearest few entries in front of the
translator lifts terminology and style more dependably than any training run, with no training run.

## It rots if you leave it 🧹

A Pokédex that nobody maintains fills up with:

* **🕰️ Entries from a previous era.** Names that were rebranded. Screens that no longer exist.
* **⚔️ Straight contradictions.** The same segment approved three different ways by three projects
  with three style guides — and the lookup returns **one of them, arbitrarily**, with no hint that
  the other two exist.
* **🏷️ The Original Trainer problem** (question 149). As repaired machine output flows back in, the
  Pokédex slowly fills with machine phrasing, and every future lookup **reinforces** it. The drawer
  becomes a mirror.
* **📄 Segments with no context left.** Approved for a screen that has since been redesigned.

Hygiene: keep a separate Pokédex per product and per region; date every entry and prefer the recent
one; run a conflict report now and then; and above all **record who caught it and when**.

⚠️ **A Pokédex without that record cannot be cleaned — only trusted or thrown away**, and a big
untrustworthy one is worse than a small honest one.
