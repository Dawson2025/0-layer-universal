# Need: Tool Portable

**Branch**: [02_continuous](../)
**Question**: "Can I use Claude Code today, Codex CLI tomorrow?"

---

## Definition

Users should not be locked to one AI app. Same project works with any supported tool.
- Single source of truth for system prompts (agnostic)
- Tool-specific files generated from agnostic source
- Tool-specific customizations preserved during sync

---

## Why This Matters

- Different tools have different strengths
- Tools have different token limits and capabilities
- Users may prefer different tools for different tasks
- Vendor lock-in limits flexibility and resilience

---

## Requirements

### Agnostic Source of Truth (from request_04)
- MUST have AGNOSTIC.md as the canonical system prompt
- MUST have .agnostic/ as the canonical config folder
- MUST be tool-independent (not Claude-specific, not Codex-specific)
- MUST contain all shared knowledge and rules
- MUST work across multiple AI tools (Claude Code, Gemini CLI, Codex CLI, OpenCode CLI)

### Tool-Specific Derivations (from request_04)
- MUST generate tool-specific files from agnostic source
- MUST support: Claude Code, Codex CLI, Gemini CLI, OpenCode CLI
- MUST have sync mechanism to propagate changes
- SHOULD auto-generate tool-specific files when source changes
- SHOULD handle differences in cascade behavior per tool
- SHOULD optimize for each tool's capabilities

### AI App-Specific Overrides (from request_04)
- MUST support tool-specific sections in each tool's file
- MUST separate agnostic content from AI app-specific content
- MUST preserve tool-specific content during sync
- MUST clearly separate agnostic from tool-specific content
- SHOULD support tool-specific resources (MCP for Claude, hooks, commands, etc.)

---

## Acceptance Criteria

- [ ] AGNOSTIC.md exists at each level (source of truth system prompt)
- [ ] .agnostic/ folder exists at each level (source of truth config)
- [ ] .agnostic/sync/ contains scripts to generate tool-specific files
- [ ] CLAUDE.md, GEMINI.md, AGENTS.md, agents.md generated from agnostic
- [ ] Sync mechanism propagates AGNOSTIC.md changes to all tool files
- [ ] Tool-specific content preserved during sync
- [ ] Clear separation between agnostic and AI app-specific content
- [ ] Same project works with all four AI apps

---

## Integrated From

- request_04: REQ-04-F00a, REQ-04-F00b
