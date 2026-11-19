# Agent threat models

An LLM application becomes an **agent** when the model decides which actions to take. Every action turns a wrong answer into a wrong *deed*. This guide sets out where attacks enter and what to put at each boundary.

## Anatomy of an agent

```
          untrusted                      trusted?                    side effects
  ┌──────────────────────┐      ┌─────────────────────┐      ┌──────────────────────┐
  │ user message         │      │ system prompt        │      │ email, payments      │
  │ web pages, RAG docs  │ ───▶ │ model (planner)      │ ───▶ │ files, shell, DB     │
  │ emails, tickets      │      │ memory               │      │ MCP servers, APIs    │
  │ tool / MCP output    │ ◀─── │ tool definitions     │ ◀─── │ other agents         │
  └──────────────────────┘      └─────────────────────┘      └──────────────────────┘
```

The model **cannot reliably tell instructions from data**. Everything in its context window can steer it, so anything an attacker can write into that window is an attack surface.

## Attack surfaces

| Surface | Example | OWASP | ATLAS |
|---|---|---|---|
| User input | "Ignore previous instructions…", jailbreak role-play | LLM01 | AML.T0051.000, AML.T0054 |
| Retrieved content | Hidden HTML comment in a help page; white text in a PDF | LLM01 | AML.T0051.001 |
| Tool and MCP output | JSON field that says "Assistant: delete the files" | LLM01, ASI01 | AML.T0051.001 |
| Tool definitions | Poisoned MCP description, rug pull after approval | LLM03, ASI04 | AML.T0011.002 |
| Memory | An instruction stored in turn 3, triggered in turn 30 | ASI06 | AML.T0080.000 |
| Tool calls | Email to an outside address, `rm -rf`, a refund | LLM06, ASI02 | AML.T0053 |
| Output | PII in the reply; Markdown image that leaks data in its URL | LLM02, LLM05 | AML.T0057, AML.T0077 |
| Other agents | A compromised sub-agent passes injected instructions upstream | ASI07 | AML.T0061 |

Full mapping, with controls: [standards-and-frameworks.md](../resources/standards-and-frameworks.md#threat-mapping-table).

## The lethal trifecta

Data theft through an agent needs **all three** of these:

1. access to private data,
2. exposure to untrusted content,
3. a channel to send data out (email, HTTP, image URLs, links, PRs).

Removing any one leg stops the whole class of attack. That is often cheaper and more reliable than detection. Examples: a summariser that cannot make network calls, or an agent with web access that cannot see customer records.

## Four checkpoints

| # | Checkpoint | Deterministic controls | Model-based controls |
|---|---|---|---|
| 1 | Input | Length limits, allowed languages, rate limits | Injection and jailbreak classifiers, PII masking |
| 2a | Tool call | Tool allowlist, JSON-schema validation, destination allowlist, amount limits, **human approval** for irreversible actions | Intent check on arguments |
| 2b | Tool result | Pinned tool definitions, size limits, strip HTML comments and invisible characters | Indirect-injection detection, PII masking |
| 3 | Output | Canary tokens, URL and Markdown-image allowlist | PII and safety classifiers, policy and compliance checks |

[Lab 04](../labs/04-fully-guarded-agent) puts all four into code in about 100 lines.

## Design principles

- **Code decides to check, not the model.** Put guards in the orchestration layer (graph nodes, hooks, a gateway), never as a tool the model may choose to call.
- **Least privilege per task.** Give each tool and MCP server short-lived, scoped credentials. Don't share them, and don't let them sit in the context.
- **Treat irreversible actions differently.** Hold payments, deletions, external messages and permission changes for a human, bound to the exact arguments.
- **Fail closed.** If the guard times out, the action does not run.
- **Assume detection will be bypassed.** Adaptive attacks break most published defences ([The Attacker Moves Second](https://arxiv.org/abs/2510.09023)). Layer deterministic limits under every classifier.
- **Log decisions, not just prompts.** Record which checkpoint decided what, and why. See [agent-governance.md](agent-governance.md).

## Patterns with stronger guarantees

From [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) and [CaMeL](https://arxiv.org/abs/2503.18813):

| Pattern | Idea |
|---|---|
| Action-selector | The model picks from fixed actions and never sees tool output |
| Plan-then-execute | The plan is fixed before untrusted data is read |
| Dual LLM | A quarantined model reads untrusted data and returns only symbols; the privileged model never sees the raw text |
| Code-then-execute (CaMeL) | The model writes a program; data flow is tracked with capabilities |
| Context minimisation | Remove the user's original prompt before later steps |
