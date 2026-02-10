# Session Log: 2026-01-30 - Agent Amnesia & Context Systems Research

**Layer**: layer_-1 (Research)
**Stage**: 02_research
**Session Start**: 2026-01-30
**Topic**: Making AI agents remember identity, traversal, instantiation, communication

---

## Session Summary

This session explored how to solve "agent amnesia" in the layer-stage system.

### Key Decisions Made

1. **Dual AGNOSTIC.md + .agnostic/ System**
   - `AGNOSTIC.md` = lean always-loaded content (like CLAUDE.md)
   - `.agnostic/` = structured on-demand resources (like .claude/)
   - Transforms to tool-specific formats (CLAUDE.md, AGENTS.md, .claude/, etc.)

2. **Context Efficiency for Claude Code**
   - CLAUDE.md: <500 lines, identity + commands + standards only
   - .claude/skills/: domain knowledge, reference material (on-demand)
   - .claude/agents/: isolated workers (separate context)
   - .claude/rules/: path-specific rules (loaded when matching)
   - .claude/hooks/: deterministic automation (zero LLM tokens)

3. **Skill Structure Clarification**
   - Only `SKILL.md` is required
   - `references/` subfolder is custom organization, not official
   - Supporting files loaded on-demand when Claude reads them

4. **New Rule: Output-First Protocol**
   - Store outputs in files BEFORE telling user
   - Creates episodic memory that survives compaction/reboots
   - Universal rule to be added at layer_0 level

### Research Documents Created

| Document | Purpose |
|----------|---------|
| `agent_amnesia_and_context_systems_conversation.md` | Main research findings |
| `agent_amnesia_external_approaches.md` | External framework research |
| `session_2026-01-30_agent_amnesia_research.md` | This session log |

### Proposed System Changes

1. **Episodic Memory System** (Universal)
   - Bare-bones: references to semantic memory (files)
   - Tracks: timestamps, git commits, diffs
   - Location: TBD (likely `outputs/episodic/` or similar)

2. **Output-First Rule** (Universal)
   - Before responding to user, write output to file
   - Enables session continuity across compaction/reboots

3. **Rule Application Protocol** (Universal)
   - When user says "do X for every API request at location Y"
   - Update .claude/ and CLAUDE.md at that location
   - Make rule permanent for that location

---

## Episodic Memory Design (Proposed)

### Structure

```
outputs/episodic/
├── sessions/
│   └── 2026-01-30_agent_amnesia.md    # This session
├── changes/
│   └── 2026-01-30_changes.md          # File changes this session
└── index.md                            # Quick reference to recent sessions
```

### Change Log Entry Format

```markdown
## 2026-01-30T14:32:00Z

**Files Changed**:
- `outputs/01_understanding_in_progress/by_topic/agent_amnesia_and_context_systems_conversation.md`
  - Git commit: abc1234
  - Diff summary: Added AGNOSTIC.md system design section

**Semantic Memory Updated**:
- New concept: Dual AGNOSTIC.md + .agnostic/ system
- New concept: Output-first protocol for session continuity
```

---

## Next Actions

1. [ ] Get user approval for proposed changes
2. [ ] Update stage_-1_02_research CLAUDE.md with output-first rule
3. [ ] Create episodic memory structure
4. [ ] Design universal output-first rule for layer_0
5. [ ] Continue research on remaining topics

---

## Git Status

To be updated after changes are committed.
