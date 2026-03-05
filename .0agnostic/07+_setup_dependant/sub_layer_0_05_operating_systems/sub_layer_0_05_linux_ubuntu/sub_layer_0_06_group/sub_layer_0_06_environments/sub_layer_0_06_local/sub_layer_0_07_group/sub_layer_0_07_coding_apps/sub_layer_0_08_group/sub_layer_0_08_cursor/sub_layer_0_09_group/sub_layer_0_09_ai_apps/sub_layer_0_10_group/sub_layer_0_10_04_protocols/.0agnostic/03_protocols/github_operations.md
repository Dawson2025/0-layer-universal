---
resource_id: "db961209-5c4a-46fe-9d59-ef9d2475ae00"
resource_type: "protocol"
resource_name: "github_operations"
---
# GitHub Operations Protocol (Claude Code CLI)

<!-- section_id: "c20d0638-033a-4cc4-a00b-52a64cde4d02" -->
## Overview

This protocol defines standard procedures for GitHub operations within Claude Code CLI. It covers both CLI-based operations (using `gh` command) and browser-based operations (using MCP servers like Playwright or Claude-in-Chrome).

<!-- section_id: "2f2d0db5-e764-4ef0-9a76-771f256bbef3" -->
## Method Selection

<!-- section_id: "90317ae6-01c3-4451-b1a6-eaf576c4e073" -->
### When to Use CLI (`gh` command)
- Creating repos (if `gh` is installed and authenticated)
- Listing repos
- Managing issues and PRs
- Quick operations that don't require visual confirmation

<!-- section_id: "eda3f01e-5748-4c15-b2f8-a5837b8122a8" -->
### When to Use Browser Automation
- When `gh` CLI is not available
- When visual confirmation is needed
- When operations require clicking through GitHub UI
- When dealing with org-level SSO authentication

---

<!-- section_id: "576f50aa-4cff-477f-bca4-a896a881e289" -->
## GitHub Repository Operations

<!-- section_id: "f7352ed5-5be6-48d9-9e26-3f8e68c9602c" -->
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

<!-- section_id: "a0aa5551-ea48-4e2b-bf50-a573a41d042b" -->
### Cloning a Repository
```bash
# HTTPS (recommended)
git clone https://github.com/{owner}/{repo-name}.git

# SSH
git clone git@github.com:{owner}/{repo-name}.git
```

<!-- section_id: "1bc57daf-5224-47d1-aca5-a66b137311f3" -->
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

<!-- section_id: "e03f91bc-07bb-4845-976a-f70f5fb7125e" -->
## Git Submodule Operations

<!-- section_id: "96cae218-d567-421d-97d2-09d6a982d978" -->
### Adding a Submodule
```bash
# Basic submodule add
git submodule add https://github.com/{owner}/{repo}.git {path}

# Example: Adding a sub-project
git submodule add https://github.com/Dawson2025/school-math.git layer_2_sub_projects/school-math
```

<!-- section_id: "e88a7556-94a8-45bc-85f4-f28579c92d49" -->
### Initializing Submodules (after clone)
```bash
# Initialize and fetch all submodules
git submodule update --init --recursive

# Or in one command during clone
git clone --recurse-submodules https://github.com/{owner}/{repo}.git
```

<!-- section_id: "6f4d96e4-99ea-4a56-88ea-7ef31f431ad2" -->
### Updating Submodules
```bash
# Update all submodules to latest commit on their tracked branch
git submodule update --remote --merge

# Update specific submodule
git submodule update --remote --merge {path}
```

<!-- section_id: "b08164bb-d482-4ae5-9413-0d73f15b325a" -->
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

<!-- section_id: "afc35b76-956c-4b6a-821b-93541b1e1731" -->
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

<!-- section_id: "b3e0824d-3e29-448e-a454-704788eeb633" -->
## Repository Visibility

<!-- section_id: "de7c0adc-f633-4e51-b926-9fdfc6f90aa8" -->
### CRITICAL RULE: Private by Default

**ALL repositories MUST be created as PRIVATE by default.**

Only create PUBLIC repositories when:
- User explicitly requests public
- Project is intended for open source sharing

<!-- section_id: "a2a58dcd-9800-4e8c-985e-b6c9059297ec" -->
### Changing Visibility via CLI
```bash
# Make private
gh repo edit {owner}/{repo} --visibility private

# Make public (ONLY when explicitly requested)
gh repo edit {owner}/{repo} --visibility public
```

<!-- section_id: "5d7684ce-e59d-4b9d-a6ac-551a46128e08" -->
### Changing Visibility via Browser
Navigate to Settings → Danger Zone → Change visibility

---

<!-- section_id: "80d51b86-7d53-47ad-8491-0129edb5d94b" -->
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

<!-- section_id: "94e8bb8c-97d4-4dbb-987b-43a9c014724b" -->
## Pre-Operation Checklist

Before any GitHub operation:

- [ ] Verify correct owner/org
- [ ] Check if repo already exists
- [ ] Confirm naming follows conventions
- [ ] Ensure visibility is set to PRIVATE (unless told otherwise)
- [ ] Have description ready

---

<!-- section_id: "ad1c19fa-b0d7-42bb-b54c-2a3a3c40c0af" -->
## Common Issues & Solutions

<!-- section_id: "09edcefe-3bf7-4d1d-afcc-a69c43bd270a" -->
### Push Rejected - Remote Has Content
```bash
git pull --rebase origin main
git push -u origin main
```

<!-- section_id: "7b233f30-614a-455c-bafb-fb9bd08b057c" -->
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

<!-- section_id: "56932ac0-7b95-4298-9ca3-0d207a94da7a" -->
### Submodule Not Initialized
```bash
git submodule update --init --recursive
```

<!-- section_id: "76de994b-5061-451c-b29f-664fdb39cabe" -->
### Wrong Remote URL
```bash
# Check current
git remote -v

# Update
git remote set-url origin {correct-url}
```

---

<!-- section_id: "0a83b927-c643-424a-84b9-cbe4aaba2bcf" -->
## Security Reminders

1. **Never commit secrets** - API keys, passwords, tokens
2. **Private by default** - Treat all repos as potentially public
3. **Review before push** - Check `git diff` before pushing
4. **Use .gitignore** - Exclude sensitive files

---

**Last Updated**: 2026-01-12
**Applies To**: Claude Code CLI on Linux/Ubuntu
