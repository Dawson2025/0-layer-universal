---
resource_id: "d1b7c122-84db-4e05-a262-0600c03ea2d7"
resource_type: "readme_knowledge"
resource_name: "README"
---
# Current Product - System Management

**Purpose:** The current deliverables of system management work.

**Last Updated:** 2026-01-15

---

<!-- section_id: "2e13bf48-9341-44bd-8c61-86c6b9618c92" -->
## Contents

```
stage_0_08_current_product/
├── README.md                 ← You are here
├── changes/                  # Change protocols
│   ├── README.md
│   ├── restructuring_migration_protocol.md
│   ├── traversal_update_protocol.md
│   └── verify_paths.sh
├── setup/                    # Entity creation guides
│   ├── README.md
│   ├── instantiation_guide.md
│   ├── project_creation_checklist.md
│   ├── feature_creation_checklist.md
│   └── component_creation_checklist.md
├── hand_off_documents/       # Stage handoffs
└── ai_agent_system/          # Agent configs
```

---

<!-- section_id: "007fb9eb-5dac-4f71-b5c0-2e825b8811e3" -->
## Quick Reference

<!-- section_id: "55f3e990-8fb3-4266-8d6f-ea435f2f8d1f" -->
### Change Protocols

| Document | Purpose |
|----------|---------|
| `changes/restructuring_migration_protocol.md` | How to restructure projects and migrate content |
| `changes/traversal_update_protocol.md` | How to update navigation docs after changes |
| `changes/verify_paths.sh` | Script to verify critical paths exist |

<!-- section_id: "7e1cfa2b-08a9-496f-b5eb-76bdbf46fa54" -->
### Setup Guides

| Document | Purpose |
|----------|---------|
| `setup/instantiation_guide.md` | Comprehensive guide for all entity types |
| `setup/project_creation_checklist.md` | Step-by-step project creation |
| `setup/feature_creation_checklist.md` | Step-by-step feature creation |
| `setup/component_creation_checklist.md` | Step-by-step component creation |

---

<!-- section_id: "2dc8b3c9-0702-4547-a0dd-289efde19b78" -->
## When to Archive

Move content to `../stage_0_09_archives/` when:
- Creating a major new version of a protocol
- Deprecating a guide in favor of a new approach
- Significant restructuring of the system

Archive format: `../stage_0_09_archives/v<version>_<date>/`

---

<!-- section_id: "b5872b6f-9827-4b20-ba54-27729da384cc" -->
## Related Stages

| Stage | Purpose |
|-------|---------|
| `stage_0_02_planning/` | Planning docs (MCP_DOCUMENTATION_PLAN.md) |
| `stage_0_09_archives/` | Historical versions |
