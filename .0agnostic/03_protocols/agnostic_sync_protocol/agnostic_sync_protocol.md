---
resource_id: "6f6e9099-eaaa-4e27-9017-e0350e6da107"
resource_type: "protocol"
resource_name: "agnostic_sync_protocol"
---
# Agnostic Sync Protocol

<!-- section_id: "f6a7b8c9-d0e1-4234-5f01-234567890123" -->
## Purpose

Transform `0AGNOSTIC.md` (the tool-agnostic source of truth) into tool-specific context files. The sync ensures every AI tool gets the context it needs in its native format.

<!-- section_id: "a7b8c9d0-e1f2-4345-6012-345678901234" -->
## When to Use

- After editing any `0AGNOSTIC.md` file
- After creating a new entity (to generate its CLAUDE.md, AGENTS.md, etc.)
- After modifying `.1merge/` override files
- When tool-specific files are out of sync with their source

<!-- section_id: "b8c9d0e1-f2a3-4456-7123-456789012345" -->
## Tools

| Tool | resource_id | Purpose |
|------|-------------|---------|
| `agnostic-sync.sh` | `781698fa-f580-4606-80e4-dc73fb30e3f7` | Main sync script — transforms 0AGNOSTIC.md into CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, copilot-instructions.md |
| `agnostic-diagram-generator.sh` | `44f8f145-6ab5-44c0-8538-887e7c652052` | Generates Mermaid diagrams of the layer-stage hierarchy |
| `user-level-sync.sh` | `5e3e7995-23d1-42e6-9a11-de1515e6367f` | Syncs universal `.0agnostic/` content to `~/.0agnostic/` |

All tools are in `tools/` relative to this protocol document.

<!-- section_id: "c9d0e1f2-a3b4-4567-8234-567890123456" -->
## Workflow

### Standard Sync (after editing 0AGNOSTIC.md)

```bash
# From any directory within the repo:
.0agnostic/03_protocols/agnostic_sync_protocol/tools/agnostic-sync.sh [directory]

# If no directory specified, uses current directory
# Cascades to all child directories with 0AGNOSTIC.md
```

### Generated Files

| File | Tool | Content |
|------|------|---------|
| `CLAUDE.md` | Claude Code | Full static content |
| `AGENTS.md` | AutoGen / Codex | Full static content |
| `GEMINI.md` | Google Gemini | Full static content |
| `OPENAI.md` | OpenAI | Full static content |
| `.cursorrules` | Cursor IDE | Lean: Identity + Navigation |
| `.github/copilot-instructions.md` | GitHub Copilot | Medium detail |

### Three-Tier Merge (.1merge/)

If `.1merge/` exists, the sync applies overrides:
1. **Synced** (base) — content from 0AGNOSTIC.md
2. **Overrides** — `.1merge/.1{tool}_merge/1_overrides/tool_boilerplate.md` replaces default boilerplate
3. **Additions** — `.1merge/.1{tool}_merge/2_additions/tool_additions.md` appended after synced content

### User-Level Sync

```bash
# Sync universal .0agnostic/ to ~/.0agnostic/
.0agnostic/03_protocols/agnostic_sync_protocol/tools/user-level-sync.sh
```

<!-- section_id: "d0e1f2a3-b4c5-4678-9345-678901234567" -->
## Integration

- **agnostic-sync.sh** calls **pointer-sync.sh --validate** at the end of every run
- **Pre-commit hook** warns if CLAUDE.md is staged without 0AGNOSTIC.md
- **Propagation chain**: Edit 0AGNOSTIC.md → run agnostic-sync.sh → commit both source and generated files

---

*This protocol handles the 0AGNOSTIC.md → tool files transformation. For pointer file maintenance, see pointer_sync_protocol. For UUID assignment, see uuid_assignment_protocol.*
