---
resource_id: "aaa1eaf3-aa3c-4d5c-850a-24dcf60e10e7"
resource_type: "readme
document"
resource_name: "README"
---
# GitHub CLI Documentation

This directory contains documentation for using the GitHub CLI (`gh`) with Claude Code.

## Contents

- **GH_CLI_SETUP.md** - Installation and authentication guide for the gh CLI
- **GITHUB_SUBMODULES_GUIDE.md** - Creating repos and managing git submodules
- **GITHUB_MCP_VS_CLI.md** - Why gh CLI is recommended over GitHub MCP server

## Quick Start

```bash
# Install gh CLI (Ubuntu/Debian)
sudo apt install gh

# Authenticate
gh auth login

# Set up git credentials
gh auth setup-git

# Verify
gh auth status
```

## Key Takeaway

**Use `gh` CLI for all GitHub operations in Claude Code.** It's the officially recommended approach per Anthropic's best practices.
