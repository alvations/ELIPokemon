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

**156 answers · mean 59.3 · median 55.2 · min 38.5 (094) · max 100.0 (111)**

| band | range | answers |
| --- | --- | --- |
| excellent | 80-100 | 17 |
| strong | 65-79 | 25 |
| adequate | 50-64 | 69 |
| thin | 35-49 | 45 |
| generic | 0-34 | 0 |

## Every answer, lowest first

| score | band | id | answer | distinct | named | generic | per 100w |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| **38.5** | thin | [`094`](answers/pokemon/094-multimodal-models.md) | multimodal-models | 6 | 9 | 30 | 1.1 |
| **40.5** | thin | [`147`](answers/pokemon/147-multimodal-benchmarks-contamination.md) | multimodal-benchmarks-contamination | 6 | 7 | 18 | 1.0 |
| **41.8** | thin | [`005`](answers/pokemon/005-layer-normalization.md) | layer-normalization | 9 | 9 | 64 | 1.3 |
| **41.8** | thin | [`036`](answers/pokemon/036-perplexity.md) | perplexity | 6 | 10 | 37 | 1.6 |
| **42.0** | thin | [`059`](answers/pokemon/059-prompt-injection.md) | prompt-injection | 5 | 10 | 25 | 1.4 |
| **42.1** | thin | [`022`](answers/pokemon/022-ppo-for-llms.md) | ppo-for-llms | 6 | 13 | 48 | 1.6 |
| **42.3** | thin | [`024`](answers/pokemon/024-constitutional-ai-rlaif.md) | constitutional-ai-rlaif | 8 | 9 | 37 | 1.2 |
| **42.8** | thin | [`058`](answers/pokemon/058-reasoning-models.md) | reasoning-models | 6 | 12 | 38 | 1.5 |
| **43.1** | thin | [`003`](answers/pokemon/003-multi-head-attention.md) | multi-head-attention | 6 | 11 | 42 | 1.8 |
| **43.2** | thin | [`048`](answers/pokemon/048-evaluating-rag.md) | evaluating-rag | 5 | 11 | 26 | 1.5 |
| **43.2** | thin | [`050`](answers/pokemon/050-self-consistency.md) | self-consistency | 5 | 8 | 14 | 1.2 |
| **43.4** | thin | [`038`](answers/pokemon/038-llm-as-a-judge.md) | llm-as-a-judge | 7 | 11 | 47 | 1.6 |
| **43.4** | thin | [`083`](answers/pokemon/083-softmax-and-logsumexp.md) | softmax-and-logsumexp | 4 | 9 | 13 | 1.5 |
| **43.4** | thin | [`138`](answers/pokemon/138-speech-language-models.md) | speech-language-models | 5 | 10 | 11 | 1.2 |
| **44.1** | thin | [`071`](answers/pokemon/071-class-imbalance.md) | class-imbalance | 4 | 10 | 4 | 1.6 |
| **44.8** | thin | [`025`](answers/pokemon/025-instruction-tuning.md) | instruction-tuning | 7 | 12 | 44 | 1.6 |
| **44.9** | thin | [`009`](answers/pokemon/009-mqa-and-gqa.md) | mqa-and-gqa | 6 | 10 | 31 | 1.8 |
| **45.0** | thin | [`027`](answers/pokemon/027-lora.md) | lora | 5 | 13 | 35 | 1.9 |
| **45.3** | thin | [`047`](answers/pokemon/047-query-rewriting-hyde.md) | query-rewriting-hyde | 7 | 8 | 19 | 1.2 |
| **45.5** | thin | [`084`](answers/pokemon/084-cross-entropy-loss.md) | cross-entropy-loss | 4 | 11 | 16 | 1.7 |
| **45.5** | thin | [`096`](answers/pokemon/096-ab-testing-ml.md) | ab-testing-ml | 8 | 11 | 42 | 1.5 |
| **45.6** | thin | [`015`](answers/pokemon/015-emergent-abilities.md) | emergent-abilities | 4 | 11 | 27 | 2.1 |
| **45.6** | thin | [`077`](answers/pokemon/077-mixed-precision-training.md) | mixed-precision-training | 6 | 7 | 9 | 1.1 |
| **45.8** | thin | [`028`](answers/pokemon/028-qlora.md) | qlora | 6 | 11 | 29 | 1.6 |
| **45.8** | thin | [`095`](answers/pokemon/095-data-drift.md) | data-drift | 7 | 10 | 27 | 1.4 |
| **46.2** | thin | [`064`](answers/pokemon/064-bias-variance-tradeoff.md) | bias-variance-tradeoff | 6 | 11 | 30 | 1.8 |
| **46.6** | thin | [`049`](answers/pokemon/049-chain-of-thought.md) | chain-of-thought | 5 | 11 | 20 | 1.6 |
| **47.0** | thin | [`090`](answers/pokemon/090-transfer-learning.md) | transfer-learning | 8 | 11 | 38 | 1.5 |
| **47.1** | thin | [`142`](answers/pokemon/142-gender-bias-in-translation.md) | gender-bias-in-translation | 4 | 15 | 13 | 1.9 |
| **47.2** | thin | [`033`](answers/pokemon/033-speculative-decoding.md) | speculative-decoding | 8 | 12 | 50 | 1.8 |
| **47.2** | thin | [`089`](answers/pokemon/089-bagging-vs-boosting.md) | bagging-vs-boosting | 8 | 9 | 24 | 1.2 |
| **47.4** | thin | [`026`](answers/pokemon/026-catastrophic-forgetting.md) | catastrophic-forgetting | 8 | 9 | 29 | 1.5 |
| **47.4** | thin | [`153`](answers/pokemon/153-speech-to-speech-translation.md) | speech-to-speech-translation | 6 | 8 | 11 | 1.4 |
| **47.5** | thin | [`020`](answers/pokemon/020-dpo-vs-ppo.md) | dpo-vs-ppo | 5 | 15 | 38 | 2.1 |
| **47.6** | thin | [`076`](answers/pokemon/076-learning-rate-schedules.md) | learning-rate-schedules | 7 | 8 | 15 | 1.1 |
| **47.8** | thin | [`002`](answers/pokemon/002-positional-encodings-rope.md) | positional-encodings-rope | 8 | 10 | 30 | 1.4 |
| **47.9** | thin | [`098`](answers/pokemon/098-training-serving-skew.md) | training-serving-skew | 7 | 10 | 25 | 1.5 |
| **48.1** | thin | [`088`](answers/pokemon/088-trees-forests-boosting.md) | trees-forests-boosting | 9 | 10 | 32 | 1.3 |
| **48.3** | thin | [`065`](answers/pokemon/065-overfitting.md) | overfitting | 7 | 11 | 31 | 1.7 |
| **48.5** | thin | [`069`](answers/pokemon/069-precision-recall-f1.md) | precision-recall-f1 | 6 | 9 | 11 | 1.5 |
| **48.7** | thin | [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md) | teacher-forcing-exposure-bias | 9 | 10 | 45 | 1.7 |
| **48.9** | thin | [`039`](answers/pokemon/039-benchmark-contamination.md) | benchmark-contamination | 7 | 13 | 40 | 1.9 |
| **49.3** | thin | [`074`](answers/pokemon/074-vanishing-exploding-gradients.md) | vanishing-exploding-gradients | 6 | 14 | 38 | 2.1 |
| **49.7** | thin | [`133`](answers/pokemon/133-terminology-glossary-enforcement.md) | terminology-glossary-enforcement | 6 | 12 | 3 | 1.6 |
| **49.9** | thin | [`061`](answers/pokemon/061-guardrails-moderation.md) | guardrails-moderation | 8 | 11 | 29 | 1.5 |
| **50.0** | adequate | [`097`](answers/pokemon/097-serving-cost-latency.md) | serving-cost-latency | 10 | 11 | 48 | 1.5 |
| **50.2** | adequate | [`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md) | encoder-decoder-vs-decoder-only | 10 | 12 | 53 | 1.6 |
| **50.2** | adequate | [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md) | finetuning-vs-peft-vs-prompting | 8 | 11 | 31 | 1.6 |
| **50.3** | adequate | [`141`](answers/pokemon/141-formality-and-honorifics.md) | formality-and-honorifics | 6 | 12 | 14 | 1.7 |
| **50.4** | adequate | [`032`](answers/pokemon/032-pruning-and-sparsity.md) | pruning-and-sparsity | 7 | 11 | 9 | 1.4 |
| **50.6** | adequate | [`062`](answers/pokemon/062-red-teaming.md) | red-teaming | 10 | 10 | 34 | 1.3 |
| **50.6** | adequate | [`093`](answers/pokemon/093-diffusion-models.md) | diffusion-models | 5 | 15 | 14 | 2.0 |
| **50.8** | adequate | [`012`](answers/pokemon/012-tokenization-bpe.md) | tokenization-bpe | 7 | 10 | 16 | 1.4 |
| **51.3** | adequate | [`072`](answers/pokemon/072-gradient-descent-optimizers.md) | gradient-descent-optimizers | 8 | 14 | 38 | 1.7 |
| **51.3** | adequate | [`129`](answers/pokemon/129-mt-evaluation-beyond-bleu.md) | mt-evaluation-beyond-bleu | 8 | 11 | 22 | 1.3 |
| **51.7** | adequate | [`011`](answers/pokemon/011-mixture-of-experts.md) | mixture-of-experts | 7 | 13 | 31 | 1.9 |
| **51.8** | adequate | [`119`](answers/pokemon/119-cross-modal-attention.md) | cross-modal-attention | 7 | 14 | 20 | 1.6 |
| **52.0** | adequate | [`081`](answers/pokemon/081-batch-size-and-lr.md) | batch-size-and-lr | 8 | 13 | 35 | 1.8 |
| **52.1** | adequate | [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md) | cross-encoder-vs-bi-encoder | 7 | 10 | 17 | 1.6 |
| **52.2** | adequate | [`068`](answers/pokemon/068-cross-validation.md) | cross-validation | 7 | 11 | 23 | 1.8 |
| **52.2** | adequate | [`135`](answers/pokemon/135-llm-versus-nmt-translation.md) | llm-versus-nmt-translation | 6 | 15 | 3 | 1.9 |
| **52.3** | adequate | [`091`](answers/pokemon/091-self-supervised-learning.md) | self-supervised-learning | 8 | 12 | 31 | 1.8 |
| **52.5** | adequate | [`060`](answers/pokemon/060-jailbreaks.md) | jailbreaks | 9 | 13 | 34 | 1.5 |
| **52.7** | adequate | [`125`](answers/pokemon/125-speech-recognition.md) | speech-recognition | 8 | 12 | 8 | 1.4 |
| **53.1** | adequate | [`045`](answers/pokemon/045-hybrid-search-reranking.md) | hybrid-search-reranking | 7 | 12 | 19 | 1.7 |
| **53.2** | adequate | [`007`](answers/pokemon/007-transformer-feed-forward-block.md) | transformer-feed-forward-block | 7 | 10 | 16 | 1.7 |
| **53.4** | adequate | [`092`](answers/pokemon/092-contrastive-learning.md) | contrastive-learning | 4 | 18 | 20 | 2.6 |
| **53.4** | adequate | [`123`](answers/pokemon/123-document-understanding-ocr.md) | document-understanding-ocr | 9 | 10 | 8 | 1.1 |
| **53.6** | adequate | [`052`](answers/pokemon/052-context-engineering.md) | context-engineering | 8 | 11 | 23 | 1.6 |
| **53.6** | adequate | [`057`](answers/pokemon/057-test-time-compute.md) | test-time-compute | 10 | 12 | 41 | 1.7 |
| **53.6** | adequate | [`156`](answers/pokemon/156-translating-code-and-markup.md) | translating-code-and-markup | 7 | 13 | 8 | 1.8 |
| **53.9** | adequate | [`023`](answers/pokemon/023-grpo-reasoning.md) | grpo-reasoning | 7 | 15 | 35 | 2.1 |
| **54.2** | adequate | [`121`](answers/pokemon/121-high-resolution-tiling.md) | high-resolution-tiling | 8 | 14 | 8 | 1.5 |
| **54.4** | adequate | [`040`](answers/pokemon/040-hallucination.md) | hallucination | 7 | 14 | 23 | 1.9 |
| **54.4** | adequate | [`131`](answers/pokemon/131-document-level-translation.md) | document-level-translation | 8 | 13 | 10 | 1.6 |
| **54.8** | adequate | [`063`](answers/pokemon/063-model-calibration.md) | model-calibration | 7 | 13 | 17 | 1.9 |
| **54.8** | adequate | [`149`](answers/pokemon/149-post-editing-human-in-the-loop.md) | post-editing-human-in-the-loop | 10 | 11 | 25 | 1.3 |
| **54.9** | adequate | [`132`](answers/pokemon/132-quality-estimation.md) | quality-estimation | 9 | 13 | 23 | 1.3 |
| **55.2** | adequate | [`073`](answers/pokemon/073-backpropagation.md) | backpropagation | 8 | 12 | 12 | 1.6 |
| **55.2** | adequate | [`075`](answers/pokemon/075-batch-norm-vs-layer-norm.md) | batch-norm-vs-layer-norm | 9 | 14 | 37 | 1.9 |
| **55.3** | adequate | [`070`](answers/pokemon/070-roc-auc-vs-pr-auc.md) | roc-auc-vs-pr-auc | 8 | 9 | 3 | 1.7 |
| **55.5** | adequate | [`079`](answers/pokemon/079-parallelism-strategies.md) | parallelism-strategies | 8 | 15 | 58 | 2.6 |
| **55.6** | adequate | [`053`](answers/pokemon/053-react-agents.md) | react-agents | 10 | 13 | 39 | 1.7 |
| **56.5** | adequate | [`044`](answers/pokemon/044-vector-databases-ann.md) | vector-databases-ann | 8 | 14 | 12 | 1.8 |
| **56.7** | adequate | [`139`](answers/pokemon/139-multimodal-safety-attacks.md) | multimodal-safety-attacks | 8 | 16 | 10 | 1.8 |
| **57.1** | adequate | [`056`](answers/pokemon/056-multi-agent-systems.md) | multi-agent-systems | 10 | 13 | 36 | 1.8 |
| **57.4** | adequate | [`018`](answers/pokemon/018-pretraining-sft-rlhf.md) | pretraining-sft-rlhf | 10 | 13 | 40 | 2.0 |
| **57.4** | adequate | [`019`](answers/pokemon/019-rlhf-end-to-end.md) | rlhf-end-to-end | 10 | 13 | 33 | 1.8 |
| **57.4** | adequate | [`082`](answers/pokemon/082-activation-functions.md) | activation-functions | 8 | 12 | 10 | 1.9 |
| **57.5** | adequate | [`087`](answers/pokemon/087-curse-of-dimensionality.md) | curse-of-dimensionality | 10 | 12 | 32 | 1.8 |
| **58.5** | adequate | [`042`](answers/pokemon/042-chunking-strategies.md) | chunking-strategies | 8 | 13 | 7 | 2.0 |
| **58.5** | adequate | [`080`](answers/pokemon/080-zero-and-fsdp.md) | zero-and-fsdp | 7 | 19 | 55 | 2.9 |
| **58.8** | adequate | [`099`](answers/pokemon/099-ml-system-design.md) | ml-system-design | 11 | 14 | 47 | 1.9 |
| **59.0** | adequate | [`152`](answers/pokemon/152-3d-and-depth-understanding.md) | 3d-and-depth-understanding | 7 | 21 | 3 | 2.4 |
| **59.5** | adequate | [`035`](answers/pokemon/035-beam-search.md) | beam-search | 8 | 15 | 32 | 2.3 |
| **59.9** | adequate | [`041`](answers/pokemon/041-rag-vs-finetuning.md) | rag-vs-finetuning | 10 | 13 | 26 | 1.7 |
| **59.9** | adequate | [`124`](answers/pokemon/124-interleaved-multimodal-data.md) | interleaved-multimodal-data | 11 | 11 | 16 | 1.3 |
| **60.3** | adequate | [`014`](answers/pokemon/014-scaling-laws.md) | scaling-laws | 11 | 15 | 55 | 2.2 |
| **60.5** | adequate | [`021`](answers/pokemon/021-reward-models.md) | reward-models | 9 | 13 | 24 | 2.0 |
| **60.9** | adequate | [`151`](answers/pokemon/151-medical-scientific-imaging.md) | medical-scientific-imaging | 11 | 12 | 20 | 1.4 |
| **61.7** | adequate | [`030`](answers/pokemon/030-quantization.md) | quantization | 9 | 14 | 22 | 2.1 |
| **61.8** | adequate | [`010`](answers/pokemon/010-flash-attention.md) | flash-attention | 10 | 11 | 19 | 1.8 |
| **62.0** | adequate | [`031`](answers/pokemon/031-knowledge-distillation.md) | knowledge-distillation | 5 | 22 | 38 | 3.3 |
| **62.0** | adequate | [`118`](answers/pokemon/118-image-patches-tokenisation.md) | image-patches-tokenisation | 8 | 20 | 1 | 2.4 |
| **62.4** | adequate | [`134`](answers/pokemon/134-domain-adaptation-translation.md) | domain-adaptation-translation | 11 | 14 | 27 | 1.6 |
| **62.6** | adequate | [`107`](answers/pokemon/107-code-switching.md) | code-switching | 8 | 20 | 45 | 2.8 |
| **62.7** | adequate | [`055`](answers/pokemon/055-model-context-protocol.md) | model-context-protocol | 12 | 12 | 30 | 1.7 |
| **62.7** | adequate | [`120`](answers/pokemon/120-contrastive-image-text-pretraining.md) | contrastive-image-text-pretraining | 11 | 14 | 12 | 1.6 |
| **62.8** | adequate | [`122`](answers/pokemon/122-multimodal-hallucination.md) | multimodal-hallucination | 9 | 19 | 5 | 2.2 |
| **63.2** | adequate | [`154`](answers/pokemon/154-dubbing-and-lip-sync.md) | dubbing-and-lip-sync | 10 | 14 | 3 | 2.0 |
| **64.1** | adequate | [`144`](answers/pokemon/144-length-constrained-translation.md) | length-constrained-translation | 9 | 19 | 16 | 2.4 |
| **64.3** | adequate | [`008`](answers/pokemon/008-kv-cache.md) | kv-cache | 11 | 15 | 50 | 2.6 |
| **64.6** | adequate | [`043`](answers/pokemon/043-embeddings.md) | embeddings | 11 | 13 | 13 | 1.8 |
| **64.8** | adequate | [`113`](answers/pokemon/113-morphology-rich-languages.md) | morphology-rich-languages | 7 | 19 | 3 | 3.0 |
| **65.4** | strong | [`067`](answers/pokemon/067-dropout.md) | dropout | 10 | 15 | 34 | 2.5 |
| **65.4** | strong | [`126`](answers/pokemon/126-video-understanding.md) | video-understanding | 12 | 15 | 32 | 1.8 |
| **65.6** | strong | [`117`](answers/pokemon/117-vision-language-architectures.md) | vision-language-architectures | 10 | 20 | 11 | 2.2 |
| **65.6** | strong | [`137`](answers/pokemon/137-diffusion-image-generation.md) | diffusion-image-generation | 8 | 23 | 12 | 2.8 |
| **65.8** | strong | [`013`](answers/pokemon/013-context-length-limits.md) | context-length-limits | 13 | 16 | 55 | 2.2 |
| **66.7** | strong | [`128`](answers/pokemon/128-visual-grounding-spatial-reasoning.md) | visual-grounding-spatial-reasoning | 10 | 21 | 18 | 2.4 |
| **67.4** | strong | [`143`](answers/pokemon/143-simultaneous-speech-translation.md) | simultaneous-speech-translation | 9 | 22 | 26 | 2.7 |
| **67.6** | strong | [`086`](answers/pokemon/086-pca.md) | pca | 13 | 15 | 43 | 2.2 |
| **67.7** | strong | [`100`](answers/pokemon/100-fairness-bias-privacy.md) | fairness-bias-privacy | 9 | 22 | 21 | 2.8 |
| **69.9** | strong | [`034`](answers/pokemon/034-sampling-temperature-top-p.md) | sampling-temperature-top-p | 9 | 21 | 28 | 3.0 |
| **69.9** | strong | [`155`](answers/pokemon/155-sign-language-translation.md) | sign-language-translation | 13 | 15 | 7 | 1.8 |
| **70.2** | strong | [`054`](answers/pokemon/054-tool-calling.md) | tool-calling | 9 | 22 | 29 | 3.1 |
| **70.5** | strong | [`146`](answers/pokemon/146-synthetic-captions-data-curation.md) | synthetic-captions-data-curation | 13 | 15 | 11 | 1.9 |
| **70.6** | strong | [`066`](answers/pokemon/066-l1-vs-l2-regularization.md) | l1-vs-l2-regularization | 6 | 27 | 20 | 4.5 |
| **70.7** | strong | [`136`](answers/pokemon/136-off-target-and-hallucinated-translation.md) | off-target-and-hallucinated-translation | 10 | 24 | 6 | 2.8 |
| **71.3** | strong | [`145`](answers/pokemon/145-gui-computer-use-agents.md) | gui-computer-use-agents | 14 | 15 | 9 | 1.7 |
| **72.9** | strong | [`140`](answers/pokemon/140-multimodal-retrieval.md) | multimodal-retrieval | 14 | 17 | 11 | 1.9 |
| **73.7** | strong | [`016`](answers/pokemon/016-next-token-prediction.md) | next-token-prediction | 14 | 17 | 43 | 2.4 |
| **74.2** | strong | [`001`](answers/pokemon/001-attention-mechanisms.md) | attention-mechanisms | 9 | 29 | 57 | 3.6 |
| **74.4** | strong | [`112`](answers/pokemon/112-byte-level-and-tokenizer-free.md) | byte-level-and-tokenizer-free | 13 | 15 | 15 | 2.4 |
| **75.8** | strong | [`078`](answers/pokemon/078-gradient-checkpointing.md) | gradient-checkpointing | 8 | 28 | 17 | 4.9 |
| **75.9** | strong | [`037`](answers/pokemon/037-evaluating-llms.md) | evaluating-llms | 14 | 16 | 34 | 2.4 |
| **76.4** | strong | [`051`](answers/pokemon/051-in-context-learning.md) | in-context-learning | 10 | 22 | 20 | 3.5 |
| **77.5** | strong | [`102`](answers/pokemon/102-tokenizer-fairness-token-premium.md) | tokenizer-fairness-token-premium | 12 | 22 | 32 | 3.0 |
| **78.4** | strong | [`085`](answers/pokemon/085-label-smoothing.md) | label-smoothing | 9 | 28 | 15 | 5.1 |
| **80.4** | excellent | [`148`](answers/pokemon/148-modality-balance-training-recipes.md) | modality-balance-training-recipes | 16 | 18 | 29 | 2.1 |
| **82.1** | excellent | [`109`](answers/pokemon/109-transliteration-romanisation.md) | transliteration-romanisation | 14 | 23 | 8 | 2.9 |
| **82.6** | excellent | [`130`](answers/pokemon/130-low-resource-translation.md) | low-resource-translation | 15 | 26 | 22 | 2.7 |
| **82.7** | excellent | [`116`](answers/pokemon/116-multilingual-instruction-tuning.md) | multilingual-instruction-tuning | 11 | 26 | 29 | 3.9 |
| **84.6** | excellent | [`150`](answers/pokemon/150-localisation-beyond-text.md) | localisation-beyond-text | 18 | 20 | 14 | 2.2 |
| **85.7** | excellent | [`127`](answers/pokemon/127-chart-and-diagram-reasoning.md) | chart-and-diagram-reasoning | 19 | 22 | 26 | 2.4 |
| **87.3** | excellent | [`115`](answers/pokemon/115-unicode-normalisation.md) | unicode-normalisation | 15 | 23 | 17 | 3.2 |
| **87.6** | excellent | [`114`](answers/pokemon/114-word-segmentation-no-spaces.md) | word-segmentation-no-spaces | 15 | 21 | 20 | 3.3 |
| **88.8** | excellent | [`006`](answers/pokemon/006-residual-connections.md) | residual-connections | 13 | 34 | 42 | 5.7 |
| **91.4** | excellent | [`110`](answers/pokemon/110-language-adapters.md) | language-adapters | 14 | 28 | 15 | 4.5 |
| **94.0** | excellent | [`106`](answers/pokemon/106-script-vs-language.md) | script-vs-language | 15 | 28 | 16 | 4.5 |
| **99.2** | excellent | [`104`](answers/pokemon/104-language-sampling-pretraining.md) | language-sampling-pretraining | 17 | 40 | 17 | 6.9 |
| **100.0** | excellent | [`101`](answers/pokemon/101-cross-lingual-transfer.md) | cross-lingual-transfer | 27 | 65 | 19 | 8.9 |
| **100.0** | excellent | [`103`](answers/pokemon/103-curse-of-multilinguality.md) | curse-of-multilinguality | 19 | 43 | 11 | 6.3 |
| **100.0** | excellent | [`105`](answers/pokemon/105-shared-multilingual-vocabulary.md) | shared-multilingual-vocabulary | 20 | 28 | 18 | 4.4 |
| **100.0** | excellent | [`108`](answers/pokemon/108-language-identification.md) | language-identification | 21 | 42 | 8 | 6.7 |
| **100.0** | excellent | [`111`](answers/pokemon/111-cross-lingual-embedding-alignment.md) | cross-lingual-embedding-alignment | 19 | 38 | 6 | 7.0 |

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

