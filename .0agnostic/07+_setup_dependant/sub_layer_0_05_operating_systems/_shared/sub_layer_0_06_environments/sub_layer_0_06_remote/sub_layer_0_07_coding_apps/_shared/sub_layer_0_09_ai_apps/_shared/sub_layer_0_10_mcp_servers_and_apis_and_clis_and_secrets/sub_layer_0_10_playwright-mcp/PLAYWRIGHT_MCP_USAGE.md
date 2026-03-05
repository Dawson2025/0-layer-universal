---
resource_id: "11b08400-9b0b-45d2-8472-07b3d8d7eb30"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_USAGE"
---
# Playwright MCP Server Usage Guide

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working

This guide explains how to start, use, and manage the Playwright MCP server with AI applications (Cursor IDE, Claude Code, etc.).

<!-- section_id: "1e5ba21b-5dce-4e50-bbaa-22c1fcfd2f85" -->
## How the MCP Server Works

The Playwright MCP server is **automatically started by the AI application** when you launch it. There is no manual startup process required.

<!-- section_id: "e52c32f0-5926-40ee-9382-721493c27fff" -->
### Automatic Startup Process

1. AI application reads MCP configuration on startup
   - **Cursor IDE**: `~/.config/mcp/mcp.json` (or `~/.cursor/mcp.json`)
   - **Claude Code**: `.mcp.json` in project root
2. For each MCP server configured, the AI application executes the specified command
3. The MCP server starts in the background and connects to the AI application
4. MCP tools become available for use in the conversation

<!-- section_id: "b626967b-6638-4953-bfc9-98d7f3b1e25e" -->
### Server Lifecycle

- **Starts:** When the AI application launches
- **Runs:** Continuously in the background during your session
- **Stops:** When the AI application closes

<!-- section_id: "0334acfc-49fc-4788-925b-6e2da293bd12" -->
## Starting the MCP Server

<!-- section_id: "c40eb6bf-0e87-4c83-8a0c-dd660b2bce8d" -->
### First Time Setup

1. Ensure you've completed the setup process (see `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for Cursor IDE)
2. Verify MCP configuration exists with valid configuration
3. Launch the AI application

The server will start automatically.

<!-- section_id: "64f33abd-daf5-401d-9c67-23ce1503ad9e" -->
### After Configuration Changes

If you modify the MCP configuration:

1. Save the file
2. **Completely close the AI application** (not just the window, ensure the process is terminated)
3. Restart the AI application
4. The MCP server will start with the new configuration

<!-- section_id: "50fd4415-d44d-4f5f-9bd5-6e20020062dc" -->
## Verifying the Server is Running

<!-- section_id: "d65bea5f-13cc-4b94-9940-0bf55fb970ea" -->
### Check 1: MCP Tools Available

In an AI application conversation, MCP tools will be available if the server is running. Tool naming varies by application:

- **Cursor IDE**: Tools may be available as `mcp_browser_*` or through Playwright MCP
- **Claude Code**: Tools start with `mcp__playwright__` (double underscore)

Common tools:
- `browser_navigate` - Navigate to a URL
- `browser_snapshot` - Get accessibility snapshot
- `browser_click` - Click on elements
- `browser_type` - Type text into inputs
- And many more...

<!-- section_id: "c11ea889-e466-4ea3-b78d-323345cae564" -->
### Check 2: Test Navigation

Ask the AI to navigate to a website:

```
Please navigate to https://example.com
```

If the server is working, the AI will successfully navigate and show you the page snapshot.

<!-- section_id: "8aa2c49a-611d-4017-beb6-7381698357f4" -->
### Check 3: Manual Server Test

You can manually test if the MCP server starts correctly:

```bash
# Load nvm if needed
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Test the server
npx -y @playwright/mcp@latest --browser chromium
```

This should start the server without errors. Press Ctrl+C to stop.

<!-- section_id: "e1a60d94-03ef-45f9-b7d3-94d410fdda58" -->
### Check 4: Verify in Application Settings

**Cursor IDE**:
- Go to Settings → Tools & MCP → Installed MCP Servers
- Should show "playwright" with "22 tools enabled"

**Claude Code**:
- Check application logs for MCP server startup messages
- Verify tools are available in conversation

<!-- section_id: "1e68a099-0dfc-4f21-82e5-c4dffaaed02d" -->
## Available Playwright Tools

Once the MCP server is running, the AI application has access to these tools:

<!-- section_id: "682b91a2-e0d2-4d9f-8052-a67a29006c65" -->
### Navigation
- `browser_navigate` - Navigate to a URL
- `browser_navigate_back` - Go back to previous page
- `browser_tabs` - List, create, close, or select tabs

<!-- section_id: "223042e8-c2bd-4f36-9146-0a915879a050" -->
### Page Interaction
- `browser_click` - Click on elements
- `browser_type` - Type text into inputs
- `browser_press_key` - Press keyboard keys
- `browser_hover` - Hover over elements
- `browser_drag` - Drag and drop elements

<!-- section_id: "a37f3524-777b-4611-9e4e-49c4355f5b96" -->
### Forms
- `browser_fill_form` - Fill multiple form fields at once
- `browser_select_option` - Select dropdown options
- `browser_file_upload` - Upload files

<!-- section_id: "9ff9f021-5c94-44fc-acee-4028b697b1e0" -->
### Information Gathering
- `browser_snapshot` - Get accessibility snapshot of the page
- `browser_take_screenshot` - Capture screenshots
- `browser_console_messages` - View console logs
- `browser_network_requests` - View network requests
- `browser_evaluate` - Execute JavaScript

<!-- section_id: "195e12dd-46aa-408c-af2d-47ff520dbbe1" -->
### Waiting & Dialogs
- `browser_wait_for` - Wait for text to appear/disappear or time to pass
- `browser_handle_dialog` - Handle alert/confirm/prompt dialogs

<!-- section_id: "5e57cdff-62a9-4b28-91f6-677fd56cbd31" -->
### Browser Management
- `browser_close` - Close the browser
- `browser_resize` - Resize browser window
- `browser_install` - Install browser (if not already installed)

<!-- section_id: "7965cfec-6102-4021-bb3b-e3a648f4ddef" -->
## Common Usage Patterns

<!-- section_id: "b93fde8f-8a3d-42c1-97a7-56563f2d1bbf" -->
### Example 1: Navigate and Extract Information

```
Navigate to https://news.ycombinator.com and tell me the top 3 stories
```

The AI will:
1. Use `browser_navigate` to load the page
2. Use `browser_snapshot` to get the page structure
3. Parse the snapshot and extract the information

<!-- section_id: "7387f4a0-6849-4831-b3b5-73d78429bcb8" -->
### Example 2: Automate Form Filling

```
Go to https://example.com/contact and fill out the contact form with:
- Name: John Doe
- Email: john@example.com
- Message: Hello, this is a test
```

The AI will:
1. Navigate to the page
2. Use `browser_snapshot` to identify form fields
3. Use `browser_fill_form` to fill all fields
4. Optionally submit the form

<!-- section_id: "1a85edde-fa03-47ff-8060-93c48a6690b8" -->
### Example 3: Take Screenshots

```
Navigate to https://example.com and take a screenshot
```

The AI will:
1. Navigate to the page
2. Use `browser_take_screenshot` to capture the page
3. Save the screenshot to a file

<!-- section_id: "6e0ba3b5-e358-43b8-8bd1-9da1f1a7b085" -->
### Example 4: Testing Workflows

```
Test the login flow on https://example.com/login:
1. Enter username: testuser
2. Enter password: testpass123
3. Click the login button
4. Verify we're redirected to the dashboard
```

The AI will:
1. Navigate to the login page
2. Use `browser_type` to enter credentials
3. Use `browser_click` to click the button
4. Use `browser_snapshot` to verify the result

<!-- section_id: "2235fb7a-1c52-4dc0-8508-7df1d48419be" -->
## Troubleshooting

<!-- section_id: "750cf3e7-4091-46a3-85c4-26915367c2e4" -->
### Server Not Starting

**Symptom:** MCP tools are not available, error message about tools not being available

**Solutions:**
1. Verify MCP configuration exists and has valid JSON syntax
2. Check that the configuration matches the format in `PLAYWRIGHT_MCP_CURSOR_SETUP.md`
3. Completely restart the AI application (ensure the process is terminated)
4. Check application logs for MCP server startup errors

<!-- section_id: "5593c585-61d4-4907-a90a-c72f68f8ae6f" -->
### Browser Not Found

**Symptom:** Error: "Chromium distribution 'chrome' is not found" or "Browser specified in your config is not installed"

**Solutions:**
1. Verify browser is installed: `ls -la ~/.cache/ms-playwright/`
2. Reinstall browser: 
   ```bash
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   npx -y playwright@latest install chromium
   ```
3. Check MCP configuration specifies the correct browser with `"--browser", "chromium"`
4. Restart the AI application

<!-- section_id: "cece75ea-7493-486d-8ad8-9f4663a3a776" -->
### Server Crashes or Disconnects

**Solutions:**
1. Check if browser binaries are corrupted
2. Reinstall browser: 
   ```bash
   rm -rf ~/.cache/ms-playwright/
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   npx -y playwright@latest install chromium
   ```
3. Restart the AI application

<!-- section_id: "175b2e57-c96c-4a38-886f-93b5e1968edc" -->
### Performance Issues

If the browser is slow or unresponsive:

1. Close unused browser tabs using the `browser_tabs` tool
2. Close and restart the browser using `browser_close`
3. Consider using headless mode (default) for better performance
4. Check system resources (RAM, CPU)

<!-- section_id: "bc8ebd34-c9fe-44bf-80b0-a6706965f3fc" -->
## Manual Server Invocation (Testing Only)

For debugging purposes, you can manually start the MCP server:

```bash
# Load nvm if needed
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Basic startup
npx -y @playwright/mcp@latest --browser chromium

# With additional options
npx -y @playwright/mcp@latest \
  --browser chromium \
  --allowed-origins "*"
```

**Note:** This is only for testing. The AI application will manage the server automatically during normal use.

<!-- section_id: "9fcd0a2b-f208-46a0-b5c6-6fa34513def7" -->
### Useful Command Options

```bash
# View help
npx -y @playwright/mcp@latest --help

# Use a different browser
npx -y @playwright/mcp@latest --browser firefox

# Enable additional capabilities
npx -y @playwright/mcp@latest --browser chromium --caps vision,pdf

# Block specific origins
npx -y @playwright/mcp@latest --browser chromium --blocked-origins "https://ads.example.com"
```

<!-- section_id: "c2091478-8dbb-47bb-9d9f-f15fd1cd95f6" -->
## Configuration Reference

<!-- section_id: "9bd6bb7a-b034-44c0-bd25-fbf67bdf0be8" -->
### Basic Configuration (Cursor IDE)

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest",
        "--browser",
        "chromium"
      ],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "0"
      }
    }
  }
}
```

**Location**: `~/.config/mcp/mcp.json` (or `~/.cursor/mcp.json`)

<!-- section_id: "817bbea0-5509-4218-979a-5693cc8aff09" -->
### Basic Configuration (Claude Code)

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest",
        "--browser",
        "chromium"
      ]
    }
  }
}
```

**Location**: `.mcp.json` in project root

<!-- section_id: "db3dc9c7-ae34-42a0-af48-384217f4208d" -->
### Advanced Configuration

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@playwright/mcp@latest",
        "--browser",
        "chromium",
        "--allowed-origins",
        "*",
        "--caps",
        "vision"
      ],
      "env": {
        "DEBUG": "pw:api"
      }
    }
  }
}
```

<!-- section_id: "57f19cfb-5bd1-4a5a-ace7-987a1088a982" -->
## Best Practices

1. **Keep it Simple:** Use the basic configuration unless you have specific needs
2. **Use Chromium:** It's the most reliable and well-tested browser option
3. **Restart After Config Changes:** Always restart the AI application after modifying MCP configuration
4. **Close Unused Tabs:** Browser tabs consume memory; close them when done
5. **Check Snapshots First:** Use `browser_snapshot` before taking screenshots (it's faster)
6. **Handle Errors Gracefully:** Be prepared for network issues, timeouts, and page errors

<!-- section_id: "ed23ea30-506a-4df8-86cd-05f0be6abc0e" -->
## Security Considerations

<!-- section_id: "e4298185-9d35-4965-a6f9-669ff013a47b" -->
### Origin Restrictions

By default, the MCP server allows all origins. To restrict access:

```json
"args": [
  "-y",
  "@playwright/mcp@latest",
  "--browser",
  "chromium",
  "--allowed-origins",
  "https://example.com;https://trusted-site.com"
]
```

<!-- section_id: "bf9d3bd4-ad14-4162-9683-de7ee10ed00b" -->
### Blocking Origins

To block specific sites (e.g., ads, trackers):

```json
"args": [
  "-y",
  "@playwright/mcp@latest",
  "--browser",
  "chromium",
  "--blocked-origins",
  "https://ads.example.com;https://tracker.example.com"
]
```

<!-- section_id: "eb3e650f-b724-41b1-9dd3-9a1393939d8c" -->
### Service Workers

To block service workers:

```json
"args": [
  "-y",
  "@playwright/mcp@latest",
  "--browser",
  "chromium",
  "--block-service-workers"
]
```

<!-- section_id: "d3ef5822-0bff-458a-975f-0cd27f853d29" -->
## Getting Help

<!-- section_id: "e73b1137-0e69-4717-a5e0-a66d9f465d1d" -->
### Check Documentation
- Official Playwright Docs: https://playwright.dev/
- MCP Protocol Docs: https://modelcontextprotocol.io/
- [Playwright MCP Cursor Setup](./PLAYWRIGHT_MCP_CURSOR_SETUP.md) - Setup guide for Cursor IDE

<!-- section_id: "c6ea3b85-51b1-4511-967f-65a55f37b187" -->
### Common Issues
- See `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for setup troubleshooting
- Check application logs for error messages
- Verify browser installation: `ls -la ~/.cache/ms-playwright/`

<!-- section_id: "41b5b8df-be84-4580-8b9e-7912f9e44c4a" -->
### Manual Testing
Test if the MCP server can start manually:
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
npx -y @playwright/mcp@latest --browser chromium
```

If this fails, the issue is with the installation, not the AI application.

<!-- section_id: "6c356e43-b3de-4ece-9ead-d291400779ef" -->
## Summary

- **Starting:** Automatic when AI application launches
- **Stopping:** Automatic when AI application closes
- **Restarting:** Close and reopen the AI application
- **Configuration:** Edit MCP config file and restart the AI application
- **Verification:** Ask the AI to navigate to a website
- **Troubleshooting:** Check logs, verify installation, restart the AI application

The Playwright MCP server requires no manual management during normal use. Just launch your AI application and start automating!

---

**Last Updated**: 2025-12-05  
**Status**: ✅ Working

