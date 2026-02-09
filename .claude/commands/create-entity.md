Create a new entity (project, feature, or component) in the layer hierarchy.

Arguments:
- type: project | feature | component
- name: Entity name (will be converted to snake_case)
- parent: Parent layer path (optional, defaults to current)

Steps:
1. Read `@imports/entity_structure.md` for canonical directory structure
2. Determine entity type and layer level (children are parent layer + 1)
3. Generate next available XX number
4. Create full directory structure per `@imports/entity_structure.md`
5. Create `0AGNOSTIC.md` and `0INDEX.md` (see INSTANTIATION_GUIDE.md for templates)
6. Run `agnostic-sync.sh` to generate CLAUDE.md and other tool files
7. Update parent's 0INDEX.md to include new entity

Reference: Use `/entity-creation` skill for detailed protocol.
