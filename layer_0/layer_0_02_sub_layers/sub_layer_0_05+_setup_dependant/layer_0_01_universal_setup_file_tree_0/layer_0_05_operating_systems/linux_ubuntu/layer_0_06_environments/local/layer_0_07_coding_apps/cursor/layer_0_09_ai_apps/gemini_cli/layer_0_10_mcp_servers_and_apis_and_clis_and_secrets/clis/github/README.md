# GitHub Integration for Gemini CLI

## Overview

Gemini CLI has **no official GitHub integration** as of January 2026. Use standard tools (git + gh CLI).

## Contents

- **GEMINI_GITHUB_INTEGRATION.md** - Recommended approach using standard tools

## Quick Start

```bash
# Install gh CLI for GitHub operations
sudo apt install gh
gh auth login
gh auth setup-git

# Use Gemini for AI, gh for GitHub
gemini "help me write code"
gh pr create --title "Feature" --body "Description"
```

## Key Point

Unlike Claude Code (gh CLI recommended) and Codex CLI (native integration), Gemini CLI has no GitHub-specific features. Use standard tools.

## Cross-Tool Documentation

See `../_shared/0.06_.../clis/github/` for comparison across AI CLI tools.
