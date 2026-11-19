# n8n: guard nodes around the AI Agent node

In n8n, add an **HTTP Request** node before the AI Agent (checkpoint 1) and after it (checkpoint 3), and wrap risky tools in a sub-workflow that checks arguments (2a) and results (2b). Route `BLOCK` to a refusal, `REVIEW` to a **Wait** node for human approval, and `ALLOW` / `MASK` onward with the returned text.

Ready-to-import workflows, with a test script, are in the cookbook:

- [`guarded-support-agent.json`](https://github.com/ProofAgent-ai/agent-guardrails-cookbook/blob/main/recipes/n8n/guarded-support-agent.json): input and output guard around an AI Agent
- [`guarded-tool.json`](https://github.com/ProofAgent-ai/agent-guardrails-cookbook/blob/main/recipes/n8n/guarded-tool.json): a tool wrapped with call and result checks
- [Recipe README](https://github.com/ProofAgent-ai/agent-guardrails-cookbook/tree/main/recipes/n8n)

Any HTTP guard works the same way. The request and response shape for ProofAgent is in [`guards/guard.py`](../../guards/guard.py) (`ProofAgentGuard`).
