# Playwright MCP - Browser Automation for AI Agents

## Overview

Playwright MCP (Model Context Protocol) enables AI agents to control web browsers programmatically. It provides a standardized interface for browser automation tasks including navigation, form filling, screenshot capture, and web scraping.

**Environment**: Linux/Ubuntu + Claude Code CLI (local Cursor setup)

## Features

- **Full Browser Control**: Navigate, click, type, scroll, and interact with any web page
- **Screenshot Capture**: Take full-page or element-specific screenshots
- **Accessibility Snapshots**: Get structured page content for AI understanding
- **Form Automation**: Fill forms, select options, and submit data
- **Multi-Tab Support**: Create, switch between, and manage browser tabs
- **Network Monitoring**: Inspect requests, responses, and console messages
- **Concurrent Browser Support**: Run multiple browser instances across different AI tools

## Quick Start

### Prerequisites

```bash
# Install Node.js (if not already installed)
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Playwright browsers
npx playwright install chromium

# Verify installation
npx playwright --version
```

### Basic Usage

Once configured in Claude Code CLI, use these MCP tools:

```
# Navigate to a URL
mcp__playwright__browser_navigate(url="https://example.com")

# Take a screenshot
mcp__playwright__browser_take_screenshot()

# Get page accessibility snapshot
mcp__playwright__browser_snapshot()

# Click an element
mcp__playwright__browser_click(element="Submit button", ref="ref_1")

# Type text
mcp__playwright__browser_type(element="Search input", ref="ref_2", text="search query")
```

## Available Tools

| Tool | Description |
|------|-------------|
| `browser_navigate` | Navigate to URL or back/forward in history |
| `browser_snapshot` | Get accessibility tree of current page |
| `browser_take_screenshot` | Capture screenshot of page or element |
| `browser_click` | Click on elements |
| `browser_type` | Type text into input fields |
| `browser_fill_form` | Fill multiple form fields at once |
| `browser_select_option` | Select dropdown options |
| `browser_hover` | Hover over elements |
| `browser_drag` | Drag and drop operations |
| `browser_press_key` | Press keyboard keys |
| `browser_tabs` | Manage browser tabs |
| `browser_console_messages` | Read console output |
| `browser_network_requests` | Monitor network activity |
| `browser_evaluate` | Execute JavaScript on page |
| `browser_wait_for` | Wait for text/element/time |
| `browser_close` | Close browser session |

## Directory Structure

```
playwright-mcp/
├── README.md                     # This file
├── setup/
│   ├── README.md                 # MCP server automation system docs
│   ├── TROUBLESHOOTING.md        # Common issues and solutions
│   ├── CONCURRENT_BROWSER_SETUP.md  # Multi-tool browser setup
│   ├── 20251210_MCP_Setup_Fix.md    # Historical fix documentation
│   └── scripts/
│       ├── mcp_manager.py            # Core MCP setup automation
│       ├── mcp_concurrent_browser.py # Concurrent browser config
│       └── codex_mcp_sync.py         # Codex CLI sync utility
├── 0.07_universal_tools/         # Shared tool configurations
├── 0.08_protocols/               # Workflow documentation
│   ├── github_browser_automation.md  # GitHub automation protocol
│   ├── web_scraping_workflow.md      # Web scraping workflow
│   ├── form_filling_workflow.md      # Form automation workflow
│   └── screenshot_capture_workflow.md # Screenshot workflow
└── 0.09_agent_setup/             # Agent-specific configurations
```

## Configuration

### Claude Code CLI

Playwright MCP is typically auto-configured. To verify or manually configure:

```bash
# Check current MCP configuration
claude mcp list

# Add Playwright MCP if not present
claude mcp add playwright -- npx -y @playwright/mcp@latest
```

### Environment Variables

For custom browser paths or headed mode:

```json
{
  "env": {
    "PLAYWRIGHT_BROWSERS_PATH": "/home/user/.cache/ms-playwright",
    "HOME": "/home/user",
    "DISPLAY": ":0"
  }
}
```

## Documentation

- **[Setup Guide](./setup/README.md)**: Detailed MCP server automation system
- **[Troubleshooting](./setup/TROUBLESHOOTING.md)**: Common issues and solutions
- **[Concurrent Browser Setup](./setup/CONCURRENT_BROWSER_SETUP.md)**: Run browsers across multiple AI tools

### Workflow Protocols

- **[Web Scraping](./0.08_protocols/web_scraping_workflow.md)**: Extract data from websites
- **[Form Filling](./0.08_protocols/form_filling_workflow.md)**: Automate form completion
- **[Screenshot Capture](./0.08_protocols/screenshot_capture_workflow.md)**: Capture and analyze pages
- **[GitHub Automation](./0.08_protocols/github_browser_automation.md)**: GitHub-specific operations

## Headed vs Headless Mode

- **Headed** (default): Opens visible browser window, useful for debugging
- **Headless**: No visible window, better for automation scripts

```bash
# Force headless mode
npx -y @playwright/mcp@latest --headless
```

**Note**: On WSLg, headed Chromium requires Wayland/Ozone flags:
```json
{
  "launchOptions": {
    "args": ["--ozone-platform=wayland", "--enable-features=UseOzonePlatform"]
  }
}
```

## Related Resources

- [Playwright Documentation](https://playwright.dev/docs/intro)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [@playwright/mcp NPM Package](https://www.npmjs.com/package/@playwright/mcp)

---

**Last Updated**: 2026-01-13
**Platform**: Linux/Ubuntu (local environment)
**AI Tool**: Claude Code CLI via Cursor
