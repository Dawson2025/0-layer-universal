# playwright-mcp (gemini_cli on wsl)

## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

## Notes
### Concurrent browser (recommended)
Use OS+tool-specific Playwright configs so Gemini can run a headed browser concurrently with Codex/Claude:

```bash
cd /home/dawson/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0.10_mcp_servers_and_tools_setup/0.06_automation/scripts

# Create the WSL + Gemini config (and any others you want)
python3 mcp_concurrent_browser.py setup --os wsl --tools gemini

# Verify
python3 mcp_concurrent_browser.py status --os wsl
```

Expected outputs:
- Config: `~/.gemini/playwright.wsl_gemini.json`
- Profile: `~/.cache/ms-playwright/mcp-chromium-wsl-gemini`
