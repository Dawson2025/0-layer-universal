---
resource_id: "b11661ef-b8ec-4241-b3b9-4cad321e7f34"
resource_type: "knowledge"
resource_name: "stage_01_research"
---
# Stage 01: Research

<!-- section_id: "39e49d0b-11c2-4874-86d7-77017fa1789a" -->
## Purpose

Explore the problem space, gather information, and build understanding before defining specific instructions. This stage bridges request gathering and instruction definition by investigating unknowns.

<!-- section_id: "b9f5582e-b6af-4db4-b918-15f5fa717ea6" -->
## Entry Criteria

- Stage 00 (Request Gathering) complete
- Initial requirements documented
- Unknown areas or questions identified

<!-- section_id: "4b710259-f573-4bbf-a98c-d8b078ebb4f1" -->
## Exit Criteria

- Research findings documented in `outputs/`
- Key decisions recorded
- Dependencies and constraints understood
- Ready to write concrete instructions

<!-- section_id: "5003a9ff-e948-4393-9196-06f9c1728568" -->
## Typical Tasks

1. **Codebase Exploration** - Understand existing architecture
2. **Technology Research** - Investigate options for implementation
3. **Constraint Discovery** - Identify technical/business limitations
4. **Stakeholder Interviews** - Gather additional context
5. **Proof of Concept** - Validate assumptions with quick experiments
6. **Documentation Review** - Read relevant existing docs

<!-- section_id: "4cb66886-0b09-4eba-94b0-df0267ee882c" -->
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

<!-- section_id: "55cd36b2-8e8a-426f-a7f9-014f7251a4c2" -->
## Handoff Pattern

**Input from 00:**
- Initial requirements
- User questions/clarifications

**Output to 02:**
- Research findings summary (in `outputs/`)
- Decision records
- Identified constraints
- Handoff document referencing outputs

<!-- section_id: "429e5c35-505e-4001-94ea-21403495d9cd" -->
## Best Practices

1. **Time-box research** - Don't get stuck in analysis paralysis
2. **Document as you go** - Write findings immediately to `outputs/`
3. **Focus on unknowns** - Research what you don't know, not what you do
4. **Validate assumptions** - Test key assumptions with minimal POCs
5. **Keep handoffs lean** - Reference outputs rather than duplicating content

<!-- section_id: "f1205f58-a467-480b-9879-d84e489c4c39" -->
## Common Outputs

| Output Type | Location | Description |
|-------------|----------|-------------|
| Research notes | `outputs/findings/` | Detailed exploration notes |
| POC code | `outputs/poc/` | Proof of concept experiments |
| Decision records | `outputs/decisions/` | Why we chose X over Y |
| Dependency analysis | `outputs/` | What this depends on |
| Risk assessment | `outputs/` | Identified risks and mitigations |
