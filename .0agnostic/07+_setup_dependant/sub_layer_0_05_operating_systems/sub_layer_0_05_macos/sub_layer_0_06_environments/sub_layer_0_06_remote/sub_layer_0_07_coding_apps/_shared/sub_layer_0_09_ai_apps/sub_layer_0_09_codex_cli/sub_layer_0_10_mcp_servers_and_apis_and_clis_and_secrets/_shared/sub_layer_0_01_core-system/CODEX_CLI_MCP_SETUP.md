---
resource_id: "267eda5a-4c3b-4bf4-9875-5de24b822878"
resource_type: "document"
resource_name: "CODEX_CLI_MCP_SETUP"
---
# Codex CLI MCP Setup (Universal Pattern)

<!-- section_id: "66b2b2e4-b7bb-45e4-a602-b7a2cc1acebe" -->
## Goal
Use the existing universal MCP management pattern to keep Codex CLI (`~/.codex/config.toml`) in sync with environment-specific server sets (dev/test/prod) while avoiding scattered manual edits.

<!-- section_id: "9f88db61-128d-45b4-ac05-fa5cd0c11f7a" -->
## Source of Truth
- Universal MCP docs: `core-system/MCP_SYSTEM_GUIDE.md`, `MCP_CONFIGURATION_GUIDE.md`
- Environment definitions: `config/mcp/development.json`, `production.json`, `testing.json` (pattern from MCP guides)
- Codex CLI config: `~/.codex/config.toml`
- Reference pattern: Gemini CLI consolidation uses a single settings file (`~/.gemini/settings.json`) with all mcpServers; mirror that by keeping Codex MCP in one canonical `config.toml` (and using generated snippets per env if you switch).

<!-- section_id: "bbc8ccfe-bd52-492b-bc68-2f7f8444753a" -->
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

<!-- section_id: "9fba9961-9ebe-4d01-b853-6202497f8653" -->
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

<!-- section_id: "f288d93c-0393-4bef-a7c5-d7612f13dfb9" -->
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

<!-- section_id: "873b3cc8-7028-4115-b831-92f6bbf3c56d" -->
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

<!-- section_id: "3d79240d-003f-4cf6-947c-f568d59d0edc" -->
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

<!-- section_id: "51603969-d349-49ff-aaec-2c30e820f69b" -->
## Usage Checklist (manual mode)
1. Choose env: dev | test | prod.
2. Paste the matching block into `~/.codex/config.toml`, replacing existing `[mcp_servers.*]` tables.
3. Ensure `PLAYWRIGHT_BROWSERS_PATH` is set; on WSLg also set `DISPLAY`, `WAYLAND_DISPLAY`, and `XDG_RUNTIME_DIR=/mnt/wslg/runtime-dir`.
4. Restart Codex CLI session.

<!-- section_id: "cb1eadf2-f95b-4e08-a1a6-7b7699065772" -->
## Secrets (recommended)
To keep API keys out of `~/.codex/config.toml`, place them in `~/.codex/mcp.env`:
```bash
TAVILY_API_KEY=...
CONTEXT7_API_KEY=...
CONTEXT7_API_URL=https://context7.com/api/v1
```
Then rerun `codex_mcp_sync.py` to inject them into the generated blocks (or export them in your shell before starting Codex).

This keeps Codex MCP aligned with the universal system while allowing quick env switches. When the generator is added, the manual paste step goes away.
