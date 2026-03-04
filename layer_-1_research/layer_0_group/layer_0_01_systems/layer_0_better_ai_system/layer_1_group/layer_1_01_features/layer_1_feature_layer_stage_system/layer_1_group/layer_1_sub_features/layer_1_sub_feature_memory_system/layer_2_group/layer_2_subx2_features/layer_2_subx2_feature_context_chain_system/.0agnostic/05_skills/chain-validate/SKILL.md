# Skill: Chain Validate

## Purpose

Validate the 0AGNOSTIC.md parent chain from any entity to the research root, reporting chain depth, each link, and any broken references.

## When to Use

- Before modifying parent references in any 0AGNOSTIC.md
- After creating new entities to confirm they are linked into the chain
- During testing or auditing the context chain system
- When a test reports a broken parent link

## When NOT to Use

- For checking avenue coverage across all 8 avenues (use `/avenue-check` instead)
- For general context gathering (use `/context-gathering` instead)
- For creating new entities (use `/entity-creation` instead)

## Protocol

### 1. Start at Current Entity

Read the 0AGNOSTIC.md in the current working directory (or specified target directory).

- If 0AGNOSTIC.md does not exist: **FAIL** — report missing file and stop

### 2. Extract Parent Path

Look for the `## Parent` section. Extract the path value.

- If no Parent section exists: this is a **root node** — chain is complete
- If Parent section exists but path is empty: **FAIL** — broken reference

### 3. Resolve Relative Path

Resolve the parent path relative to the current 0AGNOSTIC.md location.

- If the resolved path does not exist on disk: **FAIL** — broken link

### 4. Verify Parent Has Identity

Read the parent 0AGNOSTIC.md. Confirm it has an `## Identity` section.

- If no Identity section: **WARNING** — parent exists but is malformed

### 5. Recurse

Set current directory to the parent and repeat from Step 2. Continue until a root node is reached (no Parent section).

### 6. Report Results

Output a summary in this format:

```
Chain Validation Report
=======================
Start:  layer_2_subx2_feature_context_chain_system
Depth:  7 levels

  [PASS] context_chain_system → memory_system
  [PASS] memory_system → layer_stage_system
  [PASS] layer_stage_system → layer_0_features
  [PASS] layer_0_features → layer_0_group
  [PASS] layer_0_group → better_ai_system
  [PASS] better_ai_system → layer_-1_research
  [ROOT] layer_-1_research (no parent — chain complete)

Result: ALL LINKS VALID (7 levels, 0 broken)
```

If any link fails:

```
  [FAIL] memory_system → layer_stage_system
         Expected: ../../../0AGNOSTIC.md
         Error: File does not exist
```

## Checklist

- [ ] Started from correct directory
- [ ] Every link checked for file existence
- [ ] Every parent checked for Identity section
- [ ] Chain terminates at a root node (not a broken link)
- [ ] Report generated with per-link status
