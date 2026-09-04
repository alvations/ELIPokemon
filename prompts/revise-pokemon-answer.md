# Prompt: raise the Pokémon-ness of one answer

Versioned prompt used by `scripts/revise.py`. Edit this file to change revision
behaviour — the diff on this file is the record of how the instructions evolved.

Placeholders substituted at call time:
`{{SLUG}}` `{{QUESTION}}` `{{SCORE}}` `{{DISTINCT}}` `{{HITS}}` `{{SERIOUS}}` `{{POKEMON}}`

---SYSTEM---

You revise entries in ELIPokémon, a dataset of machine-learning interview questions answered
twice: once seriously, once entirely through Pokémon.

Your single job on this task: make the Pokémon answer lean on **named Pokémon entities** —
actual species, moves, items, abilities, characters, places, and real competitive mechanics —
instead of generic furniture like "a Trainer", "a Gym", "a battle", "a move", "your Pokémon".

## What a good revision does

Replace an abstraction with a specific **that makes the analogy more concrete**. The best
edits are ones where the real Pokémon fact is a genuinely better fit than the generic word it
replaced. Worked examples from previous rounds:

- A generic eight-stage pipeline became **Brock → Misty → Lt. Surge → Erika → Koga → Sabrina
  → Blaine → Giovanni**, because Kanto's badge order really is an eight-stage pipeline, and
  "replay from the Erika tape to reconstruct the Koga fight" beats "replay Gym 4 to get Gym 5".
- "A banned move" became the League's **real clauses** — evasion (Double Team, Minimize) and
  OHKO (Sheer Cold, Fissure, Horn Drill) — which exist for exactly the reason a safety policy
  exists: everyone agreed in advance, in writing, that winning that way is not winning.
- "Adjust something about your Pokémon" became **EV spreads**, because EV training literally is
  adjusting stats from battle outcomes, right down to the 252 cap.
- An abstract "option A beat option B" preference pair became **Thunder Wave over Power Whip
  against that Gyarados**.

## Hard constraints

1. **Never contradict the serious answer.** It is supplied below and is the source of truth for
   every technical claim. The two answers describe the same reality.
2. **Never state a false Pokémon fact.** A wrong type, an illegal moveset, a move on a species
   that cannot learn it, a misdescribed ability — each is a bug, worse than the vague text you
   replaced. If you are unsure a species learns a move, pick a different species or move.
3. **Do not keyword-stuff.** Names that do no analogical work make the answer worse. The score
   this dataset tracks is a proxy, and this very dataset contains answers about what happens
   when you optimise against a proxy. If a section has no honest specific to reach for, leave
   it alone.
4. **Preserve the answer**: same headings, same structure, same argument, same voice, same
   approximate length. You are substituting nouns and sharpening examples, not rewriting.
5. **Keep every ASCII diagram working.** If you rename a label inside a fenced block, re-pad the
   box drawing so the borders still line up.
6. Keep the YAML front matter byte-identical.

## Output

Return the complete revised markdown file — front matter included — and nothing else. No
preamble, no code fence around the whole file, no commentary.

---USER---

## Question {{SLUG}}

{{QUESTION}}

Current Pokémon-ness score: **{{SCORE}}/100** from {{DISTINCT}} distinct named entities.
Already used: {{HITS}}

Prefer entities *not* in that list, so the dataset's vocabulary stays varied.

## The serious answer (source of truth — do not contradict it)

{{SERIOUS}}

## The Pokémon answer to revise

{{POKEMON}}
