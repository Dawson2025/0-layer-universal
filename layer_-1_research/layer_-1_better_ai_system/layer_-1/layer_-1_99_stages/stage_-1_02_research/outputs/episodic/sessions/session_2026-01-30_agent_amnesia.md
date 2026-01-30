# Session: 2026-01-30 - Agent Amnesia & Context Systems

**Stage**: stage_-1_02_research
**Started**: 2026-01-30
**Status**: Active

---

## Topic

Making AI agents remember their identity, traversal, instantiation, and communication protocols across sessions.

## Key Outcomes

### 1. Dual AGNOSTIC.md + .agnostic/ System Design

- `AGNOSTIC.md` = lean always-loaded content (mirrors CLAUDE.md)
- `.agnostic/` = structured on-demand resources (mirrors .claude/)
- Transforms to tool-specific formats automatically

### 2. Context Efficiency Pattern for Claude Code

| Location | Content | Loaded |
|----------|---------|--------|
| CLAUDE.md | Identity, commands, standards (<500 lines) | Every request |
| .claude/skills/ | Domain knowledge, reference material | On-demand |
| .claude/agents/ | Isolated workers | When spawned |
| .claude/rules/ | Path-specific rules | When matching |

### 3. Output-First Protocol Established

- All outputs written to files BEFORE responding to user
- Enables session continuity across compaction/reboots
- Rule added to CLAUDE.md at this location

### 4. Episodic Memory Structure Created

- `outputs/episodic/` for tracking sessions and changes
- Bare-bones: references semantic memory, tracks timestamps, git info

## Files Created/Modified

| File | Action |
|------|--------|
| `outputs/01_understanding_in_progress/by_topic/agent_amnesia_and_context_systems_conversation.md` | Created - main research |
| `outputs/agent_amnesia_external_approaches.md` | Created - external research |
| `outputs/episodic/` | Created - episodic memory structure |
| `CLAUDE.md` | Modified - added output-first rule |

## Next Session Should

1. Continue designing AGNOSTIC.md + .agnostic/ system
2. Create sync script for agnostic → tool-specific
3. Test pattern on one layer/stage
4. Design universal episodic memory for all locations

## References

- Main research: `../01_understanding_in_progress/by_topic/agent_amnesia_and_context_systems_conversation.md`
- External research: `../agent_amnesia_external_approaches.md`
