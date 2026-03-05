---
resource_id: "fc6ac745-95dc-4416-8828-8edca8923f10"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_CURSOR_SETUP"
---
# Playwright MCP Server Setup for Cursor IDE

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working and tested (Linux/Ubuntu), ✅ Working (WSL)

Complete guide for setting up the Playwright MCP (Model Context Protocol) server in Cursor IDE on Ubuntu Linux systems, including WSL environments.

<!-- section_id: "fa93d4a6-5ebd-466e-b8a0-a5b1ead1258b" -->
## Prerequisites

- Ubuntu 24.04 (Noble) or later (native or WSL2)
- Administrator (sudo) access
- Internet connection
- Cursor IDE installed

<!-- section_id: "4f4fda87-4f10-4809-b402-bd9bf8478943" -->
## Overview

This guide documents the setup process for Playwright MCP server in Cursor IDE on Ubuntu Linux (native and WSL). The MCP server enables browser automation capabilities directly within Cursor, allowing AI agents to interact with web browsers for testing, automation, and web scraping tasks.

**Platforms Covered**:
- ✅ Native Linux/Ubuntu
- ✅ WSL2 (Ubuntu 24.04) on Windows 11

<!-- section_id: "8da63f63-cd70-44fc-8443-9b0dde0115c9" -->
## Setup Steps

<!-- section_id: "fc1e36f8-d374-40b6-9239-f967521c8ab5" -->
### Step 1: Install Node.js via NVM

Playwright MCP requires Node.js (v16+). We'll install it using nvm (Node Version Manager) for better version management.

```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash

# Load nvm in current session
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Install Node.js 22 (LTS)
nvm install 22
nvm use 22

# Verify installation
node --version
npx --version
```

**Note**: NVM automatically adds itself to `~/.bashrc`, so Node.js will be available in future terminal sessions.

<!-- section_id: "77a1d338-bd52-45f3-afeb-39facf3e0e66" -->
### Step 2: Install Playwright System Dependencies

Playwright requires various system libraries to run browsers. Install them with:

```bash
sudo apt-get update

sudo apt-get install -y --no-install-recommends \
  libasound2t64 libatk-bridge2.0-0t64 libatk1.0-0t64 libatspi2.0-0t64 \
  libcairo2 libcups2t64 libdbus-1-3 libdrm2 libgbm1 libglib2.0-0t64 \
  libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 \
  libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 xvfb \
  fonts-noto-color-emoji fonts-unifont libfontconfig1 libfreetype6 \
  xfonts-cyrillic xfonts-scalable fonts-liberation fonts-ipafont-gothic \
  fonts-wqy-zenhei fonts-tlwg-loma-otf fonts-freefont-ttf
```

**Installation Size**: ~50-100 MB of system dependencies

**WSL Note**: These dependencies work the same in WSL as in native Linux. X11 forwarding may be required for GUI applications.

<!-- section_id: "c88230ab-ccb7-4c5f-8185-5c73705935b2" -->
### Step 3: Install Playwright Chromium Browser

**⚠️ CRITICAL: Use Node.js Playwright, NOT Python Playwright**

The MCP server uses **Node.js Playwright** (`npx playwright`), which is different from Python Playwright (`python3 -m playwright`). They install browsers to different locations.

**✅ CORRECT (for MCP servers):**
```bash
# Load nvm first
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Install Chromium using Node.js Playwright
npx -y playwright@latest install chromium
```

**❌ WRONG (will NOT work with MCP servers):**
```bash
# Don't use Python Playwright
python3 -m playwright install chromium  # Don't use this!
```

**Why this matters:**
- Python Playwright installs browsers that the MCP server cannot find
- The MCP server expects browsers installed via Node.js Playwright
- Using Python Playwright will cause "Browser not installed" errors even after installation

**Installation Details:**
- Chromium: ~164.7 MB
- FFMPEG: ~2.3 MB
- Chromium Headless Shell: ~109.7 MB
- **Total**: ~280 MB
- **Installation Location**: `~/.cache/ms-playwright/`

**Installation takes 5-10 minutes** depending on your internet connection.

<!-- section_id: "457f3727-c0e1-4c97-aa97-f4441ebe011f" -->
### Step 4: Configure Cursor MCP Settings

Cursor uses a global MCP configuration file located at `~/.cursor/mcp.json` (which is symlinked from `~/.config/mcp/mcp.json`).

Create or update this file with the following configuration:

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

**Configuration Notes:**
- `"command": "npx"` - Uses npx to run the Playwright MCP server
- `"-y"` - Automatically confirms package installation
- `"@playwright/mcp@latest"` - Always uses the latest version
- `"--browser", "chromium"` - Specifies Chromium as the browser (recommended)
- `"PLAYWRIGHT_BROWSERS_PATH": "0"` - Uses default browser cache location

**File Locations**:
- Primary: `~/.config/mcp/mcp.json`
- Symlink: `~/.cursor/mcp.json` → `~/.config/mcp/mcp.json`

**WSL Note**: The configuration is the same for WSL and native Linux. Playwright MCP works well in WSL environments.

<!-- section_id: "1b77adf7-5034-4994-bb2e-93939e5fd36d" -->
### Step 5: Restart Cursor

After completing the setup:

1. **Completely close Cursor** (not just the window, ensure all processes are terminated)
2. **Restart Cursor IDE**
3. The Playwright MCP server should now be available

<!-- section_id: "83073585-cda6-451b-80b0-803cfb494f73" -->
## Verification

<!-- section_id: "ecbf978b-b2bb-451b-abd6-343eadaebce9" -->
### Check 1: Verify Browser Installation

```bash
ls -la ~/.cache/ms-playwright/
```

You should see directories like:
- `chromium-1200` (version number may vary)
- `chromium_headless_shell-1200`
- `ffmpeg-1011`

<!-- section_id: "435ca308-55e8-497a-852b-6294bb415e8d" -->
### Check 2: Verify MCP Configuration

```bash
cat ~/.config/mcp/mcp.json
# or
cat ~/.cursor/mcp.json
```

Should show the Playwright MCP configuration.

<!-- section_id: "c56d9f5c-c587-4123-a7ed-cef7da1a229d" -->
### Check 3: Test MCP Server Command

```bash
# Load nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Test the MCP server command
npx -y @playwright/mcp@latest --browser chromium --help
```

Should display help text without errors.

<!-- section_id: "9f072eeb-98d0-40fd-8e74-1938f42e46a3" -->
### Check 4: Verify in Cursor

After restarting Cursor:
- Playwright MCP tools should be available
- Check Cursor Settings → Tools & MCP → Installed MCP Servers
- Should show "playwright" with "22 tools enabled"
- You can ask Cursor to navigate to websites and it should work

<!-- section_id: "328667c6-4792-45e3-a873-f19e609b0483" -->
## WSL (Windows Subsystem for Linux) Setup

**Last Updated**: 2025-12-05  
**Environment**: WSL2 (Ubuntu 24.04) on Windows 11, Lenovo Yoga 9 Pro  
**Status**: ✅ Working

<!-- section_id: "0003844c-ffa9-4a4a-9ca4-6a493f914ffd" -->
### WSL-Specific Configuration

Playwright MCP works well in WSL environments. The setup process is identical to native Linux, with a few considerations:

**Key Points**:
- Playwright MCP runs entirely within WSL
- Browser binaries are installed in WSL: `~/.cache/ms-playwright/`
- No need to use Windows Chrome paths (unlike cursor-browser-extension)
- X11 forwarding may be required for GUI applications (headless mode works without it)

<!-- section_id: "0681f28d-3b74-4e4f-a58e-c4645b2fde2a" -->
### WSL Setup Process

The setup steps are the same as native Linux:

1. ✅ Install Node.js via NVM (same commands)
2. ✅ Install system dependencies (same commands)
3. ✅ Install Playwright Chromium (same commands)
4. ✅ Configure MCP settings (same configuration)
5. ✅ Restart Cursor

<!-- section_id: "8b7eef64-cb79-4256-88de-842021874c4a" -->
### WSL Verification

**Check Display Configuration** (for GUI mode):
```bash
# Verify X11 forwarding
echo $DISPLAY
# Should output: :0 or similar

# Check if GUI apps can run
which xeyes || echo "X11 apps not available"
```

**Note**: Playwright can run in headless mode without X11, so GUI forwarding is optional.

<!-- section_id: "553aa0ff-4df3-41a8-aa4d-f55785fb2757" -->
### WSL Advantages

- **Isolated Environment**: Playwright runs entirely in WSL, separate from Windows
- **Consistent Behavior**: Same behavior as native Linux
- **No Path Issues**: Unlike cursor-browser-extension, Playwright MCP doesn't need Windows paths
- **Easy Setup**: Same configuration as native Linux

<!-- section_id: "01dd2536-94f4-41f0-bc07-7a298f71cff4" -->
### WSL Troubleshooting

If Playwright MCP doesn't work in WSL:

1. **Verify Node.js is accessible**:
   ```bash
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   which node
   which npx
   ```

2. **Check browser installation**:
   ```bash
   ls -la ~/.cache/ms-playwright/
   ```

3. **Verify MCP configuration**:
   ```bash
   cat ~/.config/mcp/mcp.json | python3 -m json.tool
   ```

4. **Check Cursor logs** for MCP server errors

<!-- section_id: "42071858-afc0-47eb-a66b-584c786c91ee" -->
## Troubleshooting

<!-- section_id: "3a150054-cd11-48e7-9aac-688e7635af23" -->
### Issue: "Browser specified in your config is not installed"

**Error message:**
```
Error: Browser specified in your config is not installed. Either install it (likely) or change the config.
```

**Common cause:** You installed browsers using Python Playwright instead of Node.js Playwright.

**Solution:**
1. Check which browsers are installed:
   ```bash
   ls -la ~/.cache/ms-playwright/ | grep chromium
   ```

2. If you see multiple chromium directories with different version numbers, you likely have both Python and Node.js installations.

3. Remove Python-installed browsers (they use different version numbers):
   ```bash
   # Check which is the Node.js version (usually the newest)
   # Then remove the Python-installed ones
   rm -rf ~/.cache/ms-playwright/chromium-<python-version>
   ```

4. Install using Node.js Playwright (the correct method):
   ```bash
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   npx -y playwright@latest install chromium
   ```

5. Restart Cursor completely.

**Prevention:** Always use `npx -y playwright@latest install chromium` for MCP servers, never `python3 -m playwright install chromium`.

<!-- section_id: "9ff6aa8c-09d7-4723-bdfd-ee5fd283b149" -->
### Issue: "npx: command not found" or Node.js not found

**Cause:** Cursor can't find Node.js/npx in its environment.

**Solution:**
1. Ensure Node.js is installed via nvm:
   ```bash
   export NVM_DIR="$HOME/.nvm"
   [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
   node --version
   ```

2. Verify nvm is in your `~/.bashrc`:
   ```bash
   grep -q "NVM_DIR" ~/.bashrc && echo "NVM configured" || echo "NVM not in .bashrc"
   ```

3. If Cursor still can't find Node.js:
   - Launch Cursor from a terminal where nvm is loaded
   - Or add Node.js to system PATH (not recommended, nvm is better)

**WSL Note**: Same solution applies in WSL. Node.js must be accessible from within WSL.

<!-- section_id: "cab49002-ca34-4a5c-8650-fedef820e290" -->
### Issue: MCP tools not available in Cursor

**Possible causes:**
1. Cursor needs to be restarted after configuration changes
2. Invalid configuration in `~/.config/mcp/mcp.json` (check JSON syntax)
3. Node.js not available in Cursor's environment

**Solution:**
1. Verify `~/.config/mcp/mcp.json` syntax is correct:
   ```bash
   cat ~/.config/mcp/mcp.json | python3 -m json.tool
   ```

2. Completely restart Cursor (close all windows, ensure processes are terminated)

3. Check Cursor logs for MCP server startup errors:
   ```bash
   find ~/.cursor-server/data/logs -name "*playwright*" -type f | head -1 | xargs tail -30
   ```

4. Verify Node.js is accessible:
   ```bash
   which node
   which npx
   ```

<!-- section_id: "8663d3da-f9be-4ab9-a9d2-1c5c25454ac0" -->
### Issue: "Active lockfile found"

**Error message:**
```
An active lockfile is found at: /home/dawson/.cache/ms-playwright/__dirlock
```

**Solution:** Remove the lockfile and reinstall:
```bash
rm -rf ~/.cache/ms-playwright/__dirlock
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
npx -y playwright@latest install chromium
```

<!-- section_id: "1f4fcea4-02ab-4537-9e45-d2950f668941" -->
### Issue: Browser installation command hangs

**Solution:** The installation may be downloading in the background. Wait 5-10 minutes for it to complete. If it truly hangs:
1. Cancel with Ctrl+C
2. Remove the lockfile (see above)
3. Try again

<!-- section_id: "b9c7d5f2-1251-45c4-93ef-3e822e1d5541" -->
## Browser Options

While this guide uses Chromium (recommended), Playwright supports other browsers:

- **chromium** (recommended) - Most reliable, fully tested, automatically installed via Playwright
- **chrome** - Google Chrome (requires system Chrome installation + Playwright Chrome channel)
- **firefox** - Mozilla Firefox
- **webkit** - Safari's engine
- **msedge** - Microsoft Edge

To use a different browser:
1. Install it: `npx -y playwright@latest install <browser-name>`
2. Update `~/.config/mcp/mcp.json` args to specify: `"--browser", "<browser-name>"`
3. Restart Cursor

<!-- section_id: "93deb51e-106a-48db-8f2c-f620d0008e59" -->
## What Gets Installed

<!-- section_id: "449f25a5-c6ec-4d7b-a183-36af5d67531d" -->
### System Dependencies (via apt-get)
- Audio libraries (libasound2t64)
- Accessibility libraries (libatk, libatspi)
- Graphics libraries (libcairo2, libdrm2, libgbm1)
- Font libraries and fonts
- X11 display libraries
- Virtual framebuffer (xvfb) for headless mode

<!-- section_id: "25c53efb-2e39-4405-a4ff-16fd2f6603db" -->
### Browser Binaries (via Playwright)
- Installed to: `~/.cache/ms-playwright/`
- Chromium: ~164.7 MB
- FFMPEG: ~2.3 MB
- Chromium Headless Shell: ~109.7 MB

<!-- section_id: "9c466fdb-df68-417a-840b-472e97793925" -->
### Total Download Size
- System dependencies: ~50-100 MB (varies)
- Browser binaries: ~280 MB
- **Total: ~330-380 MB**

<!-- section_id: "d787fc4c-8c6f-49dd-972b-5d1c6ea25625" -->
## Files Modified

- `~/.config/mcp/mcp.json` - Cursor MCP server configuration (primary location)
- `~/.cursor/mcp.json` - Symlink to above (for compatibility)
- `~/.cache/ms-playwright/` - Browser binaries installed here
- `~/.bashrc` - NVM configuration added (if not already present)
- `~/.nvm/` - Node.js installation via nvm

<!-- section_id: "0a579d5b-04f8-45d9-84d9-dac1d334a379" -->
## Usage in Cursor

Once configured, you can ask Cursor to:

```
"Navigate to https://example.com and take a screenshot"

"Test the login flow by navigating to localhost:5000/login and entering credentials"

"Check if the word creation form has proper accessibility labels"

"Scrape the phoneme display table and verify all entries are present"
```

Cursor will use the Playwright MCP tools automatically to interact with browsers.

<!-- section_id: "e12e25f1-9ea9-4078-a9ec-acf55785a311" -->
## Key Differences: Cursor vs Claude Code

- **Cursor**: Uses global config at `~/.config/mcp/mcp.json` (symlinked to `~/.cursor/mcp.json`)
- **Claude Code**: Uses project-level `.mcp.json` in project root
- **Both**: Use the same MCP server command format
- **Both**: Require Node.js Playwright (not Python Playwright)

<!-- section_id: "f67d4d35-635e-4625-9c91-e4a9616b71b9" -->
## Environment-Specific Notes

<!-- section_id: "2a1a08fc-2f92-40aa-afae-e610fe7f9b17" -->
### Ubuntu 24.04 (Noble) - Native Linux
- Tested and verified on Ubuntu 24.04.3 LTS
- All system dependencies available in default repositories
- NVM installation works without issues
- Playwright browsers install successfully

<!-- section_id: "e56c9cb0-b4d0-4a8a-83cc-dd8eb3b84628" -->
### WSL2 (Ubuntu 24.04) on Windows 11
- Tested on WSL2 (Ubuntu 24.04) on Windows 11, Lenovo Yoga 9 Pro
- Same setup process as native Linux
- Playwright runs entirely within WSL
- No Windows path configuration needed
- X11 forwarding optional (headless mode works without it)

<!-- section_id: "2cbf384e-36c7-499f-8e8e-f0ed3b0d306d" -->
### Lenovo Yoga Pro 9
- Tested on Lenovo Yoga Pro 9 running Ubuntu 24.04 (native and WSL)
- No hardware-specific issues encountered
- All dependencies install correctly

<!-- section_id: "b8554990-f2bf-4f1e-af81-66046d609e2a" -->
## Related Documentation

- [Cursor Browser MCP Setup](./CURSOR_BROWSER_MCP_SETUP.md) - Browser automation setup (includes WSL notes)
- [Playwright MCP Testing](./PLAYWRIGHT_MCP_TESTING.md) - Testing documentation
- [MCP Configuration Guide](./MCP_CONFIGURATION_GUIDE.md) - General MCP configuration
- [MCP System Guide](./MCP_SYSTEM_GUIDE.md) - Complete MCP system overview

---

**Last Updated**: 2025-12-05  
**Environment**: Ubuntu 24.04.3 LTS (Noble Numbat), WSL2 (Ubuntu 24.04) on Windows 11  
**Hardware**: Lenovo Yoga Pro 9  
**Node.js Version**: 22.21.1 (via nvm)  
**Playwright Version**: Latest (via @playwright/mcp@latest)  
**Cursor Version**: Latest

