---
resource_id: "c0dfd964-e182-48fd-adc3-ec19ff9476fd"
resource_type: "document"
resource_name: "INSTALL"
---
# Playwright MCP Server Installation Guide

<!-- section_id: "ce0949af-99a4-42c1-8e41-72db863ed4c3" -->
## Overview
The Playwright MCP Server (`@playwright/mcp`) enables browser automation for AI agents.

**Repository**: [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

---

<!-- section_id: "313ca9ba-f1fb-4ae5-9a15-baf22673bde8" -->
## 🚀 Universal Automated Setup (Recommended)

We have created a unified automation tool to handle installation across all OSs and AI tools.

<!-- section_id: "4745f413-70cf-481d-99d5-76f8cb9d61eb" -->
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

<!-- section_id: "f20228d6-8059-4579-92ed-89e73f04452f" -->
## 🛠️ Manual Installation by OS & Tool

If you cannot use the automation script, follow these specific instructions.

<!-- section_id: "1238b18d-9548-4ee9-9489-d56482304a68" -->
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

<!-- section_id: "da375e73-5ea3-4470-911d-5b52e1fa2577" -->
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

<!-- section_id: "52e15b08-421e-4030-923a-1392b8443ab3" -->
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

<!-- section_id: "d5d899f1-982b-4f9c-af9e-3f444d320bbc" -->
## 🧪 Verification

1. **Install Browsers**: `npx playwright install chromium`
2. **Install Dependencies (Linux)**: `npx playwright install-deps`
3. **Test Command**:
   ```bash
   npx -y @playwright/mcp@latest --browser chromium
   ```
   (Should start and wait for input without error)
