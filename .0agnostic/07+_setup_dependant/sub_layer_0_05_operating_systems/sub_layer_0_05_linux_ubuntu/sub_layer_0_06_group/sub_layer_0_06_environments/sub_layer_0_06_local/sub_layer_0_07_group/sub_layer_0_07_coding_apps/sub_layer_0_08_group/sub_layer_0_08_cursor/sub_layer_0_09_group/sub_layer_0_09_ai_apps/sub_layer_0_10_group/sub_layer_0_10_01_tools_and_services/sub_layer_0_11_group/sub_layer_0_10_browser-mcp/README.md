---
resource_id: "e3b3d87d-37ef-40bf-95df-6a8470faf458"
resource_type: "readme_document"
resource_name: "README"
---
# browser-mcp (Claude Code CLI on Linux/Ubuntu)

<!-- section_id: "5ef51986-2265-42e7-890b-63eeff883be3" -->
## Overview

Browser MCP (`@agent-infra/mcp-server-browser`) is a general-purpose browser automation MCP server built on Playwright. It provides Claude Code CLI with the ability to control web browsers, navigate pages, interact with elements, and extract content from websites.

This server uses the same underlying Playwright engine as `playwright-mcp` but exposes a different tool schema that may work better for certain clients or use cases.

<!-- section_id: "d22ee1e3-1b0d-4d34-a0c0-f8fbbe510d6e" -->
## Features

- **Page Navigation**: Navigate to URLs, go back/forward in history
- **Element Interaction**: Click buttons, fill forms, select dropdowns
- **Content Extraction**: Read page content, extract text, take screenshots
- **Tab Management**: Create, switch between, and close browser tabs
- **Form Automation**: Fill and submit forms programmatically
- **JavaScript Execution**: Execute custom JavaScript in page context
- **Console/Network Monitoring**: Access browser console logs and network requests
- **Screenshot Capture**: Take full page or element-specific screenshots

<!-- section_id: "41159cf4-a403-422d-aea8-2b8539973765" -->
## Quick Start

<!-- section_id: "a226ec68-d21d-43af-8b8f-5a4ed081c9af" -->
### Prerequisites

1. **Node.js and npm** installed (v18+ recommended)
2. **Playwright browsers** installed:
   ```bash
   npx playwright install chromium
   ```
3. **Environment variables** configured (see Configuration section)

<!-- section_id: "22053c0b-63e3-4388-88e5-f61c500e191d" -->
### Installation

Browser MCP is typically installed via the MCP manager automation:

```bash
# Navigate to the automation scripts directory
cd /path/to/0.10_mcp_servers_and_apis_and_secrets/browser-mcp/setup/scripts

# Run the MCP manager to set up all servers
python3 mcp_manager.py --scope user
```

<!-- section_id: "d9745e20-fe8a-4b53-a602-22aaffbe816e" -->
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

<!-- section_id: "620b2206-8c0a-4221-9952-8bb9a89c496a" -->
### Verify Installation

After configuring, restart Claude Code CLI and test:
```
Navigate to https://example.com using the browser
```

<!-- section_id: "15d684e3-6d7b-4b8e-9a0d-043912d8387c" -->
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

<!-- section_id: "fb906889-13ae-4613-bcfd-4f7d690b438b" -->
## Configuration

<!-- section_id: "23d344ae-e267-4cc1-9ae8-6bb6bb8a2f34" -->
### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `PLAYWRIGHT_BROWSERS_PATH` | Path to Playwright browser installations | `/home/user/.cache/ms-playwright` |
| `HOME` | User home directory | `/home/user` |
| `DISPLAY` | X11 display (for headed mode) | `:0` |

<!-- section_id: "c74f816a-3fe0-49d6-b80a-c697eaac69b1" -->
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

<!-- section_id: "a64e6630-65ca-4b9d-ae59-01180d6b3951" -->
## Browser MCP vs Playwright MCP: When to Use Which

Both servers use Playwright under the hood, but differ in their tool schemas and use cases.

<!-- section_id: "9ba28642-3fd1-4c82-b934-bc20a7e0148a" -->
### Use Browser MCP When:

- The tool schema works better with your specific AI client
- You need a lighter-weight alternative to Playwright MCP
- Running alongside other Playwright-based tools that need isolation
- The default Playwright MCP has compatibility issues with your setup

<!-- section_id: "f1062687-459e-446d-bcf9-65be056f7482" -->
### Use Playwright MCP When:

- You need the most mature and feature-complete browser automation
- You require advanced Playwright features (custom scripts, complex selectors)
- You need better documentation and community support
- Running complex multi-page workflows

<!-- section_id: "6117e890-9a2f-4f99-87c6-ac2f1ebed7ca" -->
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

<!-- section_id: "015b3a43-6e71-4d5a-8c35-34877c1d4d17" -->
### Routing Recommendation

Per the [Browser MCP Routing Table](../_shared/0.01_core-system/BROWSER_MCP_ROUTING_TABLE.md):

| Environment | Primary | Fallback |
|-------------|---------|----------|
| Linux Desktop | Playwright MCP (headed) | Browser MCP |
| WSL/No GUI | Playwright MCP (headless) | Browser MCP (headless) |
| Remote/SSH | Playwright MCP (headless) | Hosted browser MCP |

<!-- section_id: "a3912c6b-8cd8-483a-88c2-2734927d15c1" -->
## Linux/Ubuntu Specific Notes

<!-- section_id: "6d30709b-a9a3-44fc-a7c0-3ebadcf178e6" -->
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

<!-- section_id: "40873559-5118-4c6c-b001-5e9749546d77" -->
### Permission Issues

If browser fails to launch:
```bash
# Check browser permissions
ls -la ~/.cache/ms-playwright/

# Reinstall if needed
npx playwright install chromium --with-deps
```

<!-- section_id: "3bfde025-b2f2-4003-8901-4a915eb9dbaf" -->
## Related Documentation

- **Setup Automation**: [./setup/README.md](./setup/README.md)
- **Troubleshooting**: [./setup/TROUBLESHOOTING.md](./setup/TROUBLESHOOTING.md)
- **Concurrent Browser Setup**: [./setup/CONCURRENT_BROWSER_SETUP.md](./setup/CONCURRENT_BROWSER_SETUP.md)
- **MCP Server Matrix**: [../_shared/0.01_core-system/MCP_SERVER_MATRIX.md](../_shared/0.01_core-system/MCP_SERVER_MATRIX.md)
- **Browser Routing Table**: [../_shared/0.01_core-system/BROWSER_MCP_ROUTING_TABLE.md](../_shared/0.01_core-system/BROWSER_MCP_ROUTING_TABLE.md)

<!-- section_id: "83a3ef0c-8064-4f99-89f8-7c2c942f2ae7" -->
## Protocols

Workflow documentation for common browser automation tasks:

- [Basic Navigation Workflow](./0.13_protocols/basic_navigation_workflow.md)
- [Multi-Tab Workflow](./0.13_protocols/multi_tab_workflow.md)
- [Data Extraction Workflow](./0.13_protocols/data_extraction_workflow.md)

---

**Last Updated**: 2026-01-13
**Status**: Disabled by default (see MCP_SERVER_MATRIX.md)
**Platform**: Linux/Ubuntu with Claude Code CLI
