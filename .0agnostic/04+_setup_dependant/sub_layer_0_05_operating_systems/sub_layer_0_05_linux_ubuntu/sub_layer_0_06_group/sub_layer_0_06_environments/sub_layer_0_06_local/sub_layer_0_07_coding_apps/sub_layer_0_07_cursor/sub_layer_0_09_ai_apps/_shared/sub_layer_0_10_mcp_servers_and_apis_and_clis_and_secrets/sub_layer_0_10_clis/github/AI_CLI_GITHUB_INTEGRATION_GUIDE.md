# GitHub Integration Guide for AI CLI Tools

## Overview

Different AI CLI tools have different recommended approaches for GitHub integration. This guide covers the best practices for each tool.

## Quick Reference

| AI CLI Tool | Recommended GitHub Approach | Notes |
|-------------|---------------------------|-------|
| **Claude Code CLI** | `gh` CLI | Official Anthropic recommendation |
| **Codex CLI** | Native git + OpenAI GitHub App | Built-in integration |
| **Gemini CLI** | Standard git + `gh` CLI | No official guidance; use general tools |

---

## Claude Code CLI

### Recommended: `gh` CLI

Per [Anthropic's official best practices](https://www.anthropic.com/engineering/claude-code-best-practices):

> "Install gh (GitHub's official CLI) for efficient GitHub interactions. Claude knows how to use the gh CLI to create issues, open pull requests, and more."

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

### Why gh CLI for Claude Code?

1. Claude is specifically trained on gh CLI usage
2. Native terminal integration
3. No additional servers required
4. Handles PRs, issues, repos, actions efficiently

### NOT Recommended: GitHub MCP Server

The GitHub MCP server is only a fallback when gh CLI is unavailable. It adds unnecessary complexity.

---

## OpenAI Codex CLI

### Recommended: Native Git + OpenAI GitHub App

Codex CLI has **its own built-in GitHub integration** and does not rely on gh CLI.

### How It Works

1. **Local Operations**: Codex works directly with your local git repo
   - Reads/edits files
   - Runs standard git commands (commit, push, etc.)
   - No external CLI dependency

2. **GitHub App Integration**: For PR reviews and CI fixes
   - Install the OpenAI GitHub App on your repos
   - Mention `@codex review` in PR comments
   - Autofix CI failures via GitHub Actions

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

### GitHub Operations with Codex

```bash
# Codex uses standard git - no special setup needed
cd your-repo
codex "review the changes and create a commit"
codex "push to origin"
```

### PR Review Integration

In GitHub PR comments:
```
@codex review this PR
@codex suggest improvements
```

### CI Autofix

Add to `.github/workflows/`:
```yaml
- uses: openai/codex-autofix@v1
  with:
    openai-api-key: ${{ secrets.OPENAI_API_KEY }}
```

---

## Google Gemini CLI

### Recommended: Standard Git + gh CLI (General Best Practice)

There is **no official Google guidance** for Gemini CLI GitHub integration as of January 2026.

### Approach

Use standard tools that work universally:

1. **Standard git** for local operations
2. **gh CLI** for GitHub-specific operations (repos, PRs, issues)
3. **Google Cloud integrations** if using GCP

### Setup

```bash
# Install Gemini CLI
# (Follow Google's installation guide)

# For GitHub operations, use gh CLI
sudo apt install gh
gh auth login
gh auth setup-git
```

### Why This Approach?

- Gemini CLI focuses on general AI assistance
- No built-in GitHub-specific features documented
- Standard tools provide full GitHub functionality
- gh CLI works regardless of AI tool

---

## Universal Tools (Work with Any AI CLI)

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

## Recommendations Summary

### For Claude Code Users
```bash
sudo apt install gh && gh auth login && gh auth setup-git
```

### For Codex CLI Users
```bash
npm install -g @openai/codex && codex auth login
# Install GitHub App for PR features
```

### For Gemini CLI Users
```bash
# Use standard tools
sudo apt install gh && gh auth login
# Gemini CLI + gh CLI + standard git
```

### For Multi-Tool Users
Install gh CLI as a universal GitHub interface that works alongside any AI CLI tool.

---

## References

- [Anthropic Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [OpenAI Codex CLI Documentation](https://developers.openai.com/codex/cli/)
- [OpenAI Codex GitHub Integration](https://developers.openai.com/codex/integrations/github/)
- [GitHub CLI Documentation](https://cli.github.com/manual/)
