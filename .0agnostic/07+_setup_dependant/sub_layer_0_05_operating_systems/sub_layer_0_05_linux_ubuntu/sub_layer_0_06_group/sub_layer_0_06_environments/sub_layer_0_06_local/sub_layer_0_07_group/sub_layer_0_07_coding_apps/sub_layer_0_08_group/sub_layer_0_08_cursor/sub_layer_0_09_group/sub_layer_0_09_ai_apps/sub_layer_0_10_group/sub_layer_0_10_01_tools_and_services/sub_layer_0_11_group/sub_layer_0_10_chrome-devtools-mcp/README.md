---
resource_id: "259e7436-d5dc-4d84-9721-5d1344292375"
resource_type: "readme_document"
resource_name: "README"
---
# Chrome DevTools MCP Server

Chrome DevTools Protocol (CDP) integration for Model Context Protocol (MCP) servers, enabling AI agents to interact with Chrome/Chromium browsers through the DevTools debugging interface.

<!-- section_id: "9efbd4c5-80db-4482-8d07-211231db2e65" -->
## Overview

The Chrome DevTools MCP server provides direct access to Chrome's debugging capabilities through the Chrome DevTools Protocol. This enables AI agents to:

- Inspect and manipulate the DOM in real-time
- Monitor network requests and responses
- Capture console logs and JavaScript errors
- Analyze page performance metrics
- Execute JavaScript in page context
- Debug web applications programmatically

<!-- section_id: "01b47e93-3023-4b60-8d08-43f164d8bc67" -->
## Canonical Documentation

For shared MCP server documentation, see:
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/chrome-devtools-mcp/`

<!-- section_id: "6355cfa5-b9bf-44f9-9f37-2e1c0a784d47" -->
## Features

<!-- section_id: "97485112-1b65-4470-b5ff-64c8f96f3712" -->
### Network Inspection
- Capture all HTTP/HTTPS requests and responses
- Inspect request headers, body, and timing
- Monitor WebSocket connections
- Analyze resource loading performance
- Filter requests by URL pattern, method, or type

<!-- section_id: "db466d06-f05a-46c2-a39c-726218701626" -->
### DOM Manipulation
- Query elements using CSS selectors or XPath
- Read and modify element attributes and content
- Observe DOM mutations in real-time
- Execute JavaScript in page context
- Capture accessibility tree snapshots

<!-- section_id: "166d92ed-61f7-4cb1-b784-cadb59404368" -->
### Console Access
- Capture console.log, console.error, and console.warn messages
- Monitor JavaScript exceptions and errors
- Execute JavaScript expressions and retrieve results
- Access runtime evaluation context

<!-- section_id: "4f7e1d98-4081-4cd7-9cfd-bba4813b8540" -->
### Performance Analysis
- Capture performance metrics and timings
- Monitor memory usage patterns
- Analyze rendering performance
- Profile JavaScript execution

<!-- section_id: "d3b7b847-6ddb-4e24-a723-4db85f4b7f83" -->
### Page Control
- Navigate to URLs
- Control page lifecycle (reload, stop)
- Capture screenshots
- Manage browser tabs

<!-- section_id: "a743ad8b-afc0-4ef5-9603-d0e08916ec50" -->
## Quick Start

<!-- section_id: "254ad672-1db6-4dd3-99d5-d207dc664d66" -->
### Prerequisites

1. **Chrome/Chromium with Remote Debugging Enabled**
   ```bash
   # Launch Chrome with remote debugging on port 9222
   google-chrome --remote-debugging-port=9222

   # Or for Chromium
   chromium-browser --remote-debugging-port=9222
   ```

2. **Node.js and NPX**
   ```bash
   # Verify npx is available
   which npx
   ```

<!-- section_id: "f9d46d4b-7b35-49b6-9d28-fbff4a1dc72c" -->
### Installation

The chrome-devtools-mcp server is configured through the MCP automation system:

```bash
# Run MCP manager to set up all servers including chrome-devtools
python3 setup/scripts/mcp_manager.py --scope user
```

<!-- section_id: "beaf1f6c-4505-4353-b5a0-18bdf3d433d0" -->
### Manual Configuration

Add to your `~/.config/mcp/mcp.json`:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--browserUrl", "http://127.0.0.1:9222",
        "--logFile", "/tmp/mcp-chrome.log"
      ]
    }
  }
}
```

<!-- section_id: "2815652f-a2f3-470c-ad83-d48fb9ebc085" -->
### Verification

1. Start Chrome with remote debugging enabled
2. Restart your AI agent (Claude Code CLI, Cursor, etc.)
3. Verify the MCP server is connected by listing available tools

<!-- section_id: "59bfa056-9533-4498-a929-544acfe8f744" -->
## Use Cases

<!-- section_id: "2c25af40-db6b-4277-9855-9b8e7a5c7b3d" -->
### Web Application Debugging

Debug JavaScript errors, inspect network requests, and analyze DOM state:

```
1. Launch Chrome with --remote-debugging-port=9222
2. Navigate to your web application
3. Use AI agent to:
   - Capture console errors
   - Inspect network requests failing
   - Query DOM elements for state verification
```

<!-- section_id: "a3e7e6a5-1fd9-4cda-a36a-76df506c50a1" -->
### Performance Analysis

Analyze page load times and identify bottlenecks:

```
1. Connect to Chrome DevTools
2. Navigate to target page
3. Capture performance metrics
4. Analyze network waterfall
5. Identify slow resources or JavaScript execution
```

<!-- section_id: "3845cd1f-1692-4466-b700-4e2bcfb00c5b" -->
### Automated Testing Support

Support automated testing workflows:

```
1. Monitor network requests during test execution
2. Capture JavaScript errors as they occur
3. Verify DOM state after interactions
4. Generate performance reports
```

<!-- section_id: "e7223216-7662-4ad3-b10b-83e856ba5a19" -->
### API Response Inspection

Debug API integrations by inspecting network traffic:

```
1. Filter network requests by URL pattern
2. Inspect request/response headers and body
3. Analyze response timing
4. Identify failed or slow API calls
```

<!-- section_id: "4ef3bf8e-b724-4358-8cea-2b466dd8edd2" -->
## Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `--browserUrl` | WebSocket URL for Chrome DevTools | `http://127.0.0.1:9222` |
| `--logFile` | Path to log file for debugging | `/tmp/mcp-chrome.log` |

<!-- section_id: "439c6830-13dc-4548-8eae-fb549d313429" -->
## Architecture

```
AI Agent (Claude Code CLI)
         |
         v
    MCP Protocol
         |
         v
Chrome DevTools MCP Server
         |
         v
Chrome DevTools Protocol (CDP)
         |
         v
Chrome/Chromium Browser
```

<!-- section_id: "7bb700e3-4165-4aef-a5e2-6e1450a5e5b4" -->
## Linux/Ubuntu Specific Notes

<!-- section_id: "b4eb68c8-ece3-423c-8300-0358a7dd4f09" -->
### Starting Chrome with Remote Debugging

Create a convenience script:

```bash
#!/bin/bash
# ~/bin/chrome-debug.sh
google-chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug-profile \
  "$@"
```

<!-- section_id: "1c064203-aa97-45c4-8a1e-e80a04837506" -->
### Running Headless

For server environments without display:

```bash
google-chrome \
  --headless \
  --remote-debugging-port=9222 \
  --disable-gpu \
  --no-sandbox
```

<!-- section_id: "035f0504-d5ad-4bf5-9e2b-366607983da4" -->
### Systemd Service (Optional)

For persistent Chrome debugging sessions:

```ini
# ~/.config/systemd/user/chrome-debug.service
[Unit]
Description=Chrome with Remote Debugging
After=network.target

[Service]
ExecStart=/usr/bin/google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug
Restart=on-failure

[Install]
WantedBy=default.target
```

<!-- section_id: "33283bf0-db94-4ffc-bedf-4acb53814246" -->
## Related Documentation

- [Troubleshooting Guide](./setup/TROUBLESHOOTING.md)
- [MCP Server Automation](./setup/README.md)
- [Concurrent Browser Setup](./setup/CONCURRENT_BROWSER_SETUP.md)
- [Protocol Workflows](./0.13_protocols/)

<!-- section_id: "8f05c5b7-fd5c-493c-a0ea-338a8757dfd6" -->
## See Also

- [Chrome DevTools Protocol Documentation](https://chromedevtools.github.io/devtools-protocol/)
- [MCP Server Specification](https://modelcontextprotocol.io/)

---

**Environment**: Linux Ubuntu / Local / Cursor / Claude Code CLI
**Last Updated**: 2025-01-13
