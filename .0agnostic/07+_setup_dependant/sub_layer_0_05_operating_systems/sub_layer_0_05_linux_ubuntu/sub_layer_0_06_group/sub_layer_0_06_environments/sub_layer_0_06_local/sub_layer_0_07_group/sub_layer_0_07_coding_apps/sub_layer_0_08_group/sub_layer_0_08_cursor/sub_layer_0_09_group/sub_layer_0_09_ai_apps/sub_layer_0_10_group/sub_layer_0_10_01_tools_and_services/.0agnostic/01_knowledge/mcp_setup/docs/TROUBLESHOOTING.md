---
resource_id: "0be90578-d85d-43dd-bedd-6fdb5dc7a27e"
resource_type: "knowledge"
resource_name: "TROUBLESHOOTING"
---
# MCP Setup Troubleshooting Guide

Common issues encountered during MCP server setup and their solutions.

<!-- section_id: "415a5125-b453-49a3-ac08-66d0d6137d1d" -->
## Table of Contents

1. [Browser Not Found Errors](#browser-not-found-errors)
2. [npx Not Found](#npx-not-found)
3. [Permission Denied](#permission-denied)
4. [Browser Crashes on WSLg](#browser-crashes-on-wslg)
5. [Browser Already in Use](#browser-already-in-use)
6. [MCP Server Not Responding](#mcp-server-not-responding)
7. [Environment Variables Not Set](#environment-variables-not-set)
8. [Configuration Not Loading](#configuration-not-loading)
9. [Debugging Tips](#debugging-tips)

---

<!-- section_id: "aed3db82-3437-46f5-9645-ad48c0a8ea8b" -->
## Browser Not Found Errors

<!-- section_id: "fb090d28-448f-4645-a151-e9398773e212" -->
### Symptom
```
Error: Browser specified in your config is not installed
```

<!-- section_id: "a7f99061-e597-434c-8359-05c209bdd611" -->
### Cause
MCP servers run via `npx` in isolated environments and do not inherit shell environment variables. The `PLAYWRIGHT_BROWSERS_PATH` and `HOME` variables are not passed to the MCP server process.

<!-- section_id: "fe57b596-0517-4f0c-9c59-5f8755a1f960" -->
### Solution

1. **Run the setup automation**:
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```

2. **Verify environment variables are set in mcp.json**:
   ```json
   {
     "mcpServers": {
       "playwright": {
         "env": {
           "PLAYWRIGHT_BROWSERS_PATH": "/home/username/.cache/ms-playwright",
           "HOME": "/home/username"
         }
       }
     }
   }
   ```

3. **Install Playwright browsers if missing**:
   ```bash
   npx playwright install chromium
   ```

4. **Restart your AI agent/IDE**

---

<!-- section_id: "741a2bb9-6621-4591-a12e-6e8c3b87a326" -->
## npx Not Found

<!-- section_id: "f543379e-6482-46b6-93af-b84237562d95" -->
### Symptom
```
npx: command not found
```
or
```
Warning: 'npx' not found in system PATH
```

<!-- section_id: "422e8b1c-83a1-4d2b-a634-f75aa0f9c437" -->
### Cause
Node.js is not installed or not in the system PATH. This commonly happens with NVM (Node Version Manager) installations.

<!-- section_id: "7ae63e92-ad2f-4de2-bb8a-db8631c5f9f0" -->
### Solution

1. **Check if Node.js is installed**:
   ```bash
   node --version
   which npx
   ```

2. **If using NVM, ensure it's loaded**:
   ```bash
   source ~/.nvm/nvm.sh
   nvm use default
   ```

3. **Install Node.js if missing**:
   ```bash
   # Using NVM (recommended)
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   source ~/.nvm/nvm.sh
   nvm install --lts
   ```

4. **Run setup again** - the script auto-detects NVM installations:
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```

---

<!-- section_id: "f3cc3b9a-a233-4ad1-a7d4-34bc115c9ebc" -->
## Permission Denied

<!-- section_id: "55940922-a88c-489e-b244-ef7af3edbc75" -->
### Symptom
```
Permission denied creating directories in /etc/mcp
```
or
```
Permission denied writing to /usr/local/share/mcp/servers
```

<!-- section_id: "61477f2b-e06a-463d-a71f-bc3bb361259e" -->
### Cause
Attempting system-level installation without appropriate permissions.

<!-- section_id: "c11b5da4-cbfe-441d-acd4-e8744dcfe810" -->
### Solution

1. **Use user-level scope instead** (recommended):
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```

2. **For system-level, use sudo** (if required):
   ```bash
   sudo python3 scripts/mcp_manager.py --scope system
   ```

3. **The script auto-falls back**: If system installation fails, it automatically attempts user-level installation.

---

<!-- section_id: "43766681-4845-433d-b48c-9d0e46a51d2d" -->
## Browser Crashes on WSLg

<!-- section_id: "93a21aac-284c-4a4e-ab14-1bb985808c37" -->
### Symptom
Chromium opens and immediately crashes when running headed browser mode on WSL2 with WSLg.

<!-- section_id: "02cf51a0-9b48-4a4a-b515-6c771c86c80e" -->
### Cause
Chromium requires explicit Wayland/Ozone configuration to run stably under WSLg's display server.

<!-- section_id: "c4b57465-9363-4b75-9671-ab37a868c4d6" -->
### Solution

1. **Run the setup script** - it auto-detects WSLg:
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```

2. **Verify Wayland flags are set** in the generated Playwright config:
   ```json
   {
     "browser": {
       "launchOptions": {
         "args": [
           "--ozone-platform=wayland",
           "--enable-features=UseOzonePlatform"
         ]
       }
     }
   }
   ```

3. **Check WSLg is functioning**:
   ```bash
   ls /mnt/wslg/runtime-dir
   echo $WAYLAND_DISPLAY
   ```

4. **Alternative: Use headless mode** if headed is not required:
   ```bash
   python3 scripts/codex_mcp_sync.py --headless
   ```

---

<!-- section_id: "8d28aadd-f39a-4528-9322-0d1b9a367205" -->
## Browser Already in Use

<!-- section_id: "fd711f66-4afc-43bd-9b99-15283aa74c6e" -->
### Symptom
```
Error: Browser is already in use
```
or
```
Error: Only one client can connect to a given MCP server instance at a time
```

<!-- section_id: "c3af1029-2d65-43a6-9b3b-5fbcc4967f19" -->
### Cause
Multiple AI tools (Codex CLI, Claude Code CLI, Gemini CLI) attempting to use Playwright MCP simultaneously. They share the same browser profile directory.

<!-- section_id: "c17e9696-d6ab-4c35-aaab-db68ed58c639" -->
### Solution

1. **Set up concurrent browser configurations**:
   ```bash
   python3 scripts/mcp_concurrent_browser.py setup
   python3 scripts/mcp_concurrent_browser.py apply-codex
   ```

2. **Restart all AI tools** after setup

3. **Verify each tool has its own config**:
   ```bash
   python3 scripts/mcp_concurrent_browser.py status
   ```

4. **Check for leftover processes**:
   ```bash
   ps aux | grep playwright
   ps aux | grep chromium
   # Kill if necessary
   pkill -f playwright
   ```

See `CONCURRENT_BROWSER_SETUP.md` for detailed multi-tool setup instructions.

---

<!-- section_id: "722f28a4-8d0f-4100-8fbc-d0c7cee2b082" -->
## MCP Server Not Responding

<!-- section_id: "cdbb7297-2c1c-475f-95e8-39461a9ffdf2" -->
### Symptom
MCP tools are not available or timeout when called.

<!-- section_id: "27db590e-b0cb-428c-bf0f-6e81adc7eb7a" -->
### Cause
- MCP server process failed to start
- Configuration file not found or malformed
- Wrapper script has incorrect permissions

<!-- section_id: "e87c6ff1-7bdc-4db7-8033-df15f043a9bb" -->
### Solution

1. **Check wrapper script permissions**:
   ```bash
   ls -la ~/.config/mcp/servers/
   # Should show executable permissions (rwxr-xr-x)
   chmod +x ~/.config/mcp/servers/*.sh
   ```

2. **Test wrapper script manually**:
   ```bash
   ~/.config/mcp/servers/mcp-playwright-generic.sh
   # Should output JSON-RPC messages
   ```

3. **Verify mcp.json syntax**:
   ```bash
   python3 -c "import json; json.load(open('~/.config/mcp/mcp.json'))"
   ```

4. **Check for missing dependencies**:
   ```bash
   npx -y @playwright/mcp@latest --help
   ```

5. **Regenerate configuration**:
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```

---

<!-- section_id: "ae26ca58-6068-431b-89fb-f3ce5f50d1c0" -->
## Environment Variables Not Set

<!-- section_id: "d97562a5-8455-4ad6-bcdc-3cd1de797390" -->
### Symptom
Browser tools work in terminal but fail when called from AI agent.

<!-- section_id: "4b0dda16-6a26-4374-b6fa-82c4ab7514b4" -->
### Cause
Wrapper scripts not properly setting environment variables, or AI agent not using the wrapper.

<!-- section_id: "699a7714-0976-4c31-b23c-e31d0b2c8f2e" -->
### Solution

1. **Inspect generated wrapper**:
   ```bash
   cat ~/.config/mcp/servers/mcp-playwright-generic.sh
   ```
   Should contain:
   ```bash
   export PATH="/home/username/.nvm/versions/node/vXX.X.X/bin:..."
   export PLAYWRIGHT_BROWSERS_PATH="/home/username/.cache/ms-playwright"
   export HOME="/home/username"
   ```

2. **Ensure mcp.json points to wrapper**:
   ```json
   {
     "mcpServers": {
       "playwright": {
         "command": "/home/username/.config/mcp/servers/mcp-playwright-generic.sh"
       }
     }
   }
   ```

3. **Regenerate wrappers**:
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```

---

<!-- section_id: "1182f1a5-ae8e-44f5-ba5a-098004bbe1da" -->
## Configuration Not Loading

<!-- section_id: "c3a51686-5c86-46ad-a015-b0b0419d1bc9" -->
### Symptom
Changes to mcp.json or config.toml do not take effect.

<!-- section_id: "f4e8b5a9-ecf8-4d33-b945-63fb241c04d6" -->
### Cause
AI agents cache configuration at startup. Changes require restart.

<!-- section_id: "487930c2-9696-4739-9f30-bdff44cc56e6" -->
### Solution

1. **Restart the AI agent/IDE** - this is mandatory after any config change

2. **Verify config file location**:
   - Claude Code CLI: `~/.config/mcp/mcp.json`
   - Codex CLI: `~/.codex/config.toml`
   - Gemini CLI: `~/.gemini/settings.json`
   - Cursor: `.cursor/mcp.json` or `~/.config/mcp/mcp.json`

3. **Check for syntax errors**:
   ```bash
   # JSON files
   python3 -c "import json; json.load(open('path/to/file.json'))"

   # TOML files
   python3 -c "import tomllib; tomllib.load(open('path/to/file.toml', 'rb'))"
   ```

4. **Verify file ownership and permissions**:
   ```bash
   ls -la ~/.config/mcp/mcp.json
   # Should be owned by your user
   ```

---

<!-- section_id: "5995a1e3-bde0-4742-9c6f-4d9c53f6f9f4" -->
## Debugging Tips

<!-- section_id: "4f4ed8d2-88cc-4668-be5f-d3d1953cc1cb" -->
### Enable Verbose Logging

1. **Check MCP server logs** (if configured):
   ```bash
   cat /tmp/mcp-chrome.log  # For chrome-devtools-mcp
   ```

2. **Run wrapper manually** to see output:
   ```bash
   ~/.config/mcp/servers/mcp-playwright-generic.sh 2>&1
   ```

<!-- section_id: "68dabcd9-ac01-4574-a163-45a0dd40a84c" -->
### Verify Installation

1. **Check all MCP servers are defined**:
   ```bash
   python3 -c "
   import json
   with open('/home/$USER/.config/mcp/mcp.json') as f:
       cfg = json.load(f)
   for name in cfg.get('mcpServers', {}):
       print(f'  - {name}')
   "
   ```

2. **Test npx packages directly**:
   ```bash
   npx -y @playwright/mcp@latest --help
   npx -y @agent-infra/mcp-server-browser --help
   npx -y tavily-mcp --help
   ```

<!-- section_id: "ef71dc1c-3556-4c4c-8654-1c8ca7459eac" -->
### Check Process State

```bash
# List running MCP-related processes
ps aux | grep -E "(playwright|mcp|chromium)"

# Check which ports are in use
ss -tlnp | grep node
```

<!-- section_id: "c53eb622-2f4b-4d33-a327-4b39ca18428c" -->
### Reset Configuration

If all else fails, reset and regenerate:

```bash
# Backup existing config
mv ~/.config/mcp ~/.config/mcp.backup

# Regenerate everything
python3 scripts/mcp_manager.py --scope user

# Restart AI agent
```

---

<!-- section_id: "39b4a4a0-a0bf-4550-8dd4-2586aa9b01c0" -->
## Getting Help

If issues persist after trying these solutions:

1. Check the main README in `setup/README.md` for detailed automation documentation
2. Review `CONCURRENT_BROWSER_SETUP.md` for multi-tool browser issues
3. Examine the fix history in `20251210_MCP_Setup_Fix.md` for past solutions
