---
resource_id: "d8010749-14a6-489e-a64a-4911d3aebbe4"
resource_type: "rule"
resource_name: "pointer_file_convention"
---
# Rule: Pointer File Convention (Entity-Level)

**Scope**: All files within `layer_3_subx3_feature_trigger_pointer_system`
**Type**: Static (always applies)

<!-- section_id: "0dd5f144-79d7-425a-93be-4bcf01d838b5" -->
## Rule

When creating or editing pointer files within this entity:

1. **MUST** use YAML frontmatter with at minimum: `pointer_to:` (human-readable ID), `canonical_entity:` (entity directory name)
2. **MUST** include a body line: `> **Canonical location**: \`relative/path/to/target\``
3. **MUST** use entity-name-based resolution — never hardcode absolute paths
4. **SHOULD** include `canonical_stage:` and `canonical_subpath:` when pointing to content within a specific stage
5. **MUST** run `pointer-sync.sh --validate` after creating or editing pointer files
6. **MUST NOT** duplicate canonical content — pointer files reference, they don't copy

<!-- section_id: "32723588-d22a-4fcf-9e81-a5c3c51072be" -->
## Applies To

- Stage output pointer files (stage_3_04, stage_3_06, stage_3_10)
- Any new pointer files created within this entity's directories

<!-- section_id: "92fdcee2-c38f-40e7-96e9-a0717b3f4274" -->
## References

- Root pointer sync rule: `../../../../../../../../../../../../../../.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md`
- Pointer sync protocol: `../../../../../../../../../../../../../../.0agnostic/03_protocols/pointer_sync_protocol/pointer_sync_protocol.md`
