---
resource_id: "94639b72-2326-47e7-a427-b9c168b0c013"
resource_type: "output"
resource_name: "04_CLAUDE_FILE_PATH_RULES"
---
# Claude Code CLI — CLAUDE.md File Path Rules and Discovery

**Date**: 2026-02-28
**Focus**: How Claude Code discovers and loads CLAUDE.md files in the hierarchy

---

## Overview

Claude Code CLI automatically discovers and loads CLAUDE.md files from a cascading hierarchy. This document explains **exactly how** Claude Code searches for these files, in what order, and how the cascade works.

---

## The Discovery Hierarchy

Claude Code searches for CLAUDE.md files in this order (top = highest priority):

```
1. ~/.claude/CLAUDE.md                              (Global, always loaded)
   ↓
2. ~/.claude/projects/[PROJECT_HASH]/CLAUDE.md     (Project-specific, if exists)
   ↓
3. [WORKING_DIR]/CLAUDE.md                          (Current directory, if exists)
   ↓
4. [WORKING_DIR]/../CLAUDE.md                       (Parent directory, if exists)
   ↓
5. [WORKING_DIR]/../../CLAUDE.md                    (Grandparent directory, if exists)
   ↓
...continues up directory tree...
   ↓
6. [GIT_ROOT]/CLAUDE.md                             (Git repo root, if exists)
   ↓
7. ~ (home directory, if not already loaded)        (Fallback)
```

**Key principle**: All found files are **merged**, with files higher in the hierarchy **overriding** files lower.

---

## Project Identification: The Hash

Claude Code identifies projects by hashing the **working directory path**:

```
Working Directory: /home/dawson/dawson-workspace/code/0_layer_universal
  ↓ (hash)
Project Hash: a1b2c3d4e5f6 (deterministic, same dir = same hash)
  ↓
Project Directory: ~/.claude/projects/a1b2c3d4e5f6/
  ↓
Contains:
  - CLAUDE.md (project-specific context)
  - memory/MEMORY.md (project memory)
  - history.jsonl (conversation history)
  - status.json (project state)
```

**Hash stability**: The same working directory always produces the same hash. Changing the path changes the hash.

---

## The Load Sequence: Step-by-Step

### Step 1: Session Start

```
User runs: claude [command]
  ↓
Claude Code detects working directory: /home/dawson/dawson-workspace/code/0_layer_universal
  ↓
Claude Code computes project hash: a1b2c3d4e5f6
  ↓
Claude Code checks: ~/.claude/projects/a1b2c3d4e5f6/
```

### Step 2: Discover Global CLAUDE.md

```
Check: ~/.claude/CLAUDE.md
  ↓
Found? YES
  ↓
Load into context (highest priority, ~5K tokens)
```

**Always exists** (or creates default if missing)

### Step 3: Discover Project CLAUDE.md

```
Check: ~/.claude/projects/[HASH]/CLAUDE.md
  ↓
Found? YES (usually)
  ↓
Load and merge (project settings override global)
```

**May not exist** for new projects (optional)

### Step 4: Discover Directory Chain CLAUDE.md

```
Check: [CURRENT_DIR]/CLAUDE.md
  ↓
Found? YES (for layer/stage/entity work)
  ↓
Load and merge (directory settings override project + global)
  ↓
Check: [PARENT_DIR]/CLAUDE.md
  ↓
Found? YES (parent layer context)
  ↓
Load and merge (chain continues upward)
  ↓
Check: [GRANDPARENT_DIR]/CLAUDE.md
  ↓
... (continues until git root or home reached)
```

**Traversal stops at**: Git repository root or home directory (whichever comes first)

### Step 5: Final Merged Context

```
Global CLAUDE.md (lowest priority)
  + Project CLAUDE.md (overrides global)
    + [CURRENT_DIR]/CLAUDE.md (overrides above)
      + [PARENT_DIR]/CLAUDE.md (overrides above)
        + ...
          + [GIT_ROOT]/CLAUDE.md (highest priority)
    ↓
Result: Single merged CLAUDE.md loaded into context
```

**Final size**: Typically 3K-10K tokens depending on directory depth

---

## Filesystem Structure

### Global Level

```
~/.claude/
├── CLAUDE.md                  ← Global rules (always loaded first)
├── settings.json              ← Global settings
├── keybindings.json           ← Global keybindings
├── projects/
│   └── [PROJECT_HASH]/
│       ├── CLAUDE.md          ← Project-specific rules (loaded second)
│       ├── memory/
│       │   └── MEMORY.md      ← Project memory (first 200 lines auto-loaded)
│       ├── history.jsonl      ← Conversation history for this project
│       └── status.json        ← Project state (last model, date, etc.)
└── skills/
    ├── skill-name-1/
    │   └── SKILL.md
    └── skill-name-2/
        └── SKILL.md
```

### Project/Workspace Level

```
/project/
├── CLAUDE.md                  ← Project-level context (loaded third)
├── .claude/
│   ├── rules/                 ← Custom rules for this project
│   │   └── custom-rules.md
│   └── skills/                ← Project-specific skills
│       └── skill-name/
│           └── SKILL.md
└── layer_1/
    └── CLAUDE.md              ← Layer-specific context
        └── layer_1/
            └── CLAUDE.md      ← Entity-specific context
```

### Directory Chain Pattern

```
layer_0_universal/
├── CLAUDE.md                  ← Layer 0: Universal
├── layer_1/
│   ├── CLAUDE.md              ← Layer 1: Project level
│   └── layer_1_projects/
│       └── layer_1_project_school/
│           ├── CLAUDE.md      ← Layer 1 project-specific
│           └── layer_1/
│               ├── CLAUDE.md  ← Layer 2: Sub-project
│               └── layer_1_sub_projects/
│                   └── layer_1_sub_project_classes/
│                       ├── CLAUDE.md  ← Layer 2 sub-project-specific
│                       └── layer_2/
│                           ├── CLAUDE.md  ← Layer 3: Group
│                           └── ...more levels...
```

**Chain pattern**: Each directory can have a CLAUDE.md, and Claude Code loads the entire chain when you work in that directory.

---

## File Discovery Rules

### Rule 1: Global CLAUDE.md (Always Loaded)

```
Path: ~/.claude/CLAUDE.md
Loaded: Always, first
Priority: Lowest (overridden by all others)
Size: Should be ≤300 lines (global rules, triggers, resources)
Requirement: MUST EXIST (Claude Code creates default if missing)
```

### Rule 2: Project CLAUDE.md (Optional)

```
Path: ~/.claude/projects/[HASH]/CLAUDE.md
Loaded: If exists
Priority: Overrides global
Hash: Computed from current working directory
Requirement: Optional (created automatically for new projects)
```

### Rule 3: Directory Chain (Optional)

```
Path: [CURRENT_DIR]/CLAUDE.md
Loaded: If exists
Priority: Highest (overrides all)
Traversal: Walks up directory tree
Stops: At git repo root or home directory
Requirement: Optional (only in layered projects)
```

### Rule 4: Git Root (If in Repo)

```
Path: [GIT_ROOT]/CLAUDE.md
Loaded: If exists
Priority: Very high (near top of chain)
Detection: Automatic (detects .git directory)
Requirement: Optional (only if using git-based projects)
```

---

## Merge Behavior: What "Cascade" Means

When multiple CLAUDE.md files exist, Claude Code **merges** them with specific rules:

### Example: Full Chain Merge

```
Global (~/.claude/CLAUDE.md):
  ## [CRITICAL] Rules
  Rule A: "Always require git commit before push"

Project (~/.claude/projects/a1b2c3d4/CLAUDE.md):
  ## [CRITICAL] Rules
  Rule A: "Always require git commit before push"
  Rule B: "Never edit CLAUDE.md directly"

Directory (/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md):
  ## [CRITICAL] Rules
  Rule A: "Always require git commit before push"
  Rule B: "Never edit CLAUDE.md directly"
  Rule C: "Layer-stage system applies here"

Result (merged):
  Rule A: From Directory (highest priority)
  Rule B: From Directory (highest priority)
  Rule C: From Directory (new rule, added)
  → All rules from all levels coexist, with same-named rules overridden
```

### Merge Strategy

- **Same section name**: Later (higher priority) file wins
- **Different section name**: Both sections kept
- **Conflicts**: Later file overrides earlier file
- **Lists**: Typically appended (depends on structure)

---

## Auto-Loading: MEMORY.md

In addition to CLAUDE.md, Claude Code auto-loads **only the first 200 lines** of MEMORY.md:

```
Path: ~/.claude/projects/[HASH]/memory/MEMORY.md
Loaded: Automatic, at session start
Amount: First 200 lines exactly (not whole file)
Size: ~2K tokens (stays within context budget)
Full file: Available on-demand via /memory command
```

**Not part of cascade**: MEMORY.md is project-specific only (not searched in directory chain).

---

## Commands for Exploring the Chain

| Command | What It Shows |
|---------|--------------|
| `/context` | Full context window breakdown (what's loaded, token usage) |
| `/memory` | Project MEMORY.md (full file, with file selector for topics) |
| `cat ~/.claude/CLAUDE.md` | Global configuration |
| `cat ~/.claude/projects/[HASH]/CLAUDE.md` | Project-specific configuration (if exists) |

---

## Search Algorithm (Pseudo-Code)

```
function load_claude_md(working_dir):
  result = []

  // Step 1: Always load global
  global_path = "~/.claude/CLAUDE.md"
  if exists(global_path):
    result.append(load(global_path))

  // Step 2: Load project-specific
  hash = compute_hash(working_dir)
  project_path = "~/.claude/projects/" + hash + "/CLAUDE.md"
  if exists(project_path):
    result.append(load(project_path))

  // Step 3: Walk directory chain upward
  current_dir = working_dir
  git_root = find_git_root(working_dir)  // or home if no git

  while current_dir != git_root and current_dir != home:
    claude_path = current_dir + "/CLAUDE.md"
    if exists(claude_path):
      result.append(load(claude_path))
    current_dir = parent_directory(current_dir)

  // Step 4: Merge all files (later files override earlier)
  merged = merge_all(result)

  return merged
```

---

## Common Paths Loaded (Example)

**When working in**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_1/layer_1_projects/layer_1_project_school/layer_1/...`

**Claude Code loads (in order)**:

1. `~/.claude/CLAUDE.md` (global)
2. `~/.claude/projects/abc123def456/CLAUDE.md` (project-specific for this directory)
3. `/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md` (layer 0)
4. `/home/dawson/dawson-workspace/code/0_layer_universal/layer_1/CLAUDE.md` (layer 1)
5. `/home/dawson/dawson-workspace/code/0_layer_universal/layer_1/layer_1_projects/CLAUDE.md` (layer 1 projects)
6. `/home/dawson/dawson-workspace/code/0_layer_universal/layer_1/layer_1_projects/layer_1_project_school/CLAUDE.md` (school project)
7. `/home/dawson/dawson-workspace/code/0_layer_universal/layer_1/layer_1_projects/layer_1_project_school/layer_1/CLAUDE.md` (layer 2)
8. ...continues for each level of the hierarchy...

**Result**: Deep cascade of context from global → project → layer → sub-layer

---

## Gotchas and Edge Cases

### Gotcha 1: Hash Changes If Path Changes

```
Project at: /home/user/project/
Hash: xyz789
  ↓ (user moves project)
Project at: /mnt/external/project/
Hash: different!
  ↓
Old ~/.claude/projects/xyz789/ is orphaned
New project treated as separate project
```

**Mitigation**: Don't move projects between paths. If you do, manually migrate the `.claude/projects/[OLD_HASH]/` directory to the new hash, or use `/project-migrate` command.

### Gotcha 2: .gitignore Affects Which Files Load

If CLAUDE.md is in .gitignore, it still loads (Claude Code doesn't respect .gitignore for context files). But git won't version it.

### Gotcha 3: Symlinks and Path Resolution

```
Actual: /path/to/real/project/
Symlink: /path/to/link -> /path/to/real/project/
  ↓
Hash from real path: abc123
Hash from symlink: def456 (different!)
  ↓
Same project, different hashes = two separate projects
```

**Mitigation**: Always use canonical path (resolve symlinks before working)

### Gotcha 4: Moving Between Git Repos

When you `cd` into a different git repository, the chain resets:

```
Working in: /path/to/repo-a/project/
Loaded: repo-a CLAUDE.md chain
  ↓ (user cd's to different repo)
Working in: /path/to/repo-b/project/
Loaded: repo-b CLAUDE.md chain (different!)
  ↓
Old repo-a context is dropped
```

**Mitigation**: Aware behavior — different repos have different context (intentional)

---

## Best Practices

### 1. Use Global CLAUDE.md for Universal Rules

```
~/.claude/CLAUDE.md should contain:
- Universal rules (apply to ALL projects)
- Global triggers
- Global skills listing
- Global keybindings
```

### 2. Use Project CLAUDE.md for Project-Specific Rules

```
~/.claude/projects/[HASH]/CLAUDE.md should contain:
- Project-specific rules (apply to this project only)
- Project triggers
- Project skills listing
```

### 3. Use Directory CLAUDE.md for Layer Context

```
[DIR]/CLAUDE.md should contain:
- Layer/stage/entity identity
- Layer-specific rules
- Layer-specific triggers
- Current status for this layer
```

### 4. Avoid Duplication in the Chain

If a rule exists in global CLAUDE.md, don't repeat it in project or directory CLAUDE.md. Let the cascade handle it.

### 5. Keep Global CLAUDE.md Small

Global context is loaded for **every project**. Keep it ≤300 lines.

---

## Summary

Claude Code discovers CLAUDE.md files through a **cascading hierarchy**:

✅ Always loads: `~/.claude/CLAUDE.md` (global)
✅ Optional: `~/.claude/projects/[HASH]/CLAUDE.md` (project)
✅ Optional: `[DIR]/CLAUDE.md` (directory chain, walks up to git root or home)
✅ Merge behavior: Later files override earlier (bottom of chain wins)
✅ Result: Single merged CLAUDE.md loaded into context

This system enables **universal rules** (global), **project-specific context** (project level), and **hierarchical organization** (directory chain) all in one elegant cascade.
