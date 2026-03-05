---
resource_id: "21fe4499-5522-4d05-80f6-feb1bcfb42e1"
resource_type: "document"
resource_name: "GH_CLI_SETUP"
---
# GitHub CLI (gh) Setup for Claude Code

<!-- section_id: "8f5c2b99-8326-4804-9549-349f20b70b17" -->
## Overview

The `gh` CLI is the **recommended way** to interact with GitHub when using Claude Code. According to Anthropic's official best practices, Claude Code is trained to use `gh` directly rather than the GitHub MCP server.

<!-- section_id: "554f43ae-4100-4404-8f06-d6142efa54e7" -->
## Installation

<!-- section_id: "38a977b6-1d50-4fa7-9610-961ac8c80325" -->
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

<!-- section_id: "008885d4-ef14-4239-a806-333c2c52ba64" -->
### macOS

```bash
brew install gh
```

<!-- section_id: "c79d30d4-20a7-491b-907c-738dd4f946db" -->
### Windows

```powershell
winget install --id GitHub.cli
```

<!-- section_id: "0bb1d887-15e2-4a33-97ba-e8d73d618f6c" -->
## Authentication

<!-- section_id: "687b1a92-cb68-4ff0-967b-9aff6c5ba856" -->
### Web-based Authentication (Recommended)

```bash
gh auth login
```

This opens a browser for OAuth authentication. Follow the prompts to:
1. Copy the one-time code displayed
2. Open the URL in your browser
3. Enter the code
4. Authorize the GitHub CLI

<!-- section_id: "74d3fe1e-b9e2-4d5b-9b9d-32c27be89985" -->
### Token-based Authentication

```bash
gh auth login --with-token < ~/.github_token
```

<!-- section_id: "78868e1e-5d01-420b-96a9-31d5decfbbc9" -->
### Set up Git Credential Helper

After authenticating, configure git to use gh for credentials:

```bash
gh auth setup-git
```

This allows git operations (clone, push, pull) to use your gh authentication.

<!-- section_id: "604c33ee-1a22-41c4-802c-24d388189967" -->
## Verify Installation

```bash
gh auth status
```

Should show:
```
✓ Logged in to github.com as YourUsername
```

<!-- section_id: "ec9bc69c-d078-47aa-a29b-dda2ba2dc5e7" -->
## Common Operations

<!-- section_id: "42a59a3a-66fe-4fe5-b22a-26c78e495a9c" -->
### Repository Management

```bash
# Create a new repo
gh repo create username/repo-name --private --description "Description"

# Clone a repo
gh repo clone username/repo-name

# View repo info
gh repo view username/repo-name
```

<!-- section_id: "08f9765a-7251-4954-b182-499f48688ae6" -->
### Issues and PRs

```bash
# Create an issue
gh issue create --title "Bug report" --body "Description"

# Create a PR
gh pr create --title "Feature" --body "Description"

# List PRs
gh pr list
```

<!-- section_id: "5b85dd0f-e177-4041-8ef2-f702794b57ca" -->
### GitHub Actions

```bash
# List workflow runs
gh run list

# View a specific run
gh run view <run-id>
```

<!-- section_id: "24e20d37-ee19-40dd-adbf-a91341b635ae" -->
## Why gh CLI over GitHub MCP Server?

Per Anthropic's Claude Code Best Practices:

1. **Native Support**: Claude Code "knows how to use the `gh` CLI" directly
2. **Simpler Setup**: No extra servers or tokens required beyond local auth
3. **Reliable**: Handles core operations efficiently (PRs, issues, commits)
4. **Training**: Claude is specifically trained on gh CLI usage

The GitHub MCP server is only a fallback when gh is unavailable.

<!-- section_id: "9a251ea7-ed9c-4c99-978c-a2ffa8a69356" -->
## References

- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [Anthropic Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
