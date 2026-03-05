---
resource_id: "38635067-1c66-42e4-a137-dad996280142"
resource_type: "document"
resource_name: "PLAYWRIGHT_MCP_CURSOR_SETUP"
---
# Playwright MCP Server Setup for Cursor IDE

**Location**: Universal Tools → MCP Tools  
**Last Updated**: 2025-12-05  
**Status**: ✅ Working and tested (Linux/Ubuntu), ✅ Working (WSL)

Complete guide for setting up the Playwright MCP (Model Context Protocol) server in Cursor IDE on Ubuntu Linux systems, including WSL environments.

<!-- section_id: "1ed42221-d2ba-4a8b-ac2f-a384adcfd04f" -->
## Prerequisites

- Ubuntu 24.04 (Noble) or later (native or WSL2)
- Administrator (sudo) access
- Internet connection
- Cursor IDE installed

<!-- section_id: "021f8a22-03a5-439f-97a7-39d4fe2dae10" -->
## Overview

This guide documents the setup process for Playwright MCP server in Cursor IDE on Ubuntu Linux (native and WSL). The MCP server enables browser automation capabilities directly within Cursor, allowing AI agents to interact with web browsers for testing, automation, and web scraping tasks.

**Platforms Covered**:
- ✅ Native Linux/Ubuntu
- ✅ WSL2 (Ubuntu 24.04) on Windows 11

<!-- section_id: "ab98538c-c842-40d7-bab9-54864ab61e50" -->
## Setup Steps

<!-- section_id: "360aa05b-7f0b-4968-90d0-ca8fb18a13a5" -->
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

<!-- section_id: "17767d1d-c6d0-4cfc-9316-aeafc847a70b" -->
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

<!-- section_id: "98ab569b-5950-4634-b55f-5d5b8e45a719" -->
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

<!-- section_id: "0fa2a182-6dc9-465f-a97f-e6d55b23ca11" -->
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

<!-- section_id: "326444d6-3837-4773-a287-ce615a487278" -->
### Step 5: Restart Cursor

After completing the setup:

1. **Completely close Cursor** (not just the window, ensure all processes are terminated)
2. **Restart Cursor IDE**
3. The Playwright MCP server should now be available

<!-- section_id: "66e7ef68-f85b-4bc7-aa2c-003e321fc6a5" -->
## Verification

<!-- section_id: "b024e83d-21f1-450f-95c6-d31b4e0a8fe8" -->
### Check 1: Verify Browser Installation

```bash
ls -la ~/.cache/ms-playwright/
```

You should see directories like:
- `chromium-1200` (version number may vary)
- `chromium_headless_shell-1200`
- `ffmpeg-1011`

<!-- section_id: "46448bf0-32cc-4ea1-b0c5-65a0f472d861" -->
### Check 2: Verify MCP Configuration

```bash
cat ~/.config/mcp/mcp.json
# or
cat ~/.cursor/mcp.json
```

Should show the Playwright MCP configuration.

<!-- section_id: "dd3b48d5-9b9c-4e2a-84ed-ad9baf880cf4" -->
### Check 3: Test MCP Server Command

```bash
# Load nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Test the MCP server command
npx -y @playwright/mcp@latest --browser chromium --help
```

Should display help text without errors.

<!-- section_id: "a73f8311-172b-4b8e-858b-9f1b6127fb2a" -->
### Check 4: Verify in Cursor

After restarting Cursor:
- Playwright MCP tools should be available
- Check Cursor Settings → Tools & MCP → Installed MCP Servers
- Should show "playwright" with "22 tools enabled"
- You can ask Cursor to navigate to websites and it should work

<!-- section_id: "ff0acb06-e752-4766-b539-33a94b3e251b" -->
## WSL (Windows Subsystem for Linux) Setup

**Last Updated**: 2025-12-05  
**Environment**: WSL2 (Ubuntu 24.04) on Windows 11, Lenovo Yoga 9 Pro  
**Status**: ✅ Working

<!-- section_id: "1f7585fe-515c-45f1-aaca-10f16378376a" -->
### WSL-Specific Configuration

Playwright MCP works well in WSL environments. The setup process is identical to native Linux, with a few considerations:

**Key Points**:
- Playwright MCP runs entirely within WSL
- Browser binaries are installed in WSL: `~/.cache/ms-playwright/`
- No need to use Windows Chrome paths (unlike cursor-browser-extension)
- X11 forwarding may be required for GUI applications (headless mode works without it)

<!-- section_id: "f07e3e22-a0c5-4405-9fad-cb8ab49fb051" -->
### WSL Setup Process

The setup steps are the same as native Linux:

1. ✅ Install Node.js via NVM (same commands)
2. ✅ Install system dependencies (same commands)
3. ✅ Install Playwright Chromium (same commands)
4. ✅ Configure MCP settings (same configuration)
5. ✅ Restart Cursor

<!-- section_id: "f81242c8-88be-4a19-9d41-744809e07be8" -->
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

<!-- section_id: "07c619d2-4478-4580-87d3-00f3a29674a2" -->
### WSL Advantages

- **Isolated Environment**: Playwright runs entirely in WSL, separate from Windows
- **Consistent Behavior**: Same behavior as native Linux
- **No Path Issues**: Unlike cursor-browser-extension, Playwright MCP doesn't need Windows paths
- **Easy Setup**: Same configuration as native Linux

<!-- section_id: "ed9379b3-5c6c-4157-be50-421a39ada137" -->
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

<!-- section_id: "9c2f28b2-8b61-4cf0-b268-eedd57bc43f7" -->
## Troubleshooting

<!-- section_id: "8bb659cf-3204-406d-839b-2d1db66e486d" -->
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

<!-- section_id: "c9de758c-964d-4a71-927f-57637b75f0f6" -->
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

<!-- section_id: "1c449836-e8be-4cfd-a627-f24b2771d1a1" -->
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

<!-- section_id: "66fc354b-baf1-46de-9441-0263b5201c3d" -->
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

<!-- section_id: "008fe84d-407f-4b98-91f4-bcea903c0afe" -->
### Issue: Browser installation command hangs

**Solution:** The installation may be downloading in the background. Wait 5-10 minutes for it to complete. If it truly hangs:
1. Cancel with Ctrl+C
2. Remove the lockfile (see above)
3. Try again

<!-- section_id: "918ce009-ea6f-46eb-b50c-a716b3bde61d" -->
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

<!-- section_id: "45e86a3c-43eb-4683-acf4-95de8d06e06f" -->
## What Gets Installed

<!-- section_id: "277c29cc-659a-41e1-bbb7-14a87db5ff4c" -->
### System Dependencies (via apt-get)
- Audio libraries (libasound2t64)
- Accessibility libraries (libatk, libatspi)
- Graphics libraries (libcairo2, libdrm2, libgbm1)
- Font libraries and fonts
- X11 display libraries
- Virtual framebuffer (xvfb) for headless mode

<!-- section_id: "3e34da52-dff3-44f0-a71a-04413c20b421" -->
### Browser Binaries (via Playwright)
- Installed to: `~/.cache/ms-playwright/`
- Chromium: ~164.7 MB
- FFMPEG: ~2.3 MB
- Chromium Headless Shell: ~109.7 MB

<!-- section_id: "9dfc2ce3-63c8-4fa0-977c-c5c8cab440ee" -->
### Total Download Size
- System dependencies: ~50-100 MB (varies)
- Browser binaries: ~280 MB
- **Total: ~330-380 MB**

<!-- section_id: "5609cbb7-d5f2-41ac-af7a-7f33027de9ad" -->
## Files Modified

- `~/.config/mcp/mcp.json` - Cursor MCP server configuration (primary location)
- `~/.cursor/mcp.json` - Symlink to above (for compatibility)
- `~/.cache/ms-playwright/` - Browser binaries installed here
- `~/.bashrc` - NVM configuration added (if not already present)
- `~/.nvm/` - Node.js installation via nvm

<!-- section_id: "a194f36e-a703-4023-99f8-d2ba29c735b1" -->
## Usage in Cursor

Once configured, you can ask Cursor to:

```
"Navigate to https://example.com and take a screenshot"

"Test the login flow by navigating to localhost:5000/login and entering credentials"

"Check if the word creation form has proper accessibility labels"

"Scrape the phoneme display table and verify all entries are present"
```

Cursor will use the Playwright MCP tools automatically to interact with browsers.

<!-- section_id: "ac76a438-91d0-4111-8a39-e9dd412c66be" -->
## Key Differences: Cursor vs Claude Code

- **Cursor**: Uses global config at `~/.config/mcp/mcp.json` (symlinked to `~/.cursor/mcp.json`)
- **Claude Code**: Uses project-level `.mcp.json` in project root
- **Both**: Use the same MCP server command format
- **Both**: Require Node.js Playwright (not Python Playwright)

<!-- section_id: "7bd154a0-4e78-4ebe-84df-69801b4618d2" -->
## Environment-Specific Notes

<!-- section_id: "30022b42-6e0e-41c1-8615-182a3cb56c44" -->
### Ubuntu 24.04 (Noble) - Native Linux
- Tested and verified on Ubuntu 24.04.3 LTS
- All system dependencies available in default repositories
- NVM installation works without issues
- Playwright browsers install successfully

<!-- section_id: "9e9a6ac2-0b57-4f24-a12e-3f6ffa02bf61" -->
### WSL2 (Ubuntu 24.04) on Windows 11
- Tested on WSL2 (Ubuntu 24.04) on Windows 11, Lenovo Yoga 9 Pro
- Same setup process as native Linux
- Playwright runs entirely within WSL
- No Windows path configuration needed
- X11 forwarding optional (headless mode works without it)

<!-- section_id: "6b746465-be56-48e3-8c68-823f19df2b67" -->
### Lenovo Yoga Pro 9
- Tested on Lenovo Yoga Pro 9 running Ubuntu 24.04 (native and WSL)
- No hardware-specific issues encountered
- All dependencies install correctly

<!-- section_id: "fd62ef68-c643-42a1-86b1-fb6829b0020b" -->
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

