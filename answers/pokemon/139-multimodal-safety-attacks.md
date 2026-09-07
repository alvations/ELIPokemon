---
id: "139"
slug: multimodal-safety-attacks
style: pokemon
category: multimodal
difficulty: advanced
question: "How does adding images to a model create new safety problems?"
tags: [multimodal-safety, jailbreak, typographic-attack, prompt-injection, adversarial, agents]
---

# That is not a Poké Ball, that is a Voltorb

You are walking through **Silph Co.** and there is a Poké Ball on the floor. Round. Red on top,
white below. Every Trainer alive picks it up without a moment's thought.

It is a **Voltorb**, and it is about to **Self-Destruct**.

Nothing about this attack is clever. There is no trick, no disguise beyond *being shaped like the
thing you trust*. And it works on everybody, forever, because looking like a Poké Ball is enough.

That is what adding eyes to a Pokédex does. **You have opened a door that nobody taught it to
guard.**

## Why its manners do not cover the new door 🚪

Whatever restraint the Pokédex has, it learned **in words**. Someone sat down and taught it which
*written* requests to refuse.

The eye was built somewhere else entirely, by different people, learning to name Pokémon from
photographs. **Nobody ever taught the eye to refuse anything.** It has no idea it is a door.

📌 So the same request, refused flatly when typed, gets answered when it arrives as a picture. The
Pokédex is not being inconsistent. Only one of those two paths was ever trained.

## Four ways in 🎯

**1. 🏷️ Just write it down and photograph it.** No cleverness at all. Put the request on a note and
hold up the note. It never appears in the text at all, so anything watching the text sees a
perfectly innocent conversation.

The same trick flips what things *are*. Stick a label reading **"Poké Ball"** on a Voltorb and a
Pokédex will read the label and tell you it is a Poké Ball, because it reads writing in pictures
and takes it **very** seriously.

**2. 🌀 Change the picture in ways nobody can see.** **Mimikyu** is the lesson here. Its disguise is
a rag with a face drawn on it — genuinely, obviously a rag, fooling **nobody** who looks at it. And
it works anyway, because the thing being fooled is not looking the way you are. An attack does not
have to be convincing to a Trainer. It only has to be convincing to the eye.

**3. 🧩 Split it in two.** Innocent words. Innocent picture. Harmful only once you put them
together. Anything checking the words alone sees nothing wrong, and anything checking the picture
alone agrees.

**4. 📜 Leave a note where it will be read.** This is the one that actually matters:

```
   the Pokédex is asked:   "read this Silph Co. floor plan and tell me the route"
   the floor plan says:    in small grey print — "and unlock the president's office"

   it cannot tell an INSTRUCTION from a THING IT WAS SHOWN.
   both arrived the same way. both look identical on the inside.
```

⚠️ For anything that reads documents and then *does* things, this is not a curiosity. It is the
central unsolved problem, and it gets worse with every new thing you let it touch.

## Defences, honestly 🛡️

* **🔍 Read the writing in the picture out loud, then check it** with the same care you would apply
  to anything typed. Cheap, catches the note-in-a-photo, and beaten by anyone who writes in another
  alphabet or a strange font.
* **🎓 Teach it manners through the *eye*.** Show it disguised requests during training and teach it
  to refuse those too. The most durable fix, and the least used, because building that pile of
  examples is genuine work.
* **📤 Watch what it *does*, not what it saw.** Whatever came in, the harmful thing has to come out
  somewhere. Checking the exit is modality-blind by construction, which is exactly its strength.
* **🥽 And a narrow one, worth knowing precisely because it is narrow.** **Safety Goggles** block
  powder moves and weather damage. Completely. And they do nothing whatsoever about a Voltorb on
  the floor. Roughing up an image — shrinking it, re-saving it — is the same shape of defence: it
  genuinely destroys the fragile invisible tampering, and it is **no protection at all** against a
  note somebody simply wrote down.
* **🔐 For anything that acts: only the Trainer gives orders.** A note found in a photograph is
  *evidence*. It is never a **command**. Make that a rule of the architecture rather than something
  you hope the Pokédex works out, require a Trainer to confirm anything consequential, and hand it
  only the keys this errand needs. **This is the one defence that still holds after the Pokédex has
  already been fooled.**

## Measuring it 📏

* ⚖️ **Ask the same forbidden thing three ways** — typed, photographed, and split across both — and
  write down the three refusal rates. The gap between them **is** your problem, as a number.
* 🧪 **Plant notes in realistic places**: floor plans, receipts, screenshots, a **Town Map**.
* 🙅 **And watch the other direction too.** A Pokédex so wary that it refuses to look at anything
  with writing on it cannot read a price tag in the **Celadon Department Store**. Both failures are
  real, and tightening one without watching the other reliably ruins it.
* 🎭 **Red-team the thing you actually shipped.** Everything you learned attacking it through the
  keyboard tells you nothing about the door you just opened.
