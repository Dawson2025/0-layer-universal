---
resource_id: "50fcdfb4-6fce-426f-80ba-1586b5e41f7c"
resource_type: "document"
resource_name: "TROUBLESHOOTING"
---
# Browser MCP Troubleshooting Guide

This document covers common issues encountered when using Browser MCP with Claude Code CLI on Linux/Ubuntu systems.

---

<!-- section_id: "f13a5049-360c-4f6c-98e8-5e2df12fb8a8" -->
## Connection Failures

<!-- section_id: "dc29a4c9-b40c-4363-9eb3-f9e1db4dfdc6" -->
### Issue: "MCP server failed to start"

**Symptoms:**
- Error message indicating the MCP server process could not be spawned
- Browser tools are not available in Claude Code CLI

**Causes and Solutions:**

1. **npx not found in PATH**
   ```bash
   # Check if npx is available
   which npx

   # If not found, ensure Node.js is installed
   node --version
   npm --version

   # If using nvm, ensure it's loaded
   source ~/.nvm/nvm.sh
   nvm use default
   ```

2. **Package installation failure**
   ```bash
   # Clear npm cache and retry
   npm cache clean --force
   npx -y @agent-infra/mcp-server-browser --help
   ```

3. **Configuration file syntax error**
   ```bash
   # Validate JSON syntax
   python3 -m json.tool ~/.config/mcp/mcp.json

   # Common issues:
   # - Trailing commas
   # - Missing quotes around strings
   # - Unescaped backslashes in paths
   ```

<!-- section_id: "9afaf577-1664-4388-9793-6ca0074f36e6" -->
### Issue: "Connection refused" or "Socket error"

**Symptoms:**
- MCP server starts but Claude Code CLI cannot connect
- Intermittent connection drops

**Solutions:**

1. **Check for port conflicts**
   ```bash
   # List processes using common MCP ports
   netstat -tlnp | grep -E ":(3000|8080|9222)"
   ```

2. **Restart the MCP server**
   ```bash
   # Kill existing browser processes
   pkill -f "@agent-infra/mcp-server-browser"

   # Restart Claude Code CLI
   ```

3. **Check system resources**
   ```bash
   # Ensure sufficient memory
   free -h

   # Check CPU load
   top -bn1 | head -20
   ```

---

<!-- section_id: "31bd5d42-a154-4691-b0ec-554b97f911e2" -->
## Browser Detection Problems

<!-- section_id: "8ad6d765-cdca-4691-8895-52cf46ec55bd" -->
### Issue: "Browser specified in your config is not installed"

**Symptoms:**
- Error when attempting to launch browser
- Tools return "browser not found" errors

**Root Cause:**
MCP servers run via npx do not inherit shell environment variables, preventing them from locating installed browsers.

**Solution:**

1. **Ensure PLAYWRIGHT_BROWSERS_PATH is set in MCP config**
   ```json
   {
     "mcpServers": {
       "browser": {
         "command": "npx",
         "args": ["-y", "@agent-infra/mcp-server-browser"],
         "env": {
           "PLAYWRIGHT_BROWSERS_PATH": "/home/YOUR_USER/.cache/ms-playwright",
           "HOME": "/home/YOUR_USER"
         }
       }
     }
   }
   ```

2. **Verify browser installation**
   ```bash
   # Check if Chromium is installed
   ls -la ~/.cache/ms-playwright/

   # Should show directories like:
   # chromium-1140/
   # chromium_headless_shell-1140/
   ```

3. **Reinstall browsers if missing**
   ```bash
   npx playwright install chromium
   npx playwright install chromium --with-deps  # Also installs system dependencies
   ```

<!-- section_id: "1ae8a347-c7b2-4e41-854f-78d5de5740e3" -->
### Issue: "Browser executable not found at path"

**Symptoms:**
- Specific path error mentioning a Chromium version
- Browser was working before but stopped after update

**Solutions:**

1. **Check the actual browser version installed**
   ```bash
   ls ~/.cache/ms-playwright/ | grep chromium
   # Example output: chromium-1140, chromium-1202
   ```

2. **Update explicit path in config (if using executablePath)**
   ```json
   {
     "browser": {
       "launchOptions": {
         "executablePath": "/home/user/.cache/ms-playwright/chromium-1202/chrome-linux64/chrome"
       }
     }
   }
   ```

3. **Remove old versions and reinstall**
   ```bash
   rm -rf ~/.cache/ms-playwright/chromium-*
   npx playwright install chromium
   ```

<!-- section_id: "f28cbc83-45ee-43e4-a6d1-a325fd958a07" -->
### Issue: Browser crashes immediately on launch

**Symptoms:**
- Browser window appears briefly then closes
- Error mentioning display or GPU issues

**Solutions (Linux Desktop):**

1. **Disable GPU acceleration**
   ```json
   {
     "browser": {
       "launchOptions": {
         "args": ["--disable-gpu", "--disable-software-rasterizer"]
       }
     }
   }
   ```

2. **For WSLg environments**
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

3. **Check DISPLAY variable**
   ```bash
   echo $DISPLAY
   # Should be :0 or :1

   # For WSLg
   echo $WAYLAND_DISPLAY
   ```

---

<!-- section_id: "2423291f-b685-4cbd-ac7a-6a67005e07a7" -->
## Tab Management Issues

<!-- section_id: "9eb960d9-8caa-4a8c-8cc8-a30c344b9f9b" -->
### Issue: "Browser is already in use"

**Symptoms:**
- Cannot open new browser sessions
- Error when multiple AI tools try to use browser simultaneously

**Root Cause:**
MCP server process locking - only one client can connect to a given MCP server instance at a time.

**Solutions:**

1. **Kill existing browser processes**
   ```bash
   pkill -f "chrome.*mcp-chrome"
   pkill -f "chromium.*mcp"
   pkill -f "@agent-infra/mcp-server-browser"
   ```

2. **Use isolated configurations for multiple tools**
   See [CONCURRENT_BROWSER_SETUP.md](./CONCURRENT_BROWSER_SETUP.md) for setting up tool-specific browser profiles.

3. **Enable isolated mode in config**
   ```json
   {
     "browser": {
       "isolated": true,
       "browserName": "chromium"
     }
   }
   ```

<!-- section_id: "2061496a-8894-44d1-b5a9-542175aa0f6b" -->
### Issue: "Tab not found" or "Invalid tab ID"

**Symptoms:**
- Operations fail with tab reference errors
- Browser appears to be running but tabs are not accessible

**Solutions:**

1. **List current tabs**
   ```
   Use browser_tabs with action: "list" to see available tabs
   ```

2. **Create a new tab if needed**
   ```
   Use browser_tabs with action: "new" to create a fresh tab
   ```

3. **Check for stale tab references**
   - Tab IDs may become invalid after navigation errors
   - Get fresh tab list before operations

<!-- section_id: "dbcf639c-3711-4301-8995-fa03390a343d" -->
### Issue: Tab operations hang or timeout

**Symptoms:**
- Tab commands take a long time and eventually fail
- Browser appears frozen

**Solutions:**

1. **Check for JavaScript dialogs/alerts**
   ```
   Use browser_handle_dialog to dismiss any blocking dialogs
   ```

2. **Check for slow page loads**
   ```bash
   # Increase timeout in config
   {
     "browser": {
       "launchOptions": {
         "timeout": 60000
       }
     }
   }
   ```

3. **Force close and restart**
   ```bash
   pkill -9 chromium
   # Then restart the MCP session
   ```

---

<!-- section_id: "62b76cc1-10ab-4295-bf42-84abc094bde9" -->
## Display and Rendering Issues

<!-- section_id: "8b00a99d-1fd2-434e-b3ef-f40dcf59ca99" -->
### Issue: "Cannot open display" (Linux)

**Symptoms:**
- Browser fails to launch with X11/display errors
- Headed mode does not work

**Solutions:**

1. **Verify X11 session**
   ```bash
   echo $DISPLAY
   xdpyinfo | head -5  # Should show display info
   ```

2. **Try Xvfb for headless display**
   ```bash
   # Install Xvfb
   sudo apt install xvfb

   # Run with virtual display
   Xvfb :99 -screen 0 1920x1080x24 &
   export DISPLAY=:99
   ```

3. **Switch to headless mode**
   ```json
   {
     "browser": {
       "launchOptions": {
         "headless": true
       }
     }
   }
   ```

<!-- section_id: "3c95060d-6159-41d5-8cf3-54aa6546c222" -->
### Issue: Screenshots are blank or black

**Symptoms:**
- Screenshot captures return empty images
- Page appears to load but screenshots show nothing

**Solutions:**

1. **Wait for page to fully render**
   ```
   Use browser_wait_for with text or time before taking screenshot
   ```

2. **Disable headless for debugging**
   ```json
   {
     "browser": {
       "launchOptions": {
         "headless": false
       }
     }
   }
   ```

3. **Check page content**
   ```
   Use browser_snapshot to verify page has content
   ```

---

<!-- section_id: "3715743f-8ca4-45f7-bc7a-0c4aaa0d0116" -->
## Performance Issues

<!-- section_id: "834c1780-0b73-4a9c-a544-317ffb2ba10c" -->
### Issue: Browser operations are slow

**Symptoms:**
- Navigation takes unusually long
- All browser commands have high latency

**Solutions:**

1. **Reduce page complexity**
   ```
   Disable JavaScript-heavy features when possible
   ```

2. **Use headless mode**
   - Headless is generally faster than headed

3. **Clear browser cache**
   ```bash
   rm -rf ~/.cache/ms-playwright/mcp-chromium-*
   ```

4. **Check system resources**
   ```bash
   free -h
   df -h
   ```

<!-- section_id: "6cc69177-aafa-452f-b6cb-2f858466a2c1" -->
### Issue: Memory leak / high memory usage

**Symptoms:**
- System becomes slow over time
- Browser process memory grows continuously

**Solutions:**

1. **Close unused tabs**
   ```
   Use browser_tabs action: "close" for completed tabs
   ```

2. **Restart browser periodically**
   ```
   Use browser_close to cleanly shutdown, then reopen
   ```

3. **Monitor memory**
   ```bash
   ps aux | grep chromium | awk '{sum+=$6} END {print sum/1024 "MB"}'
   ```

---

<!-- section_id: "8b87674a-d2a0-4f5d-a254-89ac0481e0f3" -->
## Diagnostic Commands

<!-- section_id: "18678f56-5fda-40dd-b3a3-6e76aa33a87d" -->
### Quick Health Check

```bash
# 1. Check Node.js/npm
node --version && npm --version

# 2. Check Playwright browsers
ls -la ~/.cache/ms-playwright/

# 3. Check display
echo "DISPLAY=$DISPLAY"

# 4. Check for running browser processes
ps aux | grep -E "(chromium|chrome|playwright)" | grep -v grep

# 5. Validate MCP config
python3 -m json.tool ~/.config/mcp/mcp.json > /dev/null && echo "Config OK"
```

<!-- section_id: "731a9a8a-462d-4af7-a079-fdc2d3ee0d5f" -->
### Verbose Logging

Enable debug output:
```bash
export DEBUG=pw:api
export DEBUG=pw:browser*
```

<!-- section_id: "1578cd3b-81d0-4073-a583-fff7d9c549c5" -->
### Reset to Clean State

```bash
# Kill all browser processes
pkill -f chromium
pkill -f "mcp-server-browser"

# Clear browser cache
rm -rf ~/.cache/ms-playwright/mcp-*

# Reinstall browsers
npx playwright install chromium --with-deps

# Restart Claude Code CLI
```

---

<!-- section_id: "1106ff2b-c5b9-41cb-9df8-0ab87748901c" -->
## Getting Help

If issues persist after trying these solutions:

1. **Check existing documentation**
   - [README.md](../README.md)
   - [CONCURRENT_BROWSER_SETUP.md](./CONCURRENT_BROWSER_SETUP.md)
   - [MCP Setup Fix](./20251210_MCP_Setup_Fix.md)

2. **Collect diagnostic information**
   ```bash
   # System info
   uname -a
   node --version

   # Browser version
   ls ~/.cache/ms-playwright/ | head -5

   # MCP config (sanitized)
   cat ~/.config/mcp/mcp.json | grep -v "key\|token\|secret"
   ```

3. **Review error logs**
   - Claude Code CLI output
   - System logs: `journalctl --user -n 50`

---

**Last Updated**: 2026-01-13
**Applies To**: Browser MCP on Linux/Ubuntu with Claude Code CLI
