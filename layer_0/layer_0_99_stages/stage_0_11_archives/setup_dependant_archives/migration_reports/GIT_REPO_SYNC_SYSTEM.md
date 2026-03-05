---
resource_id: "07720e74-020c-483c-8e82-6379d26afddc"
resource_type: "document"
resource_name: "GIT_REPO_SYNC_SYSTEM"
---
# Git Repository Sync System

**Last Updated:** 2026-01-11

This document describes the system for managing git repositories across multiple operating systems in the `dawson-workspace` synced folder.

<!-- section_id: "47a88cf7-890d-4d9e-a2fd-fb09d2297929" -->
## Overview

The `dawson-workspace` folder syncs across Windows, WSL, and Ubuntu using Syncthing with a VPS relay. However, `.git` directories are **excluded from Syncthing sync** to prevent conflicts during git operations. This means each OS needs to set up its own git connection to GitHub.

This system automates that process.

<!-- section_id: "750b7729-4fd4-421a-9588-ea005353af5f" -->
## Architecture

```
dawson-workspace/                    ← Synced via Syncthing
├── .stignore                        ← Excludes .git from sync
├── .git-repos.json                  ← Central registry of all repos
├── setup-git-repos.sh               ← Automation script
└── code/
    └── 0_ai_context/
        ├── .git/                    ← NOT synced (local to each OS)
        ├── .git-repo.json           ← Individual repo documentation
        └── 0_context/               ← Content IS synced
```

<!-- section_id: "d8dc93fa-1e4b-4811-b43b-8b6b9718b418" -->
### Key Principle

- **File content** syncs via Syncthing (automatic, real-time)
- **Git history** syncs via GitHub (manual `git pull`/`git push`)
- Each OS maintains its own `.git` directory

<!-- section_id: "9a3248e8-2bff-4b92-8467-96dfb5ad930b" -->
## Files

<!-- section_id: "f5fecb87-5454-47d1-a0e0-7e8c1cf709ac" -->
### 1. `.stignore` (Workspace Root)

Located at: `~/dawson-workspace/.stignore`

Tells Syncthing to exclude `.git` directories from sync:

```
// Syncthing ignore patterns for dawson-workspace
// Exclude .git directories to prevent sync conflicts during git operations
.git
```

<!-- section_id: "18d1ac9e-a8db-4a66-b2c3-e9d6f98c267e" -->
### 2. `.git-repos.json` (Workspace Root)

Located at: `~/dawson-workspace/.git-repos.json`

Central registry of all git repositories in the workspace:

```json
{
  "description": "Central registry of git repositories in this workspace",
  "last_updated": "2026-01-11",
  "repos": [
    {
      "path": "code/0_ai_context",
      "remote": "git@github.com:Dawson2025/0-universal-context.git",
      "branch": "main",
      "description": "Universal AI context and documentation system"
    }
  ]
}
```

**To add a new repo**, append an entry to the `repos` array with:
- `path`: Relative path from workspace root
- `remote`: Git SSH URL
- `branch`: Default branch name
- `description`: Human-readable description

<!-- section_id: "c10312ce-a20b-46c7-81ff-d3285a149c0d" -->
### 3. `setup-git-repos.sh` (Workspace Root)

Located at: `~/dawson-workspace/setup-git-repos.sh`

Automation script that:
1. Reads `.git-repos.json`
2. Checks each repo for a `.git` directory
3. If missing, initializes git and connects to the remote
4. Fetches and resets to match the remote branch

**Usage:**

```bash
# Run the setup (normal mode)
~/dawson-workspace/setup-git-repos.sh

# Preview what would be done (no changes)
~/dawson-workspace/setup-git-repos.sh --dry-run

# Show detailed output
~/dawson-workspace/setup-git-repos.sh --verbose

# Show help
~/dawson-workspace/setup-git-repos.sh --help
```

**Requirements:**
- `jq` must be installed (`sudo apt install jq` on Ubuntu)
- SSH key must be configured for GitHub access

<!-- section_id: "7ed026fe-9cfb-4344-afcf-70e60fa152c8" -->
### 4. `.git-repo.json` (Per Repository)

Located in each git repo directory, e.g.: `~/dawson-workspace/code/0_layer_universal/.git-repo.json`

Documents the individual repository for manual setup or reference:

```json
{
  "name": "0-universal-context",
  "description": "Universal AI context and documentation system",
  "remote": {
    "origin": "git@github.com:Dawson2025/0-universal-context.git",
    "https": "https://github.com/Dawson2025/0-universal-context.git"
  },
  "branch": "main",
  "setup_instructions": {
    "summary": "This directory should be connected to the 0-universal-context GitHub repository.",
    "auto_setup": "Run ~/dawson-workspace/setup-git-repos.sh from any OS to automatically set up all git repos.",
    "manual_setup": [
      "cd ~/dawson-workspace/code/0_ai_context",
      "git init --initial-branch=main",
      "git remote add origin git@github.com:Dawson2025/0-universal-context.git",
      "git fetch origin",
      "git reset --mixed origin/main",
      "git branch --set-upstream-to=origin/main main"
    ],
    "verify": [
      "git remote -v   # Should show origin pointing to 0-universal-context",
      "git status      # Should show 'On branch main' and 'up to date'"
    ]
  },
  "notes": {
    "syncthing": "The .git directory is excluded from Syncthing sync (via .stignore) to prevent conflicts.",
    "workflow": "File changes sync via Syncthing. Run 'git pull' after booting to get commits from other OS."
  }
}
```

<!-- section_id: "66d8794e-a810-43d1-83b2-5c39b5a6b8af" -->
## Workflow

<!-- section_id: "78ba0948-60ae-4200-800f-4df856d495a1" -->
### When Booting Into a New OS

1. **Syncthing syncs automatically** - All file content syncs from VPS
2. **Run setup script**:
   ```bash
   ~/dawson-workspace/setup-git-repos.sh
   ```
3. **Pull latest commits** (if any were made on other OS):
   ```bash
   cd ~/dawson-workspace/code/0_layer_universal
   git pull
   ```

<!-- section_id: "92e49ebf-eae8-4485-a8bf-892fd2d5321d" -->
### Daily Workflow

1. **Make changes** - Edit files normally
2. **Changes sync via Syncthing** - Other OS gets file changes automatically
3. **Commit when ready**:
   ```bash
   git add -A
   git commit -m "Your message"
   git push
   ```
4. **On other OS** - Run `git pull` to get the commits

<!-- section_id: "9b6176f2-8549-4d22-b943-a12844e21bce" -->
### Handling Conflicts

Since Syncthing syncs file content and git syncs history, conflicts can occur:

1. **Syncthing conflict files** (`.sync-conflict-*`):
   - Review and merge manually
   - Delete conflict file after resolving

2. **Git merge conflicts**:
   - Resolve normally with `git mergetool` or manual editing
   - Commit the resolution

<!-- section_id: "5d546f42-9a35-475e-b969-8fce36e120ce" -->
## Adding a New Repository

1. **Add to central registry** (`~/.git-repos.json`):
   ```json
   {
     "path": "code/new-project",
     "remote": "git@github.com:Dawson2025/new-project.git",
     "branch": "main",
     "description": "New project description"
   }
   ```

2. **Create individual config** (optional but recommended):
   Create `~/dawson-workspace/code/new-project/.git-repo.json` with setup instructions.

3. **Run setup script** on current OS:
   ```bash
   ~/dawson-workspace/setup-git-repos.sh
   ```

4. **On other OS** - Script will auto-detect and set up the new repo.

<!-- section_id: "9e83caac-8c84-41c9-accd-6d28588b1c46" -->
## Troubleshooting

<!-- section_id: "ba374d97-1565-4568-b9e5-4dff8d190aa9" -->
### Script says "jq is required"

Install jq:
```bash
# Ubuntu/Debian
sudo apt install jq

# macOS
brew install jq

# Windows (via Chocolatey)
choco install jq
```

<!-- section_id: "34b9980d-6d6f-4808-893c-26e9f0c322b8" -->
### SSH key not working

Ensure your SSH key is set up for GitHub:
```bash
# Check if key exists
ls -la ~/.ssh/id_ed25519

# Test GitHub connection
ssh -T git@github.com
```

<!-- section_id: "34174c52-1d90-470b-a09a-4286c5c19c6c" -->
### Git fetch fails

1. Check network connection
2. Verify SSH key is added to GitHub
3. Try HTTPS URL instead:
   ```bash
   git remote set-url origin https://github.com/Dawson2025/0-universal-context.git
   ```

<!-- section_id: "090b4f51-197a-49f8-8aad-bf731a1d5c46" -->
### Files not syncing

1. Check Syncthing is running
2. Verify folder status in Syncthing GUI (http://localhost:8384)
3. Check `.stignore` isn't excluding needed files

<!-- section_id: "9be7a0ce-85a8-4551-b85f-e07a06b4ea32" -->
## Related Documentation

- [Multi-OS Sync System](../../-1_research/-1.01_things_researched/multi_os_system/README.md) - Overall sync architecture
- [STATUS.md](../../-1_research/-1.01_things_researched/multi_os_system/STATUS.md) - Current sync status
- [VPS_CREDENTIALS.md](../../-1_research/-1.01_things_researched/multi_os_system/VPS_CREDENTIALS.md) - VPS access details

<!-- section_id: "e6c0a41d-bb33-496c-98c9-ded5d577a9d3" -->
## File Locations Quick Reference

| File | Location | Purpose |
|:---|:---|:---|
| `.stignore` | `~/dawson-workspace/` | Exclude .git from Syncthing |
| `.git-repos.json` | `~/dawson-workspace/` | Central repo registry |
| `setup-git-repos.sh` | `~/dawson-workspace/` | Automation script |
| `.git-repo.json` | Each repo directory | Individual repo docs |
