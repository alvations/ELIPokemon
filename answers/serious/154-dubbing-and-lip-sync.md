---
id: "154"
slug: dubbing-and-lip-sync
style: serious
category: translation
difficulty: advanced
question: "What makes translating for dubbing different from translating subtitles?"
tags: [dubbing, isochrony, lip-sync, phonetic-matching, alignment, av-translation]
---

# Translation for dubbing

Subtitles have a space constraint (question 144). Dubbing has a **time** constraint, a **phonetic**
constraint, and a **performance** constraint, and they bind simultaneously against a video you
cannot change.

## The three constraints

**1. Isochrony.** The translated line must occupy the same time as the original — start when the
mouth starts, end when it stops. Not approximately: a line that overruns collides with the next
speaker.

**2. Lip-sync proper.** In close-up, visible consonants must roughly match. The **bilabials**
(p, b, m) are the giveaway: the mouth closes completely, and every viewer notices when a closed
mouth produces a vowel. Open vowels at the end of a line matter for the same reason.

**3. Kinesic sync.** Gestures, nods and head shakes are locked to the original's rhythm. A
translation that puts the emphatic word somewhere else leaves the actor emphasising the wrong beat.

```
   original :  |  It's  |  im-POS-sible  |    !   |   ← 1.4s, closes on "p", emphasis mid-line
                  ▲         ▲                ▲
   bad dub  :  |     That cannot possibly happen  |  ← 2.1s, overruns, no closure, flat
   good dub :  |  But  |  that's  MAD-ness  |   !  |  ← 1.4s, "m" gives the closure, beat kept
```

Note that the good version is not the most accurate translation. **Dubbing trades semantic
precision for temporal and phonetic fit, deliberately**, and a translator who refuses to make that
trade produces unusable lines.

## Automatic dubbing pipelines

An automatic pipeline is question 153 plus timing:

```
   audio ─► ASR with word timestamps ─► MT with length control ─► TTS with duration control
                    │                            │                          │
              speaker diarization        prosodic alignment          time-stretching,
              (who is speaking)          (pauses in the right        pause insertion
                                          places)
```

The levers, in order of how much damage they do:

* **Length-controlled MT** (question 144) — generate candidates and select for duration fit. The
  cheapest and least damaging.
* **Pause redistribution** — the same words, different silences. Nearly free.
* **Speaking-rate adjustment** in synthesis. Small changes are inaudible; large ones sound rushed
  or drugged, and this is where bad automatic dubs give themselves away.
* **Time-stretching the audio** after the fact. Audible quickly. Last resort.

## What automation does badly

* **Performance.** A voice actor makes interpretive choices — irony, hesitation, subtext. TTS
  produces the average reading. This is the gap, and it is not narrowing as fast as the timing
  problem is.
* **Character consistency** across a series, including recasting when a character ages.
* **Songs**, which need singable, scannable, rhyming translations. This is verse writing, not
  translation.
* **Culture-bound references** that need transcreation (question 150) rather than rendering.

## Evaluation

Standard MT metrics are close to useless here, because the constraint they cannot see *is* the
product. Report:

* **Duration compliance** — fraction of lines within tolerance of the original.
* **Lip-sync scores** — automatic measures of viseme agreement, and human ratings for close-ups.
* **Quality on compliant lines**, so you can see what the constraint cost.
* **Viewer preference tests**, which remain the only measure that captures "does this feel dubbed".

## What an interviewer digs into next

* Why do bilabial consonants matter more than other sounds?
* Why is the most accurate translation often the wrong dubbing line?
* Which timing lever damages quality least, and which most?
* Why can't COMET evaluate a dub?
