---
resource_id: "04db4ebc-0d17-4936-bd7f-85279f515824"
resource_type: "knowledge"
resource_name: "OUTPUT_FIRST_PROTOCOL"
---
# Output-First Protocol

**Layer**: layer_0 (Universal)
**Type**: Scenario-Based Rule
**Applies When**: Enabled at a specific location via CLAUDE.md

---

<!-- section_id: "0354ff27-c166-47fd-8236-a0b4a2d14db1" -->
## Purpose

Ensure session continuity by writing outputs to files BEFORE responding to user. This creates persistent memory that survives:
- Auto-compaction
- Session reboots
- New sessions at same location
- Context window limits

---

<!-- section_id: "52ab37e9-9e84-4266-ae0d-caced05d797f" -->
## The Rule

**Before ANY response to user:**

1. **Write output** to appropriate file in `outputs/`
2. **Update episodic memory** in `outputs/episodic/`
3. **Then respond** to user

---

<!-- section_id: "8637720d-40a8-4bc9-af7e-a64cfc3936f8" -->
## Episodic Memory Structure

When enabled at a location, create:

```
outputs/episodic/
├── index.md              # Quick reference to recent sessions
├── sessions/             # Session logs
│   └── session_YYYY-MM-DD_topic.md
└── changes/              # File change logs
    └── YYYY-MM-DD_changes.md
```

<!-- section_id: "b5dbf6fb-9d8a-4418-b268-4716696d4ea5" -->
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

<!-- section_id: "0e0e643b-098b-4dbe-934c-a9180651f937" -->
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

<!-- section_id: "e2caa232-c845-4dcd-a97b-16e377ea20b7" -->
## How to Enable at a Location

Add to the location's CLAUDE.md:

```markdown
## [MANDATORY] Output-First Protocol

**Before ANY response to user, you MUST:**

1. Write your output to a file in `outputs/` first
2. Update `outputs/episodic/` with session/change info
3. THEN respond to user

**File Locations**:
- Research findings: `outputs/[appropriate_folder]/`
- Session logs: `outputs/episodic/sessions/`
- Change logs: `outputs/episodic/changes/`
```

---

<!-- section_id: "cbbb76be-54bb-4c44-a0f7-6f9daee65e48" -->
## Benefits

1. **Session Continuity**: New sessions can read previous session logs
2. **Context Recovery**: After compaction, agent can reload from files
3. **Audit Trail**: All decisions and changes tracked
4. **Git Integration**: Changes can be committed with meaningful history
5. **Cross-Agent Memory**: Other agents at same location can read history

---

<!-- section_id: "6bad6b86-1130-421c-83c6-58e9472013bb" -->
## Related Rules

- `LOCATION_RULE_APPLICATION_PROTOCOL.md` - How to apply rules to locations
- `AI_DOCUMENTATION_PROTOCOL.md` - Where to document work
