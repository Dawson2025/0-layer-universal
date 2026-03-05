---
resource_id: "2165bc5a-0764-4b2e-ba9e-b394e3442ab6"
resource_type: "readme
output"
resource_name: "README"
---
# MCP Servers (06_mcp_servers)

<!-- section_id: "29600861-5579-49e7-addd-805cb5db64a6" -->
## What This Contains

Model Context Protocol (MCP) server configurations and connections. MCP servers extend AI tools with access to external services and data.

<!-- section_id: "576b01b2-034c-43bc-850c-a17cb71dd31d" -->
## Configured MCP Servers

| Server | Purpose | Location | Status |
|--------|---------|----------|--------|
| Canvas | Canvas LMS integration | 06_mcp_servers/canvas/ | Active |
| Perplexity | Web search and reasoning | 06_mcp_servers/perplexity/ | Active |
| Claude in Chrome | Browser automation | 06_mcp_servers/claude_in_chrome/ | Active |
| GitHub | Repository operations | 06_mcp_servers/github/ | Optional |
| Custom Server | Your own MCP server | 06_mcp_servers/custom/ | Optional |

<!-- section_id: "4934ee8a-9201-4c68-83d3-952b4b4cdf0f" -->
## Example Structure

For Canvas MCP:
```
06_mcp_servers/canvas/
├── configuration.md     # Server connection details
├── authentication.md    # Canvas API token setup
├── tools.md            # Available tools/functions
└── usage_examples.md   # How to use in scripts
```

<!-- section_id: "1ef18eb6-47c7-4f4c-9f8d-7eb9a4f742ab" -->
## MCP Server Health

| Check | What | Where |
|-------|------|-------|
| Connection | Is the server reachable? | configuration.md |
| Authentication | Are credentials valid? | authentication.md |
| Tools Availability | What tools are exposed? | tools.md |
| Performance | Response times acceptable? | usage_examples.md |

<!-- section_id: "ca2cf01f-6cd2-4979-92b0-3442b3904cbc" -->
## Next Layer

After MCP servers, the next layer is **07_tools_and_apis/** (external tools and API integrations).
