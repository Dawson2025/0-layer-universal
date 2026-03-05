---
resource_id: "812065f5-4ae5-47cc-8941-66e3584b2536"
resource_type: "document"
resource_name: "stage_01_research"
---
# Stage 01: Research

<!-- section_id: "cb031918-69bc-414f-9b74-841361747283" -->
## Purpose

Explore the problem space, gather information, and build understanding before defining specific instructions. This stage bridges request gathering and instruction definition by investigating unknowns.

<!-- section_id: "785660e3-3845-4db7-93d4-2d86ac11a433" -->
## Entry Criteria

- Stage 00 (Request Gathering) complete
- Initial requirements documented
- Unknown areas or questions identified

<!-- section_id: "714b21a0-f02e-4a21-8b32-0d4917a388ab" -->
## Exit Criteria

- Research findings documented in `outputs/`
- Key decisions recorded
- Dependencies and constraints understood
- Ready to write concrete instructions

<!-- section_id: "3d6931be-e9b4-41b6-bae2-dc40aee03a2b" -->
## Typical Tasks

1. **Codebase Exploration** - Understand existing architecture
2. **Technology Research** - Investigate options for implementation
3. **Constraint Discovery** - Identify technical/business limitations
4. **Stakeholder Interviews** - Gather additional context
5. **Proof of Concept** - Validate assumptions with quick experiments
6. **Documentation Review** - Read relevant existing docs

<!-- section_id: "1d4a5d3d-e687-4a8b-a542-2837f10da442" -->
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

<!-- section_id: "b2d7c7b1-f7a2-4107-a79a-c11dff2be4e4" -->
## Handoff Pattern

**Input from 00:**
- Initial requirements
- User questions/clarifications

**Output to 02:**
- Research findings summary (in `outputs/`)
- Decision records
- Identified constraints
- Handoff document referencing outputs

<!-- section_id: "bcf5444d-56ba-4e39-8c4b-725f5bc636d6" -->
## Best Practices

1. **Time-box research** - Don't get stuck in analysis paralysis
2. **Document as you go** - Write findings immediately to `outputs/`
3. **Focus on unknowns** - Research what you don't know, not what you do
4. **Validate assumptions** - Test key assumptions with minimal POCs
5. **Keep handoffs lean** - Reference outputs rather than duplicating content

<!-- section_id: "4607fb92-55fc-448a-9abb-e6113f50ce99" -->
## Common Outputs

| Output Type | Location | Description |
|-------------|----------|-------------|
| Research notes | `outputs/findings/` | Detailed exploration notes |
| POC code | `outputs/poc/` | Proof of concept experiments |
| Decision records | `outputs/decisions/` | Why we chose X over Y |
| Dependency analysis | `outputs/` | What this depends on |
| Risk assessment | `outputs/` | Identified risks and mitigations |
