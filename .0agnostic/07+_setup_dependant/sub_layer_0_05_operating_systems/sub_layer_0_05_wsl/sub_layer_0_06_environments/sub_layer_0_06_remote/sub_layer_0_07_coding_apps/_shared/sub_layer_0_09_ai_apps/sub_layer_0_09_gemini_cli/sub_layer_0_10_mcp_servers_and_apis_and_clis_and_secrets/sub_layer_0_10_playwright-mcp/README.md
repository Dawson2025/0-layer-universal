---
resource_id: "7c9a2b30-4c54-425c-ba62-213af4af4722"
resource_type: "readme
document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "0951b7ce-4cb5-4625-9340-5ae4bce89eb7" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "31364199-c75d-47ee-8d9c-d99ebfb7a34b" -->
## Notes
<!-- section_id: "a7b678ed-c328-4306-a7c4-a040400d701e" -->
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
