---
resource_id: "3e2fc187-04d9-4ff0-8ef1-3a2cefcd2bb6"
resource_type: "output"
resource_name: "REQ-01_hook_triggers"
---
# REQ-01: Claude Code Hook Triggers

**Need**: [Trigger Automation](../README.md)

<!-- section_id: "f316ec35-3aca-4dc8-b819-0264187f9900" -->
## Requirements

- **MUST** notify the AI agent when pointer files are modified, prompting validation
- **MUST** detect whether the edited file contains pointer YAML frontmatter (`pointer_to:`)
- **MUST** be non-blocking — normal file operations continue regardless of notification outcome
- **MUST** automatically validate pointers after context file generation (agnostic-sync)
- **SHOULD** support automatic full pointer sync (not just validate) after structural changes
- **MUST NOT** break if validation tools are unavailable
- **MUST** timeout gracefully (max 10 seconds for any automated check)

> **Design note**: The specific hook mechanism (e.g., PostToolUse, PreToolUse, filesystem watcher) and tool-specific integration details are documented in stage 04 design outputs.
