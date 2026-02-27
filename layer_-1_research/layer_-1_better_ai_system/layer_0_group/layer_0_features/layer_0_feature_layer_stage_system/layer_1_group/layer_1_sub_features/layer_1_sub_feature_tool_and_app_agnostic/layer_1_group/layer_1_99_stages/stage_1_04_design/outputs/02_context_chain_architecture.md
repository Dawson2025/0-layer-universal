# Context Chain Architecture: AI Apps vs MCP Server Tools

**Date**: 2026-02-27
**Status**: ✅ Designed (terminology clarified, architecture identified)
**Author**: Claude Code Session

---

## Executive Summary

The context delivery system for AI agents involves TWO distinct categories that must not be conflated:

1. **AI Apps** (5 clients that receive context) — Claude Code CLI, Cursor IDE, GitHub Copilot, Google Gemini, OpenAI/Codex
2. **MCP Server Tools** (external services providing capabilities) — Canvas LMS API, Perplexity Search, Tavily, filesystem, bash

Previous documentation sometimes used "tools" to mean both, creating confusion. This design document clarifies the architecture and establishes terminology.

---

## Terminology Clarification

### AI Apps (LLM Clients)

AI apps are **integration points where AI models receive context and tools**. Each app has its own native configuration system and directory structure.

| App | Type | Config Location | Context Directory | Notes |
|-----|------|-----------------|-------------------|-------|
| **Claude Code** | CLI tool | `~/.claude/` | `.claude/` | Primary dev environment |
| **Cursor** | IDE | `.cursor/` | `.cursor/` | VSCode-based editor |
| **GitHub Copilot** | VS Code extension | `.github/` | `.github/` | Enterprise-ready |
| **Google Gemini** | Web/CLI | `.gemini/` | `.gemini/` | Google integration |
| **Codex/OpenAI** | API client | `.codex/` | `.codex/` | OpenAI integration |

### MCP Server Tools (External Capabilities)

MCP Server Tools are **external services providing specific capabilities** through standardized Model Context Protocol interfaces. They are NOT context recipients — they are context providers (and data sources).

| MCP Server Tool | Type | Purpose | Example Use |
|-----------------|------|---------|-------------|
| **Canvas LMS API** | Educational platform | Fetch assignments, grades, attendance | Grade dashboard skill |
| **Perplexity Search** | Web search engine | Search web, answer questions, reason | Research tasks |
| **Tavily** | Web search (cheaper) | Fact checking, source finding | Quick lookups |
| **Bash** | OS shell | Execute commands, file operations | Build, test, deploy |
| **File System** | Local storage | Read/write files | Knowledge base |

---

## Context Chain Architecture

### Three Layers of Context Delivery

The complete context chain has **three layers**:

```
Layer 0: Source of Truth (0AGNOSTIC.md)
  ↓
Layer 1: Universal Context (agnostic-sync.sh output)
  ├── CLAUDE.md (for Claude Code app)
  ├── AGENTS.md (for coordination)
  ├── GEMINI.md (for Gemini app)
  ├── OPENAI.md (for OpenAI/Codex app)
  ├── .cursorrules (for Cursor IDE)
  └── .github/copilot-instructions.md (for GitHub Copilot)
  ↓
Layer 2: AI App Integration (.1merge port system)
  ├── .claude/ (Claude Code native config)
  │   ├── skills/
  │   ├── rules/
  │   └── CLAUDE.md (context)
  ├── .cursor/ (Cursor IDE native config)
  │   └── rules/
  ├── .codex/ (OpenAI/Codex native config)
  │   └── CODEX.md
  ├── .gemini/ (Google Gemini native config)
  │   └── GEMINI.md
  └── .github/ (GitHub Copilot config)
      ├── copilot-instructions.md
      └── instructions/
```

### What Flows Through Each Layer

**Layer 0 → Layer 1 (agnostic-sync.sh)**

The `agnostic-sync.sh` script extracts STATIC context from `0AGNOSTIC.md` and generates markdown files customized for each AI app:

- **CLAUDE.md** — Full context (all sections) for Claude Code
- **AGENTS.md** — Coordination context (entity definition, triggers)
- **GEMINI.md** — Full context for Google Gemini
- **OPENAI.md** — Full context for OpenAI/Codex
- **.cursorrules** — Lean context (Identity + Navigation) for Cursor IDE
- **.github/copilot-instructions.md** — Medium context (Identity + Triggers + Navigation) for GitHub Copilot

### Layer 1 → Layer 2 (.1merge port system)

The `.1merge/` directory system (THREE-TIER MERGE) ports the Layer 1 context to each AI app's native config structure:

**Three-Tier Merge Pattern**:

```
.1merge/
├── .1claude_merge/
│   ├── 1_overrides/              ← Synced + overrides
│   │   ├── tool_boilerplate.md
│   │   └── (Claude-specific overrides)
│   └── 2_additions/               ← Additional content
│       └── (Claude-specific additions)
│
├── .1cursor_merge/
│   ├── 1_overrides/
│   │   └── cursor_boilerplate.md
│   └── 2_additions/
│       └── (Cursor-specific additions)
│
├── .1github_merge/
│   ├── 1_overrides/
│   └── 2_additions/
│
└── (similar for .1codex_merge/, .1gemini_merge/)
```

**Merge Logic**:

1. **Tier 0**: Base content from Layer 1 (CLAUDE.md, .cursorrules, etc.) — universal, synced from source
2. **Tier 1 (1_overrides/)**: App-specific boilerplate (tool_boilerplate.md) — what each app's native format requires
3. **Tier 2 (2_additions/)**: Custom content additions — app-specific enhancements or fixes

**Result**: For each app, merge produces final output at app's native location:

```
Claude Code:    .claude/CLAUDE.md       (Layer 1 CLAUDE.md + .1claude_merge/)
Cursor:         .cursor/rules           (Layer 1 .cursorrules + .1cursor_merge/)
GitHub Copilot: .github/...             (Layer 1 .github/copilot-instructions.md + .1github_merge/)
Gemini:         .gemini/GEMINI.md       (Layer 1 GEMINI.md + .1gemini_merge/)
Codex:          .codex/CODEX.md         (Layer 1 OPENAI.md + .1codex_merge/)
```

---

## Context Chain Data Flow

### Request to Response (With AI Apps & MCP Tools)

```
User makes request to AI App (e.g., "what's my grade in CSE 300?")
  ↓
AI App loads context from Layer 2 config
  ├── Loads .claude/CLAUDE.md (if Claude Code)
  ├── Loads .cursor/rules (if Cursor)
  └── (similar for other apps)
  ↓
Context includes triggers → "User asks about grade status" trigger matches
  ↓
Load Layer 1 content (via 0AGNOSTIC.md references)
  ├── Trajectory stores (`.0agnostic/03_protocols/`)
  ├── Rules (`.0agnostic/02_rules/`)
  ├── Knowledge (`.0agnostic/01_knowledge/`)
  └── Skills (`.0agnostic/06_context_avenue_web/05_skills/`)
  ↓
Execute skill → Skill invokes MCP Server Tool
  ├── Call `mcp__canvas__canvas_assignment_list()` (MCP Tool)
  ├── Call `mcp__canvas__canvas_get_my_submission()` (MCP Tool)
  └── Process results
  ↓
Generate response → AI App outputs result to user
```

### Example: CSE 300 Grade Dashboard Request

```
1. User (in Claude Code): "How am I doing in CSE 300?"

2. Claude Code loads from Layer 2:
   - Reads .claude/CLAUDE.md (contains triggers, skill references)
   - Identifies trigger: "User asks about grade status"

3. Load Layer 1 + Layer 0 content:
   - Load trigger rule: `.0agnostic/02_rules/dynamic/grade_strategy_triggers/`
   - Load trajectory: `.0agnostic/03_protocols/grade_strategy_system/canvas_grade_dashboard_trajectory.md`
   - Load grading model: `.0agnostic/01_knowledge/course_info/grading_model.md` (CSE 300 specific)

4. Execute skill:
   - Invoke `/cse300-dashboard` skill
   - Skill executes 7-step workflow from trajectory
   - Step 1: Call MCP Tool `mcp__canvas__canvas_assignment_list(course_id=406222)`
     - Returns Canvas API data (assignments, submissions)
   - Step 3-4: Count completions, compute total percentage
   - Step 7: Generate dashboard markdown

5. Claude Code outputs dashboard to user

Note: Canvas API (MCP Tool) is called FROM the skill execution, not loaded as "context".
The MCP Tool is a capability provider, not a context recipient.
```

---

## Key Distinctions

### AI Apps Receive Context

✅ AI Apps are **context recipients**. They receive `.0agnostic/` content via:
- Layer 1 generated files (CLAUDE.md, .cursorrules, GEMINI.md, etc.)
- Layer 2 ported configs (.claude/, .cursor/, .github/, etc.)
- These files contain instructions, triggers, skill references, rules

### MCP Server Tools Don't Receive Context

❌ MCP Server Tools **don't receive context**. They receive:
- Function calls with parameters (e.g., `canvas_assignment_list(course_id=406222)`)
- These calls come FROM AI app skill execution
- MCP Tools return data which AI app processes using its context

### Example Comparison

| Entity | Type | Receives Context? | Receives Calls? | Returns |
|--------|------|-------------------|-----------------|---------|
| Claude Code | AI App | ✅ Yes (CLAUDE.md) | ❌ No | Text response to user |
| Cursor IDE | AI App | ✅ Yes (.cursor/rules) | ❌ No | Code completions to user |
| Canvas MCP Tool | MCP Server | ❌ No | ✅ Yes (`canvas_assignment_list()`) | Assignment data |
| Perplexity MCP Tool | MCP Server | ❌ No | ✅ Yes (`perplexity_search()`) | Search results |

---

## .1merge Port System Design

### Purpose

The `.1merge/` system ensures that `.0agnostic/` content (universal, synced from source) can be **ported to each AI app's native directory structure** with app-specific customization.

### Three-Tier Merge Strategy

**Tier 0 (Synced)**: Base content from agnostic-sync.sh output
- Source: `0AGNOSTIC.md` → processed by agnostic-sync.sh
- Format: Markdown (CLAUDE.md, .cursorrules, GEMINI.md, OPENAI.md, etc.)
- Versioning: Regenerated on every 0AGNOSTIC.md change

**Tier 1 (Overrides)**: App-specific boilerplate
- Contains: `tool_boilerplate.md` files describing what each app's native format requires
- Purpose: Define how universal content maps to app-native directory structure
- Example:
  ```yaml
  # .1claude_merge/1_overrides/tool_boilerplate.md
  Claude_SOURCE: CLAUDE.md           # Take universal CLAUDE.md
  CLAUDE_DEST: .claude/CLAUDE.md     # Place in .claude/CLAUDE.md

  SKILLS_SOURCE: .0agnostic/06_context_avenue_web/05_skills/
  SKILLS_DEST: .claude/skills/       # Copy skills to .claude/skills/

  RULES_SOURCE: .0agnostic/02_rules/
  RULES_DEST: .claude/rules/         # Copy rules to .claude/rules/
  ```

**Tier 2 (Additions)**: Custom enhancements
- Contains: App-specific files that supplement Tier 0+1
- Purpose: Fix issues, add missing content, customize per app
- Example: `.1cursor_merge/2_additions/cursor_extra_rules.md` with Cursor-specific rules

### Merge Execution

The merge system (not yet implemented, designed) would:

1. Read Tier 0 (universal CLAUDE.md, .cursorrules, etc.)
2. Read Tier 1 (app-specific boilerplate, mapping rules)
3. Read Tier 2 (custom additions)
4. **Merge** them with **Tier 2 > Tier 1 > Tier 0** precedence (later tiers override)
5. **Port** result to app-native location (e.g., .claude/, .cursor/)

### Example Merge for Claude Code

```
Input:
  Tier 0: CLAUDE.md (universal, 50KB, contains all context)
  Tier 1: .1claude_merge/1_overrides/tool_boilerplate.md
    ├── CLAUDE_SOURCE: CLAUDE.md
    ├── CLAUDE_DEST: .claude/CLAUDE.md
    ├── SKILLS_SOURCE: .0agnostic/06_context_avenue_web/05_skills/
    └── SKILLS_DEST: .claude/skills/
  Tier 2: .1claude_merge/2_additions/
    ├── claude_extra_rules.md
    └── claude_skill_additions.md

Process:
  1. Read CLAUDE.md (all rules, triggers, navigation, resources)
  2. Apply boilerplate mapping:
     - Copy CLAUDE.md → .claude/CLAUDE.md
     - Copy .0agnostic/06_context_avenue_web/05_skills/* → .claude/skills/
     - Copy .0agnostic/02_rules/* → .claude/rules/
  3. Apply additions:
     - Merge claude_extra_rules.md into .claude/CLAUDE.md [or create separate file]
     - Merge claude_skill_additions.md into skills or create new skill file
  4. Verify all content is in place

Output:
  .claude/
  ├── CLAUDE.md (merged context from Tier 0+1+2)
  ├── skills/
  │   ├── (copied from .0agnostic/06_context_avenue_web/05_skills/)
  │   └── (+ additions from Tier 2)
  └── rules/
      ├── (copied from .0agnostic/02_rules/)
      └── (+ additions from Tier 2)
```

### Why Three-Tier Merge?

1. **Tier 0 (Synced)**: Keeps source-of-truth content consistent across all apps without duplication
2. **Tier 1 (Overrides)**: Documents what each app needs (its native format, directory structure) — explicit mapping
3. **Tier 2 (Additions)**: Allows app-specific enhancements without breaking Tier 0 regeneration workflow

**Result**: When `0AGNOSTIC.md` is updated and `agnostic-sync.sh` regenerates, all AI apps automatically receive the update via Tier 0, while Tier 1 & 2 customizations persist.

---

## Current Implementation Status

### Implemented

✅ **Layer 0**: `0AGNOSTIC.md` files created at every entity level (layer_2, layer_3, layer_4 projects)

✅ **Layer 1**: `agnostic-sync.sh` script generates:
- CLAUDE.md (full context)
- AGENTS.md (coordination context)
- GEMINI.md (full context)
- OPENAI.md (full context)
- .cursorrules (lean context)
- .github/copilot-instructions.md (medium context)

### Designed But Not Yet Implemented

🔄 **Layer 2 (.1merge port system)**:
- Three-tier merge logic designed
- `.1merge/` directory structure defined
- **Not yet implemented** — requires:
  - Merge orchestration script (reads Tier 0+1+2, produces final app-specific outputs)
  - Boilerplate specifications for each AI app
  - Integration with agnostic-sync.sh or separate execution

---

## Context Avenue Web Integration

The `.0agnostic/06_context_avenue_web/` structure supports both file-based AND data-based context delivery:

### File-Based Avenues (01-08) — Currently in Use

1. **01_aalang/** — AALang/GAB JSON-LD agent definitions
2. **02_aalang_markdown_integration/** — Markdown summaries of AALang agents
3. **03_auto_memory/** — Claude Code auto-memory topic files
4. **04_@import_references/** — Entity structure, compliance checklist, etc.
5. **05_skills/** — Skill definitions (SKILL.md files with triggers)
6. **06_agents/** — Agent stubs and orchestrators
7. **07_path_specific_rules/** — Directory-specific rule overrides
8. **08_hooks/** — Event hooks for automation

### Data-Based Avenues (09-13) — Future Extensibility

9. **09_knowledge_graph/** — Graph representation of knowledge relationships
10. **10_relational_index/** — SQL/structured relationships
11. **11_vector_embeddings/** — Semantic embeddings for similarity search
12. **12_temporal_index/** — Time-ordered logs and versioning
13. **13_shimi_structures/** — Specialized data structures

---

## Propagation Chain Verification

For context to flow correctly from source to AI app:

```
✓ 0AGNOSTIC.md created (source of truth)
  ↓
✓ agnostic-sync.sh run (generates Layer 1 files)
  ↓
✓ Layer 1 files reviewed (CLAUDE.md, .cursorrules, etc. contain correct content)
  ↓
✓ .1merge/ boilerplate created (maps Layer 1 → Layer 2 apps)
  ↓
✓ Merge orchestration script executes (ports to .claude/, .cursor/, etc.)
  ↓
✓ AI app loads from Layer 2 location (reads .claude/CLAUDE.md, etc.)
  ↓
✓ Triggers evaluate, skills invoke, MCP Server Tools called
  ↓
✓ User receives response
```

If any step is missing, context doesn't reach AI app.

---

## References

- **Terminology Clarification**: This document (2026-02-27)
- **agnostic-sync.sh Implementation**: `0_layer_universal/.0agnostic/agnostic-sync.sh`
- **Entity Structure Reference**: `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md`
- **MCP Server Tools Reference**: `.0agnostic/07+_setup_dependant/sub_layer_0_10_mcp_servers_and_apis/`
- **Canvas MCP Tool Documentation**: `.0agnostic/07+_setup_dependant/.../sub_layer_0_10_canvas_mcp/`

---

## Summary

The context chain architecture consists of:

1. **AI Apps** (5 clients: Claude Code, Cursor, Copilot, Gemini, Codex) that receive context via Layer 1→2 flow
2. **MCP Server Tools** (Canvas, Perplexity, Tavily, etc.) that provide capabilities via function calls, not context
3. **Three-layer delivery**: Source of truth (Layer 0) → Universal generated files (Layer 1) → App-native ports (Layer 2)
4. **.1merge port system** (three-tier merge) that customizes universal context for each app
5. **Context Avenue Web** with 13 avenues providing different representations of the same knowledge

The key insight: **AI Apps receive context; MCP Server Tools receive function calls.** These are fundamentally different roles in the system.
