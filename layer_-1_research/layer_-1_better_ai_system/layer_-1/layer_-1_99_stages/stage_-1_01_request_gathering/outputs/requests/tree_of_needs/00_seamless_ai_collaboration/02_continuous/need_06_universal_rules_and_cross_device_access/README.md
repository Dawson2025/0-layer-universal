# Need: Universal Rules and Cross-Device Access

**Parent**: [02_continuous](../)
**Status**: Documented with existing implementation
**Date**: 2026-01-27

---

## Overview

This need captures requirements for universal rules that apply everywhere (all users, all filesystem locations, all machines, even in emergency mode) and seamless cross-device access to the AI system.

This need is unique because it's informed by **existing working infrastructure** - you already have a functional distributed system using Syncthing. This requirement formalizes and improves upon that foundation.

---

## Documents in This Folder

| Document | Purpose |
|----------|---------|
| `requirements.md` | Full requirements specification (15 acceptance criteria) |
| `existing_implementation.md` | Current Syncthing system and how it inspired these requirements |

---

## Quick Summary

### The Requirement

**Core Question**: "How does AI access and respect universal rules across all contexts, users, machines, and emergency scenarios?"

**Scope**:
- Any user account on the system
- Any directory in the filesystem
- Normal or emergency/recovery mode
- Any physical machine the user owns
- Offline or online

### What Already Works

✓ Universal rules synced across machines
✓ Rules accessible to AI tools on all machines
✓ Memories and skills persist across sessions
✓ CLAUDE.md cascade ensures context inheritance

### What Needs Improvement

- [ ] Emergency/recovery mode access
- [ ] Multi-user account support
- [ ] System-wide filesystem locations (`/etc/`, `/opt/`, `/var/opt/`)
- [ ] Conflict resolution for multi-machine divergence
- [ ] Offline-first backup strategy

---

## Key Locations

| Item | Location |
|------|----------|
| **Existing Infrastructure** | `../../overview/existing_infrastructure.md` |
| **Requirements** | `requirements.md` (in this folder) |
| **Current Implementation** | `existing_implementation.md` (in this folder) |
| **Universal Rules** | `../../../../../../../code/0_layer_universal/layer_0/layer_0_03_sub_layers/sub_layer_0_04_rules/` |
| **System Context Research** | `../../../../../../../../../stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/system_context_hierarchy_research.md` |
| **Filesystem Locations Research** | `../../../../../../../../../stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/ai_context_filesystem_locations.md` |

---

## Next Steps

1. **Validate** existing implementation against requirements (stage_07_testing)
2. **Research** improvements (stage_02_research)
3. **Design** system-wide architecture (stage_04_design)
4. **Implement** enhancements (stage_06_development)
5. **Test** multi-user, emergency, and cross-machine scenarios

