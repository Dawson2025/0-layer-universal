---
resource_id: "4cdab211-53ca-4ef8-a424-f8b47cfae290"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_USAGE"
---
# Playwright MCP Server Usage Guide

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working

This guide explains how to start, use, and manage the Playwright MCP server with AI applications (Cursor IDE, Claude Code, etc.).

<!-- section_id: "c32edd9f-c451-45aa-a382-8c27c64b665e" -->
## How the MCP Server Works

The Playwright MCP server is **automatically started by the AI application** when you launch it. There is no manual startup process required.

<!-- section_id: "79f8d58c-ba21-4465-9694-4c57f0fc6ae4" -->
### Automatic Startup Process

1. AI application reads MCP configuration on startup
   - **Cursor IDE**: `~/.config/mcp/mcp.json` (or `~/.cursor/mcp.json`)
   - **Claude Code**: `.mcp.json` in project root
2. For each MCP server configured, the AI application executes the specified command
3. The MCP server starts in the background and connects to the AI application
4. MCP tools become available for use in the conversation

<!-- section_id: "8bd0ecdf-840a-4de2-988c-3cf525f8e71d" -->
### Server Lifecycle

- **Starts:** When the AI application launches
- **Runs:** Continuously in the background during your session
- **Stops:** When the AI application closes

<!-- section_id: "4b1d1e51-c60d-47f5-88e1-9b2acba40a08" -->
## Starting the MCP Server

<!-- section_id: "259cb27f-8068-40f1-83cc-d7fef2f5d9bf" -->
### First Time Setup

1. Ensure you've completed the setup process (see `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for Cursor IDE)
2. Verify MCP configuration exists with valid configuration
3. Launch the AI application

The server will start automatically.

<!-- section_id: "c776ce70-87b0-4a4c-8b18-67718724514d" -->
### After Configuration Changes

If you modify the MCP configuration:

1. Save the file
2. **Completely close the AI application** (not just the window, ensure the process is terminated)
3. Restart the AI application
4. The MCP server will start with the new configuration

<!-- section_id: "8f2b652a-7528-4dbc-8ece-c7c843b5275d" -->
## Verifying the Server is Running

<!-- section_id: "7c8800a6-e5ba-4008-ba97-3e35074d8ed9" -->
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

<!-- section_id: "3eab5fa0-c834-4e8f-a5a0-bc5c6ed0e8a6" -->
### Check 2: Test Navigation

Ask the AI to navigate to a website:

```
Please navigate to https://example.com
```

If the server is working, the AI will successfully navigate and show you the page snapshot.

<!-- section_id: "eb91926f-df37-488f-9bd2-e4a547287d84" -->
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

<!-- section_id: "ced8b508-dc53-4c09-b518-e9dd9d83995c" -->
### Check 4: Verify in Application Settings

**Cursor IDE**:
- Go to Settings → Tools & MCP → Installed MCP Servers
- Should show "playwright" with "22 tools enabled"

**Claude Code**:
- Check application logs for MCP server startup messages
- Verify tools are available in conversation

<!-- section_id: "01f5ee14-b13c-4d36-a8ec-4fe8ac091454" -->
## Available Playwright Tools

Once the MCP server is running, the AI application has access to these tools:

<!-- section_id: "be126cc9-76c8-4a8d-8db1-95116f744a5d" -->
### Navigation
- `browser_navigate` - Navigate to a URL
- `browser_navigate_back` - Go back to previous page
- `browser_tabs` - List, create, close, or select tabs

<!-- section_id: "d59e453f-bc64-4ccf-9548-cfaac0af60f7" -->
### Page Interaction
- `browser_click` - Click on elements
- `browser_type` - Type text into inputs
- `browser_press_key` - Press keyboard keys
- `browser_hover` - Hover over elements
- `browser_drag` - Drag and drop elements

<!-- section_id: "d41e6801-f859-4b67-a563-251678d71d40" -->
### Forms
- `browser_fill_form` - Fill multiple form fields at once
- `browser_select_option` - Select dropdown options
- `browser_file_upload` - Upload files

<!-- section_id: "d20bad35-2e1e-4a5f-9e40-a13e51784544" -->
### Information Gathering
- `browser_snapshot` - Get accessibility snapshot of the page
- `browser_take_screenshot` - Capture screenshots
- `browser_console_messages` - View console logs
- `browser_network_requests` - View network requests
- `browser_evaluate` - Execute JavaScript

<!-- section_id: "19606765-059a-46d7-981b-264942383d67" -->
### Waiting & Dialogs
- `browser_wait_for` - Wait for text to appear/disappear or time to pass
- `browser_handle_dialog` - Handle alert/confirm/prompt dialogs

<!-- section_id: "6ad30c9e-6b38-4988-b493-09fdcf71f078" -->
### Browser Management
- `browser_close` - Close the browser
- `browser_resize` - Resize browser window
- `browser_install` - Install browser (if not already installed)

<!-- section_id: "7ba43b50-11aa-47d4-9197-a6f7f29a1546" -->
## Common Usage Patterns

<!-- section_id: "17065492-b0ee-4c0b-bc9f-262c4cf9e630" -->
### Example 1: Navigate and Extract Information

```
Navigate to https://news.ycombinator.com and tell me the top 3 stories
```

The AI will:
1. Use `browser_navigate` to load the page
2. Use `browser_snapshot` to get the page structure
3. Parse the snapshot and extract the information

<!-- section_id: "1cd6813f-7cad-4f98-9a9e-bc3d86c4a7a5" -->
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

<!-- section_id: "8750e427-3d47-490f-add2-4e270b17cdbd" -->
### Example 3: Take Screenshots

```
Navigate to https://example.com and take a screenshot
```

The AI will:
1. Navigate to the page
2. Use `browser_take_screenshot` to capture the page
3. Save the screenshot to a file

<!-- section_id: "3ae0570d-d3f1-43ea-a8c6-05d5f8b40c7a" -->
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

<!-- section_id: "5dd17377-9670-482f-96e1-589882302f13" -->
## Troubleshooting

<!-- section_id: "9cb299f3-2867-4ee2-929e-012842816de3" -->
### Server Not Starting

**Symptom:** MCP tools are not available, error message about tools not being available

**Solutions:**
1. Verify MCP configuration exists and has valid JSON syntax
2. Check that the configuration matches the format in `PLAYWRIGHT_MCP_CURSOR_SETUP.md`
3. Completely restart the AI application (ensure the process is terminated)
4. Check application logs for MCP server startup errors

<!-- section_id: "d7a9dc12-fdf5-458e-a760-54cdce33cc87" -->
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

<!-- section_id: "483a58fc-4cb0-4728-803b-655cf698d0cd" -->
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

<!-- section_id: "e1902fab-29a1-4a94-9858-5f34a7291940" -->
### Performance Issues

If the browser is slow or unresponsive:

1. Close unused browser tabs using the `browser_tabs` tool
2. Close and restart the browser using `browser_close`
3. Consider using headless mode (default) for better performance
4. Check system resources (RAM, CPU)

<!-- section_id: "2605fee5-fb31-4a42-86bb-0d9b32fc75d2" -->
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

<!-- section_id: "25435bee-35d3-488f-ad4f-fa514ab22129" -->
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

<!-- section_id: "bf24a341-eec1-4806-af71-457b5f778b2b" -->
## Configuration Reference

<!-- section_id: "e3abc2aa-6e4e-434b-ac70-3059eefe4175" -->
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

<!-- section_id: "34f3b172-61be-438c-b784-f6f2a4b98f6b" -->
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

<!-- section_id: "6f877182-e908-4f3b-94e1-fb1e171bd03e" -->
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

<!-- section_id: "ec139179-20df-43b5-8b1b-72a7f1738e09" -->
## Best Practices

1. **Keep it Simple:** Use the basic configuration unless you have specific needs
2. **Use Chromium:** It's the most reliable and well-tested browser option
3. **Restart After Config Changes:** Always restart the AI application after modifying MCP configuration
4. **Close Unused Tabs:** Browser tabs consume memory; close them when done
5. **Check Snapshots First:** Use `browser_snapshot` before taking screenshots (it's faster)
6. **Handle Errors Gracefully:** Be prepared for network issues, timeouts, and page errors

<!-- section_id: "e3628dc5-78e6-40c8-b40b-01665dd277af" -->
## Security Considerations

<!-- section_id: "bb1a41e2-2afb-4232-9db7-b47284aefa77" -->
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

<!-- section_id: "1b30b413-e722-480c-822b-cd1d69ccd0d1" -->
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

<!-- section_id: "613096cf-9175-443b-9312-a11e02d8346a" -->
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

<!-- section_id: "63173b85-9a1e-4458-83fd-85e461904c49" -->
## Getting Help

<!-- section_id: "54c51256-9c2f-4d59-996b-d29586a393cd" -->
### Check Documentation
- Official Playwright Docs: https://playwright.dev/
- MCP Protocol Docs: https://modelcontextprotocol.io/
- [Playwright MCP Cursor Setup](./PLAYWRIGHT_MCP_CURSOR_SETUP.md) - Setup guide for Cursor IDE

<!-- section_id: "f37cafe8-0001-4a1c-b29a-74b12c829f8e" -->
### Common Issues
- See `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for setup troubleshooting
- Check application logs for error messages
- Verify browser installation: `ls -la ~/.cache/ms-playwright/`

<!-- section_id: "89754d43-1867-420a-9b19-89de5a89cc29" -->
### Manual Testing
Test if the MCP server can start manually:
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
npx -y @playwright/mcp@latest --browser chromium
```

If this fails, the issue is with the installation, not the AI application.

<!-- section_id: "a8e0e596-5278-40c9-ab3b-324dd8033a2e" -->
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

