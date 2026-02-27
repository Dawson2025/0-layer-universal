# Subsystem 01: AI App Context Systems

## Purpose

**AI App Context Systems** is how we port **folder structure and knowledge files** from `.0agnostic/` into each AI application's native directory layout.

This enables:
- Each AI app (Claude, Cursor, Gemini, etc.) to have its own copy of rules, knowledge, and protocols
- Mirrored folder structure: `.0agnostic/02_rules/` → `.claude/rules/`, `.cursor/rules/`, etc.
- Synchronized content: changes to universal rules propagate to all apps
- App-specific customization: each tool gets its own versions of shared knowledge

## Mapping: .0agnostic/ → AI App Directories

### Standard Mapping

| Source (.0agnostic/) | → | Claude (.claude/) | Cursor (.cursor/) | Gemini (.gemini/) | Codex (.codex/) |
|----------------------|---|-------------------|--------------------|-------------------|-----------------|
| `01_knowledge/` | → | `.claude/knowledge/` | `.cursor/knowledge/` | `.gemini/knowledge/` | `.codex/knowledge/` |
| `02_rules/static/` | → | `.claude/rules/static/` | `.cursor/rules/static/` | `.gemini/rules/static/` | `.codex/rules/static/` |
| `02_rules/dynamic/` | → | `.claude/rules/dynamic/` | `.cursor/rules/dynamic/` | `.gemini/rules/dynamic/` | `.codex/rules/dynamic/` |
| `03_protocols/` | → | `.claude/protocols/` | `.cursor/protocols/` | `.gemini/protocols/` | `.codex/protocols/` |
| `06_context_avenue_web/01_file_based/05_skills/` | → | `.claude/skills/` | `.cursor/skills/` | `.gemini/skills/` | `.codex/skills/` |

### Example: Claude Code (.claude/) Structure

```
entity_root/
├── 0AGNOSTIC.md (source of truth)
├── CLAUDE.md (auto-generated system prompt)
│
├── .0agnostic/ (universal resources)
│   ├── 01_knowledge/
│   │   ├── layer_stage_system/
│   │   ├── canvas_integration/
│   │   └── ...
│   ├── 02_rules/
│   │   ├── static/
│   │   └── dynamic/
│   └── 03_protocols/
│       ├── stage_report_protocol.md
│       └── ...
│
└── .claude/ (Claude Code mirrored structure)
    ├── CLAUDE.md (THIS is what Claude Code loads)
    ├── rules/ (copy of .0agnostic/02_rules/)
    │   ├── static/
    │   │   └── I0_FILE_CHANGE_REPORTING.md
    │   └── dynamic/
    │       └── grade_strategy_triggers.md
    ├── knowledge/ (copy of .0agnostic/01_knowledge/)
    │   ├── layer_stage_system/
    │   ├── canvas_integration/
    │   └── ...
    ├── protocols/ (copy of .0agnostic/03_protocols/)
    │   ├── stage_report_protocol.md
    │   └── ...
    ├── skills/ (copy of .0agnostic/06_context_avenue_web/01_file_based/05_skills/)
    │   ├── entity-creation/
    │   ├── stage-workflow/
    │   └── ...
    └── episodic_memory/ (session history)
```

## Synchronization Process

### Three Sync Mechanisms

**1. Universal Sync (for all projects)**

Script: `.0agnostic/agnostic-sync.sh`

Syncs:
- Root `.0agnostic/` → All `layer_X/.0agnostic/`
- Universal rules, protocols, knowledge cascade to all layers
- **Skips**: episodic memory, handoff docs, setup-dependant (repo-specific)

**2. User-Level Sync (for Claude Code desktop app)**

Script: `.0agnostic/user-level-sync.sh`

Syncs:
- Root `.0agnostic/` static content → `~/.0agnostic/`
- Generates: `~/.claude/CLAUDE.md`, `~/.claude/AGENTS.md`, etc.
- Supports: `--dry-run` flag, skips unchanged files

**3. AI App Mirroring**

Happens within agnostic-sync.sh merge process:

When Tier 1 (overrides) runs, it:
- Reads `.1merge/.1{tool}_merge/1_overrides/tool_boilerplate.md`
- References WHICH `.0agnostic/` content to include in `.{tool}/`
- Copies/mirrors specified files to `.claude/`, `.cursor/`, etc.

### Example: Canvas Integration Mirroring

**Universal source**:
```
.0agnostic/01_knowledge/canvas_integration/
├── principles/
│   └── grading_model_types.md
├── docs/
│   ├── canvas_mcp_tools_reference.md
│   └── assignment_type_taxonomy.md
└── resources/
    └── templates/
        └── grading_model_template.md
```

**Mirrored to Claude Code**:
```
.claude/knowledge/canvas_integration/
├── principles/
│   └── grading_model_types.md (copy)
├── docs/
│   ├── canvas_mcp_tools_reference.md (copy)
│   └── assignment_type_taxonomy.md (copy)
└── resources/
    └── templates/
        └── grading_model_template.md (copy)
```

**Mirrored to Cursor**:
```
.cursor/knowledge/canvas_integration/
├── principles/
│   └── grading_model_types.md (copy)
├── docs/
│   ├── canvas_mcp_tools_reference.md (copy)
│   └── assignment_type_taxonomy.md (copy)
└── resources/
    └── templates/
        └── grading_model_template.md (copy)
```

## Supported AI Tools

Each AI app gets its own directory with mirrored structure:

| Tool | Directory | Notes |
|------|-----------|-------|
| **Claude Code** | `.claude/` | Primary tool, full mirror |
| **Cursor IDE** | `.cursor/` | Full mirror |
| **GitHub Copilot** | `.github/` | Limited (rules/prompts mostly) |
| **Google Gemini** | `.gemini/` | Full mirror |
| **OpenAI Codex** | `.codex/` | Full mirror |
| **Terminal/CLI** | `.github/cli/` | Scripts and command helpers |

## Folder Structure Rules

### Numbering Convention

All `.0agnostic/` folders are numbered for deterministic ordering:

```
01_knowledge/          (Declarative: what things are)
02_rules/              (Behavioral: what to do when)
03_protocols/          (Procedural: how to do things)
04_episodic_memory/    (Historical: what happened)
05_handoff_documents/  (Transitional: context passing)
06_context_avenue_web/ (Delivery: how context flows)
07+_setup_dependant/   (Environmental: machine/OS-specific)
```

When mirrored to `.claude/`, `.cursor/`, etc., this numbering is preserved:

```
.claude/
├── 01_knowledge/
├── 02_rules/
├── 03_protocols/
├── 04_episodic_memory/
├── 05_handoff_documents/
├── 06_context_avenue_web/
└── 07_setup_dependant/
```

### Content Preservation

When copying files, maintain:
- ✅ Folder hierarchy (no flattening)
- ✅ File names (exact copies)
- ✅ Relative paths within mirrored structure
- ✅ Symbolic links (convert to copies if tool doesn't support symlinks)
- ✅ Timestamps (optional but helps diff tracking)

## Validation Checklist

After mirroring context to AI app directories:

- ✅ All `.0agnostic/` subfolders present in `.{tool}/`
- ✅ File counts match (or explain why different)
- ✅ No missing files from `.0agnostic/`
- ✅ Folder structure preserves hierarchy
- ✅ All relative paths valid within tool directory
- ✅ Tool can load/read all mirrored content
- ✅ No permission issues (files readable by tool)
- ✅ Size reasonable (no bloat, no deletion)

## Use Cases

### Case 1: Developer wants Claude Code + Cursor to have same context

1. Universal `.0agnostic/` stores shared knowledge
2. Sync mirrors it to `.claude/` and `.cursor/`
3. Both tools load from their mirrored copies
4. Update universal source once, both tools get update automatically

### Case 2: New rule needs to propagate everywhere

1. Create rule in `.0agnostic/02_rules/dynamic/{rule_name}/`
2. Run agnosync
3. Rule appears in `.claude/rules/`, `.cursor/rules/`, `.gemini/rules/`, etc.
4. All AI apps see the new rule next time they load context

### Case 3: Tool-specific knowledge customization

1. Universal version at `.0agnostic/01_knowledge/canvas_integration/`
2. Claude Code-specific at `.claude/knowledge/canvas_integration/` (mirrors universal)
3. If Claude-specific customization needed, edit `.1merge/.1claude_merge/` to override

## Phase in Propagation Funnel

AI App Context Systems are the **file-level** distribution mechanism:

- **Upstream**: 0AGNOSTIC.md (content definition)
- **Midstream**: AI App Context Systems (folder mirroring)
- **Downstream**: AI App Personal System Prompts (system message generation)

Without AI App Context Systems:
- Each tool would maintain separate folders
- Updates wouldn't propagate
- Tool-specific versions would diverge

With AI App Context Systems:
- One universal source (`.0agnostic/`)
- Auto-mirrored to all tools
- Single point of truth for all tools

## See Also

- `.0agnostic/agnostic-sync.sh` → How mirroring is implemented
- `.1merge/` → Tier 1 overrides (which files to mirror per tool)
- AI App Personal System Prompts → How to use mirrored content in system prompts
