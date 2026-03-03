# Rule: Auto-Trigger Pointer Sync

**Scope**: Triggered when structural changes are detected
**Type**: Dynamic (scenario-triggered)

## When This Rule Applies

- After renaming or moving directories that contain pointer targets
- After `git mv` operations that affect the layer-stage hierarchy
- After any file reorganization that changes directory paths
- When `pointer-sync.sh --validate` reports BROKEN or STALE pointers

## Rule

1. **MUST** run `pointer-sync.sh` (full sync) when structural changes affect pointer targets
2. **MUST** verify all pointers resolve after the sync completes
3. **SHOULD** commit updated pointer files immediately after sync
4. **MUST NOT** leave broken pointers unresolved across commits
5. **SHOULD** review the sync summary to confirm expected changes

## Trigger Mechanisms

| Mechanism | Coverage | How |
|-----------|----------|-----|
| Claude Code hook | AI agent file edits | PostToolUse fires after Edit/Write |
| agnostic-sync integration | Every sync run | Validation at end of agnostic-sync.sh |
| Manual | Developer-initiated | `pointer-sync.sh --verbose` |
| Git hook (future) | Post-commit/post-checkout | Detects path changes in diff |
