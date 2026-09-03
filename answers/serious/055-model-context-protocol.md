---
id: "055"
slug: model-context-protocol
style: serious
category: agents
difficulty: intermediate
question: "What is the Model Context Protocol and what problem does it solve?"
tags: [mcp, protocol, integrations, tools, resources]
---

# Model Context Protocol

MCP is an open protocol standardising how applications supply **context and capabilities** to LLMs.
The problem it solves is combinatorial: `M` AI applications each needing `N` integrations means `M×N`
bespoke connectors, every one written twice and maintained separately.

```
   BEFORE                              AFTER
   ──────                              ─────
   app1 ─┬─ GitHub connector           app1 ─┐
         ├─ Slack connector            app2 ─┼─► MCP ─┬─ GitHub server
         └─ Postgres connector         app3 ─┘        ├─ Slack server
   app2 ─┬─ GitHub connector                          └─ Postgres server
         ├─ Slack connector
         └─ Postgres connector          M + N implementations
   app3 ─┬─ ... (again)

   M × N implementations
```

The analogy usually offered — "USB-C for AI applications" — is apt: one connector spec, many hosts,
many peripherals, no host needing to know about any specific peripheral in advance.

## The architecture

* **Host** — the application the user interacts with (an IDE, a chat client, an agent runtime).
* **Client** — lives inside the host; maintains one connection per server.
* **Server** — exposes capabilities for one system (a database, an API, a filesystem).

Transports are stdio (local subprocess) or HTTP with Server-Sent Events (remote). Messages are
JSON-RPC 2.0.

## The three primitives

The design distinction worth knowing, because it is what makes MCP more than a tool registry:

| Primitive | Controlled by | Analogy |
| --- | --- | --- |
| **Tools** | the **model** decides to call them | POST — actions with side effects |
| **Resources** | the **application** decides what to load | GET — data, identified by URI |
| **Prompts** | the **user** invokes them | slash commands / templates |

Tools are model-controlled: the model sees descriptions and chooses. Resources are
application-controlled: the host decides what context to attach, so a server can expose a whole
filesystem or database without the model having to "call" anything. Prompts are user-controlled
templates. Separating these three keeps the model from being handed every decision, which matters
for both cost and safety.

There is also **sampling** — a server can ask the *host* to run an LLM completion, so servers get
model access without holding API keys themselves.

## Why it matters

* **Integrations become portable.** Write a server once; every MCP-capable host can use it.
* **The ecosystem is decoupled from any vendor.** Servers exist for filesystems, git, databases,
  browsers, issue trackers, and hundreds of SaaS products, maintained by their owners rather than by
  each AI application.
* **Capability negotiation** means hosts and servers can evolve independently.

## The security model, honestly

This is where an interviewer will push, and the right answer is not to be defensive about it.

MCP servers are **code you are running with your credentials, feeding text into a model's context**.
Real concerns:

* **Prompt injection via tool descriptions or results** — a malicious server can put instructions in
  a description the model reads as trusted (question 059).
* **Tool shadowing** — a server defining a tool whose description subverts another server's tool.
* **Confused deputy / over-broad scope** — a server with more access than the task requires.
* **Supply chain** — installing a community server is installing arbitrary code.

Mitigations in practice: run servers with least privilege, human-in-the-loop confirmation for
destructive tools, pin and review server versions, prefer first-party servers for sensitive systems,
and treat every tool result as untrusted input.

## What an interviewer digs into next

* Why separate resources from tools?
* What is the sampling primitive for, and why does it matter for key management?
* How would you defend an MCP-based agent against a malicious server?
* When would you *not* use MCP and just write a direct integration?
