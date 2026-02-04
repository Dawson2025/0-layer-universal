# Claude Code Enforcement System - Complete Implementation Guide

**Date Created**: January 29, 2026
**Status**: Complete and Active
**Scope**: Machine-wide enforcement for all Claude Code sessions

---

## Executive Summary

This document describes a complete multi-level enforcement system that ensures Claude Code follows 5 immutable rules across all sessions on the machine. The system uses three hierarchical enforcement levels:

1. **Machine Level** - System-wide policies that cannot be overridden
2. **User Level** - User-global instructions and permissions
3. **Project Level** - Project-specific configurations (inherits parent rules)

The enforcement system prevents rules from being ignored, bypassed, or treated as suggestions. All rules use mandatory language ("YOU WILL", "YOU WILL NOT") and failure to follow them stops work immediately.

---

## Part 1: The 5 [CRITICAL] Rules

### [CRITICAL] 1. AI Context Modification Protocol

**YOU WILL NOT modify ANY AI context files without following this protocol.**

**Scope**: `CLAUDE.md`, `.claude/`, `*_rules/`, `*_prompts/`, `*_knowledge/`, `status.json`

**Required Steps**:
1. **YOU WILL show a complete diagram** of proposed changes with full paths
2. **YOU WILL wait for explicit user approval** - do not proceed until confirmed
3. **YOU WILL execute changes exactly as approved** - no deviations

**Why This Rule Exists**:
- AI context files define how Claude should behave
- Uncontrolled modifications can corrupt the entire system
- Diagrams with approval trails ensure transparency and auditability

**Enforcement Level**: Machine + User + Project (all levels enforce this)

---

### [CRITICAL] 2. AI Context Commit/Push Rule

**YOU WILL commit all approved AI context changes.**

**Required Steps**:
1. `git add [specific files]` - stage ONLY changed files
2. `git commit -m "[AI Context] description"` - use exact format with [AI Context] prefix
3. `git push` - sync to remote immediately

**YOU WILL NOT**:
- Skip git operations
- Amend previous commits (create NEW commits instead)
- Commit without approval
- Push without describing changes

**Why This Rule Exists**:
- Git provides audit trail of all context changes
- Remote sync ensures changes are backed up
- Standardized commit messages enable tracking

**Enforcement Level**: Machine + User (enforced via settings)

---

### [CRITICAL] 3. Context Traversal Rule

**YOU WILL traverse the AI system BEFORE starting any task.**

**Required Steps**:
1. **YOU WILL read all CLAUDE.md files** in the path from root to working directory
2. **YOU WILL identify current layer and stage** (layer_0, layer_1, layer_-1; stages 01-11)
3. **YOU WILL check relevant sub_layers** for applicable rules, prompts, knowledge
4. **YOU WILL read status.json** if it exists to understand current state

**Why This Rule Exists**:
- The layer-stage system contains context that informs how work should be done
- Skipping this step causes errors and wasted time
- Proper context prevents misaligned implementations

**YOU WILL NOT**:
- Assume context without reading files
- Skip layer/stage identification
- Start work without understanding your position in the system

**Enforcement Level**: Machine + User (enforced via CLAUDE.md emphasis)

---

### [CRITICAL] 4. AI Documentation Protocol

**YOU WILL document work in the correct location - EVERY TIME.**

**Layer Structure**:
- **layer_0_group/** - Universal content (applies to all projects)
- **layer_1/layer_1_projects/** - Project-specific content
- **layer_-1_research/** - Research content

**Stage Numbers (01-11)**:
- **01_request_gathering** - Clarify requirements
- **02_research** - Explore, gather info
- **03_instructions** - Define constraints
- **04_planning** - Break into subtasks
- **05_design** - Architecture/design
- **06_development** - Implementation
- **07_testing** - Verification
- **08_criticism** - Review and analysis
- **09_fixing** - Corrections and improvements
- **10_current_product** - Final deliverable
- **11_archives** - Historical records

**YOU WILL NOT**:
- Document in the wrong layer
- Skip stage identification
- Leave work undocumented
- Assume a file belongs in one location without checking

**Why This Rule Exists**:
- Clear documentation location prevents lost work
- Layer-stage system is the organizational backbone
- Enables others to find and use work

**Enforcement Level**: Machine + User (enforced via CLAUDE.md emphasis)

---

### [CRITICAL] 5. Research and Sources Practice

**YOU WILL include sources with ALL research.**

**Required Steps**:
1. **YOU WILL always include a "Sources:" section** at the bottom of your response
2. **YOU WILL format sources as markdown links**: `[Title](URL)`
3. **YOU WILL not hide or omit sources** even if the response is short

**Applies To**: Perplexity searches, WebSearch, WebFetch, and all research tools

**This applies to EVERY research task, no exceptions.**

**Why This Rule Exists**:
- Sources enable verification of information
- Transparent attribution respects intellectual property
- Allows user to explore original sources

**Enforcement Level**: User (enforced via CLAUDE.md emphasis)

---

## Part 2: Machine-Level Enforcement

### Location
```
/etc/claude-code/managed-settings.json
```

### File Characteristics
- **Created**: January 29, 2026
- **Owner**: root
- **Permissions**: Read by all, write by root only
- **Precedence**: HIGHEST - Cannot be overridden by user or project settings

### Contents
The machine-level file contains all 4 core [CRITICAL] rules encoded in JSON format:

```json
{
  "critical_rules": {
    "enforcement_level": "MACHINE_WIDE",
    "precedence": "HIGHEST_IMMUTABLE",
    "description": "These rules apply to EVERY Claude Code session on this machine..."
  }
}
```

### How It Works
1. Claude Code checks `/etc/claude-code/managed-settings.json` FIRST when starting
2. If rules are present, they are MANDATORY for that session
3. User or project settings CANNOT override machine-level rules
4. Rule violations at this level stop all work immediately

### Implementation Details
- Created with `sudo mkdir -p /etc/claude-code/`
- Created with `sudo tee /etc/claude-code/managed-settings.json`
- Read-only to regular users (prevents tampering)
- Cannot be disabled or bypassed

---

## Part 3: User-Level Enforcement

### Files

#### File 1: ~/.claude/CLAUDE.md

**Location**: `/home/dawson/.claude/CLAUDE.md`
**Purpose**: Global instructions that apply to ALL Claude Code sessions
**Size**: ~300 lines

**Contents**:
- Machine-level enforcement notice at TOP
- 5 [CRITICAL] rules with mandatory language ("YOU WILL", "YOU WILL NOT")
- Self-compliance check section (7-item verification checklist)
- Scenario-based rules reference
- Session awareness instructions

**Key Features**:
- Rules are FIRST content user sees
- Each rule states "Failure to follow this rule stops all work immediately"
- Self-compliance checklist ensures verification before task completion
- Committed to git for version control

**Git Status**:
```
Committed: [AI Context] Restructure rules for strict enforcement
Location: ~/.claude/.git/
```

#### File 2: ~/.claude/settings.json

**Location**: `/home/dawson/.claude/settings.json`
**Purpose**: Permission enforcement and tool restrictions
**Format**: Valid Claude Code settings.json schema

**Contents**:
```json
{
  "model": "haiku",
  "permissions": {
    "allow": [
      "Task", "Read", "Edit", "Glob", "Grep", "Write",
      "Bash(git:*)", "Bash(npm:*)", "Bash(ls:*)",
      "WebSearch", "WebFetch"
    ],
    "deny": [
      "Bash(rm -rf:*)", "Bash(rm -f:*)", "Bash(sudo:*)",
      "Bash(*delete*:*)", "Bash(*destroy*:*)"
    ]
  }
}
```

**Key Features**:
- Whitelists SAFE operations (Task, Read, Edit, etc.)
- Blacklists DANGEROUS operations (rm -rf, sudo, delete)
- Blocks destructive bash operations at user level
- Committed to git for version control

**Git Status**:
```
Committed: [AI Context] Add user-level settings.json with compliance requirements
Location: ~/.claude/.git/
```

### How User-Level Works
1. ~/.claude/CLAUDE.md is read at session start
2. Rules are treated as immutable system instructions
3. Self-compliance check prevents work completion if rules violated
4. ~/.claude/settings.json enforces permission restrictions
5. Cannot be overridden by project settings (only added to)

---

## Part 4: Project-Level Enforcement

### How Project-Level Works
1. Each project has `.claude/settings.json` and/or `CLAUDE.md`
2. Project settings can ADD permissions but NOT REMOVE them
3. Project CLAUDE.md can reference user-level rules
4. Machine-level rules ALWAYS apply regardless of project settings

### Example Project Structure
```
project_root/
├── CLAUDE.md (references user/machine rules)
├── .claude/
│   ├── settings.json (adds project-specific permissions only)
│   └── CLAUDE.md (project-specific context)
└── [project files]
```

### Enforcement Chain
```
Machine Rules (MANDATORY)
         ↓
User Rules (MANDATORY - inherited by projects)
         ↓
Project Rules (CAN ADD but NOT REMOVE from parents)
```

---

## Part 5: Enforcement Mechanisms

### Mechanism 1: Structural Enforcement
- Rules positioned at TOP of CLAUDE.md (highest priority in file)
- Use **BOLD**, **CAPS**, and **emphasis** for critical rules
- Short, specific language (not vague or ambiguous)
- Each rule has clear scope and applicability

### Mechanism 2: Behavioral Enforcement
- Rules use **mandatory language**:
  - "YOU WILL NOT modify..."
  - "YOU MUST verify..."
  - "Failure to follow stops all work immediately"
- Makes rules commands, not suggestions
- Creates accountability for violations

### Mechanism 3: Permission Enforcement
- ~/.claude/settings.json blocks dangerous operations
- Whitelist approach: only safe tools enabled by default
- Blacklist dangerous bash patterns
- Works at every session level

### Mechanism 4: Self-Verification
- Self-compliance check (7-item checklist) before task completion
- "If you cannot check ALL boxes, DO NOT complete the task"
- Ensures intentional rule violations are caught
- Puts responsibility on AI to verify compliance

### Mechanism 5: Machine-Level Lock
- /etc/claude-code/managed-settings.json at system level
- Cannot be overridden by any user or project setting
- Applies to ALL sessions on the machine
- Requires sudo to modify (prevents accidental changes)

---

## Part 6: Enforcement Verification Checklist

**Before completing ANY task, verify ALL of these**:

- ✅ Did I read the relevant CLAUDE.md files?
- ✅ Did I identify the current layer and stage?
- ✅ Did I follow the [CRITICAL] rules for this task type?
- ✅ If I modified context files, did I show a diagram and wait for approval?
- ✅ If I did research, did I include a Sources: section?
- ✅ If I committed changes, did I use the [AI Context] format?
- ✅ Did I document work in the correct layer and stage?

**If you cannot check ALL boxes**: DO NOT complete the task. Ask for clarification.

---

## Part 7: File Location Summary

### Machine Level
| File | Location | Owner | Editable |
|------|----------|-------|----------|
| managed-settings.json | `/etc/claude-code/managed-settings.json` | root | Only by sudo |

### User Level
| File | Location | Owner | Editable |
|------|----------|-------|----------|
| CLAUDE.md | `~/.claude/CLAUDE.md` | user | Yes (with git commit) |
| settings.json | `~/.claude/settings.json` | user | Yes (with git commit) |
| .git/ | `~/.claude/.git/` | user | Automatically managed |

### Project Level (Per Project)
| File | Location | Owner | Editable |
|------|----------|-------|----------|
| CLAUDE.md | `./CLAUDE.md` | project | Yes (in project git) |
| settings.json | `.claude/settings.json` | project | Yes (in project git) |

---

## Part 8: Git Workflow

### Initializing User-Level Git
```bash
cd ~/.claude
git init
git add CLAUDE.md settings.json
git commit -m "[AI Context] Initial enforcement system setup"
git push origin master  # If remote configured
```

### Committing Future Changes
```bash
# Make changes to ~/.claude/CLAUDE.md or settings.json

# Stage specific files (not all)
git add ~/.claude/CLAUDE.md

# Commit with [AI Context] prefix
git commit -m "[AI Context] Update rule documentation for clarity"

# Push to remote
git push
```

### Commit Message Format
```
[AI Context] Brief description of what changed and why

Optional detailed explanation if needed
```

### Important Notes
- Always use `[AI Context]` prefix for context file changes
- Never amend commits - create new commits instead
- Never use `git add .` - stage specific files only
- Always push after committing

---

## Part 9: Implementation Timeline

| Date | Action | Status |
|------|--------|--------|
| Jan 29, 2026 | Created `/etc/claude-code/managed-settings.json` | ✅ Complete |
| Jan 29, 2026 | Restructured `~/.claude/CLAUDE.md` | ✅ Complete |
| Jan 29, 2026 | Created `~/.claude/settings.json` | ✅ Complete |
| Jan 29, 2026 | Initialized git in `~/.claude/` | ✅ Complete |
| Jan 29, 2026 | Documented enforcement system | ✅ Complete |

---

## Part 10: Troubleshooting

### Issue: Rules seem to be ignored
**Solution**:
- Check if this is a new Claude Code session (rules reload each session)
- Verify ~/.claude/CLAUDE.md was modified (git status)
- Ensure machine-level file exists: `ls -la /etc/claude-code/managed-settings.json`
- Read the self-compliance checklist before task completion

### Issue: Can't commit changes
**Solution**:
- Ensure you're in the correct directory: `cd ~/.claude`
- Check git status: `git status`
- Use correct commit format: `[AI Context]` prefix required
- Ensure files are staged: `git add [filename]`

### Issue: Permission denied error
**Solution**:
- Machine-level file requires sudo to edit (intentional)
- User and project files should not have permission issues
- Check file ownership: `ls -l ~/.claude/settings.json`
- Do not attempt to bypass machine-level restrictions

---

## Part 11: Design Principles

### Defense in Depth
- Multiple enforcement levels prevent single point of failure
- Machine-level backup ensures rules apply even if user settings corrupt
- Permission system blocks dangerous operations at source

### Least Privilege
- Allow only necessary tools by default
- Deny dangerous operations at all levels
- Force explicit approval for context modifications

### Human Oversight
- All context changes require diagram + approval
- Mandatory self-compliance check before task completion
- Audit trail via git commits

### Fail Secure
- When in doubt, follow the stricter rule
- Machine-level rules override everything
- Violations stop work immediately (fail safe)

### Auditability
- All changes tracked in git
- Commit messages describe what changed and why
- Machine-level policy file is read-only (audit log)

---

## Conclusion

This enforcement system provides:

✅ **Multi-level protection** - Three enforcement layers ensure coverage
✅ **Immutable baseline** - Machine-level rules cannot be bypassed
✅ **Clear accountability** - Mandatory language and self-checks
✅ **Audit trail** - Git commits track all changes
✅ **Fail secure** - Violations stop work immediately

The system treats the 5 [CRITICAL] rules not as suggestions but as immutable system requirements that apply to EVERY Claude Code session on this machine.

---

## Quick Reference: The 5 Rules

| # | Rule | Key Requirement |
|---|------|-----------------|
| 1 | Context Modification | Show diagram + wait for approval before modifying context files |
| 2 | Commit/Push | Commit changes with `[AI Context]` prefix and push immediately |
| 3 | Context Traversal | Read CLAUDE.md, identify layer/stage before starting tasks |
| 4 | Documentation | Document in correct layer (0/1/-1) and stage (01-11) |
| 5 | Sources Practice | Always include Sources: section with all research |

---

## Related Documentation

- Machine-level policy: `/etc/claude-code/managed-settings.json`
- User-level rules: `~/.claude/CLAUDE.md`
- User-level permissions: `~/.claude/settings.json`
- Setup checklist: `outputs/setup_checklist.md` (in this directory)
- Quick reference: `NOTES.md` (in this directory)
