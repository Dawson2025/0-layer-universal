# Gemini CLI GitHub Integration

## Overview

As of January 2026, **Google has not published official guidance** for GitHub integration with Gemini CLI. This document provides recommended best practices using standard tools.

## Recommended Approach

Use **standard git** combined with **gh CLI** for GitHub operations.

### Why This Approach?

1. Gemini CLI focuses on general AI assistance, not GitHub-specific features
2. No built-in GitHub integration documented
3. Standard tools provide full functionality
4. gh CLI works independently of any AI tool

## Setup

### 1. Install Gemini CLI

Follow Google's official installation guide for your platform.

### 2. Install gh CLI

```bash
# Linux (Ubuntu/Debian)
sudo apt install gh

# macOS
brew install gh

# Windows
winget install --id GitHub.cli
```

### 3. Authenticate gh CLI

```bash
gh auth login
```

### 4. Configure Git Credentials

```bash
gh auth setup-git
```

## Usage with Gemini CLI

### Workflow Pattern

Use Gemini CLI for AI assistance, gh CLI for GitHub operations:

```bash
# Use Gemini for code assistance
gemini "help me write a function to parse JSON"

# Use gh CLI for GitHub operations
gh repo create myuser/new-repo --private
gh pr create --title "Add JSON parser" --body "New feature"
gh issue create --title "Bug in parser" --body "Details..."
```

### Combined Workflow Example

```bash
# 1. Create a new feature branch
git checkout -b feature/json-parser

# 2. Use Gemini for coding help
gemini "write unit tests for the JSON parser in parser.js"

# 3. Commit changes
git add -A
git commit -m "Add JSON parser with tests"

# 4. Push and create PR with gh
git push -u origin feature/json-parser
gh pr create --title "Add JSON parser" --body "Implements JSON parsing with full test coverage"
```

## Comparison with Other AI CLI Tools

| Feature | Gemini CLI | Claude Code | Codex CLI |
|---------|------------|-------------|-----------|
| **GitHub Integration** | None (use gh CLI) | gh CLI | Native |
| **Official Guidance** | None | Anthropic docs | OpenAI docs |
| **PR Reviews** | Manual | Manual | @codex comments |
| **CI Integration** | Standard | Standard | Codex Autofix |

## Potential Future Integration

Google may add GitHub-specific features to Gemini CLI in the future. Check:
- [Google AI Documentation](https://ai.google.dev/)
- [Gemini CLI releases](https://github.com/google/gemini-cli) (if public)

## Google Cloud Integration

If you're using Gemini CLI with Google Cloud Platform, you may have additional options:

### Cloud Source Repositories

```bash
# If using Google Cloud Source Repositories instead of GitHub
gcloud source repos clone REPO_NAME --project=PROJECT_ID
```

### Cloud Build Integration

Gemini may integrate with Cloud Build for CI/CD on GCP projects. Check Google Cloud documentation for updates.

## Troubleshooting

### gh CLI Authentication Issues

```bash
# Check status
gh auth status

# Re-authenticate if needed
gh auth logout
gh auth login
```

### Git Credential Issues

```bash
# Reset git credential helper
gh auth setup-git

# Verify credentials work
git ls-remote https://github.com/youruser/yourrepo.git
```

## Summary

For Gemini CLI + GitHub:
1. **Install gh CLI** - your GitHub interface
2. **Use Gemini for AI tasks** - code generation, explanations, reviews
3. **Use gh CLI for GitHub ops** - repos, PRs, issues, actions
4. **Use standard git** - commits, branches, merges

This combination provides full functionality while waiting for any official Google guidance.

## References

- [GitHub CLI Documentation](https://cli.github.com/manual/)
- [Google AI Documentation](https://ai.google.dev/)
- [Git Documentation](https://git-scm.com/doc)
