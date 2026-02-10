# GitHub Operations Protocol (Claude Code CLI)

## Overview

This protocol defines standard procedures for GitHub operations within Claude Code CLI. It covers both CLI-based operations (using `gh` command) and browser-based operations (using MCP servers like Playwright or Claude-in-Chrome).

## Method Selection

### When to Use CLI (`gh` command)
- Creating repos (if `gh` is installed and authenticated)
- Listing repos
- Managing issues and PRs
- Quick operations that don't require visual confirmation

### When to Use Browser Automation
- When `gh` CLI is not available
- When visual confirmation is needed
- When operations require clicking through GitHub UI
- When dealing with org-level SSO authentication

---

## GitHub Repository Operations

### Creating a Repository

#### Via CLI (Preferred when available)
```bash
# Check if repo exists first
gh repo list {owner} --limit 100 --json name --jq '.[].name' | grep -i "{repo-name}"

# Create private repo (ALWAYS use --private unless told otherwise)
gh repo create {owner}/{repo-name} --private --description "Description here"

# Create with specific options
gh repo create {owner}/{repo-name} --private --clone --gitignore Python --license MIT
```

#### Via Browser (Playwright/Claude-in-Chrome)
See: `0.10_mcp_servers_and_apis_and_secrets/playwright-mcp/0.13_protocols/github_browser_automation.md`

### Cloning a Repository
```bash
# HTTPS (recommended)
git clone https://github.com/{owner}/{repo-name}.git

# SSH
git clone git@github.com:{owner}/{repo-name}.git
```

### Renaming a Repository

#### Via CLI
```bash
gh repo rename {new-name} --repo {owner}/{old-name}
```

#### Via Browser
Navigate to Settings → Change name → Click Rename

After renaming, update local remote:
```bash
git remote set-url origin https://github.com/{owner}/{new-name}.git
```

---

## Git Submodule Operations

### Adding a Submodule
```bash
# Basic submodule add
git submodule add https://github.com/{owner}/{repo}.git {path}

# Example: Adding a sub-project
git submodule add https://github.com/Dawson2025/school-math.git layer_2_sub_projects/school-math
```

### Initializing Submodules (after clone)
```bash
# Initialize and fetch all submodules
git submodule update --init --recursive

# Or in one command during clone
git clone --recurse-submodules https://github.com/{owner}/{repo}.git
```

### Updating Submodules
```bash
# Update all submodules to latest commit on their tracked branch
git submodule update --remote --merge

# Update specific submodule
git submodule update --remote --merge {path}
```

### Removing a Submodule
```bash
# 1. Remove from .gitmodules
git config -f .gitmodules --remove-section submodule.{path}

# 2. Remove from .git/config
git config --remove-section submodule.{path}

# 3. Remove the submodule directory
git rm --cached {path}
rm -rf {path}
rm -rf .git/modules/{path}

# 4. Commit changes
git commit -m "Remove submodule {path}"
```

### Moving/Renaming a Submodule
```bash
# 1. Remove old submodule
git submodule deinit {old-path}
git rm {old-path}
rm -rf .git/modules/{old-path}

# 2. Add at new location
git submodule add https://github.com/{owner}/{repo}.git {new-path}

# 3. Commit
git commit -m "Move submodule from {old-path} to {new-path}"
```

---

## Repository Visibility

### CRITICAL RULE: Private by Default

**ALL repositories MUST be created as PRIVATE by default.**

Only create PUBLIC repositories when:
- User explicitly requests public
- Project is intended for open source sharing

### Changing Visibility via CLI
```bash
# Make private
gh repo edit {owner}/{repo} --visibility private

# Make public (ONLY when explicitly requested)
gh repo edit {owner}/{repo} --visibility public
```

### Changing Visibility via Browser
Navigate to Settings → Danger Zone → Change visibility

---

## Repository Naming Conventions

Follow these naming patterns:

| Layer | Format | Example |
|-------|--------|---------|
| Layer 1 (Root) | `{num}-{name}` | `1-school` |
| Layer 2 (Sub) | `{parent}-{name}` | `school-math` |
| Layer 3+ (Sub*N) | `{parent}-{name}` | `school-math-calculus` |

**Rules:**
- Use hyphens, not underscores
- All lowercase
- Short and descriptive

---

## Pre-Operation Checklist

Before any GitHub operation:

- [ ] Verify correct owner/org
- [ ] Check if repo already exists
- [ ] Confirm naming follows conventions
- [ ] Ensure visibility is set to PRIVATE (unless told otherwise)
- [ ] Have description ready

---

## Common Issues & Solutions

### Push Rejected - Remote Has Content
```bash
git pull --rebase origin main
git push -u origin main
```

### Merge Conflicts During Pull
```bash
# View conflicts
git status

# Keep local version
git checkout --ours {file}
git add {file}
git rebase --continue

# Or keep remote version
git checkout --theirs {file}
git add {file}
git rebase --continue
```

### Submodule Not Initialized
```bash
git submodule update --init --recursive
```

### Wrong Remote URL
```bash
# Check current
git remote -v

# Update
git remote set-url origin {correct-url}
```

---

## Security Reminders

1. **Never commit secrets** - API keys, passwords, tokens
2. **Private by default** - Treat all repos as potentially public
3. **Review before push** - Check `git diff` before pushing
4. **Use .gitignore** - Exclude sensitive files

---

**Last Updated**: 2026-01-12
**Applies To**: Claude Code CLI on Linux/Ubuntu
