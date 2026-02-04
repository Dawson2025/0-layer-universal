# Research: Agnostic Memory System

**Related Request**: REQ-04 (AI Dynamic Memory System)
**Status**: In Progress
**Date**: 2026-01-26

---

## Problem Statement

How do we create a persistent memory system that:
1. Works without heavy context load
2. Works across multiple AI apps (Claude Code, Codex CLI, Gemini CLI, OpenCode CLI)
3. Has a single source of truth
4. Allows AI app-specific customizations

---

## Key Findings

### Claude Code's CLAUDE.md Cascade

From research (Perplexity conversation, existing documentation):

- Claude Code **automatically walks up the directory tree**
- Loads ALL parent CLAUDE.md files
- Merges into one unified system prompt
- General rules from top + specific context from current level
- This IS the mechanism for "memory without context bloat"

**Contrast with other tools**:
- OpenCode (agents.md): Single file from current directory only, no cascade
- Codex CLI (AGENTS.md): Single file, no cascade
- Gemini CLI (GEMINI.md): Manual composition required

### Existing Implementation

The manager-agent hierarchy pattern is already documented in:
- `layer_0_group/layer_0_01_ai_manager_system/README.md`
- `layer_0_feature_ai_manager_hierarchy_system/.../architecture.md`
- `layer_0_feature_ai_manager_hierarchy_system/.../tools_and_context_systems.md`

---

## Proposed Architecture

### Naming Convention

| Purpose | Agnostic (Source) | Claude Code | Codex CLI | Gemini CLI | OpenCode |
|---------|-------------------|-------------|-----------|------------|----------|
| System prompt | AGNOSTIC.md | CLAUDE.md | AGENTS.md | GEMINI.md | agents.md |
| Config folder | .agnostic/ | .claude/ | - | - | - |

### Single-File Pattern (Agnostic + AI App-Specific)

Each AI app's file contains both synced agnostic content and app-specific content:

```markdown
# CLAUDE.md

<!-- BEGIN AGNOSTIC -->
[Synced from AGNOSTIC.md - do not edit manually]

## Purpose
Common instructions for all AI apps...

## Rules
Universal rules...

<!-- END AGNOSTIC -->

## Claude Code-Specific

[Edit freely - preserved during sync]

- MCP servers configuration
- Claude Code output styles
- /slash commands
- Claude Code-specific tools
```

### Sync Mechanism Concept

```
AGNOSTIC.md                         # Source of truth (edit here)
    ↓ sync script
CLAUDE.md                           # Single file with both sections
├── <!-- BEGIN AGNOSTIC -->         # REPLACED by sync
│   [content from AGNOSTIC.md]
│   <!-- END AGNOSTIC -->
└── ## Claude Code-Specific         # PRESERVED by sync
    [AI app-specific content]
```

### AI App-Specific Sections

Each AI app can have its own specific configurations:

| AI App | File | App-Specific Section Contents |
|--------|------|------------------------------|
| Claude Code | CLAUDE.md | MCP servers, output styles, /slash commands |
| Codex CLI | AGENTS.md | Execution limits, sandbox settings, approval modes |
| Gemini CLI | GEMINI.md | API options, search settings, model parameters |
| OpenCode CLI | agents.md | Tool permissions, configurations |

### Directory Structure Concept

```
project/
├── AGNOSTIC.md            # Source of truth (tool-agnostic system prompt)
├── .agnostic/             # Source of truth config folder
│   ├── agents/            # Agent definitions (agnostic)
│   ├── skills/            # Skill definitions (agnostic)
│   ├── rules/             # Rules (agnostic)
│   └── sync/              # Sync scripts to generate tool-specific
│
├── CLAUDE.md              # Derived: Claude Code (agnostic + Claude-specific)
├── .claude/               # Derived: Claude Code config
│
├── AGENTS.md              # Derived: Codex CLI (agnostic + Codex-specific)
├── GEMINI.md              # Derived: Gemini CLI (agnostic + Gemini-specific)
└── agents.md              # Derived: OpenCode CLI (agnostic + OpenCode-specific)
```

---

## Open Questions (For Further Research)

1. **Sync Implementation**: How exactly should the sync script work?
   - File watcher for auto-sync?
   - Manual trigger?
   - Git hooks?

2. **Marker Format**: Are `<!-- BEGIN AGNOSTIC -->` markers the best approach?
   - Alternatives: YAML frontmatter, special comments, separate files

3. **Cascade Handling**: How to handle tools that don't cascade?
   - Flatten hierarchy for non-cascading tools?
   - Include parent content in the file?

4. **Conflict Resolution**: What if agnostic and app-specific content conflict?

5. **Validation**: How to validate that sync worked correctly?

---

## Related Research

- Perplexity conversation: `/home/dawson/Downloads/Hey, how's it going_ (1).md`
- Existing architecture docs: `layer_0_feature_ai_manager_hierarchy_system/`
- Tools and context systems: `.../tools_and_context_systems.md`

---

## Next Steps

1. **Research Stage**: Explore sync implementation options
2. **Instructions Stage**: Formalize the approach
3. **Design Stage**: Detailed technical design
4. **Planning Stage**: Implementation task breakdown
