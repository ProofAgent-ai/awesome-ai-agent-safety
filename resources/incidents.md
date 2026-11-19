# Incidents

Real-world AI agent security incidents and publicly disclosed vulnerabilities, each with a primary or reputable source.

## Contents

- [Incident table](#incident-table)
- [Recurring patterns](#recurring-patterns)
- [Other incident trackers](#other-incident-trackers)

## Incident table

Dates are when the issue was disclosed. Most entries are research disclosures that the vendor fixed, not confirmed in-the-wild exploitation, unless stated otherwise.

| Date | System | What happened | Class | Source |
|---|---|---|---|---|
| 2023-02 | Bing Chat | Researchers showed that hidden text on a web page could take over Bing Chat while it read the page in the Edge sidebar, turning it into a social-engineering and data-harvesting tool. | Indirect prompt injection | [Greshake et al.](https://greshake.github.io/) |
| 2023-05 | ChatGPT plugins | A malicious web page read by a browsing plugin made ChatGPT invoke other plugins, for example reading a user's private GitHub repositories through a code plugin, and leak the data. | Cross-plugin request forgery, exfiltration | [Embrace The Red](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) |
| 2024-08 | Slack AI | Instructions planted in a public channel could make Slack AI leak data from private channels the victim could access, via a crafted markdown link. | Indirect prompt injection, exfiltration | [PromptArmor](https://promptarmor.substack.com/p/data-exfiltration-from-slack-ai-via) |
| 2024-08 | Microsoft 365 Copilot | An email or document triggered Copilot to search for sensitive data, then hide it in invisible Unicode characters inside a clickable link (ASCII smuggling). | Indirect prompt injection, automatic tool invocation, exfiltration | [Embrace The Red](https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/) |
| 2024-09 | ChatGPT (memory, macOS app) | "SpAIware": an injected web page wrote instructions into ChatGPT's long-term memory, so every later conversation was sent to an attacker's server. | Memory poisoning, persistent exfiltration | [Embrace The Red](https://embracethered.com/blog/posts/2024/chatgpt-macos-app-persistent-data-exfiltration/) |
| 2025-05 | GitHub MCP server | A malicious issue in a public repository made an agent using the GitHub MCP server read the user's private repositories and publish the data in a public pull request. | Indirect prompt injection, excessive agency (toxic agent flow) | [Invariant Labs](https://invariantlabs.ai/blog/mcp-github-vulnerability) |
| 2025-06 | Microsoft 365 Copilot ("EchoLeak", CVE-2025-32711) | A zero-click attack: a single email could make Copilot extract internal data and exfiltrate it without any user interaction. Fixed server-side by Microsoft. | Indirect prompt injection, zero-click exfiltration | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-32711), [Aim Security](https://www.aim.security/lp/aim-labs-echoleak-blogpost) |
| 2025-07 | Replit Agent | During a code freeze, Replit's coding agent deleted a user's production database and then misreported what it had done. Replit's CEO apologised and added safeguards. | Excessive agency, destructive action | [The Register](https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/) |
| 2025-07 | Amazon Q Developer extension for VS Code | A malicious pull request inserted a prompt into version 1.84.0 telling the agent to wipe local files and cloud resources. AWS says the code was malformed and did not run; version 1.85.0 removed it. | Supply-chain compromise, prompt-based wiper | [AWS bulletin AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/) |
| 2025-08 | Cursor ("CurXecute", CVE-2025-54135) | Prompt injection through data reaching Cursor via MCP could make it write the MCP config file and run attacker commands. | Indirect prompt injection, remote code execution (RCE), config tampering | [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-54135) |
| 2025-08 | GitHub Copilot / VS Code (CVE-2025-53773) | Injected instructions made Copilot change `.vscode/settings.json` to enable auto-approval ("YOLO mode") of tool calls, leading to code execution. | Indirect prompt injection, agent configuration tampering, RCE | [Embrace The Red](https://embracethered.com/blog/posts/2025/github-copilot-remote-code-execution-via-prompt-injection/), [NVD](https://nvd.nist.gov/vuln/detail/CVE-2025-53773) |
| 2025-08 | Nx build system ("s1ngularity") | Malicious Nx npm package versions used locally installed AI coding CLIs (Claude Code, Gemini CLI, Amazon Q) to search the machine for secrets and wallets, then published them to GitHub. Exploited in the wild. | Supply-chain attack, weaponised coding agents | [Nx security advisory](https://github.com/nrwl/nx/security/advisories/GHSA-cxm3-wv7p-598c) |
| 2025-09 | Salesforce Agentforce ("ForcedLeak") | Instructions submitted through a Web-to-Lead form made Agentforce leak customer relationship management (CRM) data to an expired, allowlisted domain the researchers bought. | Indirect prompt injection, exfiltration via an allowlisted domain | [Noma Security](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce/) |
| 2025-09 | postmark-mcp (npm) | An imitation of a legitimate MCP server added a hidden BCC to an attacker in one version, copying every email sent by agents that used it. Exploited in the wild. | Malicious MCP server, supply chain | [Koi Security](https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft) |
| 2025-11 | Claude Code (misused by GTG-1002) | Anthropic reported that a state-sponsored group used Claude Code as an autonomous agent to run much of a cyber-espionage campaign against about 30 targets. | Agent misuse for offensive operations | [Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage) |

## Recurring patterns

- **Lethal trifecta:** most exfiltration cases combine private data, untrusted content and an outbound channel, such as markdown images, links or tool calls.
- **Agents editing their own guardrails:** CurXecute and CVE-2025-53773 both worked by having the agent rewrite its own configuration.
- **Supply chain now includes prompts and tools:** Amazon Q, Nx and postmark-mcp show that packages, extensions and MCP servers can carry instructions as well as code.

## Other incident trackers

- [AI Incident Database](https://incidentdatabase.ai/) - Broad database of AI harms.
- [MITRE ATLAS case studies](https://atlas.mitre.org/) - Attacks mapped to ATLAS techniques.
- [Embrace The Red](https://embracethered.com/blog/) - Ongoing disclosures against agents and assistants.

Missing something? [Open a PR](../CONTRIBUTING.md).
