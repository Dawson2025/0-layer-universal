---
resource_id: "92f25b04-e900-4ab7-b6f3-030338b1bd51"
resource_type: "document"
resource_name: "CHROME_DEVTOOLS_MCP_SETUP"
---
# Chrome DevTools MCP Server Setup Guide

This guide documents the setup process for the Chrome DevTools MCP (Model Context Protocol) server for use with Claude Code.

<!-- section_id: "f21c4c42-a477-495c-82dd-d30f2701ed0b" -->
## Overview

The Chrome DevTools MCP server provides Chrome-specific debugging and automation capabilities. **Unlike Playwright MCP**, this server requires **actual Google Chrome** to be installed on your system, not just Playwright's Chromium.

<!-- section_id: "bfe281b1-31e3-4a6b-82a2-db8fc3d02b8b" -->
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

<!-- section_id: "1ce4eac0-b3c8-477f-8c0f-a73cd3fc2475" -->
## Prerequisites

- **Node.js and npm** installed
- **Google Chrome** installed on your system (not just Playwright Chromium)
- Claude Code installed
- WSL2 (if on Windows) or Linux environment

<!-- section_id: "21f20a7a-c805-41c8-bbc9-645e89413e31" -->
## Key Differences from Playwright MCP

| Feature | Playwright MCP | Chrome DevTools MCP |
|---------|---------------|---------------------|
| Browser | Playwright Chromium (auto-installed) | System Google Chrome (manual install) |
| Installation | `npx playwright install chromium` | Install Chrome via system package manager |
| Use Case | Cross-browser testing, general automation | Chrome-specific debugging, performance analysis |
| Stability | Very stable | May have connection issues (see Troubleshooting) |

<!-- section_id: "11fdbe83-fb34-4c12-845a-6da83ae0a3e6" -->
## Setup Steps

<!-- section_id: "487f463a-78eb-4d37-8ebc-3f5d091c426c" -->
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

<!-- section_id: "3dfe4138-b57b-4bc7-9396-b71d4041419a" -->
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

<!-- section_id: "c0a94c0e-2f85-4267-925e-fe42ded5f6a7" -->
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

<!-- section_id: "0291dfa8-6fc5-4b7a-a6bc-8ad17ce100f1" -->
### 4. Restart Claude Code

After configuration:
1. Close Claude Code completely
2. Restart Claude Code
3. The Chrome DevTools MCP server should now be available

<!-- section_id: "3052eb87-9cd0-4e27-ab0f-2df565147892" -->
## Troubleshooting

<!-- section_id: "6ddd0393-d030-4b1e-ba0f-9dc7d80ebca7" -->
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

<!-- section_id: "7624df2b-96bb-4790-b86c-a36fc939c301" -->
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

<!-- section_id: "4e5826b1-68e7-49f1-8d81-96071b80c712" -->
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

<!-- section_id: "cf964ec6-5ed9-4e2e-8fba-bc2d04337417" -->
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

<!-- section_id: "357d284c-faf1-464b-98f8-467dd05ff2df" -->
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

<!-- section_id: "69f30885-4161-406e-9135-e2eb630d8ce7" -->
## When to Use Chrome DevTools MCP vs Playwright MCP

<!-- section_id: "30cf726a-28e6-44ff-903a-3d2dd3507504" -->
### Use Chrome DevTools MCP when:
- You need Chrome-specific debugging features
- You require performance analysis tools
- You're debugging Chrome-specific issues
- You need access to Chrome DevTools Protocol directly

<!-- section_id: "708340c4-f4ea-40b6-9456-abc65e773fc6" -->
### Use Playwright MCP when:
- You need cross-browser testing
- You want more stable automation
- You don't need Chrome-specific features
- You prefer not to install system Chrome
- **Recommended for most use cases**

<!-- section_id: "56901107-432f-4344-ab80-bfb1dc9c6379" -->
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

<!-- section_id: "9d426217-2439-467a-b163-41f3a18a1a0d" -->
## Files Modified

- `.mcp.json` - MCP server configuration
- System Chrome installation (via package manager)

<!-- section_id: "f0b3b397-d012-4acd-bd34-2de3779eceec" -->
## Next Steps

After setup is complete:
- Test Chrome DevTools MCP functionality
- If experiencing stability issues, consider switching to Playwright MCP
- See browser automation documentation for usage examples

---

**Note:** Chrome DevTools MCP has been reported to have stability issues in some environments. If you encounter persistent connection problems, we recommend using Playwright MCP with Chromium instead, which is more stable and provides similar functionality for most use cases.

