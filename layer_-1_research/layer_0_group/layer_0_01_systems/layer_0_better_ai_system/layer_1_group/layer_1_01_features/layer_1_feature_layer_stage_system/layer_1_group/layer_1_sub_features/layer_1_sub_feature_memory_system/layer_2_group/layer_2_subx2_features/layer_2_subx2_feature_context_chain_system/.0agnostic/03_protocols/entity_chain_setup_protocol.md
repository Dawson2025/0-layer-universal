---
resource_id: "b95c084b-8964-4339-a345-6bfbfe278df6"
resource_type: "protocol"
resource_name: "entity_chain_setup_protocol"
---
# Protocol: Entity Chain Setup

**Purpose**: Correctly integrate a new entity into the 0AGNOSTIC parent chain so it inherits context from all ancestors.

---

<!-- section_id: "ec60f5ea-22b7-47e6-84ed-44f13a698996" -->
## When to Use

- Creating a new feature, sub-feature, or component entity
- Adding a container (group, registry) that other entities will reference as parent
- Restructuring the hierarchy by inserting a new level

<!-- section_id: "dab4aa21-7087-48f1-b8dc-c427865f5e69" -->
## Prerequisites

- Know the parent entity's `0AGNOSTIC.md` path
- Know the new entity's role and scope
- Have `agnostic-sync.sh` available

<!-- section_id: "833a2c76-05b5-4c07-ba14-9de4f9bfb3cd" -->
## Steps

<!-- section_id: "25ab9271-b423-489d-8379-1f3654ea50a8" -->
### Step 1: Create the Entity Directory

```bash
mkdir -p [new-entity-dir]/.0agnostic/{rules,knowledge,skills,episodic_memory/{sessions,changes},hooks/scripts,agents}
mkdir -p [new-entity-dir]/.claude/{rules,skills}
mkdir -p [new-entity-dir]/.1merge
```

<!-- section_id: "22bc828f-ea15-4fd0-ba13-5812f80d13a9" -->
### Step 2: Create 0AGNOSTIC.md

Write the minimum viable source of truth:

```markdown
## Identity

**Role**: [Entity name] — [one-line description]
**Scope**: [What this entity covers]
**Parent**: [relative-path-to-parent/0AGNOSTIC.md]
**Children**: [list child entities, or "None yet"]

## Navigation

- **Detailed resources**: `.0agnostic/` folder
- **Rules**: `.0agnostic/rules/`
- **Knowledge**: `.0agnostic/knowledge/`

## Triggers

Load this context when:
- User mentions: [relevant keywords]
- Working on: [relevant tasks]
- Entering: `[directory-name]/`
```

<!-- section_id: "c52ac011-4101-4186-8220-456d7d511846" -->
### Step 3: Verify Parent Reference

```bash
cd [new-entity-dir]
parent_dir=$(dirname [relative-parent-path])
test -f "$parent_dir/0AGNOSTIC.md" && echo "Parent exists" || echo "ERROR: Parent missing"
```

<!-- section_id: "01f8ffa6-d6f3-467d-8333-224d074f9053" -->
### Step 4: Run agnostic-sync

```bash
bash .0agnostic/agnostic-sync.sh [new-entity-dir]
```

This generates `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md`.

<!-- section_id: "60301ea2-9397-4877-a6f3-7e44606461b6" -->
### Step 5: Validate the Chain

Run chain validation from the new entity to root:

```bash
./tests/test_context_chain_traversal.sh
```

Expect: all levels PASS, chain terminates at root.

<!-- section_id: "b6eb6694-6150-4492-b8d7-794d2ee63526" -->
### Step 6: Update Parent's Children List

Edit the parent's `0AGNOSTIC.md` to include the new entity in its Children line, then re-sync the parent.

<!-- section_id: "39d2bd3f-d442-41b4-abda-d28bfa1f3ea8" -->
### Step 7: Audit Avenue Coverage

Run the Avenue Audit Protocol on the new entity. Target: 5+ avenues PASS at creation.

<!-- section_id: "54244e46-319a-408a-ba57-a03faf7aa968" -->
## Verification Checklist

- [ ] `0AGNOSTIC.md` has `## Identity` with Role, Scope, Parent
- [ ] Parent path resolves to an existing `0AGNOSTIC.md`
- [ ] `agnostic-sync.sh` ran successfully (CLAUDE.md generated)
- [ ] Chain validation passes (no breaks)
- [ ] Parent's Children list updated
- [ ] Avenue coverage: 5+ PASS
