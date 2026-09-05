# Pokémon-ness ledger

How much each Pokémon answer actually leans on **named** Pokémon entities —
real species, moves, items, abilities, characters, places — rather than generic
furniture ("a Trainer", "a Gym", "a battle"). Generic terms are the denominator,
not the numerator.

Regenerate with `python3 scripts/pokemon_score.py`. Scoring is deterministic, so
the diff between two commits of this file is the change in Pokémon-ness.

```
score = breadth (0-45) + density (0-35) + specificity (0-20)
  breadth      distinct named entities used
  density      named-entity mentions per 100 words
  specificity  named / (named + generic) mentions
```

**102 answers · mean 51.9 · median 49.9 · min 31.5 (094) · max 100.0 (101)**

| band | range | answers |
| --- | --- | --- |
| excellent | 80-100 | 2 |
| strong | 65-79 | 10 |
| adequate | 50-64 | 38 |
| thin | 35-49 | 51 |
| generic | 0-34 | 1 |

## Every answer, lowest first

| score | band | id | answer | distinct | named | generic | per 100w |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| **31.5** | generic | [`094`](answers/pokemon/094-multimodal-models.md) | multimodal-models | 5 | 7 | 30 | 0.9 |
| **37.2** | thin | [`093`](answers/pokemon/093-diffusion-models.md) | diffusion-models | 3 | 8 | 15 | 1.1 |
| **38.9** | thin | [`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md) | encoder-decoder-vs-decoder-only | 8 | 9 | 56 | 1.2 |
| **39.0** | thin | [`088`](answers/pokemon/088-trees-forests-boosting.md) | trees-forests-boosting | 7 | 8 | 31 | 1.0 |
| **39.3** | thin | [`013`](answers/pokemon/013-context-length-limits.md) | context-length-limits | 7 | 10 | 55 | 1.4 |
| **39.4** | thin | [`049`](answers/pokemon/049-chain-of-thought.md) | chain-of-thought | 4 | 9 | 20 | 1.3 |
| **39.5** | thin | [`030`](answers/pokemon/030-quantization.md) | quantization | 5 | 8 | 21 | 1.2 |
| **39.9** | thin | [`047`](answers/pokemon/047-query-rewriting-hyde.md) | query-rewriting-hyde | 6 | 7 | 19 | 1.0 |
| **40.1** | thin | [`074`](answers/pokemon/074-vanishing-exploding-gradients.md) | vanishing-exploding-gradients | 4 | 12 | 38 | 1.8 |
| **40.3** | thin | [`022`](answers/pokemon/022-ppo-for-llms.md) | ppo-for-llms | 6 | 12 | 48 | 1.5 |
| **40.7** | thin | [`044`](answers/pokemon/044-vector-databases-ann.md) | vector-databases-ann | 4 | 9 | 12 | 1.2 |
| **40.7** | thin | [`056`](answers/pokemon/056-multi-agent-systems.md) | multi-agent-systems | 7 | 9 | 37 | 1.3 |
| **40.8** | thin | [`072`](answers/pokemon/072-gradient-descent-optimizers.md) | gradient-descent-optimizers | 6 | 11 | 37 | 1.4 |
| **40.8** | thin | [`098`](answers/pokemon/098-training-serving-skew.md) | training-serving-skew | 6 | 8 | 24 | 1.2 |
| **40.9** | thin | [`003`](answers/pokemon/003-multi-head-attention.md) | multi-head-attention | 6 | 10 | 42 | 1.6 |
| **40.9** | thin | [`095`](answers/pokemon/095-data-drift.md) | data-drift | 6 | 9 | 27 | 1.3 |
| **40.9** | thin | [`096`](answers/pokemon/096-ab-testing-ml.md) | ab-testing-ml | 7 | 10 | 42 | 1.3 |
| **41.4** | thin | [`062`](answers/pokemon/062-red-teaming.md) | red-teaming | 8 | 8 | 33 | 1.1 |
| **41.8** | thin | [`005`](answers/pokemon/005-layer-normalization.md) | layer-normalization | 9 | 9 | 64 | 1.3 |
| **41.8** | thin | [`036`](answers/pokemon/036-perplexity.md) | perplexity | 6 | 10 | 37 | 1.6 |
| **42.0** | thin | [`059`](answers/pokemon/059-prompt-injection.md) | prompt-injection | 5 | 10 | 25 | 1.4 |
| **42.3** | thin | [`024`](answers/pokemon/024-constitutional-ai-rlaif.md) | constitutional-ai-rlaif | 8 | 9 | 37 | 1.2 |
| **42.8** | thin | [`058`](answers/pokemon/058-reasoning-models.md) | reasoning-models | 6 | 12 | 38 | 1.5 |
| **43.2** | thin | [`048`](answers/pokemon/048-evaluating-rag.md) | evaluating-rag | 5 | 11 | 26 | 1.5 |
| **43.2** | thin | [`050`](answers/pokemon/050-self-consistency.md) | self-consistency | 5 | 8 | 14 | 1.2 |
| **43.4** | thin | [`038`](answers/pokemon/038-llm-as-a-judge.md) | llm-as-a-judge | 7 | 11 | 47 | 1.6 |
| **43.4** | thin | [`083`](answers/pokemon/083-softmax-and-logsumexp.md) | softmax-and-logsumexp | 4 | 9 | 13 | 1.5 |
| **44.1** | thin | [`071`](answers/pokemon/071-class-imbalance.md) | class-imbalance | 4 | 10 | 4 | 1.6 |
| **44.5** | thin | [`069`](answers/pokemon/069-precision-recall-f1.md) | precision-recall-f1 | 5 | 8 | 11 | 1.3 |
| **44.8** | thin | [`025`](answers/pokemon/025-instruction-tuning.md) | instruction-tuning | 7 | 12 | 44 | 1.6 |
| **44.9** | thin | [`009`](answers/pokemon/009-mqa-and-gqa.md) | mqa-and-gqa | 6 | 10 | 31 | 1.8 |
| **45.0** | thin | [`027`](answers/pokemon/027-lora.md) | lora | 5 | 13 | 35 | 1.9 |
| **45.5** | thin | [`084`](answers/pokemon/084-cross-entropy-loss.md) | cross-entropy-loss | 4 | 11 | 16 | 1.7 |
| **45.6** | thin | [`015`](answers/pokemon/015-emergent-abilities.md) | emergent-abilities | 4 | 11 | 27 | 2.1 |
| **45.6** | thin | [`077`](answers/pokemon/077-mixed-precision-training.md) | mixed-precision-training | 6 | 7 | 9 | 1.1 |
| **45.8** | thin | [`028`](answers/pokemon/028-qlora.md) | qlora | 6 | 11 | 29 | 1.6 |
| **46.0** | thin | [`075`](answers/pokemon/075-batch-norm-vs-layer-norm.md) | batch-norm-vs-layer-norm | 7 | 12 | 37 | 1.6 |
| **46.2** | thin | [`064`](answers/pokemon/064-bias-variance-tradeoff.md) | bias-variance-tradeoff | 6 | 11 | 30 | 1.8 |
| **46.9** | thin | [`070`](answers/pokemon/070-roc-auc-vs-pr-auc.md) | roc-auc-vs-pr-auc | 6 | 7 | 3 | 1.3 |
| **47.0** | thin | [`090`](answers/pokemon/090-transfer-learning.md) | transfer-learning | 8 | 11 | 38 | 1.5 |
| **47.2** | thin | [`033`](answers/pokemon/033-speculative-decoding.md) | speculative-decoding | 8 | 12 | 50 | 1.8 |
| **47.2** | thin | [`089`](answers/pokemon/089-bagging-vs-boosting.md) | bagging-vs-boosting | 8 | 9 | 24 | 1.2 |
| **47.4** | thin | [`026`](answers/pokemon/026-catastrophic-forgetting.md) | catastrophic-forgetting | 8 | 9 | 29 | 1.5 |
| **47.5** | thin | [`020`](answers/pokemon/020-dpo-vs-ppo.md) | dpo-vs-ppo | 5 | 15 | 38 | 2.1 |
| **47.6** | thin | [`076`](answers/pokemon/076-learning-rate-schedules.md) | learning-rate-schedules | 7 | 8 | 15 | 1.1 |
| **47.7** | thin | [`045`](answers/pokemon/045-hybrid-search-reranking.md) | hybrid-search-reranking | 6 | 10 | 19 | 1.4 |
| **47.8** | thin | [`002`](answers/pokemon/002-positional-encodings-rope.md) | positional-encodings-rope | 8 | 10 | 30 | 1.4 |
| **48.3** | thin | [`065`](answers/pokemon/065-overfitting.md) | overfitting | 7 | 11 | 31 | 1.7 |
| **48.7** | thin | [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md) | teacher-forcing-exposure-bias | 9 | 10 | 45 | 1.7 |
| **48.9** | thin | [`039`](answers/pokemon/039-benchmark-contamination.md) | benchmark-contamination | 7 | 13 | 40 | 1.9 |
| **49.8** | thin | [`035`](answers/pokemon/035-beam-search.md) | beam-search | 6 | 13 | 32 | 2.0 |
| **49.9** | thin | [`061`](answers/pokemon/061-guardrails-moderation.md) | guardrails-moderation | 8 | 11 | 29 | 1.5 |
| **50.0** | adequate | [`097`](answers/pokemon/097-serving-cost-latency.md) | serving-cost-latency | 10 | 11 | 48 | 1.5 |
| **50.2** | adequate | [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md) | finetuning-vs-peft-vs-prompting | 8 | 11 | 31 | 1.6 |
| **50.4** | adequate | [`032`](answers/pokemon/032-pruning-and-sparsity.md) | pruning-and-sparsity | 7 | 11 | 9 | 1.4 |
| **50.8** | adequate | [`012`](answers/pokemon/012-tokenization-bpe.md) | tokenization-bpe | 7 | 10 | 16 | 1.4 |
| **51.2** | adequate | [`014`](answers/pokemon/014-scaling-laws.md) | scaling-laws | 9 | 13 | 55 | 1.9 |
| **51.5** | adequate | [`100`](answers/pokemon/100-fairness-bias-privacy.md) | fairness-bias-privacy | 7 | 12 | 21 | 1.5 |
| **51.7** | adequate | [`011`](answers/pokemon/011-mixture-of-experts.md) | mixture-of-experts | 7 | 13 | 31 | 1.9 |
| **52.0** | adequate | [`081`](answers/pokemon/081-batch-size-and-lr.md) | batch-size-and-lr | 8 | 13 | 35 | 1.8 |
| **52.1** | adequate | [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md) | cross-encoder-vs-bi-encoder | 7 | 10 | 17 | 1.6 |
| **52.2** | adequate | [`068`](answers/pokemon/068-cross-validation.md) | cross-validation | 7 | 11 | 23 | 1.8 |
| **52.3** | adequate | [`091`](answers/pokemon/091-self-supervised-learning.md) | self-supervised-learning | 8 | 12 | 31 | 1.8 |
| **52.5** | adequate | [`060`](answers/pokemon/060-jailbreaks.md) | jailbreaks | 9 | 13 | 34 | 1.5 |
| **53.2** | adequate | [`007`](answers/pokemon/007-transformer-feed-forward-block.md) | transformer-feed-forward-block | 7 | 10 | 16 | 1.7 |
| **53.4** | adequate | [`092`](answers/pokemon/092-contrastive-learning.md) | contrastive-learning | 4 | 18 | 20 | 2.6 |
| **53.6** | adequate | [`052`](answers/pokemon/052-context-engineering.md) | context-engineering | 8 | 11 | 23 | 1.6 |
| **53.6** | adequate | [`057`](answers/pokemon/057-test-time-compute.md) | test-time-compute | 10 | 12 | 41 | 1.7 |
| **53.9** | adequate | [`023`](answers/pokemon/023-grpo-reasoning.md) | grpo-reasoning | 7 | 15 | 35 | 2.1 |
| **54.4** | adequate | [`040`](answers/pokemon/040-hallucination.md) | hallucination | 7 | 14 | 23 | 1.9 |
| **54.8** | adequate | [`063`](answers/pokemon/063-model-calibration.md) | model-calibration | 7 | 13 | 17 | 1.9 |
| **55.2** | adequate | [`073`](answers/pokemon/073-backpropagation.md) | backpropagation | 8 | 12 | 12 | 1.6 |
| **55.5** | adequate | [`079`](answers/pokemon/079-parallelism-strategies.md) | parallelism-strategies | 8 | 15 | 58 | 2.6 |
| **55.6** | adequate | [`053`](answers/pokemon/053-react-agents.md) | react-agents | 10 | 13 | 39 | 1.7 |
| **57.4** | adequate | [`018`](answers/pokemon/018-pretraining-sft-rlhf.md) | pretraining-sft-rlhf | 10 | 13 | 40 | 2.0 |
| **57.4** | adequate | [`082`](answers/pokemon/082-activation-functions.md) | activation-functions | 8 | 12 | 10 | 1.9 |
| **57.9** | adequate | [`019`](answers/pokemon/019-rlhf-end-to-end.md) | rlhf-end-to-end | 10 | 13 | 32 | 1.8 |
| **58.1** | adequate | [`087`](answers/pokemon/087-curse-of-dimensionality.md) | curse-of-dimensionality | 10 | 12 | 31 | 1.8 |
| **58.3** | adequate | [`055`](answers/pokemon/055-model-context-protocol.md) | model-context-protocol | 11 | 11 | 29 | 1.6 |
| **58.5** | adequate | [`042`](answers/pokemon/042-chunking-strategies.md) | chunking-strategies | 8 | 13 | 7 | 2.0 |
| **58.5** | adequate | [`080`](answers/pokemon/080-zero-and-fsdp.md) | zero-and-fsdp | 7 | 19 | 55 | 2.9 |
| **58.8** | adequate | [`099`](answers/pokemon/099-ml-system-design.md) | ml-system-design | 11 | 14 | 47 | 1.9 |
| **59.9** | adequate | [`041`](answers/pokemon/041-rag-vs-finetuning.md) | rag-vs-finetuning | 10 | 13 | 26 | 1.7 |
| **60.5** | adequate | [`021`](answers/pokemon/021-reward-models.md) | reward-models | 9 | 13 | 24 | 2.0 |
| **60.7** | adequate | [`043`](answers/pokemon/043-embeddings.md) | embeddings | 10 | 12 | 13 | 1.7 |
| **61.8** | adequate | [`010`](answers/pokemon/010-flash-attention.md) | flash-attention | 10 | 11 | 19 | 1.8 |
| **62.0** | adequate | [`031`](answers/pokemon/031-knowledge-distillation.md) | knowledge-distillation | 5 | 22 | 38 | 3.3 |
| **62.7** | adequate | [`034`](answers/pokemon/034-sampling-temperature-top-p.md) | sampling-temperature-top-p | 7 | 19 | 25 | 2.8 |
| **62.8** | adequate | [`054`](answers/pokemon/054-tool-calling.md) | tool-calling | 7 | 20 | 29 | 2.8 |
| **64.3** | adequate | [`008`](answers/pokemon/008-kv-cache.md) | kv-cache | 11 | 15 | 50 | 2.6 |
| **65.4** | strong | [`067`](answers/pokemon/067-dropout.md) | dropout | 10 | 15 | 34 | 2.5 |
| **67.5** | strong | [`102`](answers/pokemon/102-tokenizer-fairness-token-premium.md) | tokenizer-fairness-token-premium | 10 | 18 | 32 | 2.5 |
| **67.6** | strong | [`086`](answers/pokemon/086-pca.md) | pca | 13 | 15 | 43 | 2.2 |
| **70.6** | strong | [`066`](answers/pokemon/066-l1-vs-l2-regularization.md) | l1-vs-l2-regularization | 6 | 27 | 20 | 4.5 |
| **71.2** | strong | [`051`](answers/pokemon/051-in-context-learning.md) | in-context-learning | 9 | 20 | 19 | 3.2 |
| **73.7** | strong | [`016`](answers/pokemon/016-next-token-prediction.md) | next-token-prediction | 14 | 17 | 43 | 2.4 |
| **74.2** | strong | [`001`](answers/pokemon/001-attention-mechanisms.md) | attention-mechanisms | 9 | 29 | 57 | 3.6 |
| **75.8** | strong | [`078`](answers/pokemon/078-gradient-checkpointing.md) | gradient-checkpointing | 8 | 28 | 17 | 4.9 |
| **75.9** | strong | [`037`](answers/pokemon/037-evaluating-llms.md) | evaluating-llms | 14 | 16 | 34 | 2.4 |
| **78.4** | strong | [`085`](answers/pokemon/085-label-smoothing.md) | label-smoothing | 9 | 28 | 15 | 5.1 |
| **88.8** | excellent | [`006`](answers/pokemon/006-residual-connections.md) | residual-connections | 13 | 34 | 42 | 5.7 |
| **100.0** | excellent | [`101`](answers/pokemon/101-cross-lingual-transfer.md) | cross-lingual-transfer | 23 | 46 | 19 | 6.3 |

## What this score does not measure

It counts named entities. It cannot tell whether they are doing any work.

That makes it a **proxy**, and this repository contains an answer about exactly
what happens when you optimise against a proxy hard enough — see
[`021`](answers/pokemon/021-reward-models.md) on Goodharting a reward model, and
[`038`](answers/pokemon/038-llm-as-a-judge.md) on judges that reward surface
features. A Pokémon answer can be stuffed with species names and be worse than the
vague one it replaced.

So the score is a **search tool, not a target**: it finds answers leaning on generic
furniture so a human can go and look. Every raise in this ledger's history came from
replacing an abstraction with a specific that made the analogy more concrete — the
eight Kanto Gym Leaders standing in for a generic eight-stage pipeline, EV spreads
standing in for "adjust something", the League's real evasion and OHKO clauses
standing in for "a banned move". Where no such substitution existed, the answer was
left alone at a low score.

A low score is a question, not a verdict.

