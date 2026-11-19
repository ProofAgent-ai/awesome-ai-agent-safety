# Lab 04 · A fully guarded agent

**You will learn:** the reference architecture that guards all four places where untrusted text or actions cross a boundary, with allow, mask, block and human-review decisions, and why each layer catches what the others miss.

<p align="center"><img src="../../docs/assets/fully-guarded-agent.svg" alt="Fully guarded agent: user request, input guardrail, agent with MCP guardrails on tool calls and tool results, output guardrail, validated response" width="640"></p>

| | |
|---|---|
| Time | 20 minutes |
| Needs | Python 3.9+, nothing to install |
| OWASP | LLM01 · LLM02 · LLM06 · LLM07 |

## Run it

```bash
python3 labs/04-fully-guarded-agent/run.py                 # unguarded, then guarded
python3 labs/04-fully-guarded-agent/run.py --approve       # a human approves held actions
python3 labs/04-fully-guarded-agent/run.py --guard proofagent
python3 -m unittest labs/04-fully-guarded-agent/test_lab.py
```

## The four checkpoints

| # | Checkpoint | Checks | Decisions | Code |
|---|---|---|---|---|
| 1 | **Input** | PII, jailbreak, prompt injection | ALLOW · MASK · BLOCK | `GuardedAgent.run` |
| 2a | **Tool call** | ① policy rules: known tool, schema, destination allowlist ② guard model on the arguments | ALLOW · REVIEW (human) · BLOCK | `ToolPolicy`, `guard.check(..., "tool_call")` |
| 2b | **Tool result** | Indirect injection, PII in data | ALLOW · MASK (cleaned) | `guard.check(..., "tool_result")` |
| 3 | **Output** | Privacy, system-prompt canary, safety | ALLOW · MASK · BLOCK | `guard.check(..., "output")` |

**Your code decides to check, not the model.** If the LLM chooses whether to call the guard, an injection can talk it out of it.

## Expected outcome

```
scenario                              unguarded  guarded
direct injection                      UNSAFE     safe
jailbreak                             UNSAFE     safe
indirect injection in a web page      UNSAFE     safe
personal data in a tool result        UNSAFE     safe
data sent outside the company         UNSAFE     safe
benign: allowed destination           safe       safe
benign: question                      safe       safe
```

The last two rows matter as much as the first five. A guard that blocks useful work gets switched off.

## Design choices worth copying

- **Fail closed.** The remote guard returns BLOCK on timeouts and errors, and the default approver says no.
- **Placeholders all the way through.** The model sees `[EMAIL_1]`. Policy rules and tools see the real value, restored at the last moment, on your side.
- **Rules before models.** The allowlist decides `books@acme-accounting.com` needs approval in microseconds, and the guard model only judges what rules allow.
- **Memory stores guarded text only**, so a poisoned turn cannot come back later (Lab 05, RT-04).
- **A canary in the system prompt** (`ROUTE-7731`) makes prompt leaks detectable at the output, even when the input guard missed a paraphrase.

## Plug in your framework

The loop in [`guards/agent.py`](../../guards/agent.py) is about 100 lines, so you can read it in one go. The same four calls go into any framework:

- **LangGraph:** guard nodes around the agent node and a wrapped `ToolNode`. See [`examples/langgraph`](../../examples/langgraph).
- **Claude Code / Claude Agent SDK:** `PreToolUse` / `PostToolUse` hooks. See [`examples/claude-code`](../../examples/claude-code).
- **n8n, CrewAI, OpenAI Agents SDK:** see [`examples/`](../../examples) and the [Agent Guardrails Cookbook](https://github.com/ProofAgent-ai/agent-guardrails-cookbook).
