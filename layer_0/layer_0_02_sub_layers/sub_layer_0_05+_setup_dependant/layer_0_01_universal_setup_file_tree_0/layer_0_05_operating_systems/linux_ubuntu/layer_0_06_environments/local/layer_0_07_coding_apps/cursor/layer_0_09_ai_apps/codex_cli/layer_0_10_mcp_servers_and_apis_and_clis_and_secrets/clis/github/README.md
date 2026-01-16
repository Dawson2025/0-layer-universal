# GitHub Integration for Codex CLI

## Overview

Codex CLI uses **native GitHub integration** via the OpenAI GitHub App - not gh CLI.

## Contents

- **CODEX_GITHUB_INTEGRATION.md** - Full setup and usage guide

## Quick Start

```bash
# 1. Install Codex CLI
npm install -g @openai/codex

# 2. Authenticate
codex auth login

# 3. (Optional) Install GitHub App for PR features
# Visit: https://github.com/apps/openai-codex
```

## Key Difference from Claude Code

| Tool | GitHub Approach |
|------|-----------------|
| Claude Code | Uses `gh` CLI |
| Codex CLI | Native integration + GitHub App |

## Cross-Tool Documentation

See `../_shared/0.06_.../clis/github/` for comparison across AI CLI tools.
