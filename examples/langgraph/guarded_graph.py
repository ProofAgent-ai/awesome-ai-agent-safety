"""A LangGraph agent with the four checkpoints from Lab 04.

    pip install langgraph langchain-anthropic
    export ANTHROPIC_API_KEY=...            # or swap in any chat model
    python3 examples/langgraph/guarded_graph.py "Summarise https://help.acme.test/returns"

Guard calls are plain nodes and a tool wrapper, so the graph, not the model,
decides when to check. Set GUARD=proofagent to use the hosted guard.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Annotated, TypedDict

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "guards"))
from agent import DEMO_TOOLS, demo_policy  # noqa: E402
from guard import Vault, get_guard  # noqa: E402

from langchain_anthropic import ChatAnthropic  # noqa: E402
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage  # noqa: E402
from langchain_core.tools import tool  # noqa: E402
from langgraph.graph import END, START, StateGraph  # noqa: E402
from langgraph.graph.message import add_messages  # noqa: E402

GUARD = get_guard()
POLICY = demo_policy()
VAULT = Vault()
REFUSAL = "Sorry, I can't help with that request."


def check(text, checkpoint):
    try:
        return GUARD.check(text, checkpoint, vault=VAULT)
    except TypeError:
        return GUARD.check(text, checkpoint)


def guarded(fn):
    """Checkpoints 2a and 2b around a tool."""
    def run(**kwargs):
        real = {k: VAULT.restore(v) if isinstance(v, str) else v for k, v in kwargs.items()}
        p = POLICY.check(fn.__name__, real)
        if p.blocked or p.needs_review:          # wire REVIEW to your approval flow (LangGraph interrupt())
            return f"Tool call not executed: {'; '.join(p.reasons)}"
        g = check(json.dumps({"tool": fn.__name__, "args": kwargs}), "tool_call")
        if g.blocked or g.needs_review:
            return "Tool call refused by guardrail."
        r = check(str(fn(**real)), "tool_result")
        return "[withheld by guardrail]" if r.blocked else r.text
    run.__name__, run.__doc__ = fn.__name__, fn.__doc__ or fn.__name__
    return run


@tool
def fetch_url(url: str) -> str:
    """Fetch a help-centre page."""
    return guarded(DEMO_TOOLS["fetch_url"])(url=url)


@tool
def lookup_order(order_id: str) -> str:
    """Look up an order by id, e.g. A1234."""
    return guarded(DEMO_TOOLS["lookup_order"])(order_id=order_id)


@tool
def send_email(to: str, body: str, subject: str = "") -> str:
    """Send an email."""
    return guarded(DEMO_TOOLS["send_email"])(to=to, body=body, subject=subject)


TOOLS = {t.name: t for t in (fetch_url, lookup_order, send_email)}
llm = ChatAnthropic(model="claude-haiku-5-5").bind_tools(list(TOOLS.values()))


class State(TypedDict):
    messages: Annotated[list, add_messages]
    blocked: bool


def input_guard(state):                                   # checkpoint 1
    d = check(state["messages"][-1].content, "input")
    if d.blocked or d.needs_review:
        return {"blocked": True, "messages": [AIMessage(REFUSAL)]}
    return {"blocked": False, "messages": [HumanMessage(d.text, id=state["messages"][-1].id)]}


def agent(state):
    return {"messages": [llm.invoke(state["messages"])]}


def tools(state):
    out = []
    for call in state["messages"][-1].tool_calls:
        out.append(ToolMessage(TOOLS[call["name"]].invoke(call["args"]), tool_call_id=call["id"]))
    return {"messages": out}


def output_guard(state):                                  # checkpoint 3
    d = check(state["messages"][-1].content, "output")
    text = REFUSAL if (d.blocked or d.needs_review) else VAULT.restore(d.text)
    return {"messages": [AIMessage(text, id=state["messages"][-1].id)]}


g = StateGraph(State)
for name, fn in [("input_guard", input_guard), ("agent", agent), ("tools", tools), ("output_guard", output_guard)]:
    g.add_node(name, fn)
g.add_edge(START, "input_guard")
g.add_conditional_edges("input_guard", lambda s: END if s["blocked"] else "agent")
g.add_conditional_edges("agent", lambda s: "tools" if s["messages"][-1].tool_calls else "output_guard")
g.add_edge("tools", "agent")
g.add_edge("output_guard", END)
graph = g.compile()

if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "Summarise https://help.acme.test/returns"
    print(graph.invoke({"messages": [HumanMessage(question)], "blocked": False})["messages"][-1].content)
