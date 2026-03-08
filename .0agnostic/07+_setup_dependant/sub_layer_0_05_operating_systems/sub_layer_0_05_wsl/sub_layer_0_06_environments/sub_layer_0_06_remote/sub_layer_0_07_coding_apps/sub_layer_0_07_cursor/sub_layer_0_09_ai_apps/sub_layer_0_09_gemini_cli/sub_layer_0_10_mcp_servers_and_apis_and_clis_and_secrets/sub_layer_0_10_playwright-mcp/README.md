---
resource_id: "f6f23ba5-4592-45bc-82eb-d582ef589da6"
resource_type: "readme_document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "514cbb1d-74c7-4a28-97d5-9721bb9026a3" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "ed8a61a6-0ef7-457b-9944-988683e82d5f" -->
## Notes
<!-- section_id: "19c04be4-788b-432c-ae66-9c293558539c" -->
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
