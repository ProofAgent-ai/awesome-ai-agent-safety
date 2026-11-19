# Framework examples

The labs use a 100-line agent loop so you can see everything. These examples put the same guard calls into real frameworks. For complete, tested recipes (LangGraph, CrewAI, OpenAI Agents SDK, Claude Agent SDK, n8n) with a replay playground, see the **[Agent Guardrails Cookbook](https://github.com/ProofAgent-ai/agent-guardrails-cookbook)**.

| Folder | Framework | Checkpoints |
|---|---|---|
| [langgraph](langgraph) | LangGraph `StateGraph` | input node, wrapped tools (call + result), output node |
| [claude-code](claude-code) | Claude Code / Claude Agent SDK hooks | `UserPromptSubmit`, `PreToolUse`, `PostToolUse` |
| [mcp](mcp) | Any MCP client | scan and pin `tools/list` before the model sees it |
| [n8n](n8n) | n8n workflows | HTTP guard nodes around the AI Agent node |
