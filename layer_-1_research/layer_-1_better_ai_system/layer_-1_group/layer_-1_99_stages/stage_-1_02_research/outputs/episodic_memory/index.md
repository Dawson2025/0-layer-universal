# Episodic Memory Index

**Location**: stage_-1_02_research
**Purpose**: Track sessions and changes for continuity across compaction/reboots

---

## Recent Sessions

| Date | Topic | Session Log |
|------|-------|-------------|
| 2026-02-08 | Claude Code Chain Testing & Agnostic Gap Analysis | (inline — see outputs below) |
| 2026-02-02 | Research Synthesis Creation | [session_2026-02-02_synthesis.md](sessions/session_2026-02-02_synthesis.md) |
| 2026-02-01 | AI Tool Conventions Research | [session_2026-02-01_tool_conventions.md](sessions/session_2026-02-01_tool_conventions.md) |
| 2026-01-30 | Agent Amnesia & Context Systems | [session_2026-01-30_agent_amnesia.md](sessions/session_2026-01-30_agent_amnesia.md) |

---

## Key Outputs (2026-02-08)

- **Chain test results**: `01_understanding_in_progress/by_topic/claude_code_chain_test_results.md` — 31 PASS, 46 FAIL, 4 WARN
- **Gap analysis**: `../../layer_0_group/layer_0_features/layer_0_feature_context_framework/docs/agnostic_system_gap_analysis.md`
- **Agnostic sync design** (moved from deleted `layer_-1/`): `01_understanding_in_progress/by_topic/agnostic_sync_system_design.md`
- **Finding**: Avenues 1-2 (GAB + integration MD) work well. Agnostic system (0AGNOSTIC, .0agnostic, .1merge, agnostic-sync) is completely invisible to Claude Code context chain (40/40 FAIL).

---

## Synthesis Document

**NEW**: All research consolidated in `01_understanding_in_progress/synthesis/research_synthesis.md`

Use the synthesis for:
- Quick overview of all research topics
- Finding which file to read for specific needs
- Understanding triggers for when to load what
- Tracking what's ready for next stage

---

## How to Use

1. **New session**: Create `sessions/session_YYYY-MM-DD_topic.md`
2. **File changes**: Log in `changes/YYYY-MM-DD_changes.md`
3. **Update this index**: Add entry to Recent Sessions table

---

## Structure

```
episodic/
├── index.md              # This file - quick reference
├── sessions/             # Session logs
│   └── session_YYYY-MM-DD_topic.md
└── changes/              # File change logs with git info
    └── YYYY-MM-DD_changes.md
```
