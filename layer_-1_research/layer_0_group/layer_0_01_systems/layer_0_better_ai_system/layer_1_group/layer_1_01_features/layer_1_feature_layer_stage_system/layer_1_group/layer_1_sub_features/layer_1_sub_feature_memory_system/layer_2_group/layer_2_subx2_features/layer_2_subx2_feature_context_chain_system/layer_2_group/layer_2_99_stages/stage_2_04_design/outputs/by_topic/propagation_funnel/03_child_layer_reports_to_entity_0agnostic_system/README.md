# Level 03: Layer Reports → Entity Reports

**Purpose**: Customize layer context for each child entity, creating entity-specific context and 0AGNOSTIC.md

**Flow**:
```
Layer Report (parent layer)
            ↓
        (For each child entity:)
            ↓
    Customize context for entity
    + Override with entity-specific rules
    + Create entity 0AGNOSTIC.md
            ↓
   Entity Report (02_aggregated_entity_reports/)
            ↓
   Entity 0AGNOSTIC.md (source of truth)
            ↓
   (Ready for Level 04: Entity → AI Apps porting)
```

## Subdirectories

### `01_layer_reports/`
**Content**: Input from parent layer
- `layer_report.md` — Parent layer's synthesis
- `0AGNOSTIC.md` — Parent layer context
- `.0agnostic/` — Parent layer resources
  - Rules (static + dynamic) — inherited by all children
  - Knowledge — inherited by all children
  - Protocols — inherited by all children

### `02_aggregated_entity_reports/`
**Content**: Entity-specific reports derived from layer context
- `[entity_name]_report.md` for each entity
  - How entity inherits from parent layer
  - Entity-specific customizations
  - Overrides to parent rules
  - New entity-specific rules introduced
  - Child entities (if any)
  - Status and readiness

**Example entities**:
- `layer_1_sub_project_classes_report.md`
- `layer_2_subx2_project_computer_science_report.md`
- `layer_3_subx2_project_machine_learning_report.md`
- etc.

### `03_entity_0agnostic/`
**Content**: Entity-specific context definitions
- For each child entity, create:
  - `[entity_name]/0AGNOSTIC.md` — Entity source of truth
  - `[entity_name]/.0agnostic/` — Entity resources
    - `01_knowledge/` — Entity-specific knowledge
    - `02_rules/{static,dynamic}/` — Entity-specific rules
    - `03_protocols/` — Entity-specific protocols
    - `04_episodic_memory/` — Entity memory
    - `05_handoff_documents/` — Entity handoff
    - `06_context_avenue_web/` — Entity context avenues
    - `07+_setup_dependant/` — Entity setup-specific

## Customization Rules

### Inheritance Hierarchy
```
Universal Rules (layer_0)
    ↓
Layer Rules (layer_1, layer_2, etc.)
    ↓
Entity Rules (inherits from all above)
    ↓
Feature Rules (inherits from all above + entity)
```

Each level can:
- **Inherit** all parent rules (default)
- **Override** specific parent rules (child wins)
- **Add** new rules not in parent
- **Disable** parent rules (explicitly exclude)

### Entity-Specific Customizations

**Scope**: What applies uniquely to this entity?
- Name, identity, role
- Direct children (features, sub-projects)
- Specific rules that apply only here
- Specific knowledge domain
- Specific protocols

**Inheritance**: What comes from parent?
- Universal grading strategies (if class)
- Canvas integration patterns (if school)
- Coordination protocols (if project)
- Shared skills (if inherited)

**Overrides**: What is different from parent?
- Different grading model (MATH 119 vs CSE 300)
- Different deadlines (course schedule)
- Different assignment categories
- Different tool integrations

## Entity 0AGNOSTIC.md Structure

```markdown
# [Entity Name] — [Entity Role]

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity
- Role, scope
- Parent and children
- Key relationships

## Key Behaviors
- What this entity does
- How it inherits from parent
- How it differs from siblings

## Triggers
- When to load this entity's context
- Triggers specific to this entity

# ── Current Status ──

## Current Status
- What's been done
- What's in progress
- What's needed next

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail
- Detailed current situation
- Open items
- Blockers

# ── References ──

## Navigation
## Resources
## Success Criteria
## On Exit
```

## Workflow

1. **Read** — Review `01_layer_reports/layer_report.md`
2. **For each child entity**:
   a. **Understand** — Entity role, scope, parent-child relationships
   b. **Customize** — What should be different for this entity?
   c. **Create** — Entity `0AGNOSTIC.md` (source of truth)
   d. **Create** — Entity `.0agnostic/` structure
   e. **Report** — Document customization in entity_report.md
3. **Validate** — Check all entities have proper context
4. **Output** — Place reports in `02_aggregated_entity_reports/`
5. **Ready** — Entities ready for Level 04 (AI app porting)

## Integration

**Input From**: Level 02 (layer_report.md and 0AGNOSTIC.md)
**Output To**: Level 04 (entity_context → ai_apps porting)
**Cross-ref**: Each entity's `.0agnostic/`, parent layer's rules, sibling entities

---

**Status**: Directory structure created, documentation in progress
**Next**: Create entity 0AGNOSTIC.md files and entity reports
