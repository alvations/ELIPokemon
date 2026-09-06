---
id: "111"
slug: cross-lingual-embedding-alignment
style: serious
category: multilingual
difficulty: intermediate
question: "How do embedding spaces for different languages get aligned?"
tags: [muse, procrustes, csls, isomorphism, bilingual-lexicon, hubness]
---

# Aligning embedding spaces across languages

Train word embeddings on English and on Italian separately and you get two clouds with similar
*shape* — the geometry of "king is to queen as man is to woman" recurs in both — but arbitrary
orientation. [Mikolov et al. (2013)](https://arxiv.org/abs/1309.4168) observed this and proposed
learning a linear map `W` that rotates one space onto the other using a seed dictionary.

## The recipe

With a seed dictionary of `n` translation pairs `(x_i, z_i)`, solve

$$W^\star = \arg\min_W \sum_i \lVert W x_i - z_i \rVert^2 \quad \text{s.t. } W^\top W = I$$

Constraining `W` to be orthogonal (the **Procrustes** problem) has a closed form via SVD,
preserves distances, and works much better than an unconstrained map. Then iterate: use the
current `W` to induce new pairs, re-solve, repeat — the self-learning loop that makes tiny seed
dictionaries viable ([Artetxe et al., 2018](https://aclanthology.org/P18-1073/)).

[MUSE](https://arxiv.org/abs/1710.04087) (Conneau et al., 2017) removed the dictionary entirely:
an adversarial discriminator tries to tell mapped source vectors from target vectors, giving a
rough `W`, which Procrustes then refines on the confident pairs.

```
   EN space              IT space              After Procrustes
   ┌──────────┐          ┌──────────┐          ┌──────────┐
   │ king     │          │  gatto   │          │ king/re  │
   │   queen  │    +     │ re       │    ──►   │  queen/  │
   │ cat      │          │    regina│          │   regina │
   └──────────┘          └──────────┘          │ cat/gatto│
   same shape, different orientation           └──────────┘
```

## Two failure modes that define the field

**Hubness.** In high dimensions a few vectors are the nearest neighbour of a huge number of
points. Naive nearest-neighbour retrieval keeps returning those hubs. **CSLS** — cross-domain
similarity local scaling — fixes it by penalising points whose neighbourhood is densely
populated, and it is a bigger accuracy win than most changes to the mapping itself.

**The isomorphism assumption is false for the pairs you care about.**
[Søgaard et al. (2018)](https://aclanthology.org/P18-1072/) showed unsupervised alignment
degrades sharply when the two languages are typologically distant, when their corpora are from
different domains, or when one corpus is small — which is exactly the low-resource case.
[Vulić et al. (2019)](https://aclanthology.org/D19-1449/) found fully unsupervised methods often
fail outright on such pairs while a 500-word seed dictionary succeeds. If you can get a small
dictionary, get one.

## Where this sits today

Post-hoc alignment of static embeddings has largely been superseded by **joint multilingual
pretraining**, which produces a shared space by construction, and by sentence-level encoders
trained on parallel data (question 125). The alignment literature still matters for three
reasons: bilingual lexicon induction for genuinely unresourced languages; aligning a new
language's embeddings onto an existing model during vocabulary expansion; and as the clearest
statement of *why* multilingual spaces are only approximately shared.

## What an interviewer digs into next

* Why constrain the mapping to be orthogonal?
* What is hubness, and why does CSLS help more than a better objective?
* When does unsupervised alignment fail, and what is the cheapest fix?
* Do contextual models make this obsolete, or just implicit?
