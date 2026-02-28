# Existing Infrastructure: Syncthing-Based Distributed AI System

**Status**: Active, Currently Deployed
**Date Documented**: 2026-01-27
**Synced Since**: Early 2026

---

## Overview

The AI system is currently distributed across multiple machines using **Syncthing**, an open-source peer-to-peer file sync tool. This infrastructure enables seamless access to universal rules, skills, memories, and context from any machine.

---

## What Is Synced

### Primary Sync Directory
**Location**: `/home/dawson/dawson-workspace/`

This directory is synced across all machines, containing:

| Component | Path | Status |
|-----------|------|--------|
| **Code Repository** | `code/` | Synced (includes git repos) |
| **Universal Rules** | `code/0_layer_universal/layer_0_group/layer_0_03_sub_layers/sub_layer_0_04_rules/` | Synced |
| **Prompts & Skills** | `code/0_layer_universal/layer_0_group/layer_0_03_sub_layers/sub_layer_0_01_prompts/` | Synced |
| **Knowledge Base** | `code/0_layer_universal/layer_0_group/layer_0_03_sub_layers/sub_layer_0_02_knowledge/` | Synced |
| **Projects** | `code/0_layer_universal/layer_1/` | Synced |
| **Research** | `code/0_layer_universal/layer_-1_research/` | Synced |
| **Dotfiles** | `dotfiles/` | Synced (symlinked to `~/`) |
| **Scripts** | `scripts/` | Synced |
| **Documentation** | `docs/` | Synced |

### Sync Exclusions

Files excluded from sync (`.stignore` patterns):
- `.git/` directories (git manages versioning separately)
- `node_modules/`, `venv/`, other package caches
- `*.log` files (local runtime only)
- System temp files (`__pycache__/`, `.pytest_cache/`, etc.)

---

## Machines Currently Synced

| Machine | OS | Status | Role |
|---------|-----|--------|------|
| Ubuntu (primary) | Linux | Active | Primary development machine |
| Windows | WSL (Linux kernel) | Active | Secondary development / testing |
| [Additional machines] | Various | [Status] | [Role] |

**Note**: Add additional machines and their sync status as they come online.

---

## How It Works

### Session Flow (Cross-Device)

1. **Start Session**: Open Claude Code on any synced machine
2. **CLAUDE.md Cascade**: Claude Code loads context files walking UP the directory tree:
   ```
   ~/.claude/CLAUDE.md (global)
   → /home/dawson/CLAUDE.md
   → /home/dawson/dawson-workspace/CLAUDE.md
   → /home/dawson/dawson-workspace/code/CLAUDE.md
   → /home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md
   → [and deeper layers as needed]
   ```
3. **Rules Loaded**: Universal rules from `layer_0_04_rules/` are accessible
4. **Skills Available**: Any skills from synced `layer_0_01_prompts/` are available
5. **Memory Access**: Memories and learnings from other sessions (stored in synced directories) are queryable
6. **Work Locally**: Make changes on local machine
7. **Sync Propagates**: Changes automatically sync to other machines via Syncthing

### File Sync Latency

- **Local changes**: Available immediately
- **Network sync**: Typically within 2-10 seconds on local network
- **WAN sync**: May take longer depending on connection
- **Conflict handling**: Syncthing uses `.sync` marker files; resolved per FHS patterns

---

## Universal Rules Across All Machines

Because `layer_0_group/layer_0_03_sub_layers/sub_layer_0_04_rules/` is synced:

✓ Same rules apply on all machines
✓ Rules can be updated on any machine (sync propagates)
✓ New rules are immediately available everywhere
✓ No per-machine manual configuration needed

---

## Cross-Device AI Access

### Current Capabilities

**AI tools can:**
- Access `/home/dawson/dawson-workspace/code/0_layer_universal/` from any synced machine
- Read universal rules (which are identical across machines)
- Access shared prompts and skills
- Query memories from sessions on other machines
- Traverse project structure consistently across machines

**Example**: You could:
- Develop feature on laptop (machine A)
- Continue development on desktop (machine B)
- Run tests on VPS (machine C)
- All machines have same rules, skills, and memory context

### Limitations (Current)

- Machines must be on same network (or VPN) for Syncthing
- Changes sync asynchronously (small delay possible)
- Conflict resolution needed if same files edited on multiple machines simultaneously
- Emergency/recovery mode: Rules NOT yet accessible if main filesystem corrupted

---

## Context Architecture Across Machines

### Global Level
```
~/.claude/CLAUDE.md
  └── User-global preferences (managed by user)

/home/dawson/CLAUDE.md
  └── User root level context
```

### Workspace Level
```
/home/dawson/dawson-workspace/CLAUDE.md
  └── Workspace manager
      ├── Provides sync awareness
      └── Lists key directories
```

### Code Root Level
```
/home/dawson/dawson-workspace/code/CLAUDE.md
  └── Code root manager
      └── Points to 0_layer_universal/ as primary
```

### Universal System Level
```
/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md
  ├── Root Manager role
  ├── Embedded universal rules (AI Context Modification Protocol, Commit/Push Rule)
  ├── Lists children: layer_0, layer_1, layer_-1_research
  └── All synced across machines
```

### Layer Level
```
layer_0_group/CLAUDE.md         ← Universal layer (applies to ALL)
layer_1/CLAUDE.md         ← Projects layer
layer_-1_research/CLAUDE.md ← Research layer
```

---

## How AI Tools Use This Infrastructure

### On Session Start

1. **Load**: Claude Code automatically loads cascading CLAUDE.md files
2. **Discover**: AI reads structure and finds:
   - Universal rules (what to follow everywhere)
   - Available skills (what abilities are available)
   - Project context (what's currently being worked on)
   - Hand-off documents (any pending tasks)
3. **Initialize**: Set up with proper context for the session
4. **Execute**: Perform work following loaded rules

### During Session

- AI tools respect universal rules (from `layer_0_04_rules/`)
- AI can access memories/learnings from synced storage
- AI can invoke skills from synced prompts
- AI follows layer-stage patterns for organizing work

### Between Sessions

- All context persists in synced filesystem
- Memories and learnings remain accessible
- Rules/skills can be updated and synced
- Next session picks up from same context

---

## Existing Patterns That Work

### Pattern 1: Universal Rules as Source of Truth

**Works**: Storing universal rules in `/code/0_layer_universal/layer_0_group/layer_0_03_sub_layers/sub_layer_0_04_rules/` and having them synced means:
- AI tools always have correct rules
- Rules updates instantly propagate to all machines
- No per-machine manual configuration needed

### Pattern 2: Hand-Off Documents for Continuity

**Works**: Four-directional hand-off documents in `hand_off_documents/` mean:
- Work can be paused on one machine and resumed on another
- Status persists in synced storage
- Agents can hand off work up/down the hierarchy

### Pattern 3: CLAUDE.md Cascade for Context Inheritance

**Works**: Because CLAUDE.md is hierarchical and synced:
- Starting at any depth gives accumulated context
- Each level adds specificity
- Macros and rules stack properly
- Multi-machine consistency is automatic

### Pattern 4: Agnostic vs. Claude-Specific Split

**Works**: Having both `agnostic.md` (tool-agnostic) and `CLAUDE.md` (Claude-specific) means:
- Patterns survive tool changes
- Claude gets tool-specific optimizations
- Other AI tools can use agnostic structure

---

## Gaps & Future Improvements

### Limitation 1: Emergency/Recovery Mode

**Current**: Rules are NOT accessible if main filesystem corrupted

**Needed**: Redundant rule storage in:
- `/root/.claude/EMERGENCY_RULES.md` (accessible even if /home corrupted)
- `/etc/claude/` (OS-level storage for emergency access)
- Read-only backups on separate partition

### Limitation 2: Multiple User Accounts

**Current**: Rules live in `/home/dawson/` - only accessible to dawson user

**Needed**:
- Universal rules in `/etc/claude/` (accessible by ALL users)
- Per-user overrides in `~/.claude/` (user-specific customizations)
- Audit logging for which user invoked which rule

### Limitation 3: Cross-Machine Conflict Resolution

**Current**: Syncthing has basic conflict handling (`.sync` marker files)

**Needed**:
- Versioning for rules (track which machine has "correct" version)
- Merge strategy for conflicting changes
- Automatic conflict detection and resolution

### Limitation 4: Machine Divergence

**Current**: If one machine is offline, rules might diverge

**Needed**:
- Version control for rules (git already does this)
- Sync validation to ensure consistency
- Rollback capability for conflicts

### Limitation 5: Offline Access

**Current**: Works well on local network; slower on WAN

**Needed**:
- Central repository (git remote) as backup source of truth
- Offline-first capabilities (work without sync, merge later)
- Replication strategy for critical rules

---

## Current Deployment Checklist

- [x] Syncthing installed and configured
- [x] `/home/dawson/dawson-workspace/` synced across machines
- [x] Universal rules in `layer_0_04_rules/` (synced)
- [x] CLAUDE.md files at all hierarchy levels (synced)
- [x] agnostic.md files for tool-agnostic patterns (synced)
- [x] Hand-off documents structure (synced)
- [x] Skills/prompts accessible (synced)
- [ ] Emergency mode rule access (NOT YET)
- [ ] Multi-user support (NOT YET)
- [ ] Cross-machine conflict resolution (BASIC, via Syncthing)
- [ ] Central repository as backup (PLANNED)

---

## Integration with Requirements

This existing infrastructure directly addresses requirements in the Tree of Needs:

| Requirement | How Current System Satisfies It | Gaps |
|------|------|------|
| `need_01_tool_portable` | Rules/skills synced (portable) | Needs ~/opt/ system-wide support |
| `need_02_session_resilient` | Hand-off docs persist across sessions | Works, needs recovery mode support |
| `need_05_cross_platform` | Syncing works on Linux, WSL, macOS | Needs formalized path abstractions |
| `need_06_universal_rules_cross_device` | Universal rules synced, AI access works | Needs multi-user, emergency mode |

---

## References

- **Syncthing**: https://syncthing.net/ - Open-source file sync
- **Universal Rules**: `layer_0_group/layer_0_03_sub_layers/sub_layer_0_04_rules/`
- **System Context Hierarchy Research**: `stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/system_context_hierarchy_research.md`
- **Filesystem Locations Research**: `stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/ai_context_filesystem_locations.md`

---

## Next Steps

1. **Formalize this infrastructure** in request_gathering outputs
2. **Research improvements** in stage_02 (emergency mode, multi-user, conflict resolution)
3. **Design system-wide** locations in stage_04_design
4. **Implement enhancements** in stage_06_development
5. **Test** emergency/recovery scenarios in stage_07_testing

