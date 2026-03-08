---
resource_id: "79e2d18e-1341-45fe-a3ec-672f74840fe2"
resource_type: "readme_document"
resource_name: "README"
---
# playwright-mcp (gemini_cli on wsl)

<!-- section_id: "28a29f7d-0c60-4b19-bfa9-6df50e597cc5" -->
## Canonical docs
- ../../../../../_shared/0.04_ai_apps/_shared/0.05_mcp_servers/playwright-mcp/

<!-- section_id: "ac9fef64-b57b-4b3e-9734-c5d8c1483162" -->
## Notes
<!-- section_id: "69b2c3b8-9730-44d6-8fe7-f0513636aaee" -->
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
