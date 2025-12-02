# Playwright MCP Server Setup Guide

This guide documents the complete setup process for the Playwright MCP (Model Context Protocol) server for use with Claude Code.

**For Cursor IDE setup on Ubuntu, see [Playwright MCP Cursor Setup](playwright-mcp-cursor-setup.md).**

## Prerequisites

- Node.js and npm installed
- Claude Code installed
- WSL2 (if on Windows) or Linux environment
- sudo access for system dependencies

## Setup Steps

### 1. Create MCP Configuration

Create or edit `.mcp.json` in your project root with the following configuration:

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

**Configuration Notes:**
- `"command": "npx"` - Uses npx to run the Playwright MCP server
- `"-y"` - Automatically confirms package installation
- `"@playwright/mcp@latest"` - Always uses the latest version
- `"--browser", "chromium"` - Specifies Chromium as the browser (recommended)
- **Do not** include `PLAYWRIGHT_BROWSERS_PATH` environment variable unless you have a custom browser installation path

### 2. Install System Dependencies

Playwright requires various system libraries to run browsers. Run the following commands:

```bash
# Update package list
sudo apt-get update

# Install required system dependencies
sudo apt-get install -y --no-install-recommends \
  libasound2t64 libatk-bridge2.0-0t64 libatk1.0-0t64 libatspi2.0-0t64 \
  libcairo2 libcups2t64 libdbus-1-3 libdrm2 libgbm1 libglib2.0-0t64 \
  libnspr4 libnss3 libpango-1.0-0 libx11-6 libxcb1 libxcomposite1 \
  libxdamage1 libxext6 libxfixes3 libxkbcommon0 libxrandr2 xvfb \
  fonts-noto-color-emoji fonts-unifont libfontconfig1 libfreetype6 \
  xfonts-cyrillic xfonts-scalable fonts-liberation fonts-ipafont-gothic \
  fonts-wqy-zenhei fonts-tlwg-loma-otf fonts-freefont-ttf
```

**Alternative:** Use the provided installation script:
```bash
bash install-playwright.sh
```

### 3. Install Browser Binaries

Install the Chromium browser for Playwright:

```bash
npx -y playwright@latest install chromium
```

**⚠️ CRITICAL: Use Node.js Playwright, NOT Python Playwright**

The MCP server uses **Node.js Playwright** (`npx playwright`), which is different from Python Playwright (`python3 -m playwright`). They install browsers to different locations and use different browser builds.

**✅ CORRECT (for MCP servers):**
```bash
# Use run_terminal_cmd directly (don't wrap Node.js commands in Python wrapper)
run_terminal_cmd("npx -y playwright@latest install chromium ; exit")
```

**❌ WRONG (will NOT work with MCP servers):**
```bash
# Don't use Python Playwright
python3 -m playwright install chromium  # Don't use this!

# Don't wrap Node.js commands unnecessarily
python3 scripts/terminal_wrapper.py "npx playwright install chromium ; exit"  # Unnecessary
```

**Why not wrap Node.js commands:**
- Wrapping Node.js commands in Python wrapper can cause confusion
- Seeing `python3` at the start might lead to using Python Playwright instead
- Node.js commands don't have Python subprocess hanging issues
- Direct `run_terminal_cmd` with `; exit` is clearer and simpler

**Why this matters:**
- Python Playwright installs browsers that the MCP server cannot find
- The MCP server expects browsers installed via Node.js Playwright
- Using Python Playwright will cause "Browser not installed" errors even after installation
- You'll end up downloading browsers multiple times unnecessarily

**If you accidentally used Python Playwright:**
1. Remove the Python-installed browsers: `rm -rf ~/.cache/ms-playwright/chromium-*` (keep only the Node.js version)
2. Install using Node.js: `npx -y playwright@latest install chromium`
3. Restart Cursor/Claude Code

This will download:
- Chromium browser (~174 MB)
- FFMPEG (~2.3 MB)
- Chromium Headless Shell (~104 MB)

**Note:** You may see a warning about installing without project dependencies. This is normal and can be safely ignored.

**Installation takes 5-10 minutes** depending on your internet connection. Wait for the download to complete fully.

### 4. Verify Installation

Check that the browsers were installed successfully:

```bash
ls -la ~/.cache/ms-playwright/
```

You should see directories like:
- `chromium-1194` (version number may vary)
- `chromium_headless_shell-1194`
- `ffmpeg-1011`

### 5. Restart Claude Code

After completing the setup:
1. Close Claude Code completely
2. Restart Claude Code
3. The Playwright MCP server should now be available

## Troubleshooting

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

2. If you see multiple chromium directories (e.g., `chromium-1187`, `chromium-1200`), you likely have both Python and Node.js installations.

3. Remove Python-installed browsers (they use different version numbers):
   ```bash
   # Check which is the Node.js version (usually the newest)
   # Then remove the Python-installed ones
   rm -rf ~/.cache/ms-playwright/chromium-1200 ~/.cache/ms-playwright/chromium_headless_shell-1200
   ```

4. Install using Node.js Playwright (the correct method):
   ```bash
   npx -y playwright@latest install chromium
   ```

5. Restart Cursor/Claude Code completely.

**Prevention:** Always use `npx -y playwright@latest install chromium` for MCP servers, never `python3 -m playwright install chromium`.

### Issue: "Chromium distribution 'chrome' is not found"

**Error message:**
```
Error: Chromium distribution 'chrome' is not found at /opt/google/chrome/chrome
Run "npx playwright install chrome"
```

**Common cause:** The configuration is trying to use Chrome instead of Chromium, or Chrome is not properly installed.

**Solution 1: Use Chromium (Recommended)**
1. Update `.mcp.json` to use Chromium:
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

2. Install Chromium:
   ```bash
   npx -y playwright@latest install chromium
   ```

3. Restart Claude Code

**Solution 2: Use Chrome (If you specifically need Chrome)**
1. Install system Chrome first (if not already installed):
   ```bash
   # On Ubuntu/WSL2:
   wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
   sudo apt install ./google-chrome-stable_current_amd64.deb
   ```

2. Install Playwright Chrome channel:
   ```bash
   npx -y playwright@latest install chrome
   ```

3. Ensure `.mcp.json` uses `"--browser", "chrome"` (not "chromium")

4. Restart Claude Code

**Note:** For most use cases, Chromium is recommended as it's more stable and doesn't require system Chrome installation.

### Issue: "Active lockfile found"

**Error message:**
```
An active lockfile is found at: /home/dawson/.cache/ms-playwright/__dirlock
```

**Solution:** Remove the lockfile and reinstall:
```bash
rm -rf ~/.cache/ms-playwright/__dirlock
npx -y playwright@latest install chromium
```

### Issue: Browser installation command hangs

**Solution:** The installation may be downloading in the background. Wait 5-10 minutes for it to complete. If it truly hangs, cancel with Ctrl+C, remove the lockfile (see above), and try again.

### Issue: MCP tools not available in Claude Code

**Possible causes:**
1. Claude Code needs to be restarted after configuration changes
2. Invalid configuration in `.mcp.json` (check JSON syntax)
3. Invalid command-line arguments passed to the MCP server

**Solution:**
1. Verify `.mcp.json` syntax is correct
2. Completely restart Claude Code
3. Check Claude Code logs for MCP server startup errors

### Issue: "sudo: a password is required"

**Solution:** System dependencies require sudo access. Run the installation commands in a terminal where you can provide your password, or ask your system administrator to install the dependencies.

## Browser Options

While this guide uses Chromium (recommended), Playwright supports other browsers:

- **chromium** (recommended) - Most reliable, fully tested, automatically installed via Playwright
- **chrome** - Google Chrome (requires system Chrome installation + Playwright Chrome channel)
- **firefox** - Mozilla Firefox
- **webkit** - Safari's engine
- **msedge** - Microsoft Edge

### Important: Chrome vs Chromium

**Chromium** (recommended):
- Open-source browser automatically installed by Playwright
- No additional system installation needed
- Use: `npx -y playwright@latest install chromium`
- Configure: `"--browser", "chromium"` in `.mcp.json`

**Chrome** (Google Chrome):
- Requires **both** system Chrome installation AND Playwright Chrome channel
- System Chrome must be installed separately (not via Playwright)
- Then install Playwright Chrome channel: `npx -y playwright@latest install chrome`
- Configure: `"--browser", "chrome"` in `.mcp.json`
- **Note**: Chrome DevTools MCP server requires system Chrome, not Playwright Chromium

**⚠️ Common Error with Chrome:**
```
Error: Chromium distribution 'chrome' is not found at /opt/google/chrome/chrome
Run "npx playwright install chrome"
```

**Solution:**
1. Install system Chrome first (if not already installed)
2. Then run: `npx -y playwright@latest install chrome`
3. Ensure `.mcp.json` uses `"--browser", "chrome"` (not "chromium")

To use a different browser:
1. Install it: `npx -y playwright@latest install <browser-name>`
2. Update `.mcp.json` args to specify: `"--browser", "<browser-name>"`
3. Restart Claude Code

## What Gets Installed

### System Dependencies (via apt-get)
- Audio libraries (libasound2t64)
- Accessibility libraries (libatk, libatspi)
- Graphics libraries (libcairo2, libdrm2, libgbm1)
- Font libraries and fonts
- X11 display libraries
- Virtual framebuffer (xvfb) for headless mode

### Browser Binaries (via Playwright)
- Installed to: `~/.cache/ms-playwright/`
- Chromium: ~174 MB
- FFMPEG: ~2.3 MB
- Chromium Headless Shell: ~104 MB

### Total Download Size
- System dependencies: ~50-100 MB (varies)
- Browser binaries: ~280 MB
- **Total: ~330-380 MB**

## Files Modified

- `.mcp.json` - MCP server configuration
- `~/.cache/ms-playwright/` - Browser binaries installed here

## Next Steps

After setup is complete, see `playwright-mcp-usage.md` for instructions on how to use the Playwright MCP server.