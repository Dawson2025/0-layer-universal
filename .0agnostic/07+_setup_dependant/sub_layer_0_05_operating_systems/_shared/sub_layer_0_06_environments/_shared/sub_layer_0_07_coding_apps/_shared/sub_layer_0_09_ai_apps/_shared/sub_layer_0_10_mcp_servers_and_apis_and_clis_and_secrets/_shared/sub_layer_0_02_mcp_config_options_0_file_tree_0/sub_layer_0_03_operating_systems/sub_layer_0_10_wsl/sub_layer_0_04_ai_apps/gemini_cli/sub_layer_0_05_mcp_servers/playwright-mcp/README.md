---
resource_id: "4758b4c0-80ca-46c9-b4af-01029538c396"
resource_type: "readme
document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "13f818ee-e9a9-4a1e-a741-3270702d67ad" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "2f7ae948-c2d7-4844-b5bc-12c274c16601" -->
## Notes
<!-- section_id: "a84a82c4-5343-476d-98b9-745ba583005a" -->
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
