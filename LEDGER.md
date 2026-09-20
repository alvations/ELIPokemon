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

**232 answers · mean 64.4 · median 60.5 · min 39.9 (199) · max 100.0 (218)**

| band | range | answers |
| --- | --- | --- |
| excellent | 80-100 | 42 |
| strong | 65-79 | 55 |
| adequate | 50-64 | 86 |
| thin | 35-49 | 49 |
| generic | 0-34 | 0 |

## Every answer, lowest first

| score | band | id | answer | distinct | named | generic | per 100w |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| **39.9** | thin | [`199`](answers/pokemon/199-choosing-an-approach.md) | choosing-an-approach | 5 | 6 | 12 | 0.9 |
| **41.8** | thin | [`005`](answers/pokemon/005-layer-normalization.md) | layer-normalization | 9 | 9 | 64 | 1.3 |
| **42.1** | thin | [`022`](answers/pokemon/022-ppo-for-llms.md) | ppo-for-llms | 6 | 13 | 48 | 1.6 |
| **42.3** | thin | [`024`](answers/pokemon/024-constitutional-ai-rlaif.md) | constitutional-ai-rlaif | 8 | 9 | 37 | 1.2 |
| **42.8** | thin | [`058`](answers/pokemon/058-reasoning-models.md) | reasoning-models | 6 | 12 | 38 | 1.5 |
| **43.1** | thin | [`003`](answers/pokemon/003-multi-head-attention.md) | multi-head-attention | 6 | 11 | 42 | 1.8 |
| **43.2** | thin | [`050`](answers/pokemon/050-self-consistency.md) | self-consistency | 5 | 8 | 14 | 1.2 |
| **43.4** | thin | [`038`](answers/pokemon/038-llm-as-a-judge.md) | llm-as-a-judge | 7 | 11 | 47 | 1.6 |
| **43.4** | thin | [`083`](answers/pokemon/083-softmax-and-logsumexp.md) | softmax-and-logsumexp | 4 | 9 | 13 | 1.5 |
| **43.4** | thin | [`138`](answers/pokemon/138-speech-language-models.md) | speech-language-models | 5 | 10 | 11 | 1.2 |
| **44.1** | thin | [`071`](answers/pokemon/071-class-imbalance.md) | class-imbalance | 4 | 10 | 4 | 1.6 |
| **44.8** | thin | [`025`](answers/pokemon/025-instruction-tuning.md) | instruction-tuning | 7 | 12 | 44 | 1.6 |
| **44.9** | thin | [`009`](answers/pokemon/009-mqa-and-gqa.md) | mqa-and-gqa | 6 | 10 | 31 | 1.8 |
| **45.0** | thin | [`027`](answers/pokemon/027-lora.md) | lora | 5 | 13 | 35 | 1.9 |
| **45.0** | thin | [`184`](answers/pokemon/184-face-recognition-and-biometrics.md) | face-recognition-and-biometrics | 6 | 7 | 13 | 1.1 |
| **45.2** | thin | [`187`](answers/pokemon/187-mt-in-regulated-domains.md) | mt-in-regulated-domains | 7 | 8 | 18 | 1.1 |
| **45.4** | thin | [`094`](answers/pokemon/094-multimodal-models.md) | multimodal-models | 7 | 11 | 30 | 1.4 |
| **45.5** | thin | [`084`](answers/pokemon/084-cross-entropy-loss.md) | cross-entropy-loss | 4 | 11 | 16 | 1.7 |
| **45.5** | thin | [`096`](answers/pokemon/096-ab-testing-ml.md) | ab-testing-ml | 8 | 11 | 42 | 1.5 |
| **45.6** | thin | [`015`](answers/pokemon/015-emergent-abilities.md) | emergent-abilities | 4 | 11 | 27 | 2.1 |
| **45.6** | thin | [`077`](answers/pokemon/077-mixed-precision-training.md) | mixed-precision-training | 6 | 7 | 9 | 1.1 |
| **45.8** | thin | [`028`](answers/pokemon/028-qlora.md) | qlora | 6 | 11 | 29 | 1.6 |
| **45.8** | thin | [`095`](answers/pokemon/095-data-drift.md) | data-drift | 7 | 10 | 27 | 1.4 |
| **46.2** | thin | [`064`](answers/pokemon/064-bias-variance-tradeoff.md) | bias-variance-tradeoff | 6 | 11 | 30 | 1.8 |
| **46.3** | thin | [`182`](answers/pokemon/182-vlm-distillation.md) | vlm-distillation | 5 | 10 | 13 | 1.5 |
| **46.4** | thin | [`180`](answers/pokemon/180-mt-infrastructure-and-cost.md) | mt-infrastructure-and-cost | 5 | 10 | 5 | 1.5 |
| **46.6** | thin | [`049`](answers/pokemon/049-chain-of-thought.md) | chain-of-thought | 5 | 11 | 20 | 1.6 |
| **46.7** | thin | [`036`](answers/pokemon/036-perplexity.md) | perplexity | 7 | 11 | 37 | 1.8 |
| **47.0** | thin | [`059`](answers/pokemon/059-prompt-injection.md) | prompt-injection | 6 | 11 | 25 | 1.6 |
| **47.0** | thin | [`090`](answers/pokemon/090-transfer-learning.md) | transfer-learning | 8 | 11 | 38 | 1.5 |
| **47.1** | thin | [`169`](answers/pokemon/169-mt-security-and-poisoning.md) | mt-security-and-poisoning | 6 | 8 | 3 | 1.3 |
| **47.2** | thin | [`089`](answers/pokemon/089-bagging-vs-boosting.md) | bagging-vs-boosting | 8 | 9 | 24 | 1.2 |
| **47.2** | thin | [`163`](answers/pokemon/163-endangered-language-documentation.md) | endangered-language-documentation | 7 | 7 | 3 | 1.0 |
| **47.4** | thin | [`026`](answers/pokemon/026-catastrophic-forgetting.md) | catastrophic-forgetting | 8 | 9 | 29 | 1.5 |
| **47.4** | thin | [`153`](answers/pokemon/153-speech-to-speech-translation.md) | speech-to-speech-translation | 6 | 8 | 11 | 1.4 |
| **47.5** | thin | [`020`](answers/pokemon/020-dpo-vs-ppo.md) | dpo-vs-ppo | 5 | 15 | 38 | 2.1 |
| **47.6** | thin | [`076`](answers/pokemon/076-learning-rate-schedules.md) | learning-rate-schedules | 7 | 8 | 15 | 1.1 |
| **47.8** | thin | [`002`](answers/pokemon/002-positional-encodings-rope.md) | positional-encodings-rope | 8 | 10 | 30 | 1.4 |
| **47.8** | thin | [`194`](answers/pokemon/194-on-device-translation.md) | on-device-translation | 6 | 9 | 4 | 1.4 |
| **47.9** | thin | [`098`](answers/pokemon/098-training-serving-skew.md) | training-serving-skew | 7 | 10 | 25 | 1.5 |
| **48.1** | thin | [`048`](answers/pokemon/048-evaluating-rag.md) | evaluating-rag | 6 | 12 | 26 | 1.6 |
| **48.1** | thin | [`088`](answers/pokemon/088-trees-forests-boosting.md) | trees-forests-boosting | 9 | 10 | 32 | 1.3 |
| **48.3** | thin | [`065`](answers/pokemon/065-overfitting.md) | overfitting | 7 | 11 | 31 | 1.7 |
| **48.3** | thin | [`172`](answers/pokemon/172-named-entity-translation.md) | named-entity-translation | 7 | 8 | 11 | 1.1 |
| **48.5** | thin | [`069`](answers/pokemon/069-precision-recall-f1.md) | precision-recall-f1 | 6 | 9 | 11 | 1.5 |
| **48.7** | thin | [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md) | teacher-forcing-exposure-bias | 9 | 10 | 45 | 1.7 |
| **48.9** | thin | [`039`](answers/pokemon/039-benchmark-contamination.md) | benchmark-contamination | 7 | 13 | 40 | 1.9 |
| **49.3** | thin | [`074`](answers/pokemon/074-vanishing-exploding-gradients.md) | vanishing-exploding-gradients | 6 | 14 | 38 | 2.1 |
| **49.9** | thin | [`061`](answers/pokemon/061-guardrails-moderation.md) | guardrails-moderation | 8 | 11 | 29 | 1.5 |
| **50.0** | adequate | [`097`](answers/pokemon/097-serving-cost-latency.md) | serving-cost-latency | 10 | 11 | 48 | 1.5 |
| **50.2** | adequate | [`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md) | encoder-decoder-vs-decoder-only | 10 | 12 | 53 | 1.6 |
| **50.2** | adequate | [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md) | finetuning-vs-peft-vs-prompting | 8 | 11 | 31 | 1.6 |
| **50.2** | adequate | [`166`](answers/pokemon/166-watermarking-and-provenance.md) | watermarking-and-provenance | 5 | 14 | 23 | 2.0 |
| **50.6** | adequate | [`047`](answers/pokemon/047-query-rewriting-hyde.md) | query-rewriting-hyde | 8 | 9 | 19 | 1.3 |
| **50.6** | adequate | [`062`](answers/pokemon/062-red-teaming.md) | red-teaming | 10 | 10 | 34 | 1.3 |
| **50.8** | adequate | [`012`](answers/pokemon/012-tokenization-bpe.md) | tokenization-bpe | 7 | 10 | 16 | 1.4 |
| **51.0** | adequate | [`177`](answers/pokemon/177-multilingual-rag.md) | multilingual-rag | 6 | 12 | 8 | 1.8 |
| **51.3** | adequate | [`072`](answers/pokemon/072-gradient-descent-optimizers.md) | gradient-descent-optimizers | 8 | 14 | 38 | 1.7 |
| **51.3** | adequate | [`197`](answers/pokemon/197-multimodal-model-documentation.md) | multimodal-model-documentation | 7 | 10 | 10 | 1.5 |
| **51.3** | adequate | [`208`](answers/pokemon/208-open-weight-equivalence.md) | open-weight-equivalence | 9 | 12 | 40 | 1.7 |
| **51.7** | adequate | [`011`](answers/pokemon/011-mixture-of-experts.md) | mixture-of-experts | 7 | 13 | 31 | 1.9 |
| **51.9** | adequate | [`183`](answers/pokemon/183-multimodal-accessibility.md) | multimodal-accessibility | 8 | 8 | 9 | 1.3 |
| **52.0** | adequate | [`081`](answers/pokemon/081-batch-size-and-lr.md) | batch-size-and-lr | 8 | 13 | 35 | 1.8 |
| **52.1** | adequate | [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md) | cross-encoder-vs-bi-encoder | 7 | 10 | 17 | 1.6 |
| **52.2** | adequate | [`068`](answers/pokemon/068-cross-validation.md) | cross-validation | 7 | 11 | 23 | 1.8 |
| **52.3** | adequate | [`091`](answers/pokemon/091-self-supervised-learning.md) | self-supervised-learning | 8 | 12 | 31 | 1.8 |
| **52.3** | adequate | [`189`](answers/pokemon/189-multimodal-data-flywheel.md) | multimodal-data-flywheel | 6 | 12 | 9 | 1.9 |
| **52.5** | adequate | [`060`](answers/pokemon/060-jailbreaks.md) | jailbreaks | 9 | 13 | 34 | 1.5 |
| **52.7** | adequate | [`205`](answers/pokemon/205-model-tiering-and-routing.md) | model-tiering-and-routing | 7 | 18 | 56 | 2.4 |
| **53.1** | adequate | [`045`](answers/pokemon/045-hybrid-search-reranking.md) | hybrid-search-reranking | 7 | 12 | 19 | 1.7 |
| **53.6** | adequate | [`057`](answers/pokemon/057-test-time-compute.md) | test-time-compute | 10 | 12 | 41 | 1.7 |
| **53.6** | adequate | [`156`](answers/pokemon/156-translating-code-and-markup.md) | translating-code-and-markup | 7 | 13 | 8 | 1.8 |
| **53.9** | adequate | [`023`](answers/pokemon/023-grpo-reasoning.md) | grpo-reasoning | 7 | 15 | 35 | 2.1 |
| **54.1** | adequate | [`141`](answers/pokemon/141-formality-and-honorifics.md) | formality-and-honorifics | 7 | 13 | 14 | 1.8 |
| **54.2** | adequate | [`191`](answers/pokemon/191-3d-scene-generation.md) | 3d-scene-generation | 7 | 13 | 11 | 1.8 |
| **54.4** | adequate | [`093`](answers/pokemon/093-diffusion-models.md) | diffusion-models | 6 | 16 | 14 | 2.1 |
| **54.7** | adequate | [`147`](answers/pokemon/147-multimodal-benchmarks-contamination.md) | multimodal-benchmarks-contamination | 8 | 11 | 18 | 1.6 |
| **54.8** | adequate | [`063`](answers/pokemon/063-model-calibration.md) | model-calibration | 7 | 13 | 17 | 1.9 |
| **54.8** | adequate | [`149`](answers/pokemon/149-post-editing-human-in-the-loop.md) | post-editing-human-in-the-loop | 10 | 11 | 25 | 1.3 |
| **54.8** | adequate | [`195`](answers/pokemon/195-multilingual-reasoning.md) | multilingual-reasoning | 5 | 15 | 4 | 2.5 |
| **55.2** | adequate | [`073`](answers/pokemon/073-backpropagation.md) | backpropagation | 8 | 12 | 12 | 1.6 |
| **55.2** | adequate | [`075`](answers/pokemon/075-batch-norm-vs-layer-norm.md) | batch-norm-vs-layer-norm | 9 | 14 | 37 | 1.9 |
| **55.2** | adequate | [`142`](answers/pokemon/142-gender-bias-in-translation.md) | gender-bias-in-translation | 5 | 20 | 13 | 2.5 |
| **55.3** | adequate | [`070`](answers/pokemon/070-roc-auc-vs-pr-auc.md) | roc-auc-vs-pr-auc | 8 | 9 | 3 | 1.7 |
| **55.5** | adequate | [`079`](answers/pokemon/079-parallelism-strategies.md) | parallelism-strategies | 8 | 15 | 58 | 2.6 |
| **55.6** | adequate | [`053`](answers/pokemon/053-react-agents.md) | react-agents | 10 | 13 | 39 | 1.7 |
| **55.8** | adequate | [`033`](answers/pokemon/033-speculative-decoding.md) | speculative-decoding | 9 | 15 | 50 | 2.2 |
| **55.9** | adequate | [`129`](answers/pokemon/129-mt-evaluation-beyond-bleu.md) | mt-evaluation-beyond-bleu | 9 | 12 | 22 | 1.4 |
| **55.9** | adequate | [`175`](answers/pokemon/175-remote-sensing-imagery.md) | remote-sensing-imagery | 9 | 10 | 7 | 1.4 |
| **56.3** | adequate | [`032`](answers/pokemon/032-pruning-and-sparsity.md) | pruning-and-sparsity | 8 | 14 | 9 | 1.8 |
| **56.3** | adequate | [`196`](answers/pokemon/196-cross-lingual-evaluation-design.md) | cross-lingual-evaluation-design | 6 | 14 | 10 | 2.4 |
| **56.5** | adequate | [`044`](answers/pokemon/044-vector-databases-ann.md) | vector-databases-ann | 8 | 14 | 12 | 1.8 |
| **56.7** | adequate | [`173`](answers/pokemon/173-audio-and-music-generation.md) | audio-and-music-generation | 9 | 12 | 7 | 1.5 |
| **56.9** | adequate | [`179`](answers/pokemon/179-controlled-language-authoring.md) | controlled-language-authoring | 6 | 14 | 9 | 2.4 |
| **57.0** | adequate | [`133`](answers/pokemon/133-terminology-glossary-enforcement.md) | terminology-glossary-enforcement | 7 | 16 | 3 | 2.1 |
| **57.0** | adequate | [`135`](answers/pokemon/135-llm-versus-nmt-translation.md) | llm-versus-nmt-translation | 7 | 17 | 3 | 2.1 |
| **57.1** | adequate | [`056`](answers/pokemon/056-multi-agent-systems.md) | multi-agent-systems | 10 | 13 | 36 | 1.8 |
| **57.4** | adequate | [`018`](answers/pokemon/018-pretraining-sft-rlhf.md) | pretraining-sft-rlhf | 10 | 13 | 40 | 2.0 |
| **57.4** | adequate | [`019`](answers/pokemon/019-rlhf-end-to-end.md) | rlhf-end-to-end | 10 | 13 | 33 | 1.8 |
| **57.4** | adequate | [`178`](answers/pokemon/178-translating-user-generated-content.md) | translating-user-generated-content | 9 | 11 | 8 | 1.6 |
| **57.5** | adequate | [`087`](answers/pokemon/087-curse-of-dimensionality.md) | curse-of-dimensionality | 10 | 12 | 32 | 1.8 |
| **58.1** | adequate | [`167`](answers/pokemon/167-multimodal-preference-tuning.md) | multimodal-preference-tuning | 7 | 15 | 4 | 2.3 |
| **58.4** | adequate | [`132`](answers/pokemon/132-quality-estimation.md) | quality-estimation | 10 | 14 | 23 | 1.4 |
| **58.5** | adequate | [`042`](answers/pokemon/042-chunking-strategies.md) | chunking-strategies | 8 | 13 | 7 | 2.0 |
| **58.5** | adequate | [`080`](answers/pokemon/080-zero-and-fsdp.md) | zero-and-fsdp | 7 | 19 | 55 | 2.9 |
| **58.6** | adequate | [`052`](answers/pokemon/052-context-engineering.md) | context-engineering | 9 | 12 | 23 | 1.8 |
| **58.6** | adequate | [`092`](answers/pokemon/092-contrastive-learning.md) | contrastive-learning | 5 | 20 | 20 | 2.9 |
| **58.6** | adequate | [`190`](answers/pokemon/190-image-quality-and-aesthetics.md) | image-quality-and-aesthetics | 9 | 11 | 5 | 1.7 |
| **58.6** | adequate | [`200`](answers/pokemon/200-what-actually-matters.md) | what-actually-matters | 10 | 11 | 6 | 1.4 |
| **58.8** | adequate | [`099`](answers/pokemon/099-ml-system-design.md) | ml-system-design | 11 | 14 | 47 | 1.9 |
| **58.9** | adequate | [`164`](answers/pokemon/164-participatory-mt.md) | participatory-mt | 8 | 14 | 17 | 2.1 |
| **59.2** | adequate | [`119`](answers/pokemon/119-cross-modal-attention.md) | cross-modal-attention | 8 | 19 | 20 | 2.1 |
| **59.5** | adequate | [`035`](answers/pokemon/035-beam-search.md) | beam-search | 8 | 15 | 32 | 2.3 |
| **60.3** | adequate | [`014`](answers/pokemon/014-scaling-laws.md) | scaling-laws | 11 | 15 | 55 | 2.2 |
| **60.3** | adequate | [`125`](answers/pokemon/125-speech-recognition.md) | speech-recognition | 9 | 17 | 8 | 1.9 |
| **60.3** | adequate | [`188`](answers/pokemon/188-cat-tools-and-translator-workflow.md) | cat-tools-and-translator-workflow | 9 | 14 | 18 | 1.9 |
| **60.5** | adequate | [`021`](answers/pokemon/021-reward-models.md) | reward-models | 9 | 13 | 24 | 2.0 |
| **60.5** | adequate | [`158`](answers/pokemon/158-image-editing-inpainting.md) | image-editing-inpainting | 5 | 19 | 5 | 3.1 |
| **60.9** | adequate | [`151`](answers/pokemon/151-medical-scientific-imaging.md) | medical-scientific-imaging | 11 | 12 | 20 | 1.4 |
| **61.6** | adequate | [`040`](answers/pokemon/040-hallucination.md) | hallucination | 8 | 18 | 23 | 2.4 |
| **61.6** | adequate | [`121`](answers/pokemon/121-high-resolution-tiling.md) | high-resolution-tiling | 9 | 19 | 8 | 2.1 |
| **61.8** | adequate | [`010`](answers/pokemon/010-flash-attention.md) | flash-attention | 10 | 11 | 19 | 1.8 |
| **61.8** | adequate | [`174`](answers/pokemon/174-egocentric-and-streaming-perception.md) | egocentric-and-streaming-perception | 7 | 20 | 4 | 2.7 |
| **62.0** | adequate | [`031`](answers/pokemon/031-knowledge-distillation.md) | knowledge-distillation | 5 | 22 | 38 | 3.3 |
| **62.0** | adequate | [`123`](answers/pokemon/123-document-understanding-ocr.md) | document-understanding-ocr | 10 | 16 | 8 | 1.8 |
| **62.9** | adequate | [`209`](answers/pokemon/209-distillation-from-a-frontier-parent.md) | distillation-from-a-frontier-parent | 10 | 14 | 33 | 2.3 |
| **63.2** | adequate | [`154`](answers/pokemon/154-dubbing-and-lip-sync.md) | dubbing-and-lip-sync | 10 | 14 | 3 | 2.0 |
| **63.3** | adequate | [`203`](answers/pokemon/203-constrained-output-and-hallucination.md) | constrained-output-and-hallucination | 10 | 16 | 39 | 2.4 |
| **63.5** | adequate | [`124`](answers/pokemon/124-interleaved-multimodal-data.md) | interleaved-multimodal-data | 12 | 12 | 16 | 1.4 |
| **64.0** | adequate | [`168`](answers/pokemon/168-multimodal-embeddings.md) | multimodal-embeddings | 9 | 16 | 3 | 2.4 |
| **64.2** | adequate | [`082`](answers/pokemon/082-activation-functions.md) | activation-functions | 9 | 15 | 10 | 2.4 |
| **64.4** | adequate | [`131`](answers/pokemon/131-document-level-translation.md) | document-level-translation | 9 | 20 | 10 | 2.4 |
| **64.4** | adequate | [`170`](answers/pokemon/170-translationese.md) | translationese | 10 | 14 | 15 | 2.1 |
| **64.4** | adequate | [`171`](answers/pokemon/171-human-evaluation-translation.md) | human-evaluation-translation | 11 | 14 | 21 | 1.8 |
| **64.6** | adequate | [`043`](answers/pokemon/043-embeddings.md) | embeddings | 11 | 13 | 13 | 1.8 |
| **65.1** | strong | [`176`](answers/pokemon/176-multimodal-agents-with-tools.md) | multimodal-agents-with-tools | 8 | 21 | 6 | 2.8 |
| **65.4** | strong | [`067`](answers/pokemon/067-dropout.md) | dropout | 10 | 15 | 34 | 2.5 |
| **65.6** | strong | [`137`](answers/pokemon/137-diffusion-image-generation.md) | diffusion-image-generation | 8 | 23 | 12 | 2.8 |
| **65.6** | strong | [`217`](answers/pokemon/217-grpo-and-mit-weights.md) | grpo-and-mit-weights | 12 | 21 | 52 | 2.0 |
| **65.8** | strong | [`013`](answers/pokemon/013-context-length-limits.md) | context-length-limits | 13 | 16 | 55 | 2.2 |
| **66.2** | strong | [`186`](answers/pokemon/186-terminology-mining.md) | terminology-mining | 10 | 17 | 3 | 2.3 |
| **66.5** | strong | [`134`](answers/pokemon/134-domain-adaptation-translation.md) | domain-adaptation-translation | 12 | 15 | 27 | 1.8 |
| **66.5** | strong | [`152`](answers/pokemon/152-3d-and-depth-understanding.md) | 3d-and-depth-understanding | 8 | 26 | 3 | 2.9 |
| **66.8** | strong | [`118`](answers/pokemon/118-image-patches-tokenisation.md) | image-patches-tokenisation | 9 | 22 | 1 | 2.7 |
| **67.3** | strong | [`139`](answers/pokemon/139-multimodal-safety-attacks.md) | multimodal-safety-attacks | 9 | 24 | 10 | 2.7 |
| **67.6** | strong | [`086`](answers/pokemon/086-pca.md) | pca | 13 | 15 | 43 | 2.2 |
| **67.7** | strong | [`100`](answers/pokemon/100-fairness-bias-privacy.md) | fairness-bias-privacy | 9 | 22 | 21 | 2.8 |
| **67.7** | strong | [`144`](answers/pokemon/144-length-constrained-translation.md) | length-constrained-translation | 10 | 20 | 16 | 2.5 |
| **67.7** | strong | [`165`](answers/pokemon/165-vlm-inference-efficiency.md) | vlm-inference-efficiency | 10 | 17 | 11 | 2.5 |
| **67.7** | strong | [`181`](answers/pokemon/181-vision-language-action.md) | vision-language-action | 10 | 17 | 26 | 2.5 |
| **68.0** | strong | [`161`](answers/pokemon/161-translation-memory-systems.md) | translation-memory-systems | 9 | 18 | 10 | 2.8 |
| **69.0** | strong | [`204`](answers/pokemon/204-effort-and-adaptive-thinking.md) | effort-and-adaptive-thinking | 13 | 19 | 62 | 2.5 |
| **69.6** | strong | [`030`](answers/pokemon/030-quantization.md) | quantization | 10 | 18 | 22 | 2.7 |
| **69.9** | strong | [`034`](answers/pokemon/034-sampling-temperature-top-p.md) | sampling-temperature-top-p | 9 | 21 | 28 | 3.0 |
| **69.9** | strong | [`155`](answers/pokemon/155-sign-language-translation.md) | sign-language-translation | 13 | 15 | 7 | 1.8 |
| **70.2** | strong | [`054`](answers/pokemon/054-tool-calling.md) | tool-calling | 9 | 22 | 29 | 3.1 |
| **70.6** | strong | [`066`](answers/pokemon/066-l1-vs-l2-regularization.md) | l1-vs-l2-regularization | 6 | 27 | 20 | 4.5 |
| **71.1** | strong | [`143`](answers/pokemon/143-simultaneous-speech-translation.md) | simultaneous-speech-translation | 10 | 23 | 26 | 2.9 |
| **71.2** | strong | [`008`](answers/pokemon/008-kv-cache.md) | kv-cache | 12 | 17 | 50 | 2.9 |
| **71.8** | strong | [`055`](answers/pokemon/055-model-context-protocol.md) | model-context-protocol | 13 | 15 | 30 | 2.2 |
| **71.9** | strong | [`160`](answers/pokemon/160-multimodal-chain-of-thought.md) | multimodal-chain-of-thought | 12 | 17 | 11 | 2.4 |
| **72.0** | strong | [`212`](answers/pokemon/212-reading-model-announcements.md) | reading-model-announcements | 13 | 16 | 29 | 2.1 |
| **72.2** | strong | [`221`](answers/pokemon/221-long-context-extension-yarn.md) | long-context-extension-yarn | 13 | 25 | 38 | 2.1 |
| **72.5** | strong | [`122`](answers/pokemon/122-multimodal-hallucination.md) | multimodal-hallucination | 10 | 26 | 5 | 3.0 |
| **72.5** | strong | [`185`](answers/pokemon/185-massively-multilingual-models.md) | massively-multilingual-models | 13 | 14 | 12 | 2.1 |
| **72.7** | strong | [`157`](answers/pokemon/157-video-generation.md) | video-generation | 10 | 22 | 23 | 3.1 |
| **73.7** | strong | [`016`](answers/pokemon/016-next-token-prediction.md) | next-token-prediction | 14 | 17 | 43 | 2.4 |
| **73.8** | strong | [`007`](answers/pokemon/007-transformer-feed-forward-block.md) | transformer-feed-forward-block | 8 | 22 | 16 | 3.8 |
| **73.9** | strong | [`120`](answers/pokemon/120-contrastive-image-text-pretraining.md) | contrastive-image-text-pretraining | 13 | 20 | 12 | 2.3 |
| **74.0** | strong | [`126`](answers/pokemon/126-video-understanding.md) | video-understanding | 13 | 19 | 32 | 2.3 |
| **74.1** | strong | [`193`](answers/pokemon/193-multilingual-safety.md) | multilingual-safety | 11 | 19 | 10 | 2.9 |
| **74.9** | strong | [`202`](answers/pokemon/202-calibrated-decision-training.md) | calibrated-decision-training | 12 | 17 | 25 | 2.7 |
| **75.0** | strong | [`107`](answers/pokemon/107-code-switching.md) | code-switching | 10 | 24 | 45 | 3.3 |
| **75.2** | strong | [`128`](answers/pokemon/128-visual-grounding-spatial-reasoning.md) | visual-grounding-spatial-reasoning | 11 | 27 | 18 | 3.0 |
| **75.3** | strong | [`136`](answers/pokemon/136-off-target-and-hallucinated-translation.md) | off-target-and-hallucinated-translation | 11 | 26 | 6 | 3.1 |
| **75.8** | strong | [`078`](answers/pokemon/078-gradient-checkpointing.md) | gradient-checkpointing | 8 | 28 | 17 | 4.9 |
| **75.8** | strong | [`113`](answers/pokemon/113-morphology-rich-languages.md) | morphology-rich-languages | 8 | 26 | 3 | 4.2 |
| **75.8** | strong | [`162`](answers/pokemon/162-dialects-and-varieties.md) | dialects-and-varieties | 8 | 31 | 13 | 4.4 |
| **75.9** | strong | [`037`](answers/pokemon/037-evaluating-llms.md) | evaluating-llms | 14 | 16 | 34 | 2.4 |
| **76.1** | strong | [`198`](answers/pokemon/198-building-an-evaluation-suite.md) | building-an-evaluation-suite | 14 | 15 | 14 | 2.2 |
| **76.2** | strong | [`214`](answers/pokemon/214-fine-grained-and-shared-experts.md) | fine-grained-and-shared-experts | 15 | 19 | 25 | 2.0 |
| **76.4** | strong | [`051`](answers/pokemon/051-in-context-learning.md) | in-context-learning | 10 | 22 | 20 | 3.5 |
| **76.5** | strong | [`146`](answers/pokemon/146-synthetic-captions-data-curation.md) | synthetic-captions-data-curation | 14 | 18 | 11 | 2.3 |
| **77.0** | strong | [`201`](answers/pokemon/201-system-one-models.md) | system-one-models | 13 | 21 | 47 | 2.9 |
| **77.2** | strong | [`041`](answers/pokemon/041-rag-vs-finetuning.md) | rag-vs-finetuning | 11 | 25 | 26 | 3.3 |
| **77.3** | strong | [`192`](answers/pokemon/192-multimodal-monitoring.md) | multimodal-monitoring | 14 | 17 | 7 | 2.4 |
| **78.4** | strong | [`085`](answers/pokemon/085-label-smoothing.md) | label-smoothing | 9 | 28 | 15 | 5.1 |
| **78.4** | strong | [`112`](answers/pokemon/112-byte-level-and-tokenizer-free.md) | byte-level-and-tokenizer-free | 14 | 16 | 15 | 2.5 |
| **79.7** | strong | [`001`](answers/pokemon/001-attention-mechanisms.md) | attention-mechanisms | 10 | 31 | 57 | 3.9 |
| **79.9** | strong | [`228`](answers/pokemon/228-attention-variants-and-kv-arithmetic.md) | attention-variants-and-kv-arithmetic | 16 | 23 | 48 | 2.3 |
| **80.1** | excellent | [`140`](answers/pokemon/140-multimodal-retrieval.md) | multimodal-retrieval | 16 | 19 | 11 | 2.1 |
| **80.4** | excellent | [`148`](answers/pokemon/148-modality-balance-training-recipes.md) | modality-balance-training-recipes | 16 | 18 | 29 | 2.1 |
| **80.6** | excellent | [`216`](answers/pokemon/216-fp8-training-and-cost-figures.md) | fp8-training-and-cost-figures | 16 | 22 | 39 | 2.2 |
| **80.7** | excellent | [`219`](answers/pokemon/219-hosted-tiers-versus-open-checkpoints.md) | hosted-tiers-versus-open-checkpoints | 16 | 21 | 34 | 2.2 |
| **80.8** | excellent | [`220`](answers/pokemon/220-thinking-budget-and-effort-control.md) | thinking-budget-and-effort-control | 12 | 37 | 43 | 3.4 |
| **80.9** | excellent | [`145`](answers/pokemon/145-gui-computer-use-agents.md) | gui-computer-use-agents | 15 | 22 | 9 | 2.5 |
| **82.6** | excellent | [`117`](answers/pokemon/117-vision-language-architectures.md) | vision-language-architectures | 12 | 32 | 11 | 3.6 |
| **84.8** | excellent | [`231`](answers/pokemon/231-linear-and-hybrid-attention.md) | linear-and-hybrid-attention | 30 | 31 | 45 | 2.3 |
| **85.1** | excellent | [`102`](answers/pokemon/102-tokenizer-fairness-token-premium.md) | tokenizer-fairness-token-premium | 14 | 24 | 32 | 3.3 |
| **86.1** | excellent | [`130`](answers/pokemon/130-low-resource-translation.md) | low-resource-translation | 16 | 27 | 22 | 2.8 |
| **86.2** | excellent | [`116`](answers/pokemon/116-multilingual-instruction-tuning.md) | multilingual-instruction-tuning | 12 | 27 | 29 | 4.0 |
| **86.4** | excellent | [`226`](answers/pokemon/226-hosting-long-context-multimodal-weights.md) | hosting-long-context-multimodal-weights | 18 | 27 | 53 | 2.5 |
| **86.5** | excellent | [`150`](answers/pokemon/150-localisation-beyond-text.md) | localisation-beyond-text | 19 | 22 | 14 | 2.5 |
| **88.8** | excellent | [`006`](answers/pokemon/006-residual-connections.md) | residual-connections | 13 | 34 | 42 | 5.7 |
| **88.9** | excellent | [`229`](answers/pokemon/229-fine-grained-expert-routing.md) | fine-grained-expert-routing | 28 | 37 | 39 | 2.7 |
| **90.3** | excellent | [`127`](answers/pokemon/127-chart-and-diagram-reasoning.md) | chart-and-diagram-reasoning | 20 | 27 | 26 | 2.9 |
| **90.4** | excellent | [`211`](answers/pokemon/211-capability-thresholds-and-staged-release.md) | capability-thresholds-and-staged-release | 17 | 22 | 30 | 3.0 |
| **91.0** | excellent | [`230`](answers/pokemon/230-multi-token-prediction-and-drafting.md) | multi-token-prediction-and-drafting | 29 | 42 | 87 | 3.1 |
| **91.4** | excellent | [`110`](answers/pokemon/110-language-adapters.md) | language-adapters | 14 | 28 | 15 | 4.5 |
| **91.8** | excellent | [`232`](answers/pokemon/232-reading-an-open-model-card.md) | reading-an-open-model-card | 30 | 43 | 65 | 3.1 |
| **92.3** | excellent | [`207`](answers/pokemon/207-sparse-moe-serving.md) | sparse-moe-serving | 18 | 23 | 32 | 3.1 |
| **92.5** | excellent | [`109`](answers/pokemon/109-transliteration-romanisation.md) | transliteration-romanisation | 15 | 30 | 8 | 3.8 |
| **94.0** | excellent | [`159`](answers/pokemon/159-referring-segmentation.md) | referring-segmentation | 15 | 29 | 4 | 4.1 |
| **94.4** | excellent | [`225`](answers/pokemon/225-agentic-post-training-and-evaluation.md) | agentic-post-training-and-evaluation | 30 | 41 | 68 | 3.4 |
| **94.5** | excellent | [`224`](answers/pokemon/224-muon-optimizer-and-training-stability.md) | muon-optimizer-and-training-stability | 24 | 36 | 68 | 3.4 |
| **94.5** | excellent | [`227`](answers/pokemon/227-open-weight-licence-conditions.md) | open-weight-licence-conditions | 23 | 33 | 50 | 3.4 |
| **96.2** | excellent | [`115`](answers/pokemon/115-unicode-normalisation.md) | unicode-normalisation | 17 | 26 | 17 | 3.7 |
| **96.6** | excellent | [`106`](answers/pokemon/106-script-vs-language.md) | script-vs-language | 16 | 31 | 16 | 5.0 |
| **96.6** | excellent | [`213`](answers/pokemon/213-multi-head-latent-attention.md) | multi-head-latent-attention | 16 | 43 | 49 | 4.2 |
| **96.7** | excellent | [`215`](answers/pokemon/215-multi-token-prediction-and-speculation.md) | multi-token-prediction-and-speculation | 24 | 37 | 68 | 3.6 |
| **97.0** | excellent | [`206`](answers/pokemon/206-million-token-context.md) | million-token-context | 23 | 26 | 18 | 3.7 |
| **97.3** | excellent | [`223`](answers/pokemon/223-trillion-parameter-moe-sparsity.md) | trillion-parameter-moe-sparsity | 22 | 33 | 54 | 3.7 |
| **97.4** | excellent | [`222`](answers/pokemon/222-open-weight-licence-patchwork.md) | open-weight-licence-patchwork | 32 | 45 | 43 | 3.7 |
| **98.2** | excellent | [`114`](answers/pokemon/114-word-segmentation-no-spaces.md) | word-segmentation-no-spaces | 17 | 25 | 20 | 3.9 |
| **99.2** | excellent | [`104`](answers/pokemon/104-language-sampling-pretraining.md) | language-sampling-pretraining | 17 | 40 | 17 | 6.9 |
| **100.0** | excellent | [`101`](answers/pokemon/101-cross-lingual-transfer.md) | cross-lingual-transfer | 28 | 71 | 19 | 9.8 |
| **100.0** | excellent | [`103`](answers/pokemon/103-curse-of-multilinguality.md) | curse-of-multilinguality | 20 | 44 | 11 | 6.4 |
| **100.0** | excellent | [`105`](answers/pokemon/105-shared-multilingual-vocabulary.md) | shared-multilingual-vocabulary | 20 | 28 | 18 | 4.4 |
| **100.0** | excellent | [`108`](answers/pokemon/108-language-identification.md) | language-identification | 23 | 52 | 8 | 8.2 |
| **100.0** | excellent | [`111`](answers/pokemon/111-cross-lingual-embedding-alignment.md) | cross-lingual-embedding-alignment | 19 | 38 | 6 | 7.0 |
| **100.0** | excellent | [`210`](answers/pokemon/210-model-name-collisions.md) | model-name-collisions | 23 | 34 | 31 | 5.5 |
| **100.0** | excellent | [`218`](answers/pokemon/218-dense-versus-moe-checkpoints.md) | dense-versus-moe-checkpoints | 21 | 53 | 38 | 5.1 |

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

