# Browser MCP Troubleshooting Guide

This document covers common issues encountered when using Browser MCP with Claude Code CLI on Linux/Ubuntu systems.

---

## Connection Failures

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

## Browser Detection Problems

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

## Tab Management Issues

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

## Display and Rendering Issues

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

## Performance Issues

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

## Diagnostic Commands

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

### Verbose Logging

Enable debug output:
```bash
export DEBUG=pw:api
export DEBUG=pw:browser*
```

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
