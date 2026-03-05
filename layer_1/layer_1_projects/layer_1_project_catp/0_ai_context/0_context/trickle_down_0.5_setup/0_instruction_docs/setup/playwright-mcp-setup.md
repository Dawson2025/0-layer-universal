---
resource_id: "e78170ac-d822-44a6-bb8a-7360bec18ba4"
resource_type: "document"
resource_name: "playwright-mcp-setup"
---
# Playwright MCP Server Setup Guide

This guide documents the complete setup process for the Playwright MCP (Model Context Protocol) server for use with Claude Code.

<!-- section_id: "824ebf59-de96-438f-96d1-1b1a875aa62b" -->
## Prerequisites

- Node.js and npm installed
- Claude Code installed
- WSL2 (if on Windows) or Linux environment
- sudo access for system dependencies

<!-- section_id: "2aca8639-addf-4789-8147-cb355469f3fa" -->
## Setup Steps

<!-- section_id: "f89d8cb7-c51c-4739-8f3d-386233f8da5b" -->
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

<!-- section_id: "56a27954-bb39-4d82-a3c0-18909254a4d6" -->
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

<!-- section_id: "560025b7-3858-4677-8dc5-86df654732ef" -->
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

<!-- section_id: "5748201c-00f8-4bee-9337-aaa711226c82" -->
### 4. Verify Installation

Check that the browsers were installed successfully:

```bash
ls -la ~/.cache/ms-playwright/
```

You should see directories like:
- `chromium-1194` (version number may vary)
- `chromium_headless_shell-1194`
- `ffmpeg-1011`

<!-- section_id: "db5de1aa-d1f4-490f-a681-ef8a92abc5d6" -->
### 5. Restart Claude Code

After completing the setup:
1. Close Claude Code completely
2. Restart Claude Code
3. The Playwright MCP server should now be available

<!-- section_id: "bbb397d0-c970-45b4-b7b9-6652fd369823" -->
## Troubleshooting

<!-- section_id: "759ab402-317a-4c4f-b507-907177d16c07" -->
### Issue: "Chromium distribution 'chrome' is not found"

**Solution:** The configuration is trying to use Chrome instead of Chromium. Update `.mcp.json` to include `"--browser", "chromium"` in the args array.

<!-- section_id: "6ce7f234-ad5d-4763-98d8-b26cd286d4d3" -->
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

<!-- section_id: "a56354dc-7e0f-404c-bdb7-4dc97fa34991" -->
### Issue: Browser installation command hangs

**Solution:** The installation may be downloading in the background. Wait 5-10 minutes for it to complete. If it truly hangs, cancel with Ctrl+C, remove the lockfile (see above), and try again.

<!-- section_id: "31c01540-a88a-4ecc-a11e-fc3861127724" -->
### Issue: MCP tools not available in Claude Code

**Possible causes:**
1. Claude Code needs to be restarted after configuration changes
2. Invalid configuration in `.mcp.json` (check JSON syntax)
3. Invalid command-line arguments passed to the MCP server

**Solution:**
1. Verify `.mcp.json` syntax is correct
2. Completely restart Claude Code
3. Check Claude Code logs for MCP server startup errors

<!-- section_id: "a8e3f67c-1fe1-4d81-be58-265b09c0b4d3" -->
### Issue: "sudo: a password is required"

**Solution:** System dependencies require sudo access. Run the installation commands in a terminal where you can provide your password, or ask your system administrator to install the dependencies.

<!-- section_id: "d57da115-0bb8-4864-9707-6d9bcf943669" -->
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

<!-- section_id: "01bb563b-0606-49a1-84d4-90bb65ee9e8b" -->
## What Gets Installed

<!-- section_id: "62f24ea3-ba90-4e87-9cbf-65ce044bfc0c" -->
### System Dependencies (via apt-get)
- Audio libraries (libasound2t64)
- Accessibility libraries (libatk, libatspi)
- Graphics libraries (libcairo2, libdrm2, libgbm1)
- Font libraries and fonts
- X11 display libraries
- Virtual framebuffer (xvfb) for headless mode

<!-- section_id: "0a8837a5-dc8b-4e11-ade8-6628f2dd50d0" -->
### Browser Binaries (via Playwright)
- Installed to: `~/.cache/ms-playwright/`
- Chromium: ~174 MB
- FFMPEG: ~2.3 MB
- Chromium Headless Shell: ~104 MB

<!-- section_id: "79af90a2-a3b2-4a1c-a127-a6aa5a11a7c1" -->
### Total Download Size
- System dependencies: ~50-100 MB (varies)
- Browser binaries: ~280 MB
- **Total: ~330-380 MB**

<!-- section_id: "cacd599a-a5cd-4c54-927e-c45e9078c573" -->
## Files Modified

- `.mcp.json` - MCP server configuration
- `~/.cache/ms-playwright/` - Browser binaries installed here

<!-- section_id: "91c10cff-b0df-41e1-95e5-9a0c4998cd3f" -->
## Next Steps

After setup is complete, see `playwright-mcp-usage.md` for instructions on how to use the Playwright MCP server.