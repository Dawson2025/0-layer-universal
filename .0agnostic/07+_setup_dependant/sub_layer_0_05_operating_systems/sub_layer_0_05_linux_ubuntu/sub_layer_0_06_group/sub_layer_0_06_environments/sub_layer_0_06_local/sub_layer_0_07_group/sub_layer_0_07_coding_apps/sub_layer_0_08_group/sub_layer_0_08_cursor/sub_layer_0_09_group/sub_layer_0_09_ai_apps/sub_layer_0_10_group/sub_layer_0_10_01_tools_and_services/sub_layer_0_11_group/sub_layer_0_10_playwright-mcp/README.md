---
resource_id: "5f1c2e26-7610-4aad-b067-41e536ce358d"
resource_type: "readme
document"
resource_name: "README"
---
# Playwright MCP - Browser Automation for AI Agents

<!-- section_id: "5c4abf83-9801-404a-b851-d9432abf5d18" -->
## Overview

Playwright MCP (Model Context Protocol) enables AI agents to control web browsers programmatically. It provides a standardized interface for browser automation tasks including navigation, form filling, screenshot capture, and web scraping.

**Environment**: Linux/Ubuntu + Claude Code CLI (local Cursor setup)

<!-- section_id: "7a90acef-a57f-4da3-ac20-642200ba786b" -->
## Features

- **Full Browser Control**: Navigate, click, type, scroll, and interact with any web page
- **Screenshot Capture**: Take full-page or element-specific screenshots
- **Accessibility Snapshots**: Get structured page content for AI understanding
- **Form Automation**: Fill forms, select options, and submit data
- **Multi-Tab Support**: Create, switch between, and manage browser tabs
- **Network Monitoring**: Inspect requests, responses, and console messages
- **Concurrent Browser Support**: Run multiple browser instances across different AI tools

<!-- section_id: "82b6404a-9f1b-4c78-8043-18e7bd04973b" -->
## Quick Start

<!-- section_id: "fda71554-48d3-43e4-a42a-c664774e4c80" -->
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

<!-- section_id: "76909170-da00-4681-88ba-2c9bbd9eb4f8" -->
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

<!-- section_id: "5fc1e800-e7d8-4599-a5a0-7d85d6dc2986" -->
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

<!-- section_id: "30c10ad8-f4bf-456b-8278-c9bdc13f87f8" -->
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
├── 0.12_universal_tools/         # Shared tool configurations
├── 0.13_protocols/               # Workflow documentation
│   ├── github_browser_automation.md  # GitHub automation protocol
│   ├── web_scraping_workflow.md      # Web scraping workflow
│   ├── form_filling_workflow.md      # Form automation workflow
│   └── screenshot_capture_workflow.md # Screenshot workflow
└── 0.14_agent_setup/             # Agent-specific configurations
```

<!-- section_id: "d50b05c6-c7d4-44cf-8f5c-49a59ac456b1" -->
## Configuration

<!-- section_id: "8d53cc98-9170-454a-9759-a50bd11285dd" -->
### Claude Code CLI

Playwright MCP is typically auto-configured. To verify or manually configure:

```bash
# Check current MCP configuration
claude mcp list

# Add Playwright MCP if not present
claude mcp add playwright -- npx -y @playwright/mcp@latest
```

<!-- section_id: "d3ba0ffa-0444-4cf7-9e14-dd9c897f8643" -->
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

<!-- section_id: "8686b336-e4de-4f17-b2d7-e9c7ea22b809" -->
## Documentation

- **[Setup Guide](./setup/README.md)**: Detailed MCP server automation system
- **[Troubleshooting](./setup/TROUBLESHOOTING.md)**: Common issues and solutions
- **[Concurrent Browser Setup](./setup/CONCURRENT_BROWSER_SETUP.md)**: Run browsers across multiple AI tools

<!-- section_id: "3a22f1f3-2a88-4884-9976-4dac8574ea9e" -->
### Workflow Protocols

- **[Web Scraping](./0.13_protocols/web_scraping_workflow.md)**: Extract data from websites
- **[Form Filling](./0.13_protocols/form_filling_workflow.md)**: Automate form completion
- **[Screenshot Capture](./0.13_protocols/screenshot_capture_workflow.md)**: Capture and analyze pages
- **[GitHub Automation](./0.13_protocols/github_browser_automation.md)**: GitHub-specific operations

<!-- section_id: "730a7982-9ac7-4829-965d-15b4707c4bd5" -->
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

<!-- section_id: "aa4db44e-5958-4c9d-9f1f-d4ea5df42231" -->
## Related Resources

- [Playwright Documentation](https://playwright.dev/docs/intro)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [@playwright/mcp NPM Package](https://www.npmjs.com/package/@playwright/mcp)

---

**Last Updated**: 2026-01-13
**Platform**: Linux/Ubuntu (local environment)
**AI Tool**: Claude Code CLI via Cursor
