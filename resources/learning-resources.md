# Learning Resources

Courses, essays, blogs, games and books for learning how AI agents get attacked and how to defend them.

## Contents

- [Key essays](#key-essays)
- [Vendor security write-ups](#vendor-security-write-ups)
- [Blogs and research](#blogs-and-research)
- [Courses](#courses)
- [CTFs and games](#ctfs-and-games)
- [Talks](#talks)
- [Newsletters](#newsletters)
- [Books](#books)

## Key essays

- [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) - Simon Willison's 2022 post that named the attack.
- [The Dual LLM pattern for building AI assistants that can resist prompt injection](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/) - Simon Willison, an early design pattern for keeping a privileged model away from untrusted content.
- [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) - Simon Willison: private data, untrusted content and external communication together make data exfiltration possible.
- [Simon Willison's prompt-injection tag](https://simonwillison.net/tags/prompt-injection/) - An ongoing log of new attacks and defenses.
- [Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection](https://arxiv.org/abs/2302.12173) - Greshake et al., 2023. The foundational paper on indirect prompt injection.
- [Design Patterns for Securing LLM Agents against Prompt Injections](https://arxiv.org/abs/2506.08837) - Beurer-Kellner et al., 2025. Six patterns that limit what an injected agent can do.
- [Defeating Prompt Injections by Design (CaMeL)](https://arxiv.org/abs/2503.18813) - Google DeepMind, 2025. Separates control flow from data flow, with capability tracking.

## Vendor security write-ups

- [Mitigating the risk of prompt injections in browser use](https://www.anthropic.com/research/prompt-injection-defenses) - Anthropic on defenses for Claude acting in a browser.
- [Claude Code sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing) - Anthropic engineering on filesystem and network isolation for a coding agent.
- [Understanding prompt injections: a frontier security challenge](https://openai.com/index/prompt-injections/) - OpenAI's overview and approach.
- [Mitigating prompt injection attacks with a layered defense strategy](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html) - Google security blog on Gemini's defenses.
- [Google's approach for secure AI agents](https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) - Google's agent security principles paper.
- [How Microsoft defends against indirect prompt injection attacks](https://www.microsoft.com/en-us/msrc/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks) - Microsoft Security Response Center (MSRC) on spotlighting, Prompt Shields and deterministic blocks.

## Blogs and research

- [Embrace The Red](https://embracethered.com/blog/) - Johann Rehberger's disclosures of exfiltration and injection bugs across ChatGPT, Copilot, Claude, Gemini and coding agents.
- [Invariant Labs: MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) - The tool poisoning attack on MCP.
- [Invariant Labs: GitHub MCP Exploited](https://invariantlabs.ai/blog/mcp-github-vulnerability) - Private repository data leaked through a malicious issue.
- [PromptArmor blog](https://promptarmor.substack.com/) - Disclosures such as the Slack AI exfiltration.
- [Trail of Bits blog, machine learning tag](https://blog.trailofbits.com/categories/machine-learning/) - Audits and research on AI and agent security.
- [NVIDIA AI Red Team blog posts](https://developer.nvidia.com/blog/tag/ai-red-team/) - Practical attacks and mitigations for LLM applications.

## Courses

- [Red Teaming LLM Applications](https://www.deeplearning.ai/short-courses/red-teaming-llm-applications/) - DeepLearning.AI with Giskard, free short course.
- [Microsoft AI Red Teaming 101](https://learn.microsoft.com/en-us/security/ai-red-team/training) - Microsoft AI Red Team training series.
- [PortSwigger Web Security Academy: Web LLM attacks](https://portswigger.net/web-security/llm-attacks) - Free hands-on labs on LLM API abuse and indirect injection.
- [Learn Prompting: Prompt Hacking](https://learnprompting.org/docs/prompt_hacking/introduction) - Free guide to injection, jailbreaking and defenses.

## CTFs and games

- [Gandalf](https://gandalf.lakera.ai/) - Lakera's game: trick the model into revealing a password, level by level.
- [HackAPrompt](https://www.hackaprompt.com/) - Prompt hacking competitions; the 2023 dataset is public.
- [Tensor Trust](https://tensortrust.ai/) - Attack and defend prompt-based "bank accounts" (UC Berkeley).
- [Prompt Airlines](https://promptairlines.com/) - Wiz's CTF: jailbreak an airline customer service bot.
- [Damn Vulnerable LLM Agent](https://github.com/ReversecLabs/damn-vulnerable-llm-agent) - A deliberately vulnerable ReAct agent to practise on.
- [Damn Vulnerable MCP Server](https://github.com/harishsg993010/damn-vulnerable-MCP-server) - MCP security challenges.

## Talks

- [Prompt injection explained, with video, slides, and a transcript](https://simonwillison.net/2023/May/2/prompt-injection-explained/) - Simon Willison, 2023 talk.

## Newsletters

- [Simon Willison's newsletter](https://simonw.substack.com/) - Frequent coverage of prompt injection and agents.
- [tl;dr sec](https://tldrsec.com/) - Weekly security newsletter with a strong AI security section.

## Books

- [The Developer's Playbook for Large Language Model Security](https://www.oreilly.com/library/view/the-developers-playbook/9781098162191/) - Steve Wilson (OWASP LLM Top 10 lead), O'Reilly, 2024.
- [Adversarial AI Attacks, Mitigations, and Defense Strategies](https://www.packtpub.com/en-us/product/adversarial-ai-attacks-mitigations-and-defense-strategies-9781835087985) - John Sotiropoulos, Packt, 2024.

Missing something? [Open a PR](../CONTRIBUTING.md).
