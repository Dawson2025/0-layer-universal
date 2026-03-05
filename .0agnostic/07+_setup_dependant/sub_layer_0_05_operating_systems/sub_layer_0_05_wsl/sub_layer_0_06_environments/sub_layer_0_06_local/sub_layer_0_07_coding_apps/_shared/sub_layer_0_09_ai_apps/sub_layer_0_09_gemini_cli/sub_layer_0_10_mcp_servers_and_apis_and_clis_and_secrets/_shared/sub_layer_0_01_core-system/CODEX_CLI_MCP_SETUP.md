---
resource_id: "85e00fcd-1f34-4142-bacb-a2c66d80e2ad"
resource_type: "document"
resource_name: "CODEX_CLI_MCP_SETUP"
---
# Codex CLI MCP Setup (Universal Pattern)

<!-- section_id: "06027821-5779-4cc4-ae26-503179d4bcbc" -->
## Goal
Use the existing universal MCP management pattern to keep Codex CLI (`~/.codex/config.toml`) in sync with environment-specific server sets (dev/test/prod) while avoiding scattered manual edits.

<!-- section_id: "5977d777-a73e-4921-a98c-754a962b8e8a" -->
## Source of Truth
- Universal MCP docs: `core-system/MCP_SYSTEM_GUIDE.md`, `MCP_CONFIGURATION_GUIDE.md`
- Environment definitions: `config/mcp/development.json`, `production.json`, `testing.json` (pattern from MCP guides)
- Codex CLI config: `~/.codex/config.toml`
- Reference pattern: Gemini CLI consolidation uses a single settings file (`~/.gemini/settings.json`) with all mcpServers; mirror that by keeping Codex MCP in one canonical `config.toml` (and using generated snippets per env if you switch).

<!-- section_id: "11c673d1-89ad-4e86-8b64-702310be4ba7" -->
## Recommended Approach
1) **Define servers per environment** (mirroring the universal pattern):
   - **dev**: chrome-devtools, playwright, browser (optional), web-search, context7, filesystem
   - **test**: playwright, browser (optional), filesystem
   - **prod**: web-search, context7, filesystem (and any prod-only like slack/postgres if needed)

2) **Generate Codex config blocks** instead of hand-editing:
   - Keep a small generator (bash/python) that reads `config/mcp/<env>.json` and emits the `[mcp_servers.*]` blocks for Codex.
   - Store the generated snippet under `~/.codex/environments/<env>.toml`.
   - Update `~/.codex/config.toml` by replacing the existing `[mcp_servers.*]` table with the generated snippet for the chosen env.

3) **Environment switch procedure (manual if generator isn’t built yet)**:
   - Open `~/.codex/config.toml`
   - Replace `[mcp_servers.*]` entries with the block for your target env
   - Keep API keys out of the file when possible; prefer env vars exported in your shell or an `.env` loaded by your MCP servers

<!-- section_id: "fccacc0f-5cc0-4cae-9e7f-48ee2f66c53b" -->
## Example Codex MCP blocks (Dev)
Add under `~/.codex/config.toml` (replace existing `[mcp_servers.*]`):
```toml
[mcp_servers.chrome-devtools]
command = "npx"
args = ["-y", "chrome-devtools-mcp@latest"]

[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest", "--config", "/home/dawson/.codex/playwright.development.json"]
[mcp_servers.playwright.env]
PLAYWRIGHT_BROWSERS_PATH = "/home/dawson/.cache/ms-playwright"
HOME = "/home/dawson"
DISPLAY = ":0"
WAYLAND_DISPLAY = "wayland-0"
XDG_RUNTIME_DIR = "/mnt/wslg/runtime-dir"

[mcp_servers.browser]
command = "npx"
args = ["@agent-infra/mcp-server-browser"]
[mcp_servers.browser.env]
PLAYWRIGHT_BROWSERS_PATH = "/home/dawson/.cache/ms-playwright"
HOME = "/home/dawson"

[mcp_servers.web-search]
command = "npx"
args = ["tavily-mcp"]
# TAVILY_API_KEY should be set in your shell or .env

[mcp_servers.context7]
command = "npx"
args = ["@upstash/context7-mcp"]
# CONTEXT7_API_KEY / CONTEXT7_API_URL should be set in your shell or .env

[mcp_servers.filesystem]
command = "npx"
args = ["mcp-filesystem-server"]  # swap to your preferred fs server
```

<!-- section_id: "a0a3c033-2eeb-48d1-b26e-9bfb0717b206" -->
## Example Codex MCP blocks (Test)
```toml
[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest", "--config", "/home/dawson/.codex/playwright.testing.json"]
[mcp_servers.playwright.env]
PLAYWRIGHT_BROWSERS_PATH = "/home/dawson/.cache/ms-playwright"
HOME = "/home/dawson"
DISPLAY = ":0"
WAYLAND_DISPLAY = "wayland-0"
XDG_RUNTIME_DIR = "/mnt/wslg/runtime-dir"

[mcp_servers.browser]
command = "npx"
args = ["@agent-infra/mcp-server-browser"]
[mcp_servers.browser.env]
PLAYWRIGHT_BROWSERS_PATH = "/home/dawson/.cache/ms-playwright"
HOME = "/home/dawson"

[mcp_servers.filesystem]
command = "npx"
args = ["mcp-filesystem-server"]
```

<!-- section_id: "4129b91f-158a-4387-b31a-b7bea98824b7" -->
## Example Codex MCP blocks (Prod-lite)
```toml
[mcp_servers.web-search]
command = "npx"
args = ["tavily-mcp"]

[mcp_servers.context7]
command = "npx"
args = ["@upstash/context7-mcp"]

[mcp_servers.filesystem]
command = "npx"
args = ["mcp-filesystem-server"]
```

<!-- section_id: "d4f9f013-929f-4b12-9951-d2ff824071cb" -->
## Next Steps (automation)
- Use the generator `automation/scripts/codex_mcp_sync.py`:
  ```bash
  # From repo root:
  python3 0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts/codex_mcp_sync.py --env development
  # Optional: disable specific servers
  python3 .../codex_mcp_sync.py --env development --disable chrome-devtools web-search
  # Optional: run Playwright headless (more reliable on systems without GUI)
  python3 .../codex_mcp_sync.py --env development --headless
  ```
  - Writes active snippet to `~/.codex/environments/<env>.toml`
  - Writes full baseline to `~/.codex/environments/<env>.full.toml`
  - Writes disabled servers (if any) to `~/.codex/environments/<env>.disabled.toml`
  - Backs up `~/.codex/config.toml` to `config.toml.bak`
  - Rewrites `[mcp_servers.*]` in `~/.codex/config.toml`
- Optional: add a make target `make codex-mcp ENV=development|testing|production-lite`.

<!-- section_id: "6af5511a-5ecc-47b0-9f8d-dc0f258f887e" -->
## Usage Checklist (manual mode)
1. Choose env: dev | test | prod.
2. Paste the matching block into `~/.codex/config.toml`, replacing existing `[mcp_servers.*]` tables.
3. Ensure `PLAYWRIGHT_BROWSERS_PATH` is set; on WSLg also set `DISPLAY`, `WAYLAND_DISPLAY`, and `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`.
4. Restart Codex CLI session.

<!-- section_id: "9784b336-04a2-46f4-8d36-ca2f6763af9a" -->
## Secrets (recommended)
To keep API keys out of `~/.codex/config.toml`, place them in `~/.codex/mcp.env`:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```
Then rerun `codex_mcp_sync.py` to inject them into the generated blocks (or export them in your shell before starting Codex).

This keeps Codex MCP aligned with the universal system while allowing quick env switches. When the generator is added, the manual paste step goes away.
