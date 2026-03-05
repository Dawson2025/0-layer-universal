---
resource_id: "d3380c0d-ee3f-4276-aa00-36b932fd2ffe"
resource_type: "readme
knowledge"
resource_name: "README"
---
# GitHub Integration for AI CLI Tools (Shared)

This directory contains documentation that applies across multiple AI CLI tools.

## Contents

- **AI_CLI_GITHUB_INTEGRATION_GUIDE.md** - Comprehensive guide for GitHub integration with Claude Code, Codex CLI, and Gemini CLI

## Quick Summary

| Tool | Best GitHub Approach |
|------|---------------------|
| Claude Code CLI | `gh` CLI (official recommendation) |
| Codex CLI | Native git + OpenAI GitHub App |
| Gemini CLI | Standard git + `gh` CLI |

## Tool-Specific Documentation

For tool-specific details, see:
- `../claude_code_cli/0.06_.../clis/github/` - Claude Code specific docs
- `../codex_cli/0.06_.../clis/github/` - Codex CLI specific docs (if exists)
- `../gemini_cli/0.06_.../clis/github/` - Gemini CLI specific docs (if exists)

## Universal Recommendation

If you use multiple AI CLI tools, install `gh` CLI as a universal GitHub interface:

```bash
sudo apt install gh
gh auth login
gh auth setup-git
```

This works alongside any AI CLI tool for repository management, PRs, and issues.
