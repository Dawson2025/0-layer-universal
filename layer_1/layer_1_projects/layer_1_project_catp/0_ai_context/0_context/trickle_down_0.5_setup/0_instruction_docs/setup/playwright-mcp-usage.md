---
resource_id: "a61a700a-a752-40b4-96d5-2200f5440921"
resource_type: "document"
resource_name: "playwright-mcp-usage"
---
# Playwright MCP Server Usage Guide

This guide explains how to start, use, and manage the Playwright MCP server with Claude Code.

<!-- section_id: "fa7f9e25-50f0-45db-9a16-dd523980f779" -->
## How the MCP Server Works

The Playwright MCP server is **automatically started by Claude Code** when you launch the application. There is no manual startup process required.

<!-- section_id: "5101d402-febb-40a0-be33-b0302dbe954e" -->
### Automatic Startup Process

1. Claude Code reads `.mcp.json` on startup
2. For each MCP server configured, Claude Code executes the specified command
3. The MCP server starts in the background and connects to Claude Code
4. MCP tools become available for use in the conversation

<!-- section_id: "e2a4a66f-34e9-4b70-84fd-59db577ef472" -->
### Server Lifecycle

- **Starts:** When Claude Code launches
- **Runs:** Continuously in the background during your session
- **Stops:** When Claude Code closes

<!-- section_id: "946857f9-6b04-4abb-a66b-4f1aa073417e" -->
## Starting the MCP Server

<!-- section_id: "a46feabd-4f92-4238-bc42-bd029fd501b0" -->
### First Time Setup

1. Ensure you've completed the setup process (see `playwright-mcp-setup.md`)
2. Verify `.mcp.json` exists in your project root with valid configuration
3. Launch Claude Code

The server will start automatically.

<!-- section_id: "254faf07-9c15-433f-9079-65e11d6a980d" -->
### After Configuration Changes

If you modify `.mcp.json`:

1. Save the file
2. **Completely close Claude Code** (not just the window, ensure the process is terminated)
3. Restart Claude Code
4. The MCP server will start with the new configuration

<!-- section_id: "2dc7f962-2736-47d8-837d-1ca67f89d2bb" -->
## Verifying the Server is Running

<!-- section_id: "e3721275-53c4-43f1-8905-ca806099de63" -->
### Check 1: MCP Tools Available

In a Claude Code conversation, MCP tools will be available if the server is running. These tools start with `mcp__playwright__`:

- `mcp__playwright__browser_navigate`
- `mcp__playwright__browser_snapshot`
- `mcp__playwright__browser_click`
- `mcp__playwright__browser_type`
- And many more...

<!-- section_id: "59ccfff3-1e67-43bd-aec2-766def849516" -->
### Check 2: Test Navigation

Ask Claude to navigate to a website:

```
Please navigate to https://example.com
```

If the server is working, Claude will successfully navigate and show you the page snapshot.

<!-- section_id: "5a71ae44-2d5b-4ddb-8797-a847cd0d7338" -->
### Check 3: Manual Server Test

You can manually test if the MCP server starts correctly:

```bash
npx -y @playwright/mcp@latest --browser chromium
```

This should start the server without errors. Press Ctrl+C to stop.

<!-- section_id: "ef057693-3100-4796-bb21-0c4695b11925" -->
## Available Playwright Tools

Once the MCP server is running, Claude Code has access to these tools:

<!-- section_id: "ce67f8e4-e3a8-4c6f-994c-998a8d85a629" -->
### Navigation
- `browser_navigate` - Navigate to a URL
- `browser_navigate_back` - Go back to previous page
- `browser_tabs` - List, create, close, or select tabs

<!-- section_id: "dd9b6281-0996-42e3-9c00-7cff665f76f8" -->
### Page Interaction
- `browser_click` - Click on elements
- `browser_type` - Type text into inputs
- `browser_press_key` - Press keyboard keys
- `browser_hover` - Hover over elements
- `browser_drag` - Drag and drop elements

<!-- section_id: "603c3e1c-dc0f-4607-bfdd-d2a3ed290ca2" -->
### Forms
- `browser_fill_form` - Fill multiple form fields at once
- `browser_select_option` - Select dropdown options
- `browser_file_upload` - Upload files

<!-- section_id: "a2f07902-b21a-4aef-ada2-02895369b141" -->
### Information Gathering
- `browser_snapshot` - Get accessibility snapshot of the page
- `browser_take_screenshot` - Capture screenshots
- `browser_console_messages` - View console logs
- `browser_network_requests` - View network requests
- `browser_evaluate` - Execute JavaScript

<!-- section_id: "04365ce6-cae7-4375-9ca4-8fdc7507666a" -->
### Waiting & Dialogs
- `browser_wait_for` - Wait for text to appear/disappear or time to pass
- `browser_handle_dialog` - Handle alert/confirm/prompt dialogs

<!-- section_id: "9c2be692-8211-4d49-8bd4-cbb7e22d1895" -->
### Browser Management
- `browser_close` - Close the browser
- `browser_resize` - Resize browser window
- `browser_install` - Install browser (if not already installed)

<!-- section_id: "36a84be0-eb58-4b0c-9c12-5d59e04df621" -->
## Common Usage Patterns

<!-- section_id: "c898ac28-6933-4455-a26a-372efddf018b" -->
### Example 1: Navigate and Extract Information

```
Navigate to https://news.ycombinator.com and tell me the top 3 stories
```

Claude will:
1. Use `browser_navigate` to load the page
2. Use `browser_snapshot` to get the page structure
3. Parse the snapshot and extract the information

<!-- section_id: "fe2dc027-6016-4611-b7cd-f497b6d23452" -->
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

<!-- section_id: "a8835000-36e1-4db7-b994-458f286892a6" -->
### Example 3: Take Screenshots

```
Navigate to https://example.com and take a screenshot
```

Claude will:
1. Navigate to the page
2. Use `browser_take_screenshot` to capture the page
3. Save the screenshot to a file

<!-- section_id: "86e7f460-3ec6-4dfd-acbc-45fe45ca8b70" -->
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

<!-- section_id: "d1717898-4517-4d25-b4e9-9f8de814e682" -->
## Troubleshooting

<!-- section_id: "5869a921-6e5d-42fa-9a80-17c9ec8e8c5d" -->
### Server Not Starting

**Symptom:** MCP tools are not available, error message: "No such tool available: mcp__playwright__browser_navigate"

**Solutions:**
1. Verify `.mcp.json` exists and has valid JSON syntax
2. Check that the configuration matches the format in `playwright-mcp-setup.md`
3. Completely restart Claude Code (ensure the process is terminated)
4. Check Claude Code logs for MCP server startup errors

<!-- section_id: "95c92a31-9154-4f34-be82-8f26c4f9f847" -->
### Browser Not Found

**Symptom:** Error: "Chromium distribution 'chrome' is not found"

**Solutions:**
1. Verify browser is installed: `ls -la ~/.cache/ms-playwright/`
2. Reinstall browser: `npx -y playwright@latest install chromium`
3. Check `.mcp.json` specifies the correct browser with `"--browser", "chromium"`
4. Restart Claude Code

<!-- section_id: "1c998e0a-a60c-4f29-a171-3e9e34ce407b" -->
### Server Crashes or Disconnects

**Solutions:**
1. Check if browser binaries are corrupted
2. Reinstall browser: `rm -rf ~/.cache/ms-playwright/ && npx -y playwright@latest install chromium`
3. Restart Claude Code

<!-- section_id: "c988b460-9f1c-4e37-a9b6-904758fc73c3" -->
### Performance Issues

If the browser is slow or unresponsive:

1. Close unused browser tabs using the `browser_tabs` tool
2. Close and restart the browser using `browser_close`
3. Consider using headless mode (default) for better performance
4. Check system resources (RAM, CPU)

<!-- section_id: "cb94fe60-3e58-4bc5-96aa-6322b509224d" -->
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

<!-- section_id: "89d0bc73-54d8-4fe8-bfc9-2e43bf821ad3" -->
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

<!-- section_id: "dc287b4b-c761-4208-a5e7-363c1df0ad1c" -->
## Configuration Reference

<!-- section_id: "78aa544c-c030-4793-9934-226ae0e22f3c" -->
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

<!-- section_id: "ad4da4c1-6c1e-4275-a265-15b00cbeee39" -->
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

<!-- section_id: "3df94a93-f19f-4359-9fec-bea0b908175e" -->
## Best Practices

1. **Keep it Simple:** Use the basic configuration unless you have specific needs
2. **Use Chromium:** It's the most reliable and well-tested browser option
3. **Restart After Config Changes:** Always restart Claude Code after modifying `.mcp.json`
4. **Close Unused Tabs:** Browser tabs consume memory; close them when done
5. **Check Snapshots First:** Use `browser_snapshot` before taking screenshots (it's faster)
6. **Handle Errors Gracefully:** Be prepared for network issues, timeouts, and page errors

<!-- section_id: "82715eec-6e19-43e9-863b-7a0a6711570e" -->
## Security Considerations

<!-- section_id: "55d50354-0f3b-4531-a4e5-eb955575a067" -->
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

<!-- section_id: "b02c99ce-e6ac-4d31-b0bd-e481768a6d23" -->
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

<!-- section_id: "c40df22b-6ad1-4041-b07d-89ca18244bcf" -->
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

<!-- section_id: "583b0535-d921-4086-b71f-0da4ec69e270" -->
## Getting Help

<!-- section_id: "0d12fd16-0c32-4dde-af43-d2af90bb7b11" -->
### Check Documentation
- Official Playwright Docs: https://playwright.dev/
- MCP Protocol Docs: https://modelcontextprotocol.io/

<!-- section_id: "4c251f8c-ff14-4d0f-a6af-a548c2485014" -->
### Common Issues
- See `playwright-mcp-setup.md` for setup troubleshooting
- Check Claude Code logs for error messages
- Verify browser installation: `ls -la ~/.cache/ms-playwright/`

<!-- section_id: "299aa9ee-d826-4c93-bdbc-fc628f2f3b7b" -->
### Manual Testing
Test if the MCP server can start manually:
```bash
npx -y @playwright/mcp@latest --browser chromium
```

If this fails, the issue is with the installation, not Claude Code.

<!-- section_id: "21215804-4d91-42c8-a886-5762ed4a044f" -->
## Summary

- **Starting:** Automatic when Claude Code launches
- **Stopping:** Automatic when Claude Code closes
- **Restarting:** Close and reopen Claude Code
- **Configuration:** Edit `.mcp.json` and restart Claude Code
- **Verification:** Ask Claude to navigate to a website
- **Troubleshooting:** Check logs, verify installation, restart Claude Code

The Playwright MCP server requires no manual management during normal use. Just launch Claude Code and start automating!
