---
resource_id: "caf541ea-c5b1-4b70-a2cd-080d9d3a1990"
resource_type: "document"
resource_name: "VPS_AI_CLI_SETUP_COMPLETE"
---
# VPS AI CLI Setup - Complete

**Date:** 2026-01-17
**VPS:** Hetzner CX23 (46.224.184.10)
**Status:** ✅ All CLIs configured and working

---

<!-- section_id: "13ea9bc0-cb03-4c12-aa96-7008405865b1" -->
## Installed AI CLIs

| CLI | Version | Status | Auth Method |
|-----|---------|--------|-------------|
| Gemini CLI | 0.24.0 | ✅ Working | OAuth (copied from Windows) |
| Claude Code CLI | 2.1.11 | ✅ Working | OAuth (copied from Windows) |
| Codex CLI | 0.87.0 | ✅ Working | OAuth (copied from Windows) |

---

<!-- section_id: "dfe0506f-0d4f-48fb-b9df-9a6e443bea98" -->
## Quick Reference Commands

<!-- section_id: "1156c8d7-2ed3-4f92-8340-be1aee897f75" -->
### SSH into VPS
```bash
ssh root@46.224.184.10
```

<!-- section_id: "73d1f046-f550-4a4c-9463-124853144180" -->
### Gemini CLI
```bash
# Simple prompt
gemini "your question here"

# Interactive mode
gemini
```

<!-- section_id: "7b505b91-a986-4857-9ace-838c5ef6ca7d" -->
### Claude Code CLI
```bash
# One-shot prompt
claude -p "your question here"

# Interactive mode
claude

# With specific tools disabled
claude -p "question" --allowedTools ''
```

<!-- section_id: "71bfbd8c-9f6e-404e-bb12-06ac2f0058c4" -->
### Codex CLI
```bash
# One-shot (requires skip flag outside git repos)
codex exec --skip-git-repo-check "your question"

# In a git repo directory
cd /root/sync/dawson-workspace/code/0_ai_context
codex exec "your question"

# Interactive mode
codex
```

---

<!-- section_id: "29806ddb-6f23-4f16-a9d2-1fdc99439d44" -->
## File Locations on VPS

<!-- section_id: "6bb715c2-a97c-417d-a891-2fc77077a41a" -->
### Credentials
- Gemini: `/root/.gemini/oauth_creds.json`
- Claude: `/root/.claude/.credentials.json`
- Codex: `/root/.codex/auth.json`

<!-- section_id: "458a1b33-fb32-413a-ba6d-7a8339990285" -->
### Synced Workspace
```
/root/sync/dawson-workspace/
```

<!-- section_id: "e0f8c443-8898-45cf-8785-c073983a27ab" -->
### Fix Scripts
```
/root/sync/dawson-workspace/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/0.02_operating_systems/linux_ubuntu/setup/trickle_down_0.5_setup/0_instruction_docs/setup/
├── fix_linux_login_loop.sh
├── cloud_server_ai_cli_master_setup.sh
└── cloud_server_setup_gemini.sh
```

---

<!-- section_id: "ed15f56a-6de6-4db8-8a40-8267d3441466" -->
## Configuration Details

<!-- section_id: "323aa808-5a36-4edb-b5e4-31d36e81440d" -->
### Node.js
- Version: 20.20.0
- Installed via: NodeSource apt repository
- Location: `/usr/bin/node`

<!-- section_id: "d6a1509e-34e2-4cde-a763-940a3d05df7c" -->
### Gemini CLI
- Config: `/root/.gemini/settings.json`
- Auth: OAuth personal (copied from Windows)
- Note: API key auth doesn't work from Germany (regional restriction)

<!-- section_id: "e5e2cea4-c11b-4ffa-8497-700d06c2534c" -->
### Claude Code CLI
- Config: `/root/.claude/`
- Auth: Claude.ai OAuth (Max subscription)
- Credentials expire: 2026-01-18 (auto-refreshes)

<!-- section_id: "ab876ea9-ea7a-4854-adc6-824538a25f5c" -->
### Codex CLI
- Config: `/root/.codex/`
- Auth: OpenAI OAuth (Plus subscription)
- Note: Requires `--skip-git-repo-check` flag outside git repos

---

<!-- section_id: "34aeeb43-f22f-4222-975d-7784f1935d0a" -->
## Troubleshooting

<!-- section_id: "69f9d5de-25d3-444a-8dd9-b31ebb7b74ac" -->
### Gemini "API key invalid"
The API key has regional restrictions. Use OAuth instead:
```bash
# OAuth credentials should already be configured
# If not, run: gemini (it will prompt for browser auth)
```

<!-- section_id: "24f73e6e-8a72-4fe5-aac2-5967b80cc464" -->
### Codex "Not inside a trusted directory"
```bash
# Either cd to a git repo:
cd /root/sync/dawson-workspace/code/0_ai_context

# Or use the skip flag:
codex exec --skip-git-repo-check "prompt"
```

<!-- section_id: "f2418ca2-f3a8-4dcc-b17e-3dfcedeb277f" -->
### Claude auth expired
```bash
# Re-authenticate (requires browser)
claude
# Follow the auth prompts
```

<!-- section_id: "72dfc324-52e4-4558-a81e-aa0a3ebe9c92" -->
### Credentials need refresh
Copy fresh credentials from Windows:
```bash
# From Windows, run:
scp ~/.claude/.credentials.json root@46.224.184.10:/root/.claude/
scp ~/.codex/auth.json root@46.224.184.10:/root/.codex/
scp ~/.gemini/oauth_creds.json root@46.224.184.10:/root/.gemini/
```

---

<!-- section_id: "bd3fe0b5-580c-4d02-b9ba-27695bf00050" -->
## Setup History

1. Installed Node.js 20 via NodeSource
2. Installed Gemini CLI via npm (`@google/gemini-cli`)
3. Installed Claude Code CLI via npm (`@anthropic-ai/claude-code`)
4. Installed Codex CLI via npm (`codex`)
5. Copied OAuth credentials from Windows for all 3 CLIs
6. Verified all CLIs working with test prompts
