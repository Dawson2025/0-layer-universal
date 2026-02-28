# Session: AI Tool Conventions Research

**Date**: 2026-02-01
**Stage**: Research (02)
**Topic**: Layer-Stage Instantiation - AI Tool Native Conventions

---

## Summary

Completed research on AI coding tool native conventions for the three-tier folder architecture (.0agnostic → .1*_merge → native outputs).

---

## Work Completed

### Terminal/CLI Tools Researched

| Tool | Native Location | Notes |
|------|-----------------|-------|
| Claude Code | `.claude/` + `CLAUDE.md` | Folder + file, hierarchy from ~/.claude/ |
| OpenAI Codex CLI | `~/.codex/config.toml` | Global only (TOML), no project folder |
| Aider | `.aider.conf.yml` | YAML file at repo root |

### IDE Extensions Researched

| Tool | Native Location | Notes |
|------|-----------------|-------|
| GitHub Copilot | `.github/copilot-instructions.md` | Also `.github/instructions/*.instructions.md` |
| Cursor | `.cursor/rules/*.mdc` | MDC format with YAML frontmatter |
| Continue | `.continuerc.json` | Workspace partial config (JSON) |
| Gemini Code Assist | IDE settings | No project file (manual config) |

---

## Files Modified

- `outputs/01_understanding_in_progress/by_topic/layer_stage_instantiation_understanding.md`
  - Added "Terminal/CLI Tools" section with Claude Code, Codex CLI, Aider
  - Added "IDE Extensions" section with Copilot, Cursor, Continue, Gemini
  - Added "Supported Tools Reference" table with native locations
  - Updated build process diagram to show correct native output locations
  - Added sources for each tool's documentation

---

## Key Decisions

1. **Codex CLI is global-only**: No project-level config file; uses `~/.codex/config.toml`
2. **Gemini has no project file**: Configuration is in IDE settings, so we output `GEMINI.md` as reference only
3. **Three merge folders removed**: `.1codex_merge/`, `.1gemini_merge/` output to non-folder locations

---

## Next Steps (Potential)

1. Implement `agnostic-merge.sh` script
2. Apply architecture to actual folder structures
3. Create sync-config.yaml templates for each tool

---

## Sources

- Claude Code: https://code.claude.com/docs/en/settings
- OpenAI Codex CLI: https://developers.openai.com/codex/config-basic/
- Aider: https://aider.chat/docs/config/aider_conf.html
- GitHub Copilot: https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
- Cursor: https://docs.cursor.com/context/rules
- Continue: https://docs.continue.dev/reference
- Gemini: https://developers.google.com/gemini-code-assist/docs/overview
