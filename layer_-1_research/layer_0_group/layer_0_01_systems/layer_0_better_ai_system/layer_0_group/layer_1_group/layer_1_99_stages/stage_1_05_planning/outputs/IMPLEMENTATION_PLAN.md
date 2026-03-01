# Implementation Plan - Better AI System

**Date**: 2026-01-30
**Stage**: stage_-1_05_planning → stage_-1_06_development
**Status**: IN PROGRESS

---

## Implementation Order (Priority)

### Phase 1: Foundation Systems (EMPHASIZED)

**Priority 1: AGNOSTIC System** (System Prompt / Tool Portability)
- Create 0AGNOSTIC.md template
- Create .0agnostic/ folder structure
- Implement agnostic-sync.sh transformation script
- Generate CLAUDE.md from 0AGNOSTIC.md

**Priority 2: Episodic Memory** (Agent Amnesia Solution)
- Create session file templates
- Create divergence.log format
- Create conflicts.log format
- Create index.md structure
- Implement compaction logic

**Priority 3: Multi-Agent Sync** (SHIMI Core)
- Implement file locking mechanism
- Implement atomic writes
- Implement change detection (hash-based)
- Implement conflict resolution (last-write-wins)

**Priority 4: Automated Traversal** (SHIMI Core)
- Create 0INDEX.md template
- Place indices at 20-30 branching points
- Implement /find skill
- Integrate LLM-based navigation

### Phase 2: Integration & Testing

- Test all 4 layers together
- Verify SHIMI concepts work
- Test multi-agent scenarios
- Test session continuity (no amnesia)

### Phase 3: Production Deployment

- Deploy to layer_0 (universal)
- Deploy to layer_1 (projects)
- Verify working in real environment

---

## Implementation Targets

| System | Key Files | Location |
|--------|-----------|----------|
| AGNOSTIC | 0AGNOSTIC.md, .0agnostic/, agnostic-sync.sh | Each layer root |
| Episodic | sessions/, divergence.log, index.md | outputs/episodic/ |
| Sync | .locks/, atomic write scripts | Each outputs/ dir |
| Traversal | 0INDEX.md, /find skill | Branching points |

---

## Emphasis Areas

1. **SHIMI Concepts**: File locking, hash-based detection, LLM traversal
2. **System Prompt/AGNOSTIC**: Tool-portable context, lean + detailed split
3. **Agent Amnesia**: Episodic memory preserves context across sessions

All three areas are PRIORITY 1 - implementing now.

