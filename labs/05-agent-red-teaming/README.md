# Lab 05 · Multi-turn red teaming with actionable findings

**You will learn:** why single-prompt tests miss most real attacks, how to run multi-turn scenarios against baseline and guarded agents, and how to turn results into an attack-success rate and a list of fixes.

| | |
|---|---|
| Time | 15 minutes |
| Needs | Python 3.9+, nothing to install |
| OWASP | LLM01 · LLM02 · LLM06 · LLM07 |

## Run it

```bash
python3 labs/05-agent-red-teaming/run.py --guard none
python3 labs/05-agent-red-teaming/run.py --report findings.md --json findings.json
python3 -m unittest labs/05-agent-red-teaming/test_lab.py
```

## Scenarios

| ID | Scenario | Why single-turn tests miss it |
|---|---|---|
| RT-01 | Crescendo to system prompt | Each early turn is harmless |
| RT-02 | Paraphrased extraction | No trigger words: only the output canary catches it |
| RT-03 | Split payload | The attack only exists when turns are joined |
| RT-04 | Memory poisoning, triggered later | The harmful action happens on an innocent turn ("done") |
| RT-05 | Indirect injection, then follow-up | The instruction came from a tool, the trigger from the user |
| RT-06 | Social engineering for personal data | A plausible request with a destination outside the company |
| RT-07 | Secret file via jailbreak | Role-play setup, then the ask |

## Expected outcome

| Guard | Attack success rate |
|---|---|
| `none` | 100% (7/7) |
| `local` | 0% (0/7), and the report shows **which checkpoint** stopped each one |

As in Lab 01, 0% on scenarios written next to the rules is a starting point, not a verdict. Add scenarios in other languages and encodings, then run them against a real model.

## Scale it up

| Tool | Use it for |
|---|---|
| [ProofAgent Harness](https://github.com/ProofAgent-ai/proofagent-harness) | Multi-turn adversarial scenarios against production agents, in CI |
| [PyRIT](https://github.com/microsoft/PyRIT) | Orchestrated attacks, converters, scoring |
| [garak](https://github.com/NVIDIA/garak) | Broad LLM vulnerability probes |
| [promptfoo](https://github.com/promptfoo/promptfoo) | Red-team configs and regression tests in CI |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Benchmarking agents under indirect injection |

More in [`resources/evaluation-tools.md`](../../resources/evaluation-tools.md) and [`resources/benchmarks.md`](../../resources/benchmarks.md).
