---
resource_id: "09a3f5ec-cd76-41dc-9e8c-5b828712ff5e"
resource_type: "readme_document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "fce0f2ec-92b9-4ef2-9cf1-108f9be062ca" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "59c4c1b2-8aad-4c4c-92bd-a6f0fc1c66df" -->
## Notes
<!-- section_id: "ab9d7006-7dbe-4ae0-a4cc-6d3bbda4e81c" -->
### Concurrent browser (recommended)
Use OS+tool-specific Playwright configs so Gemini can run a headed browser concurrently with Codex/Claude:

```bash
cd /home/dawson/dawson-workspace/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts

# Create the WSL + Gemini config (and any others you want)
python3 mcp_concurrent_browser.py setup --os wsl --tools gemini

# Verify
python3 mcp_concurrent_browser.py status --os wsl
```

Expected outputs:
- Config: `~/.gemini/playwright.wsl_gemini.json`
- Profile: `~/.cache/ms-playwright/mcp-chromium-wsl-gemini`
