---
resource_id: "6d080834-9d91-4aeb-a900-c88b1a54bb74"
resource_type: "document"
resource_name: "INSTALL"
---
# Playwright MCP Server Installation Guide

<!-- section_id: "7c7aff5b-e119-416c-8c1b-d30827a59dfe" -->
## Overview
The Playwright MCP Server (`@playwright/mcp`) enables browser automation for AI agents.

**Repository**: [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

---

<!-- section_id: "0eee5e07-242a-4b41-9512-6d58fab4657f" -->
## 🚀 Universal Automated Setup (Recommended)

We have created a unified automation tool to handle installation across all OSs and AI tools.

<!-- section_id: "07a511f8-314d-4431-a039-ae099b9850ac" -->
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

<!-- section_id: "366139ed-ca5d-468c-8532-c3da0b400ac7" -->
## 🛠️ Manual Installation by OS & Tool

If you cannot use the automation script, follow these specific instructions.

<!-- section_id: "b539fb30-c7f3-4e3d-9e14-e4f83f23e2d0" -->
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

<!-- section_id: "e44efe6b-375e-4001-a2dd-2f089660f698" -->
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

<!-- section_id: "8920cb11-f1c7-4dc4-a0f1-e90ab97556b8" -->
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

<!-- section_id: "7147b01c-1401-4bd0-9806-2765e313649b" -->
## 🧪 Verification

1. **Install Browsers**: `npx playwright install chromium`
2. **Install Dependencies (Linux)**: `npx playwright install-deps`
3. **Test Command**:
   ```bash
   npx -y @playwright/mcp@latest --browser chromium
   ```
   (Should start and wait for input without error)
