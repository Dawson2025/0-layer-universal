---
resource_id: "cb621cdc-4ed1-46be-9311-78f83cbfd017"
resource_type: "document"
resource_name: "stage_01_research.sync-conflict-20260126-102028-IF2WOGZ"
---
# Stage 01: Research

<!-- section_id: "b7c5dbbf-b8ea-4e99-9f8f-e44bbc7c6b60" -->
## Purpose

Explore the problem space, gather information, and build understanding before defining specific instructions. This stage bridges request gathering and instruction definition by investigating unknowns.

<!-- section_id: "39735b8c-cdaa-4bb5-b460-3933534bb01d" -->
## Entry Criteria

- Stage 00 (Request Gathering) complete
- Initial requirements documented
- Unknown areas or questions identified

<!-- section_id: "77f1b7a3-9252-4c2e-86c6-89c9b006cd14" -->
## Exit Criteria

- Research findings documented in `outputs/`
- Key decisions recorded
- Dependencies and constraints understood
- Ready to write concrete instructions

<!-- section_id: "3d146545-531a-485a-8123-2ee98d4d9d4b" -->
## Typical Tasks

1. **Codebase Exploration** - Understand existing architecture
2. **Technology Research** - Investigate options for implementation
3. **Constraint Discovery** - Identify technical/business limitations
4. **Stakeholder Interviews** - Gather additional context
5. **Proof of Concept** - Validate assumptions with quick experiments
6. **Documentation Review** - Read relevant existing docs

<!-- section_id: "ea9a382e-0c76-44c9-9a10-c0ec3f56e719" -->
## Directory Structure

```
stage_N_01_research/
├── ai_agent_system/       # Agent configuration for research tasks
├── hand_off_documents/    # Handoff notes referencing outputs
└── outputs/               # Research artifacts
    ├── findings/          # Research findings documents
    ├── poc/               # Proof of concept code/results
    └── decisions/         # Decision records
```

<!-- section_id: "e87ef0b5-2313-4b57-945e-ef05b57dba76" -->
## Handoff Pattern

**Input from 00:**
- Initial requirements
- User questions/clarifications

**Output to 02:**
- Research findings summary (in `outputs/`)
- Decision records
- Identified constraints
- Handoff document referencing outputs

<!-- section_id: "4aeee02a-b76f-4cb2-8ae2-f4460c8c4e16" -->
## Best Practices

1. **Time-box research** - Don't get stuck in analysis paralysis
2. **Document as you go** - Write findings immediately to `outputs/`
3. **Focus on unknowns** - Research what you don't know, not what you do
4. **Validate assumptions** - Test key assumptions with minimal POCs
5. **Keep handoffs lean** - Reference outputs rather than duplicating content

<!-- section_id: "b87da269-59bf-4243-b0a7-dacfaa31649c" -->
## Common Outputs

| Output Type | Location | Description |
|-------------|----------|-------------|
| Research notes | `outputs/findings/` | Detailed exploration notes |
| POC code | `outputs/poc/` | Proof of concept experiments |
| Decision records | `outputs/decisions/` | Why we chose X over Y |
| Dependency analysis | `outputs/` | What this depends on |
| Risk assessment | `outputs/` | Identified risks and mitigations |
