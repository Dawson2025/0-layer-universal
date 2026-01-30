# Claude Code Memory Gap Analysis

**Date**: 2026-01-30
**Stage**: stage_-1_02_research
**Topic**: Why Claude Code has data but no effective episodic memory

---

## Key Finding

Claude Code stores extensive session data but doesn't use it for memory/continuity.

## What Claude Code Stores

Located in `~/.claude/`:

| Data | File/Folder | Size/Scope |
|------|-------------|------------|
| Conversation history | `history.jsonl` | 1598+ entries |
| Project-specific data | `projects/` | Per-project folders |
| File editing history | `file-history/` | All file changes |
| Todo tracking | `todos/` | Task lists |
| Session environment | `session-env/` | Session state |
| Plans | `plans/` | Plan mode data |
| Tasks | `tasks/` | Task management |

## What It's Used For

| Data | Current Use |
|------|-------------|
| `history.jsonl` | `/resume` command, debugging |
| `projects/` | Session isolation by project |
| `file-history/` | Undo/recovery operations |
| `todos/` | Todo list display |

## What It's NOT Used For

| Missing Capability | What Would Help |
|--------------------|-----------------|
| Auto-load context on new session | "Continuing from yesterday..." |
| Summarize past sessions | "Last 3 sessions covered X, Y, Z" |
| Connect related conversations | "This relates to your work on..." |
| Proactive reminders | "You left off at..." |
| Cross-session learning | "You prefer X approach" |

## The Gap

```
DATA EXISTS → [MISSING] → CONTEXT LOADED
              ↑
              │
    ┌─────────┴─────────┐
    │ What's Missing:   │
    │ • Retrieval       │
    │ • Summarization   │
    │ • Injection       │
    └───────────────────┘
```

### 1. Retrieval Problem
- Which past data is relevant to current session?
- No semantic search over history
- No relevance scoring

### 2. Summarization Problem
- Raw history too large for context window
- No automatic compression
- No extraction of key decisions/outcomes

### 3. Injection Problem
- When to load historical context?
- How much to load?
- How to format it?

## Current Workarounds

### Manual: Output-First Protocol
What we implemented in this research stage:
- Write outputs to files before responding
- Maintain `outputs/episodic/` with session logs
- New sessions can read previous session files

**Pros**: Works now, structured, git-tracked
**Cons**: Manual, requires discipline, per-location setup

### Built-in: /resume Command
- Continues a previous session
- Loads full conversation history
- Limited to single session continuation

**Pros**: Easy, built-in
**Cons**: Only works for immediate continuation, loads full context

## Potential Solutions

### Short-term (What We Can Do)
1. **Output-First Protocol** - Already implemented
2. **Episodic memory structure** - Already implemented
3. **Session summaries** - Write at end of each session
4. **CLAUDE.md pointers** - "Read episodic/ on session start"

### Medium-term (What Claude Code Could Do)
1. **Auto-summarize on session end** - Compress to key points
2. **Load summaries on session start** - Inject recent context
3. **Semantic search over history** - Find relevant past conversations
4. **Project-level memory** - Per-project persistent context

### Long-term (What Would Be Ideal)
1. **Memory retrieval system** - Query past sessions
2. **Automatic context injection** - Load relevant history
3. **Cross-session learning** - Remember preferences/patterns
4. **Hierarchical memory** - Recent detailed, old summarized

## Implications for Our System

The 0AGNOSTIC.md + .0agnostic/ system should:
1. **Not rely on Claude Code's memory** - It doesn't work well
2. **Build our own episodic layer** - outputs/episodic/
3. **Keep context files lean** - Identity, Triggers, Pointers
4. **Use skills for retrieval** - Load history on-demand

## Related Files

- Session log: `outputs/episodic/sessions/session_2026-01-30_agent_amnesia.md`
- Change log: `outputs/episodic/changes/2026-01-30_changes.md`
- Context pattern: `layer_0/.../CONTEXT_FILE_PATTERN.md`
