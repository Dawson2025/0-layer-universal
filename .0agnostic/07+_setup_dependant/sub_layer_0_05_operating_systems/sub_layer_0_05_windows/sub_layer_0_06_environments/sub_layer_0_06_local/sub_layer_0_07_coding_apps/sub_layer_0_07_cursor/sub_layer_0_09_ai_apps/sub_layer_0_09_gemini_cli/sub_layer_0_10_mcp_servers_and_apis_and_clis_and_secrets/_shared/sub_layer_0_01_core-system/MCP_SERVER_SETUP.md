---
resource_id: "9517aae6-656b-4edf-b66e-d90a1b31fbdc"
resource_type: "document"
resource_name: "MCP_SERVER_SETUP"
---
# MCP Server Setup Guide

<!-- section_id: "4d6455a5-bdd5-4d52-b4ef-ad2b346ff751" -->
## Overview

This project is configured to use the **Playwright MCP Server**, which enables Claude Code to interact with web browsers for testing, automation, and web scraping tasks.

<!-- section_id: "79985499-ae68-4476-84a7-30a184dc9b8a" -->
## Configuration

The MCP server configuration is stored in [`.mcp.json`](../../.mcp.json) at the project root.

<!-- section_id: "86bf2242-bab9-488f-b14a-b89e54352bcb" -->
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

<!-- section_id: "e827b4c9-4127-4310-a234-96654bdfc942" -->
## What is Playwright MCP?

The Playwright MCP server provides browser automation capabilities to Claude Code, enabling:

- **Web Testing**: Automated browser testing for the Flask application
- **Web Scraping**: Extracting data from web pages
- **UI Automation**: Simulating user interactions (clicks, form fills, navigation)
- **Accessibility Testing**: Using Playwright's accessibility tree for structured page analysis
- **Multi-Browser Support**: Chrome, Firefox, WebKit (Safari), Edge

<!-- section_id: "b60f5ea3-c4e2-4ab8-9681-832ffb28f642" -->
## How It Works

The MCP server runs locally and communicates with Claude Code through the Model Context Protocol (MCP). When you ask Claude to interact with a web page:

1. Claude Code invokes the Playwright MCP server via `npx`
2. The server launches a browser instance (headless or headed)
3. Claude issues commands through the MCP protocol
4. Playwright executes browser actions and returns results
5. The server automatically cleans up browser instances when done

<!-- section_id: "101eab49-3282-484a-8f10-b9f8afdb28d9" -->
## Prerequisites

- **Node.js** (v16+) - Already installed: `v22.20.0` ✅
- **npx** - Already installed: `10.9.3` ✅

<!-- section_id: "0a7bdb8b-6e9e-43ac-8b00-02ee6089019e" -->
## Usage in Claude Code

Once configured, you can ask Claude to:

```
"Test the login flow by navigating to localhost:5000/login and entering credentials"

"Take a screenshot of the dashboard page after login"

"Check if the word creation form has proper accessibility labels"

"Scrape the phoneme display table and verify all entries are present"
```

<!-- section_id: "80447e70-1dab-480f-9c1f-89f23cc26332" -->
## Advanced Configuration

<!-- section_id: "af9a710a-bd88-445e-a6cd-75e3966f1bdb" -->
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

<!-- section_id: "47af4049-0535-4a00-9a0a-9b44ffa8ba51" -->
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

<!-- section_id: "ce1c0b90-c031-4694-afba-8b367187dfc0" -->
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

<!-- section_id: "281cfa56-01cd-45ea-ae96-e96f01d13b67" -->
## Common Use Cases for This Project

<!-- section_id: "b736542a-5af5-4c2a-b2f8-f8656bc5ac51" -->
### 1. Testing User Authentication
```
"Navigate to the login page and verify the registration form is accessible"
```

<!-- section_id: "4bb2da25-3604-462e-aced-b51d422be805" -->
### 2. Testing Dashboard Navigation
```
"Log in as a test user and verify all project cards are displayed correctly"
```

<!-- section_id: "15228f9a-3da3-488c-b632-077168c36ac4" -->
### 3. Testing Word Creation Flow
```
"Test the word creation workflow: navigate to create word, fill in syllables, verify suggestions appear"
```

<!-- section_id: "40a99c6e-5609-4053-b308-918ebdb4834d" -->
### 4. Testing Responsive Design
```
"Test the mobile word creation flow on a 375px viewport"
```

<!-- section_id: "afc10e34-a072-4cbc-b45b-b6853743e261" -->
### 5. Accessibility Auditing
```
"Check the phonemes hierarchy view for proper ARIA labels and keyboard navigation"
```

<!-- section_id: "99084222-c1f4-4cf7-a654-86cbd47d0fd5" -->
## Troubleshooting

<!-- section_id: "6b0ebb6c-4da3-45dc-a6d5-43afb02ca553" -->
### MCP Server Not Starting
- Verify Node.js is in PATH: `which node`
- Try running manually: `npx @playwright/mcp@latest`
- Check Claude Code logs for error messages

<!-- section_id: "5b5ecdcf-5fc4-4138-a0b3-af7af7d14815" -->
### Browser Not Launching
- Install Playwright browsers: `npx playwright install`
- Check system dependencies: `npx playwright install-deps`

<!-- section_id: "b22a30d4-67ed-4875-8991-9af4f362ba1b" -->
### Slow First Run
- First invocation downloads Playwright browsers (~200MB)
- Subsequent runs use cached browsers and are much faster

<!-- section_id: "feba2ae4-0f48-4409-a5fd-869b2e588d5a" -->
## Testing the Configuration

To verify the MCP server is working:

1. Restart Claude Code (if it was running)
2. Ask Claude: "Can you navigate to google.com and tell me the page title?"
3. The MCP server should launch, open a browser, and return results

<!-- section_id: "dce6c7a1-2bf3-4f2f-b4e6-7b0a59356a27" -->
## Resources

- **Playwright MCP Server**: https://github.com/microsoft/playwright-mcp
- **Playwright Documentation**: https://playwright.dev/
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Claude Code MCP Guide**: https://docs.claude.com/en/docs/claude-code/mcp

<!-- section_id: "a3a37a6a-9971-4134-8298-976cb7974f22" -->
## Related Documentation

- [Claude Code CLI Guide](CLAUDE_CODE_CLI_GUIDE.md)
- [Web App README](WEB_APP_README.md)
- [Testing Documentation](../for_ai/requirements/README.md#-cross-cutting-testing--infrastructure)

---

**Last Updated**: October 16, 2025
**MCP Server Version**: @playwright/mcp@latest (auto-updating)

<!-- section_id: "e54a718b-e37e-4708-a9a0-104d1956649a" -->
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
