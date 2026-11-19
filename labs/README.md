# Labs

Six runnable labs. Each has an **unprotected baseline**, a **guarded** version, **tests** and the **expected outcome**. You need Python 3.9 or newer and nothing else, and every lab runs offline.

| Lab | What you learn | Time |
|---|---|---|
| [01 · Prompt injection](01-prompt-injection) | Detect malicious instructions in user and retrieved content, and measure the detector | 10 min |
| [02 · MCP tool poisoning](02-mcp-tool-poisoning) | Scan, pin and validate MCP tools; clean tool results | 15 min |
| [03 · Privacy protection](03-privacy-protection) | Mask PII and secrets locally on CPU, restore on your side | 10 min |
| [04 · Fully guarded agent](04-fully-guarded-agent) | Input, tool-call, tool-result and output guards with human review | 20 min |
| [05 · Agent red teaming](05-agent-red-teaming) | Multi-turn attacks, attack-success rate, findings report | 15 min |
| [06 · MCP guard server](06-mcp-guard-server) | A guardrail over MCP: per-checkpoint tools, risk-scored actions, human approval | 15 min |

```bash
python3 run_tests.py          # all labs, about 35 tests, under a second
```

## Choosing a guard

Every lab takes `--guard` (or the `GUARD` environment variable):

| `--guard` | What it is | Needs |
|---|---|---|
| `none` | No protection: the baseline | nothing |
| `local` (default) | Transparent regex rules in [`guards/guard.py`](../guards/guard.py). Learn with them, don't ship them alone | nothing |
| `proofagent` | [ProofAgent](https://proofagent.ai) model-based guard over HTTP (Lab 06: over MCP) | `PROOFAGENT_NANO_API_KEY` (free key: [how to get one](06-mcp-guard-server#1-get-a-free-api-key)) |

To add another backend (NeMo Guardrails, Guardrails AI, LLM Guard, Llama Prompt Guard, Lakera, a cloud provider), write one class with a `check(text, checkpoint)` method and open a PR. Side-by-side comparisons on the same labs are the most useful contribution this repo can get.
