---
resource_id: "382d9d97-b0ce-4fb6-bee7-0500f6f81a97"
resource_type: "document"
resource_name: "INSTALL"
---
# Playwright MCP Server Installation Guide

<!-- section_id: "0751eaf3-370d-4e1d-9ab9-3a7d38a83633" -->
## Overview
The Playwright MCP Server (`@playwright/mcp`) enables browser automation for AI agents.

**Repository**: [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

---

<!-- section_id: "c55257de-ab53-48a9-a402-a692f6f92b79" -->
## 🚀 Universal Automated Setup (Recommended)

We have created a unified automation tool to handle installation across all OSs and AI tools.

<!-- section_id: "0848566b-0087-4aa0-869b-8748bacaec45" -->
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

<!-- section_id: "3394b52f-ee37-46eb-8fe9-a9bb1f402cc0" -->
## 🛠️ Manual Installation by OS & Tool

If you cannot use the automation script, follow these specific instructions.

<!-- section_id: "66421e48-fb30-4b3e-a2fc-e0bb5790f375" -->
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

<!-- section_id: "ae3526ec-9842-4a55-b1e4-549d11bd452a" -->
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

<!-- section_id: "d5fa28bb-9e76-4bd8-8db1-17d1888ad100" -->
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

<!-- section_id: "2497e2d5-b7c8-4d62-9b91-ed6b9cdac074" -->
## 🧪 Verification

1. **Install Browsers**: `npx playwright install chromium`
2. **Install Dependencies (Linux)**: `npx playwright install-deps`
3. **Test Command**:
   ```bash
   npx -y @playwright/mcp@latest --browser chromium
   ```
   (Should start and wait for input without error)
