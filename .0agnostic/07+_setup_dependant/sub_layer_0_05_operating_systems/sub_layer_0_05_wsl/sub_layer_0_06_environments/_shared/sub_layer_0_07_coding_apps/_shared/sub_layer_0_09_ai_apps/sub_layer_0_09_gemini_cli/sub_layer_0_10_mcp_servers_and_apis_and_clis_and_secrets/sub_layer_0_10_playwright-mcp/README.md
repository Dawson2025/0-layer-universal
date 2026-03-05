---
resource_id: "6b0c2ad2-da17-4914-b14f-d3c9f25d6f16"
resource_type: "readme
document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "f9f4d537-7967-4b2e-9f2a-264a46e55e6b" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "176212f1-82ec-4efc-96f8-8c68ab3ae058" -->
## Notes
<!-- section_id: "273d9030-183b-4223-8d71-9b60d20111a6" -->
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
