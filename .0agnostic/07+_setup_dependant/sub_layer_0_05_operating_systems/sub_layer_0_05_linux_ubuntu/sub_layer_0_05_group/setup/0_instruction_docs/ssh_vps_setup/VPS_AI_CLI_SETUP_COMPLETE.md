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

## Installed AI CLIs

| CLI | Version | Status | Auth Method |
|-----|---------|--------|-------------|
| Gemini CLI | 0.24.0 | ✅ Working | OAuth (copied from Windows) |
| Claude Code CLI | 2.1.11 | ✅ Working | OAuth (copied from Windows) |
| Codex CLI | 0.87.0 | ✅ Working | OAuth (copied from Windows) |

---

## Quick Reference Commands

### SSH into VPS
```bash
ssh root@46.224.184.10
```

### Gemini CLI
```bash
# Simple prompt
gemini "your question here"

# Interactive mode
gemini
```

### Claude Code CLI
```bash
# One-shot prompt
claude -p "your question here"

# Interactive mode
claude

# With specific tools disabled
claude -p "question" --allowedTools ''
```

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

## File Locations on VPS

### Credentials
- Gemini: `/root/.gemini/oauth_creds.json`
- Claude: `/root/.claude/.credentials.json`
- Codex: `/root/.codex/auth.json`

### Synced Workspace
```
/root/sync/dawson-workspace/
```

### Fix Scripts
```
/root/sync/dawson-workspace/code/0_ai_context/0_context/layer_0_universal/0.02_sub_layers/sub_layer_0_05-0.014_setup/0.01_universal_setup_file_tree_0/0.02_operating_systems/linux_ubuntu/setup/trickle_down_0.5_setup/0_instruction_docs/setup/
├── fix_linux_login_loop.sh
├── cloud_server_ai_cli_master_setup.sh
└── cloud_server_setup_gemini.sh
```

---

## Configuration Details

### Node.js
- Version: 20.20.0
- Installed via: NodeSource apt repository
- Location: `/usr/bin/node`

### Gemini CLI
- Config: `/root/.gemini/settings.json`
- Auth: OAuth personal (copied from Windows)
- Note: API key auth doesn't work from Germany (regional restriction)

### Claude Code CLI
- Config: `/root/.claude/`
- Auth: Claude.ai OAuth (Max subscription)
- Credentials expire: 2026-01-18 (auto-refreshes)

### Codex CLI
- Config: `/root/.codex/`
- Auth: OpenAI OAuth (Plus subscription)
- Note: Requires `--skip-git-repo-check` flag outside git repos

---

## Troubleshooting

### Gemini "API key invalid"
The API key has regional restrictions. Use OAuth instead:
```bash
# OAuth credentials should already be configured
# If not, run: gemini (it will prompt for browser auth)
```

### Codex "Not inside a trusted directory"
```bash
# Either cd to a git repo:
cd /root/sync/dawson-workspace/code/0_ai_context

# Or use the skip flag:
codex exec --skip-git-repo-check "prompt"
```

### Claude auth expired
```bash
# Re-authenticate (requires browser)
claude
# Follow the auth prompts
```

### Credentials need refresh
Copy fresh credentials from Windows:
```bash
# From Windows, run:
scp ~/.claude/.credentials.json root@46.224.184.10:/root/.claude/
scp ~/.codex/auth.json root@46.224.184.10:/root/.codex/
scp ~/.gemini/oauth_creds.json root@46.224.184.10:/root/.gemini/
```

---

## Setup History

1. Installed Node.js 20 via NodeSource
2. Installed Gemini CLI via npm (`@google/gemini-cli`)
3. Installed Claude Code CLI via npm (`@anthropic-ai/claude-code`)
4. Installed Codex CLI via npm (`codex`)
5. Copied OAuth credentials from Windows for all 3 CLIs
6. Verified all CLIs working with test prompts
