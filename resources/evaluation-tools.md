# Evaluation and Red Teaming Tools

Tools, harnesses and benchmarks for attacking and evaluating LLM applications and agents before (and after) they ship.

## Contents

- [Red teaming and vulnerability scanners](#red-teaming-and-vulnerability-scanners)
- [Evaluation frameworks](#evaluation-frameworks)
- [Agent security benchmarks and harnesses](#agent-security-benchmarks-and-harnesses)
- [Commercial red teaming](#commercial-red-teaming)

## Red teaming and vulnerability scanners

- [Agentic Radar](https://github.com/splx-ai/agentic-radar) — Scans agentic workflow code to map tools and flag vulnerabilities. `OSS` `Apache-2.0`
- [Agentic Security](https://github.com/msoedov/agentic_security) — LLM vulnerability scanner and red teaming kit with fuzzing and multi-step attacks. `OSS` `Apache-2.0`
- [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — Tencent red teaming platform covering agents, skills, MCP servers and AI infrastructure. `OSS` `Apache-2.0`
- [AI Red Teaming Playground Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs) — Microsoft hands-on challenge labs for AI red teaming training. `OSS` `MIT`
- [Augustus](https://github.com/praetorian-inc/augustus) — Praetorian LLM security testing framework for prompt injection and jailbreaks. `OSS` `Apache-2.0`
- [DeepTeam](https://github.com/confident-ai/deepteam) — Red teaming framework for LLMs and agents with built-in attacks and vulnerability metrics. `OSS` `Apache-2.0`
- [FuzzyAI](https://github.com/cyberark/FuzzyAI) — CyberArk automated LLM fuzzer for jailbreak discovery. `OSS` `Apache-2.0`
- [garak](https://github.com/NVIDIA/garak) — NVIDIA LLM vulnerability scanner with probes for injection, leakage, jailbreaks and more. `OSS` `Apache-2.0`
- [power-pwn](https://github.com/mbrg/power-pwn) — Offensive and defensive toolset for recon and assessment of AI agents such as Copilot Studio. `OSS` `MIT`
- [promptfoo](https://github.com/promptfoo/promptfoo) — CLI for evals and red teaming of prompts, RAG and agents, with CI integration. `OSS` `MIT`
- [promptmap](https://github.com/utkusen/promptmap) — Security scanner for prompt injection in custom LLM applications. `OSS` `GPL-3.0`
- [ProofAgent Harness](https://github.com/ProofAgent-ai/proofagent-harness) — open-source multi-turn adversarial test harness for agents, runs in CI. `OSS` `Apache-2.0`
- [ps-fuzz](https://github.com/prompt-security/ps-fuzz) — Prompt Security fuzzer for hardening system prompts against attacks. `OSS` `MIT`
- [PyRIT](https://github.com/microsoft/PyRIT) — Microsoft Python Risk Identification Tool for automated generative AI red teaming. `OSS` `MIT`
- [Rogue](https://github.com/rogue-security/rogue) — Agent evaluator and red team platform that tests agents against policies. `OSS`

## Evaluation frameworks

- [DeepEval](https://github.com/confident-ai/deepeval) — LLM evaluation framework with metrics for agents, RAG and safety. `OSS` `Apache-2.0`
- [Giskard](https://github.com/Giskard-AI/giskard-oss) — Open-source evaluation and testing library for LLM agents, including vulnerability scans. `OSS` `Apache-2.0`
- [Inspect](https://github.com/UKGovernmentBEIS/inspect_ai) — UK AISI framework for LLM and agent evaluations with sandboxed tool use. `OSS` `MIT`
- [Inspect Evals](https://github.com/UKGovernmentBEIS/inspect_evals) — Community collection of evals (including agentic and safety evals) for Inspect. `OSS` `MIT`
- [Invariant Explorer](https://github.com/invariantlabs-ai/explorer) — Tool for inspecting and analyzing agent traces. `OSS` `Apache-2.0`
- [OpenAI Evals](https://github.com/openai/evals) — Framework and registry for evaluating LLMs and LLM systems. `OSS`
- [Phoenix](https://github.com/Arize-ai/phoenix) — Arize AI observability and evaluation platform for LLM apps and agents. `OSS`
- [TruLens](https://github.com/truera/trulens) — Evaluation and tracking for LLM experiments and agents. `OSS` `MIT`

## Agent security benchmarks and harnesses

- [AgentDojo](https://github.com/ethz-spylab/agentdojo) — Dynamic environment for evaluating prompt injection attacks and defenses on tool-using agents. `OSS` `MIT`
- [AgentHarm](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) — UK AISI / Gray Swan benchmark of harmful multi-step agent tasks. `OSS`
- [Agent Security Bench (ASB)](https://github.com/agiresearch/ASB) — Benchmark of attacks and defenses across agent scenarios and tools. `OSS` `MIT`
- [Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench) — Benchmark of interactive environments for agent safety failures. `OSS` `MIT`
- [BIPIA](https://github.com/microsoft/BIPIA) — Microsoft benchmark for indirect prompt injection robustness. `OSS` `Archived`
- [DoomArena](https://github.com/ServiceNow/DoomArena) — ServiceNow framework for testing agents against evolving security threats. `OSS` `Apache-2.0`
- [HarmBench](https://github.com/centerforaisafety/HarmBench) — Standardized evaluation for automated red teaming and refusal robustness. `OSS` `MIT`
- [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) — Benchmark for indirect prompt injection in tool-integrated agents. `OSS` `MIT`
- [JailbreakBench](https://github.com/JailbreakBench/jailbreakbench) — Open robustness benchmark and leaderboard for jailbreak attacks. `OSS` `MIT`
- [LLMail-Inject](https://github.com/microsoft/llmail-inject-challenge) — Code and data from Microsoft's adaptive prompt injection challenge against an email agent. `OSS` `MIT`
- [PINT Benchmark](https://github.com/lakeraai/pint-benchmark) — Lakera benchmark for prompt injection detectors. `OSS` `MIT` `Archived`
- [R-Judge](https://github.com/Lordog/R-Judge) — Benchmark of LLM ability to judge safety risks in agent interaction records. `OSS`
- [τ-bench](https://github.com/sierra-research/tau-bench) — Benchmark of tool-agent-user interaction with policy adherence in realistic domains. `OSS` `MIT`
- [WASP](https://github.com/facebookresearch/wasp) — Meta benchmark for prompt injection against web agents. `OSS` `Archived`

## Commercial red teaming

- [Lakera Red](https://www.lakera.ai/lakera-red) — Lakera red teaming service for GenAI apps and agents. `Commercial`
- [Mindgard](https://www.mindgard.ai) — Automated AI red teaming and security testing. `Commercial`
- [Repello AI](https://repello.ai) — AI red teaming and runtime protection platform. `Commercial`
- [SPLX](https://www.splx.ai) — Automated red teaming and runtime protection for AI agents. `Commercial`

Missing something? [Open a PR](../CONTRIBUTING.md).
