---
resource_id: "caa32e59-aae5-436a-93b9-d1a6610399d4"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_USAGE"
---
# Playwright MCP Server Usage Guide

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working

This guide explains how to start, use, and manage the Playwright MCP server with AI applications (Cursor IDE, Claude Code, etc.).

<!-- section_id: "011cfdc2-2080-4066-9ddd-19aebc4ae8f7" -->
## How the MCP Server Works

The Playwright MCP server is **automatically started by the AI application** when you launch it. There is no manual startup process required.

<!-- section_id: "cbe6a0c7-9e2e-43cb-b7c3-f3d06dde0428" -->
### Automatic Startup Process

1. AI application reads MCP configuration on startup
   - **Cursor IDE**: `~/.config/mcp/mcp.json` (or `~/.cursor/mcp.json`)
   - **Claude Code**: `.mcp.json` in project root
2. For each MCP server configured, the AI application executes the specified command
3. The MCP server starts in the background and connects to the AI application
4. MCP tools become available for use in the conversation

<!-- section_id: "a7f8e213-2711-4f46-a703-0ccad5f53ddd" -->
### Server Lifecycle

- **Starts:** When the AI application launches
- **Runs:** Continuously in the background during your session
- **Stops:** When the AI application closes

<!-- section_id: "3045bebb-7fdf-4561-8733-c84831f66f51" -->
## Starting the MCP Server

<!-- section_id: "b631fd89-3df0-4acb-8528-d1fd1bf82df8" -->
### First Time Setup

1. Ensure you've completed the setup process (see `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for Cursor IDE)
2. Verify MCP configuration exists with valid configuration
3. Launch the AI application

The server will start automatically.

<!-- section_id: "804cd2f9-9f82-418b-813a-6d0113f40cca" -->
### After Configuration Changes

If you modify the MCP configuration:

1. Save the file
2. **Completely close the AI application** (not just the window, ensure the process is terminated)
3. Restart the AI application
4. The MCP server will start with the new configuration

<!-- section_id: "f16b67c2-9f22-43ac-9c4a-3cd51b5f80dc" -->
## Verifying the Server is Running

<!-- section_id: "9557ad6f-f928-4aee-89a3-ccab2e3288fc" -->
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

<!-- section_id: "5f6ecc4a-bba4-4cb8-a1a0-3e62f5c95f59" -->
### Check 2: Test Navigation

Ask the AI to navigate to a website:

```
Please navigate to https://example.com
```

If the server is working, the AI will successfully navigate and show you the page snapshot.

<!-- section_id: "444c9d6b-ba7b-48f3-9d23-c1d7d199d7ba" -->
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

<!-- section_id: "4c440307-f740-4efd-85e4-042f4d4fad59" -->
### Check 4: Verify in Application Settings

**Cursor IDE**:
- Go to Settings → Tools & MCP → Installed MCP Servers
- Should show "playwright" with "22 tools enabled"

**Claude Code**:
- Check application logs for MCP server startup messages
- Verify tools are available in conversation

<!-- section_id: "737ff4f2-265f-45f1-b193-96efdc61f594" -->
## Available Playwright Tools

Once the MCP server is running, the AI application has access to these tools:

<!-- section_id: "df30b9a9-02bc-4435-bd97-09d97ad06a90" -->
### Navigation
- `browser_navigate` - Navigate to a URL
- `browser_navigate_back` - Go back to previous page
- `browser_tabs` - List, create, close, or select tabs

<!-- section_id: "0d2ea919-7ad4-4bc7-9563-2d21044dce68" -->
### Page Interaction
- `browser_click` - Click on elements
- `browser_type` - Type text into inputs
- `browser_press_key` - Press keyboard keys
- `browser_hover` - Hover over elements
- `browser_drag` - Drag and drop elements

<!-- section_id: "5dc8b51b-47e2-4d0b-bef8-e870b8e9a9a8" -->
### Forms
- `browser_fill_form` - Fill multiple form fields at once
- `browser_select_option` - Select dropdown options
- `browser_file_upload` - Upload files

<!-- section_id: "31fb7a45-6343-41e2-9562-1bb77b9a828d" -->
### Information Gathering
- `browser_snapshot` - Get accessibility snapshot of the page
- `browser_take_screenshot` - Capture screenshots
- `browser_console_messages` - View console logs
- `browser_network_requests` - View network requests
- `browser_evaluate` - Execute JavaScript

<!-- section_id: "3f502ca1-d098-448b-8596-4cbbb282800e" -->
### Waiting & Dialogs
- `browser_wait_for` - Wait for text to appear/disappear or time to pass
- `browser_handle_dialog` - Handle alert/confirm/prompt dialogs

<!-- section_id: "21b8ab38-b13e-4dd3-84b0-784e0eea7d8c" -->
### Browser Management
- `browser_close` - Close the browser
- `browser_resize` - Resize browser window
- `browser_install` - Install browser (if not already installed)

<!-- section_id: "5eeeb2df-4c09-440e-b11d-e6f412a3f79d" -->
## Common Usage Patterns

<!-- section_id: "4f481e3e-7d62-422f-b20c-4411acf7a527" -->
### Example 1: Navigate and Extract Information

```
Navigate to https://news.ycombinator.com and tell me the top 3 stories
```

The AI will:
1. Use `browser_navigate` to load the page
2. Use `browser_snapshot` to get the page structure
3. Parse the snapshot and extract the information

<!-- section_id: "b12af671-7581-4ca4-bef3-5fed966e8276" -->
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

<!-- section_id: "77e9d314-089a-4236-840b-d1d10f93b837" -->
### Example 3: Take Screenshots

```
Navigate to https://example.com and take a screenshot
```

The AI will:
1. Navigate to the page
2. Use `browser_take_screenshot` to capture the page
3. Save the screenshot to a file

<!-- section_id: "4a5d3f4e-2378-412e-9c92-02423807611a" -->
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

<!-- section_id: "bc09df6c-a0aa-4659-b4ce-ec398d71216d" -->
## Troubleshooting

<!-- section_id: "fdd96a4f-5ecd-4dd9-b80c-49cef0e07310" -->
### Server Not Starting

**Symptom:** MCP tools are not available, error message about tools not being available

**Solutions:**
1. Verify MCP configuration exists and has valid JSON syntax
2. Check that the configuration matches the format in `PLAYWRIGHT_MCP_CURSOR_SETUP.md`
3. Completely restart the AI application (ensure the process is terminated)
4. Check application logs for MCP server startup errors

<!-- section_id: "c72ef781-b7da-4bce-ad0a-dec2fdc149c6" -->
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

<!-- section_id: "caf020ed-233e-4cbc-81aa-ff40e8cd6811" -->
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

<!-- section_id: "7bcd886b-4536-49c9-ab9b-dc22ee3a9c9a" -->
### Performance Issues

If the browser is slow or unresponsive:

1. Close unused browser tabs using the `browser_tabs` tool
2. Close and restart the browser using `browser_close`
3. Consider using headless mode (default) for better performance
4. Check system resources (RAM, CPU)

<!-- section_id: "9a26afe0-2c3e-4f64-8d04-f86cc4bfff4b" -->
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

<!-- section_id: "fb093516-0432-4458-8d77-6affade5492f" -->
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

<!-- section_id: "ff7dbb60-36fd-4969-8a1a-f0a88b38ad2f" -->
## Configuration Reference

<!-- section_id: "83c7459e-f23f-4546-9fd0-e560d32808fb" -->
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

<!-- section_id: "3a283dac-6fdb-4e26-8e4f-b84d26fbebee" -->
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

<!-- section_id: "75c4586f-af84-4e31-a3a4-86be6baac468" -->
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

<!-- section_id: "8d49a80c-535f-4b3e-b57b-1a801b918b26" -->
## Best Practices

1. **Keep it Simple:** Use the basic configuration unless you have specific needs
2. **Use Chromium:** It's the most reliable and well-tested browser option
3. **Restart After Config Changes:** Always restart the AI application after modifying MCP configuration
4. **Close Unused Tabs:** Browser tabs consume memory; close them when done
5. **Check Snapshots First:** Use `browser_snapshot` before taking screenshots (it's faster)
6. **Handle Errors Gracefully:** Be prepared for network issues, timeouts, and page errors

<!-- section_id: "85b2a5e1-8be4-4c2d-a8da-b59a2fd1dac5" -->
## Security Considerations

<!-- section_id: "7f7f9829-398f-4fc4-856a-609b747a6f05" -->
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

<!-- section_id: "289d7455-a418-4a45-95a9-2588d13a0240" -->
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

<!-- section_id: "f98f98dc-3be4-404a-bf4c-b3b6ff1dad4f" -->
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

<!-- section_id: "3a92a833-9315-4eea-9c46-ac104da8edbc" -->
## Getting Help

<!-- section_id: "67d5df72-63f6-4f1b-bca6-61e445049939" -->
### Check Documentation
- Official Playwright Docs: https://playwright.dev/
- MCP Protocol Docs: https://modelcontextprotocol.io/
- [Playwright MCP Cursor Setup](./PLAYWRIGHT_MCP_CURSOR_SETUP.md) - Setup guide for Cursor IDE

<!-- section_id: "ce2a931d-8092-4f41-ad5a-e53de89a779c" -->
### Common Issues
- See `PLAYWRIGHT_MCP_CURSOR_SETUP.md` for setup troubleshooting
- Check application logs for error messages
- Verify browser installation: `ls -la ~/.cache/ms-playwright/`

<!-- section_id: "aa573368-e57e-4639-9dc0-a5697ec30401" -->
### Manual Testing
Test if the MCP server can start manually:
```bash
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
npx -y @playwright/mcp@latest --browser chromium
```

If this fails, the issue is with the installation, not the AI application.

<!-- section_id: "4c856dc8-8447-436e-9501-5a5f3734f47b" -->
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

