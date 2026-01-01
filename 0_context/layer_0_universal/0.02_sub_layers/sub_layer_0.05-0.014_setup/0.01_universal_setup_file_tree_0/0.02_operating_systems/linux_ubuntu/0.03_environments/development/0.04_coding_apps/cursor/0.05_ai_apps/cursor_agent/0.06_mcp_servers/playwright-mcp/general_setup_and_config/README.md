# Playwright MCP Setup: Linux Ubuntu + Cursor + Cursor Agent

This is the setup documentation for **Playwright MCP** in the following environment:
- **OS**: Linux Ubuntu
- **Environment**: Development
- **Coding App**: Cursor IDE
- **AI App**: Cursor Agent
- **MCP Server**: Playwright MCP

## Known Issues

### CRITICAL: Playwright MCP Tools Not Exposed in Cursor IDE on Linux

**Issue**: Playwright MCP server connects successfully and reports tools, but Cursor IDE fails to expose these tools to the AI agent on Linux (and also Windows/WSL). This is a Cursor IDE bug affecting versions 2.0.77+.

**Evidence**:
- MCP server shows as connected in Cursor settings
- Server logs show successful initialization
- Tools are NOT available to the AI agent
- Affects Linux, Windows, and WSL equally (not Linux-specific)

**Workaround**: Use `@agent-infra/mcp-server-browser` (browser-mcp) instead:
- Install: `npm install -g @agent-infra/mcp-server-browser`
- Configure in `.cursor/config.json` or `~/.cursor/config.json`
- Tools: `mcp_browser_*` prefix instead of `mcp__playwright__*`
- Works reliably on Linux/Ubuntu with Cursor

### Browser Path Detection Issues

**Issue**: Playwright cannot auto-detect browser paths on Linux

**Solution**: Always specify explicit `--executable-path` in MCP config:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp-server",
        "--executable-path",
        "/usr/bin/chromium-browser"
      ]
    }
  }
}
```

Common browser paths on Ubuntu:
- Chromium: `/usr/bin/chromium-browser`
- Chrome: `/usr/bin/google-chrome`
- Firefox: `/usr/bin/firefox`

### Display Server Requirements

**Issue**: Headed browser automation requires display server

**Solution**:
- For WSL: Ensure WSLg is enabled (Windows 11)
- For native Linux: X11 or Wayland display server
- For headless: Add `--headless` arg to Playwright config

## Setup Steps

1. **Install Playwright MCP** (if you still want to try):
   ```bash
   npm install -g @playwright/mcp-server
   ```

2. **Install browsers**:
   ```bash
   npx playwright install chromium
   # Or use system browser
   sudo apt install chromium-browser
   ```

3. **Configure in Cursor** (`.cursor/config.json`):
   ```json
   {
     "mcpServers": {
       "playwright": {
         "command": "npx",
         "args": [
           "@playwright/mcp-server",
           "--executable-path",
           "/usr/bin/chromium-browser"
         ],
         "env": {
           "DISPLAY": ":0"
         }
       }
     }
   }
   ```

4. **Test connection**:
   - Restart Cursor
   - Check MCP servers in settings
   - Verify tools are exposed (they likely WON'T be)

5. **Switch to browser-mcp** (recommended):
   ```bash
   npm install -g @agent-infra/mcp-server-browser
   ```

   Update config:
   ```json
   {
     "mcpServers": {
       "browser": {
         "command": "mcp-server-browser"
       }
     }
   }
   ```

## Links to Detailed Documentation

- **sub_layer_0.10_mcp_servers_and_tools_setup/0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/linux_ubuntu/0.04_ai_apps/cursor_agent/0.05_mcp_servers/playwright-mcp/**
- **sub_layer_0.09_ai_apps_tools_setup/** for Cursor-specific setup

## Related Issues

See also:
- `0.06_mcp_servers/_mcp_core/general_setup_and_config/` - Core MCP tool exposure issues
- `0.02_operating_systems/linux_ubuntu/README.md` - Linux-specific MCP limitations
