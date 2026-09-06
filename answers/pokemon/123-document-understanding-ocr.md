---
id: "123"
slug: document-understanding-ocr
style: pokemon
category: multimodal
difficulty: intermediate
question: "How do you build question answering over scanned documents?"
tags: [ocr, docvqa, layout, reading-order, tables, anls, grounding]
---

# Reading the Celadon Department Store directory

Six floors. A board by the lift telling you what is on each one. Shelves of items with prices on
little labels. Vending machines on the roof — **Fresh Water ¥200, Soda Pop ¥300, Lemonade ¥350**.

A Trainer asks: *"Which floor sells the thing that cures a burn, and what does it cost?"*

This is not "what Pokémon is in this picture". This is **words, printed small, arranged in a
shape that means something.** The floor number and the department name are on the same row for a
reason. Get the arrangement wrong and every word you read is worthless.

## Two ways to answer 🏬

**Send a clerk up with a notepad.** They copy down every label and every price, note where each
one was, and bring the list back. Then you answer from the list.

```
   the board ─► 📝 clerk copies it out ─► words, and where each one sat
                                                │
                                                ├─► which column? which row? what order?
                                                ├─► that price belongs to THAT item
                                                ▼
                                       a tidy list ─► 📖 reason over it ─► "4F, ¥250, third shelf"
```

**Or hand the whole photograph to the Pokédex** and let it read and answer in one go, no clerk, no
notepad.

| | Clerk with a notepad | Pokédex reads it directly |
| --- | --- | --- |
| ❌ When it goes wrong | the clerk's mistake is now *fact*, and nothing downstream can tell | one machine, one place to look |
| 👉 Pointing at the source | free — the clerk wrote down where everything was | only if you taught it to |
| 🔎 Checking the working | you can inspect every step | you cannot |
| ✍️ Scrawled handwriting | usually hopeless | often much better |
| 💰 Cost | cheap per page | expensive — every panel, full detail |

⚠️ **The clerk's errors are the dangerous ones.** If they write down **Full Heal** where the shelf
said **Full Restore**, everything after that is confidently, fluently wrong — and those are two
genuinely different items. One clears a status condition. The other clears status *and* refills
HP completely. A Trainer acting on the wrong one loses the match, and nobody at any later stage
has any way of knowing.

Most real setups use the clerk **and** keep a Pokédex on hand for the pages the clerk cannot
manage. Not because it is elegant — because when someone asks *"where does this answer come
from?"* the notepad can point at the shelf.

## Reading in the wrong order 📰

The single most underrated failure. A board with two columns, read straight across:

```
   THE ACTUAL BOARD                      READ STRAIGHT ACROSS
   ┌────────────┬────────────┐           "2F Trainer's  4F Evolution
   │ 2F Trainer │ 4F Evo     │            Market stones 3F TM
   │  Market    │   stones   │            Corner 5F Drugstore..."
   │ 3F TM      │ 5F Drug    │
   │  Corner    │   store    │           ← every line is half of two different floors
   └────────────┴────────────┘
```

The words are all perfectly correct. The answer is still garbage, because **4F now appears to
sell TMs and the Drugstore has moved to the third floor.** No amount of careful reading fixes a
board read in the wrong order.

📌 So: work out the blocks *first*, then the order to read them in, and keep tables as tables. A
price list flattened into a run of words loses the one thing that made it a price list — that the
number sits beside its item.

## Scoring it fairly 🏅

* 🔤 **Give part marks for near misses.** A clerk who writes `Leftovrs` has made a smudge. A clerk
  who writes `Lucky Egg` has read a different shelf. Marking both simply "wrong" tells you nothing
  about which kind of Pokédex you have.
* 🧾 **Grade the clerk separately from the reasoning.** When the final answer is wrong you need to
  know whether the words came back wrong or the thinking did. One notepad column, checked on its
  own, settles it.
* 🌀 **Test the awkward pages on purpose.** Two columns. A page pinned up sideways. A table that
  runs over onto the next board. A handwritten note stuck over the printed one. A photograph taken
  from too far away.
* 👉 **Check where it points, not just what it says.** A Pokédex that gives the right price and
  points at the wrong shelf got lucky, and you will find out which the next time it does not.

## Practical bits 🔧

* 🧼 **Straighten and clean the photograph before the clerk reads it.** A crooked, grainy shot
  costs more accuracy than any choice of clerk.
* 🔭 **Walk closer than you think you need to** (question 121). A Pokédex that identifies an
  **Onix** across a quarry cannot read a ¥250 price tag, and the reason is not intelligence.
* 🔡 **Settle the spelling afterwards** (question 115). Clerks are wildly inconsistent about
  accents and about letters that get printed joined together.
* 🗂️ **Do not photograph all six floors.** Find the right floor first, then read it (question
  044). Hauling the entire store into the conversation is how you run out of room before you have
  answered anything.
