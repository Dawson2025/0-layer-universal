---
resource_id: "1f3b8c91-d4fb-4f2d-9534-041185b42c39"
resource_type: "knowledge"
resource_name: "AI_CLI_GITHUB_INTEGRATION_GUIDE"
---
# GitHub Integration Guide for AI CLI Tools

<!-- section_id: "b2e3d238-e8d0-402e-8d92-3b3d81cdb7d4" -->
## Overview

Different AI CLI tools have different recommended approaches for GitHub integration. This guide covers the best practices for each tool.

<!-- section_id: "2a58af74-1119-4591-bf5d-8af96049f768" -->
## Quick Reference

| AI CLI Tool | Recommended GitHub Approach | Notes |
|-------------|---------------------------|-------|
| **Claude Code CLI** | `gh` CLI | Official Anthropic recommendation |
| **Codex CLI** | Native git + OpenAI GitHub App | Built-in integration |
| **Gemini CLI** | Standard git + `gh` CLI | No official guidance; use general tools |

---

<!-- section_id: "1d2ee68c-a4e3-45be-a455-6ac56d5cc142" -->
## Claude Code CLI

<!-- section_id: "57f55a43-4150-4b65-a921-d98117e3c5e7" -->
### Recommended: `gh` CLI

Per [Anthropic's official best practices](https://www.anthropic.com/engineering/claude-code-best-practices):

> "Install gh (GitHub's official CLI) for efficient GitHub interactions. Claude knows how to use the gh CLI to create issues, open pull requests, and more."

<!-- section_id: "261304df-0648-4055-9c7a-e799eec43287" -->
### Setup

```bash
# Install
sudo apt install gh  # Linux
brew install gh      # macOS

# Authenticate
gh auth login

# Configure git credentials
gh auth setup-git
```

<!-- section_id: "d3a8c29c-f9a6-4b76-a6eb-e6850035bbaf" -->
### Why gh CLI for Claude Code?

1. Claude is specifically trained on gh CLI usage
2. Native terminal integration
3. No additional servers required
4. Handles PRs, issues, repos, actions efficiently

<!-- section_id: "b60821c1-f8fd-4faf-bf95-7836a1f711e1" -->
### NOT Recommended: GitHub MCP Server

The GitHub MCP server is only a fallback when gh CLI is unavailable. It adds unnecessary complexity.

---

<!-- section_id: "cdcec6c3-1dc4-4e1d-a553-dc2ea01f0fad" -->
## OpenAI Codex CLI

<!-- section_id: "482ce4ed-cd1d-4b1b-9792-aeb3922ba324" -->
### Recommended: Native Git + OpenAI GitHub App

Codex CLI has **its own built-in GitHub integration** and does not rely on gh CLI.

<!-- section_id: "6995a344-d4c9-4de5-89f1-a9c7c1492d41" -->
### How It Works

1. **Local Operations**: Codex works directly with your local git repo
   - Reads/edits files
   - Runs standard git commands (commit, push, etc.)
   - No external CLI dependency

2. **GitHub App Integration**: For PR reviews and CI fixes
   - Install the OpenAI GitHub App on your repos
   - Mention `@codex review` in PR comments
   - Autofix CI failures via GitHub Actions

<!-- section_id: "d6fc0c70-5cd2-44ec-8c3a-6917125aef5f" -->
### Setup

```bash
# 1. Install Codex CLI
npm install -g @openai/codex

# 2. Authenticate with OpenAI
codex auth login
# (Uses ChatGPT account - Plus/Pro required)

# 3. Install GitHub App (for PR features)
# Go to: https://github.com/apps/openai-codex
# Install on your repos
```

<!-- section_id: "991ae200-4410-413c-a424-ac5e8707c01f" -->
### GitHub Operations with Codex

```bash
# Codex uses standard git - no special setup needed
cd your-repo
codex "review the changes and create a commit"
codex "push to origin"
```

<!-- section_id: "c821f0d8-80b2-450a-9799-e00acceea611" -->
### PR Review Integration

In GitHub PR comments:
```
@codex review this PR
@codex suggest improvements
```

<!-- section_id: "bbf68bd1-82f1-4497-894d-7bd404f6f3d2" -->
### CI Autofix

Add to `.github/workflows/`:
```yaml
- uses: openai/codex-autofix@v1
  with:
    openai-api-key: ${{ secrets.OPENAI_API_KEY }}
```

---

<!-- section_id: "a9c9351d-9af3-4801-9d08-e6f21c2316d8" -->
## Google Gemini CLI

<!-- section_id: "c23ea060-0c78-4afe-b711-8550999944c6" -->
### Recommended: Standard Git + gh CLI (General Best Practice)

There is **no official Google guidance** for Gemini CLI GitHub integration as of January 2026.

<!-- section_id: "2fe3bc59-222b-4921-8608-47e9096dc48c" -->
### Approach

Use standard tools that work universally:

1. **Standard git** for local operations
2. **gh CLI** for GitHub-specific operations (repos, PRs, issues)
3. **Google Cloud integrations** if using GCP

<!-- section_id: "44884687-7c9b-4d3d-973d-a53aea4da676" -->
### Setup

```bash
# Install Gemini CLI
# (Follow Google's installation guide)

# For GitHub operations, use gh CLI
sudo apt install gh
gh auth login
gh auth setup-git
```

<!-- section_id: "d786f57e-f306-4c1f-bae0-d990c57e7f5f" -->
### Why This Approach?

- Gemini CLI focuses on general AI assistance
- No built-in GitHub-specific features documented
- Standard tools provide full GitHub functionality
- gh CLI works regardless of AI tool

---

<!-- section_id: "efeca485-c4c1-47b4-ab5c-703427d14ad2" -->
## Universal Tools (Work with Any AI CLI)

<!-- section_id: "1cdc7f19-0dbd-4c1e-bf59-07410a2c9c4e" -->
### gh CLI

The GitHub CLI works independently of any AI tool and is useful for:

```bash
# Repository management
gh repo create username/repo --private
gh repo clone username/repo
gh repo view

# Pull requests
gh pr create --title "Feature" --body "Description"
gh pr list
gh pr merge

# Issues
gh issue create --title "Bug" --body "Details"
gh issue list

# Actions
gh run list
gh run view <id>
```

<!-- section_id: "79f1d828-2b22-4438-a99c-da51cb329b34" -->
### Standard Git

All AI CLI tools support standard git:

```bash
git clone https://github.com/user/repo.git
git add -A
git commit -m "message"
git push origin main
git pull
```

---

<!-- section_id: "e32d0209-39e6-473f-845b-bdf0ec31e75a" -->
## Comparison Matrix

| Feature | Claude Code | Codex CLI | Gemini CLI |
|---------|-------------|-----------|------------|
| **Git Operations** | Via gh CLI | Native | Standard git |
| **PR Creation** | gh pr create | Native/GitHub App | gh pr create |
| **PR Reviews** | Manual | @codex review | Manual |
| **Issue Management** | gh issue | Manual | gh issue |
| **CI Integration** | gh actions | Codex Autofix | Standard |
| **Authentication** | gh auth | OpenAI account | Standard |
| **MCP Server** | Not recommended | N/A | N/A |

---

<!-- section_id: "3e366566-438a-4c97-8da6-87d348118146" -->
## Recommendations Summary

<!-- section_id: "2df4597b-39dc-4d8a-9765-2bff334e441a" -->
### For Claude Code Users
```bash
sudo apt install gh && gh auth login && gh auth setup-git
```

<!-- section_id: "22848246-8d65-4645-8802-a936154fd55c" -->
### For Codex CLI Users
```bash
npm install -g @openai/codex && codex auth login
# Install GitHub App for PR features
```

<!-- section_id: "6b9251dd-1419-4767-bd25-9c238cc5a62c" -->
### For Gemini CLI Users
```bash
# Use standard tools
sudo apt install gh && gh auth login
# Gemini CLI + gh CLI + standard git
```

<!-- section_id: "598b0958-7a50-4c02-990a-8564e6fbff13" -->
### For Multi-Tool Users
Install gh CLI as a universal GitHub interface that works alongside any AI CLI tool.

---

<!-- section_id: "8c80fff0-10c5-499b-8cf3-87991526c17d" -->
## References

- [Anthropic Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [OpenAI Codex CLI Documentation](https://developers.openai.com/codex/cli/)
- [OpenAI Codex GitHub Integration](https://developers.openai.com/codex/integrations/github/)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
