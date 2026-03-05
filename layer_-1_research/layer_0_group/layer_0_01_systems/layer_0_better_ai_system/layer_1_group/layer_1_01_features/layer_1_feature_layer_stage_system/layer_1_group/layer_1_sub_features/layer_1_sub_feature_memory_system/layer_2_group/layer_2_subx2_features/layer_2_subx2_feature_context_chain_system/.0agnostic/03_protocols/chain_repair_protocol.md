---
resource_id: "2b0181ed-0333-4e4b-8a9e-553621bc1644"
resource_type: "protocol"
resource_name: "chain_repair_protocol"
---
# Protocol: Chain Repair

**Purpose**: Restore a broken 0AGNOSTIC parent chain to working state.

---

## When to Use

- Chain validation reports a FAIL at any level
- An agent reports it cannot find parent context
- A directory was renamed or moved without updating references
- A `0AGNOSTIC.md` was accidentally deleted

## Diagnosis

### Step 1: Run Chain Validation

```bash
./tests/test_context_chain_traversal.sh
```

Look for: `FAIL: Parent path does not exist: [path]`

### Step 2: Identify the Break Type

| Symptom | Break Type | Severity |
|---------|-----------|----------|
| "Parent path does not exist" | Missing node | CRITICAL |
| "No Identity section found" | Incomplete node | HIGH |
| "No Parent line found" (non-root) | Missing reference | HIGH |
| Chain depth unexpectedly short | Premature termination | MEDIUM |

### Step 3: Locate the Break Point

The test output shows the last successful level and the first failed level. The break is between them.

## Repair Procedures

### Missing Node (0AGNOSTIC.md doesn't exist)

1. Create the directory if it doesn't exist
2. Create a minimum viable `0AGNOSTIC.md`:

```markdown
## Identity

**Role**: [Infer from directory name]
**Scope**: [Container/entity for child entities]
**Parent**: [path to the next level up's 0AGNOSTIC.md]
```

3. Run `agnostic-sync.sh` on the directory
4. Re-validate the chain

### Incomplete Node (exists but missing Identity)

1. Open the `0AGNOSTIC.md`
2. Add the `## Identity` section with Role, Scope, Parent
3. Run `agnostic-sync.sh`
4. Re-validate

### Missing Parent Reference

1. Open the `0AGNOSTIC.md` at the break point
2. Add or fix the `**Parent**:` line
3. Verify the parent path resolves:
   ```bash
   cd [entity-dir] && ls [relative-parent-path]
   ```
4. Run `agnostic-sync.sh`
5. Re-validate

### Stale Reference (directory was renamed)

1. Find all `0AGNOSTIC.md` files that reference the old path:
   ```bash
   grep -r "old-directory-name" --include="0AGNOSTIC.md"
   ```
2. Update each reference to the new path
3. Run `agnostic-sync.sh` on each modified directory
4. Re-validate the full chain

## Post-Repair Verification

After any repair:

1. **Chain validation**: Must show 0 breaks
2. **Avenue audit**: Run to ensure other avenues weren't affected
3. **Commit**: Stage repaired files and commit with `[AI Context] repair chain break at [node]`

## Prevention

- Always run chain validation before and after structural changes
- Follow the `validate_before_modify` dynamic rule
- Keep container nodes even if they seem "empty" — they may be chain links
