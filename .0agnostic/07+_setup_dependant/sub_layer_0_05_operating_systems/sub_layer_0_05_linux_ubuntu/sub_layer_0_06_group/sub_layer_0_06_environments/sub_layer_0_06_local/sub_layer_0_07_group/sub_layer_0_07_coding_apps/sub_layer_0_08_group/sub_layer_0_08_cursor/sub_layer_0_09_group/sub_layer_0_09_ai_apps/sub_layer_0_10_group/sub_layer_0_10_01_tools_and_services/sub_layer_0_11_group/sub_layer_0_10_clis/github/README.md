---
resource_id: "aaa1eaf3-aa3c-4d5c-850a-24dcf60e10e7"
resource_type: "readme_document"
resource_name: "README"
---
# GitHub CLI Documentation

This directory contains documentation for using the GitHub CLI (`gh`) with Claude Code.

<!-- section_id: "da21f6e6-dad0-4549-97e2-0f9ba351733f" -->
## Contents

- **GH_CLI_SETUP.md** - Installation and authentication guide for the gh CLI
- **GITHUB_SUBMODULES_GUIDE.md** - Creating repos and managing git submodules
- **GITHUB_MCP_VS_CLI.md** - Why gh CLI is recommended over GitHub MCP server

<!-- section_id: "0aea5254-5234-4916-96ab-3a3e51dad15a" -->
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

<!-- section_id: "9b46660b-b445-46ee-9dc2-e82544cc5370" -->
## Key Takeaway

**Use `gh` CLI for all GitHub operations in Claude Code.** It's the officially recommended approach per Anthropic's best practices.
