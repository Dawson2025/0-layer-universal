# Codex CLI GitHub Integration

## Overview

OpenAI Codex CLI has **native GitHub integration** built-in. Unlike Claude Code (which recommends gh CLI), Codex uses its own integration via the OpenAI GitHub App.

## How Codex Handles GitHub

### Local Git Operations

Codex CLI works directly with standard git:
- Reads and edits files in your local repo
- Executes git commands (commit, push, pull, etc.)
- No external CLI dependency required

### GitHub App Integration

For advanced features (PR reviews, CI fixes), Codex uses the OpenAI GitHub App:
- Install once on your GitHub repos
- Enables `@codex` mentions in PR comments
- Powers automated CI failure fixes

## Setup

### 1. Install Codex CLI

```bash
npm install -g @openai/codex
```

### 2. Authenticate

```bash
codex auth login
```

This uses your ChatGPT account (Plus or Pro subscription required).

### 3. Install GitHub App (Optional but Recommended)

For PR review and CI features:

1. Go to: https://github.com/apps/openai-codex
2. Click "Install"
3. Select repositories to enable

## Usage

### Local Operations

```bash
cd your-repo

# Have Codex make changes and commit
codex "fix the bug in auth.js and commit the changes"

# Review and push
codex "review the staged changes and push to origin"
```

### PR Reviews (via GitHub)

In any PR comment on an enabled repo:
```
@codex review this PR
@codex suggest improvements to the error handling
@codex check for security issues
```

### CI Autofix

Add to your GitHub Actions workflow (`.github/workflows/ci.yml`):

```yaml
name: CI with Codex Autofix

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run tests
        run: npm test

      - name: Codex Autofix on Failure
        if: failure()
        uses: openai/codex-autofix@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
```

## Comparison: Codex vs Claude Code GitHub Approach

| Aspect | Codex CLI | Claude Code CLI |
|--------|-----------|-----------------|
| **Primary Tool** | Native integration | gh CLI |
| **Git Operations** | Direct git commands | Via gh CLI |
| **PR Reviews** | @codex in comments | Manual via gh |
| **CI Integration** | Codex Autofix action | Standard gh actions |
| **Setup Complexity** | Moderate (app install) | Simple (gh auth) |
| **External Dependencies** | OpenAI GitHub App | gh CLI |

## Do You Need gh CLI with Codex?

**Generally no.** Codex handles GitHub operations natively.

However, gh CLI can still be useful for:
- Creating repos (`gh repo create`)
- Quick issue management (`gh issue create`)
- Viewing workflow runs (`gh run list`)

If you use multiple AI CLI tools, having gh CLI installed provides a universal fallback.

## Supported Repository Types

- ✅ GitHub public repos
- ✅ GitHub private repos (with app installed)
- ❌ GitLab (not supported)
- ❌ Bitbucket (not supported)
- ❌ Azure DevOps (not supported)

## Troubleshooting

### "Repository not found" Error

Ensure the OpenAI GitHub App is installed on the repo:
1. Go to repo Settings → Integrations
2. Check if OpenAI Codex app is listed
3. If not, install from https://github.com/apps/openai-codex

### PR Review Not Responding

- Ensure you're using `@codex` (not `@openai` or `@codex-cli`)
- Check that the app has permissions on the repo
- Verify your OpenAI account has API access

### CI Autofix Not Working

- Ensure `OPENAI_API_KEY` secret is set in repo settings
- Check workflow permissions allow writing to the repo
- Verify the action version is current

## References

- [Codex CLI Documentation](https://developers.openai.com/codex/cli/)
- [Codex GitHub Integration](https://developers.openai.com/codex/integrations/github/)
- [Codex Autofix for GitHub Actions](https://cookbook.openai.com/examples/codex/autofix-github-actions)
