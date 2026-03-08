---
resource_id: "312f5c68-6fa1-4a19-b332-339ce6364991"
resource_type: "readme_document"
resource_name: "README"
---
# Playwright MCP (Claude Code CLI on WSL/WSLg)

<!-- section_id: "ea15e8ec-abc1-4021-b753-2f414f507e8b" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/`

<!-- section_id: "d2c52918-71b5-4344-93b7-384a21c261fb" -->
## Status
✅ **WORKING** (as of 2025-12-13)

<!-- section_id: "5f940aec-bc46-46d7-bd8e-25ada3842d0a" -->
## WSL/WSLg Requirements (Headed)

Ensure WSLg runtime environment is present in the MCP server process:
- `DISPLAY=:0`
- `WAYLAND_DISPLAY=wayland-0`
- `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`

<!-- section_id: "6718a41f-130f-473c-8fd2-16143c348ef7" -->
## Claude Code CLI Configuration

<!-- section_id: "16edb938-5bc4-489c-895f-74ccdf6a6720" -->
### MCP Server Setup

Claude Code CLI uses a different configuration approach than Codex. The Playwright MCP server is configured in the Claude Code settings.

**Configuration Location**: Managed by Claude Code's MCP system (not a manual config file)

**Key Configuration**:
- `isolated: true` - **REQUIRED** to allow multiple browser instances
- `launchOptions.headless: false` - For headed browser in WSLg
- `launchOptions.args`: `["--ozone-platform=wayland","--enable-features=UseOzonePlatform"]` - Wayland support
- `launchOptions.executablePath`: `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`

<!-- section_id: "58fcf3a5-361b-436c-8467-906a3c5a501e" -->
## Known Issues

<!-- section_id: "9a806387-235c-4399-8830-0a165e641097" -->
### Issue: "Browser is already in use" Error

**Symptom**:
```
Error: Browser is already in use for /home/dawson/.cache/ms-playwright/mcp-chromium-ec5e1e8,
use --isolated to run multiple instances of the same browser
```

**Cause**: Multiple MCP clients (e.g., Claude Code CLI and Codex CLI) trying to access the same browser profile simultaneously.

**Resolution**:
1. Ensure `isolated: true` is set in the Playwright MCP config
2. Close other MCP sessions using the browser
3. If the error persists despite `isolated: true`, it indicates an active browser lock from another session

<!-- section_id: "5322cd25-8786-4987-b8d9-86510633174e" -->
### Issue: Cannot Access Browser Opened in Another Session

**Symptom**: Browser opened in Codex session is not accessible from Claude Code session (and vice versa).

**Cause**: Even with `isolated: true`, each MCP client maintains its own browser session context.

**Expected Behavior**: Each AI tool (Codex, Claude Code) manages its own isolated browser instance when `isolated: true` is configured.

<!-- section_id: "9c6fb93c-9040-47a8-ba07-1cc67daf0be6" -->
## Verification

To verify Playwright MCP is working in Claude Code CLI:

```bash
# Should succeed (opens a new browser window in WSLg)
mcp__playwright__browser_navigate(url="https://example.com")

# Should capture the page
mcp__playwright__browser_snapshot()

# Should close cleanly
mcp__playwright__browser_close()
```

<!-- section_id: "beeeb5c0-36d0-493e-a419-45304581d9d9" -->
## Environment Variables

The MCP server process must have access to WSLg environment variables. Claude Code should automatically inherit these from the shell environment.

If browser fails to launch, verify:
```bash
echo $DISPLAY
echo $WAYLAND_DISPLAY
echo $XDG_RUNTIME_DIR
```

Should output:
```
:0
wayland-0
/mnt/wslg/runtime-dir
```

<!-- section_id: "5e5855c9-a90a-4c16-b964-d29d96eb5960" -->
## Comparison to Codex CLI

| Aspect | Codex CLI | Claude Code CLI |
|--------|-----------|-----------------|
| Config file | `~/.codex/config.toml` | Managed by Claude Code |
| Config automation | `codex_mcp_sync.py` | Manual / built-in |
| Browser isolation | `isolated: true` in JSON | `isolated: true` in config |
| WSLg env vars | Set in TOML `[env]` | Inherited from shell |
| Browser sharing | Not supported | Not supported |

<!-- section_id: "fa7463a3-860d-43e1-840d-4327eec28f62" -->
## Concurrent Browser Setup (NEW)

To enable **simultaneous** Playwright MCP browser use in both Codex CLI and Claude Code CLI:

```bash
# Navigate to automation scripts
cd /home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts

# Set up OS+tool-specific concurrent browser configs (auto-detects OS)
python3 mcp_concurrent_browser.py setup --tools codex claude

# Update Codex CLI config to use the OS+tool-specific Playwright config
python3 mcp_concurrent_browser.py apply-codex

# Verify setup (WSL)
python3 mcp_concurrent_browser.py status --os wsl
```

**What this does:**
- Creates separate Playwright configs: `playwright.wsl_codex.json` and `playwright.wsl_claude.json`
- Assigns unique browser profile directories per OS+tool combination
- Enables `isolated: true` in both configs
- Automatically adds WSLg Wayland/Ozone flags

**Documentation:** See [CONCURRENT_BROWSER_SETUP.md](../../../../../../0.06_automation/CONCURRENT_BROWSER_SETUP.md)

<!-- section_id: "54393188-25e0-4f99-b1c8-fac562955c62" -->
## Best Practices

1. **Use concurrent browser setup** (recommended) - enables simultaneous browser use across AI tools
2. **Use `isolated: true`** to prevent profile conflicts
3. **Verify WSLg env vars** are present in the shell before starting Claude Code
4. **Each tool has its own browser instance** - browser state is not shared between tools

<!-- section_id: "9d3998d9-1cb4-4a90-a7a3-be8d89ab0942" -->
## Related Documentation

- Codex Playwright MCP setup: `../../../codex_cli/0.05_mcp_servers/playwright-mcp/README.md`
- WSL/WSLg browser setup: `../../../../0.07_apps_browsers_extensions_setup/`

---

**Last Updated**: 2025-12-13
**Tested With**: Claude Code CLI on WSL2 (Ubuntu 22.04) with WSLg
**Status**: ✅ Working with `isolated: true` configuration
