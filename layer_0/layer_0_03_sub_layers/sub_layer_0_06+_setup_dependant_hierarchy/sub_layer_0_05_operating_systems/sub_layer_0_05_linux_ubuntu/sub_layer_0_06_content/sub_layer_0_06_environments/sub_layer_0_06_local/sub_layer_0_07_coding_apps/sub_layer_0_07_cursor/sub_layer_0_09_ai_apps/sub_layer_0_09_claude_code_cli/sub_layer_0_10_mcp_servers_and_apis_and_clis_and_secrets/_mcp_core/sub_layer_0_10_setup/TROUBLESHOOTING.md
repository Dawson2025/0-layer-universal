# MCP Setup Troubleshooting Guide

Common issues encountered during MCP server setup and their solutions.

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

## Browser Not Found Errors

### Symptom
```
Error: Browser specified in your config is not installed
```

### Cause
MCP servers run via `npx` in isolated environments and do not inherit shell environment variables. The `PLAYWRIGHT_BROWSERS_PATH` and `HOME` variables are not passed to the MCP server process.

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

## npx Not Found

### Symptom
```
npx: command not found
```
or
```
Warning: 'npx' not found in system PATH
```

### Cause
Node.js is not installed or not in the system PATH. This commonly happens with NVM (Node Version Manager) installations.

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

## Permission Denied

### Symptom
```
Permission denied creating directories in /etc/mcp
```
or
```
Permission denied writing to /usr/local/share/mcp/servers
```

### Cause
Attempting system-level installation without appropriate permissions.

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

## Browser Crashes on WSLg

### Symptom
Chromium opens and immediately crashes when running headed browser mode on WSL2 with WSLg.

### Cause
Chromium requires explicit Wayland/Ozone configuration to run stably under WSLg's display server.

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

## Browser Already in Use

### Symptom
```
Error: Browser is already in use
```
or
```
Error: Only one client can connect to a given MCP server instance at a time
```

### Cause
Multiple AI tools (Codex CLI, Claude Code CLI, Gemini CLI) attempting to use Playwright MCP simultaneously. They share the same browser profile directory.

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

## MCP Server Not Responding

### Symptom
MCP tools are not available or timeout when called.

### Cause
- MCP server process failed to start
- Configuration file not found or malformed
- Wrapper script has incorrect permissions

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

## Environment Variables Not Set

### Symptom
Browser tools work in terminal but fail when called from AI agent.

### Cause
Wrapper scripts not properly setting environment variables, or AI agent not using the wrapper.

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

## Configuration Not Loading

### Symptom
Changes to mcp.json or config.toml do not take effect.

### Cause
AI agents cache configuration at startup. Changes require restart.

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

## Debugging Tips

### Enable Verbose Logging

1. **Check MCP server logs** (if configured):
   ```bash
   cat /tmp/mcp-chrome.log  # For chrome-devtools-mcp
   ```

2. **Run wrapper manually** to see output:
   ```bash
   ~/.config/mcp/servers/mcp-playwright-generic.sh 2>&1
   ```

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

### Check Process State

```bash
# List running MCP-related processes
ps aux | grep -E "(playwright|mcp|chromium)"

# Check which ports are in use
ss -tlnp | grep node
```

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

## Getting Help

If issues persist after trying these solutions:

1. Check the main README in `setup/README.md` for detailed automation documentation
2. Review `CONCURRENT_BROWSER_SETUP.md` for multi-tool browser issues
3. Examine the fix history in `20251210_MCP_Setup_Fix.md` for past solutions
