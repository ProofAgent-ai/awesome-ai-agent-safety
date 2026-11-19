# Benchmarks

Benchmarks for measuring prompt-injection robustness, jailbreak resistance and safe behavior of LLM agents.

License is taken from the GitHub repository's license field. "Unverified" means the repo declares no standard SPDX license (custom or none); check the repo before reuse.

## Contents

- [Agent and prompt-injection benchmarks](#agent-and-prompt-injection-benchmarks)
- [Jailbreak and harmful-behavior benchmarks](#jailbreak-and-harmful-behavior-benchmarks)
- [MCP benchmarks](#mcp-benchmarks)
- [Privacy benchmarks](#privacy-benchmarks)

## Agent and prompt-injection benchmarks

| Name | What it measures | Link | License |
|---|---|---|---|
| AgentDojo | Utility and security of tool-using agents under indirect injection (workspace, banking, travel, Slack) | [paper](https://arxiv.org/abs/2406.13352) · [code](https://github.com/ethz-spylab/agentdojo) | MIT |
| InjecAgent | Indirect injection via tool responses: direct harm and data exfiltration | [paper](https://arxiv.org/abs/2403.02691) · [code](https://github.com/uiuc-kang-lab/InjecAgent) | MIT |
| ASB (Agent Security Bench) | Injection, memory poisoning and backdoor attacks plus defenses across agent scenarios | [paper](https://arxiv.org/abs/2410.02644) · [code](https://github.com/agiresearch/ASB) | MIT |
| BIPIA | Indirect prompt injection in email, web, table and code QA | [paper](https://arxiv.org/abs/2312.14197) · [code](https://github.com/microsoft/BIPIA) | Unverified |
| Open-Prompt-Injection | Formalized injection attacks and defenses across tasks | [paper](https://arxiv.org/abs/2310.12815) · [code](https://github.com/liu00222/Open-Prompt-Injection) | MIT |
| Tensor Trust | Hijacking and prompt-extraction robustness from game data | [paper](https://arxiv.org/abs/2311.01011) · [code](https://github.com/HumanCompatibleAI/tensor-trust) | BSD-2-Clause |
| WASP | Web-agent security against realistic prompt injection | [paper](https://arxiv.org/abs/2504.18575) · [code](https://github.com/facebookresearch/wasp) | Unverified |
| VPI-Bench | Visual prompt injection on computer-use and browser agents | [paper](https://arxiv.org/abs/2506.02456) | — |
| BrowserART | Harmful behavior of browser agents vs. chat refusals | [paper](https://arxiv.org/abs/2410.13886) · [code](https://github.com/scaleapi/browser-art) | Unverified |
| PINT (Lakera) | Prompt-injection detector accuracy and false positives | [code](https://github.com/lakeraai/pint-benchmark) | MIT |
| GenTel-Bench | Prompt-injection detection across scenarios | [paper](https://arxiv.org/abs/2409.19521) | — |
| R-Judge | Whether LLMs can judge safety risks in agent interaction records | [paper](https://arxiv.org/abs/2401.10019) · [code](https://github.com/Lordog/R-Judge) | No license declared |
| ToolEmu | Risky agent actions with LM-emulated tools and safety evaluator | [paper](https://arxiv.org/abs/2309.15817) · [code](https://github.com/ryoungj/ToolEmu) | Apache-2.0 |
| Agent-SafetyBench | Agent safety across 349 environments and 2,000 test cases | [paper](https://arxiv.org/abs/2412.14470) · [code](https://github.com/thu-coai/Agent-SafetyBench) | MIT |
| ToolSword | Tool-learning safety at input, execution and output stages | [paper](https://arxiv.org/abs/2402.10753) | — |
| RedCode | Risky code execution and generation by code agents | [paper](https://arxiv.org/abs/2411.07781) · [code](https://github.com/AI-secure/RedCode) | MIT |
| AgentPoison | Memory/knowledge-base poisoning of RAG agents | [paper](https://arxiv.org/abs/2407.12784) · [code](https://github.com/AI-secure/AgentPoison) | MIT |
| DoomArena | Plug-in attack framework for τ-bench, BrowserGym and similar environments | [paper](https://arxiv.org/abs/2504.14064) · [code](https://github.com/ServiceNow/DoomArena) | Apache-2.0 |
| SHADE-Arena | Agent sabotage of hidden side-tasks and monitor detection | [paper](https://arxiv.org/abs/2506.15740) | — |
| CyberSecEval 2 | Prompt injection, code-interpreter abuse and offensive cyber capability | [paper](https://arxiv.org/abs/2404.13161) · [code](https://github.com/meta-llama/PurpleLlama) | Unverified (custom) |

## Jailbreak and harmful-behavior benchmarks

| Name | What it measures | Link | License |
|---|---|---|---|
| AgentHarm | Harmful multi-step agent tasks and jailbreak robustness | [paper](https://arxiv.org/abs/2410.09024) · [code](https://github.com/UKGovernmentBEIS/inspect_evals) | MIT (inspect_evals) |
| HarmBench | Automated red-teaming attacks vs. refusal robustness | [paper](https://arxiv.org/abs/2402.04249) · [code](https://github.com/centerforaisafety/HarmBench) | MIT |
| JailbreakBench | Standardized jailbreak behaviors, artifacts and leaderboard | [paper](https://arxiv.org/abs/2404.01318) · [code](https://github.com/JailbreakBench/jailbreakbench) | MIT |
| SALAD-Bench | Hierarchical safety, attack and defense evaluation | [paper](https://arxiv.org/abs/2402.05044) | — |
| SafetyBench | Multiple-choice safety evaluation (English/Chinese) | [code](https://github.com/thu-coai/SafetyBench) | MIT |

## MCP benchmarks

| Name | What it measures | Link | License |
|---|---|---|---|
| MCPTox | Tool-poisoning attack success on real-world MCP servers | [paper](https://arxiv.org/abs/2508.14925) | — |
| MCPSecBench | Attacks across MCP client, server, transport and host layers | [paper](https://arxiv.org/abs/2508.13220) · [code](https://github.com/AIS2Lab/MCPSecBench) | MIT |
| MCP-SafetyBench | Safety of LLMs with real-world MCP servers in multi-turn tasks | [paper](https://arxiv.org/abs/2512.15163) | — |

## Privacy benchmarks

| Name | What it measures | Link | License |
|---|---|---|---|
| PrivacyLens | Privacy-norm violations in agent actions | [paper](https://arxiv.org/abs/2409.00138) · [code](https://github.com/SALT-NLP/PrivacyLens) | MIT |
| ConfAIde | Contextual-integrity reasoning about private information | [paper](https://arxiv.org/abs/2310.17884) | — |
| EIA | Web-agent PII leakage via environmental injection | [paper](https://arxiv.org/abs/2409.11295) · [code](https://github.com/OSU-NLP-Group/EIA_against_webagent) | MIT |

Missing something? [Open a PR](../CONTRIBUTING.md).
