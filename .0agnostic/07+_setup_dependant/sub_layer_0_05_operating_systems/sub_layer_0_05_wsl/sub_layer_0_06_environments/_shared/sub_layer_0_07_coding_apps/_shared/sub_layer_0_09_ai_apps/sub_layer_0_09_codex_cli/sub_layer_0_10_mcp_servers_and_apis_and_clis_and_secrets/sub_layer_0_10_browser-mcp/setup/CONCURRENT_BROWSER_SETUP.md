---
resource_id: "5e4939c7-412a-4e23-9273-3579fa439fbf"
resource_type: "document"
resource_name: "CONCURRENT_BROWSER_SETUP"
---
# Concurrent Browser Setup for Multiple AI Tools

<!-- section_id: "a54aab3a-994a-4cdb-a0a0-c503e3c0bbc0" -->
## Problem Statement

When multiple AI CLI tools (Codex CLI, Claude Code CLI, Gemini CLI, etc.) attempt to use Playwright MCP on the same machine, they encounter a "Browser is already in use" error. This happens because:

1. **MCP server process locking**: Only one client can connect to a given MCP server instance at a time
2. **Browser profile conflicts**: Even with `isolated: true`, different AI tools were attempting to use the same browser profile directory
3. **Shared configuration**: Tools were referencing the same Playwright MCP config file

<!-- section_id: "fc2835b2-20f1-43ca-9c21-e2abffc17964" -->
## Solution Architecture

The `mcp_concurrent_browser.py` script solves this by creating **OS-specific and tool-specific isolated browser configurations** using the naming pattern `{os}_{tool}` (e.g., `wsl_codex`, `wsl_claude`, `linux_gemini`, `windows_cursor`):

```
Configuration        Config File                           Profile Directory
-------------        ---------------------------------     ---------------------------------------------
wsl_codex            ~/.codex/playwright.wsl_codex.json    ~/.cache/ms-playwright/mcp-chromium-wsl-codex
wsl_claude           ~/.config/mcp/playwright.wsl_claude.json ~/.cache/ms-playwright/mcp-chromium-wsl-claude
linux_gemini         ~/.gemini/playwright.linux_gemini.json ~/.cache/ms-playwright/mcp-chromium-linux-gemini
macos_cursor         ~/.config/mcp/playwright.macos_cursor.json ~/.cache/ms-playwright/mcp-chromium-macos-cursor
```

<!-- section_id: "c107a433-8f46-41fb-97fc-88f2a14ed7ec" -->
### Key Design Principles

1. **OS-aware configuration**: Auto-detects operating system (WSL, Linux, macOS, Windows)
2. **Separate config files per OS+tool combination**: Each combination gets its own Playwright MCP JSON config
3. **Isolated browser profiles**: Each config uses a unique browser data directory
4. **OS-specific optimizations**: Automatically adds OS-specific launch args (e.g., Wayland/Ozone for WSLg)
5. **Concurrent execution**: All tools can now run headed browsers simultaneously on any OS

<!-- section_id: "957d7b11-6df7-4479-ab0f-0eef5705a680" -->
## Installation and Setup

<!-- section_id: "31b91b5b-c35e-4960-a195-b7b0f428996e" -->
### Prerequisites

- Python 3.7+
- Playwright browsers installed (`npx playwright install chromium`)
- Multiple AI CLI tools installed (Codex, Claude Code, etc.)

<!-- section_id: "d5b90e9f-877b-4c77-ac05-f69904ffa079" -->
### Quick Start

```bash
# Navigate to the automation scripts directory
cd /home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/scripts

# 1. Set up OS-specific concurrent browser configs (auto-detects OS)
python3 mcp_concurrent_browser.py setup

# 2. Update Codex CLI to use OS+tool-specific config
python3 mcp_concurrent_browser.py apply-codex

# 3. Restart all AI CLI tools
# (Close and reopen Codex, Claude Code, etc.)

# 4. Verify setup
python3 mcp_concurrent_browser.py status --os wsl
```

**Note**: The script auto-detects your OS (WSL, Linux, macOS, Windows) and creates configurations accordingly.

<!-- section_id: "b1952386-2b54-4327-b784-3cc8daace793" -->
### Step-by-Step Setup

#### Step 1: Set Up Concurrent Configs

This creates OS-specific and tool-specific isolated Playwright MCP configurations:

```bash
# Auto-detect OS and set up all tools
python3 mcp_concurrent_browser.py setup

# Or explicitly specify OS
python3 mcp_concurrent_browser.py setup --os wsl
```

**What this does:**
- Auto-detects current OS (WSL, Linux, macOS, Windows)
- Creates `playwright.{os}_{tool}.json` in each tool's config directory
- Sets `isolated: true` in all configs
- Adds OS-specific launch args (e.g., Wayland/Ozone for WSLg)
- Creates separate profile directories for each OS+tool combination
- Detects the newest Chromium executable automatically
- Adds metadata to config files for tracking

**Options:**

```bash
# Set up for specific tools only
python3 mcp_concurrent_browser.py setup --tools codex claude

# Set up for specific OS (useful for pre-configuring other machines)
python3 mcp_concurrent_browser.py setup --os linux --tools gemini

# Set up in headless mode
python3 mcp_concurrent_browser.py setup --headless
```

#### Step 2: Update Codex CLI Config

The Codex CLI uses `config.toml` to manage MCP servers. Update it to use the OS+tool-specific config:

```bash
# Auto-detect OS and update config
python3 mcp_concurrent_browser.py apply-codex

# Or explicitly specify OS
python3 mcp_concurrent_browser.py apply-codex --os wsl
```

**What this does:**
- Reads `~/.codex/config.toml`
- Finds the `[mcp_servers.playwright]` section
- Updates the `args` line to reference `playwright.{os}_codex.json` (e.g., `playwright.wsl_codex.json`)
- Creates a backup at `~/.codex/config.toml.bak`

**Manual alternative:**

Edit `~/.codex/config.toml` and change:

```toml
[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest", "--config", "/home/dawson/.codex/playwright.development.json"]
```

To (for WSL):

```toml
[mcp_servers.playwright]
command = "npx"
args = ["-y", "@playwright/mcp@latest", "--config", "/home/dawson/.codex/playwright.wsl_codex.json"]
```

#### Step 3: Configure Claude Code CLI

Claude Code CLI manages MCP servers internally (not via a manual config file like Codex). To use the tool-specific Playwright config:

**Current limitation**: Claude Code CLI's MCP configuration is managed internally and doesn't currently support specifying a custom `--config` path for Playwright MCP.

**Workaround options:**

1. **Use Playwright MCP only from Codex CLI** (recommended for now)
2. **Close Codex before using Claude Code CLI's Playwright MCP**
3. **Wait for Claude Code CLI to support custom MCP config paths** (check documentation updates)

#### Step 4: Restart AI Tools

After configuration changes:

```bash
# Close all AI CLI sessions
# Reopen them to load new MCP configurations
```

#### Step 5: Verify Setup

```bash
# Show status for current OS only
python3 mcp_concurrent_browser.py status --os wsl

# Or show status for all OSes
python3 mcp_concurrent_browser.py status
```

**Example output (WSL):**

```
📊 Concurrent Browser Configuration Status
======================================================================

Environment:
   Detected OS: WSL
   WSLg detected: ✅ Yes
   Chromium executable: /home/dawson/.cache/ms-playwright/chromium-1202/chrome-linux64/chrome

Configuration for WSL:

  ✅ Codex CLI (wsl_codex)
     Config: /home/dawson/.codex/playwright.wsl_codex.json
             ✅ Exists
             isolated=True, headless=False
             OS: wsl, Tool: codex
     Profile: /home/dawson/.cache/ms-playwright/mcp-chromium-wsl-codex
              ✅ Exists

  ✅ Claude Code CLI (wsl_claude)
     Config: /home/dawson/.config/mcp/playwright.wsl_claude.json
             ✅ Exists
             isolated=True, headless=False
             OS: wsl, Tool: claude
     Profile: /home/dawson/.cache/ms-playwright/mcp-chromium-wsl-claude
              ✅ Exists
```

<!-- section_id: "f46facba-df0a-402c-8cd0-12b0c0a7a760" -->
## Testing Concurrent Browser Use

<!-- section_id: "20fdadfa-a307-439a-a8da-d2b7860739ea" -->
### Test 1: Open Browser in Codex CLI

```bash
# Start Codex CLI
codex

# In Codex session, ask Claude:
"Open a browser and navigate to https://example.com"
```

Expected: Browser opens in WSLg window (if headed mode), Playwright MCP tools work.

<!-- section_id: "5b6401eb-546e-425b-bbe2-132ece33cf33" -->
### Test 2: Open Browser in Claude Code CLI (While Codex is Running)

```bash
# In a separate terminal, start Claude Code CLI
claude

# In Claude Code session, ask:
"Navigate to https://example.com using the browser"
```

**Expected (after full setup):** Claude Code opens its own browser instance without conflicts.

**Current status:** May still encounter conflicts due to Claude Code CLI's internal MCP management. See workarounds above.

<!-- section_id: "918632b4-38bc-4f7e-bf49-f90f1c3bbad3" -->
## Configuration Files Reference

<!-- section_id: "74d837d9-c914-4a50-aae2-0739fae403e9" -->
### Playwright MCP Config Structure

Each `playwright.{os}_{tool}.json` file has this structure:

```json
{
  "browser": {
    "browserName": "chromium",
    "isolated": true,
    "launchOptions": {
      "headless": false,
      "executablePath": "/home/dawson/.cache/ms-playwright/chromium-1202/chrome-linux64/chrome",
      "args": [
        "--ozone-platform=wayland",
        "--enable-features=UseOzonePlatform"
      ]
    }
  },
  "_metadata": {
    "os": "wsl",
    "tool": "codex",
    "config_name": "wsl_codex"
  }
}
```

**Key fields:**
- `isolated: true` - **Critical**: Enables concurrent instances
- `headless: false` - Headed browser (set to `true` for headless)
- `executablePath` - Explicit Chromium binary path (improves reliability)
- `args` - OS-specific launch args (e.g., Wayland/Ozone for WSLg, only added when appropriate)
- `_metadata` - Tracking information (OS, tool, config name)

<!-- section_id: "acd2ec11-9a58-4af4-be7e-499b6bb0c6b2" -->
## Troubleshooting

<!-- section_id: "c9fe15f9-0b0f-4b13-952d-8a44123ae910" -->
### Error: "Browser is already in use"

**Cause:** Another AI tool has an active MCP server connection.

**Solutions:**

1. **Verify each tool uses its own config:**
   ```bash
   python3 mcp_concurrent_browser.py status
   ```

2. **Check for leftover processes:**
   ```bash
   ps aux | grep playwright
   ps aux | grep chromium
   ```

3. **Close active browser sessions in other tools**

4. **Restart all AI CLI tools** after config changes

<!-- section_id: "de35df3b-e64e-4e55-ad4c-d40e44fa23ae" -->
### Config File Not Found

**Cause:** Setup script hasn't been run or config was deleted.

**Solution:**
```bash
python3 mcp_concurrent_browser.py setup
```

<!-- section_id: "f838e779-dd8b-4468-9a2f-686463a1efa0" -->
### Chromium Executable Not Found

**Cause:** Playwright browsers not installed.

**Solution:**
```bash
npx playwright install chromium
```

<!-- section_id: "f2d9f67c-f5eb-491b-a87f-e105f15be666" -->
### WSLg Browser Crashes Immediately

**Cause:** Chromium not using Wayland/Ozone on WSLg.

**Solution:** The setup script automatically detects WSLg and adds the required flags. Verify:

```bash
python3 mcp_concurrent_browser.py status
```

Config should show:
```json
"args": [
  "--ozone-platform=wayland",
  "--enable-features=UseOzonePlatform"
]
```

<!-- section_id: "f4f0ecb7-20d2-45f2-a08f-31a22a91a758" -->
### Claude Code CLI Still Conflicts

**Cause:** Claude Code CLI doesn't currently support custom Playwright MCP config paths.

**Workarounds:**

1. **Use Playwright MCP only from Codex CLI** (recommended)
2. **Close Codex before using Claude Code**
3. **Use headless mode in one tool:**
   ```bash
   python3 mcp_concurrent_browser.py setup --tools claude --headless
   ```

<!-- section_id: "90885d81-f402-4674-915b-383cfcd547bb" -->
## Advanced Usage

<!-- section_id: "941d54a0-3aef-4209-afe5-b63e4567c692" -->
### Switching Between Headed and Headless

To reconfigure all tools for headless mode:

```bash
python3 mcp_concurrent_browser.py setup --headless
python3 mcp_concurrent_browser.py apply-codex
```

To switch back to headed:

```bash
python3 mcp_concurrent_browser.py setup
python3 mcp_concurrent_browser.py apply-codex
```

<!-- section_id: "a136a48f-d0f2-47c3-8b25-5266bd9dbb43" -->
### Adding a New AI Tool

Edit `mcp_concurrent_browser.py` and add to the `AI_TOOLS` dict:

```python
AI_TOOLS = {
    # ... existing tools ...
    "newtool": {
        "name": "New AI Tool",
        "config_dir": HOME / ".newtool",
        "profile_dir": HOME / ".cache/ms-playwright/mcp-chromium-newtool",
        "config_file": "playwright.newtool.json",
    },
}
```

Then run:

```bash
python3 mcp_concurrent_browser.py setup --tools newtool
```

<!-- section_id: "fe3ae88e-87ae-4520-a35a-fe88e4b7f049" -->
## Architecture Notes

<!-- section_id: "255eb3e4-6d4f-4e55-baf0-566f5cd87bdd" -->
### Why This Approach Works

1. **Separate MCP server instances**: Each AI tool spawns its own `npx @playwright/mcp@latest` process
2. **Unique config files**: Each process reads a different JSON config via `--config` flag
3. **Isolated profiles**: `isolated: true` + unique profile dirs = no browser lock conflicts
4. **Process isolation**: OS handles process separation, no manual orchestration needed

<!-- section_id: "b4658f3a-2a72-4381-8844-c50936e04801" -->
### What Doesn't Work

1. **Sharing browser state between tools**: Each tool has its own browser instance (by design)
2. **Accessing a browser opened in Tool A from Tool B**: Browser sessions are tool-specific
3. **Real-time config switching**: Requires restarting the AI tool to reload MCP config

<!-- section_id: "97376761-2a8e-4333-8f4c-1ad4a9eca304" -->
### Future Improvements

1. **Claude Code CLI integration**: Wait for support for custom MCP config paths
2. **Automatic config updates**: Script to update all tools' configs when Playwright MCP updates
3. **Session sharing**: Potential feature to share browser state via remote debugging protocol
4. **Config validation**: Pre-flight checks to ensure configs are valid before restarting tools

<!-- section_id: "707de58c-9729-49dc-9dab-80af3ee98f6f" -->
## Related Documentation

- Codex Playwright MCP: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/wsl/0.04_ai_apps/codex_cli/0.05_mcp_servers/playwright-mcp/README.md`
- Claude Code Playwright MCP: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.02_mcp_config_options_0_file_tree_0/0.03_operating_systems/wsl/0.04_ai_apps/claude_code_cli/0.05_mcp_servers/playwright-mcp/README.md`
- MCP Server Automation: `/home/dawson/code/0_layer_universal/0_context/layer_0/0.02_sub_layers/sub_layer_0_10_mcp_servers_and_tools_setup/0.06_automation/README.md`

---

**Last Updated**: 2025-12-13
**Tested With**: Codex CLI on WSL2 (Ubuntu 22.04) with WSLg
**Status**: ✅ Working for Codex CLI; ⚠️ Partial support for Claude Code CLI (manual config needed)
