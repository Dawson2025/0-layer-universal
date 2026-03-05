---
resource_id: "3893dc6e-54fd-4b05-bf34-e271f7661c0d"
resource_type: "readme
document"
resource_name: "README"
---
# Playwright MCP (Claude Code CLI on WSL/WSLg)

<!-- section_id: "3709a23e-d0e3-4075-ae0b-fc9babaa00fb" -->
## Canonical docs
- `../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/`

<!-- section_id: "6e713a39-d1bb-471f-a8df-ead74f6cd58d" -->
## Status
✅ **WORKING** (as of 2025-12-13)

<!-- section_id: "a097e279-c878-47bd-b7bf-120ac6f773cb" -->
## WSL/WSLg Requirements (Headed)

Ensure WSLg runtime environment is present in the MCP server process:
- `DISPLAY=:0`
- `WAYLAND_DISPLAY=wayland-0`
- `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`

<!-- section_id: "c9323b72-3221-4949-beb9-051903b13123" -->
## Claude Code CLI Configuration

<!-- section_id: "80734f81-0293-4754-90ea-a93f6dad4e95" -->
### MCP Server Setup

Claude Code CLI uses a different configuration approach than Codex. The Playwright MCP server is configured in the Claude Code settings.

**Configuration Location**: Managed by Claude Code's MCP system (not a manual config file)

**Key Configuration**:
- `isolated: true` - **REQUIRED** to allow multiple browser instances
- `launchOptions.headless: false` - For headed browser in WSLg
- `launchOptions.args`: `["--ozone-platform=wayland","--enable-features=UseOzonePlatform"]` - Wayland support
- `launchOptions.executablePath`: `~/.cache/ms-playwright/chromium-*/chrome-linux64/chrome`

<!-- section_id: "718df121-6d84-4a74-b6ed-374383cafaab" -->
## Known Issues

<!-- section_id: "1b4dad6d-5247-4de7-b159-eabf50f87391" -->
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

<!-- section_id: "ebc64fe1-3fc5-4a9c-97df-9e7cc1d9f6b0" -->
### Issue: Cannot Access Browser Opened in Another Session

**Symptom**: Browser opened in Codex session is not accessible from Claude Code session (and vice versa).

**Cause**: Even with `isolated: true`, each MCP client maintains its own browser session context.

**Expected Behavior**: Each AI tool (Codex, Claude Code) manages its own isolated browser instance when `isolated: true` is configured.

<!-- section_id: "31e96d80-806f-4680-a1c2-a31d788c13ce" -->
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

<!-- section_id: "c5c2306d-6c33-4515-b4f4-95d852da2ae2" -->
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

<!-- section_id: "800fd425-0953-40c9-afa6-d034e9100eb0" -->
## Comparison to Codex CLI

| Aspect | Codex CLI | Claude Code CLI |
|--------|-----------|-----------------|
| Config file | `~/.codex/config.toml` | Managed by Claude Code |
| Config automation | `codex_mcp_sync.py` | Manual / built-in |
| Browser isolation | `isolated: true` in JSON | `isolated: true` in config |
| WSLg env vars | Set in TOML `[env]` | Inherited from shell |
| Browser sharing | Not supported | Not supported |

<!-- section_id: "7ddd50b3-6209-4803-b20e-479e49f28461" -->
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

<!-- section_id: "0a7608be-03f0-4adc-b784-44024fbb1bff" -->
## Best Practices

1. **Use concurrent browser setup** (recommended) - enables simultaneous browser use across AI tools
2. **Use `isolated: true`** to prevent profile conflicts
3. **Verify WSLg env vars** are present in the shell before starting Claude Code
4. **Each tool has its own browser instance** - browser state is not shared between tools

<!-- section_id: "93868739-5de2-43d5-857a-2f053113fec6" -->
## Related Documentation

- Codex Playwright MCP setup: `../../../codex_cli/0.05_mcp_servers/playwright-mcp/README.md`
- WSL/WSLg browser setup: `../../../../0.07_apps_browsers_extensions_setup/`

---

**Last Updated**: 2025-12-13
**Tested With**: Claude Code CLI on WSL2 (Ubuntu 22.04) with WSLg
**Status**: ✅ Working with `isolated: true` configuration
