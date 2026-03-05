---
resource_id: "8d72cf09-2db4-4566-8534-59f2fa2c94bb"
resource_type: "document"
resource_name: "playwright-mcp-usage"
---
# Playwright MCP Server Usage Guide

This guide explains how to start, use, and manage the Playwright MCP server with Claude Code.

<!-- section_id: "f0d5d1a5-3fb5-4569-bca5-b1fba44aaf16" -->
## How the MCP Server Works

The Playwright MCP server is **automatically started by Claude Code** when you launch the application. There is no manual startup process required.

<!-- section_id: "66f74744-1e2d-4183-afcb-d4ae9d90b117" -->
### Automatic Startup Process

1. Claude Code reads `.mcp.json` on startup
2. For each MCP server configured, Claude Code executes the specified command
3. The MCP server starts in the background and connects to Claude Code
4. MCP tools become available for use in the conversation

<!-- section_id: "18c3e1d8-0cfb-428e-82a4-73bd14ffbe68" -->
### Server Lifecycle

- **Starts:** When Claude Code launches
- **Runs:** Continuously in the background during your session
- **Stops:** When Claude Code closes

<!-- section_id: "7155c48d-e48a-4698-8916-4f8dd8b5ea3c" -->
## Starting the MCP Server

<!-- section_id: "55fb4134-a471-4d82-b691-d6a0ba3590e0" -->
### First Time Setup

1. Ensure you've completed the setup process (see `playwright-mcp-setup.md`)
2. Verify `.mcp.json` exists in your project root with valid configuration
3. Launch Claude Code

The server will start automatically.

<!-- section_id: "ae47a707-caa2-46a6-80f3-0790f65d59b7" -->
### After Configuration Changes

If you modify `.mcp.json`:

1. Save the file
2. **Completely close Claude Code** (not just the window, ensure the process is terminated)
3. Restart Claude Code
4. The MCP server will start with the new configuration

<!-- section_id: "cfac75f0-65f0-4ed5-b6a8-8be2095f12f8" -->
## Verifying the Server is Running

<!-- section_id: "8a8bad52-d107-49ab-b07e-7ea67ca12e92" -->
### Check 1: MCP Tools Available

In a Claude Code conversation, MCP tools will be available if the server is running. These tools start with `mcp__playwright__`:

- `mcp__playwright__browser_navigate`
- `mcp__playwright__browser_snapshot`
- `mcp__playwright__browser_click`
- `mcp__playwright__browser_type`
- And many more...

<!-- section_id: "5dfccb73-cf5e-4ff4-8545-d6d2253c879c" -->
### Check 2: Test Navigation

Ask Claude to navigate to a website:

```
Please navigate to https://example.com
```

If the server is working, Claude will successfully navigate and show you the page snapshot.

<!-- section_id: "417211bd-fc56-4b8f-9330-b17022a277db" -->
### Check 3: Manual Server Test

You can manually test if the MCP server starts correctly:

```bash
npx -y @playwright/mcp@latest --browser chromium
```

This should start the server without errors. Press Ctrl+C to stop.

<!-- section_id: "6cafed25-4f8f-4b82-bd0c-62aedff521fe" -->
## Available Playwright Tools

Once the MCP server is running, Claude Code has access to these tools:

<!-- section_id: "9c16e21e-4aad-4bdf-ace1-94cec76250ae" -->
### Navigation
- `browser_navigate` - Navigate to a URL
- `browser_navigate_back` - Go back to previous page
- `browser_tabs` - List, create, close, or select tabs

<!-- section_id: "64d0842d-9124-419a-8356-210b46367e8a" -->
### Page Interaction
- `browser_click` - Click on elements
- `browser_type` - Type text into inputs
- `browser_press_key` - Press keyboard keys
- `browser_hover` - Hover over elements
- `browser_drag` - Drag and drop elements

<!-- section_id: "56dbd2d9-fd11-4a0a-971a-94cedd9e1ac5" -->
### Forms
- `browser_fill_form` - Fill multiple form fields at once
- `browser_select_option` - Select dropdown options
- `browser_file_upload` - Upload files

<!-- section_id: "9acd31f5-769d-4689-a223-11e391632a47" -->
### Information Gathering
- `browser_snapshot` - Get accessibility snapshot of the page
- `browser_take_screenshot` - Capture screenshots
- `browser_console_messages` - View console logs
- `browser_network_requests` - View network requests
- `browser_evaluate` - Execute JavaScript

<!-- section_id: "544bb67f-3336-41ec-8847-04c385dc61aa" -->
### Waiting & Dialogs
- `browser_wait_for` - Wait for text to appear/disappear or time to pass
- `browser_handle_dialog` - Handle alert/confirm/prompt dialogs

<!-- section_id: "0613342c-653e-467e-930a-16c51c94ed79" -->
### Browser Management
- `browser_close` - Close the browser
- `browser_resize` - Resize browser window
- `browser_install` - Install browser (if not already installed)

<!-- section_id: "ff1323df-a6ac-4bb4-9736-708dffa84133" -->
## Common Usage Patterns

<!-- section_id: "02094d13-845d-41be-8a2a-630df78b37be" -->
### Example 1: Navigate and Extract Information

```
Navigate to https://news.ycombinator.com and tell me the top 3 stories
```

Claude will:
1. Use `browser_navigate` to load the page
2. Use `browser_snapshot` to get the page structure
3. Parse the snapshot and extract the information

<!-- section_id: "8f5ad069-828e-4c30-a6b8-d6cd41ffb4e4" -->
### Example 2: Automate Form Filling

```
Go to https://example.com/contact and fill out the contact form with:
- Name: John Doe
- Email: john@example.com
- Message: Hello, this is a test
```

Claude will:
1. Navigate to the page
2. Use `browser_snapshot` to identify form fields
3. Use `browser_fill_form` to fill all fields
4. Optionally submit the form

<!-- section_id: "8fdf5de8-a6c6-4089-b295-ef78fd5d71fe" -->
### Example 3: Take Screenshots

```
Navigate to https://example.com and take a screenshot
```

Claude will:
1. Navigate to the page
2. Use `browser_take_screenshot` to capture the page
3. Save the screenshot to a file

<!-- section_id: "963f0ba4-a43c-4245-976a-f227902e9bef" -->
### Example 4: Testing Workflows

```
Test the login flow on https://example.com/login:
1. Enter username: testuser
2. Enter password: testpass123
3. Click the login button
4. Verify we're redirected to the dashboard
```

Claude will:
1. Navigate to the login page
2. Use `browser_type` to enter credentials
3. Use `browser_click` to click the button
4. Use `browser_snapshot` to verify the result

<!-- section_id: "28bd3147-4d67-4b8f-ba52-086f69d9cc1a" -->
## Troubleshooting

<!-- section_id: "29204f12-056c-4034-b393-8e6863fbb15d" -->
### Server Not Starting

**Symptom:** MCP tools are not available, error message: "No such tool available: mcp__playwright__browser_navigate"

**Solutions:**
1. Verify `.mcp.json` exists and has valid JSON syntax
2. Check that the configuration matches the format in `playwright-mcp-setup.md`
3. Completely restart Claude Code (ensure the process is terminated)
4. Check Claude Code logs for MCP server startup errors

<!-- section_id: "d5650cd5-1702-4a99-b697-b6b021c46b90" -->
### Browser Not Found

**Symptom:** Error: "Chromium distribution 'chrome' is not found"

**Solutions:**
1. Verify browser is installed: `ls -la ~/.cache/ms-playwright/`
2. Reinstall browser: `npx -y playwright@latest install chromium`
3. Check `.mcp.json` specifies the correct browser with `"--browser", "chromium"`
4. Restart Claude Code

<!-- section_id: "337402f3-27d1-4bbe-b54b-7f92499f7e56" -->
### Server Crashes or Disconnects

**Solutions:**
1. Check if browser binaries are corrupted
2. Reinstall browser: `rm -rf ~/.cache/ms-playwright/ && npx -y playwright@latest install chromium`
3. Restart Claude Code

<!-- section_id: "943fe152-4401-4c5a-afbb-d74a2733f933" -->
### Performance Issues

If the browser is slow or unresponsive:

1. Close unused browser tabs using the `browser_tabs` tool
2. Close and restart the browser using `browser_close`
3. Consider using headless mode (default) for better performance
4. Check system resources (RAM, CPU)

<!-- section_id: "3ab51513-98a1-4b2d-a273-3b2937e043ba" -->
## Manual Server Invocation (Testing Only)

For debugging purposes, you can manually start the MCP server:

```bash
# Basic startup
npx -y @playwright/mcp@latest --browser chromium

# With additional options
npx -y @playwright/mcp@latest \
  --browser chromium \
  --allowed-origins "*"
```

**Note:** This is only for testing. Claude Code will manage the server automatically during normal use.

<!-- section_id: "56e8b6cf-043e-409f-badd-90a1c4aa8345" -->
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

<!-- section_id: "a647b0f9-4d8d-47db-9cd3-adb545b86bf3" -->
## Configuration Reference

<!-- section_id: "2b318f93-cefc-45d4-ad3e-5911d5c89169" -->
### Basic Configuration

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

<!-- section_id: "2f97abbe-dc21-4987-bf3b-29835a85ad78" -->
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

<!-- section_id: "ac2d5370-de33-45b2-861d-f4dda158e027" -->
## Best Practices

1. **Keep it Simple:** Use the basic configuration unless you have specific needs
2. **Use Chromium:** It's the most reliable and well-tested browser option
3. **Restart After Config Changes:** Always restart Claude Code after modifying `.mcp.json`
4. **Close Unused Tabs:** Browser tabs consume memory; close them when done
5. **Check Snapshots First:** Use `browser_snapshot` before taking screenshots (it's faster)
6. **Handle Errors Gracefully:** Be prepared for network issues, timeouts, and page errors

<!-- section_id: "cd30e435-85db-4708-8daa-db7d6c93b579" -->
## Security Considerations

<!-- section_id: "c5f6c1ba-679a-49a8-95a3-adccff29c4bf" -->
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

<!-- section_id: "3676b622-8bfa-468b-aa68-83afc529232b" -->
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

<!-- section_id: "93f7e3b9-eb49-4d22-bc23-6ad5f2b90064" -->
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

<!-- section_id: "8fab9b0b-62d1-48de-ac3b-85c2a332c907" -->
## Getting Help

<!-- section_id: "273ac2e9-c6d8-4420-ba73-57bcf3894507" -->
### Check Documentation
- Official Playwright Docs: https://playwright.dev/
- MCP Protocol Docs: https://modelcontextprotocol.io/

<!-- section_id: "13cfdac8-6787-45be-8fdd-14881a2fc17f" -->
### Common Issues
- See `playwright-mcp-setup.md` for setup troubleshooting
- Check Claude Code logs for error messages
- Verify browser installation: `ls -la ~/.cache/ms-playwright/`

<!-- section_id: "94cf8be8-a661-451a-bf26-9c4b4c97959f" -->
### Manual Testing
Test if the MCP server can start manually:
```bash
npx -y @playwright/mcp@latest --browser chromium
```

If this fails, the issue is with the installation, not Claude Code.

<!-- section_id: "47a05a22-2b88-4f68-9d42-11efeaa0eb6a" -->
## Summary

- **Starting:** Automatic when Claude Code launches
- **Stopping:** Automatic when Claude Code closes
- **Restarting:** Close and reopen Claude Code
- **Configuration:** Edit `.mcp.json` and restart Claude Code
- **Verification:** Ask Claude to navigate to a website
- **Troubleshooting:** Check logs, verify installation, restart Claude Code

The Playwright MCP server requires no manual management during normal use. Just launch Claude Code and start automating!
