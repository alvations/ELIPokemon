# Standing brief — writing for the medical domain

You have been assigned a **specialty** and a **block of IDs**. Everything else you need is here.
Read this file, then `../SAFETY.md`, then `../README.md`. Then write.

## Read first, in this order

1. **`../SAFETY.md`** — the most important file in the domain. Read it twice.
2. `../README.md` — the seven specialties, the layout, the conventions.
3. `../../../CONTRIBUTING.md` and `../../../for-agents/LEARNINGS.md` — especially "Named entities
   that are load-bearing", "A good analogy can score near zero, and the scorer is right to do it",
   and "The brief was wrong, and the right move was to write against it".
4. **Two existing pairs in your own specialty**, if any exist, for voice and for the conventions
   already established. If your specialty is empty, read
   `../answers/pharmacology/serious/m006-*.md` and its Pokémon counterpart — the highest-scoring
   block written so far.
5. `CONVENTIONS.md` in this directory — the analogy mappings already in use. **Reuse them where
   they fit.** A specialty with one vocabulary is worth more than a specialty with fifty
   metaphors.

## The shape of an answer

Both halves carry the same sections in the same order:

| Section | Both halves? | Notes |
| --- | --- | --- |
| H1 | yes | A claim, not a label |
| body | yes | The mechanism. At least one column-aligned fenced diagram in the serious half |
| `## Where the metaphor stops` (Pokémon) / `## The human stakes, said plainly` (serious) | yes | **Plain prose, no analogy.** House pattern — the validator checks for it |
| `## What an examiner digs into next` | yes | Or a specialty-appropriate equivalent. **Its position is the specialty's, not this table's** — see below |
| `## Sources` | yes | See below. Immediately before Scope and safety |
| `## Scope and safety` | yes | What this is not for, and local guidance |
| `## Where this stands, <Month Year>` | yes | What will date, and where the authority lives |

**On the order of the last four.** This table's order is the common case, not a rule. Specialties
differ — some put `## What an examiner digs into next` before `## Sources`, others after
`## Scope and safety` — and two writers found that out by matching their specialty against a table
that contradicted it. **Match the pairs already in your specialty.** The only hard constraint is
that `## Sources` comes immediately before `## Scope and safety`. The two halves of your own pair
must correspond section for section, so a reader can set them side by side.

Front matter, with `question` matching the catalogue row character for character:

```
---
id: "m042"
slug: your-slug-here
style: serious
category: nursing
difficulty: intermediate
question: "Your question text here?"
tags: [four, or, five, lowercase, tags]
---
```

Both answers at least 600 words — the validator's hard floor is 120, which is a tripwire for a
stub and not a target; nothing in the domain is under 1,600. **Prose** wraps at 98 **characters**
— an em dash is one character, not three. Never wrap inside a fenced block, and **the 98 does not
apply to Markdown table rows**; long rows are normal here and a writer checking their own wrapping
should not try to break them.

## The clinical rules, which are not negotiable

* **Mainstream consensus only.** Where practice differs by country or institution, say so rather
  than picking one and asserting it.
* **Never invent a number.** No fabricated thresholds, doses, scores, intervals, sensitivities,
  prevalences or survival figures. Use a genuinely uncontroversial figure and name the authority,
  or **write the principle without the number** — which is usually the better answer anyway. An
  invented clinical number is a more serious defect than an invented Pokémon fact, and this
  repository already treats the latter as a correctness failure.
* **Never fabricate a citation.** No invented trial names, guideline numbers, DOIs, author-year
  references or document titles. The validator fails the build on all four patterns.
* **No answer addresses the reader as their clinician.** Explain what is done and why; never tell
  a reader what to take, stop or apply. The validator's regex is deliberately crude and will
  over-flag. Reword rather than argue with it. Known trap: `take \d+ mg` fires on an innocent
  sentence like "a trunk will take 100 g" — phrase quantities as *needs* or *is of the order of*.
* **Cut rather than soften.** A claim you cannot attribute to a nameable document comes out.

## Sourcing: attribution without quotation

**No medical authority is reachable from this environment.** `who.int`, `cdc.gov`, `nice.org.uk`,
`pubmed.ncbi.nlm.nih.gov`, `bnf.nice.org.uk`, `resus.org.uk`, `nhs.uk`, `medlineplus.gov`,
`cochranelibrary.com`, `dermnetnz.org` and `en.wikipedia.org` all return a 403 policy denial.
Several writers have verified this first-hand rather than taking it on trust, which is the right
instinct — do the same if you are about to assert it.

Web search returns aggregated summaries. A summary is the summariser's words. **Quoting one as a
guideline would be fabricating a medical citation.**

So every answer carries a `## Sources` section:

* headed by this line, **verbatim** (the validator checks for it):

  `**None of the sources below was retrieved.** They were unreachable from the environment this
  was written in, so every claim here rests on general professional knowledge and is attributed,
  not quoted. Open the document before relying on anything in this answer.`

* then the documents a reader should open, named precisely enough to find, with the issuing body
  named. **Standing documents for your specialty live in `SOURCES-<specialty>.md` in this
  directory. **Point at it from an answer as
  `[`../../../for-agents/SOURCES-<specialty>.md`](../../../for-agents/SOURCES-<specialty>.md)` —
  three levels, not two.** Five writers independently wrote `../../` and produced fifty broken
  links, because this instruction used to name the file without giving the path from an answer
  file. Point at that file and list only what is specific to your answer.** That keeps the section
  short; near-identical 180-word blocks repeated a hundred times are waste. Early answers repeat
  the standing list inline instead; that is the older form, it is not the one to copy, and it is
  being swept. If the pairs you read for voice repeat it, follow this instruction and not them.
* **no quotation marks around source text, no DOIs, no author-year citations, no guideline codes,
  no URLs.**

Mark each load-bearing claim inline with its basis: *mechanism*, *definitional*, *consensus*, or
*country-dependent*. Declare your markers once per answer.

**Use those four words, bold and in parentheses: `(**mechanism**)`, `(**consensus**)`.** Several
of them together go in one bracket: `(**mechanism**, **consensus**)`. That is now the only form in
the domain, 1,187 annotations across all seven specialties.

Getting here took two wrong instructions from me and three writers pushing back, so the history is
worth one paragraph. Three forms were in use at once: the bold-parenthesised one (781 uses), a
`[mechanism]` square-bracket one (356), and a declared `[M]` `[C]` `[D]` `[L]` letter legend (71).
This brief told writers to use "the italic inline form", which was **not** any of them — the
italic count was about fifty. One writer matched its specialty's bracket form and broke the
brief's letter; another counted the corpus, found the brief outnumbered, said *"I added five more
bracket-form answers and I think that was right for local consistency and wrong for the corpus"*,
and asked for one sweep commit rather than a per-writer decision. That was the right request and
it is what happened, except that the sweep went to the form the corpus actually used rather than
the one the brief claimed.

**Double-mark when a claim is two things**, which is common and was being hidden by a hedge. A
writer pointed out that *"a split at or below the basement membrane may scar"* is a clinical
generalisation wearing a mechanism's clothes, and marked it `(**mechanism**, **consensus**)`
because the two words looked exclusive and are not. They are not. Mark both rather than choosing,
and there is no fifth marker.

**A Pokémon half that carries clinical markers declares them too.** The declaration is one short
section, placed where the serious half has one. If your Pokémon half carries no clinical claim, it
needs no declaration — do not announce a convention the answer then does not use. The reason to
declare in a register that also contains `TYPE_MUL_NO_EFFECT` and `holdEffectParam` is that an
undeclared marker there is genuinely ambiguous.

**Pokémon facts are different, and you may source them properly.** `raw.githubusercontent.com`
reaches `pret/pokered`, `pret/pokeemerald` and `rh-hideout/pokeemerald-expansion`. Read the
decompilation rather than trusting memory — every writer so far who did caught at least one error
they would otherwise have shipped. Where a Pokémon figure is **not** from code, say so in the same
note rather than letting a blanket statement imply it was.

## Pokémon accuracy is a correctness bar, not a style

Every fact must be true of the actual games: legal movesets, real base stats, correct type
match-ups, real item and ability effects, correct character roles, level cap 100, stat stages ±6.
Generation-dependent figures must be pinned to their generation. **If you are not certain, use a
different fact.**

## Where the metaphor stops

`../SAFETY.md` has the list and it binds: prognosis, dying, bereavement, pain, suffering,
distress, mental-health crisis, self-harm, safeguarding, capacity, coercion, and any point where a
reader could be a patient rather than a student.

**No Pokémon stands in for a person.** Nothing maps fainting to death, a lost battle to dying,
reviving to resuscitation, or a type match-up to someone's chances. If a mapping needs a Pokémon
to be the patient, the mapping is wrong — find another or drop the metaphor for that section.

Whimsy about a mechanism is useful. Whimsy about an outcome is grotesque.

## The quality gate

```
python3 scripts/medical/validate.py          # blocking. Must print OK before every commit
python3 scripts/medical/build_dataset.py
python3 scripts/medical/score.py --detail m042
```

**Target at least 45.** The scorer ignores the mandated plain-prose sections, so you are measured
on the analogy-bearing body only — do not pad those sections and do not avoid writing them.

If an answer scores low, run `--detail` **before** rewriting. The scorer's vocabulary has blind
spots and several writers have found their central device invisible to it. That is a report, not a
rewrite. When an answer genuinely is thin, fix it by replacing an abstraction with a **specific
that makes the analogy more concrete** — a named species with the right stat, a real move with its
real accuracy — never by adding Pokémon words.

**If holding the line on taste or safety costs you score, take the lower score** and say so. That
is the one place in this repository where the metric is not the arbiter.

## Deliverables

1. `../answers/<specialty>/serious/mNNN-slug.md` and
   `../answers/<specialty>/pokemon/mNNN-slug.md`.
2. Your rows appended to `../questions/questions.tsv` — `id⇥slug⇥category⇥difficulty⇥question`.
3. `scripts/medical/build_dataset.py` re-run, outputs included.
4. Commit in your worktree as `alvations <alvations@gmail.com>`, no trailers. **Do not push.**

**The session scratchpad is shared between everyone writing at the same time, and it is not
isolated.** Three writers in one wave had helper scripts silently overwritten mid-task by a
sibling using the same filename, and one of them watched its own script print another writer's
file list. Nothing was lost because they noticed, which is luck. **Prefix every scratchpad
filename with your specialty and ID block** — `endo-m056-m060-reflow.py`, not `reflow.py` — and
smoke-test any reflow or rewrite helper as a no-op against an existing answer before pointing it
at your own.

## Before you are given a territory list

**The topic list in your wave brief may contain topics that are already written.** This has
happened: a nursing brief offered eight topics of which three existed already, because whoever
wrote it summarised existing coverage from `CONVENTIONS.md` Part II, which is indexed by *device*
and not by *question*. m004 absorbs two of those eight topics and Part II renders it as "Something
that extends a state rather than causing it — Damp Rock".

So before you draft, run

```
python3 scripts/medical/coverage.py --next <your-specialty>
```

and read the **question text** of every pair your specialty already holds. If an offered topic is
already written, **say so in your hand-back and pick something else** — do not write a near
duplicate to fill the slot, and do not assume a list of five means five are available. The writer
who caught this also pointed out that an eight-for-five list with three dead entries leaves no
slack for a topic you need to decline on taste grounds, which is a real risk and not a theoretical
one.

## Two things about headings the section table does not say

**The examiner section's heading text differs between the two halves.** In nursing the serious
half says `## What an examiner digs into next` and the Pokémon half says `## What Nurse Joy is
listening for`, ten for ten. Read your specialty's pairs and match them; a writer using one
heading in both halves would be the odd one out.

**"The two halves correspond section for section" means the mandated trailing sections, not the
body.** Taken literally no pair in the corpus satisfies it: nursing runs 2↔5, 3↔5, 5↔3, 3↔3. What
is required is that the mandated trailing sections correspond one-to-one and in the same order,
and that the body sections correspond in *content* so a reader can set the halves side by side.
They need not be equal in number, and in practice the Pokémon half usually has more.

## Your worktree

Create it yourself and work by absolute path:

```
git worktree add -b <specialty>-<ids> .claude/worktrees/<specialty>-<ids> HEAD
```

**Do not use `EnterWorktree`.** It refuses from a pinned working directory, and its default base
is the remote default branch rather than `HEAD`, so in a wave where those differ you would
silently branch from a stale base.

## The gate, in full

Run all four before you commit, in this order:

```
python3 scripts/medical/validate.py                    # blocking; must print OK
python3 scripts/rewrap.py --check <your ten files>     # must report already wrapped
python3 scripts/medical/build_dataset.py               # outputs go in your commit
python3 scripts/medical/score.py --detail mNNN         # your score, one answer at a time
```

`rewrap.py --check` was missing from this list until a writer pointed out that the brief names the
gate without naming the one committed script that actually catches a wrapping regression — so a
writer following the brief literally would never run it. It is read-only with `--check`, it skips
front matter, fenced blocks and table rows, and it reports rather than rewrites.

Never run bare `score.py`. It rewrites `../LEDGER.md`, which integration regenerates centrally
once all blocks land; several writers running it in parallel worktrees produce several conflicting
partial ledgers.

## Do not edit

`scripts/` anything, `../SAFETY.md`, `../README.md`, `CONVENTIONS.md`, the root `README.md`,
`CHANGELOG.md`, `DATASHEET.md`, `TERMINOLOGY.md`, and **both** `LEDGER.md` files — the root one
and `../LEDGER.md` — or `../../../for-agents/`.

**On `../LEDGER.md` specifically**, because three writers read that line three different ways and
all three readings were reasonable. Run `score.py --detail mNNN` to read your own score. Do
**not** run bare `score.py`, which rewrites the ledger. Several specialties are written
concurrently in sibling worktrees, so a ledger regenerated in your worktree reflects a partial
tree, and five writers doing it produces five conflicting ledgers. **Integration regenerates it
centrally, once, after all blocks land.** If you have already regenerated it, say so in your
hand-back; it is not a problem, it is just noise in your diff.

**`TERMINOLOGY.md` and `CONTRIBUTING.md` step 6 conflict**, and a writer was right to flag it.
Step 6 asks for new Pokémon entities to be added to the glossary; this brief forbids editing it,
because seven writers editing one file in seven worktrees is a guaranteed conflict. **The brief
wins:** list the new entities in your hand-back and integration adds them. Report vocabulary gaps,
validator false positives and any defect you find in your hand-back instead — six scorer bugs have
been found that way and all six are now fixed.

**Never** mention Claude, Anthropic, AI assistance or any assistant model name, anywhere.

## Report back

IDs and slugs; each score; claims cut as unattributable and how many; any **clinical** claim a
reviewer should check first, in priority order; any **Pokémon** fact you were unsure about and how
you resolved it; validator false positives; scorer vocabulary gaps as exact strings; and anywhere
you wrote against this brief and why. **Writing against the brief is expected** — six of eight
writers in the machine-learning domain did, and in every case the corrected answer was better.
