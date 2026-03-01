# MCP Servers (06_mcp_servers)

## What This Contains

Model Context Protocol (MCP) server configurations and connections. MCP servers extend AI tools with access to external services and data.

## Configured MCP Servers

| Server | Purpose | Location | Status |
|--------|---------|----------|--------|
| Canvas | Canvas LMS integration | 06_mcp_servers/canvas/ | Active |
| Perplexity | Web search and reasoning | 06_mcp_servers/perplexity/ | Active |
| Claude in Chrome | Browser automation | 06_mcp_servers/claude_in_chrome/ | Active |
| GitHub | Repository operations | 06_mcp_servers/github/ | Optional |
| Custom Server | Your own MCP server | 06_mcp_servers/custom/ | Optional |

## Example Structure

For Canvas MCP:
```
06_mcp_servers/canvas/
├── configuration.md     # Server connection details
├── authentication.md    # Canvas API token setup
├── tools.md            # Available tools/functions
└── usage_examples.md   # How to use in scripts
```

## MCP Server Health

| Check | What | Where |
|-------|------|-------|
| Connection | Is the server reachable? | configuration.md |
| Authentication | Are credentials valid? | authentication.md |
| Tools Availability | What tools are exposed? | tools.md |
| Performance | Response times acceptable? | usage_examples.md |

## Next Layer

After MCP servers, the next layer is **07_tools_and_apis/** (external tools and API integrations).
