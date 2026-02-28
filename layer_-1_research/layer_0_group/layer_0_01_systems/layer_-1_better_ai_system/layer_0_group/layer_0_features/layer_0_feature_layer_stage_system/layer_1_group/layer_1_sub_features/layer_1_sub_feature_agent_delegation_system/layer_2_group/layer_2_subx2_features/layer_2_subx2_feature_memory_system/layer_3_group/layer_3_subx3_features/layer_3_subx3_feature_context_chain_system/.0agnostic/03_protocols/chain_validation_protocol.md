# Protocol: Chain Validation

**Purpose**: Verify that the full 0AGNOSTIC parent chain is intact from a given entity to the root.

---

## When to Use

- After structural modifications (directory renames, parent reference changes)
- When chain integrity is uncertain
- As part of entity creation verification
- When an agent reports missing parent context

## Steps

### Step 1: Identify Starting Entity

Locate the `0AGNOSTIC.md` for the entity you want to validate.

```bash
ls [entity-directory]/0AGNOSTIC.md
```

### Step 2: Extract Parent Reference

```bash
grep -i "parent" [entity-directory]/0AGNOSTIC.md | head -1
```

The parent line should contain a relative path to the parent's `0AGNOSTIC.md`.

### Step 3: Resolve Parent Path

Convert the relative parent reference to an absolute path:

```bash
parent_path=$(cd [entity-directory] && cd [relative-parent-dir] && pwd)
```

### Step 4: Verify Parent Exists

```bash
test -f "$parent_path/0AGNOSTIC.md" && echo "PASS" || echo "FAIL"
```

### Step 5: Verify Parent Has Identity

```bash
grep -q "## Identity" "$parent_path/0AGNOSTIC.md" && echo "PASS" || echo "FAIL"
```

### Step 6: Recurse

Repeat Steps 2-5 from the parent's directory until you reach a node with no Parent reference (the root).

### Step 7: Report

Report the full chain with pass/fail at each level:

```
Level 0: context_chain_system     → PASS (Identity found)
Level 1: memory_system            → PASS (Identity found)
Level 2: layer_stage_system       → PASS (Identity found)
Level 3: layer_0_features         → PASS (Identity found)
Level 4: layer_0_group            → PASS (Identity found)
Level 5: better_ai_system         → PASS (Identity found)
Level 6: layer_-1_research        → PASS (ROOT, no Parent)
Chain depth: 7 levels, 0 breaks
```

## Success Criteria

- Every parent reference resolves to an existing file
- Every resolved file contains `## Identity`
- The chain terminates at a root node (no Parent line)
- Zero breaks in the chain

## Failure Recovery

If any step fails, follow the Chain Repair Protocol.
