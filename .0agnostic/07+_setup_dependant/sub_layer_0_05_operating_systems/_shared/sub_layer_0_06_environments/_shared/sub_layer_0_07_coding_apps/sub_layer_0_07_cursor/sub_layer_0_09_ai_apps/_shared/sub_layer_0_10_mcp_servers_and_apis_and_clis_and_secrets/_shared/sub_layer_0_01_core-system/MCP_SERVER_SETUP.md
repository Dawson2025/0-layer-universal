---
resource_id: "9f64e948-cf21-47ea-9420-7e05ba98a3c6"
resource_type: "document"
resource_name: "MCP_SERVER_SETUP"
---
# MCP Server Setup Guide

<!-- section_id: "1d86148a-c4f5-46d5-bfeb-b3eea3a3f6ad" -->
## Overview

This project is configured to use the **Playwright MCP Server**, which enables Claude Code to interact with web browsers for testing, automation, and web scraping tasks.

<!-- section_id: "64fa073d-4b56-4d50-8a8c-3f05a0c30fef" -->
## Configuration

The MCP server configuration is stored in [`.mcp.json`](../../.mcp.json) at the project root.

<!-- section_id: "b91e244a-0cfa-422e-84ce-5cb20ba26acf" -->
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

<!-- section_id: "47e9bb08-a199-4964-86aa-38b305e0df5d" -->
## What is Playwright MCP?

The Playwright MCP server provides browser automation capabilities to Claude Code, enabling:

- **Web Testing**: Automated browser testing for the Flask application
- **Web Scraping**: Extracting data from web pages
- **UI Automation**: Simulating user interactions (clicks, form fills, navigation)
- **Accessibility Testing**: Using Playwright's accessibility tree for structured page analysis
- **Multi-Browser Support**: Chrome, Firefox, WebKit (Safari), Edge

<!-- section_id: "9254bdf2-4aea-4e8b-bda7-7237f47b09e4" -->
## How It Works

The MCP server runs locally and communicates with Claude Code through the Model Context Protocol (MCP). When you ask Claude to interact with a web page:

1. Claude Code invokes the Playwright MCP server via `npx`
2. The server launches a browser instance (headless or headed)
3. Claude issues commands through the MCP protocol
4. Playwright executes browser actions and returns results
5. The server automatically cleans up browser instances when done

<!-- section_id: "280117d2-e6dd-4f56-9a91-3c2435b897c9" -->
## Prerequisites

- **Node.js** (v16+) - Already installed: `v22.20.0` ✅
- **npx** - Already installed: `10.9.3` ✅

<!-- section_id: "d60cbabb-b1d9-4c5c-b582-abee922f9756" -->
## Usage in Claude Code

Once configured, you can ask Claude to:

```
"Test the login flow by navigating to localhost:5000/login and entering credentials"

"Take a screenshot of the dashboard page after login"

"Check if the word creation form has proper accessibility labels"

"Scrape the phoneme display table and verify all entries are present"
```

<!-- section_id: "2752f59a-1e21-4253-96c1-e6e14bcf2d11" -->
## Advanced Configuration

<!-- section_id: "9735f98a-be25-4251-9d92-127858312ac8" -->
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

<!-- section_id: "b7dc994b-3751-4267-b4c3-c49f0868a694" -->
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

<!-- section_id: "8478fa18-bcf7-4621-a6cb-070af84c977e" -->
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

<!-- section_id: "d31a24dc-2ba0-4497-9b19-16c44c528c19" -->
## Common Use Cases for This Project

<!-- section_id: "115f55af-1b60-439e-b037-95b8995e1b0e" -->
### 1. Testing User Authentication
```
"Navigate to the login page and verify the registration form is accessible"
```

<!-- section_id: "e0336bee-f59c-4f7a-a7a3-5bb1c19a118b" -->
### 2. Testing Dashboard Navigation
```
"Log in as a test user and verify all project cards are displayed correctly"
```

<!-- section_id: "a9ece53d-7a21-421f-8ae6-32e6bbf2adb9" -->
### 3. Testing Word Creation Flow
```
"Test the word creation workflow: navigate to create word, fill in syllables, verify suggestions appear"
```

<!-- section_id: "316bdfd5-dc23-492c-bfba-8e75a09c0517" -->
### 4. Testing Responsive Design
```
"Test the mobile word creation flow on a 375px viewport"
```

<!-- section_id: "ebd89509-44e5-463c-a95d-83ae4031ecb1" -->
### 5. Accessibility Auditing
```
"Check the phonemes hierarchy view for proper ARIA labels and keyboard navigation"
```

<!-- section_id: "ee1a8ca2-aad3-4ba6-b32e-0b79d9d8c11c" -->
## Troubleshooting

<!-- section_id: "506272f7-344a-48ea-92b8-b5e4d1c7e178" -->
### MCP Server Not Starting
- Verify Node.js is in PATH: `which node`
- Try running manually: `npx @playwright/mcp@latest`
- Check Claude Code logs for error messages

<!-- section_id: "fc3e1256-e5cd-4c29-81fc-0829788c5187" -->
### Browser Not Launching
- Install Playwright browsers: `npx playwright install`
- Check system dependencies: `npx playwright install-deps`

<!-- section_id: "99cccacf-1838-410f-86d4-f5eceef9ff06" -->
### Slow First Run
- First invocation downloads Playwright browsers (~200MB)
- Subsequent runs use cached browsers and are much faster

<!-- section_id: "6243f24f-4a9c-4829-85fe-c2d339557799" -->
## Testing the Configuration

To verify the MCP server is working:

1. Restart Claude Code (if it was running)
2. Ask Claude: "Can you navigate to google.com and tell me the page title?"
3. The MCP server should launch, open a browser, and return results

<!-- section_id: "a3fdf88e-0550-47a7-b244-9e0e1c243df3" -->
## Resources

- **Playwright MCP Server**: https://github.com/microsoft/playwright-mcp
- **Playwright Documentation**: https://playwright.dev/
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Claude Code MCP Guide**: https://docs.claude.com/en/docs/claude-code/mcp

<!-- section_id: "591ec008-1f9c-462d-adc5-cd0c06770f7b" -->
## Related Documentation

- [Claude Code CLI Guide](CLAUDE_CODE_CLI_GUIDE.md)
- [Web App README](WEB_APP_README.md)
- [Testing Documentation](../for_ai/requirements/README.md#-cross-cutting-testing--infrastructure)

---

**Last Updated**: October 16, 2025
**MCP Server Version**: @playwright/mcp@latest (auto-updating)

<!-- section_id: "b4193917-6323-4b13-97ca-382910fcc325" -->
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
