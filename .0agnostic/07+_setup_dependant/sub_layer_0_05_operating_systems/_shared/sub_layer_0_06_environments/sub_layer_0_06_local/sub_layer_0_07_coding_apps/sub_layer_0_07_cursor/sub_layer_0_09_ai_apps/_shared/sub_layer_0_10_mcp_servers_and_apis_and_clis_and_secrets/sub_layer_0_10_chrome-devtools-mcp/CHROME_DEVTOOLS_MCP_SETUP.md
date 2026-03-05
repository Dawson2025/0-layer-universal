---
resource_id: "cbca7fe7-ae9d-4184-80c5-b0efc4ab04aa"
resource_type: "document"
resource_name: "CHROME_DEVTOOLS_MCP_SETUP"
---
# Chrome DevTools MCP Server Setup Guide

This guide documents the setup process for the Chrome DevTools MCP (Model Context Protocol) server for use with Claude Code.

<!-- section_id: "3781747c-4985-419a-b4ef-ad4b3db01ac8" -->
## Overview

The Chrome DevTools MCP server provides Chrome-specific debugging and automation capabilities. **Unlike Playwright MCP**, this server requires **actual Google Chrome** to be installed on your system, not just Playwright's Chromium.

<!-- section_id: "a266152c-ba88-40ca-8a8e-19866202aa20" -->
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

<!-- section_id: "a709207f-0ce0-4ddf-83b5-1fea15e3a781" -->
## Prerequisites

- **Node.js and npm** installed
- **Google Chrome** installed on your system (not just Playwright Chromium)
- Claude Code installed
- WSL2 (if on Windows) or Linux environment

<!-- section_id: "c7788547-3079-49f4-babe-fcb5fb307060" -->
## Key Differences from Playwright MCP

| Feature | Playwright MCP | Chrome DevTools MCP |
|---------|---------------|---------------------|
| Browser | Playwright Chromium (auto-installed) | System Google Chrome (manual install) |
| Installation | `npx playwright install chromium` | Install Chrome via system package manager |
| Use Case | Cross-browser testing, general automation | Chrome-specific debugging, performance analysis |
| Stability | Very stable | May have connection issues (see Troubleshooting) |

<!-- section_id: "ac5cd333-587a-4cc3-b1be-f0a32b89a871" -->
## Setup Steps

<!-- section_id: "dca62b29-b9e6-4057-92de-238bc2452e5d" -->
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

<!-- section_id: "85b03425-95e6-44a1-971c-b5593b47bbe1" -->
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

<!-- section_id: "b37d055d-3007-40b7-acb5-244cade40990" -->
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

<!-- section_id: "534b2f14-b68d-4c95-9f20-0e456b4709a0" -->
### 4. Restart Claude Code

After configuration:
1. Close Claude Code completely
2. Restart Claude Code
3. The Chrome DevTools MCP server should now be available

<!-- section_id: "6b763028-2c89-44d3-abfc-82ae9d6bc03c" -->
## Troubleshooting

<!-- section_id: "e838be6a-53d3-4264-8453-7bb081508034" -->
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

<!-- section_id: "c1a9379e-1504-471f-bfe2-b4e48fa46230" -->
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

<!-- section_id: "41ce5e99-4c47-40de-98f9-1035f360e031" -->
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

<!-- section_id: "06ad9be0-088d-4c5e-804b-bde9d626d2b3" -->
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

<!-- section_id: "247b784b-cfa3-4d29-b5b7-b0ea065c411e" -->
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

<!-- section_id: "c36d232e-fd02-4b7d-9b5a-4007a65872e7" -->
## When to Use Chrome DevTools MCP vs Playwright MCP

<!-- section_id: "faf424e4-b26e-45ee-a681-4f52ce5ce59e" -->
### Use Chrome DevTools MCP when:
- You need Chrome-specific debugging features
- You require performance analysis tools
- You're debugging Chrome-specific issues
- You need access to Chrome DevTools Protocol directly

<!-- section_id: "3cd6697d-7c8c-4176-8637-96d1bf40e314" -->
### Use Playwright MCP when:
- You need cross-browser testing
- You want more stable automation
- You don't need Chrome-specific features
- You prefer not to install system Chrome
- **Recommended for most use cases**

<!-- section_id: "c2da84a0-c483-497d-aff5-3827e1f8a891" -->
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

<!-- section_id: "48d9026b-c612-4345-bab0-64c9d936cd9c" -->
## Files Modified

- `.mcp.json` - MCP server configuration
- System Chrome installation (via package manager)

<!-- section_id: "4ef0d0ed-94f3-4ccb-95fa-ff307f57463c" -->
## Next Steps

After setup is complete:
- Test Chrome DevTools MCP functionality
- If experiencing stability issues, consider switching to Playwright MCP
- See browser automation documentation for usage examples

---

**Note:** Chrome DevTools MCP has been reported to have stability issues in some environments. If you encounter persistent connection problems, we recommend using Playwright MCP with Chromium instead, which is more stable and provides similar functionality for most use cases.

