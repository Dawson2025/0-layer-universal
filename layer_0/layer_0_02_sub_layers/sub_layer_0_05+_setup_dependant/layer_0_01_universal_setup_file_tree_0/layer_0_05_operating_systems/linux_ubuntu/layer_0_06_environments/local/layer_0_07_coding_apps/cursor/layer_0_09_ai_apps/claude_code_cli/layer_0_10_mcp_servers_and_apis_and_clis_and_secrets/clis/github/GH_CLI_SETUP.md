# GitHub CLI (gh) Setup for Claude Code

## Overview

The `gh` CLI is the **recommended way** to interact with GitHub when using Claude Code. According to Anthropic's official best practices, Claude Code is trained to use `gh` directly rather than the GitHub MCP server.

## Installation

### Linux (Ubuntu/Debian)

```bash
# Add GitHub CLI repository
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Install
sudo apt update
sudo apt install gh -y
```

### macOS

```bash
brew install gh
```

### Windows

```powershell
winget install --id GitHub.cli
```

## Authentication

### Web-based Authentication (Recommended)

```bash
gh auth login
```

This opens a browser for OAuth authentication. Follow the prompts to:
1. Copy the one-time code displayed
2. Open the URL in your browser
3. Enter the code
4. Authorize the GitHub CLI

### Token-based Authentication

```bash
gh auth login --with-token < ~/.github_token
```

### Set up Git Credential Helper

After authenticating, configure git to use gh for credentials:

```bash
gh auth setup-git
```

This allows git operations (clone, push, pull) to use your gh authentication.

## Verify Installation

```bash
gh auth status
```

Should show:
```
✓ Logged in to github.com as YourUsername
```

## Common Operations

### Repository Management

```bash
# Create a new repo
gh repo create username/repo-name --private --description "Description"

# Clone a repo
gh repo clone username/repo-name

# View repo info
gh repo view username/repo-name
```

### Issues and PRs

```bash
# Create an issue
gh issue create --title "Bug report" --body "Description"

# Create a PR
gh pr create --title "Feature" --body "Description"

# List PRs
gh pr list
```

### GitHub Actions

```bash
# List workflow runs
gh run list

# View a specific run
gh run view <run-id>
```

## Why gh CLI over GitHub MCP Server?

Per Anthropic's Claude Code Best Practices:

1. **Native Support**: Claude Code "knows how to use the `gh` CLI" directly
2. **Simpler Setup**: No extra servers or tokens required beyond local auth
3. **Reliable**: Handles core operations efficiently (PRs, issues, commits)
4. **Training**: Claude is specifically trained on gh CLI usage

The GitHub MCP server is only a fallback when gh is unavailable.

## References

- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [Anthropic Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
