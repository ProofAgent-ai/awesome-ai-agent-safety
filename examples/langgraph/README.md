# LangGraph: four checkpoints as graph nodes

```
START → input_guard ─(blocked)→ END
             │
           agent ⇄ tools (each tool wrapped: policy + 2a tool-call guard → run → 2b tool-result guard)
             │
        output_guard → END
```

```bash
pip install langgraph langchain-anthropic
export ANTHROPIC_API_KEY=...
python3 examples/langgraph/guarded_graph.py "Summarise https://help.acme.test/returns"
GUARD=proofagent python3 examples/langgraph/guarded_graph.py "Where is order A1234?"
```

- Guards are **nodes and wrappers**, so no prompt can skip them.
- `REVIEW` decisions return a refusal here. In production, use LangGraph's `interrupt()` to pause for a human and resume with `Command(resume=...)`.
- It uses the same tools, policy and guard as [Lab 04](../../labs/04-fully-guarded-agent), so you can compare a real model with the naive one.
- Other wiring patterns (API guard nodes, MCP-in-agent, hybrid) are in the [cookbook's LangGraph recipe](https://github.com/ProofAgent-ai/agent-guardrails-cookbook/tree/main/recipes/langgraph).
