# playwright-mcp (cursor_agent on wsl)

## Canonical docs
- ../../../../../../0.05_mcp_servers/playwright-mcp/

## Notes
### Concurrent browser (recommended)
Use OS+tool-specific Playwright configs so Cursor Agent can run a headed browser concurrently with Codex/Claude:

```bash
cd /home/dawson/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.09_mcp_servers_and_tools_setup/0.03_automation/scripts

# Create the WSL + Cursor config (and any others you want)
python3 mcp_concurrent_browser.py setup --os wsl --tools cursor

# Verify
python3 mcp_concurrent_browser.py status --os wsl
```

Expected outputs:
- Config: `~/.config/mcp/playwright.wsl_cursor.json`
- Profile: `~/.cache/ms-playwright/mcp-chromium-wsl-cursor`
