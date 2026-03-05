---
resource_id: "67bb014b-d471-4e6e-8d5d-ef4bdb6eddb3"
resource_type: "document"
resource_name: "MCP_SERVER_SETUP"
---
# MCP Server Setup Guide

<!-- section_id: "1764c72b-097a-4daf-ad7b-6be47bcfaea9" -->
## Overview

This project is configured to use the **Playwright MCP Server**, which enables Claude Code to interact with web browsers for testing, automation, and web scraping tasks.

<!-- section_id: "bd632d2c-d556-4918-8f1e-9971bc86665a" -->
## Configuration

The MCP server configuration is stored in [`.mcp.json`](../../.mcp.json) at the project root.

<!-- section_id: "4452880a-b75c-4f6f-beba-42e4de99b16e" -->
### Current Configuration

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "env": {}
    }
  }
}
```

<!-- section_id: "d9523802-f4f4-4c69-acc2-1f98ad054730" -->
## What is Playwright MCP?

The Playwright MCP server provides browser automation capabilities to Claude Code, enabling:

- **Web Testing**: Automated browser testing for the Flask application
- **Web Scraping**: Extracting data from web pages
- **UI Automation**: Simulating user interactions (clicks, form fills, navigation)
- **Accessibility Testing**: Using Playwright's accessibility tree for structured page analysis
- **Multi-Browser Support**: Chrome, Firefox, WebKit (Safari), Edge

<!-- section_id: "d4dd8ffc-ef0f-43e0-a5b1-546025cde4e4" -->
## How It Works

The MCP server runs locally and communicates with Claude Code through the Model Context Protocol (MCP). When you ask Claude to interact with a web page:

1. Claude Code invokes the Playwright MCP server via `npx`
2. The server launches a browser instance (headless or headed)
3. Claude issues commands through the MCP protocol
4. Playwright executes browser actions and returns results
5. The server automatically cleans up browser instances when done

<!-- section_id: "8093877d-e554-40f7-a103-a7423b63cdc8" -->
## Prerequisites

- **Node.js** (v16+) - Already installed: `v22.20.0` ✅
- **npx** - Already installed: `10.9.3` ✅

<!-- section_id: "11cbde19-aa97-433a-983f-650440798a7c" -->
## Usage in Claude Code

Once configured, you can ask Claude to:

```
"Test the login flow by navigating to localhost:5000/login and entering credentials"

"Take a screenshot of the dashboard page after login"

"Check if the word creation form has proper accessibility labels"

"Scrape the phoneme display table and verify all entries are present"
```

<!-- section_id: "a065f5f6-1f78-4277-99fc-7c70040ab210" -->
## Advanced Configuration

<!-- section_id: "2c6f439f-a558-4e45-829f-4a6ae9f68dfb" -->
### Running Headless Mode

To run the browser without a visible UI (faster, good for CI/CD):

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--headless"],
      "env": {}
    }
  }
}
```

<!-- section_id: "92d3a742-f94f-4d5c-a45a-e7c11cd92dc6" -->
### Using Specific Browser

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--browser=firefox"],
      "env": {}
    }
  }
}
```

<!-- section_id: "898fccbf-357c-48dd-80fe-5bc8a6df2c16" -->
### Enabling Additional Capabilities

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest", "--caps=vision,pdf"],
      "env": {}
    }
  }
}
```

**Available capabilities:**
- `vision` - Enable visual/screenshot capabilities
- `pdf` - Enable PDF generation

<!-- section_id: "419a3485-a707-4094-837b-d937cd709cf3" -->
## Common Use Cases for This Project

<!-- section_id: "fdec3dc8-9c93-49db-9d7d-9c6966fe74e3" -->
### 1. Testing User Authentication
```
"Navigate to the login page and verify the registration form is accessible"
```

<!-- section_id: "0f32a28e-aed4-40da-bc77-f9b69e579e66" -->
### 2. Testing Dashboard Navigation
```
"Log in as a test user and verify all project cards are displayed correctly"
```

<!-- section_id: "ba215f0e-340f-45e7-8647-83dafa7bc870" -->
### 3. Testing Word Creation Flow
```
"Test the word creation workflow: navigate to create word, fill in syllables, verify suggestions appear"
```

<!-- section_id: "8b0fb204-4783-4f2f-81fe-2ac5055d364e" -->
### 4. Testing Responsive Design
```
"Test the mobile word creation flow on a 375px viewport"
```

<!-- section_id: "6967a472-dc35-405e-9f5f-dd3b8e352432" -->
### 5. Accessibility Auditing
```
"Check the phonemes hierarchy view for proper ARIA labels and keyboard navigation"
```

<!-- section_id: "0849cdc7-0f69-4924-8b13-017c82181305" -->
## Troubleshooting

<!-- section_id: "a64d5e88-a126-4a95-90bf-f313b0c0a697" -->
### MCP Server Not Starting
- Verify Node.js is in PATH: `which node`
- Try running manually: `npx @playwright/mcp@latest`
- Check Claude Code logs for error messages

<!-- section_id: "8676cb1f-6615-45bf-81d2-968f072613f6" -->
### Browser Not Launching
- Install Playwright browsers: `npx playwright install`
- Check system dependencies: `npx playwright install-deps`

<!-- section_id: "5615ac4c-589e-4728-a2c0-26dbcfe0d83c" -->
### Slow First Run
- First invocation downloads Playwright browsers (~200MB)
- Subsequent runs use cached browsers and are much faster

<!-- section_id: "1731fa84-ad07-4145-9793-535f0df3158a" -->
## Testing the Configuration

To verify the MCP server is working:

1. Restart Claude Code (if it was running)
2. Ask Claude: "Can you navigate to google.com and tell me the page title?"
3. The MCP server should launch, open a browser, and return results

<!-- section_id: "b9d77492-ca15-42e3-a885-80f2e00b33b0" -->
## Resources

- **Playwright MCP Server**: https://github.com/microsoft/playwright-mcp
- **Playwright Documentation**: https://playwright.dev/
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Claude Code MCP Guide**: https://docs.claude.com/en/docs/claude-code/mcp

<!-- section_id: "55a81113-6b07-4c28-b2e3-e31ccf2f6751" -->
## Related Documentation

- [Claude Code CLI Guide](CLAUDE_CODE_CLI_GUIDE.md)
- [Web App README](WEB_APP_README.md)
- [Testing Documentation](../for_ai/requirements/README.md#-cross-cutting-testing--infrastructure)

---

**Last Updated**: October 16, 2025
**MCP Server Version**: @playwright/mcp@latest (auto-updating)

<!-- section_id: "5e28f844-0dbc-4616-82a0-d8a404152ae9" -->
## Starting the MCP server locally

This repository includes helper scripts and npm scripts to start the Playwright MCP server locally.

Shell helper:

```bash
bash scripts/mcp-start.sh           # headless on port 9234
bash scripts/mcp-start.sh --headed  # headed browser
bash scripts/mcp-start.sh --port 9235
```

npm scripts:

```bash
npm run mcp:playwright       # start headless on port 9234 (uses PLAYWRIGHT_BROWSERS_PATH=0)
npm run mcp:playwright:headed
```

The helper sets PLAYWRIGHT_BROWSERS_PATH=0 to avoid downloading browsers into your user cache.
