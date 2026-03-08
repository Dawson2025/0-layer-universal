---
resource_id: "0be2b70d-2734-4ffa-bafa-46dd3cbeefe2"
resource_type: "skill_document"
resource_name: "SKILL"
---
# Skill: Chain Validate

<!-- section_id: "c4dda4c4-b387-4428-aecd-9bf02c7e74f5" -->
## Purpose

Validate the 0AGNOSTIC.md parent chain from any entity to the research root, reporting chain depth, each link, and any broken references.

<!-- section_id: "c147e398-29ab-4b41-be93-3df8dcc17e51" -->
## When to Use

- Before modifying parent references in any 0AGNOSTIC.md
- After creating new entities to confirm they are linked into the chain
- During testing or auditing the context chain system
- When a test reports a broken parent link

<!-- section_id: "81e7992c-ca39-498d-84e0-78e9b80b7f0a" -->
## When NOT to Use

- For checking avenue coverage across all 8 avenues (use `/avenue-check` instead)
- For general context gathering (use `/context-gathering` instead)
- For creating new entities (use `/entity-creation` instead)

<!-- section_id: "358ecafc-1df7-4aba-9da5-c7386193277d" -->
## Protocol

<!-- section_id: "0b17e06d-8f38-415b-a9ef-2eae96e27b27" -->
### 1. Start at Current Entity

Read the 0AGNOSTIC.md in the current working directory (or specified target directory).

- If 0AGNOSTIC.md does not exist: **FAIL** — report missing file and stop

<!-- section_id: "cb34c1bc-b3e9-43cf-840e-f773d4581087" -->
### 2. Extract Parent Path

Look for the `## Parent` section. Extract the path value.

- If no Parent section exists: this is a **root node** — chain is complete
- If Parent section exists but path is empty: **FAIL** — broken reference

<!-- section_id: "96a9bcbe-e486-4622-a96c-28d35a00c35b" -->
### 3. Resolve Relative Path

Resolve the parent path relative to the current 0AGNOSTIC.md location.

- If the resolved path does not exist on disk: **FAIL** — broken link

<!-- section_id: "da69d2d2-3b77-445f-8b8d-b6010a3ec10b" -->
### 4. Verify Parent Has Identity

Read the parent 0AGNOSTIC.md. Confirm it has an `## Identity` section.

- If no Identity section: **WARNING** — parent exists but is malformed

<!-- section_id: "6a1ef706-1c6c-41ac-902a-9cdce03b2bbe" -->
### 5. Recurse

Set current directory to the parent and repeat from Step 2. Continue until a root node is reached (no Parent section).

<!-- section_id: "8b3bab21-d8ba-45aa-9450-dc827cbd757f" -->
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

<!-- section_id: "af3854c1-c78c-47b4-8cd2-a869a0c4fb18" -->
## Checklist

- [ ] Started from correct directory
- [ ] Every link checked for file existence
- [ ] Every parent checked for Identity section
- [ ] Chain terminates at a root node (not a broken link)
- [ ] Report generated with per-link status
