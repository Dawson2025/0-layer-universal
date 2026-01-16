# Browser Opening Rule

## Rule: Always Use Playwright MCP for Browser Automation

Whenever opening a Chromium or browser instance for automation or interaction, it MUST be done through the Playwright MCP server, NOT by launching standalone chromium processes via the terminal.

### Rationale

- **Interactability**: Playwright-controlled browsers allow full programmatic control (clicking, filling forms, navigating, taking screenshots, etc.)
- **Tab Management**: Can open and manage multiple tabs within a single browser instance
- **Persistent Access**: Browser instances remain accessible and interactable until explicitly closed
- **Integration**: Seamlessly integrates with other MCP tools and automation workflows

### Implementation

Instead of:
```bash
chromium --user-data-dir="/tmp/chromium-instance1" file.html &
```

Use Playwright MCP tools:
- `mcp_playwright_browser_navigate` - Navigate to URLs
- `mcp_playwright_browser_tabs` - Manage tabs (open new tabs, switch between tabs)
- `mcp_playwright_browser_snapshot` - Capture page state
- `mcp_playwright_browser_click` - Click elements
- And other Playwright MCP interaction tools

### Exception

The ONLY time to use standalone chromium processes is when you need a temporary browser window that the user will manually interact with directly (e.g., for them to authenticate or manually browse), and even then, Playwright should be preferred if programmatic interaction will be needed afterward.

