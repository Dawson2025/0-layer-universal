---
resource_id: "b1b52f5f-f145-4ce8-a83c-49aad3cebd76"
resource_type: "document"
resource_name: "MCP_SERVER_SETUP"
---
# MCP Server Setup Guide

<!-- section_id: "505413a0-bdd6-46f7-be77-8837825ff8bd" -->
## Overview

This project is configured to use the **Playwright MCP Server**, which enables Claude Code to interact with web browsers for testing, automation, and web scraping tasks.

<!-- section_id: "e02b9ba2-09e8-45e1-9e5b-ce616c537be7" -->
## Configuration

The MCP server configuration is stored in [`.mcp.json`](../../.mcp.json) at the project root.

<!-- section_id: "b6101871-0206-4b73-b18d-c4ebc2604640" -->
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

<!-- section_id: "f24e62f5-d6d1-41ba-9ed2-93e1d0d288ee" -->
## What is Playwright MCP?

The Playwright MCP server provides browser automation capabilities to Claude Code, enabling:

- **Web Testing**: Automated browser testing for the Flask application
- **Web Scraping**: Extracting data from web pages
- **UI Automation**: Simulating user interactions (clicks, form fills, navigation)
- **Accessibility Testing**: Using Playwright's accessibility tree for structured page analysis
- **Multi-Browser Support**: Chrome, Firefox, WebKit (Safari), Edge

<!-- section_id: "f92b71b0-89cc-48fd-a947-81393e837f10" -->
## How It Works

The MCP server runs locally and communicates with Claude Code through the Model Context Protocol (MCP). When you ask Claude to interact with a web page:

1. Claude Code invokes the Playwright MCP server via `npx`
2. The server launches a browser instance (headless or headed)
3. Claude issues commands through the MCP protocol
4. Playwright executes browser actions and returns results
5. The server automatically cleans up browser instances when done

<!-- section_id: "7859ec43-a05d-46e1-afc4-d81ad287c0d2" -->
## Prerequisites

- **Node.js** (v16+) - Already installed: `v22.20.0` ✅
- **npx** - Already installed: `10.9.3` ✅

<!-- section_id: "2ccbb4aa-a189-4a23-aed2-746268757f86" -->
## Usage in Claude Code

Once configured, you can ask Claude to:

```
"Test the login flow by navigating to localhost:5000/login and entering credentials"

"Take a screenshot of the dashboard page after login"

"Check if the word creation form has proper accessibility labels"

"Scrape the phoneme display table and verify all entries are present"
```

<!-- section_id: "e6a395e4-dba4-4d0b-8d06-a3c6f2e78909" -->
## Advanced Configuration

<!-- section_id: "68537da5-5ece-469d-928f-0eca8cec3d19" -->
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

<!-- section_id: "778a77c3-98a4-413d-9ce9-b16effe986a4" -->
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

<!-- section_id: "8454ab59-04d1-4b6d-8312-4769bea3a899" -->
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

<!-- section_id: "3000c5f0-bb1e-4de9-bdd3-8d79f39f68fd" -->
## Common Use Cases for This Project

<!-- section_id: "3e866bc1-9fe3-447c-a9c2-75063a03e621" -->
### 1. Testing User Authentication
```
"Navigate to the login page and verify the registration form is accessible"
```

<!-- section_id: "0d08e6c8-2659-42fb-b985-64dafce3e9dc" -->
### 2. Testing Dashboard Navigation
```
"Log in as a test user and verify all project cards are displayed correctly"
```

<!-- section_id: "ce69651f-65f2-40ca-b51a-668bf8c17948" -->
### 3. Testing Word Creation Flow
```
"Test the word creation workflow: navigate to create word, fill in syllables, verify suggestions appear"
```

<!-- section_id: "41333be3-f594-47fa-b4e8-a2e36a210e92" -->
### 4. Testing Responsive Design
```
"Test the mobile word creation flow on a 375px viewport"
```

<!-- section_id: "1dfc091e-18da-4757-a053-9a908657430d" -->
### 5. Accessibility Auditing
```
"Check the phonemes hierarchy view for proper ARIA labels and keyboard navigation"
```

<!-- section_id: "374c2805-b068-4c86-88e0-f72f4a9f7aa7" -->
## Troubleshooting

<!-- section_id: "89b9d7fe-6c5e-4137-b287-89c621bf717a" -->
### MCP Server Not Starting
- Verify Node.js is in PATH: `which node`
- Try running manually: `npx @playwright/mcp@latest`
- Check Claude Code logs for error messages

<!-- section_id: "e8682903-8587-4c2b-b422-b94e22dfb8cd" -->
### Browser Not Launching
- Install Playwright browsers: `npx playwright install`
- Check system dependencies: `npx playwright install-deps`

<!-- section_id: "f71bb045-4bf6-4d30-b260-3ec61e1cbd32" -->
### Slow First Run
- First invocation downloads Playwright browsers (~200MB)
- Subsequent runs use cached browsers and are much faster

<!-- section_id: "983e8208-ee44-4539-9dcf-3037e182f51c" -->
## Testing the Configuration

To verify the MCP server is working:

1. Restart Claude Code (if it was running)
2. Ask Claude: "Can you navigate to google.com and tell me the page title?"
3. The MCP server should launch, open a browser, and return results

<!-- section_id: "a3ef321d-e095-455c-bfb4-1b67ba0afca8" -->
## Resources

- **Playwright MCP Server**: https://github.com/microsoft/playwright-mcp
- **Playwright Documentation**: https://playwright.dev/
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Claude Code MCP Guide**: https://docs.claude.com/en/docs/claude-code/mcp

<!-- section_id: "2d0bb7bb-3217-44cc-b104-b92e5b94897c" -->
## Related Documentation

- [Claude Code CLI Guide](CLAUDE_CODE_CLI_GUIDE.md)
- [Web App README](WEB_APP_README.md)
- [Testing Documentation](../for_ai/requirements/README.md#-cross-cutting-testing--infrastructure)

---

**Last Updated**: October 16, 2025
**MCP Server Version**: @playwright/mcp@latest (auto-updating)

<!-- section_id: "0c78bcdf-b637-4f6a-8b63-0a45a28b5631" -->
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
