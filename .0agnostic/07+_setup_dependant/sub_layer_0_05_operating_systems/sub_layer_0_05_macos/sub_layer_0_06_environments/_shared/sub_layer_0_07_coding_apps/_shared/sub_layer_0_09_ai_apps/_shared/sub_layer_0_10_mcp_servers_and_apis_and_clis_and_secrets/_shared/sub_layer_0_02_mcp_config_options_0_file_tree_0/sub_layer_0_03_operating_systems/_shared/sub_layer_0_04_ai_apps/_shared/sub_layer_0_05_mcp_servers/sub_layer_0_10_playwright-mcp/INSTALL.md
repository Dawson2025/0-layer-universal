---
resource_id: "f4b83256-7318-4092-aafc-115445912443"
resource_type: "document"
resource_name: "INSTALL"
---
# Playwright MCP Server Installation Guide

<!-- section_id: "fb8bc302-1cdd-4016-b9d9-4606acebbef5" -->
## Overview
The Playwright MCP Server (`@playwright/mcp`) enables browser automation for AI agents.

**Repository**: [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

---

<!-- section_id: "fbb7f9af-2a4f-494f-8dcd-1dc94f4e7b77" -->
## 🚀 Universal Automated Setup (Recommended)

We have created a unified automation tool to handle installation across all OSs and AI tools.

<!-- section_id: "e5fbfa7e-4f3f-42af-830a-5887e562fc0f" -->
### 1. Run the Automation Script
```bash
# Run from the project root or universal context
python3 automation/scripts/mcp_manager.py --scope user
```

This script automatically:
- Detects your OS (Linux/WSL, Windows, macOS)
- Generates robust wrapper scripts to handle PATH and Environment Variables
- Updates your `mcp.json` configuration

---

<!-- section_id: "3e17d989-b375-4863-9668-2db9cd65830e" -->
## 🛠️ Manual Installation by OS & Tool

If you cannot use the automation script, follow these specific instructions.

<!-- section_id: "3bf5fec2-cc70-45c0-9b20-ccfc4917763e" -->
### 🐧 Linux / WSL (Ubuntu)

**Critical Prerequisite**: You must set `PLAYWRIGHT_BROWSERS_PATH` and `HOME` environment variables, or the server will fail to find browsers.

**Important note (current Playwright MCP)**:
- Playwright MCP is **headed by default**.
- To force headless, use the `--headless` flag.
- Do **not** use `--headless=false` (it is not a supported flag and will cause the server to exit during startup).

#### For Gemini CLI
Update `~/.gemini/settings.json`:
```json
{
  "mcpServers": {
    "playwright": {
      "command": "/bin/bash",
      "args": ["-c", "export PLAYWRIGHT_BROWSERS_PATH=$HOME/.cache/ms-playwright && export HOME=$HOME && npx -y @playwright/mcp@latest --browser chromium"],
      "env": {}
    }
  }
}
```

#### For Claude Code
Update `~/.claude.json` (or project config):
```json
"mcpServers": {
  "playwright": {
    "command": "/bin/bash",
    "args": ["-c", "export PLAYWRIGHT_BROWSERS_PATH=$HOME/.cache/ms-playwright && export HOME=$HOME && npx -y @playwright/mcp@latest --browser chromium"],
    "env": {}
  }
}
```

#### WSLg headed stability (recommended)
On WSLg, Chromium may crash immediately in headed mode unless you launch it with Wayland/Ozone flags. The most reliable way is to use a Playwright MCP config file:

```bash
cat > /tmp/playwright-wslg.json <<'EOF'
{
  "browser": {
    "browserName": "chromium",
    "isolated": true,
    "launchOptions": {
      "headless": false,
      "args": ["--ozone-platform=wayland", "--enable-features=UseOzonePlatform"]
    }
  }
}
EOF
```

Then run MCP with:
```bash
npx -y @playwright/mcp@latest --config /tmp/playwright-wslg.json
```

If you need headless on WSL (no GUI), set `"headless": true` (or use `--headless`).

#### For Cursor IDE
**⚠️ WARNING**: As of v2.0.77, Cursor on Linux/WSL has a bug where Playwright tools are not exposed to the agent even if connected.
**Workaround**: Use `@agent-infra/mcp-server-browser` instead.

<!-- section_id: "00309d7b-063f-4de4-948b-c150a80a648a" -->
### 🪟 Windows

#### For Gemini CLI / Claude / Cursor
Ensure Node.js is in your PATH.
Config structure:
```json
"playwright": {
  "command": "npx.cmd",
  "args": ["-y", "@playwright/mcp@latest", "--browser", "chromium"],
  "env": {
    "PLAYWRIGHT_BROWSERS_PATH": "C:\\Users\\YourUser\\AppData\\Local\\ms-playwright"
  }
}
```

<!-- section_id: "e4103ead-085a-4bb1-b457-25d15c4861bb" -->
### 🍎 macOS

Similar to Linux, but typically requires less strict environment wrapping if your shell environment is standard.
```json
"playwright": {
  "command": "npx",
  "args": ["-y", "@playwright/mcp@latest", "--browser", "chromium"],
  "env": {
    "PLAYWRIGHT_BROWSERS_PATH": "/Users/you/Library/Caches/ms-playwright"
  }
}
```

---

<!-- section_id: "a8586369-a16e-4e85-b1a4-0fd44917a240" -->
## 🧪 Verification

1. **Install Browsers**: `npx playwright install chromium`
2. **Install Dependencies (Linux)**: `npx playwright install-deps`
3. **Test Command**:
   ```bash
   npx -y @playwright/mcp@latest --browser chromium
   ```
   (Should start and wait for input without error)
