---
resource_id: "4cd465ba-50cf-40f2-b300-2100865b21ff"
resource_type: "document"
resource_name: "playwright-mcp-setup"
---
# Playwright MCP Server Setup Guide

This guide documents the complete setup process for the Playwright MCP (Model Context Protocol) server for use with Claude Code.

<!-- section_id: "39300060-b166-4aaa-afb5-09f33d2b2960" -->
## Prerequisites

- Node.js and npm installed
- Claude Code installed
- WSL2 (if on Windows) or Linux environment
- sudo access for system dependencies

<!-- section_id: "05683afa-17c0-4127-b7cc-91ab41eb2f8f" -->
## Setup Steps

<!-- section_id: "dfd44f2b-8a18-4748-a444-7123d1ffb4d8" -->
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

<!-- section_id: "c308bd57-dd76-4a46-924c-8bb51cda90e2" -->
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

<!-- section_id: "d2f7ec90-af93-4b10-b757-dc82db5b4b96" -->
### 3. Install Browser Binaries

Install the Chromium browser for Playwright:

```bash
npx -y playwright@latest install chromium
```

This will download:
- Chromium browser (~174 MB)
- FFMPEG (~2.3 MB)
- Chromium Headless Shell (~104 MB)

**Note:** You may see a warning about installing without project dependencies. This is normal and can be safely ignored.

**Installation takes 5-10 minutes** depending on your internet connection. Wait for the download to complete fully.

<!-- section_id: "718fe33f-08bb-4923-8a06-8e6ef45a1ecb" -->
### 4. Verify Installation

Check that the browsers were installed successfully:

```bash
ls -la ~/.cache/ms-playwright/
```

You should see directories like:
- `chromium-1194` (version number may vary)
- `chromium_headless_shell-1194`
- `ffmpeg-1011`

<!-- section_id: "90f363cd-85e4-4116-9029-92dfc4261d0b" -->
### 5. Restart Claude Code

After completing the setup:
1. Close Claude Code completely
2. Restart Claude Code
3. The Playwright MCP server should now be available

<!-- section_id: "4ddbd512-e5c7-47cd-8632-143049636f68" -->
## Troubleshooting

<!-- section_id: "d339f8ea-c7bc-4036-aff3-f54bc7853dd2" -->
### Issue: "Chromium distribution 'chrome' is not found"

**Solution:** The configuration is trying to use Chrome instead of Chromium. Update `.mcp.json` to include `"--browser", "chromium"` in the args array.

<!-- section_id: "ebb37438-40e1-44ca-9c9c-7765c1156ef6" -->
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

<!-- section_id: "c788d20f-fbcb-4cf5-b800-7b8c89d992ef" -->
### Issue: Browser installation command hangs

**Solution:** The installation may be downloading in the background. Wait 5-10 minutes for it to complete. If it truly hangs, cancel with Ctrl+C, remove the lockfile (see above), and try again.

<!-- section_id: "5f915ce6-c17c-41d0-a3aa-11fc59e0bc34" -->
### Issue: MCP tools not available in Claude Code

**Possible causes:**
1. Claude Code needs to be restarted after configuration changes
2. Invalid configuration in `.mcp.json` (check JSON syntax)
3. Invalid command-line arguments passed to the MCP server

**Solution:**
1. Verify `.mcp.json` syntax is correct
2. Completely restart Claude Code
3. Check Claude Code logs for MCP server startup errors

<!-- section_id: "4dc49d5c-6cf9-4918-ac67-3f111d9a8d3d" -->
### Issue: "sudo: a password is required"

**Solution:** System dependencies require sudo access. Run the installation commands in a terminal where you can provide your password, or ask your system administrator to install the dependencies.

<!-- section_id: "74747d43-9214-46b6-ac39-7d9ae834c874" -->
## Browser Options

While this guide uses Chromium (recommended), Playwright supports other browsers:

- **chromium** (recommended) - Most reliable, fully tested
- **chrome** - Google Chrome (requires different installation)
- **firefox** - Mozilla Firefox
- **webkit** - Safari's engine
- **msedge** - Microsoft Edge

To use a different browser:
1. Install it: `npx -y playwright@latest install <browser-name>`
2. Update `.mcp.json` args to specify: `"--browser", "<browser-name>"`
3. Restart Claude Code

<!-- section_id: "f4de998f-57ed-4986-86b5-39a11ae07ba1" -->
## What Gets Installed

<!-- section_id: "f60267a8-3f78-4375-bb99-9df6c6845fd8" -->
### System Dependencies (via apt-get)
- Audio libraries (libasound2t64)
- Accessibility libraries (libatk, libatspi)
- Graphics libraries (libcairo2, libdrm2, libgbm1)
- Font libraries and fonts
- X11 display libraries
- Virtual framebuffer (xvfb) for headless mode

<!-- section_id: "e941944a-904e-471b-be34-cd45a014d50f" -->
### Browser Binaries (via Playwright)
- Installed to: `~/.cache/ms-playwright/`
- Chromium: ~174 MB
- FFMPEG: ~2.3 MB
- Chromium Headless Shell: ~104 MB

<!-- section_id: "bbefe9ca-b774-46fc-95b0-5985c20ef538" -->
### Total Download Size
- System dependencies: ~50-100 MB (varies)
- Browser binaries: ~280 MB
- **Total: ~330-380 MB**

<!-- section_id: "90263d2c-7894-4966-816e-7f19afb74f5b" -->
## Files Modified

- `.mcp.json` - MCP server configuration
- `~/.cache/ms-playwright/` - Browser binaries installed here

<!-- section_id: "b6be87cf-f5f3-48bb-af9b-f26731df6551" -->
## Next Steps

After setup is complete, see `playwright-mcp-usage.md` for instructions on how to use the Playwright MCP server.