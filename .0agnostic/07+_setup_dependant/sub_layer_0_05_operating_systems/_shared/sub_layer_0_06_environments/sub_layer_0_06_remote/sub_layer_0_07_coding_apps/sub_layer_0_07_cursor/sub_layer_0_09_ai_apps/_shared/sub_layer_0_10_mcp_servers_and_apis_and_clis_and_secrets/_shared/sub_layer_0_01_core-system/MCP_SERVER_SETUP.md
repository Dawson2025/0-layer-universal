---
resource_id: "1c3510ce-8927-4de1-8d41-288ecd539e3b"
resource_type: "document"
resource_name: "MCP_SERVER_SETUP"
---
# MCP Server Setup Guide

<!-- section_id: "364e157e-a1ec-4ae5-980c-f3c642df9c8e" -->
## Overview

This project is configured to use the **Playwright MCP Server**, which enables Claude Code to interact with web browsers for testing, automation, and web scraping tasks.

<!-- section_id: "ce7ba714-e479-41cc-98c5-9c9ca4b02614" -->
## Configuration

The MCP server configuration is stored in [`.mcp.json`](../../.mcp.json) at the project root.

<!-- section_id: "c9936509-47f9-47f8-bf44-adf633aa3938" -->
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

<!-- section_id: "ff69575f-b6b2-4d02-b476-d7bb3f94ff96" -->
## What is Playwright MCP?

The Playwright MCP server provides browser automation capabilities to Claude Code, enabling:

- **Web Testing**: Automated browser testing for the Flask application
- **Web Scraping**: Extracting data from web pages
- **UI Automation**: Simulating user interactions (clicks, form fills, navigation)
- **Accessibility Testing**: Using Playwright's accessibility tree for structured page analysis
- **Multi-Browser Support**: Chrome, Firefox, WebKit (Safari), Edge

<!-- section_id: "c2ff7a15-dd84-4fbb-8a21-b1476c35e95a" -->
## How It Works

The MCP server runs locally and communicates with Claude Code through the Model Context Protocol (MCP). When you ask Claude to interact with a web page:

1. Claude Code invokes the Playwright MCP server via `npx`
2. The server launches a browser instance (headless or headed)
3. Claude issues commands through the MCP protocol
4. Playwright executes browser actions and returns results
5. The server automatically cleans up browser instances when done

<!-- section_id: "1266b58f-2593-494f-b51c-d03d04cd20b9" -->
## Prerequisites

- **Node.js** (v16+) - Already installed: `v22.20.0` ✅
- **npx** - Already installed: `10.9.3` ✅

<!-- section_id: "31977635-decd-411d-82c9-ffe57d188970" -->
## Usage in Claude Code

Once configured, you can ask Claude to:

```
"Test the login flow by navigating to localhost:5000/login and entering credentials"

"Take a screenshot of the dashboard page after login"

"Check if the word creation form has proper accessibility labels"

"Scrape the phoneme display table and verify all entries are present"
```

<!-- section_id: "2d98f252-7e1a-42a2-8aa4-8c02607ec428" -->
## Advanced Configuration

<!-- section_id: "129cc6d9-1767-4d4c-beee-7b0d1a089d10" -->
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

<!-- section_id: "34dab895-54b3-458f-a097-70898976eefb" -->
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

<!-- section_id: "a98fefd2-a594-4253-ab8c-1b8a5aac7886" -->
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

<!-- section_id: "572ab4e4-e063-4510-bc9f-540b03bdd199" -->
## Common Use Cases for This Project

<!-- section_id: "78d0bd77-2985-41e5-b185-4d1abf1c732c" -->
### 1. Testing User Authentication
```
"Navigate to the login page and verify the registration form is accessible"
```

<!-- section_id: "a43c165d-7136-4bbf-9dff-f14146e0d6ee" -->
### 2. Testing Dashboard Navigation
```
"Log in as a test user and verify all project cards are displayed correctly"
```

<!-- section_id: "56ea32f9-baee-4267-a570-c0591c3efda6" -->
### 3. Testing Word Creation Flow
```
"Test the word creation workflow: navigate to create word, fill in syllables, verify suggestions appear"
```

<!-- section_id: "2b57dd07-3d56-4f41-87d4-010b952bc986" -->
### 4. Testing Responsive Design
```
"Test the mobile word creation flow on a 375px viewport"
```

<!-- section_id: "30840c67-fec4-473a-b270-391dd4bccc19" -->
### 5. Accessibility Auditing
```
"Check the phonemes hierarchy view for proper ARIA labels and keyboard navigation"
```

<!-- section_id: "3d72273f-62f7-46ab-931e-9100a376e652" -->
## Troubleshooting

<!-- section_id: "706b1c45-0698-40c7-b331-7c3ca01f102d" -->
### MCP Server Not Starting
- Verify Node.js is in PATH: `which node`
- Try running manually: `npx @playwright/mcp@latest`
- Check Claude Code logs for error messages

<!-- section_id: "0280750a-8556-413a-ae47-9913c88ba092" -->
### Browser Not Launching
- Install Playwright browsers: `npx playwright install`
- Check system dependencies: `npx playwright install-deps`

<!-- section_id: "ab82c8e7-3637-4a62-8d40-a8352b89ae7d" -->
### Slow First Run
- First invocation downloads Playwright browsers (~200MB)
- Subsequent runs use cached browsers and are much faster

<!-- section_id: "9b3ca9c8-cea5-48c4-bbe5-244e1cae7896" -->
## Testing the Configuration

To verify the MCP server is working:

1. Restart Claude Code (if it was running)
2. Ask Claude: "Can you navigate to google.com and tell me the page title?"
3. The MCP server should launch, open a browser, and return results

<!-- section_id: "045ff47c-32e2-483c-8109-d02b08e209a4" -->
## Resources

- **Playwright MCP Server**: https://github.com/microsoft/playwright-mcp
- **Playwright Documentation**: https://playwright.dev/
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Claude Code MCP Guide**: https://docs.claude.com/en/docs/claude-code/mcp

<!-- section_id: "7ccfd37c-2734-4dbc-a252-4f5de06fca68" -->
## Related Documentation

- [Claude Code CLI Guide](CLAUDE_CODE_CLI_GUIDE.md)
- [Web App README](WEB_APP_README.md)
- [Testing Documentation](../for_ai/requirements/README.md#-cross-cutting-testing--infrastructure)

---

**Last Updated**: October 16, 2025
**MCP Server Version**: @playwright/mcp@latest (auto-updating)

<!-- section_id: "97693bb2-a9a5-4ae4-96f3-cf381c1ef9c1" -->
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
