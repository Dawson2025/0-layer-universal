---
resource_id: "d216a87c-58dd-4dfa-8f92-aa0b20988846"
resource_type: "protocol"
resource_name: "chain_validation_protocol"
---
# Protocol: Chain Validation

**Purpose**: Verify that the full 0AGNOSTIC parent chain is intact from a given entity to the root.

---

<!-- section_id: "e1dc18d1-e874-4d18-acac-4f80cfe0c859" -->
## When to Use

- After structural modifications (directory renames, parent reference changes)
- When chain integrity is uncertain
- As part of entity creation verification
- When an agent reports missing parent context

<!-- section_id: "cd86d44c-2452-4d4a-9859-74050f93735b" -->
## Steps

<!-- section_id: "819219b7-36e4-4b47-a691-ea652d7c8310" -->
### Step 1: Identify Starting Entity

Locate the `0AGNOSTIC.md` for the entity you want to validate.

```bash
ls [entity-directory]/0AGNOSTIC.md
```

<!-- section_id: "d88d04f6-ee65-44f1-b15e-fa508f1777ac" -->
### Step 2: Extract Parent Reference

```bash
grep -i "parent" [entity-directory]/0AGNOSTIC.md | head -1
```

The parent line should contain a relative path to the parent's `0AGNOSTIC.md`.

<!-- section_id: "fe26d4ac-5adb-4af8-8a5e-ec26b96d0ce0" -->
### Step 3: Resolve Parent Path

Convert the relative parent reference to an absolute path:

```bash
parent_path=$(cd [entity-directory] && cd [relative-parent-dir] && pwd)
```

<!-- section_id: "1789e4e2-4a5a-4f41-b4a1-10d24f6842ec" -->
### Step 4: Verify Parent Exists

```bash
test -f "$parent_path/0AGNOSTIC.md" && echo "PASS" || echo "FAIL"
```

<!-- section_id: "6f91cd9a-bbb2-4fc1-a20a-f9f0cedcb3df" -->
### Step 5: Verify Parent Has Identity

```bash
grep -q "## Identity" "$parent_path/0AGNOSTIC.md" && echo "PASS" || echo "FAIL"
```

<!-- section_id: "9ab4851e-77bc-46e6-b1d7-81295b58b2b6" -->
### Step 6: Recurse

Repeat Steps 2-5 from the parent's directory until you reach a node with no Parent reference (the root).

<!-- section_id: "9ae02793-3160-4da1-8e40-ef2502af84bb" -->
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

<!-- section_id: "c1031758-c02e-4d1b-9fc9-adb603a186e8" -->
## Success Criteria

- Every parent reference resolves to an existing file
- Every resolved file contains `## Identity`
- The chain terminates at a root node (no Parent line)
- Zero breaks in the chain

<!-- section_id: "a35c4e96-dc9a-4515-b5ff-f5ee3f615cae" -->
## Failure Recovery

If any step fails, follow the Chain Repair Protocol.
