# MCP and tool security

The [Model Context Protocol](https://modelcontextprotocol.io/) lets an agent use tools from any server. That makes tools a **supply chain**. Each server you add can put text into the model's context and receives whatever arguments the model sends it.

## Threats

| Threat | What happens | Control |
|---|---|---|
| **Tool poisoning** | Instructions hidden in a tool's description or schema, read by the model and never seen by the user | Scan definitions before loading them; show users the full description |
| **Rug pull** | The server changes a tool after you approved it | Pin a hash of name, description and schema; re-approve when it changes |
| **Tool shadowing** | One server's description changes how the model uses *another* server's tools | Scan for cross-tool references; isolate servers per task |
| **Result injection** | Tool output carries instructions (indirect prompt injection) | Check every result at checkpoint 2b |
| **Argument exfiltration** | The model is persuaded to put secrets into tool arguments | Strict schemas (`additionalProperties: false`), argument checks at 2a |
| **Confused deputy / token passthrough** | A server uses its own privileges, or your token, for someone else | Follow the [MCP authorization spec](https://modelcontextprotocol.io/specification/draft/basic/authorization); audience-bound tokens and no passthrough |
| **Malicious package** | A look-alike or compromised server package | Allowlist servers, pin versions, verify the publisher |
| **Excess privilege** | A filesystem server with access to `~`, or a database server with write access | Least privilege, sandboxing, read-only by default |

## A minimum checklist

- [ ] Only install servers from an allowlist, pinned to a version.
- [ ] Scan `tools/list` when a server is added and in CI ([examples/mcp](../examples/mcp), [scanners](../resources/mcp-security-tools.md#scanners)).
- [ ] Pin tool definitions, and block or re-approve on change ([Lab 02](../labs/02-mcp-tool-poisoning)).
- [ ] Validate every call against the pinned schema.
- [ ] Require human approval for tools with external side effects.
- [ ] Check every tool result for injected instructions and personal data.
- [ ] Run local servers in a sandbox with an egress allowlist.
- [ ] Use separate credentials per server, short-lived and scoped, kept out of the model context.
- [ ] Log every call with its decision, arguments hash and result.

## Further reading

- [MCP security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [mcp-security-tools.md](../resources/mcp-security-tools.md): scanners, gateways, sandboxes and notable attacks
- [research-papers.md: MCP security](../resources/research-papers.md#mcp-security)
