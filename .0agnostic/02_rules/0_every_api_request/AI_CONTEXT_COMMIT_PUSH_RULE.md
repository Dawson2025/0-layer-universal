---
resource_id: "ce94177e-c9ee-4344-8cf0-634c1278d486"
resource_type: "rule"
resource_name: "AI_CONTEXT_COMMIT_PUSH_RULE"
---
# AI Context Commit and Push Rule

<!-- section_id: "2f9658d0-0e2a-4e61-b8a0-907c323f1907" -->
## Rule

After any approved changes are made to the AI context system, the AI MUST:

1. **Stage the changed files** with `git add`
2. **Commit** with a descriptive message
3. **Push** to the remote repository

<!-- section_id: "43f43b1a-5c78-421b-9507-1a0e24cc6e2d" -->
## Scope

This rule applies to all modifications within:

| Path Pattern | Description |
|--------------|-------------|
| `0_layer_universal/` | Entire AI context system |
| `layer_*/` | All layer directories |
| `sub_layer_*/` | All sublayer directories |
| `stage_*/` | All stage directories |
| `CLAUDE.md` | Claude context files |
| `status.json` | Status tracking files |

<!-- section_id: "69b4db74-da3a-4ff0-9cb5-6ad0bc39949b" -->
## Commit Message Format

```
[AI Context] <brief description>

- File 1: <change type>
- File 2: <change type>
...

Co-Authored-By: Claude <noreply@anthropic.com>
```

<!-- section_id: "3c220eca-193c-442f-a9eb-9d9c70ff5b04" -->
## Rationale

- **Preservation**: Changes are saved and not lost
- **Sync**: Enables synchronization across devices (Windows/Linux dual boot)
- **History**: Creates version history of AI context evolution
- **Collaboration**: Changes are visible to user on all devices

<!-- section_id: "d05f1077-273d-41df-83bc-85eab12c5bc4" -->
## Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   User      │     │   AI Shows  │     │   User      │     │  AI Commits │
│   Request   │ ──▶ │   Diagram   │ ──▶ │   Approves  │ ──▶ │  and Pushes │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

<!-- section_id: "79b15953-7648-434d-92c2-33ff476ed387" -->
## Date Added
2026-01-26

<!-- section_id: "8e0d9cd1-0f7c-4485-87b5-c69523d71db9" -->
## Related Rules
- AI_CONTEXT_MODIFICATION_PROTOCOL.md - Show diagram before modifying
