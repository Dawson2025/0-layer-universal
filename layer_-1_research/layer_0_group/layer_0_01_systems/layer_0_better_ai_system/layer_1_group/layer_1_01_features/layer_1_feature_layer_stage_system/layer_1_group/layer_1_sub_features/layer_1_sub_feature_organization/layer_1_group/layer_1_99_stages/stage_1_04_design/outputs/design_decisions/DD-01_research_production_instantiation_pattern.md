---
resource_id: "1e6c8090-a437-4c08-aa46-74b682941a1a"
resource_type: "output"
resource_name: "DD-01_research_production_instantiation_pattern"
---
# DD-01: Research/Production/Instantiation Pattern

**Date**: 2026-02-25
**Status**: accepted
**Addresses**: Branch 01 (Research/Production Lifecycle), Branch 03 need_01 (General Pattern)

---

## Problem Statement

Any system that evolves needs a way to separate experimental work from stable patterns, and both from personalized instances. Without this separation:

1. Experimental changes risk breaking stable systems
2. Users can't get personalized experiences
3. There's no clear lifecycle from idea to delivery
4. Features have no structured path from research to production

## Proposed Solution: The R/P/I Tri-Version Pattern

Every system maintains three concurrent structural versions:

### 1. Research (layer_-1)

```
system/
  layer_-1_research/
    layer_-1_system_name/           # Research project
      layer_0_group/
        layer_0_features/
          layer_0_feature_X/        # Research feature
            layer_1_group/
              layer_1_99_stages/    # Full stage lifecycle
                stage_1_01_request_gathering/
                stage_1_02_research/
                ...
```

**Characteristics**:
- Experimental, exploratory, permission to fail
- Each feature has its own stage lifecycle (01-11)
- Isolated from production — failures don't cascade
- Can reference production content (read-only)
- Multiple research features can run in parallel

### 2. Production (standard entity)

```
system/
  layer_0/                          # Universal production content
    .0agnostic/                     # Validated rules, knowledge, protocols
      01_knowledge/                 # Proven patterns
      02_rules/                     # Tested rules
      03_protocols/                 # Validated protocols
  layer_1/
    layer_1_projects/               # Active projects using production patterns
```

**Characteristics**:
- Stable, tried-and-true, default for all agents
- Content has been validated through promotion workflow
- Serves as the template for new entity creation
- Conservative — prefers proven patterns over novel ones
- Version tracked — knows what was promoted and when

### 3. Instantiation (children)

```
system/
  layer_1/
    layer_1_projects/
      layer_1_project_school/       # System instantiation
        layer_2_group/
          layer_2_instances/
            layer_2_instance_student_A/  # Per-user instance
              0AGNOSTIC.md               # User-specific identity
              .0agnostic/                # User-specific context
```

**Characteristics**:
- Per-user or per-context entities
- Inherit from production template via context chain
- Store user-specific state (profile, progress, goals)
- Multiple instances coexist independently
- Can be dynamically created as new users are added

## The R/P/I Lifecycle

```
RESEARCH ──[promotion]──→ PRODUCTION ──[instantiation]──→ INSTANCES
    ↑                          ↑                              │
    │                          │                              │
    └──────────────────────────┴──────[feedback]──────────────┘
```

1. **Research proposes**: New features, patterns, approaches
2. **Promotion validates**: Testing, review, approval
3. **Production stabilizes**: Becomes the default, template for instances
4. **Instantiation personalizes**: Per-user context, specific to their needs
5. **Feedback informs**: Instance usage reveals needs for new research

## Alternatives Considered

### Alternative A: Single-Version System
Everything in one place. No separation between experimental and stable.
- **Rejected**: Too risky. Experimental changes affect all users immediately.

### Alternative B: Branch-Based Versioning (git-style)
Use git branches for research vs production.
- **Rejected**: Branches are temporal (eventually merge). R/P/I is permanent and concurrent. Also doesn't handle instantiation.

### Alternative C: Configuration-Based Versioning
Use feature flags to toggle between research and production content.
- **Rejected**: Doesn't provide structural separation. Config drift is hard to track. Doesn't address instantiation.

## Trade-offs

| Trade-off | Accepted | Why |
|-----------|----------|-----|
| More directories | Yes | Structure prevents contamination — worth the overhead |
| Promotion overhead | Yes | Controlled promotion is safer than ad-hoc copying |
| Context chain complexity | Yes | Inheritance through context chain avoids content duplication |
| Duplication of entity structure | Minimal | Same conventions at every level reduce cognitive load |

## Design Constraints

- MUST use existing layer-stage conventions (entity structure, .0agnostic/, etc.)
- MUST be compatible with the context chain system
- MUST NOT require agents to understand all three versions simultaneously
- SHOULD be adoptable incrementally (start with R/P, add I later)

## Implementation Notes

- Research entities use `layer_-1_research/` prefix
- Production is the standard entity (no special prefix)
- Instances use `layer_N_instance_name/` naming
- Context chain mode switching enables agents to access research when needed
- Existing `research_promotion_protocol.md` handles the R→P transition
