# Agent governance

Guardrails stop attacks. Governance proves to customers, auditors and regulators that the right controls ran on every action, and shows who decided when they didn't.

## What to record for every agent action

| Field | Why |
|---|---|
| Agent, version, model, tool definitions hash | Reproduce what the agent could see and do |
| Checkpoint and decision (allow / mask / review / block) | Show that controls ran |
| Reasons and the policy rule that fired | Explain the decision |
| Arguments hash, not raw values | Prove what ran without storing personal data |
| Approver, time and the exact arguments approved | Make human review accountable |
| Guard latency and errors | Show that failures closed safely |

## Human approval done right

- Bind each approval to a **hash of the exact arguments**. Approving "refund $20" must not approve "refund $2,000".
- Make approvals **single-use** and **time-limited**.
- Only authorised reviewers can approve, never the agent and never the requester.
- Decide per organisation which actions need review (payments, deletions, external messages, permission changes). Don't hard-code it.

## Policy as code

Keep allowlists, approval rules, data classes and confidential terms in version-controlled files such as `tools.json` with risk metadata, or `policy.yaml`. Then:

- changes are reviewed like code,
- tests ([Lab 04](../labs/04-fully-guarded-agent), [Lab 05](../labs/05-agent-red-teaming)) run on every change,
- auditors can read exactly what was enforced on any date.

## Before production

- [ ] Threat model written, mapped to OWASP and ATLAS ([agent-threat-models.md](agent-threat-models.md))
- [ ] All four checkpoints enforced in code, failing closed
- [ ] Red-team results on file: attack-success rate, multi-turn, other languages
- [ ] False-positive rate measured on real benign traffic
- [ ] Human-review flow tested end to end
- [ ] Decision logs retained, with personal data minimised
- [ ] Incident runbook: how to disable a tool or server in minutes
- [ ] Mapped to the frameworks you report against: NIST AI RMF, ISO/IEC 42001, EU AI Act ([standards-and-frameworks.md](../resources/standards-and-frameworks.md))
