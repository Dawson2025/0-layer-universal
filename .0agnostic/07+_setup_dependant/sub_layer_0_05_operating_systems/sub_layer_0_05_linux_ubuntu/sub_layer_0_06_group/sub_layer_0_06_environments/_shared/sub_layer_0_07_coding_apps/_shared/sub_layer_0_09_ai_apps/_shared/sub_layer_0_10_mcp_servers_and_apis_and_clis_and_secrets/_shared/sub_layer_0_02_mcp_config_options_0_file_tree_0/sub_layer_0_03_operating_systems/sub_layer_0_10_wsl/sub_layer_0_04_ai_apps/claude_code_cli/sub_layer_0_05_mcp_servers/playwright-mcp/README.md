---
resource_id: "abd2cd43-b31f-422d-a00d-9c87b7dc23d6"
resource_type: "readme
document"
resource_name: "README"
---
# Playwright MCP (Claude Code CLI on WSL/WSLg)

<!-- section_id: "d6e3e1d5-dcba-450b-8de0-95f8395f1335" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/`

<!-- section_id: "829a3b29-46ea-4da2-ab89-ed1ad9b0b07d" -->
## Status
✅ **WORKING** (as of 2025-12-13)

<!-- section_id: "45954313-d798-4593-848e-2db8dd0e41d0" -->
## WSL/WSLg Requirements (Headed)

Ensure WSLg runtime environment is present in the MCP server process:
- `DISPLAY=:0`
- `WAYLAND_DISPLAY=wayland-0`
- `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`

<!-- section_id: "b5c8712a-edde-4f29-a9b9-1faef5be79a9" -->
## Claude Code CLI Configuration

<!-- section_id: "4b275aa7-157b-420b-b7c3-7335e12c1095" -->
### MCP Server Setup

Claude Code CLI uses a different configuration approach than Codex. The Playwright MCP server is configured in the Claude Code settings.

**Configuration Location**: Managed by Claude Code's MCP system (not a manual config file)

**Key Configuration**:
- `isolated: true` - **REQUIRED** to allow multiple browser instances
- `launchOptions.headless: false` - For headed browser in WSLg
- `launchOptions.args`: `["--ozone-platform=wayland","--enable-features=UseOzonePlatform"]` - Wayland support
- `launchOptions.executablePath`: `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`

<!-- section_id: "90d3bea4-548c-4aba-a65c-afbcd51200a9" -->
## Known Issues

<!-- section_id: "feaa9b97-5414-4b1b-aa4f-f9f5b6e702f1" -->
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

<!-- section_id: "37129030-f8fe-40e8-a791-5c6152e91591" -->
### Issue: Cannot Access Browser Opened in Another Session

**Symptom**: Browser opened in Codex session is not accessible from Claude Code session (and vice versa).

**Cause**: Even with `isolated: true`, each MCP client maintains its own browser session context.

**Expected Behavior**: Each AI tool (Codex, Claude Code) manages its own isolated browser instance when `isolated: true` is configured.

<!-- section_id: "85ef6e55-3efe-4c1c-aed4-dd05f43d38d4" -->
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

<!-- section_id: "8b365fe3-907d-4d6b-a4ea-089a5c4ce55a" -->
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

<!-- section_id: "f11c7e3e-343b-472c-b1a6-aa99ef6cd11d" -->
## Comparison to Codex CLI

| Aspect | Codex CLI | Claude Code CLI |
|--------|-----------|-----------------|
| Config file | `~/.codex/config.toml` | Managed by Claude Code |
| Config automation | `codex_mcp_sync.py` | Manual / built-in |
| Browser isolation | `isolated: true` in JSON | `isolated: true` in config |
| WSLg env vars | Set in TOML `[env]` | Inherited from shell |
| Browser sharing | Not supported | Not supported |

<!-- section_id: "0e43522f-5604-4dbd-95dc-21cf5e33634f" -->
## Concurrent Browser Setup (NEW)

To enable **simultaneous** Playwright MCP browser use in both Codex CLI and Claude Code CLI:

```bash
# Navigate to automation scripts
cd /home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts

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

<!-- section_id: "fe0de058-4052-44ac-a8f0-84cc5735ac2c" -->
## Best Practices

1. **Use concurrent browser setup** (recommended) - enables simultaneous browser use across AI tools
2. **Use `isolated: true`** to prevent profile conflicts
3. **Verify WSLg env vars** are present in the shell before starting Claude Code
4. **Each tool has its own browser instance** - browser state is not shared between tools

<!-- section_id: "6ce68219-e201-45e3-b465-869a4025f57d" -->
## Related Documentation

- Codex Playwright MCP setup: `../../../codex_cli/0.05_mcp_servers/playwright-mcp/README.md`
- WSL/WSLg browser setup: `../../../../0.07_apps_browsers_extensions_setup/`

---

**Last Updated**: 2025-12-13
**Tested With**: Claude Code CLI on WSL2 (Ubuntu 22.04) with WSLg
**Status**: ✅ Working with `isolated: true` configuration
