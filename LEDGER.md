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

**100 answers · mean 24.0 · median 18.8 · min 0.0 (020) · max 88.8 (006)**

| band | range | answers |
| --- | --- | --- |
| excellent | 80-100 | 1 |
| strong | 65-79 | 5 |
| adequate | 50-64 | 7 |
| thin | 35-49 | 12 |
| generic | 0-34 | 75 |

## Every answer, lowest first

| score | band | id | answer | distinct | named | generic | per 100w |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| **0.0** | generic | [`020`](answers/pokemon/020-dpo-vs-ppo.md) | dpo-vs-ppo | 0 | 0 | 49 | 0.0 |
| **0.0** | generic | [`021`](answers/pokemon/021-reward-models.md) | reward-models | 0 | 0 | 31 | 0.0 |
| **0.0** | generic | [`028`](answers/pokemon/028-qlora.md) | qlora | 0 | 0 | 29 | 0.0 |
| **0.0** | generic | [`045`](answers/pokemon/045-hybrid-search-reranking.md) | hybrid-search-reranking | 0 | 0 | 15 | 0.0 |
| **0.0** | generic | [`048`](answers/pokemon/048-evaluating-rag.md) | evaluating-rag | 0 | 0 | 25 | 0.0 |
| **0.0** | generic | [`060`](answers/pokemon/060-jailbreaks.md) | jailbreaks | 0 | 0 | 33 | 0.0 |
| **0.0** | generic | [`062`](answers/pokemon/062-red-teaming.md) | red-teaming | 0 | 0 | 29 | 0.0 |
| **0.0** | generic | [`072`](answers/pokemon/072-gradient-descent-optimizers.md) | gradient-descent-optimizers | 0 | 0 | 25 | 0.0 |
| **0.0** | generic | [`075`](answers/pokemon/075-batch-norm-vs-layer-norm.md) | batch-norm-vs-layer-norm | 0 | 0 | 30 | 0.0 |
| **0.0** | generic | [`078`](answers/pokemon/078-gradient-checkpointing.md) | gradient-checkpointing | 0 | 0 | 20 | 0.0 |
| **0.0** | generic | [`081`](answers/pokemon/081-batch-size-and-lr.md) | batch-size-and-lr | 0 | 0 | 35 | 0.0 |
| **0.0** | generic | [`087`](answers/pokemon/087-curse-of-dimensionality.md) | curse-of-dimensionality | 0 | 0 | 31 | 0.0 |
| **0.0** | generic | [`088`](answers/pokemon/088-trees-forests-boosting.md) | trees-forests-boosting | 0 | 0 | 32 | 0.0 |
| **0.0** | generic | [`089`](answers/pokemon/089-bagging-vs-boosting.md) | bagging-vs-boosting | 0 | 0 | 28 | 0.0 |
| **0.0** | generic | [`096`](answers/pokemon/096-ab-testing-ml.md) | ab-testing-ml | 0 | 0 | 39 | 0.0 |
| **0.0** | generic | [`098`](answers/pokemon/098-training-serving-skew.md) | training-serving-skew | 0 | 0 | 28 | 0.0 |
| **4.8** | generic | [`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md) | encoder-decoder-vs-decoder-only | 1 | 1 | 58 | 0.1 |
| **5.0** | generic | [`097`](answers/pokemon/097-serving-cost-latency.md) | serving-cost-latency | 1 | 1 | 49 | 0.1 |
| **5.1** | generic | [`038`](answers/pokemon/038-llm-as-a-judge.md) | llm-as-a-judge | 1 | 1 | 49 | 0.2 |
| **5.7** | generic | [`094`](answers/pokemon/094-multimodal-models.md) | multimodal-models | 1 | 1 | 29 | 0.1 |
| **5.8** | generic | [`091`](answers/pokemon/091-self-supervised-learning.md) | self-supervised-learning | 1 | 1 | 30 | 0.2 |
| **7.5** | generic | [`079`](answers/pokemon/079-parallelism-strategies.md) | parallelism-strategies | 1 | 2 | 64 | 0.4 |
| **7.7** | generic | [`050`](answers/pokemon/050-self-consistency.md) | self-consistency | 1 | 1 | 14 | 0.1 |
| **7.9** | generic | [`076`](answers/pokemon/076-learning-rate-schedules.md) | learning-rate-schedules | 1 | 1 | 13 | 0.1 |
| **8.7** | generic | [`061`](answers/pokemon/061-guardrails-moderation.md) | guardrails-moderation | 1 | 2 | 30 | 0.3 |
| **8.9** | generic | [`041`](answers/pokemon/041-rag-vs-finetuning.md) | rag-vs-finetuning | 1 | 2 | 27 | 0.3 |
| **9.4** | generic | [`022`](answers/pokemon/022-ppo-for-llms.md) | ppo-for-llms | 1 | 3 | 48 | 0.4 |
| **9.8** | generic | [`077`](answers/pokemon/077-mixed-precision-training.md) | mixed-precision-training | 1 | 1 | 9 | 0.2 |
| **9.9** | generic | [`099`](answers/pokemon/099-ml-system-design.md) | ml-system-design | 2 | 2 | 49 | 0.3 |
| **10.3** | generic | [`090`](answers/pokemon/090-transfer-learning.md) | transfer-learning | 2 | 2 | 41 | 0.3 |
| **10.4** | generic | [`025`](answers/pokemon/025-instruction-tuning.md) | instruction-tuning | 1 | 3 | 41 | 0.5 |
| **10.7** | generic | [`024`](answers/pokemon/024-constitutional-ai-rlaif.md) | constitutional-ai-rlaif | 2 | 2 | 35 | 0.3 |
| **11.0** | generic | [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md) | finetuning-vs-peft-vs-prompting | 2 | 2 | 35 | 0.3 |
| **12.0** | generic | [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md) | cross-encoder-vs-bi-encoder | 1 | 2 | 16 | 0.3 |
| **12.3** | generic | [`052`](answers/pokemon/052-context-engineering.md) | context-engineering | 2 | 2 | 24 | 0.3 |
| **13.6** | generic | [`082`](answers/pokemon/082-activation-functions.md) | activation-functions | 1 | 2 | 12 | 0.3 |
| **13.8** | generic | [`070`](answers/pokemon/070-roc-auc-vs-pr-auc.md) | roc-auc-vs-pr-auc | 1 | 1 | 5 | 0.2 |
| **14.4** | generic | [`095`](answers/pokemon/095-data-drift.md) | data-drift | 2 | 3 | 29 | 0.4 |
| **14.8** | generic | [`073`](answers/pokemon/073-backpropagation.md) | backpropagation | 1 | 3 | 17 | 0.4 |
| **15.4** | generic | [`057`](answers/pokemon/057-test-time-compute.md) | test-time-compute | 3 | 3 | 42 | 0.4 |
| **15.9** | generic | [`039`](answers/pokemon/039-benchmark-contamination.md) | benchmark-contamination | 2 | 4 | 39 | 0.6 |
| **15.9** | generic | [`056`](answers/pokemon/056-multi-agent-systems.md) | multi-agent-systems | 3 | 3 | 37 | 0.4 |
| **16.4** | generic | [`037`](answers/pokemon/037-evaluating-llms.md) | evaluating-llms | 2 | 4 | 36 | 0.6 |
| **16.5** | generic | [`036`](answers/pokemon/036-perplexity.md) | perplexity | 2 | 4 | 37 | 0.7 |
| **16.8** | generic | [`023`](answers/pokemon/023-grpo-reasoning.md) | grpo-reasoning | 2 | 4 | 31 | 0.6 |
| **17.0** | generic | [`013`](answers/pokemon/013-context-length-limits.md) | context-length-limits | 3 | 4 | 53 | 0.6 |
| **17.4** | generic | [`065`](answers/pokemon/065-overfitting.md) | overfitting | 2 | 4 | 31 | 0.7 |
| **17.5** | generic | [`010`](answers/pokemon/010-flash-attention.md) | flash-attention | 2 | 3 | 19 | 0.5 |
| **18.0** | generic | [`009`](answers/pokemon/009-mqa-and-gqa.md) | mqa-and-gqa | 2 | 4 | 31 | 0.7 |
| **18.4** | generic | [`100`](answers/pokemon/100-fairness-bias-privacy.md) | fairness-bias-privacy | 1 | 5 | 23 | 0.6 |
| **18.8** | generic | [`005`](answers/pokemon/005-layer-normalization.md) | layer-normalization | 4 | 4 | 64 | 0.6 |
| **18.9** | generic | [`080`](answers/pokemon/080-zero-and-fsdp.md) | zero-and-fsdp | 2 | 6 | 58 | 0.9 |
| **19.8** | generic | [`067`](answers/pokemon/067-dropout.md) | dropout | 2 | 5 | 35 | 0.8 |
| **20.7** | generic | [`068`](answers/pokemon/068-cross-validation.md) | cross-validation | 1 | 5 | 21 | 0.8 |
| **20.8** | generic | [`027`](answers/pokemon/027-lora.md) | lora | 3 | 5 | 38 | 0.7 |
| **21.1** | generic | [`059`](answers/pokemon/059-prompt-injection.md) | prompt-injection | 3 | 4 | 24 | 0.6 |
| **21.8** | generic | [`012`](answers/pokemon/012-tokenization-bpe.md) | tokenization-bpe | 2 | 4 | 16 | 0.6 |
| **23.5** | generic | [`008`](answers/pokemon/008-kv-cache.md) | kv-cache | 4 | 5 | 49 | 0.9 |
| **23.5** | generic | [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md) | teacher-forcing-exposure-bias | 4 | 5 | 47 | 0.9 |
| **23.5** | generic | [`033`](answers/pokemon/033-speculative-decoding.md) | speculative-decoding | 3 | 7 | 53 | 1.0 |
| **25.2** | generic | [`084`](answers/pokemon/084-cross-entropy-loss.md) | cross-entropy-loss | 1 | 6 | 18 | 0.9 |
| **25.4** | generic | [`086`](answers/pokemon/086-pca.md) | pca | 5 | 5 | 43 | 0.7 |
| **26.1** | generic | [`018`](answers/pokemon/018-pretraining-sft-rlhf.md) | pretraining-sft-rlhf | 4 | 6 | 40 | 0.9 |
| **26.7** | generic | [`035`](answers/pokemon/035-beam-search.md) | beam-search | 3 | 7 | 36 | 1.1 |
| **26.8** | generic | [`071`](answers/pokemon/071-class-imbalance.md) | class-imbalance | 1 | 3 | 5 | 0.5 |
| **27.1** | generic | [`002`](answers/pokemon/002-positional-encodings-rope.md) | positional-encodings-rope | 4 | 6 | 32 | 0.9 |
| **28.2** | generic | [`055`](answers/pokemon/055-model-context-protocol.md) | model-context-protocol | 5 | 5 | 29 | 0.8 |
| **28.3** | generic | [`032`](answers/pokemon/032-pruning-and-sparsity.md) | pruning-and-sparsity | 1 | 5 | 9 | 0.7 |
| **28.7** | generic | [`019`](answers/pokemon/019-rlhf-end-to-end.md) | rlhf-end-to-end | 5 | 6 | 35 | 0.8 |
| **30.8** | generic | [`093`](answers/pokemon/093-diffusion-models.md) | diffusion-models | 2 | 6 | 13 | 0.9 |
| **31.2** | generic | [`030`](answers/pokemon/030-quantization.md) | quantization | 4 | 6 | 21 | 0.9 |
| **31.5** | generic | [`064`](answers/pokemon/064-bias-variance-tradeoff.md) | bias-variance-tradeoff | 3 | 8 | 29 | 1.3 |
| **31.6** | generic | [`014`](answers/pokemon/014-scaling-laws.md) | scaling-laws | 5 | 8 | 51 | 1.2 |
| **32.5** | generic | [`063`](answers/pokemon/063-model-calibration.md) | model-calibration | 2 | 7 | 15 | 1.0 |
| **34.7** | generic | [`058`](answers/pokemon/058-reasoning-models.md) | reasoning-models | 6 | 8 | 38 | 1.1 |
| **36.8** | thin | [`040`](answers/pokemon/040-hallucination.md) | hallucination | 3 | 10 | 23 | 1.3 |
| **37.3** | thin | [`053`](answers/pokemon/053-react-agents.md) | react-agents | 7 | 8 | 40 | 1.1 |
| **38.8** | thin | [`042`](answers/pokemon/042-chunking-strategies.md) | chunking-strategies | 3 | 8 | 7 | 1.3 |
| **39.1** | thin | [`069`](answers/pokemon/069-precision-recall-f1.md) | precision-recall-f1 | 4 | 6 | 11 | 1.0 |
| **39.4** | thin | [`049`](answers/pokemon/049-chain-of-thought.md) | chain-of-thought | 4 | 9 | 20 | 1.3 |
| **39.9** | thin | [`047`](answers/pokemon/047-query-rewriting-hyde.md) | query-rewriting-hyde | 6 | 7 | 19 | 1.0 |
| **40.1** | thin | [`074`](answers/pokemon/074-vanishing-exploding-gradients.md) | vanishing-exploding-gradients | 4 | 12 | 38 | 1.8 |
| **40.7** | thin | [`044`](answers/pokemon/044-vector-databases-ann.md) | vector-databases-ann | 4 | 9 | 12 | 1.2 |
| **40.9** | thin | [`003`](answers/pokemon/003-multi-head-attention.md) | multi-head-attention | 6 | 10 | 42 | 1.6 |
| **43.4** | thin | [`083`](answers/pokemon/083-softmax-and-logsumexp.md) | softmax-and-logsumexp | 4 | 9 | 13 | 1.5 |
| **45.6** | thin | [`015`](answers/pokemon/015-emergent-abilities.md) | emergent-abilities | 4 | 11 | 27 | 2.1 |
| **47.4** | thin | [`026`](answers/pokemon/026-catastrophic-forgetting.md) | catastrophic-forgetting | 8 | 9 | 29 | 1.5 |
| **51.7** | adequate | [`011`](answers/pokemon/011-mixture-of-experts.md) | mixture-of-experts | 7 | 13 | 31 | 1.9 |
| **53.2** | adequate | [`007`](answers/pokemon/007-transformer-feed-forward-block.md) | transformer-feed-forward-block | 7 | 10 | 16 | 1.7 |
| **53.4** | adequate | [`092`](answers/pokemon/092-contrastive-learning.md) | contrastive-learning | 4 | 18 | 20 | 2.6 |
| **60.7** | adequate | [`043`](answers/pokemon/043-embeddings.md) | embeddings | 10 | 12 | 13 | 1.7 |
| **62.0** | adequate | [`031`](answers/pokemon/031-knowledge-distillation.md) | knowledge-distillation | 5 | 22 | 38 | 3.3 |
| **62.7** | adequate | [`034`](answers/pokemon/034-sampling-temperature-top-p.md) | sampling-temperature-top-p | 7 | 19 | 25 | 2.8 |
| **62.8** | adequate | [`054`](answers/pokemon/054-tool-calling.md) | tool-calling | 7 | 20 | 29 | 2.8 |
| **70.6** | strong | [`066`](answers/pokemon/066-l1-vs-l2-regularization.md) | l1-vs-l2-regularization | 6 | 27 | 20 | 4.5 |
| **71.2** | strong | [`051`](answers/pokemon/051-in-context-learning.md) | in-context-learning | 9 | 20 | 19 | 3.2 |
| **73.7** | strong | [`016`](answers/pokemon/016-next-token-prediction.md) | next-token-prediction | 14 | 17 | 43 | 2.4 |
| **74.2** | strong | [`001`](answers/pokemon/001-attention-mechanisms.md) | attention-mechanisms | 9 | 29 | 57 | 3.6 |
| **78.4** | strong | [`085`](answers/pokemon/085-label-smoothing.md) | label-smoothing | 9 | 28 | 15 | 5.1 |
| **88.8** | excellent | [`006`](answers/pokemon/006-residual-connections.md) | residual-connections | 13 | 34 | 42 | 5.7 |

