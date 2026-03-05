---
resource_id: "1bf6e361-efae-477f-b8f4-8961b25e468b"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_USAGE"
---
# Playwright MCP Server Usage Guide

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working

This guide explains how to start, use, and manage the Playwright MCP server with AI applications (Cursor IDE, Claude Code, etc.).

<!-- section_id: "415b9ce9-2882-4d26-8a4b-a09d8a3f52b5" -->
## How the MCP Server Works

The Playwright MCP server is **automatically started by the AI application** when you launch it. There is no manual startup process required.

<!-- section_id: "5375bece-9895-498c-bf8c-801d3936f1b6" -->
### Automatic Startup Process

1. AI application reads MCP configuration on startup
   - **Cursor IDE**: `~/.config/mcp/mcp.json` (or `~/.cursor/mcp.json`)
   - **Claude Code**: `.mcp.json` in project root
2. For each MCP server configured, the AI application executes the specified command
3. The MCP server starts in the background and connects to the AI application
4. MCP tools become available for use in the conversation

<!-- section_id: "dd2c065f-204a-4219-976f-6944a1cc6a72" -->
### Server Lifecycle

- **Starts:** When the AI application launches
- **Runs:** Continuously in the background during your session
- **Stops:** When the AI application closes

<!-- section_id: "97906bdd-7db0-42c3-b98e-1a896eb4279f" -->
## Starting the MCP Server

<!-- section_id: "9f79d5fc-d410-4491-b453-27c2d17050ee" -->
### First Time Setup

1. Ensure you've completed the setup process (see `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for Cursor IDE)
2. Verify MCP configuration exists with valid configuration
3. Launch the AI application

The server will start automatically.

<!-- section_id: "f5fceb91-7a7c-4ff1-b12d-03a3179ca420" -->
### After Configuration Changes

If you modify the MCP configuration:

1. Save the file
2. **Completely close the AI application** (not just the window, ensure the process is terminated)
3. Restart the AI application
4. The MCP server will start with the new configuration

<!-- section_id: "f835344a-6029-4511-8408-da7640550e16" -->
## Verifying the Server is Running

<!-- section_id: "68880d47-de94-4191-9c64-42c2b744903d" -->
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

<!-- section_id: "557c94b7-03c5-44a1-86c0-5e052ad1928f" -->
### Check 2: Test Navigation

Ask the AI to navigate to a website:

```
Please navigate to https://example.com
```

If the server is working, the AI will successfully navigate and show you the page snapshot.

<!-- section_id: "f1d327dd-a100-4c4b-b560-9b098ad9c911" -->
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

<!-- section_id: "c85c7525-59a2-4c94-92d2-350aff9cb8ea" -->
### Check 4: Verify in Application Settings

**Cursor IDE**:
- Go to Settings → Tools & MCP → Installed MCP Servers
- Should show "playwright" with "22 tools enabled"

**Claude Code**:
- Check application logs for MCP server startup messages
- Verify tools are available in conversation

<!-- section_id: "e8ea7046-89f0-4005-8b96-b2df7eae58aa" -->
## Available Playwright Tools

Once the MCP server is running, the AI application has access to these tools:

<!-- section_id: "7b25bc36-9c2f-4782-949d-7c0dffc4c583" -->
### Navigation
- `browser_navigate` - Navigate to a URL
- `browser_navigate_back` - Go back to previous page
- `browser_tabs` - List, create, close, or select tabs

<!-- section_id: "02f75d6e-e3ab-4940-b0b3-ee0911689b2f" -->
### Page Interaction
- `browser_click` - Click on elements
- `browser_type` - Type text into inputs
- `browser_press_key` - Press keyboard keys
- `browser_hover` - Hover over elements
- `browser_drag` - Drag and drop elements

<!-- section_id: "4e86d86c-f559-409c-bf8d-df0e8d12337c" -->
### Forms
- `browser_fill_form` - Fill multiple form fields at once
- `browser_select_option` - Select dropdown options
- `browser_file_upload` - Upload files

<!-- section_id: "0a2d6262-346b-42d6-a6bb-6eacc9082a59" -->
### Information Gathering
- `browser_snapshot` - Get accessibility snapshot of the page
- `browser_take_screenshot` - Capture screenshots
- `browser_console_messages` - View console logs
- `browser_network_requests` - View network requests
- `browser_evaluate` - Execute JavaScript

<!-- section_id: "b93f8667-b426-4dfe-af3f-bb8018578eff" -->
### Waiting & Dialogs
- `browser_wait_for` - Wait for text to appear/disappear or time to pass
- `browser_handle_dialog` - Handle alert/confirm/prompt dialogs

<!-- section_id: "d20f8ea7-859d-4e0e-b71a-f88e8372799f" -->
### Browser Management
- `browser_close` - Close the browser
- `browser_resize` - Resize browser window
- `browser_install` - Install browser (if not already installed)

<!-- section_id: "73fea5a0-cea6-45b4-8329-94faf0cc7cf3" -->
## Common Usage Patterns

<!-- section_id: "306b5f03-fd60-4a5f-9a36-3bb76ecd8a36" -->
### Example 1: Navigate and Extract Information

```
Navigate to https://news.ycombinator.com and tell me the top 3 stories
```

The AI will:
1. Use `browser_navigate` to load the page
2. Use `browser_snapshot` to get the page structure
3. Parse the snapshot and extract the information

<!-- section_id: "718c62a9-7011-4182-b063-747dc013bdb0" -->
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

<!-- section_id: "3d918031-f180-469e-bca9-2850b9d67069" -->
### Example 3: Take Screenshots

```
Navigate to https://example.com and take a screenshot
```

The AI will:
1. Navigate to the page
2. Use `browser_take_screenshot` to capture the page
3. Save the screenshot to a file

<!-- section_id: "8f87a1fb-206c-42fe-b013-b4502129c5f0" -->
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

<!-- section_id: "3440cfeb-8c44-46da-950e-90de3692ecc5" -->
## Troubleshooting

<!-- section_id: "998cb6d0-3f78-4a41-a04e-b6f8ad7da9dc" -->
### Server Not Starting

**Symptom:** MCP tools are not available, error message about tools not being available

**Solutions:**
1. Verify MCP configuration exists and has valid JSON syntax
2. Check that the configuration matches the format in `PLAYWRIGHT_MCP_CURSOR_SETUP.md`
3. Completely restart the AI application (ensure the process is terminated)
4. Check application logs for MCP server startup errors

<!-- section_id: "fe3f6b32-4aed-4d88-a53c-42051c6669f5" -->
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

<!-- section_id: "411d4733-e727-4933-95e7-b38f89e4ee47" -->
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

<!-- section_id: "87b5ee84-b24e-43a4-9a0d-b5b38c171bf5" -->
### Performance Issues

If the browser is slow or unresponsive:

1. Close unused browser tabs using the `browser_tabs` tool
2. Close and restart the browser using `browser_close`
3. Consider using headless mode (default) for better performance
4. Check system resources (RAM, CPU)

<!-- section_id: "dfdb669b-449a-4e9c-9265-133965702ebd" -->
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

<!-- section_id: "d0f04694-1198-462d-9411-345b661f4625" -->
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

<!-- section_id: "e4a072fa-51cf-455b-b2fb-3a1120d762b9" -->
## Configuration Reference

<!-- section_id: "49813927-76e0-4a66-8a27-a2961f1b2e6a" -->
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

<!-- section_id: "4ad6bb16-714e-44e1-aa57-a33b3205b50a" -->
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

<!-- section_id: "49ba6851-fb5f-4161-96ba-f9fdf66d7a8c" -->
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

<!-- section_id: "2dbe940c-12ba-4aa2-8b86-7641579efc79" -->
## Best Practices

1. **Keep it Simple:** Use the basic configuration unless you have specific needs
2. **Use Chromium:** It's the most reliable and well-tested browser option
3. **Restart After Config Changes:** Always restart the AI application after modifying MCP configuration
4. **Close Unused Tabs:** Browser tabs consume memory; close them when done
5. **Check Snapshots First:** Use `browser_snapshot` before taking screenshots (it's faster)
6. **Handle Errors Gracefully:** Be prepared for network issues, timeouts, and page errors

<!-- section_id: "cdbc213e-81e0-460a-96c7-15e960613b04" -->
## Security Considerations

<!-- section_id: "748c9dfe-12f3-40d6-a084-bd80f958354a" -->
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

<!-- section_id: "fc4091ab-4ae0-4ad3-a742-8b4141a8b9ff" -->
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

<!-- section_id: "c4366733-8c91-41ab-bf27-13bd725da9ea" -->
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

<!-- section_id: "96f85bbd-418f-4487-a610-f08f4d695567" -->
## Getting Help

<!-- section_id: "b154dcaf-f5cb-46c8-97f5-46b1bd36c68a" -->
### Check Documentation
- Official Playwright Docs: https://playwright.dev/
- MCP Protocol Docs: https://modelcontextprotocol.io/
- [Playwright MCP Cursor Setup](./PLAYWRIGHT_MCP_CURSOR_SETUP.md) - Setup guide for Cursor IDE

<!-- section_id: "21bb2df3-6613-464c-a95c-ba79d64e7c13" -->
### Common Issues
- See `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for setup troubleshooting
- Check application logs for error messages
- Verify browser installation: `ls -la ~/.cache/ms-playwright/`

<!-- section_id: "c2b9fb3f-6290-4493-95f2-ebaf93cab19c" -->
### Manual Testing
Test if the MCP server can start manually:
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
npx -y @playwright/mcp@latest --browser chromium
```

If this fails, the issue is with the installation, not the AI application.

<!-- section_id: "04c7a516-4d92-4137-9a36-32e1555c465a" -->
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

