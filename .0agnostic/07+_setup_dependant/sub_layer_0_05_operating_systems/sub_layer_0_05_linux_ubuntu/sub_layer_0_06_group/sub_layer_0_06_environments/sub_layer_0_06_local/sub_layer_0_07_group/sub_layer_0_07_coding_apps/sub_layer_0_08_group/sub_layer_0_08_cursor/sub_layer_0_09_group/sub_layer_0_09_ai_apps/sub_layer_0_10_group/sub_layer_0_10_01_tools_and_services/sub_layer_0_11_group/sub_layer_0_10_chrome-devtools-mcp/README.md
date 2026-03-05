---
resource_id: "259e7436-d5dc-4d84-9721-5d1344292375"
resource_type: "readme
document"
resource_name: "README"
---
# Chrome DevTools MCP Server

Chrome DevTools Protocol (CDP) integration for Model Context Protocol (MCP) servers, enabling AI agents to interact with Chrome/Chromium browsers through the DevTools debugging interface.

## Overview

The Chrome DevTools MCP server provides direct access to Chrome's debugging capabilities through the Chrome DevTools Protocol. This enables AI agents to:

- Inspect and manipulate the DOM in real-time
- Monitor network requests and responses
- Capture console logs and JavaScript errors
- Analyze page performance metrics
- Execute JavaScript in page context
- Debug web applications programmatically

## Canonical Documentation

For shared MCP server documentation, see:
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/chrome-devtools-mcp/`

## Features

### Network Inspection
- Capture all HTTP/HTTPS requests and responses
- Inspect request headers, body, and timing
- Monitor WebSocket connections
- Analyze resource loading performance
- Filter requests by URL pattern, method, or type

### DOM Manipulation
- Query elements using CSS selectors or XPath
- Read and modify element attributes and content
- Observe DOM mutations in real-time
- Execute JavaScript in page context
- Capture accessibility tree snapshots

### Console Access
- Capture console.log, console.error, and console.warn messages
- Monitor JavaScript exceptions and errors
- Execute JavaScript expressions and retrieve results
- Access runtime evaluation context

### Performance Analysis
- Capture performance metrics and timings
- Monitor memory usage patterns
- Analyze rendering performance
- Profile JavaScript execution

### Page Control
- Navigate to URLs
- Control page lifecycle (reload, stop)
- Capture screenshots
- Manage browser tabs

## Quick Start

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

### Installation

The chrome-devtools-mcp server is configured through the MCP automation system:

```bash
# Run MCP manager to set up all servers including chrome-devtools
python3 setup/scripts/mcp_manager.py --scope user
```

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

### Verification

1. Start Chrome with remote debugging enabled
2. Restart your AI agent (Claude Code CLI, Cursor, etc.)
3. Verify the MCP server is connected by listing available tools

## Use Cases

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

### Performance Analysis

Analyze page load times and identify bottlenecks:

```
1. Connect to Chrome DevTools
2. Navigate to target page
3. Capture performance metrics
4. Analyze network waterfall
5. Identify slow resources or JavaScript execution
```

### Automated Testing Support

Support automated testing workflows:

```
1. Monitor network requests during test execution
2. Capture JavaScript errors as they occur
3. Verify DOM state after interactions
4. Generate performance reports
```

### API Response Inspection

Debug API integrations by inspecting network traffic:

```
1. Filter network requests by URL pattern
2. Inspect request/response headers and body
3. Analyze response timing
4. Identify failed or slow API calls
```

## Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `--browserUrl` | WebSocket URL for Chrome DevTools | `http://127.0.0.1:9222` |
| `--logFile` | Path to log file for debugging | `/tmp/mcp-chrome.log` |

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

## Linux/Ubuntu Specific Notes

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

### Running Headless

For server environments without display:

```bash
google-chrome \
  --headless \
  --remote-debugging-port=9222 \
  --disable-gpu \
  --no-sandbox
```

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

## Related Documentation

- [Troubleshooting Guide](./setup/TROUBLESHOOTING.md)
- [MCP Server Automation](./setup/README.md)
- [Concurrent Browser Setup](./setup/CONCURRENT_BROWSER_SETUP.md)
- [Protocol Workflows](./0.13_protocols/)

## See Also

- [Chrome DevTools Protocol Documentation](https://chromedevtools.github.io/devtools-protocol/)
- [MCP Server Specification](https://modelcontextprotocol.io/)

---

**Environment**: Linux Ubuntu / Local / Cursor / Claude Code CLI
**Last Updated**: 2025-01-13
