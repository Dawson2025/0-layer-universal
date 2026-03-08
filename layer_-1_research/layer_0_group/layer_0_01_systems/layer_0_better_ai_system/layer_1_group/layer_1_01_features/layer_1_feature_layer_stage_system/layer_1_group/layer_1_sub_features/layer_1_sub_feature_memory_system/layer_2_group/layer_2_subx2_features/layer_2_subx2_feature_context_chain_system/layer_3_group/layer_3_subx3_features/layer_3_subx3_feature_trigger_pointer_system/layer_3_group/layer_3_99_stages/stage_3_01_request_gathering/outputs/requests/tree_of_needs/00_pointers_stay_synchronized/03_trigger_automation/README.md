---
resource_id: "3b35f6cf-f9e0-44c6-843a-1bbedde770fd"
resource_type: "readme_output"
resource_name: "README"
---
# Branch 03: Trigger Automation

**Core Question**: How does the system detect changes and run automatically?

<!-- section_id: "fdcd6229-4989-4b1f-99fe-30997554fed2" -->
## Description

The pointer system must not require manual invocation. This branch defines the trigger mechanisms: Claude Code hooks that fire after file edits, git hooks that fire after commits/moves, and filesystem watchers that detect structural changes. The goal is zero-intervention pointer maintenance.

<!-- section_id: "6bafcf48-f1d5-4749-91f1-a9df21da1895" -->
## Child Needs

| Need | Question | Description |
|------|----------|-------------|
| need_01_hook_triggers | How do editing tools trigger sync? | Automated notifications detect pointer edits, remind agents, fire validation |
| need_02_git_integration | How do git operations trigger sync? | Post-commit/post-checkout hooks detect renames and moves |
| need_03_change_detection | How do we detect what actually changed? | Diff analysis to identify affected pointers vs full rescan |

<!-- section_id: "b9892a30-c02a-4d86-844d-7d1e80f0e947" -->
## Key Insight

The trigger layer is what transforms pointer-sync from a **manual tool** into an **automated system**. Without triggers, pointers are only as fresh as the last manual run. With triggers, pointers stay fresh continuously — the developer never needs to think about them.
