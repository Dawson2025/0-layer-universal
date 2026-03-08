---
resource_id: "46eab9c2-123b-4fc7-9a3b-47a6cad044d9"
resource_type: "readme_document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "7a674323-97d9-43ae-8bbf-87373a2258d3" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "75637be5-b992-4460-8b10-9b12b4de9d5a" -->
## Notes
<!-- section_id: "e37a6d81-3ce1-4a7f-99ce-7d1254499e4a" -->
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
