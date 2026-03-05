---
resource_id: "63930b33-ced5-43a6-9a35-eb47acc742c4"
resource_type: "output"
resource_name: "session_2026-01-30_agent_amnesia_research"
---
# Session Log: 2026-01-30 - Agent Amnesia & Context Systems Research

**Layer**: layer_-1 (Research)
**Stage**: 02_research
**Session Start**: 2026-01-30
**Topic**: Making AI agents remember identity, traversal, instantiation, communication

---

<!-- section_id: "73d7cc70-f12d-40e9-9a2b-2bf8cfc6ae97" -->
## Session Summary

This session explored how to solve "agent amnesia" in the layer-stage system.

<!-- section_id: "32439d58-f016-4f79-bc3a-020a8e5c39a6" -->
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

<!-- section_id: "a53dd820-59e3-4d46-a7c8-0fcd04b6c233" -->
### Research Documents Created

| Document | Purpose |
|----------|---------|
| `agent_amnesia_and_context_systems_conversation.md` | Main research findings |
| `agent_amnesia_external_approaches.md` | External framework research |
| `session_2026-01-30_agent_amnesia_research.md` | This session log |

<!-- section_id: "03d82622-ba6c-41d3-9806-83f9dab8c7a3" -->
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

<!-- section_id: "39583901-476a-48fb-89ba-bc6688242275" -->
## Episodic Memory Design (Proposed)

<!-- section_id: "28c27011-bac5-4e4d-8a8e-dd628c4d3646" -->
### Structure

```
outputs/episodic/
├── sessions/
│   └── 2026-01-30_agent_amnesia.md    # This session
├── changes/
│   └── 2026-01-30_changes.md          # File changes this session
└── index.md                            # Quick reference to recent sessions
```

<!-- section_id: "ef526c7c-77e3-436c-9203-e00d04995260" -->
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

<!-- section_id: "22ecdde5-537d-4e21-a26b-09398f45b04c" -->
## Next Actions

1. [ ] Get user approval for proposed changes
2. [ ] Update stage_-1_02_research CLAUDE.md with output-first rule
3. [ ] Create episodic memory structure
4. [ ] Design universal output-first rule for layer_0
5. [ ] Continue research on remaining topics

---

<!-- section_id: "bb3a8d43-3cd0-4e34-b759-483cb882a46c" -->
## Git Status

To be updated after changes are committed.
