---
resource_id: "c81cf874-b239-4174-b346-3eee96d9a661"
resource_type: "document"
resource_name: "TROUBLESHOOTING"
---
# Playwright MCP Troubleshooting Guide

This guide covers common issues encountered when using Playwright MCP with Claude Code CLI on Linux/Ubuntu.

---

<!-- section_id: "3526fa29-640e-4151-b7e0-5ebb96aff787" -->
## Browser Not Launching

<!-- section_id: "e9689338-75cd-4636-bf6b-f5445f121c48" -->
### Issue: "Browser specified in your config is not installed"

**Symptoms:**
- Error message: "Browser specified in your config is not installed"
- Browser automation tools fail immediately

**Cause:**
MCP servers run in isolated environments and do not inherit shell environment variables. The `PLAYWRIGHT_BROWSERS_PATH` is not set.

**Solutions:**

1. **Install Playwright browsers:**
   ```bash
   npx playwright install chromium
   ```

2. **Verify browser installation:**
   ```bash
   ls ~/.cache/ms-playwright/
   # Should show chromium-XXXX directory
   ```

3. **Set environment variables in MCP config:**
   ```json
   {
     "env": {
       "PLAYWRIGHT_BROWSERS_PATH": "/home/YOUR_USER/.cache/ms-playwright",
       "HOME": "/home/YOUR_USER"
     }
   }
   ```

4. **Use the MCP manager script:**
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```

<!-- section_id: "4263a01b-c201-4ca8-a512-5301b058087e" -->
### Issue: "Could not find expected browser"

**Symptoms:**
- Playwright cannot locate the Chromium executable
- Error mentions specific version not found

**Solutions:**

1. **Reinstall browsers with specific version:**
   ```bash
   npx playwright install chromium --force
   ```

2. **Check for version mismatch:**
   ```bash
   npx playwright --version
   ls ~/.cache/ms-playwright/
   ```

3. **Use explicit executable path in config:**
   ```json
   {
     "browser": {
       "launchOptions": {
         "executablePath": "/home/user/.cache/ms-playwright/chromium-1202/chrome-linux64/chrome"
       }
     }
   }
   ```

---

<!-- section_id: "505cfc12-ff0d-4977-9798-8810c82222e5" -->
## Browser Already In Use

<!-- section_id: "af3be23d-ca8f-4b59-a9e1-1b0262f71377" -->
### Issue: "Browser is already in use"

**Symptoms:**
- Cannot start new browser session
- Error when multiple AI tools try to use Playwright

**Cause:**
Another process (Codex CLI, Gemini CLI, etc.) has an active MCP server connection.

**Solutions:**

1. **Kill existing browser processes:**
   ```bash
   pkill -f "chrome.*mcp-chrome" || pkill -f "chromium.*mcp" || echo "No processes found"
   ps aux | grep -E "(playwright|chromium)" | grep -v grep
   ```

2. **Close browser in other AI tools first:**
   - Use `browser_close` tool in the other session
   - Or exit the other AI CLI completely

3. **Set up concurrent browser configs:**
   ```bash
   python3 scripts/mcp_concurrent_browser.py setup
   python3 scripts/mcp_concurrent_browser.py status
   ```

4. **Use isolated browser profiles:**
   ```json
   {
     "browser": {
       "isolated": true
     }
   }
   ```

See [CONCURRENT_BROWSER_SETUP.md](./CONCURRENT_BROWSER_SETUP.md) for detailed multi-tool setup.

---

<!-- section_id: "b9ade99d-7da0-4643-9f9c-e9cbcbecddbd" -->
## Permission Errors

<!-- section_id: "017b5f52-22e0-4feb-b658-07acc22defcc" -->
### Issue: "Permission denied" when launching browser

**Symptoms:**
- Browser fails to start with permission errors
- Sandbox-related errors

**Solutions:**

1. **Fix Chromium sandbox permissions:**
   ```bash
   # Find the chrome-sandbox file
   find ~/.cache/ms-playwright -name "chrome-sandbox" 2>/dev/null

   # Set correct permissions (if needed)
   chmod 4755 ~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome-sandbox
   ```

2. **Disable sandbox (not recommended for production):**
   ```json
   {
     "browser": {
       "launchOptions": {
         "args": ["--no-sandbox", "--disable-setuid-sandbox"]
       }
     }
   }
   ```

3. **Run with appropriate user:**
   Ensure you are running as the same user who installed Playwright browsers.

<!-- section_id: "7171ac3a-17a5-403a-adba-2136f29b3481" -->
### Issue: "Cannot write to browser profile directory"

**Solutions:**

1. **Check directory permissions:**
   ```bash
   ls -la ~/.cache/ms-playwright/
   ```

2. **Create profile directory manually:**
   ```bash
   mkdir -p ~/.cache/ms-playwright/mcp-chromium-profile
   chmod 755 ~/.cache/ms-playwright/mcp-chromium-profile
   ```

---

<!-- section_id: "9fc36903-0bde-48cf-b707-24a4fbf31422" -->
## Headless vs Headed Mode Issues

<!-- section_id: "6d311618-1a67-4908-8bb9-1ee26d18ff2b" -->
### Issue: Browser window does not appear (headed mode)

**Symptoms:**
- Configured for headed mode but no window shows
- Browser starts but is invisible

**Cause:**
Display environment variable not set or X11/Wayland not configured.

**Solutions:**

1. **Set DISPLAY variable:**
   ```bash
   export DISPLAY=:0
   # Or in MCP config:
   {
     "env": {
       "DISPLAY": ":0"
     }
   }
   ```

2. **For WSLg, use Wayland/Ozone flags:**
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

3. **Verify X11/Wayland is running:**
   ```bash
   # For X11
   echo $DISPLAY
   xdpyinfo | head -5

   # For Wayland
   echo $WAYLAND_DISPLAY
   ```

<!-- section_id: "7ff1f459-5e8c-4bc5-8c84-af7ae4963519" -->
### Issue: Browser crashes immediately in headed mode (WSLg)

**Cause:**
Chromium on WSLg requires specific Wayland flags.

**Solution:**
Add Ozone platform flags (see above) or use headless mode:
```bash
npx -y @playwright/mcp@latest --headless
```

<!-- section_id: "e4e56269-ab10-4058-858c-1b06159d1d85" -->
### Issue: Screenshots are blank or incorrect in headless mode

**Solutions:**

1. **Increase viewport size:**
   ```json
   {
     "browser": {
       "launchOptions": {
         "viewport": { "width": 1920, "height": 1080 }
       }
     }
   }
   ```

2. **Wait for page load:**
   ```
   mcp__playwright__browser_wait_for(time=2)
   mcp__playwright__browser_take_screenshot()
   ```

---

<!-- section_id: "55625da1-9d70-4181-823d-67efc1458e1d" -->
## Path Configuration Problems

<!-- section_id: "72ec48d7-36cc-40bf-8dce-c469b004103c" -->
### Issue: "npx: command not found"

**Symptoms:**
- MCP server fails to start
- Error indicates npx cannot be found

**Cause:**
Node.js/npm not in PATH for MCP server process.

**Solutions:**

1. **Verify Node.js installation:**
   ```bash
   which node
   which npx
   node --version
   ```

2. **Add Node.js to PATH in wrapper script:**
   The `mcp_manager.py` script handles this automatically:
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```

3. **Manual PATH configuration:**
   ```json
   {
     "env": {
       "PATH": "/home/user/.nvm/versions/node/v20.10.0/bin:/usr/local/bin:/usr/bin:/bin"
     }
   }
   ```

<!-- section_id: "0b3fd6de-22eb-46b7-b48b-f5b64f631b8e" -->
### Issue: "PLAYWRIGHT_BROWSERS_PATH not set"

**Solutions:**

1. **Set in MCP config:**
   ```json
   {
     "env": {
       "PLAYWRIGHT_BROWSERS_PATH": "/home/user/.cache/ms-playwright"
     }
   }
   ```

2. **Use wrapper scripts:**
   ```bash
   python3 scripts/mcp_manager.py --scope user
   ```
   This creates wrapper scripts that set all required environment variables.

---

<!-- section_id: "86c9a37e-d699-4aaa-8526-0298594ff467" -->
## MCP Server Connection Issues

<!-- section_id: "227a5347-4228-4fcf-8fb1-fbe67c45e981" -->
### Issue: "MCP server not responding"

**Symptoms:**
- Tools timeout
- No response from browser tools

**Solutions:**

1. **Restart Claude Code CLI:**
   ```bash
   # Exit current session and restart
   exit
   claude
   ```

2. **Check MCP server status:**
   ```bash
   claude mcp list
   ```

3. **Verify MCP configuration:**
   ```bash
   cat ~/.config/claude-code/mcp.json
   ```

4. **Check for process conflicts:**
   ```bash
   ps aux | grep -E "(npx|playwright|mcp)" | grep -v grep
   ```

<!-- section_id: "4c0f6592-4613-4d37-b985-55085584ad18" -->
### Issue: "Cannot connect to browser" after timeout

**Solutions:**

1. **Increase connection timeout:**
   ```json
   {
     "browser": {
       "launchOptions": {
         "timeout": 60000
       }
     }
   }
   ```

2. **Check system resources:**
   ```bash
   free -h
   df -h
   ```

---

<!-- section_id: "c03dd215-f01a-442e-8617-1f73fe583200" -->
## Common Error Messages Reference

| Error Message | Likely Cause | Quick Fix |
|--------------|--------------|-----------|
| "Browser not installed" | Missing browsers | `npx playwright install chromium` |
| "Browser already in use" | Concurrent access | Kill existing processes or use concurrent setup |
| "Permission denied" | Sandbox/file permissions | Check/fix permissions |
| "npx: not found" | Node.js not in PATH | Install Node.js or fix PATH |
| "Cannot find module" | npm package issue | `npm cache clean --force && npx playwright install` |
| "DISPLAY not set" | Missing display env | Set DISPLAY=:0 or use headless |
| "Timeout" | Slow startup/network | Increase timeout or check network |

---

<!-- section_id: "0dd12191-29b7-4614-b635-15fe2dca2471" -->
## Getting Help

1. **Check Playwright logs:**
   ```bash
   DEBUG=pw:* npx -y @playwright/mcp@latest
   ```

2. **Verify configuration:**
   ```bash
   python3 scripts/mcp_concurrent_browser.py status
   ```

3. **Review setup documentation:**
   - [Setup README](./README.md)
   - [Concurrent Browser Setup](./CONCURRENT_BROWSER_SETUP.md)
   - [MCP Setup Fix](./20251210_MCP_Setup_Fix.md)

---

**Last Updated**: 2026-01-13
**Platform**: Linux/Ubuntu
**AI Tool**: Claude Code CLI
