# MCP Security Tools

Scanners, gateways, sandboxes, guidance and attack write-ups for securing Model Context Protocol (MCP) servers and clients.

## Contents

- [Scanners](#scanners)
- [Gateways and proxies](#gateways-and-proxies)
- [Sandboxing](#sandboxing)
- [Auth and guidance](#auth-and-guidance)
- [Notable attacks and write-ups](#notable-attacks-and-write-ups)

## Scanners

- [Agent Scan (formerly mcp-scan)](https://github.com/snyk/agent-scan) — Snyk/Invariant scanner for MCP servers, agents and skills: tool poisoning, rug pulls, toxic flows. `OSS` `Apache-2.0`
- [AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) — Tencent platform that includes MCP server and agent skill scanning. `OSS` `Apache-2.0`
- [Cisco MCP Scanner](https://github.com/cisco-ai-defense/mcp-scanner) — Scans MCP servers with YARA rules, LLM judging and Cisco AI Defense. `OSS` `Apache-2.0`
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — Official developer tool for testing and inspecting MCP servers. `OSS`
- [MCP Security Scanner sample](https://github.com/aws-samples/sample-mcp-security-scanner) — AWS sample MCP server that wraps code security scanners. `OSS` `MIT-0`
- [MCP Server Fuzzer](https://github.com/tavric-labs/mcp-server-fuzzer) — Black-box fuzzing and security assessment of live MCP servers. `OSS` `MIT`
- [MCP-Shield](https://github.com/riseandignite/mcp-shield) — Scans installed MCP servers for tool poisoning, exfiltration and cross-origin attacks. `OSS` `MIT`
- [MCPSafetyScanner](https://github.com/johnhalloran321/mcpSafetyScanner) — Agent-based MCP safety auditing and remediation (from arXiv 2504.03767). `OSS` `MPL-2.0`

## Gateways and proxies

- [agentgateway](https://github.com/agentgateway/agentgateway) — Proxy for agents and MCP servers with authn/authz and observability. `OSS` `Apache-2.0`
- [ContextForge MCP Gateway](https://github.com/IBM/mcp-context-forge) — IBM gateway, registry and proxy for MCP, A2A and REST tools. `OSS` `Apache-2.0`
- [Docker MCP Gateway](https://github.com/docker/mcp-gateway) — Docker CLI plugin that runs MCP servers in containers behind a gateway. `OSS` `MIT`
- [Invariant Gateway](https://github.com/invariantlabs-ai/invariant-gateway) — LLM and MCP proxy for observing agents and enforcing guardrails. `OSS` `Apache-2.0`
- [Lasso MCP Gateway](https://github.com/lasso-security/mcp-gateway) — Plugin-based MCP gateway with security plugins (masking, scanning). `OSS` `MIT`
- [MCP Defender](https://github.com/MCP-Defender/MCP-Defender) — Desktop app that scans and blocks malicious MCP traffic in AI apps. `OSS` `AGPL-3.0`
- [MCP Gateway (Microsoft)](https://github.com/microsoft/mcp-gateway) — Reverse proxy and management layer for MCP servers on Kubernetes. `OSS` `MIT`
- [MCP Guardian](https://github.com/eqtylab/mcp-guardian) — Manage, proxy and approve MCP server traffic. `OSS` `Apache-2.0`
- [ToolHive](https://github.com/stacklok/toolhive) — Runs MCP servers in isolated containers with permission profiles. `OSS` `Apache-2.0`
- [MCP Manager](https://mcpmanager.ai) — Hosted MCP gateway with policies, logging and identity. `Commercial`
- [MintMCP](https://www.mintmcp.com) — Enterprise MCP gateway with auth and audit. `Commercial`

## Sandboxing

- [Anthropic Sandbox Runtime](https://github.com/anthropics/sandbox-runtime) — Lightweight filesystem and network sandbox for processes, usable for MCP servers. `OSS` `Apache-2.0`
- [E2B](https://github.com/e2b-dev/E2B) — Cloud sandboxes for agent code and tool execution. `OSS` `Apache-2.0`
- [Firecracker](https://github.com/firecracker-microvm/firecracker) — MicroVM runtime used to isolate untrusted workloads. `OSS` `Apache-2.0`
- [gVisor](https://github.com/google/gvisor) — Application kernel that sandboxes containers. `OSS` `Apache-2.0`
- [microsandbox](https://github.com/superradcompany/microsandbox) — Local-first microVM runtime for running untrusted code. `OSS` `Apache-2.0`
- [mcp-run-python](https://github.com/pydantic/mcp-run-python) — MCP server running Python in a Pyodide/Deno sandbox. `OSS` `MIT` `Archived`

## Auth and guidance

- [MCP Authorization spec](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization) — OAuth 2.1-based authorization for HTTP MCP transports.
- [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) — Official guidance on confused deputy, token passthrough, session hijacking.
- [MCP Security Checklist](https://github.com/slowmist/MCP-Security-Checklist) — SlowMist checklist for MCP hosts, clients and servers. `MIT`
- [SAF-MCP](https://github.com/secure-agentic-framework/saf-mcp) — ATT&CK-style framework of MCP threat techniques and mitigations.
- [workers-oauth-provider](https://github.com/cloudflare/workers-oauth-provider) — Cloudflare library for adding OAuth to remote MCP servers. `OSS` `MIT`
- [Vulnerable MCP Project](https://vulnerablemcp.info) — Database of MCP vulnerabilities and security issues.

## Notable attacks and write-ups

- [MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) — Invariant Labs: hidden instructions in tool descriptions, plus rug pulls and shadowing. ([PoC code](https://github.com/invariantlabs-ai/mcp-injection-experiments))
- [WhatsApp MCP Exploited](https://invariantlabs.ai/blog/whatsapp-mcp-exploited) — Invariant Labs: a malicious MCP server exfiltrates WhatsApp history via a trusted one.
- [GitHub MCP Exploited](https://invariantlabs.ai/blog/mcp-github-vulnerability) — Invariant Labs: a malicious public issue makes an agent leak private repo data.
- [Toxic Agent Flows](https://invariantlabs.ai/blog/toxic-flows) — Invariant Labs: analyzing dangerous combinations of tools and data across agent flows.
- [Supabase MCP can leak your entire SQL database](https://www.generalanalysis.com/blog/supabase-mcp-blog) — General Analysis: support ticket injection against a service-role MCP agent; [Supabase response](https://supabase.com/blog/defense-in-depth-mcp).
- [Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) — Simon Willison overview of MCP risks.
- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) — Simon Willison: private data, untrusted content and external communication.
- [Poison Everywhere](https://www.cyberark.com/resources/threat-research-blog/poison-everywhere-no-output-from-your-mcp-server-is-safe) — CyberArk: full-schema and tool-output poisoning beyond descriptions.
- [CVE-2025-6514 in mcp-remote](https://jfrog.com/blog/2025-6514-critical-mcp-remote-rce-vulnerability/) — JFrog: OS command injection via malicious OAuth endpoint in mcp-remote.
- [CVE-2025-49596 in MCP Inspector](https://www.oligo.security/blog/critical-rce-vulnerability-in-anthropic-mcp-inspector-cve-2025-49596) — Oligo: browser-reachable RCE in the MCP Inspector proxy.
- [Malicious postmark-mcp package](https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft) — Koi Security: npm MCP server that BCC'd users' emails to an attacker.
- [Hundreds of MCP servers vulnerable to abuse](https://www.backslash.security/blog/hundreds-of-mcp-servers-vulnerable-to-abuse) — Backslash: NeighborJack exposure and command injection in public MCP servers.
- [MCP: Security risks and exploits](https://embracethered.com/blog/posts/2025/model-context-protocol-security-risks-and-exploits/) — Embrace The Red: hidden Unicode instructions and other MCP exploits.
- [MCP tools: attack vectors and defense](https://www.elastic.co/security-labs/mcp-tools-attack-defense-recommendations) — Elastic Security Labs analysis and recommendations.
- [MCP Horror Stories: GitHub prompt injection](https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/) — Docker write-up of the GitHub MCP data heist.
- [MCP Safety Audit (arXiv 2504.03767)](https://arxiv.org/abs/2504.03767) — Paper showing LLMs coerced via MCP into credential theft and remote access.

Missing something? [Open a PR](../CONTRIBUTING.md).
