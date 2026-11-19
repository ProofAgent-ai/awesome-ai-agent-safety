# MCP: scan and pin tools before the model sees them

A tool's description goes straight into the model's context, so a malicious or compromised server can attack your agent **without its tools ever being called**. Lab 02 explains the attacks. This script is the reusable part.

```bash
python3 examples/mcp/scan_tools.py examples/mcp/sample_tools.json
python3 examples/mcp/scan_tools.py examples/mcp/sample_tools.json --pin pins.json
python3 examples/mcp/scan_tools.py examples/mcp/sample_tools.json --verify pins.json   # use in CI
```

For production, also look at dedicated scanners and gateways in [`resources/mcp-security-tools.md`](../../resources/mcp-security-tools.md), and follow the [MCP security best practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices).
