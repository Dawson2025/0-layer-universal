# Protocol: Entity Chain Setup

**Purpose**: Correctly integrate a new entity into the 0AGNOSTIC parent chain so it inherits context from all ancestors.

---

## When to Use

- Creating a new feature, sub-feature, or component entity
- Adding a container (group, registry) that other entities will reference as parent
- Restructuring the hierarchy by inserting a new level

## Prerequisites

- Know the parent entity's `0AGNOSTIC.md` path
- Know the new entity's role and scope
- Have `agnostic-sync.sh` available

## Steps

### Step 1: Create the Entity Directory

```bash
mkdir -p [new-entity-dir]/.0agnostic/{rules,knowledge,skills,episodic_memory/{sessions,changes},hooks/scripts,agents}
mkdir -p [new-entity-dir]/.claude/{rules,skills}
mkdir -p [new-entity-dir]/.1merge
```

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

### Step 3: Verify Parent Reference

```bash
cd [new-entity-dir]
parent_dir=$(dirname [relative-parent-path])
test -f "$parent_dir/0AGNOSTIC.md" && echo "Parent exists" || echo "ERROR: Parent missing"
```

### Step 4: Run agnostic-sync

```bash
bash layer_0/.0agnostic/agnostic-sync.sh [new-entity-dir]
```

This generates `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md`.

### Step 5: Validate the Chain

Run chain validation from the new entity to root:

```bash
./tests/test_context_chain_traversal.sh
```

Expect: all levels PASS, chain terminates at root.

### Step 6: Update Parent's Children List

Edit the parent's `0AGNOSTIC.md` to include the new entity in its Children line, then re-sync the parent.

### Step 7: Audit Avenue Coverage

Run the Avenue Audit Protocol on the new entity. Target: 5+ avenues PASS at creation.

## Verification Checklist

- [ ] `0AGNOSTIC.md` has `## Identity` with Role, Scope, Parent
- [ ] Parent path resolves to an existing `0AGNOSTIC.md`
- [ ] `agnostic-sync.sh` ran successfully (CLAUDE.md generated)
- [ ] Chain validation passes (no breaks)
- [ ] Parent's Children list updated
- [ ] Avenue coverage: 5+ PASS
