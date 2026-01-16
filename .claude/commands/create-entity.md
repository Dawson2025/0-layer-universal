Create a new entity (project, feature, or component) in the layer hierarchy.

Arguments:
- type: project | feature | component
- name: Entity name (will be converted to snake_case)
- parent: Parent layer path (optional, defaults to current)

Steps:
1. Determine entity type and layer level
2. Generate next available XX number
3. Create directory structure with entity pattern
4. Initialize status file and CLAUDE.md
5. Link to parent entity
