---
resource_id: "cc721803-873f-40ff-b6c2-23f6607e95ac"
resource_type: "readme_output"
resource_name: "README"
---
# Stage 03: .1merge System (AI App Context Porting)

<!-- section_id: "e79432e9-aeab-4ffa-8892-2e3bc8639c8f" -->
## Purpose

The **.1merge system** is the **three-tier merge architecture** that ports 0AGNOSTIC.md context into each AI application's native configuration format.

It enables:
- **Tier 0 (Synced)**: agnostic-sync.sh auto-generates base files from 0AGNOSTIC.md
- **Tier 1 (Overrides)**: App-specific boilerplate templates (tool_boilerplate.md)
- **Tier 2 (Additions)**: Custom enhancements per app

This makes context **portable across 6+ AI apps** (Claude, Cursor, Codex, Gemini, GitHub Copilot, OpenAI) without duplication.

<!-- section_id: "77d53ad7-4145-4ca2-beae-5389905a7416" -->
## Architecture: Two Subsystems

The .1merge system has two parallel subsystems:

<!-- section_id: "c486c1e9-d09b-4c95-8ab6-0482241066b9" -->
### 1. AI App Context Systems (01_ai_app_context_systems/)

**What**: How to port `.0agnostic/` folders to each AI app's native directory structure

**Examples**:
- `.0agnostic/02_rules/` → `.claude/rules/`, `.cursor/rules/`, `.gemini/rules/`, etc.
- `.0agnostic/01_knowledge/` → `.claude/knowledge/`, `.codex/knowledge/`, etc.
- `.0agnostic/03_protocols/` → `.claude/protocols/`, `.cursor/protocols/`, etc.

**Output**: Mirrored directory structures for each AI app

<!-- section_id: "e543438f-de2d-41e3-afe7-3e986b53148a" -->
### 2. AI App Personal System Prompts (02_ai_app_personal_system_prompts/)

**What**: How to port context into each AI app's personal system prompt file

**Examples**:
- 0AGNOSTIC.md → CLAUDE.md (Claude Code native format)
- 0AGNOSTIC.md → AGENTS.md (Multi-agent configuration)
- 0AGNOSTIC.md → GEMINI.md (Google Gemini format)
- 0AGNOSTIC.md → OPENAI.md (OpenAI GPT format)
- 0AGNOSTIC.md → .cursorrules (Cursor IDE format)
- 0AGNOSTIC.md → .github/copilot-instructions.md (GitHub Copilot format)

**Output**: One system prompt file per AI app

<!-- section_id: "1e848781-cc85-41e6-bd85-443f06742e4b" -->
## How It Works: Three-Tier Merge

```
┌─────────────────────────────────────────────────────────────┐
│  Tier 0: Synced (agnostic-sync.sh generates automatically) │
│  ─────────────────────────────────────────────────────────  │
│  CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
                     Merge (Tier 1 overrides)
                            │
┌─────────────────────────────────────────────────────────────┐
│  Tier 1: Overrides (tool_boilerplate.md for each app)      │
│  ─────────────────────────────────────────────────────────  │
│  .1merge/.1claude_merge/1_overrides/tool_boilerplate.md    │
│  .1merge/.1cursor_merge/1_overrides/tool_boilerplate.md    │
│  etc.                                                        │
└─────────────────────────────────────────────────────────────┘
                            ▲
                            │
                     Merge (Tier 2 additions)
                            │
┌─────────────────────────────────────────────────────────────┐
│  Tier 2: Additions (custom tool_additions.md for each app)  │
│  ─────────────────────────────────────────────────────────  │
│  .1merge/.1claude_merge/2_additions/tool_additions.md       │
│  .1merge/.1cursor_merge/2_additions/tool_additions.md       │
│  etc.                                                        │
└─────────────────────────────────────────────────────────────┘

Final output: Merged file = Tier 0 + Tier 1 overrides + Tier 2 additions
```

**Merge Precedence**: Tier 2 > Tier 1 > Tier 0 (additions override overrides override synced base)

<!-- section_id: "2e68e928-cbd2-4e9c-9585-8269a6990888" -->
## Directory Structure

```
.1merge/
├── .1claude_merge/
│   ├── 1_overrides/
│   │   └── tool_boilerplate.md (Claude Code template customizations)
│   └── 2_additions/
│       └── tool_additions.md (Custom Claude Code enhancements)
│
├── .1cursor_merge/
│   ├── 1_overrides/
│   │   └── tool_boilerplate.md (Cursor IDE template customizations)
│   └── 2_additions/
│       └── tool_additions.md (Custom Cursor enhancements)
│
├── .1codex_merge/
│   ├── 1_overrides/
│   │   └── tool_boilerplate.md (Codex template customizations)
│   └── 2_additions/
│       └── tool_additions.md (Custom Codex enhancements)
│
├── .1gemini_merge/
│   ├── 1_overrides/
│   │   └── tool_boilerplate.md (Gemini template customizations)
│   └── 2_additions/
│       └── tool_additions.md (Custom Gemini enhancements)
│
├── .1github_merge/
│   ├── 1_overrides/
│   │   └── tool_boilerplate.md (GitHub Copilot template customizations)
│   └── 2_additions/
│       └── tool_additions.md (Custom GitHub enhancements)
│
└── .1openai_merge/
    ├── 1_overrides/
    │   └── tool_boilerplate.md (OpenAI template customizations)
    └── 2_additions/
        └── tool_additions.md (Custom OpenAI enhancements)
```

<!-- section_id: "1495a3da-b7b4-4066-9bf4-e71d9677cb5a" -->
## AI App Context Systems (Subsystem 01)

**Purpose**: Port `.0agnostic/` folder structure to each AI app's native directory system

**Example: Claude Code (.claude/)**

```
0AGNOSTIC.md
└── .0agnostic/
    ├── 01_knowledge/ → .claude/knowledge/
    ├── 02_rules/ → .claude/rules/
    ├── 03_protocols/ → .claude/protocols/
    └── 06_context_avenue_web/01_file_based/05_skills/ → .claude/skills/
```

**Mapping Rules**:
- Each `.0agnostic/` numbered folder (01_knowledge, 02_rules, etc.) maps to a directory in `.claude/`, `.cursor/`, `.gemini/`, etc.
- Folder structure within each is preserved
- Content sync via `user-level-sync.sh` (for user-level .0agnostic/) or equivalent per entity

**Tools Supported**:
- Claude Code (`.claude/`)
- Cursor IDE (`.cursor/`)
- GitHub Copilot (`.github/`)
- Codex / OpenAI (`.codex/`)
- Google Gemini (`.gemini/`)
- Terminal tools (`.github/cli/`)

<!-- section_id: "67f1470a-b3e3-4d3f-9849-1f9479c46b09" -->
## AI App Personal System Prompts (Subsystem 02)

**Purpose**: Port 0AGNOSTIC.md content into each AI app's personal system prompt format

**Example: Claude Code Format**

```markdown
# Claude Code Context

## Identity
You are an agent at **Layer X** (Entity Type), **Entity**: [Name].
- **Role**: ...
- **Scope**: ...
- **Parent**: ...

## Navigation
- Detailed resources: `.0agnostic/` folder
- Universal rules: [path]
- [Other navigation]

## Key Behaviors
[Extracted from 0AGNOSTIC.md Key Behaviors section]

## Triggers
[Trigger table from 0AGNOSTIC.md]

## Resources
[Resource references from 0AGNOSTIC.md]

---

*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
```

**Supported Formats**:
- **CLAUDE.md** — Claude Code system message
- **AGENTS.md** — Multi-agent orchestration config
- **GEMINI.md** — Google Gemini system prompt
- **OPENAI.md** — OpenAI GPT system prompt
- **.cursorrules** — Cursor IDE rules file
- **.github/copilot-instructions.md** — GitHub Copilot instructions

<!-- section_id: "fb9f8c42-7a56-411a-9a1f-6d36878fee6b" -->
## Merge Execution Workflow

**When agnostic-sync.sh runs**:

```
1. Read 0AGNOSTIC.md
2. Extract STATIC CONTEXT section
3. Generate base CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules
   (These are Tier 0 — synced, auto-generated)

4. For each .1merge/.1{tool}_merge/:
   a. Read 1_overrides/tool_boilerplate.md (Tier 1)
   b. Read 2_additions/tool_additions.md (Tier 2)
   c. Merge: Tier 0 + Tier 1 + Tier 2 → Final {TOOL}.md
   d. Write final file (e.g., CLAUDE.md)
```

<!-- section_id: "497e9d86-5c98-4378-a366-9c908e78df1e" -->
## Validation Checklist

After running merge, verify:

- ✅ All 6 tool files generated (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, .github/copilot-instructions.md)
- ✅ Each file contains full STATIC context from 0AGNOSTIC.md
- ✅ Tier 1 overrides appear in final files (if configured)
- ✅ Tier 2 additions appear in final files (if configured)
- ✅ No duplicate content between tiers
- ✅ All paths/references are valid
- ✅ Grammar and formatting correct
- ✅ Files are readable by respective AI tools

<!-- section_id: "36f97cf5-f299-42c0-b39d-0939bfc37538" -->
## Phase in Propagation Funnel

The .1merge system is the **final translation** between:
- **Upstream**: 0AGNOSTIC.md (canonical entity context)
- **Downstream**: AI app native formats (tool-specific system prompts)

Without .1merge:
- Each AI app would need manual context updates
- Context would diverge across tools
- Changes to 0AGNOSTIC.md wouldn't propagate automatically

With .1merge:
- Single source of truth (0AGNOSTIC.md) propagates to 6+ AI apps
- Automated merge process ensures consistency
- Tool-specific customizations stay isolated in Tier 1-2
- Easy to add new tools (just add new .1{tool}_merge/ subdirectory)

<!-- section_id: "63a0d76d-ffd4-4d9a-9093-04f82545424f" -->
## See Also

- Level 04 (AI Apps) → Final deployment to each AI tool
- `.1merge/` directory structure → Actual merge system implementation
- `agnostic-sync.sh` → Script that executes the merge
- Agnostic Update Protocol → When/how to update .1merge/ content
