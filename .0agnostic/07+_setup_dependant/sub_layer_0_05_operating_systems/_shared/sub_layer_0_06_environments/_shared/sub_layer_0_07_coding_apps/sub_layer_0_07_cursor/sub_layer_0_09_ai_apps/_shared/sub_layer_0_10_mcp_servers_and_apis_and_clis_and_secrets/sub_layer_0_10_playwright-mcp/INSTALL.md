---
resource_id: "797a9e3a-f53a-4b06-94bd-4f2993dbd21d"
resource_type: "document"
resource_name: "INSTALL"
---
# Playwright MCP Server Installation Guide

<!-- section_id: "906371f3-9a19-43d3-b55a-2e531ec006e4" -->
## Overview
The Playwright MCP Server (`@playwright/mcp`) enables browser automation for AI agents.

**Repository**: [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

---

<!-- section_id: "9d6d21a8-cb9d-4e44-92e7-fd972e9c5688" -->
## 🚀 Universal Automated Setup (Recommended)

We have created a unified automation tool to handle installation across all OSs and AI tools.

<!-- section_id: "d08a927b-4beb-4091-8ee4-517ae344a7f5" -->
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

<!-- section_id: "8269ad81-410e-4dfe-9f16-1855a2122a07" -->
## 🛠️ Manual Installation by OS & Tool

If you cannot use the automation script, follow these specific instructions.

<!-- section_id: "67b18bb7-0a3e-4cbd-a0bc-a6d92b2846ae" -->
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

<!-- section_id: "f85df167-fadb-4187-81f0-4b7aefa06f86" -->
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

<!-- section_id: "dd03ef93-7dd2-47f5-a63a-2865f20c3bcc" -->
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

<!-- section_id: "8d1d8886-0bcd-4f79-8d05-0074b1c106f8" -->
## 🧪 Verification

1. **Install Browsers**: `npx playwright install chromium`
2. **Install Dependencies (Linux)**: `npx playwright install-deps`
3. **Test Command**:
   ```bash
   npx -y @playwright/mcp@latest --browser chromium
   ```
   (Should start and wait for input without error)
