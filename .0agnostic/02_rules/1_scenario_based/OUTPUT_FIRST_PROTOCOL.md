---
resource_id: "24d1e3a1-0a1b-4afa-95b7-7080c0dc91ca"
resource_type: "rule"
resource_name: "OUTPUT_FIRST_PROTOCOL"
---
# Output-First Protocol

**Layer**: layer_0 (Universal)
**Type**: Scenario-Based Rule
**Applies When**: Enabled at a specific location via CLAUDE.md

---

## Purpose

Ensure session continuity by writing outputs to files BEFORE responding to user. This creates persistent memory that survives:
- Auto-compaction
- Session reboots
- New sessions at same location
- Context window limits

---

## The Rule

**Before ANY response to user:**

1. **Write output** to appropriate file in `outputs/`
2. **Update episodic memory** in `.0agnostic/episodic_memory/`
3. **Then respond** to user

---

## Episodic Memory Structure

When enabled at a location, create:

```
.0agnostic/episodic_memory/
├── index.md              # Quick reference to recent sessions
├── sessions/             # Session logs
│   └── session_YYYY-MM-DD_topic.md
└── changes/              # File change logs
    └── YYYY-MM-DD_changes.md
```

### Session Log Template

```markdown
# Session: YYYY-MM-DD - Topic

**Stage**: [current stage]
**Started**: YYYY-MM-DD
**Status**: Active/Complete

## Topic
[What this session is about]

## Key Outcomes
[Decisions made, designs created, etc.]

## Files Created/Modified
| File | Action |
|------|--------|

## Next Session Should
[Continuation points]
```

### Change Log Template

```markdown
# Changes Log: YYYY-MM-DD

**Stage**: [current stage]
**Session**: [session topic]

## Changes Made

### HH:MM - [Action]
**Created/Modified**: `path/to/file`
- [Description of change]
- Git commit: [if committed]
```

---

## How to Enable at a Location

Add to the location's CLAUDE.md:

```markdown
## [MANDATORY] Output-First Protocol

**Before ANY response to user, you MUST:**

1. Write your output to a file in `outputs/` first
2. Update `.0agnostic/episodic_memory/` with session/change info
3. THEN respond to user

**File Locations**:
- Research findings: `outputs/[appropriate_folder]/`
- Session logs: `.0agnostic/episodic_memory/sessions/`
- Change logs: `.0agnostic/episodic_memory/changes/`
```

---

## Benefits

1. **Session Continuity**: New sessions can read previous session logs
2. **Context Recovery**: After compaction, agent can reload from files
3. **Audit Trail**: All decisions and changes tracked
4. **Git Integration**: Changes can be committed with meaningful history
5. **Cross-Agent Memory**: Other agents at same location can read history

---

## Related Rules

- `LOCATION_RULE_APPLICATION_PROTOCOL.md` - How to apply rules to locations
- `AI_DOCUMENTATION_PROTOCOL.md` - Where to document work
