# Learnings

What worked, what failed, and the specific mistakes — including the ones that shipped and
had to be fixed afterwards. Written so the next worker can skip the rediscovery.

---

## Part 1 — What failed

### The 21 accuracy errors, and what they have in common

A full audit of the 100 Pokémon answers, prompted by the observation that some of them
"made little Pokémon sense", found 21 factual errors across 23 files (commit `1540837`).
They fall into five classes, and the classes are more useful than the list:

| Class | Example found | Why it happened |
| --- | --- | --- |
| **Illegal movesets** | Splash listed alongside Thunderbolt on the same Pokémon; Charizard using Surf / Waterfall / Aqua Tail | The move *sounded* right for the analogy; nobody checked whether the species can learn it. |
| **Wrong numbers** | Focus Sash described as leaving 8% HP (it leaves exactly 1); Brock's Onix given 75 HP (it has 41); a "Level 280" Pokémon (the cap is 100) | Numbers were invented to make the arithmetic of the analogy come out neatly. |
| **Wrong item/move effects** | Damp Rock described as boosting Water moves (it extends rain) | Plausible-sounding effect inferred from the name. |
| **Wrong roles for characters** | Agatha and Lance used as Gym Leaders (both are Elite Four) | Character recalled correctly, position not. |
| **Mechanics that do not work** | Targeting a fainted Pokémon; Swords Dance used six times (it caps at +6, so three) | The analogy needed the mechanic to work that way, so it was assumed to. |

The single most instructive one: **Q040 used Flareon's Hidden Ability as an example of a
model hallucinating — but the stated ability, Guts, is correct.** The "hallucination" was
true. An answer *about* hallucination was demonstrating nothing, and the error was invisible
to anyone who didn't happen to know Flareon's ability list. It was rewritten around a
genuinely false claim.

**The generalisation:** in a corpus like this, the analogy exerts continuous pressure to
bend the source domain. Whenever a fact would make the metaphor land better, there is a pull
to assume that fact. Every error above is that pull winning. The countermeasure is to treat
the playful domain as having a truth condition of its own — which is why Pokémon accuracy
was promoted from "nice" to a correctness bar equal to the ML claims.

**A better move than correcting:** in most cases the fix was not to soften the claim but to
find the *real* fact that fits better. Q030 wanted a stat outlier for quantisation and had
invented one for Snorlax; Blissey's genuine 255 base HP is a sharper example than the
invention was. Reality is usually a better writer than the shortcut.

### Scorer bug 1 — the vocabulary parser silently produced zeros

Multi-word vocabulary blocks (moves, items, characters) were split on newlines, so each
*line* became one "term" — a 90-character string that appears in no answer. Every score came
back 0, and the bug read as a content problem rather than a tooling problem.

Fix: comma-separated blocks and a `_clean()` that splits on commas.

**Lesson:** a measurement tool needs a smoke test with a known-good input before its output
is trusted. Ten minutes of "why is this answer scoring zero, it's full of move names" was
spent debugging the corpus instead of the scorer.

### Scorer bug 2 — overlapping terms double-counted

`Thunder Wave` scored as both `Thunder Wave` and `Thunder`. Longer, more verbose answers
therefore beat precise ones, which is the opposite of what the score was supposed to reward.

Fix: sort all terms longest-first, and blank each match out of a working copy of the text
before trying shorter terms, so a shorter term can never re-match inside a longer one that
already scored. See `mask` handling in `scripts/pokemon_score.py`.

### Scorer bug 3 — over-broad ambiguity exclusion

`Protect`, `Recover` and `Surf` were on the `AMBIGUOUS` exclusion list because they are
ordinary English words. But in these answers they are almost always capitalised move names,
so real signal was being discarded.

Fix: narrow `AMBIGUOUS` to terms that genuinely collide, and let capitalisation carry the
rest.

**The important part is what happened next.** Fixing bugs 2 and 3 changed the meaning of
every historical score. Rather than quietly re-baselining, the recalibration was committed
**on its own**, with no content change, as `fd7e69f`:

```
10535d0  22.4  baseline
fd7e69f  24.0  Recalibrate scorer  (+1.6)   <- tooling change, zero content change
40c7e1f  26.9  wave 1              (+2.9)   <- first real content movement
```

A metric's history is only readable if changes to the metric are separable from changes to
the thing being measured. One commit, one kind of change.

(While rewriting the moves block for bug 3, ~40 common moves were accidentally dropped from
the vocabulary. Caught by scores falling where no edit had been made. **Vocabulary files
need a length assertion.**)

### The line-wrap regression

Answers are wrapped at ~98 columns. Dozens of string-replacement edits joined prose past
that limit, producing 300-character lines that made diffs unreadable.

Fix: a re-wrapper that is aware of fenced code blocks (never touch them — ASCII diagrams
depend on exact column alignment) and preserves list and blockquote prefixes. Run as its own
commit (`deb16b2`), for the same separability reason as above.

**Lesson:** if the corpus has a formatting invariant, the formatter must be a script that
runs as part of the loop, not a thing done by eye.

### `git add -A` collided with a concurrent worker

While a second agent was writing `TERMINOLOGY.md`, a `git add -A` in the main loop swept its
half-finished file into an unrelated commit.

Fix, now a standing rule: **when any other process may be working in the tree, `git add`
explicit paths only.** Also caught by this: `scripts/__pycache__/*.pyc` had been tracked
since early on — a `.gitignore` should exist before the first commit, not after the first
accident.

### The edit-miss rate rose in later waves

By wave 18, six string replacements in that wave failed to match. Cause: composing edits
from *remembered* file contents after many rounds of changes. The remembered text had
drifted from what was on disk.

Fix, applied from wave 19: `grep` or `sed -n` the actual current text immediately before
composing any replacement. The miss rate went to near zero.

**Lesson:** in a long editing session, memory of file contents decays faster than confidence
in that memory does. Re-read before every edit; it is cheaper than a failed edit.

### The tooling that did not exist

A request came in to check in "the scorer and ledger and the LLM revision calls and prompts
scripts". The scorer and ledger existed. **The LLM revision scripts did not — every revision
so far had been written by hand.**

The only correct response was to say so, and then build them. `scripts/revise.py` carries
that fact in its docstring so nobody later infers a provenance for the committed revisions
that they do not have.

**Lesson:** a request that presupposes an artefact is not authorisation to retrofit its
provenance. Correct the premise, then satisfy the request going forward.

---

## Part 2 — What worked

### Serious answer first, always

The Pokémon answer is a translation, not a sibling. Written second, from the finished
serious answer, every Pokémon paragraph has a technical paragraph it is accountable to.
Written in parallel, they drift within one page.

### Named entities that are *load-bearing*

The score rewards named entities, but the answers that genuinely improved are the ones where
the real Pokémon fact does analytical work the abstraction wasn't doing. The biggest wins:

| Answer | Substitution | Why it worked |
| --- | --- | --- |
| Q078 (+75.8) | Kanto's eight Gym Leaders as the eight stages of a pipeline | The Gyms have a *canonical order*, so the analogy carries sequencing for free. |
| Q060 | Competitive play's real Evasion and OHKO clauses as safety policy | An actual rules document, written by a community, banning strategies that break the game — a genuine structural match, not a costume. |
| Q072 / Q081 | EV spreads as parameter budgets | EVs are literally a fixed budget allocated across dimensions with diminishing returns. |
| Q030 | Blissey's 255 base HP as the quantisation outlier | A real outlier in a real distribution beats an invented one. |
| Q071 | The Lake of Rage red Gyarados for rare-event sampling | A single canonical known-location rare encounter — exactly the shape of the problem. |

**The pattern:** the best substitutions are ones where Pokémon *already contains* the
structure, so you are pointing at it rather than dressing something up as it. When you are
straining to make a species fit, the abstraction was probably the honest choice.

### Deterministic scoring, committed

Because the scorer has no model in the loop, `git diff LEDGER.md` between two commits *is*
the change in Pokémon-ness. That made "improve the low scorers and track it" a mechanical
loop instead of a judgement call, and made `ledger_history.py` possible at all: the trend
table is reconstructed from git, not from a log that has to be maintained.

### One wave, one commit

Twenty waves, twenty commits, one ledger row each. Bisectable, reviewable, and immediately
legible as a trend. Batching five waves into one commit would have destroyed the entire
history for no gain.

### The conventions table

`TERMINOLOGY.md`'s ~200-row analogy-conventions table (each Pokémon prop mapped to the
concept it consistently stands for) started as a reader aid and became the corpus's
consistency mechanism. Once a mapping is written down, later answers reuse it, and the
dataset develops a shared vocabulary instead of 100 unrelated metaphors.

### The revision guard

`revise.py` reverts an LLM edit unless it clears the score gain **and** keeps front matter
byte-identical **and** still passes `validate.py`. Given a scored objective, a model will
keyword-stuff; the guard means the worst outcome of a bad generation is a no-op.

---

## Part 3 — The meta-lesson

### The score is a search tool, not a target

Per-wave gains, in order:

```
+2.9  +3.7  +2.9  +2.2  +2.7  +1.6  +1.8  +1.8  +1.8  +1.5
+0.9  +1.0  +0.8  +1.3  +1.0  +1.1  +1.0  +0.6  +0.6
```

Mean 22.4 to 55.2 corpus-wide, with every zero-scoring answer eliminated and the minimum
rising from 0.0 to 38.5. But the flattening is the honest signal: the cheap wins were real
improvements, and past roughly wave 15 the remaining low scorers are answers whose analogy
is *structural* — a pipeline, a trade-off curve, a distribution shift — where forcing in
species names would trade clarity for score.

This is not an abstract worry. **The dataset contains its own warning.** Q021 (reward model
over-optimisation) and Q038 (LLM-as-judge bias) are answers explaining exactly this failure
mode. Optimising this corpus against a proxy metric while it explains why that goes wrong
would be a nice piece of irony and a worse dataset.

So `LEDGER.md` carries a "What this score does not measure" section, and it says the score
is a search tool for finding answers worth re-reading — not a target. **A low score is a
question. It is not a defect.**

### Report the flattening

When gains fell to +0.6, that was reported rather than presented as continued progress. An
improvement loop that reports diminishing returns honestly can be stopped at the right point
by whoever is running it. One that reports every wave as a win cannot.
