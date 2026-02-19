# Stage 01: Research

## Purpose

Explore the problem space, gather information, and build understanding before defining specific instructions. This stage bridges request gathering and instruction definition by investigating unknowns.

## Entry Criteria

- Stage 00 (Request Gathering) complete
- Initial requirements documented
- Unknown areas or questions identified

## Exit Criteria

- Research findings documented in `outputs/`
- Key decisions recorded
- Dependencies and constraints understood
- Ready to write concrete instructions

## Typical Tasks

1. **Codebase Exploration** - Understand existing architecture
2. **Technology Research** - Investigate options for implementation
3. **Constraint Discovery** - Identify technical/business limitations
4. **Stakeholder Interviews** - Gather additional context
5. **Proof of Concept** - Validate assumptions with quick experiments
6. **Documentation Review** - Read relevant existing docs

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

## Handoff Pattern

**Input from 00:**
- Initial requirements
- User questions/clarifications

**Output to 02:**
- Research findings summary (in `outputs/`)
- Decision records
- Identified constraints
- Handoff document referencing outputs

## Best Practices

1. **Time-box research** - Don't get stuck in analysis paralysis
2. **Document as you go** - Write findings immediately to `outputs/`
3. **Focus on unknowns** - Research what you don't know, not what you do
4. **Validate assumptions** - Test key assumptions with minimal POCs
5. **Keep handoffs lean** - Reference outputs rather than duplicating content

## Common Outputs

| Output Type | Location | Description |
|-------------|----------|-------------|
| Research notes | `outputs/findings/` | Detailed exploration notes |
| POC code | `outputs/poc/` | Proof of concept experiments |
| Decision records | `outputs/decisions/` | Why we chose X over Y |
| Dependency analysis | `outputs/` | What this depends on |
| Risk assessment | `outputs/` | Identified risks and mitigations |
