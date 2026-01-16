# browser-mcp (Claude Code CLI on Linux/Ubuntu)

## Overview

Browser MCP (`@agent-infra/mcp-server-browser`) is a general-purpose browser automation MCP server built on Playwright. It provides Claude Code CLI with the ability to control web browsers, navigate pages, interact with elements, and extract content from websites.

This server uses the same underlying Playwright engine as `playwright-mcp` but exposes a different tool schema that may work better for certain clients or use cases.

## Features

- **Page Navigation**: Navigate to URLs, go back/forward in history
- **Element Interaction**: Click buttons, fill forms, select dropdowns
- **Content Extraction**: Read page content, extract text, take screenshots
- **Tab Management**: Create, switch between, and close browser tabs
- **Form Automation**: Fill and submit forms programmatically
- **JavaScript Execution**: Execute custom JavaScript in page context
- **Console/Network Monitoring**: Access browser console logs and network requests
- **Screenshot Capture**: Take full page or element-specific screenshots

## Quick Start

### Prerequisites

1. **Node.js and npm** installed (v18+ recommended)
2. **Playwright browsers** installed:
   ```bash
   npx playwright install chromium
   ```
3. **Environment variables** configured (see Configuration section)

### Installation

Browser MCP is typically installed via the MCP manager automation:

```bash
# Navigate to the automation scripts directory
cd /path/to/0.10_mcp_servers_and_apis_and_secrets/browser-mcp/setup/scripts

# Run the MCP manager to set up all servers
python3 mcp_manager.py --scope user
```

### Manual Configuration

Add to your MCP configuration file (e.g., `~/.config/mcp/mcp.json`):

```json
{
  "mcpServers": {
    "browser": {
      "command": "npx",
      "args": ["-y", "@agent-infra/mcp-server-browser"],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/home/YOUR_USER/.cache/ms-playwright",
        "HOME": "/home/YOUR_USER",
        "DISPLAY": ":0"
      }
    }
  }
}
```

### Verify Installation

After configuring, restart Claude Code CLI and test:
```
Navigate to https://example.com using the browser
```

## Available Tools

| Tool | Description |
|------|-------------|
| `browser_navigate` | Navigate to a URL |
| `browser_click` | Click on an element |
| `browser_type` | Type text into an input field |
| `browser_snapshot` | Get accessibility tree of current page |
| `browser_take_screenshot` | Capture page screenshot |
| `browser_evaluate` | Execute JavaScript on the page |
| `browser_fill_form` | Fill multiple form fields |
| `browser_select_option` | Select dropdown options |
| `browser_press_key` | Press keyboard keys |
| `browser_tabs` | Manage browser tabs |
| `browser_wait_for` | Wait for text/element/time |
| `browser_console_messages` | Get console log messages |
| `browser_network_requests` | Get network request history |

## Configuration

### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `PLAYWRIGHT_BROWSERS_PATH` | Path to Playwright browser installations | `/home/user/.cache/ms-playwright` |
| `HOME` | User home directory | `/home/user` |
| `DISPLAY` | X11 display (for headed mode) | `:0` |

### Headed vs Headless Mode

**Headed mode** (default): Opens a visible browser window
- Requires working display (X11 or Wayland)
- Good for debugging and visual verification
- Allows human intervention when needed

**Headless mode**: Browser runs without visible window
- Works on servers without display
- Faster execution
- Use when visual verification not needed

Configure via Playwright config file:
```json
{
  "browser": {
    "launchOptions": {
      "headless": true
    }
  }
}
```

## Browser MCP vs Playwright MCP: When to Use Which

Both servers use Playwright under the hood, but differ in their tool schemas and use cases.

### Use Browser MCP When:

- The tool schema works better with your specific AI client
- You need a lighter-weight alternative to Playwright MCP
- Running alongside other Playwright-based tools that need isolation
- The default Playwright MCP has compatibility issues with your setup

### Use Playwright MCP When:

- You need the most mature and feature-complete browser automation
- You require advanced Playwright features (custom scripts, complex selectors)
- You need better documentation and community support
- Running complex multi-page workflows

### Comparison Table

| Feature | Browser MCP | Playwright MCP |
|---------|-------------|----------------|
| Underlying Engine | Playwright | Playwright |
| Package | `@agent-infra/mcp-server-browser` | `@playwright/mcp` |
| Tool Schema | Simplified | Full Playwright API |
| Maturity | Newer | More established |
| Documentation | Basic | Comprehensive |
| Default in Routing | Fallback | Primary |
| Config Complexity | Lower | Higher |

### Routing Recommendation

Per the [Browser MCP Routing Table](../_shared/0.01_core-system/BROWSER_MCP_ROUTING_TABLE.md):

| Environment | Primary | Fallback |
|-------------|---------|----------|
| Linux Desktop | Playwright MCP (headed) | Browser MCP |
| WSL/No GUI | Playwright MCP (headless) | Browser MCP (headless) |
| Remote/SSH | Playwright MCP (headless) | Hosted browser MCP |

## Linux/Ubuntu Specific Notes

### Display Configuration

For headed mode on Linux, ensure:

1. **X11/Wayland session** is running
2. **DISPLAY variable** is set correctly:
   ```bash
   echo $DISPLAY  # Should show :0 or :1
   ```
3. **For WSLg**, add Chromium args:
   ```json
   {
     "browser": {
       "launchOptions": {
         "args": [
           "--ozone-platform=wayland",
           "--enable-features=UseOzonePlatform"
         ]
       }
     }
   }
   ```

### Permission Issues

If browser fails to launch:
```bash
# Check browser permissions
ls -la ~/.cache/ms-playwright/

# Reinstall if needed
npx playwright install chromium --with-deps
```

## Related Documentation

- **Setup Automation**: [./setup/README.md](./setup/README.md)
- **Troubleshooting**: [./setup/TROUBLESHOOTING.md](./setup/TROUBLESHOOTING.md)
- **Concurrent Browser Setup**: [./setup/CONCURRENT_BROWSER_SETUP.md](./setup/CONCURRENT_BROWSER_SETUP.md)
- **MCP Server Matrix**: [../_shared/0.01_core-system/MCP_SERVER_MATRIX.md](../_shared/0.01_core-system/MCP_SERVER_MATRIX.md)
- **Browser Routing Table**: [../_shared/0.01_core-system/BROWSER_MCP_ROUTING_TABLE.md](../_shared/0.01_core-system/BROWSER_MCP_ROUTING_TABLE.md)

## Protocols

Workflow documentation for common browser automation tasks:

- [Basic Navigation Workflow](./0.13_protocols/basic_navigation_workflow.md)
- [Multi-Tab Workflow](./0.13_protocols/multi_tab_workflow.md)
- [Data Extraction Workflow](./0.13_protocols/data_extraction_workflow.md)

---

**Last Updated**: 2026-01-13
**Status**: Disabled by default (see MCP_SERVER_MATRIX.md)
**Platform**: Linux/Ubuntu with Claude Code CLI
