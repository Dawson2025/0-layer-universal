---
resource_id: "94639b72-2326-47e7-a427-b9c168b0c013"
resource_type: "output"
resource_name: "04_CLAUDE_FILE_PATH_RULES"
---
# Claude Code CLI — CLAUDE.md File Path Rules and Discovery

**Date**: 2026-02-28
**Focus**: How Claude Code discovers and loads CLAUDE.md files in the hierarchy

---

<!-- section_id: "2708b842-569c-4d58-a1a3-6c435f55b33e" -->
## Overview

Claude Code CLI automatically discovers and loads CLAUDE.md files from a cascading hierarchy. This document explains **exactly how** Claude Code searches for these files, in what order, and how the cascade works.

---

<!-- section_id: "818e2f21-91cd-427a-9d96-2c15603c115a" -->
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

<!-- section_id: "3f513509-b0fb-47c2-98bd-651c61b09105" -->
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

<!-- section_id: "57274e26-57ff-487b-8410-0a2aa9900e16" -->
## The Load Sequence: Step-by-Step

<!-- section_id: "eabe22d6-da45-40b2-829d-683c4e2abc25" -->
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

<!-- section_id: "24bfa5b7-e811-4eaa-93da-7548c5cca69d" -->
### Step 2: Discover Global CLAUDE.md

```
Check: ~/.claude/CLAUDE.md
  ↓
Found? YES
  ↓
Load into context (highest priority, ~5K tokens)
```

**Always exists** (or creates default if missing)

<!-- section_id: "ed36f861-591a-4a5a-8ff8-8520ff67f476" -->
### Step 3: Discover Project CLAUDE.md

```
Check: ~/.claude/projects/[HASH]/CLAUDE.md
  ↓
Found? YES (usually)
  ↓
Load and merge (project settings override global)
```

**May not exist** for new projects (optional)

<!-- section_id: "bc3b3bfc-a93e-4ceb-a378-5827f7ba33ca" -->
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

<!-- section_id: "79590226-4c9b-400c-8d90-6d425ec94e58" -->
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

<!-- section_id: "b430dcc7-6886-40be-82d5-37533d902f78" -->
## Filesystem Structure

<!-- section_id: "72d87539-8a80-44e4-8528-6652f39b5d93" -->
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

<!-- section_id: "1710c52f-e26c-4d32-bc30-12013e319c9d" -->
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

<!-- section_id: "798a8ea7-8261-4d66-8db5-e534294e93af" -->
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

<!-- section_id: "9b944d9e-cbae-4fd9-922b-1fbde78875af" -->
## File Discovery Rules

<!-- section_id: "e6776dd0-6efe-4b3b-bee1-9d9b5e437a0e" -->
### Rule 1: Global CLAUDE.md (Always Loaded)

```
Path: ~/.claude/CLAUDE.md
Loaded: Always, first
Priority: Lowest (overridden by all others)
Size: Should be ≤300 lines (global rules, triggers, resources)
Requirement: MUST EXIST (Claude Code creates default if missing)
```

<!-- section_id: "ccb0d105-caa6-4141-9b93-2dca065512f0" -->
### Rule 2: Project CLAUDE.md (Optional)

```
Path: ~/.claude/projects/[HASH]/CLAUDE.md
Loaded: If exists
Priority: Overrides global
Hash: Computed from current working directory
Requirement: Optional (created automatically for new projects)
```

<!-- section_id: "c2364017-4715-403d-8d78-8184005bc001" -->
### Rule 3: Directory Chain (Optional)

```
Path: [CURRENT_DIR]/CLAUDE.md
Loaded: If exists
Priority: Highest (overrides all)
Traversal: Walks up directory tree
Stops: At git repo root or home directory
Requirement: Optional (only in layered projects)
```

<!-- section_id: "6f1c83e7-522d-4c73-8453-1c415819a86c" -->
### Rule 4: Git Root (If in Repo)

```
Path: [GIT_ROOT]/CLAUDE.md
Loaded: If exists
Priority: Very high (near top of chain)
Detection: Automatic (detects .git directory)
Requirement: Optional (only if using git-based projects)
```

---

<!-- section_id: "2330ce38-d1ba-4fcb-9941-f68bce6dcb51" -->
## Merge Behavior: What "Cascade" Means

When multiple CLAUDE.md files exist, Claude Code **merges** them with specific rules:

<!-- section_id: "4732a521-4bb6-4e3d-af34-265441550f29" -->
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

<!-- section_id: "5e49d2f8-0221-414b-991d-70a0d965bf97" -->
### Merge Strategy

- **Same section name**: Later (higher priority) file wins
- **Different section name**: Both sections kept
- **Conflicts**: Later file overrides earlier file
- **Lists**: Typically appended (depends on structure)

---

<!-- section_id: "b0699de5-f448-4015-8a90-dd2a70baa2d7" -->
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

<!-- section_id: "7b595767-c7ac-4c97-ac6e-6519bb170677" -->
## Commands for Exploring the Chain

| Command | What It Shows |
|---------|--------------|
| `/context` | Full context window breakdown (what's loaded, token usage) |
| `/memory` | Project MEMORY.md (full file, with file selector for topics) |
| `cat ~/.claude/CLAUDE.md` | Global configuration |
| `cat ~/.claude/projects/[HASH]/CLAUDE.md` | Project-specific configuration (if exists) |

---

<!-- section_id: "0e8d9016-376f-4767-96b2-d722331f83bd" -->
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

<!-- section_id: "88141a34-1e22-459e-8b0d-93f4b5cf64ab" -->
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

<!-- section_id: "2fdd9cec-b0f2-47e1-93be-3c823ef9f1ce" -->
## Gotchas and Edge Cases

<!-- section_id: "72805d6c-4abf-4b5c-85c3-9387b88688e7" -->
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

<!-- section_id: "ecffc89c-eccf-465d-bb1e-32dc8ce58509" -->
### Gotcha 2: .gitignore Affects Which Files Load

If CLAUDE.md is in .gitignore, it still loads (Claude Code doesn't respect .gitignore for context files). But git won't version it.

<!-- section_id: "563455d9-d40a-4951-90bf-d9769a2acc1a" -->
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

<!-- section_id: "694adbca-5d61-4900-8081-f6d11b15d720" -->
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

<!-- section_id: "cc7ec4d5-234c-4003-8d87-07dcb38c50a5" -->
## Best Practices

<!-- section_id: "3cffd5bb-5c3c-4866-a32c-a584da5fc384" -->
### 1. Use Global CLAUDE.md for Universal Rules

```
~/.claude/CLAUDE.md should contain:
- Universal rules (apply to ALL projects)
- Global triggers
- Global skills listing
- Global keybindings
```

<!-- section_id: "d59ed3b7-366d-4b1a-80e9-fda5f1947c3e" -->
### 2. Use Project CLAUDE.md for Project-Specific Rules

```
~/.claude/projects/[HASH]/CLAUDE.md should contain:
- Project-specific rules (apply to this project only)
- Project triggers
- Project skills listing
```

<!-- section_id: "b294185f-779c-4e17-8fff-c82868748c9c" -->
### 3. Use Directory CLAUDE.md for Layer Context

```
[DIR]/CLAUDE.md should contain:
- Layer/stage/entity identity
- Layer-specific rules
- Layer-specific triggers
- Current status for this layer
```

<!-- section_id: "9511bad1-ab9c-435d-8f60-7118514b1764" -->
### 4. Avoid Duplication in the Chain

If a rule exists in global CLAUDE.md, don't repeat it in project or directory CLAUDE.md. Let the cascade handle it.

<!-- section_id: "fa2e3464-9035-4baa-9d28-4362f24b583c" -->
### 5. Keep Global CLAUDE.md Small

Global context is loaded for **every project**. Keep it ≤300 lines.

---

<!-- section_id: "9006e9a1-e828-44fc-b750-92cb78829d79" -->
## Summary

Claude Code discovers CLAUDE.md files through a **cascading hierarchy**:

✅ Always loads: `~/.claude/CLAUDE.md` (global)
✅ Optional: `~/.claude/projects/[HASH]/CLAUDE.md` (project)
✅ Optional: `[DIR]/CLAUDE.md` (directory chain, walks up to git root or home)
✅ Merge behavior: Later files override earlier (bottom of chain wins)
✅ Result: Single merged CLAUDE.md loaded into context

This system enables **universal rules** (global), **project-specific context** (project level), and **hierarchical organization** (directory chain) all in one elegant cascade.
