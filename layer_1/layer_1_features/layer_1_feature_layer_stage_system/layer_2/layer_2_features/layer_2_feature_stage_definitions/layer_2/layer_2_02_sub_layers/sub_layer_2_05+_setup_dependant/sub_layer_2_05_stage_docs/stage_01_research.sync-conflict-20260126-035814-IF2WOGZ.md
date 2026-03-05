---
resource_id: "83debe39-7615-406c-ab95-10dfccc70601"
resource_type: "document"
resource_name: "stage_01_research.sync-conflict-20260126-035814-IF2WOGZ"
---
# Stage 01: Research

<!-- section_id: "56bca159-fe79-431e-8972-360f6742d860" -->
## Purpose

Explore the problem space, gather information, and build understanding before defining specific instructions. This stage bridges request gathering and instruction definition by investigating unknowns.

<!-- section_id: "46b2a5b8-86d8-4a80-b85c-1348b8c4113d" -->
## Entry Criteria

- Stage 00 (Request Gathering) complete
- Initial requirements documented
- Unknown areas or questions identified

<!-- section_id: "ee794db2-9951-4fce-b1ce-b56228e3aaa4" -->
## Exit Criteria

- Research findings documented in `outputs/`
- Key decisions recorded
- Dependencies and constraints understood
- Ready to write concrete instructions

<!-- section_id: "177155fc-4604-4456-ba64-cb080f17261e" -->
## Typical Tasks

1. **Codebase Exploration** - Understand existing architecture
2. **Technology Research** - Investigate options for implementation
3. **Constraint Discovery** - Identify technical/business limitations
4. **Stakeholder Interviews** - Gather additional context
5. **Proof of Concept** - Validate assumptions with quick experiments
6. **Documentation Review** - Read relevant existing docs

<!-- section_id: "8f13ae45-c52e-4b0d-abb2-eac24864cc8b" -->
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

<!-- section_id: "6492753a-28b9-4eb4-82f5-7993efa9a455" -->
## Handoff Pattern

**Input from 00:**
- Initial requirements
- User questions/clarifications

**Output to 02:**
- Research findings summary (in `outputs/`)
- Decision records
- Identified constraints
- Handoff document referencing outputs

<!-- section_id: "f0319adb-6be0-4a6a-9dbb-999cfa539fbd" -->
## Best Practices

1. **Time-box research** - Don't get stuck in analysis paralysis
2. **Document as you go** - Write findings immediately to `outputs/`
3. **Focus on unknowns** - Research what you don't know, not what you do
4. **Validate assumptions** - Test key assumptions with minimal POCs
5. **Keep handoffs lean** - Reference outputs rather than duplicating content

<!-- section_id: "d8b99429-acc9-4334-bbe0-551668ed0967" -->
## Common Outputs

| Output Type | Location | Description |
|-------------|----------|-------------|
| Research notes | `outputs/findings/` | Detailed exploration notes |
| POC code | `outputs/poc/` | Proof of concept experiments |
| Decision records | `outputs/decisions/` | Why we chose X over Y |
| Dependency analysis | `outputs/` | What this depends on |
| Risk assessment | `outputs/` | Identified risks and mitigations |
