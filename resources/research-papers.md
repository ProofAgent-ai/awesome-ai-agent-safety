# Research Papers

Key papers on prompt injection, jailbreaks, agent and tool-use security, MCP, privacy leakage and red teaming for LLM agents.

All arXiv links were checked against the arXiv API. Venue is given only where we are confident; otherwise the arXiv year is listed.

## Contents

- [Surveys and position papers](#surveys-and-position-papers)
- [Prompt injection](#prompt-injection)
- [Defenses](#defenses)
- [Jailbreaks](#jailbreaks)
- [Agent and tool-use security](#agent-and-tool-use-security)
- [MCP security](#mcp-security)
- [Privacy and data leakage](#privacy-and-data-leakage)
- [Multi-agent risks](#multi-agent-risks)
- [Evaluation methodology](#evaluation-methodology)

## Surveys and position papers

- **AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways** — Zehang Deng et al., arXiv 2024. [paper](https://arxiv.org/abs/2406.02630) — Threat taxonomy organized around the agent loop (perception, brain, action).
- **Security of AI Agents** — Yifeng He et al., arXiv 2024. [paper](https://arxiv.org/abs/2406.08689) — Systems-security view of agent vulnerabilities and mitigations.
- **Jailbreak Attacks and Defenses Against Large Language Models: A Survey** — Sibo Yi et al., arXiv 2024. [paper](https://arxiv.org/abs/2407.04295) — Taxonomy of black-/white-box jailbreaks and defenses.
- **From LLMs to MLLMs to Agents: A Survey of Emerging Paradigms in Jailbreak Attacks and Defenses within LLM Ecosystem** — Yanxu Mao et al., arXiv 2025. [paper](https://arxiv.org/abs/2506.15170) — Extends jailbreak taxonomy to multimodal models and agents.
- **A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents** — Lingbo Mo et al., arXiv 2024. [paper](https://arxiv.org/abs/2402.10196) — Maps attack surfaces across agent components.
- **A Survey on the Memory Mechanism of Large Language Model based Agents** — Zeyu Zhang et al., arXiv 2024. [paper](https://arxiv.org/abs/2404.13501) — Background on agent memory, the target of memory-poisoning attacks.
- **Position: Adversarial ML for LLMs Is Not Making Any Progress** — Javier Rando et al., arXiv 2025. [paper](https://arxiv.org/abs/2502.02260) — Critique of LLM security research practice and evaluation.

## Prompt injection

- **Ignore Previous Prompt: Attack Techniques For Language Models** — Fábio Perez et al., arXiv 2022. [paper](https://arxiv.org/abs/2211.09527) — Early systematic study of goal hijacking and prompt leaking (PromptInject).
- **Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection** — Kai Greshake et al., AISec 2023. [paper](https://arxiv.org/abs/2302.12173) — Defined indirect prompt injection via retrieved content.
- **Prompt Injection attack against LLM-integrated Applications** — Yi Liu et al., arXiv 2023. [paper](https://arxiv.org/abs/2306.05499) — HouYi black-box injection against real apps.
- **Formalizing and Benchmarking Prompt Injection Attacks and Defenses** — Yupei Liu et al., USENIX Security 2024. [paper](https://arxiv.org/abs/2310.12815) · [code](https://github.com/liu00222/Open-Prompt-Injection) — Formal framework and benchmark of attacks/defenses.
- **Assessing Prompt Injection Risks in 200+ Custom GPTs** — Jiahao Yu et al., arXiv 2023. [paper](https://arxiv.org/abs/2311.11538) — System-prompt and file leakage from custom GPTs.
- **Tensor Trust: Interpretable Prompt Injection Attacks from an Online Game** — Sam Toyer et al., ICLR 2024. [paper](https://arxiv.org/abs/2311.01011) · [code](https://github.com/HumanCompatibleAI/tensor-trust) — Large human-generated attack/defense dataset.
- **Automatic and Universal Prompt Injection Attacks against Large Language Models** — Xiaogeng Liu et al., arXiv 2024. [paper](https://arxiv.org/abs/2403.04957) — Gradient-based universal injections.
- **Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models** — Jingwei Yi et al., arXiv 2023. [paper](https://arxiv.org/abs/2312.14197) · [code](https://github.com/microsoft/BIPIA) — BIPIA benchmark and boundary-awareness defenses.
- **Cognitive Overload Attack: Prompt Injection for Long Context** — Bibek Upadhayay et al., arXiv 2024. [paper](https://arxiv.org/abs/2410.11272) — Exploits long-context cognitive load.
- **Can Indirect Prompt Injection Attacks Be Detected and Removed?** — Yulin Chen et al., arXiv 2025. [paper](https://arxiv.org/abs/2502.16580) — Evaluates detection and removal of injected content.

## Defenses

- **The Dual LLM pattern for building AI assistants that can resist prompt injection** — Simon Willison, blog 2023. [post](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) — Privileged vs. quarantined LLM split; precursor to CaMeL.
- **Defending Against Indirect Prompt Injection Attacks With Spotlighting** — Keegan Hines et al., arXiv 2024. [paper](https://arxiv.org/abs/2403.14720) — Delimiting, datamarking and encoding of untrusted input.
- **StruQ: Defending Against Prompt Injection with Structured Queries** — Sizhe Chen et al., USENIX Security 2025. [paper](https://arxiv.org/abs/2402.06363) · [code](https://github.com/Sizhe-Chen/StruQ) — Separate instruction/data channels plus fine-tuning.
- **SecAlign: Defending Against Prompt Injection with Preference Optimization** — Sizhe Chen et al., arXiv 2024. [paper](https://arxiv.org/abs/2410.05451) · [code](https://github.com/facebookresearch/SecAlign) — Preference optimization to ignore injected instructions.
- **Meta-SecAlign: Training LLMs against Prompt Injection for Robust Agents** — Sizhe Chen et al., arXiv 2025. [paper](https://arxiv.org/abs/2507.02735) — Open-weight model with built-in injection robustness.
- **The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions** — Eric Wallace et al., arXiv 2024. [paper](https://arxiv.org/abs/2404.13208) — System > user > tool output priority training.
- **Instructional Segment Embedding: Improving LLM Safety with Instruction Hierarchy** — Tong Wu et al., arXiv 2024. [paper](https://arxiv.org/abs/2410.09102) — Architectural segment embeddings for the hierarchy.
- **Defeating Prompt Injections by Design (CaMeL)** — Edoardo Debenedetti et al., arXiv 2025. [paper](https://arxiv.org/abs/2503.18813) · [code](https://github.com/google-research/camel-prompt-injection) — Capability-based control/data-flow separation with provable guarantees.
- **Design Patterns for Securing LLM Agents against Prompt Injections** — Luca Beurer-Kellner et al., arXiv 2025. [paper](https://arxiv.org/abs/2506.08837) — Six principled patterns (plan-then-execute, map-reduce, etc.).
- **Securing AI Agents with Information-Flow Control** — Manuel Costa et al., arXiv 2025. [paper](https://arxiv.org/abs/2505.23643) — Taint tracking / IFC for agent planners (FIDES).
- **Progent: Securing AI Agents with Privilege Control** — Tianneng Shi et al., arXiv 2025. [paper](https://arxiv.org/abs/2504.11703) — Least-privilege policies on tool calls.
- **MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents** — Kaijie Zhu et al., arXiv 2025. [paper](https://arxiv.org/abs/2502.05174) — Detects injections via masked re-execution.
- **The Task Shield: Enforcing Task Alignment to Defend Against Indirect Prompt Injection in LLM Agents** — Feiran Jia et al., arXiv 2024. [paper](https://arxiv.org/abs/2412.16682) — Checks each action serves the user goal.
- **DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks** — Yupei Liu et al., arXiv 2025. [paper](https://arxiv.org/abs/2504.11358) — Adversarially trained detector.
- **ShieldAgent: Shielding Agents via Verifiable Safety Policy Reasoning** — Zhaorun Chen et al., arXiv 2025. [paper](https://arxiv.org/abs/2503.22738) — Guardrail agent with verifiable policy checks.
- **LlamaFirewall: An open source guardrail system for building secure AI agents** — Sahana Chennabasappa et al., arXiv 2025. [paper](https://arxiv.org/abs/2505.03574) · [code](https://github.com/meta-llama/PurpleLlama) — PromptGuard, alignment checks and code scanning.
- **Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations** — Hakan Inan et al., arXiv 2023. [paper](https://arxiv.org/abs/2312.06674) — Influential safety classifier model.
- **Baseline Defenses for Adversarial Attacks Against Aligned Language Models** — Neel Jain et al., arXiv 2023. [paper](https://arxiv.org/abs/2309.00614) — Perplexity filtering, paraphrasing, retokenization.
- **SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks** — Alexander Robey et al., arXiv 2023. [paper](https://arxiv.org/abs/2310.03684) — Randomized smoothing against suffix attacks.
- **Defending Against Unforeseen Failure Modes with Latent Adversarial Training** — Stephen Casper et al., arXiv 2024. [paper](https://arxiv.org/abs/2403.05030) — Robustness via latent-space perturbations.

## Jailbreaks

- **Jailbroken: How Does LLM Safety Training Fail?** — Alexander Wei et al., NeurIPS 2023. [paper](https://arxiv.org/abs/2307.02483) — Competing objectives and mismatched generalization.
- **Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG)** — Andy Zou et al., arXiv 2023. [paper](https://arxiv.org/abs/2307.15043) · [code](https://github.com/llm-attacks/llm-attacks) — Gradient-searched universal adversarial suffixes.
- **Jailbreaking Black Box Large Language Models in Twenty Queries (PAIR)** — Patrick Chao et al., arXiv 2023. [paper](https://arxiv.org/abs/2310.08419) · [code](https://github.com/patrickrchao/JailbreakingLLMs) — Attacker-LLM iterative refinement.
- **Tree of Attacks: Jailbreaking Black-Box LLMs Automatically (TAP)** — Anay Mehrotra et al., NeurIPS 2024. [paper](https://arxiv.org/abs/2312.02119) · [code](https://github.com/RICommunity/TAP) — Tree search with pruning over attack prompts.
- **AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models** — Xiaogeng Liu et al., ICLR 2024. [paper](https://arxiv.org/abs/2310.04451) — Genetic-algorithm readable jailbreaks.
- **Many-shot Jailbreaking** — Cem Anil et al. (Anthropic), NeurIPS 2024. [paper](https://www.anthropic.com/research/many-shot-jailbreaking) — Long-context in-context attacks scale with shot count.
- **Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack** — Mark Russinovich et al., arXiv 2024. [paper](https://arxiv.org/abs/2404.01833) — Gradual multi-turn escalation.
- **Emerging Vulnerabilities in Frontier Models: Multi-Turn Jailbreak Attacks** — Tom Gibbs et al., arXiv 2024. [paper](https://arxiv.org/abs/2409.00137) — Multi-turn vs. single-turn jailbreak dataset.
- **Jailbreaking Leading Safety-Aligned LLMs with Simple Adaptive Attacks** — Maksym Andriushchenko et al., arXiv 2024. [paper](https://arxiv.org/abs/2404.02151) — Near-100% success with simple adaptive methods.
- **"Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models** — Xinyue Shen et al., ACM CCS 2024. [paper](https://arxiv.org/abs/2308.03825) · [code](https://github.com/verazuo/jailbreak_llms) — Largest study of community jailbreaks.
- **Jailbreaking ChatGPT via Prompt Engineering: An Empirical Study** — Yi Liu et al., arXiv 2023. [paper](https://arxiv.org/abs/2305.13860) — Early jailbreak-pattern taxonomy.
- **Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation** — Yangsibo Huang et al., arXiv 2023. [paper](https://arxiv.org/abs/2310.06987) — Decoding-config manipulation breaks alignment.
- **Multilingual Jailbreak Challenges in Large Language Models** — Yue Deng et al., arXiv 2023. [paper](https://arxiv.org/abs/2310.06474) — Low-resource languages bypass safety.
- **Query-Based Adversarial Prompt Generation** — Jonathan Hayase et al., arXiv 2024. [paper](https://arxiv.org/abs/2402.12329) — Black-box query-only GCG-style attacks.
- **WildTeaming at Scale: From In-the-Wild Jailbreaks to (Adversarially) Safer Language Models** — Liwei Jiang et al., arXiv 2024. [paper](https://arxiv.org/abs/2406.18510) — Mined tactics and the WildJailbreak dataset.
- **Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast** — Xiangming Gu et al., arXiv 2024. [paper](https://arxiv.org/abs/2402.08567) — Infectious jailbreaks spreading across agents.

## Agent and tool-use security

- **Identifying the Risks of LM Agents with an LM-Emulated Sandbox (ToolEmu)** — Yangjun Ruan et al., ICLR 2024. [paper](https://arxiv.org/abs/2309.15817) · [code](https://github.com/ryoungj/ToolEmu) — LM-emulated tools for risk discovery.
- **InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents** — Qiusi Zhan et al., Findings of ACL 2024. [paper](https://arxiv.org/abs/2403.02691) · [code](https://github.com/uiuc-kang-lab/InjecAgent) — Injection via tool outputs.
- **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents** — Edoardo Debenedetti et al., NeurIPS 2024 (D&B). [paper](https://arxiv.org/abs/2406.13352) · [code](https://github.com/ethz-spylab/agentdojo) — De facto agent injection benchmark.
- **Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents** — Qiusi Zhan et al., arXiv 2025. [paper](https://arxiv.org/abs/2503.00061) — All eight tested defenses bypassed adaptively.
- **AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases** — Zhaorun Chen et al., NeurIPS 2024. [paper](https://arxiv.org/abs/2407.12784) · [code](https://github.com/AI-secure/AgentPoison) — Backdoor triggers in RAG/memory.
- **EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage** — Zeyi Liao et al., arXiv 2024. [paper](https://arxiv.org/abs/2409.11295) · [code](https://github.com/OSU-NLP-Group/EIA_against_webagent) — Hidden web elements exfiltrate PII.
- **WIPI: A New Web Threat for LLM-Driven Web Agents** — Fangzhou Wu et al., arXiv 2024. [paper](https://arxiv.org/abs/2402.16965) — Web-page indirect injection.
- **AdvAgent: Controllable Blackbox Red-teaming on Web Agents** — Chejian Xu et al., arXiv 2024. [paper](https://arxiv.org/abs/2410.17401) — RL-trained adversarial injection generator.
- **Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents** — Priyanshu Kumar et al., arXiv 2024. [paper](https://arxiv.org/abs/2410.13886) · [code](https://github.com/scaleapi/browser-art) — Chat refusals don't transfer to agents.
- **When LLMs Go Online: The Emerging Threat of Web-Enabled LLMs** — Hanna Kim et al., arXiv 2024. [paper](https://arxiv.org/abs/2410.14569) — Web agents for cyberattacks on people.
- **VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents** — Tri Cao et al., arXiv 2025. [paper](https://arxiv.org/abs/2506.02456) — Visual injection against computer-use agents.
- **Jailbreaking LLM-Controlled Robots** — Alexander Robey et al., arXiv 2024. [paper](https://arxiv.org/abs/2410.13691) — Physical-world consequences of jailbreaks.
- **ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages** — Junjie Ye et al., arXiv 2024. [paper](https://arxiv.org/abs/2402.10753) — Safety across input, execution and output stages.
- **Takedown: How It's Done in Modern Coding Agent Exploits** — Eunkyu Lee et al., arXiv 2025. [paper](https://arxiv.org/abs/2509.24240) — Exploits against coding agents.
- **Attacks on Third-Party APIs of Large Language Models** — Wanru Zhao et al., arXiv 2024. [paper](https://arxiv.org/abs/2404.16891) — Plugin/API supply-chain attacks.

## MCP security

- **Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions** — Xinyi Hou et al., arXiv 2025. [paper](https://arxiv.org/abs/2503.23278) — MCP lifecycle threat model.
- **MCP Safety Audit: LLMs with the Model Context Protocol Allow Major Security Exploits** — Brandon Radosevich et al., arXiv 2025. [paper](https://arxiv.org/abs/2504.03767) — Demonstrated MCP exploits and the McpSafetyScanner.
- **Enterprise-Grade Security for the Model Context Protocol (MCP): Frameworks and Mitigation Strategies** — Vineeth Sai Narajala et al., arXiv 2025. [paper](https://arxiv.org/abs/2504.08623) — Enterprise mitigations for MCP deployments.
- **ETDI: Mitigating Tool Squatting and Rug Pull Attacks in Model Context Protocol (MCP)** — Manish Bhatt et al., arXiv 2025. [paper](https://arxiv.org/abs/2506.01333) — Signed tool definitions with OAuth and policy.
- **MCPTox: A Benchmark for Tool Poisoning Attack on Real-World MCP Servers** — Zhiqiang Wang et al., arXiv 2025. [paper](https://arxiv.org/abs/2508.14925) — Tool-poisoning success across real servers.
- **MCPSecBench: A Systematic Security Benchmark and Playground for Testing Model Context Protocols** — Yixuan Yang et al., arXiv 2025. [paper](https://arxiv.org/abs/2508.13220) · [code](https://github.com/AIS2Lab/MCPSecBench) — Attack taxonomy across MCP layers.
- **MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers** — Xuanjun Zong et al., arXiv 2025. [paper](https://arxiv.org/abs/2512.15163) — Multi-server safety evaluation.
- **MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP** — Ruiqi Li et al., arXiv 2026. [paper](https://arxiv.org/abs/2601.07395) — Automated implicit poisoning attacks.
- **TRUSTDESC: Preventing Tool Poisoning in LLM Applications via Trusted Description Generation** — Hengkai Ye et al., arXiv 2026. [paper](https://arxiv.org/abs/2604.07536) — Regenerates tool descriptions from trusted sources.
- **MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study** — Farooq Shaikh et al., arXiv 2026. [paper](https://arxiv.org/abs/2611.03555) — Measures poisoning across agent frameworks.

## Privacy and data leakage

- **Extracting Training Data from Large Language Models** — Nicholas Carlini et al., USENIX Security 2021. [paper](https://arxiv.org/abs/2012.07805) — Foundational training-data extraction.
- **Quantifying Memorization Across Neural Language Models** — Nicholas Carlini et al., ICLR 2023. [paper](https://arxiv.org/abs/2202.07646) — Memorization scales with size, duplication, context.
- **Scalable Extraction of Training Data from (Production) Language Models** — Milad Nasr et al., arXiv 2023. [paper](https://arxiv.org/abs/2311.17035) — Divergence attack extracts data from ChatGPT.
- **Beyond Memorization: Violating Privacy Via Inference with Large Language Models** — Robin Staab et al., ICLR 2024. [paper](https://arxiv.org/abs/2310.07298) — LLMs infer personal attributes from text.
- **Can LLMs Keep a Secret? Testing Privacy Implications of Language Models via Contextual Integrity Theory (ConfAIde)** — Niloofar Mireshghallah et al., ICLR 2024. [paper](https://arxiv.org/abs/2310.17884) — Contextual-integrity privacy benchmark.
- **PrivacyLens: Evaluating Privacy Norm Awareness of Language Models in Action** — Yijia Shao et al., NeurIPS 2024 (D&B). [paper](https://arxiv.org/abs/2409.00138) · [code](https://github.com/SALT-NLP/PrivacyLens) — Privacy leakage in agent actions.
- **"It's a Fair Game", or Is It? Examining How Users Navigate Disclosure Risks and Benefits When Using LLM-Based Conversational Agents** — Zhiping Zhang et al., CHI 2024. [paper](https://arxiv.org/abs/2309.11653) — User disclosure behavior study.

## Multi-agent risks

- **Multi-Agent Risks from Advanced AI** — Lewis Hammond et al., arXiv 2025. [paper](https://arxiv.org/abs/2502.14143) — Miscoordination, conflict and collusion taxonomy.
- **Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents** — Christian Schroeder de Witt, arXiv 2025. [paper](https://arxiv.org/abs/2505.02077) — Research agenda for multi-agent security.
- **Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems** — Donghyun Lee et al., arXiv 2024. [paper](https://arxiv.org/abs/2410.07283) — Self-replicating injections across agents.
- **Why Do Multi-Agent LLM Systems Fail?** — Mert Cemri et al., arXiv 2025. [paper](https://arxiv.org/abs/2503.13657) — Failure taxonomy (MAST) for multi-agent systems.

## Evaluation methodology

- **The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections** — Milad Nasr et al., arXiv 2025. [paper](https://arxiv.org/abs/2510.09023) — Defenses must be evaluated against adaptive attackers.
- **HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal** — Mantas Mazeika et al., ICML 2024. [paper](https://arxiv.org/abs/2402.04249) · [code](https://github.com/centerforaisafety/HarmBench) — Standardized red-teaming evaluation.
- **JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models** — Patrick Chao et al., NeurIPS 2024 (D&B). [paper](https://arxiv.org/abs/2404.01318) · [code](https://github.com/JailbreakBench/jailbreakbench) — Reproducible jailbreak artifacts and judging.
- **SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents** — Jonathan Kutasov et al., arXiv 2025. [paper](https://arxiv.org/abs/2506.15740) — Agent sabotage and monitor evaluation.
- **DoomArena: A framework for Testing AI Agents Against Evolving Security Threats** — Leo Boisvert et al., arXiv 2025. [paper](https://arxiv.org/abs/2504.14064) · [code](https://github.com/ServiceNow/DoomArena) — Plug-in threat modeling for agent environments.

Missing something? [Open a PR](../CONTRIBUTING.md).
