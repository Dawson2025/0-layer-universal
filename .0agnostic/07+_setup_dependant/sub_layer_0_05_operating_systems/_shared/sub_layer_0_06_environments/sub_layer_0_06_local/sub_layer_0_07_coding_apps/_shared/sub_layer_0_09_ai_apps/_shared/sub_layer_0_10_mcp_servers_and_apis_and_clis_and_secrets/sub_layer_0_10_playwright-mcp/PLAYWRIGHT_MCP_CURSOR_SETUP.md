---
resource_id: "18c61b38-5ef3-49a0-a91a-0740b1d5f593"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_CURSOR_SETUP"
---
# Playwright MCP Server Setup for Cursor IDE

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working and tested (Linux/Ubuntu), ✅ Working (WSL)

Complete guide for setting up the Playwright MCP (Model Context Protocol) server in Cursor IDE on Ubuntu Linux systems, including WSL environments.

<!-- section_id: "1d4b88fc-3155-4318-8055-f2247cd0bc8e" -->
## Prerequisites

- Ubuntu 24.04 (Noble) or later (native or WSL2)
- Administrator (sudo) access
- Internet connection
- Cursor IDE installed

<!-- section_id: "6cf32b57-b4c4-403d-9bbf-4fbfbc5bbace" -->
## Overview

This guide documents the setup process for Playwright MCP server in Cursor IDE on Ubuntu Linux (native and WSL). The MCP server enables browser automation capabilities directly within Cursor, allowing AI agents to interact with web browsers for testing, automation, and web scraping tasks.

**Platforms Covered**:
- ✅ Native Linux/Ubuntu
- ✅ WSL2 (Ubuntu 24.04) on Windows 11

<!-- section_id: "7de291c7-efd7-423a-8ec9-7aa014c886ee" -->
## Setup Steps

<!-- section_id: "91c7d34b-f5f2-4095-a0ff-2ba0c8ede68b" -->
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

<!-- section_id: "a970b7b6-e2f0-423a-bf78-2a75cbbbcd02" -->
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

<!-- section_id: "b5d6f30e-5077-4b82-b09e-e66ab153745c" -->
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

<!-- section_id: "d9d58c97-ba6f-46d9-bb2f-9c6e02ae16bf" -->
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

<!-- section_id: "021bd0ef-a31a-4593-8167-5a5030dbfc9f" -->
### Step 5: Restart Cursor

After completing the setup:

1. **Completely close Cursor** (not just the window, ensure all processes are terminated)
2. **Restart Cursor IDE**
3. The Playwright MCP server should now be available

<!-- section_id: "3da4fd5f-192c-4a31-9416-7cc76d2f193e" -->
## Verification

<!-- section_id: "64f125ee-251c-40a8-afb1-88304f45b141" -->
### Check 1: Verify Browser Installation

```bash
ls -la ~/.cache/ms-playwright/
```

You should see directories like:
- `chromium-1200` (version number may vary)
- `chromium_headless_shell-1200`
- `ffmpeg-1011`

<!-- section_id: "1643bcaf-cdfb-4c56-b0c3-9f12c4b6a633" -->
### Check 2: Verify MCP Configuration

```bash
cat ~/.config/mcp/mcp.json
# or
cat ~/.cursor/mcp.json
```

Should show the Playwright MCP configuration.

<!-- section_id: "aa6b451a-d6b6-4797-840b-94a96b767b98" -->
### Check 3: Test MCP Server Command

```bash
# Load nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Test the MCP server command
npx -y @playwright/mcp@latest --browser chromium --help
```

Should display help text without errors.

<!-- section_id: "f00d2275-57ee-4cca-9121-0bb1d48986e8" -->
### Check 4: Verify in Cursor

After restarting Cursor:
- Playwright MCP tools should be available
- Check Cursor Settings → Tools & MCP → Installed MCP Servers
- Should show "playwright" with "22 tools enabled"
- You can ask Cursor to navigate to websites and it should work

<!-- section_id: "d4a4dee2-35ef-4700-8b29-9779a4ed1c60" -->
## WSL (Windows Subsystem for Linux) Setup

**Last Updated**: 2025-12-05  
**Environment**: WSL2 (Ubuntu 24.04) on Windows 11, Lenovo Yoga 9 Pro  
**Status**: ✅ Working

<!-- section_id: "a53c22b1-5e77-487d-a23f-4be2193e0169" -->
### WSL-Specific Configuration

Playwright MCP works well in WSL environments. The setup process is identical to native Linux, with a few considerations:

**Key Points**:
- Playwright MCP runs entirely within WSL
- Browser binaries are installed in WSL: `~/.cache/ms-playwright/`
- No need to use Windows Chrome paths (unlike cursor-browser-extension)
- X11 forwarding may be required for GUI applications (headless mode works without it)

<!-- section_id: "011457b4-5d2b-4c0b-8071-07cadb4880b9" -->
### WSL Setup Process

The setup steps are the same as native Linux:

1. ✅ Install Node.js via NVM (same commands)
2. ✅ Install system dependencies (same commands)
3. ✅ Install Playwright Chromium (same commands)
4. ✅ Configure MCP settings (same configuration)
5. ✅ Restart Cursor

<!-- section_id: "1eddd13a-3610-4153-bde5-e51cb088cc72" -->
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

<!-- section_id: "09c7dd01-f2ad-40ca-b8e2-f2c78795f90a" -->
### WSL Advantages

- **Isolated Environment**: Playwright runs entirely in WSL, separate from Windows
- **Consistent Behavior**: Same behavior as native Linux
- **No Path Issues**: Unlike cursor-browser-extension, Playwright MCP doesn't need Windows paths
- **Easy Setup**: Same configuration as native Linux

<!-- section_id: "a1bf9e6a-f155-4c0e-a576-3cbcb38aa850" -->
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

<!-- section_id: "d1c31a39-011a-4fa4-ac87-6d448ff62297" -->
## Troubleshooting

<!-- section_id: "6088017b-37f4-451c-a1fb-0f4da1bcc9ff" -->
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

<!-- section_id: "f62c7c0f-b0e2-44c9-8f6c-12dbf1585550" -->
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

<!-- section_id: "bde37d77-73d9-492b-a75b-6cc7aec6d2cc" -->
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

<!-- section_id: "ea806c80-9b92-4056-9d79-3e1d01821486" -->
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

<!-- section_id: "7ff01d2a-386a-491f-a618-56c0b39235ab" -->
### Issue: Browser installation command hangs

**Solution:** The installation may be downloading in the background. Wait 5-10 minutes for it to complete. If it truly hangs:
1. Cancel with Ctrl+C
2. Remove the lockfile (see above)
3. Try again

<!-- section_id: "5dbcd4f3-cda3-4fac-af3d-ee65da8a1116" -->
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

<!-- section_id: "79253252-057c-4c10-978c-90e6ae856124" -->
## What Gets Installed

<!-- section_id: "3d161141-7642-4973-8ec4-e6fa4b8b2041" -->
### System Dependencies (via apt-get)
- Audio libraries (libasound2t64)
- Accessibility libraries (libatk, libatspi)
- Graphics libraries (libcairo2, libdrm2, libgbm1)
- Font libraries and fonts
- X11 display libraries
- Virtual framebuffer (xvfb) for headless mode

<!-- section_id: "7192470a-2f6e-4e3c-bae8-a1af3b7d1611" -->
### Browser Binaries (via Playwright)
- Installed to: `~/.cache/ms-playwright/`
- Chromium: ~164.7 MB
- FFMPEG: ~2.3 MB
- Chromium Headless Shell: ~109.7 MB

<!-- section_id: "54120311-931b-421f-8343-54e1805eb479" -->
### Total Download Size
- System dependencies: ~50-100 MB (varies)
- Browser binaries: ~280 MB
- **Total: ~330-380 MB**

<!-- section_id: "6dd60c16-0e92-4940-8c87-66eee61f945b" -->
## Files Modified

- `~/.config/mcp/mcp.json` - Cursor MCP server configuration (primary location)
- `~/.cursor/mcp.json` - Symlink to above (for compatibility)
- `~/.cache/ms-playwright/` - Browser binaries installed here
- `~/.bashrc` - NVM configuration added (if not already present)
- `~/.nvm/` - Node.js installation via nvm

<!-- section_id: "1e8d63be-4310-4363-800c-e316c8d59842" -->
## Usage in Cursor

Once configured, you can ask Cursor to:

```
"Navigate to https://example.com and take a screenshot"

"Test the login flow by navigating to localhost:5000/login and entering credentials"

"Check if the word creation form has proper accessibility labels"

"Scrape the phoneme display table and verify all entries are present"
```

Cursor will use the Playwright MCP tools automatically to interact with browsers.

<!-- section_id: "5d8eb14d-d603-49f7-b6e5-4257f4211e9b" -->
## Key Differences: Cursor vs Claude Code

- **Cursor**: Uses global config at `~/.config/mcp/mcp.json` (symlinked to `~/.cursor/mcp.json`)
- **Claude Code**: Uses project-level `.mcp.json` in project root
- **Both**: Use the same MCP server command format
- **Both**: Require Node.js Playwright (not Python Playwright)

<!-- section_id: "4a5455ce-92b3-4af9-845e-048448da83bd" -->
## Environment-Specific Notes

<!-- section_id: "2f4582b9-ff60-445b-9d52-ce2830300f32" -->
### Ubuntu 24.04 (Noble) - Native Linux
- Tested and verified on Ubuntu 24.04.3 LTS
- All system dependencies available in default repositories
- NVM installation works without issues
- Playwright browsers install successfully

<!-- section_id: "f89cef19-6ea6-4754-8c80-e056d2fc8453" -->
### WSL2 (Ubuntu 24.04) on Windows 11
- Tested on WSL2 (Ubuntu 24.04) on Windows 11, Lenovo Yoga 9 Pro
- Same setup process as native Linux
- Playwright runs entirely within WSL
- No Windows path configuration needed
- X11 forwarding optional (headless mode works without it)

<!-- section_id: "11f8b6bd-b6c8-404c-b2bc-205599153abc" -->
### Lenovo Yoga Pro 9
- Tested on Lenovo Yoga Pro 9 running Ubuntu 24.04 (native and WSL)
- No hardware-specific issues encountered
- All dependencies install correctly

<!-- section_id: "9dbde42d-af51-4d32-82bd-2a8492dd336f" -->
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

