---
resource_id: "23eff2dd-a204-43b1-a421-ba69a8054800"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_USAGE"
---
# Playwright MCP Server Usage Guide

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working

This guide explains how to start, use, and manage the Playwright MCP server with AI applications (Cursor IDE, Claude Code, etc.).

<!-- section_id: "b570bc8f-3a8f-4cab-bb91-b2c62196c425" -->
## How the MCP Server Works

The Playwright MCP server is **automatically started by the AI application** when you launch it. There is no manual startup process required.

<!-- section_id: "98cdefcf-4f4d-4b23-b828-a2b0c4d67ad2" -->
### Automatic Startup Process

1. AI application reads MCP configuration on startup
   - **Cursor IDE**: `~/.config/mcp/mcp.json` (or `~/.cursor/mcp.json`)
   - **Claude Code**: `.mcp.json` in project root
2. For each MCP server configured, the AI application executes the specified command
3. The MCP server starts in the background and connects to the AI application
4. MCP tools become available for use in the conversation

<!-- section_id: "2787fe05-5537-4d52-b2bd-1af8c41fe7bf" -->
### Server Lifecycle

- **Starts:** When the AI application launches
- **Runs:** Continuously in the background during your session
- **Stops:** When the AI application closes

<!-- section_id: "403ef64d-2983-4d22-8d9b-284f985af44d" -->
## Starting the MCP Server

<!-- section_id: "994b9cc5-b2d6-41ba-a25f-170ebc182654" -->
### First Time Setup

1. Ensure you've completed the setup process (see `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for Cursor IDE)
2. Verify MCP configuration exists with valid configuration
3. Launch the AI application

The server will start automatically.

<!-- section_id: "b6fdd7b8-b5b7-49fa-809c-1624cbb6c551" -->
### After Configuration Changes

If you modify the MCP configuration:

1. Save the file
2. **Completely close the AI application** (not just the window, ensure the process is terminated)
3. Restart the AI application
4. The MCP server will start with the new configuration

<!-- section_id: "2bb3f9f2-80c6-4b1e-90f9-c0ecac976034" -->
## Verifying the Server is Running

<!-- section_id: "723be8c5-602f-47a7-9b68-beac638cbe3c" -->
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

<!-- section_id: "471336e8-4495-4c51-b9db-952285d8b3e0" -->
### Check 2: Test Navigation

Ask the AI to navigate to a website:

```
Please navigate to https://example.com
```

If the server is working, the AI will successfully navigate and show you the page snapshot.

<!-- section_id: "dda375e6-4228-47e4-8db0-a05f94de8fd8" -->
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

<!-- section_id: "daca1d38-99ab-4276-8e52-201e9f4d865e" -->
### Check 4: Verify in Application Settings

**Cursor IDE**:
- Go to Settings → Tools & MCP → Installed MCP Servers
- Should show "playwright" with "22 tools enabled"

**Claude Code**:
- Check application logs for MCP server startup messages
- Verify tools are available in conversation

<!-- section_id: "d21f3597-956b-47f0-b9f0-4097ef388a8d" -->
## Available Playwright Tools

Once the MCP server is running, the AI application has access to these tools:

<!-- section_id: "fa5aebc7-7aa9-4c00-a44a-d817f022e364" -->
### Navigation
- `browser_navigate` - Navigate to a URL
- `browser_navigate_back` - Go back to previous page
- `browser_tabs` - List, create, close, or select tabs

<!-- section_id: "5e66b0c9-39ec-4897-bc67-d863a79dff27" -->
### Page Interaction
- `browser_click` - Click on elements
- `browser_type` - Type text into inputs
- `browser_press_key` - Press keyboard keys
- `browser_hover` - Hover over elements
- `browser_drag` - Drag and drop elements

<!-- section_id: "6ec4953a-b75c-46cd-8512-37699dc6b904" -->
### Forms
- `browser_fill_form` - Fill multiple form fields at once
- `browser_select_option` - Select dropdown options
- `browser_file_upload` - Upload files

<!-- section_id: "98a36db2-86dc-4b81-ac5f-e4099e6e5078" -->
### Information Gathering
- `browser_snapshot` - Get accessibility snapshot of the page
- `browser_take_screenshot` - Capture screenshots
- `browser_console_messages` - View console logs
- `browser_network_requests` - View network requests
- `browser_evaluate` - Execute JavaScript

<!-- section_id: "affc4197-a9b5-4b5b-a8b5-3a2a98c5113a" -->
### Waiting & Dialogs
- `browser_wait_for` - Wait for text to appear/disappear or time to pass
- `browser_handle_dialog` - Handle alert/confirm/prompt dialogs

<!-- section_id: "64aa7387-d46a-40d7-985f-53dd75b211f0" -->
### Browser Management
- `browser_close` - Close the browser
- `browser_resize` - Resize browser window
- `browser_install` - Install browser (if not already installed)

<!-- section_id: "d92830f3-f3ac-4b5f-8b9f-51511efecfc7" -->
## Common Usage Patterns

<!-- section_id: "b8061e69-1fdf-40ff-a9dd-609c27ac7541" -->
### Example 1: Navigate and Extract Information

```
Navigate to https://news.ycombinator.com and tell me the top 3 stories
```

The AI will:
1. Use `browser_navigate` to load the page
2. Use `browser_snapshot` to get the page structure
3. Parse the snapshot and extract the information

<!-- section_id: "431fed82-692f-4ede-9385-a11e54d1e398" -->
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

<!-- section_id: "7bc07740-1c35-469d-a6ba-7e32eccd66d5" -->
### Example 3: Take Screenshots

```
Navigate to https://example.com and take a screenshot
```

The AI will:
1. Navigate to the page
2. Use `browser_take_screenshot` to capture the page
3. Save the screenshot to a file

<!-- section_id: "611691fe-1041-4f2c-a06c-0d5c2c46139b" -->
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

<!-- section_id: "2e155ed6-e2a7-4990-9ef1-9ed0635ed33d" -->
## Troubleshooting

<!-- section_id: "f98b0ada-57af-453e-866a-03ef460dfb9d" -->
### Server Not Starting

**Symptom:** MCP tools are not available, error message about tools not being available

**Solutions:**
1. Verify MCP configuration exists and has valid JSON syntax
2. Check that the configuration matches the format in `PLAYWRIGHT_MCP_CURSOR_SETUP.md`
3. Completely restart the AI application (ensure the process is terminated)
4. Check application logs for MCP server startup errors

<!-- section_id: "609de7a5-339a-4ab2-98e1-663cb198827a" -->
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

<!-- section_id: "661a53c3-a364-474c-bb19-7bb552eaee05" -->
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

<!-- section_id: "0475d6d4-33f8-4294-8966-d985cb938778" -->
### Performance Issues

If the browser is slow or unresponsive:

1. Close unused browser tabs using the `browser_tabs` tool
2. Close and restart the browser using `browser_close`
3. Consider using headless mode (default) for better performance
4. Check system resources (RAM, CPU)

<!-- section_id: "c318d459-f981-432b-b4e4-a4e7c6eddd42" -->
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

<!-- section_id: "8690b3a7-9b3d-49f0-8980-497a23f3907e" -->
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

<!-- section_id: "2de6f8dc-67c0-4eb0-820a-870593885c87" -->
## Configuration Reference

<!-- section_id: "da9f7c33-d2a3-4e3a-a3bb-d4ead3cb47d5" -->
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

<!-- section_id: "6614adba-cfb5-4221-83e4-2b6f2cbc1377" -->
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

<!-- section_id: "df2285da-6b3f-471d-bf89-17a4a7581acc" -->
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

<!-- section_id: "829b87e1-e0a6-4bc2-8703-861e387474c3" -->
## Best Practices

1. **Keep it Simple:** Use the basic configuration unless you have specific needs
2. **Use Chromium:** It's the most reliable and well-tested browser option
3. **Restart After Config Changes:** Always restart the AI application after modifying MCP configuration
4. **Close Unused Tabs:** Browser tabs consume memory; close them when done
5. **Check Snapshots First:** Use `browser_snapshot` before taking screenshots (it's faster)
6. **Handle Errors Gracefully:** Be prepared for network issues, timeouts, and page errors

<!-- section_id: "07b33c4f-6754-4e48-9a73-8d4bbf11ff28" -->
## Security Considerations

<!-- section_id: "a9f026cb-76c9-45e0-a62d-8750fab3896c" -->
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

<!-- section_id: "2399a9a4-aaf6-4b6c-b17c-76c06e4b3e12" -->
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

<!-- section_id: "ba12076c-c9eb-4c8e-ae19-6ee587f5a445" -->
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

<!-- section_id: "42440d2c-1ba9-45b6-afe0-a3945f3f3eed" -->
## Getting Help

<!-- section_id: "c364eafc-cdaa-4b93-b028-e512cf987b2f" -->
### Check Documentation
- Official Playwright Docs: https://playwright.dev/
- MCP Protocol Docs: https://modelcontextprotocol.io/
- [Playwright MCP Cursor Setup](./PLAYWRIGHT_MCP_CURSOR_SETUP.md) - Setup guide for Cursor IDE

<!-- section_id: "c13438ec-59de-4bd0-9c73-f90de9433951" -->
### Common Issues
- See `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for setup troubleshooting
- Check application logs for error messages
- Verify browser installation: `ls -la ~/.cache/ms-playwright/`

<!-- section_id: "230420e9-75a6-47f1-a620-33538ebc7038" -->
### Manual Testing
Test if the MCP server can start manually:
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
npx -y @playwright/mcp@latest --browser chromium
```

If this fails, the issue is with the installation, not the AI application.

<!-- section_id: "716c91d4-63c3-47fe-b202-b00fb7580b0f" -->
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

