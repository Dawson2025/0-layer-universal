---
resource_id: "aaad0a60-1369-4649-9b98-a889f24eb1f7"
resource_type: "readme_document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "b710548e-38b5-4801-b5a5-b53a0a80a5db" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "9a9ccce6-fb0c-487d-a65b-f4a83a3517f2" -->
## Notes
<!-- section_id: "624111e4-0471-41be-a11f-b31d609d0985" -->
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
