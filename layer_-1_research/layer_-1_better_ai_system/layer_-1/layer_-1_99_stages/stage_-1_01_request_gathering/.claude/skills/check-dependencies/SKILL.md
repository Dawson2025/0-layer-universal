# Skill: Check Dependencies

Verify and visualize dependencies between needs in the Tree of Needs.

## Trigger
- `/check-dependencies`
- When asked about need relationships
- When planning implementation order

## Actions

### 1. Read Dependency Map
Read `outputs/requests/tree_of_needs/_meta/DEPENDENCIES.md`.

### 2. Parse Dependencies
Extract:
- Cross-branch dependencies (which branches depend on which)
- Intra-branch dependencies (needs within same branch)
- Implementation priority order

### 3. Validate Dependencies
For each dependency, verify:
- [ ] Both needs exist
- [ ] No circular dependencies
- [ ] Dependencies are documented in both directions

### 4. Check for Issues
Look for:
- Missing dependencies (need references something not documented)
- Orphan needs (no dependencies in or out)
- Circular dependencies
- Unclear priority

### 5. Output Dependency Report

```
## Dependency Check Report

### Cross-Branch Dependencies

```
01_capable ──────────────────┐
     │                       │
     ├──→ 02_continuous      │
     ├──→ 03_trustworthy     │
     └──→ 04_observable ─────┘
                 │
                 └──→ (supports all)
```

### Implementation Priority

| Phase | Needs | Reason |
|-------|-------|--------|
| 1 | persistent_knowledge, discoverable | Foundation |
| 2 | scalable_context | Depends on Phase 1 |
| 3 | tool_portable, session_resilient | Depends on Phase 1 |
| ... | ... | ... |

### Issues Found

| Issue | Severity | Location |
|-------|----------|----------|
| [issue] | [high/medium/low] | [need] |

### Recommendations

- [Any suggestions for improving dependency structure]
```

## Dependency Rules

1. **01_capable is foundational** - Other branches depend on it
2. **04_observable supports all** - Can be implemented last
3. **No circular dependencies** - Graph must be acyclic
4. **Dependencies should be minimal** - Prefer loose coupling

## Files to Read
- `outputs/requests/tree_of_needs/_meta/DEPENDENCIES.md`
- All `requirements.md` files for cross-references

## Output
Dependency validation report with any issues and implementation guidance.
