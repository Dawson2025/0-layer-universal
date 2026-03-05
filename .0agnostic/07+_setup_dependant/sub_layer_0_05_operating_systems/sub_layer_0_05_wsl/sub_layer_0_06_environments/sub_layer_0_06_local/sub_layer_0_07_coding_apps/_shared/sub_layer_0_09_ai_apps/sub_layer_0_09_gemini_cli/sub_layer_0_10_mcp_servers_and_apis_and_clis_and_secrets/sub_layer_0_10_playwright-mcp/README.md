---
resource_id: "f169b1f3-4e66-4916-b85d-a2309bbdb0d2"
resource_type: "readme
document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "e0623bea-91fe-458b-a858-749dcac5b729" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "1c8ced03-d2c3-45a1-9465-d4345bf960c8" -->
## Notes
<!-- section_id: "133e5dd4-d812-41df-a73d-215896362f85" -->
### Concurrent browser (recommended)
Use OS+tool-specific Playwright configs so Gemini can run a headed browser concurrently with Codex/Claude:

```bash
cd /home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts

# Create the WSL + Gemini config (and any others you want)
python3 mcp_concurrent_browser.py setup --os wsl --tools gemini

# Verify
python3 mcp_concurrent_browser.py status --os wsl
```

Expected outputs:
- Config: `~/.gemini/playwright.wsl_gemini.json`
- Profile: `~/.cache/ms-playwright/mcp-chromium-wsl-gemini`
