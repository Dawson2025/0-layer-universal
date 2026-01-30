# Example Request: Complete Reference

This is a complete example based on Request 01 (Better Layer-Stage System) showing proper formatting and content depth.

---

## request.md Example

```markdown
# Request: Better Layer-Stage System

**Request ID**: 01
**Date**: 2026-01-25
**Priority**: HIGH
**Status**: Active

## Problem Statement

The current Layer-Stage Framework has inconsistent naming conventions, multiple stage numbering schemes, and missing registries that make navigation difficult and break automation.

## Key Issues Identified

1. **Naming Inconsistency**: Mix of dots and underscores in directory names (e.g., `layer_0.01` vs `layer_0_01`)
2. **Stage Numbering Conflict**: Two different stage numbering schemes exist (01-11 vs 00-09)
3. **Missing Registries**: `layer_registry.yaml` referenced but doesn't exist
4. **Wrong Prefixes**: Sub-layers contain `layer_` prefixed children instead of `sub_layer_`
5. **Plus Notation Ambiguity**: `sub_layer_0_05+` meaning is undefined

## Stakeholder

- AI agents navigating the framework
- Developers maintaining the codebase
- Automation scripts relying on consistent patterns

## Desired Outcome

A consistent, well-documented framework where:
- All naming follows underscore convention
- Single stage numbering scheme (01-11)
- All registries exist and are populated
- Automation can reliably traverse the structure
```

---

## requirements.md Example

```markdown
# Requirements: Better Layer-Stage System

**Request ID**: 01
**Last Updated**: 2026-01-25

## Functional Requirements

### REQ-01-F01: Underscore Naming Convention
- All layer, stage, and sub-layer directories use underscores exclusively
- Pattern: `layer_N_XX_name`, `stage_N_XX_name`, `sub_layer_N_XX_name`
- No dots in directory names

### REQ-01-F02: Unified Stage Numbering
- Stages numbered 01-11 consistently
- Scheme: request_gathering(01), research(02), instructions(03), planning(04), design(05), development(06), testing(07), criticism(08), fixing(09), current_product(10), archives(11)

### REQ-01-F03: Layer Registry
- `layer_registry.yaml` exists at designated location
- Contains all layer definitions with id, name, purpose, path
- Follows defined schema

### REQ-01-F04: Sub-Layer Prefix Consistency
- Children of sub_layers use `sub_layer_` prefix, not `layer_`
- Recursive sub-layers maintain proper naming

### REQ-01-F05: Plus Notation Definition
- `sub_layer_N_XX+_name` formally defined
- Means: consolidates XX through XX+9 or until next defined
- Documented in framework docs

## Non-Functional Requirements

### REQ-01-NF01: Backward Compatibility
- Migration path provided for existing content
- No data loss during transition

### REQ-01-NF02: Discoverability
- Structure is self-documenting via README files
- New users can navigate without external docs

### REQ-01-NF03: Automation Support
- Consistent patterns enable scripted traversal
- No special cases or exceptions

## Acceptance Criteria

- [ ] Zero directories with dots in names
- [ ] All stages use 01-11 numbering
- [ ] layer_registry.yaml exists and validates
- [ ] No `layer_` prefixed children inside sub_layers
- [ ] Plus notation documented with examples
```

---

## specs.md Example

```markdown
# Specifications: Better Layer-Stage System

**Request ID**: 01
**Last Updated**: 2026-01-25

## Naming Convention Specification

### Layer Naming
Pattern: `layer_<N>_<XX>_<name>`
- N = Layer number (integer, can be negative)
- XX = Two-digit sequence (00-99)
- name = Snake_case descriptive name

Examples:
- `layer_0_01_ai_manager_system`
- `layer_-1_99_stages`

### Stage Naming
Pattern: `stage_<N>_<XX>_<name>`

| XX | Name |
|----|------|
| 01 | request_gathering |
| 02 | research |
| 03 | instructions |
| 04 | planning |
| 05 | design |
| 06 | development |
| 07 | testing |
| 08 | criticism |
| 09 | fixing |
| 10 | current_product |
| 11 | archives |

## Registry Schema

### layer_registry.yaml
\`\`\`yaml
version: "1.0"
layers:
  - id: "layer_-1"
    name: "Research Layer"
    purpose: "Experimental projects"
    path: "layer_-1_research/"
  - id: "layer_0"
    name: "Universal Layer"
    purpose: "Framework internals"
    path: "layer_0/"
\`\`\`

## Directory Structure

\`\`\`
layer_N/
├── CLAUDE.md
├── layer_N_00_layer_registry/
├── layer_N_01_<system>/
├── layer_N_03_sub_layers/
│   ├── sub_layer_N_01_prompts/
│   ├── sub_layer_N_02_knowledge_system/
│   └── sub_layer_N_05+_setup_dependant/
│       └── sub_layer_N_05_operating_systems/  # Correct: sub_layer_ prefix
└── layer_N_99_stages/
    ├── stage_N_01_request_gathering/
    └── stage_N_11_archives/
\`\`\`
```

---

## Key Takeaways

1. **request.md**: Focus on the problem, not the solution
2. **requirements.md**: Be specific and testable
3. **specs.md**: Provide concrete schemas and examples
4. **Consistency**: Use the same Request ID across all three files
