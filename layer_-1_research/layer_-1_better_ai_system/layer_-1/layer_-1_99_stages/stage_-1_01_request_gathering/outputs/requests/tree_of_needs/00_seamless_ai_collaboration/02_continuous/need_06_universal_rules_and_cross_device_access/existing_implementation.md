# Existing Implementation: Syncthing-Based System

**Status**: Already deployed and working
**Date**: 2026-01-27

---

## Context

This need (`universal_rules_and_cross_device_access`) was developed by examining what ALREADY WORKS in your existing infrastructure. This document explains the existing system and how it informed the requirements.

---

## What Already Exists

### Your Current Setup

You are currently using **Syncthing** to sync `/home/dawson/dawson-workspace/` across multiple machines (Ubuntu, Windows/WSL, etc.).

This sync includes:
- **Universal rules**: `layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/`
- **Skills/prompts**: `layer_0/layer_0_03_sub_layers/sub_layer_0_01_prompts/`
- **Knowledge base**: `layer_0/layer_0_03_sub_layers/sub_layer_0_02_knowledge/`
- **Project structure**: `layer_1/` (all projects)
- **Configuration**: `CLAUDE.md` files at all levels

### How It Works Today

1. **On any machine**, when you start Claude Code, it loads context files walking UP the directory tree
2. **All machines see** the same universal rules (because they're synced)
3. **AI tools automatically** have access to rules, skills, and memories from the synced directory
4. **Changes propagate** to all machines within seconds/minutes

### What This Enables

✓ Same rules apply everywhere
✓ AI context is portable between machines
✓ Skills and memories persist across sessions
✓ Work can be paused on one machine and resumed on another

---

## What Works Well

| Pattern | Why It Works | Location |
|---------|------|----------|
| **Synced Universal Rules** | Files identical across machines → AI sees same rules everywhere | `layer_0_04_rules/` |
| **CLAUDE.md Cascade** | Each machine's Claude Code loads same context hierarchy | `*/CLAUDE.md` |
| **Agnostic + Specific Split** | Framework survives tool changes | `agnostic.md` + `CLAUDE.md` |
| **Four-Directional Handoffs** | Work state persists in synced storage | `hand_off_documents/` |
| **Syncthing Sync** | Automatic propagation without manual work | P2P syncing |

---

## What's Missing (Gaps This Requirement Addresses)

| Gap | Impact | How need_06 Addresses It |
|-----|--------|--------------------------|
| **Emergency Mode Access** | Rules not accessible if main filesystem corrupted | Requires redundant storage in `/etc/`, `/root/` |
| **Multi-User Support** | Rules only accessible to `dawson` user | Requires `/etc/claude/` for all users |
| **Conflict Resolution** | Syncthing handles conflicts but not well for critical rules | Requires versioning and merge strategy |
| **Offline-First** | No clear handling for machine divergence | Requires git as backup source of truth |
| **System-Wide Access** | Rules confined to `/home/` | Requires `/etc/opt/`, `/var/opt/` locations |

---

## How This Need Builds On Current Infrastructure

### From "What Works" to "What's Needed"

**Current State**:
```
/home/dawson/dawson-workspace/code/0_layer_universal/
├── layer_0/
│   └── layer_0_03_sub_layers/
│       └── sub_layer_0_04_rules/
│           └── [universal rules synced across machines]
```

**Needed State** (after fulfilling this requirement):
```
/etc/claude/UNIVERSAL_RULES.md              ← Accessible even in emergency mode
/etc/opt/claude/settings.json               ← System-wide config
/var/opt/claude/shared_memories/            ← Shared cache across users
/home/*/. claude/PERSONAL_OVERRIDES.md      ← Per-user customizations
/root/.claude/EMERGENCY_RULES.md            ← Recovery mode access
[synced backup: git repository]             ← Conflict resolution + backup
```

### Requirements Derived From Current Success

The specific requirements in `requirements.md` came from analyzing what makes the CURRENT system work:

1. **"Universal Rules Across All Accounts"** - You need multiple users to access same rules (currently only `dawson` can)
2. **"Universal Rules Across Filesystem"** - You need rules accessible from `/` level (currently confined to `/home/`)
3. **"Universal Rules in Emergency/Recovery Mode"** - You need rules accessible even if main filesystem fails (currently not resilient)
4. **"Universal Rules Across Machines"** - You already have this via Syncthing; need to formalize and improve
5. **"Cross-Device AI System Access"** - You already can do this; need to ensure it survives infrastructure changes
6. **"Skills and Memories Access Across Devices"** - You already have this; need clearer access patterns

---

## Implementation Path

### Phase 1: Formalize Current System (LOW EFFORT)

- Document existing Syncthing setup
- Create backup git repository
- Test current access patterns across machines
- Establish baseline

### Phase 2: Add Emergency Mode Support (MEDIUM EFFORT)

- Create `/etc/claude/` directory structure
- Copy critical rules to `/root/.claude/`
- Test recovery mode access
- Implement backup/redundancy

### Phase 3: Add Multi-User Support (MEDIUM EFFORT)

- Move system config to `/etc/` (readable by all)
- Create per-user override mechanism
- Implement audit logging
- Test with multiple users

### Phase 4: Add Conflict Resolution (MEDIUM EFFORT)

- Set up git as backup source of truth
- Implement versioning for rules
- Create conflict detection
- Document merge strategies

### Phase 5: Standardize System-Wide Locations (LOW EFFORT)

- Create `/opt/claude/` for system-wide install
- Create `/etc/opt/claude/` for config
- Create `/var/opt/claude/` for runtime data
- Abstract platform differences

---

## Acceptance Criteria (Testing Against Current System)

- [ ] **Current system works**: Verify Syncthing sync, CLAUDE.md cascade, rule access across machines
- [ ] **Emergency access works**: Test in recovery mode, verify rules accessible
- [ ] **Multi-user access works**: Add test user account, verify rule access
- [ ] **Conflict handling works**: Manually create sync conflict, verify resolution
- [ ] **Git backup works**: Verify git repository contains all rules
- [ ] **Cross-platform works**: Test on Linux, WSL, macOS
- [ ] **Documentation complete**: Document all access patterns and procedures

---

## References

See main overview document: `../../../overview/existing_infrastructure.md`

For full requirements: `requirements.md` (in this folder)

