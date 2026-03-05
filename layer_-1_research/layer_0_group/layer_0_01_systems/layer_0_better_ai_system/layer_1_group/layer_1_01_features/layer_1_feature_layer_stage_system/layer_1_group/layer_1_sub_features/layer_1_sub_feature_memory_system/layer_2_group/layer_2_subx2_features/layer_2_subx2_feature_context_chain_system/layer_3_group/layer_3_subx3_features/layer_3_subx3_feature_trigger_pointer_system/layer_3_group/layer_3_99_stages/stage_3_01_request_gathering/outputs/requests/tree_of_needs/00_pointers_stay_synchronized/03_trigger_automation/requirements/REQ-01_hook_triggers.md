---
resource_id: "3e2fc187-04d9-4ff0-8ef1-3a2cefcd2bb6"
resource_type: "output"
resource_name: "REQ-01_hook_triggers"
---
# REQ-01: Claude Code Hook Triggers

**Need**: [Trigger Automation](../README.md)

<!-- section_id: "f316ec35-3aca-4dc8-b819-0264187f9900" -->
## Requirements

- **MUST** fire a PostToolUse hook after Edit/Write operations on `.md` files
- **MUST** detect whether the edited file contains pointer YAML frontmatter (`pointer_to:`)
- **MUST** remind the AI agent that pointer validation is needed (non-blocking)
- **MUST** automatically run `pointer-sync.sh --validate` after `agnostic-sync.sh`
- **SHOULD** support a hook that auto-runs `pointer-sync.sh` (full sync, not just validate) after structural changes
- **MUST NOT** block normal file operations if pointer-sync.sh is unavailable
- **MUST** timeout gracefully (max 10 seconds for hook execution)
