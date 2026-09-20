---
id: "232"
slug: reading-an-open-model-card
style: serious
category: open-weights
difficulty: intermediate
question: "You have downloaded an open model's weights. What do you read before you try to serve it?"
tags: [model-card, licensing, tokenizer, quantisation, vllm]
---

# Downloading the weights is step one of about seven.

The gap between "I have the weights" and "I can serve this" is five files and one compatibility
question, and every one of them has ruined somebody's week. Read them in this order, because each
one decides whether the next one matters.

```
   repo/
   ├── config.json                  ← read first. decides everything below it.
   ├── model.safetensors.index.json ← how many bytes, in how many shards
   ├── model-00001-of-000NN.safetensors
   ├── tokenizer.json               ← must agree with config.vocab_size
   ├── tokenizer_config.json        ← chat_template, eos_token, stop strings
   ├── generation_config.json       ← the defaults the lab actually used
   ├── LICENSE        ─┐
   ├── LICENSE-MODEL   ├── three different files, three different scopes
   └── USE_POLICY.md  ─┘
```

## 1. config.json, and the one field that outranks the rest

`architectures` is the field that decides whether any of this works. It is a Python class name,
and if your engine's version does not know it, no amount of correct configuration helps. Check it
against your *installed* vLLM or SGLang version, not the current docs.

Then the shape, which gives you the arithmetic from
[228](228-attention-variants-and-kv-arithmetic.md) and [207](207-sparse-moe-serving.md):

```
   num_hidden_layers · hidden_size · num_attention_heads · num_key_value_heads · head_dim
        → KV bytes per token = 2 · n_kv · head_dim · bytes, × layers

   n_routed_experts · num_experts_per_tok · moe_intermediate_size · n_shared_experts
        → total parameters (memory) vs active parameters (FLOPs)

   torch_dtype, quantization_config     → bytes per parameter
   max_position_embeddings, rope_scaling→ the REAL context window
   vocab_size                           → must equal the tokenizer's, exactly
```

Two traps live here. **`max_position_embeddings` is often not the advertised context**: the
headline number frequently requires a YaRN or rope-scaling override that the card documents in
prose and the config leaves off by default. And **`num_key_value_heads` constrains your tensor
parallelism** — 8 KV heads does not divide cleanly across 16-way TP without replication, which is
the kind of thing you find out at 2am.

## 2. Count the bytes before you count on anything

`model.safetensors.index.json` lists every shard. Sum them. That number, not the parameter count,
is your weight footprint, and it already reflects whatever dtype the repo shipped. Compare it to
aggregate HBM minus KV minus activations. Safetensors is the format you want; a repo that still
ships `pytorch_model.bin` is asking you to unpickle arbitrary code.

## 3. The licence, which is three questions not one

*Can I use it commercially, are there conditions that travel, and can the terms change?*

| Licence | Cap | What travels | Can it change |
| --- | --- | --- | --- |
| Apache 2.0 / MIT | none | attribution; Apache adds a patent grant | no |
| Llama 4 Community | 700M MAU (Apr 2025) | naming, pass-through, output limits | AUP amendable |
| Qwen (Tongyi Qianwen) | 100M MAU on the larger models | acceptable use | vendor-set |
| Vendor "community" terms | varies | varies — read it, it is short | varies |

As of September 2026 the permissive end is crowded: DeepSeek, Mistral Large 3 (reported 675B
total / 41B active, Apache 2.0), GLM-5.3 and GLM-5.3-Flash (MIT), and Meta's Muse Glimmer (30B,
Apache 2.0, August 2026) all sit there. Llama 4 remains under the Llama 4 Community License with
the MAU threshold and the derivative-naming rule; many small Qwen models are Apache 2.0 while the
flagships are not. **The question to take to legal is not "is it open" — it is whether an
acceptable-use policy travels with the file and whether the vendor may amend it unilaterally.**

## 4. The tokenizer and the chat template

This is where silent failures live.

* **`vocab_size` must match.** A mismatch does not crash; it produces fluent nonsense at the tail
  of the distribution.
* **The chat template is a Jinja string in `tokenizer_config.json`.** Applying your own formatting
  instead loses several points on every benchmark and nobody will tell you.
* **`eos_token` is not always the stop token.** The canonical bug: the model was trained to end
  turns with `<|im_end|>` while `eos_token` is `<|endoftext|>`, so generation runs to
  `max_tokens` every time. Check `generation_config.json` and the template's stop strings
  together.
* **Reasoning models add delimiters** for the thinking segment, and your parser has to know them
  or your users see the scratchpad.
* Tokenizers also set your **cost per word** — see [206](206-million-token-context.md). Two models
  with the same context number do not hold the same amount of English.

## 5. What the community actually ships, and when

```
   day 0        the lab's own BF16/FP8 safetensors + a vLLM/SGLang PR
   day 0–3      AWQ and FP8 quants for GPU serving  ← the 2026 datacentre default
   day 3–21     GGUF for llama.cpp / Ollama / LM Studio (Q4_K_M is the default pick)
   later        GPTQ, if anyone bothers; it is fading
   newest       MXFP4 (OCP microscaling) and NVFP4 (Blackwell), now reaching GGUF too
```

The ordering is not arbitrary. vLLM and SGLang take a Python modelling file, which a lab can
contribute on release day. llama.cpp needs a hand-written graph in C++ plus a conversion script,
so a genuinely new architecture — a novel attention variant, a new MoE routing scheme — lands
there weeks later or not at all. **"Is there a GGUF yet" is a proxy for "has anyone outside the
lab implemented this architecture".**

## 6. The compatibility question, asked properly

Do not ask "does vLLM support this model". Ask, of your pinned version: is the architecture class
present; is there a kernel for this quantisation on this GPU generation; is there a tool-calling
parser and a reasoning parser for this template; does prefix caching work with this attention
type ([231](231-linear-and-hybrid-attention.md)); and does `num_key_value_heads` divide your TP
degree. Five yeses is a deployment. Four is a weekend.

## Where this stands, September 2026

The formats move: AWQ is the current GPU default, GPTQ is fading, and FP4 in its two flavours is
arriving. The licences move less but they do move, and the Llama family's amendable
acceptable-use policy is the reason to re-read rather than remember. Hugging Face was unreachable
from this environment, so the licence and format details above are from coverage rather than from
the model cards themselves — read the actual `LICENSE-MODEL` in the repo you are deploying, every
time. The reading order is the durable part: architecture, bytes, licence, tokenizer, format,
engine. It has not changed in three years and it will not change next year.

## What an interviewer digs into next

* Why might `max_position_embeddings` disagree with the advertised context window?
* A model never stops generating. What do you look at first?
* Why does GGUF lag vLLM for a brand-new architecture?
