# Standards and Frameworks

The standards, threat taxonomies and regulations that matter when you build or secure AI agents, and what each one means in practice.

## Contents

- [Threat taxonomies](#threat-taxonomies)
- [Risk management and governance](#risk-management-and-governance)
- [Regulation and codes of practice](#regulation-and-codes-of-practice)
- [Industry frameworks](#industry-frameworks)
- [Protocol security (MCP)](#protocol-security-mcp)
- [Threat mapping table](#threat-mapping-table)

## Threat taxonomies

### OWASP Top 10 for LLM Applications 2025
- **Link:** https://genai.owasp.org/llm-top-10/
- **Issuer:** OWASP GenAI Security Project

**For agent builders:** This is the baseline list of LLM risks: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption. For agents, LLM01, LLM05 and LLM06 matter most. Treat every model output as untrusted input to your tools, and give the agent only the functions, permissions and autonomy the task needs.

### OWASP Top 10 for Agentic Applications 2026
- **Link:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **Issuer:** OWASP GenAI Security Project, Agentic Security Initiative (released 9 December 2025)

**For agent builders:** This list covers risks that only show up when a model plans, remembers and acts: ASI01 Agent Goal Hijack, ASI02 Tool Misuse and Exploitation, ASI03 Identity and Privilege Abuse, ASI04 Agentic Supply Chain Vulnerabilities, ASI05 Unexpected Code Execution, ASI06 Memory and Context Poisoning, ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents. Use it as the threat-model checklist for any design review of a tool-using or multi-agent system. It builds on the earlier OWASP [Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) guide (February 2025).

### OWASP AI Exchange
- **Link:** https://owaspai.org/
- **Issuer:** OWASP

**For agent builders:** An open, detailed reference of AI threats and controls. It has also fed into the EU AI Act standards work and ISO/IEC 27090. Use it when you need the reasoning behind a control, not just its name, for example input segregation, least model privilege, or oversight of automated actions.

### MITRE ATLAS
- **Link:** https://atlas.mitre.org/
- **Issuer:** MITRE

**For agent builders:** A matrix of adversary tactics and techniques against AI systems, modeled on ATT&CK, with real case studies. It now has agent-specific techniques, such as AML.T0053 AI Agent Tool Invocation, AML.T0080 AI Agent Context Poisoning and AML.T0086 Exfiltration via AI Agent Tool Invocation. Use the IDs to label red-team findings and detections so security teams can line them up with their ATT&CK work.

### NIST AI 100-2 E2025, Adversarial Machine Learning taxonomy
- **Link:** https://csrc.nist.gov/pubs/ai/100/2/e2025/final
- **Issuer:** NIST

**For agent builders:** A shared vocabulary for attacks on predictive and generative AI: evasion, poisoning, privacy attacks, and direct and indirect prompt injection, including attacks on agents. Use its terms in threat models and reports. It is frank about which mitigations are still weak, which helps you avoid overstating a single defense.

## Risk management and governance

### NIST AI Risk Management Framework (AI RMF 1.0) and Generative AI Profile (NIST AI 600-1)
- **Links:** https://www.nist.gov/itl/ai-risk-management-framework and https://doi.org/10.6028/NIST.AI.600-1
- **Issuer:** NIST

**For agent builders:** The RMF organizes AI risk work into Govern, Map, Measure and Manage. The Generative AI Profile (July 2024) lists GenAI-specific risks, such as information security, data privacy and confabulation, with suggested actions. In the US it is the usual reference for showing that agent risks were identified, measured and given an owner.

### ISO/IEC 42001:2023, AI management system
- **Link:** https://www.iso.org/standard/81230.html
- **Issuer:** ISO/IEC JTC 1/SC 42

**For agent builders:** A certifiable management-system standard for AI, similar to ISO 27001 for security. It does not prescribe technical controls. It requires documented policies, risk assessments, impact assessments and lifecycle controls. Enterprise customers increasingly ask for it, so agent logging, approval flows and change control should produce evidence an auditor can use.

### ISO/IEC 23894:2023, AI risk management guidance
- **Link:** https://www.iso.org/standard/77304.html
- **Issuer:** ISO/IEC JTC 1/SC 42

**For agent builders:** Guidance that applies ISO 31000 risk management to AI. Use it with 42001 to structure how agent risks, such as unintended actions or data leakage, are identified, analysed, treated and monitored.

## Regulation and codes of practice

### EU AI Act, Regulation (EU) 2024/1689
- **Link:** https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- **Issuer:** European Union

**For agent builders:** The Act regulates by risk tier and role (provider or deployer). Key dates:

| Date | What applies |
|---|---|
| 1 Aug 2024 | Entry into force |
| 2 Feb 2025 | Prohibited practices and AI literacy duties |
| 2 Aug 2025 | General-purpose AI (GPAI) model obligations and governance. Models already on the market before this date have until 2 Aug 2027. |
| 2 Aug 2026 | Most remaining provisions, including transparency duties (Art. 50) and penalties |
| 2 Dec 2027 | Stand-alone Annex III high-risk systems (moved from 2 Aug 2026 by the Digital Omnibus on AI, Regulation (EU) 2026/1744) |
| 2 Aug 2028 | High-risk AI in products under Annex I (moved from 2 Aug 2027 by the same Omnibus) |

An agent used for a high-risk purpose, such as hiring or credit decisions, takes on risk management, logging, human oversight, accuracy and robustness, and cybersecurity duties (Arts. 9 to 15). Robustness explicitly covers attempts to manipulate the system. Sources for the Omnibus changes: [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/), [European Commission AI Act page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai). Check the Official Journal for the final text.

### UK AI Cyber Security Code of Practice
- **Link:** https://www.gov.uk/government/publications/ai-cyber-security-code-of-practice
- **Issuer:** UK Department for Science, Innovation and Technology (January 2025)

**For agent builders:** A voluntary code of 13 principles across the AI lifecycle. It is the basis for the ETSI TS 104 223 baseline. It is a practical checklist: threat modelling, securing the supply chain, documenting data and prompts, testing, monitoring system behaviour, and communicating with end users.

## Industry frameworks

### CSA AI Controls Matrix (AICM)
- **Link:** https://cloudsecurityalliance.org/artifacts/ai-controls-matrix
- **Issuer:** Cloud Security Alliance

**For agent builders:** A vendor-neutral set of over 240 controls across 18 domains, mapped to ISO 42001, NIST AI RMF and other frameworks. It splits responsibility between model providers, orchestrators and application providers, which helps you work out which agent controls are yours and which belong to your model vendor.

### Google Secure AI Framework (SAIF)
- **Link:** https://saif.google/
- **Issuer:** Google

**For agent builders:** A conceptual framework with a risk map and controls for AI systems. Google's agent guidance adds three principles: agents need well-defined human controllers, their powers must be limited, and their actions and planning must be observable. These translate directly into scoped credentials, action allowlists and audit logs.

### Coalition for Secure AI (CoSAI)
- **Link:** https://www.coalitionforsecureai.org/
- **Issuer:** OASIS Open project (industry coalition)

**For agent builders:** Open-source workstreams on AI supply chain security, preparing defenders, AI risk governance, and secure design patterns for agentic systems, including MCP security guidance. Its outputs work as reference architectures you can adopt directly.

## Protocol security (MCP)

### Model Context Protocol: Security Best Practices and Authorization
- **Links:** https://modelcontextprotocol.io/specification/latest/basic/security_best_practices and https://modelcontextprotocol.io/specification/latest/basic/authorization
- **Issuer:** MCP project (originated at Anthropic)

**For agent builders:** The authorization spec bases remote MCP servers on OAuth 2.1, with protected resource metadata and resource indicators, so tokens are tied to the right server. The best-practices page covers confused-deputy attacks, token passthrough (forbidden), session hijacking, and server-side request forgery (SSRF) during discovery. If you ship or consume MCP servers, these documents are the minimum bar. They do not address tool-description poisoning; you need your own allowlisting and pinning for that.

## Threat mapping table

OWASP IDs: `LLMxx` = LLM Top 10 2025, `ASIxx` = Agentic Top 10 2026. MITRE ATLAS IDs were checked against [atlas-data](https://github.com/mitre-atlas/atlas-data).

| Threat | OWASP ID | MITRE ATLAS technique | Typical control |
|---|---|---|---|
| Direct prompt injection / jailbreak | LLM01, ASI01 | AML.T0051.000 LLM Prompt Injection: Direct; AML.T0054 LLM Jailbreak | Input classifiers, privilege separation, never rely on the system prompt for security |
| Indirect prompt injection (web pages, email, documents, tool output) | LLM01, ASI01 | AML.T0051.001 LLM Prompt Injection: Indirect | Treat retrieved content as data, isolate untrusted context (e.g. dual-LLM or CaMeL patterns), require confirmation for sensitive actions |
| Sensitive information disclosure | LLM02 | AML.T0057 LLM Data Leakage | Data minimisation, PII/secret redaction, per-user access control on retrieval |
| Data exfiltration through tools or rendered output | LLM02, LLM05, ASI02 | AML.T0086 Exfiltration via AI Agent Tool Invocation; AML.T0077 LLM Response Rendering | Egress allowlists, block markdown images/links to unknown domains, break the "lethal trifecta" |
| Excessive agency | LLM06, ASI03 | AML.T0053 AI Agent Tool Invocation | Least privilege, scoped short-lived credentials, human approval for irreversible actions |
| Tool misuse | ASI02 | AML.T0053 AI Agent Tool Invocation | Argument validation, policy engine before execution, rate limits, dry-run modes |
| System prompt leakage | LLM07 | AML.T0056 Extract LLM System Prompt | Keep secrets and authorization logic out of prompts |
| Memory poisoning | ASI06 | AML.T0080.000 AI Agent Context Poisoning: Memory | Provenance on memory writes, user review of stored memories, expiry, isolation per user |
| RAG / vector store poisoning | LLM04, LLM08 | AML.T0070 RAG Poisoning | Source vetting, content signing, access-controlled indexes, retrieval anomaly detection |
| Poisoned tool / MCP server (supply chain) | LLM03, ASI04 | AML.T0011.002 Poisoned AI Agent Tool; AML.T0099 AI Agent Tool Data Poisoning | Pin and review tool descriptions, signed packages, server allowlists |
| Credential theft via agent tools | ASI03 | AML.T0098 AI Agent Tool Credential Harvesting | Secrets vault, no credentials in context, per-tool scoped tokens |
| Agent configuration tampering | ASI01, ASI10 | AML.T0081 Modify AI Agent Configuration | Integrity checks on config/rules files, protect agent settings from agent writes |
| Hallucinated packages ("slopsquatting") | LLM09, ASI04 | AML.T0060 Publish Hallucinated Entities | Dependency allowlists, lockfiles, registry verification |
| Unsafe output handling / code execution | LLM05, ASI05 | AML.T0053 AI Agent Tool Invocation | Sandboxed execution, output encoding, no `eval` of model output |
| Self-replicating prompts across agents | ASI07, ASI08 | AML.T0061 LLM Prompt Self-Replication | Authenticate inter-agent messages, isolate agents, circuit breakers |
| Denial of wallet / runaway loops | LLM10, ASI08 | AML.T0034 Cost Harvesting | Token and step budgets, timeouts, rate limits |

Missing something? [Open a PR](../CONTRIBUTING.md).
