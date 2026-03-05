---
resource_id: "e7f54061-2531-4c60-bc4f-cb38d26a061e"
resource_type: "document"
resource_name: "CHROME_DEVTOOLS_MCP_SETUP"
---
# Chrome DevTools MCP Server Setup Guide

This guide documents the setup process for the Chrome DevTools MCP (Model Context Protocol) server for use with Claude Code.

<!-- section_id: "c012c8e2-10ee-4417-9b75-2464f4be35c3" -->
## Overview

The Chrome DevTools MCP server provides Chrome-specific debugging and automation capabilities. **Unlike Playwright MCP**, this server requires **actual Google Chrome** to be installed on your system, not just Playwright's Chromium.

<!-- section_id: "f4994dc8-487d-418d-91ca-db8ad914c409" -->
## Common Setup Issues

**Before starting setup, check these common issues:**

1. **Chrome not installed** - Most common issue. Chrome DevTools MCP requires system Chrome, not Playwright Chromium.
   - Check: `google-chrome --version`
   - Fix: Install Chrome (see Step 1 below)

2. **Configuration has `--browserUrl` pointing to non-existent Chrome** - If Chrome isn't running, this will fail.
   - Check: Look for `--browserUrl http://127.0.0.1:9222` in your config
   - Fix: Remove `--browserUrl` to allow auto-launch, or ensure Chrome is running

3. **Port 9222 not active** - Chrome DevTools port must be available.
   - Check: `netstat -tuln | grep 9222`
   - Fix: Remove `--browserUrl` from config or start Chrome manually

4. **Multiple Chrome DevTools MCP processes** - Indicates connection failures.
   - Check: `ps aux | grep chrome-devtools-mcp`
   - Fix: Install Chrome and restart Claude Code

<!-- section_id: "a62819ea-5188-4334-9c3b-39c3be5a9b33" -->
## Prerequisites

- **Node.js and npm** installed
- **Google Chrome** installed on your system (not just Playwright Chromium)
- Claude Code installed
- WSL2 (if on Windows) or Linux environment

<!-- section_id: "816611d4-57a4-4ae0-9769-373b80e630a1" -->
## Key Differences from Playwright MCP

| Feature | Playwright MCP | Chrome DevTools MCP |
|---------|---------------|---------------------|
| Browser | Playwright Chromium (auto-installed) | System Google Chrome (manual install) |
| Installation | `npx playwright install chromium` | Install Chrome via system package manager |
| Use Case | Cross-browser testing, general automation | Chrome-specific debugging, performance analysis |
| Stability | Very stable | May have connection issues (see Troubleshooting) |

<!-- section_id: "69eb3754-7276-4c69-8e71-3633e4b4b673" -->
## Setup Steps

<!-- section_id: "1679b6bd-5f4d-4a5f-97c2-85f7e36f315d" -->
### 1. Install Google Chrome (System Installation)

**On Ubuntu/WSL2:**
```bash
# Download Chrome .deb package
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install Chrome
sudo apt install ./google-chrome-stable_current_amd64.deb

# Verify installation
google-chrome --version
```

**On other Linux distributions:**
- Follow Google's official installation guide: https://www.google.com/chrome/

**⚠️ Important:** Chrome DevTools MCP requires the actual Google Chrome browser, not Playwright's Chromium. Installing Chromium via Playwright (`npx playwright install chromium`) will NOT work for Chrome DevTools MCP.

<!-- section_id: "dcb20720-564c-4998-beda-6ddf19a9fb4d" -->
### 2. Create MCP Configuration

Create or edit `.mcp.json` in your project root:

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--logFile",
        "/tmp/mcp-chrome.log"
      ]
    }
  }
}
```

**Configuration Notes:**
- `--logFile` (optional): Logs Chrome DevTools MCP activity to a file for debugging
- **Do NOT** include `--browserUrl` unless Chrome is already running with remote debugging
- Without `--browserUrl`, Chrome DevTools MCP will auto-launch Chrome when needed

<!-- section_id: "1554b961-dd0d-4c75-b997-56df642bfb8c" -->
### 3. Verify Chrome Installation

Check that Chrome is accessible:

```bash
# Check if Chrome is in PATH
which google-chrome

# Check Chrome version
google-chrome --version

# Check if Chrome executable exists
ls -la /opt/google/chrome/chrome
```

<!-- section_id: "33033edb-53a1-457a-a4d7-52c71234746f" -->
### 4. Restart Claude Code

After configuration:
1. Close Claude Code completely
2. Restart Claude Code
3. The Chrome DevTools MCP server should now be available

<!-- section_id: "98ac4de7-512a-42f5-8aec-17d2b7889a73" -->
## Troubleshooting

<!-- section_id: "301a59a5-2d03-4844-b387-53d25522d15e" -->
### Issue: "Chrome not found" or "Chrome executable not found"

**Error message:**
```
Error: Chrome not found at /opt/google/chrome/chrome
google-chrome: command not found
```

**Common cause:** Chrome is not installed on the system.

**Diagnosis:**
1. Check if Chrome is installed:
   ```bash
   google-chrome --version
   which google-chrome
   dpkg -l | grep -i chrome
   ```

2. If all commands return "not found", Chrome is not installed.

**Solution:**
1. Install Chrome (see Step 1 above):
   ```bash
   cd /tmp
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo apt install ./google-chrome-stable_current_amd64.deb
   ```

2. Verify installation:
   ```bash
   google-chrome --version
   ```

3. If Chrome is installed but not found, check the installation path:
   ```bash
   which google-chrome
   ls -la /opt/google/chrome/chrome
   ```

4. Create a symlink if Chrome is installed elsewhere:
   ```bash
   # Find Chrome location
   find /usr -name "google-chrome" 2>/dev/null
   
   # Create symlink if needed
   sudo mkdir -p /opt/google/chrome
   sudo ln -s $(which google-chrome) /opt/google/chrome/chrome
   ```

<!-- section_id: "7315ef17-14ed-410f-bbaa-4d0355bd5777" -->
### Issue: Chrome DevTools MCP closes immediately or disconnects

**Symptom:** The MCP server connects but then immediately closes or disconnects.

**Known Issue:** Chrome DevTools MCP has been reported to have stability issues in some environments.

**Solutions:**
1. **Use Playwright MCP instead** (recommended for most use cases):
   - Playwright MCP is more stable and works with Chromium
   - Configure: `"--browser", "chromium"` in Playwright MCP config
   - See `playwright-mcp-setup.md` for details

2. **Check Chrome version compatibility:**
   ```bash
   google-chrome --version
   ```
   - Ensure you have a recent stable version
   - Update Chrome if using an old version

3. **Check system dependencies:**
   ```bash
   # Install required libraries (same as Playwright)
   sudo apt-get install -y --no-install-recommends \
     libasound2t64 libatk-bridge2.0-0t64 libatk1.0-0t64 libatspi2.0-0t64 \
     libcairo2 libcups2t64 libdbus-1-3 libdrm2 libgbm1 libglib2.0-0t64 \
     libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 \
     libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 xvfb
   ```

4. **Try running Chrome in headless mode manually:**
   ```bash
   google-chrome --headless --remote-debugging-port=9222
   ```
   If this fails, Chrome may not be properly configured for headless operation.

<!-- section_id: "9b3a5220-d9d3-4283-ac3a-9f61b5038e59" -->
### Issue: "Cannot connect to Chrome DevTools"

**Error message:**
```
Error: Cannot connect to Chrome DevTools Protocol
```

**Solution:**
1. Ensure Chrome is running or can be launched
2. Check if port 9222 (default DevTools port) is available:
   ```bash
   netstat -tuln | grep 9222
   ```
3. Try specifying a different port in Chrome DevTools MCP configuration (if supported)

<!-- section_id: "a6c1692d-046c-4cf5-b87c-b1b502b91d3d" -->
### Issue: Chrome DevTools MCP connects but cannot use Chrome

**Symptom:** Chrome DevTools MCP server starts and connects to MCP protocol, but operations fail or Chrome DevTools port (9222) is not active.

**Diagnosis:**
1. Check if Chrome is running:
   ```bash
   ps aux | grep -i chrome | grep -v grep
   ```

2. Check if port 9222 is in use:
   ```bash
   netstat -tuln | grep 9222
   ```

3. Check Chrome DevTools MCP logs:
   ```bash
   tail -50 /tmp/mcp-chrome.log
   ```

**Common causes:**
- Chrome is not installed (see "Chrome not found" issue above)
- Configuration has `--browserUrl` pointing to non-existent Chrome instance
- Chrome DevTools MCP cannot auto-launch Chrome

**Solution:**
1. **Remove `--browserUrl` from configuration** to allow auto-launch:
   ```json
   {
     "chrome-devtools": {
       "command": "npx",
       "args": ["-y", "chrome-devtools-mcp@latest"]
       // Remove --browserUrl to let it auto-launch Chrome
     }
   }
   ```

2. **Or** manually start Chrome with remote debugging:
   ```bash
   google-chrome --remote-debugging-port=9222 --headless &
   ```

3. Verify Chrome is accessible:
   ```bash
   google-chrome --version
   ```

<!-- section_id: "f9146d49-8b89-4c6a-9598-9e90e04b2189" -->
### Issue: Chrome DevTools MCP not available in Claude Code

**Possible causes:**
1. Claude Code needs to be restarted after configuration changes
2. Invalid configuration in `.mcp.json` (check JSON syntax)
3. Chrome not properly installed
4. Multiple Chrome DevTools MCP processes running (indicates connection issues)

**Solution:**
1. Verify `.mcp.json` syntax is correct
2. Check for multiple Chrome DevTools MCP processes:
   ```bash
   ps aux | grep chrome-devtools-mcp | grep -v grep
   ```
   If many processes are running, Chrome may not be installed or accessible.

3. Completely restart Claude Code
4. Check Claude Code logs for MCP server startup errors
5. Verify Chrome installation (see Step 3 above)
6. Check Chrome DevTools MCP logs: `tail -50 /tmp/mcp-chrome.log`

<!-- section_id: "4e21117b-aee0-48e1-ab9d-42f8250e8348" -->
## When to Use Chrome DevTools MCP vs Playwright MCP

<!-- section_id: "3ab8ba18-1ec7-40a1-99fa-4f921d406c42" -->
### Use Chrome DevTools MCP when:
- You need Chrome-specific debugging features
- You require performance analysis tools
- You're debugging Chrome-specific issues
- You need access to Chrome DevTools Protocol directly

<!-- section_id: "cbc9d32a-962a-4673-998a-b5ebd69b5cbf" -->
### Use Playwright MCP when:
- You need cross-browser testing
- You want more stable automation
- You don't need Chrome-specific features
- You prefer not to install system Chrome
- **Recommended for most use cases**

<!-- section_id: "6b224a79-b207-4f89-b596-b83174257fa7" -->
## Alternative: Use Playwright MCP with Chromium

If Chrome DevTools MCP is causing issues, consider using Playwright MCP instead:

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

Then install Chromium:
```bash
npx -y playwright@latest install chromium
```

See `playwright-mcp-setup.md` for complete Playwright MCP setup instructions.

<!-- section_id: "ab9866de-6f02-4cab-8e1d-4d33ec079689" -->
## Files Modified

- `.mcp.json` - MCP server configuration
- System Chrome installation (via package manager)

<!-- section_id: "3c772431-5c86-436d-beec-03c20b6c8940" -->
## Next Steps

After setup is complete:
- Test Chrome DevTools MCP functionality
- If experiencing stability issues, consider switching to Playwright MCP
- See browser automation documentation for usage examples

---

**Note:** Chrome DevTools MCP has been reported to have stability issues in some environments. If you encounter persistent connection problems, we recommend using Playwright MCP with Chromium instead, which is more stable and provides similar functionality for most use cases.

