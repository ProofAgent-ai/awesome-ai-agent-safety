# Guardrails and Firewalls

Runtime guardrails, detection models and hosted platforms that inspect what goes into and comes out of LLM agents, including their tool calls.

## Contents

- [Open-source guardrail frameworks](#open-source-guardrail-frameworks)
- [Detection models and classifiers](#detection-models-and-classifiers)
- [PII and secrets detection](#pii-and-secrets-detection)
- [Commercial and hosted platforms](#commercial-and-hosted-platforms)

## Open-source guardrail frameworks

- [Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) — Microsoft toolkit for agent policy enforcement, identity and execution sandboxing. `OSS` `MIT`
- [Guardrails AI](https://github.com/guardrails-ai/guardrails) — Python framework for validating LLM inputs and outputs with a hub of reusable validators. `OSS` `Apache-2.0`
- [Invariant Guardrails](https://github.com/invariantlabs-ai/invariant) — Rule-based guardrails for agent traces and tool calls, by Invariant Labs (now part of Snyk). `OSS` `Apache-2.0`
- [LangKit](https://github.com/whylabs/langkit) — Toolkit that extracts safety and quality signals (injection, toxicity, PII) from prompts and responses. `OSS` `Apache-2.0`
- [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) — Meta's agent guardrail combining PromptGuard, alignment checks on agent reasoning, and CodeShield. `OSS`
- [LLM Guard](https://github.com/protectai/llm-guard) — Input and output scanners for prompt injection, PII, secrets and toxicity, by Protect AI. `OSS` `MIT` `Archived`
- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) — NVIDIA toolkit for programmable rails (input, output, dialog, retrieval, execution) around LLM and agent apps. `OSS`
- [OpenAI Guardrails (Python)](https://github.com/openai/openai-guardrails-python) — OpenAI library for configurable input/output checks wrapped around OpenAI client calls. `OSS` `MIT`
- [Plexiglass](https://github.com/w4-advisory/plexiglass) — Toolkit for detecting and protecting against LLM vulnerabilities. `OSS` `Apache-2.0`
- [Rebuff](https://github.com/protectai/rebuff) — Multi-layer prompt injection detector (heuristics, LLM check, vector DB, canary tokens). `OSS` `Apache-2.0` `Archived`
- [Superagent](https://github.com/superagent-ai/superagent) — Guardrails against prompt injection, data leaks and harmful outputs for AI apps. `OSS` `MIT`
- [Vigil](https://github.com/deadbits/vigil-llm) — Scanner for prompt injection and jailbreak inputs using YARA, vector similarity and canaries. `OSS` `Apache-2.0`

## Detection models and classifiers

- [Constitutional Classifiers](https://www.anthropic.com/research/constitutional-classifiers) — Anthropic research on input/output classifiers trained from a constitution to block universal jailbreaks.
- [GLiNER PII](https://huggingface.co/urchade/gliner_multi_pii-v1) — Multilingual GLiNER model fine-tuned for zero-shot PII entity extraction. `OSS`
- [gpt-oss-safeguard](https://huggingface.co/openai/gpt-oss-safeguard-20b) — OpenAI open-weight reasoning model that classifies content against a policy you supply. `OSS`
- [Granite Guardian](https://github.com/ibm-granite/granite-guardian) — IBM models that detect harm, jailbreaks, RAG hallucination and function-call risks in prompts and responses. `OSS` `Apache-2.0`
- [Llama Guard 4](https://huggingface.co/meta-llama/Llama-Guard-4-12B) — Meta multimodal safety classifier for prompts and responses against the MLCommons hazard taxonomy. `OSS`
- [Llama Prompt Guard 2](https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M) — Meta lightweight classifier for prompt injection and jailbreak detection. `OSS`
- [NemoGuard Content Safety](https://huggingface.co/nvidia/llama-3.1-nemoguard-8b-content-safety) — NVIDIA content-safety model used with NeMo Guardrails. `OSS`
- [OpenAI Moderation](https://platform.openai.com/docs/guides/moderation) — Hosted classifier for harmful text and image categories. `Commercial` `Free tier`
- [Protect AI DeBERTa prompt-injection v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2) — Fine-tuned DeBERTa classifier for prompt injection detection. `OSS`
- [Qwen3Guard](https://huggingface.co/Qwen/Qwen3Guard-Gen-8B) — Multilingual generative safety moderation model from the Qwen team. `OSS`
- [ShieldGemma](https://huggingface.co/google/shieldgemma-2b) — Google safety classifiers built on Gemma for prompts and responses. `OSS`
- [WildGuard](https://huggingface.co/allenai/wildguard) — Ai2 moderation model for harmful prompts, harmful responses and refusals. `OSS`

## PII and secrets detection

- [Bearer](https://github.com/Bearer/bearer) — SAST scanner focused on security and privacy (sensitive data flow) risks in code. `OSS`
- [detect-secrets](https://github.com/Yelp/detect-secrets) — Yelp baseline-driven secret detection for codebases and pre-commit. `OSS` `Apache-2.0`
- [ggshield](https://github.com/GitGuardian/ggshield) — GitGuardian CLI to detect hardcoded secrets in code and pre-commit hooks. `OSS` `MIT`
- [git-secrets](https://github.com/awslabs/git-secrets) — AWS Labs git hooks that prevent committing secrets. `OSS` `Apache-2.0`
- [Gitleaks](https://github.com/gitleaks/gitleaks) — Fast regex/entropy secret scanner for git repos, files and stdin. `OSS` `MIT`
- [Piiranha](https://huggingface.co/iiiorg/piiranha-v1-detect-personal-information) — Token-classification model for detecting personal information across languages. `OSS`
- [Presidio](https://github.com/data-privacy-stack/presidio) — Framework for detecting and anonymizing PII in text, images and structured data (originally Microsoft). `OSS` `MIT`
- [Secrets Patterns DB](https://github.com/mazen160/secrets-patterns-db) — Open database of regex patterns for API keys, tokens and passwords. `OSS` `CC-BY-SA-4.0`
- [TruffleHog](https://github.com/trufflesecurity/trufflehog) — Finds and verifies leaked credentials across git, cloud storage and more. `OSS` `AGPL-3.0`
- [Amazon Comprehend](https://aws.amazon.com/comprehend/) — AWS NLP service with PII detection and redaction. `Commercial`
- [Azure AI Language PII detection](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/overview) — Azure service for detecting and redacting PII in text and conversations. `Commercial`
- [Google Sensitive Data Protection](https://cloud.google.com/sensitive-data-protection) — Google Cloud DLP for discovering, classifying and de-identifying sensitive data. `Commercial`
- [Nightfall](https://www.nightfall.ai) — DLP platform detecting PII and secrets across SaaS and AI apps. `Commercial`
- [Private AI](https://www.private-ai.com) — PII detection and redaction API supporting many languages and formats. `Commercial`
- [Skyflow LLM Privacy Vault](https://www.skyflow.com/product/llm-privacy-vault) — Vault that tokenizes sensitive data before it reaches LLMs. `Commercial`

## Commercial and hosted platforms

- [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/) — Configurable content filters, denied topics, PII filters, prompt-attack detection and automated reasoning checks. `Commercial`
- [Arthur](https://www.arthur.ai) — AI monitoring and guardrails platform; also ships the open-source [Arthur Engine](https://github.com/arthur-ai/arthur-engine) (`MIT`). `Commercial`
- [Azure AI Content Safety Prompt Shields](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection) — Detects direct jailbreaks and indirect (document) prompt injection. `Commercial`
- [CalypsoAI](https://www.calypsoai.com) — AI security platform with runtime defense and red teaming (part of F5). `Commercial`
- [Cloudflare Firewall for AI](https://www.cloudflare.com/application-services/products/firewall-for-ai/) — WAF layer that detects prompt injection, PII and unsafe topics in LLM traffic. `Commercial`
- [F5 AI Gateway](https://www.f5.com/products/ai-gateway) — Gateway that inspects and enforces policy on AI traffic. `Commercial`
- [Google Cloud Model Armor](https://cloud.google.com/security/products/model-armor) — Screens prompts and responses for injection, jailbreaks, sensitive data and malicious URLs. `Commercial`
- [HiddenLayer](https://www.hiddenlayer.com) — AI security platform including runtime detection for models and agents. `Commercial`
- [Kong AI Gateway](https://www.kong.com/products/kong-ai-gateway) — API gateway with AI plugins for prompt guarding, PII sanitization and semantic filters. `Commercial`
- [Lakera Guard](https://www.lakera.ai/lakera-guard) — API that screens LLM inputs and outputs for prompt injection, data leakage and harmful content. `Commercial` `Free tier`
- [Lasso Security](https://www.lasso.security) — GenAI and agent security platform with runtime policies and MCP gateway. `Commercial`
- [Noma Security](https://noma.security) — AI and agent security posture and runtime protection. `Commercial`
- [Palo Alto Networks Prisma AIRS](https://www.paloaltonetworks.com/prisma/prisma-ai-runtime-security) — AI runtime security for prompts, responses, models and agents. `Commercial`
- [Pillar Security](https://www.pillar.security) — AI security platform with runtime guardrails and red teaming. `Commercial`
- [Prompt Security](https://www.prompt.security) — Runtime protection for employee AI use and homegrown AI apps (part of SentinelOne). `Commercial`
- [PromptArmor](https://www.promptarmor.com) — Detection and threat intelligence for indirect prompt injection and AI data leakage. `Commercial`
- [ProofAgent](https://proofagent.ai) — Runtime guardrail for agents: PII masking, prompt-injection and tool-call checks over API or MCP; free tier. `Commercial` `Free tier`
- [Straiker](https://www.straiker.ai) — Runtime guardrails and attack simulation for AI agents. `Commercial`
- [Zenity](https://zenity.io) — Security and governance for AI agents and low-code platforms. `Commercial`

Missing something? [Open a PR](../CONTRIBUTING.md).
