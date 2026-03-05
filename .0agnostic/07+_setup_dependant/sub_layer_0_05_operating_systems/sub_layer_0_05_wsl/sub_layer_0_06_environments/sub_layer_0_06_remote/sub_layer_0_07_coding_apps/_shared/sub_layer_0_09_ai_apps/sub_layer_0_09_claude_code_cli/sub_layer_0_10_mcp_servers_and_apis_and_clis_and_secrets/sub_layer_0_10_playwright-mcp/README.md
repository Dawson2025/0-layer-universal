---
resource_id: "b4cee60c-3d25-4560-8b6c-8349357139bd"
resource_type: "readme
document"
resource_name: "README"
---
# Playwright MCP (Claude Code CLI on WSL/WSLg)

<!-- section_id: "bdf13bf9-cd35-47d0-aca1-26f47882dbc5" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/`

<!-- section_id: "b2d20b93-f657-40cd-b46f-b7416519455b" -->
## Status
✅ **WORKING** (as of 2025-12-13)

<!-- section_id: "27555933-3863-4831-a8a7-3e28147b9018" -->
## WSL/WSLg Requirements (Headed)

Ensure WSLg runtime environment is present in the MCP server process:
- `DISPLAY=:0`
- `WAYLAND_DISPLAY=wayland-0`
- `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`

<!-- section_id: "d8570c29-50c3-406f-a34d-cbfb87ee8045" -->
## Claude Code CLI Configuration

<!-- section_id: "11712e92-efa0-4749-b7d7-e63c9c5f949a" -->
### MCP Server Setup

Claude Code CLI uses a different configuration approach than Codex. The Playwright MCP server is configured in the Claude Code settings.

**Configuration Location**: Managed by Claude Code's MCP system (not a manual config file)

**Key Configuration**:
- `isolated: true` - **REQUIRED** to allow multiple browser instances
- `launchOptions.headless: false` - For headed browser in WSLg
- `launchOptions.args`: `["--ozone-platform=wayland","--enable-features=UseOzonePlatform"]` - Wayland support
- `launchOptions.executablePath`: `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`

<!-- section_id: "ddcae0f5-5789-4720-a412-583528329f1e" -->
## Known Issues

<!-- section_id: "07cb1d76-e681-449e-80e3-0594e4d3b1d7" -->
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

<!-- section_id: "7390e60f-9cb4-4912-9ab4-400e2149de70" -->
### Issue: Cannot Access Browser Opened in Another Session

**Symptom**: Browser opened in Codex session is not accessible from Claude Code session (and vice versa).

**Cause**: Even with `isolated: true`, each MCP client maintains its own browser session context.

**Expected Behavior**: Each AI tool (Codex, Claude Code) manages its own isolated browser instance when `isolated: true` is configured.

<!-- section_id: "1cd03625-acd6-4a8a-88f4-f44f4747ac1d" -->
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

<!-- section_id: "fd0e94c9-2326-42af-8f1e-2705992147e5" -->
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

<!-- section_id: "a6aad2da-d34b-4545-98be-3ef3dbc4460f" -->
## Comparison to Codex CLI

| Aspect | Codex CLI | Claude Code CLI |
|--------|-----------|-----------------|
| Config file | `~/.codex/config.toml` | Managed by Claude Code |
| Config automation | `codex_mcp_sync.py` | Manual / built-in |
| Browser isolation | `isolated: true` in JSON | `isolated: true` in config |
| WSLg env vars | Set in TOML `[env]` | Inherited from shell |
| Browser sharing | Not supported | Not supported |

<!-- section_id: "792a72c0-c725-45fa-9a73-5eaba2006f4f" -->
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

<!-- section_id: "ee75fff7-fc10-479e-b2b4-26962584059e" -->
## Best Practices

1. **Use concurrent browser setup** (recommended) - enables simultaneous browser use across AI tools
2. **Use `isolated: true`** to prevent profile conflicts
3. **Verify WSLg env vars** are present in the shell before starting Claude Code
4. **Each tool has its own browser instance** - browser state is not shared between tools

<!-- section_id: "9efd0585-3366-41c5-a239-94e35ba836ca" -->
## Related Documentation

- Codex Playwright MCP setup: `../../../codex_cli/0.05_mcp_servers/playwright-mcp/README.md`
- WSL/WSLg browser setup: `../../../../0.07_apps_browsers_extensions_setup/`

---

**Last Updated**: 2025-12-13
**Tested With**: Claude Code CLI on WSL2 (Ubuntu 22.04) with WSLg
**Status**: ✅ Working with `isolated: true` configuration
