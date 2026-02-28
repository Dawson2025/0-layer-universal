# Research Layer Organization and Structure

**Date**: 2026-02-28
**Context**: layer_-1_research reorganization and structure validation
**Purpose**: Document the organizational design and rationale for research layer structure

---

## Executive Summary

The research layer (`layer_-1_research`) has been reorganized with a nested group structure that clearly separates:
- **Layer_-1 concerns** (research layer's own organization) via `layer_-1_group/`
- **Layer_0 research** (validating foundational structures before production) via `layer_0_group/`
- **Systems vs Projects** distinction (foundational patterns vs specific applications)

This structure enables efficient research, clear categorization, and seamless promotion of validated structures to production.

---

## Overall Architecture

```
layer_-1_research/
├── layer_-1_group/                    # Research layer metadata & workflow
│   ├── layer_-1_00_layer_registry/    # Registry for layer_-1 level
│   └── layer_-1_99_stages/            # Workflow stages for research layer (01-11)
│
├── layer_0_group/                     # Layer_0 structures under research
│   ├── layer_0_00_layer_registry/     # Registry for layer_0 level
│   ├── layer_0_99_stages/             # Workflow stages for layer_0 work (01-11)
│   │
│   ├── layer_0_systems/               # Foundational, reusable patterns
│   │   ├── layer_-1_better_ai_system/
│   │   └── layer_-1_learning_simulation_system/
│   │
│   └── layer_0_projects/              # Specific applications/initiatives
│       └── layer_-1_langtrak_dev_agent_system/
│
├── .0agnostic/                        # Universal resources
├── outputs/                           # Episodic memory
├── hand_off_documents/                # Handoff documentation
└── 0AGNOSTIC.md                       # Source of truth
```

---

## Key Organizational Principles

### 1. Nested Group Structure

**Two-level group hierarchy** provides clear separation of concerns:

| Level | Group | Purpose | Contains |
|-------|-------|---------|----------|
| Layer_-1 | `layer_-1_group/` | Research layer's own organization | Registry, stages for research workflow |
| Layer_0 | `layer_0_group/` | Layer_0 structures being validated | Registry, stages, systems, projects |

**Benefits**:
- Research layer can organize itself independently
- Layer_0 structures can be researched, tested, and promoted as a unit
- Clear boundaries between research infrastructure and research content
- Extensible: additional layers (layer_1_group, layer_2_group) can be added as needed

### 2. Systems vs Projects Distinction

**layer_0_systems** — Foundational, reusable architectural constructs:
- Patterns and frameworks applicable across multiple contexts
- Establish core behaviors and constraints
- Have broad applicability
- Examples: better_ai_system (SHIMI, agent memory), learning_simulation_system

**layer_0_projects** — Specific applications and initiatives:
- Demonstrate or implement layer_0 systems
- Have focused scope and clear outcomes
- Build on foundational systems
- Examples: langtrak_dev_agent_system (demonstrates language tracking capabilities)

**Why this distinction matters**:
- Prevents conflation of patterns (reusable) with applications (specific)
- Enables systematic reuse of proven systems across new projects
- Clarifies promotion path: systems → layer_0 core patterns; projects → layer_0 applications
- Supports scaling: add new projects leveraging existing systems

### 3. Workflow Stages at Each Level

**Layer_-1 stages** (in `layer_-1_group/layer_-1_99_stages/`):
- For organizing the research process itself
- Manages how research is conducted, reviewed, validated
- 11 stages: 01_request_gathering through 11_archives

**Layer_0 stages** (in `layer_0_group/layer_0_99_stages/`):
- For organizing the development of layer_0 structures
- Tracks maturity of systems and projects from research → production
- 11 stages: 01_request_gathering through 11_archives
- Each system/project can progress through these stages independently

---

## Organization Details

### Systems Organization

#### layer_-1_better_ai_system
- **Type**: System (foundational patterns)
- **Purpose**: SHIMI concepts, agent memory, multi-agent sync architectures
- **Status**: Active research
- **Structure**: Full layer_-1 entity with own `.0agnostic/`, stages, and layer hierarchy
- **Integration**: Provides AI patterns applicable across other systems and projects

#### layer_-1_learning_simulation_system
- **Type**: System (foundational patterns)
- **Purpose**: Learning simulation frameworks, intelligent tutoring architectures
- **Status**: Active research
- **Structure**: Full layer_-1 entity with own `.0agnostic/`, stages, and layer hierarchy
- **Integration**: Provides simulation patterns for educational applications

### Projects Organization

#### layer_-1_langtrak_dev_agent_system
- **Type**: Project (specific application)
- **Purpose**: Language tracking agent system demonstrating layer_0 AI patterns
- **Status**: Active development
- **Structure**: Full layer_-1 entity with own `.0agnostic/`, stages, and layer hierarchy
- **Integration**: Applies layer_0 AI system patterns to language learning domain

---

## Resource Navigation

### For Research Layer Coordination

| Need | Location |
|------|----------|
| Layer_-1 metadata | `layer_-1_group/layer_-1_00_layer_registry/` |
| Research workflow stages | `layer_-1_group/layer_-1_99_stages/` |
| Universal context | `0AGNOSTIC.md` |
| Universal resources | `.0agnostic/` |

### For Layer_0 Research

| Need | Location |
|------|----------|
| Layer_0 metadata | `layer_0_group/layer_0_00_layer_registry/` |
| Layer_0 development stages | `layer_0_group/layer_0_99_stages/` |
| Systems research | `layer_0_group/layer_0_systems/` |
| Projects research | `layer_0_group/layer_0_projects/` |

### For Individual Entities

Each research project (better_ai_system, learning_simulation_system, langtrak_dev_agent_system):
- Has own `0AGNOSTIC.md` source of truth
- Has own `.0agnostic/` resources (knowledge, rules, protocols)
- Has own layer hierarchy (nested groups and stages)
- Can be worked on independently or in coordination with others

---

## Promotion Path

### From Research to Production

Once a layer_0 structure is validated:

1. **Research Phase** (in layer_-1_research):
   - Progress through layer_0 stages (01_request_gathering → 10_current_product)
   - Validate against requirements
   - Complete handoff documentation

2. **Promotion Phase**:
   - Use research promotion protocol: `.0agnostic/03_protocols/research_promotion_protocol.md`
   - Systems → `/home/dawson/dawson-workspace/code/0_layer_universal/layer_0/layer_0_*_*/`
   - Projects → Appropriate layer_1 or higher location

3. **Archive Phase**:
   - Move to stage_0_11_archives in research location
   - Maintain historical reference

---

## Design Rationale

### Why Nested Groups?

The nested group structure (layer_-1_group within layer_-1_research, plus layer_0_group within layer_-1_research) provides:

1. **Separation of Concerns**
   - Research layer infrastructure (layer_-1_group) separate from research content (layer_0_group)
   - Enables independent evolution of both

2. **Scalability**
   - Can add layer_1_group, layer_2_group as needs expand
   - Each layer's research organized consistently
   - New research layers inherit proven organizational patterns

3. **Clear Promotion Path**
   - layer_0_group contains layer_0 structures
   - When validated, move directly to production layer_0
   - No structural transformation needed

### Why Systems vs Projects?

Distinction prevents common pitfalls:

1. **Reusability Anti-Pattern**: Mixing patterns with applications makes patterns harder to identify and reuse
2. **Complexity**: Systems need different validation criteria than projects
3. **Scope Clarity**: Systems answer "what foundational patterns do we need?"; Projects answer "what specific applications need we build?"

---

## Current Research Status

### Systems Under Research

| System | Stage | Key Focus |
|--------|-------|-----------|
| Better AI System | 01-11 stages available | SHIMI, agent memory, multi-agent coordination |
| Learning Simulation System | 01-11 stages available | Educational frameworks, intelligent tutoring |

### Projects Under Research

| Project | Stage | Key Focus |
|---------|-------|-----------|
| LangTrack Dev Agent | 01-11 stages available | Language tracking demonstration of AI patterns |

### Infrastructure

- ✅ layer_-1_group with registry and 11 stages
- ✅ layer_0_group with registry and 11 stages
- ✅ layer_0_systems directory with README and organization docs
- ✅ layer_0_projects directory with README and organization docs
- ✅ All 3 research entities properly placed
- ✅ 0AGNOSTIC.md updated with new structure
- ✅ READMEs created for all subdirectories

---

## Integration Points

### Cascading Context

The organizational structure cascades through:
- **0AGNOSTIC.md** (source of truth) → **CLAUDE.md** (auto-generated) → **Agent context**
- **Navigation section** lists all key locations
- **Triggers table** references applicable rules and protocols

### Skills and Protocols

| Resource | Location | Purpose |
|----------|----------|---------|
| Research promotion protocol | `.0agnostic/03_protocols/research_promotion_protocol.md` | Guides moving validated structures to production |
| Entity creation skill | `/entity-creation` | Creates new research entities following canonical structure |
| Stage workflow skill | `/stage-workflow` | Guides navigation through research stages |

---

## Next Steps

### Immediate

1. ✅ Structure created and validated
2. ✅ Documentation in place
3. Next: Use stage workflow to progress research entities through stages

### Medium-term

1. Complete layer_0_99_stages for each research entity
2. Progress systems/projects toward stage_0_10_current_product
3. Populate layer_0_00_layer_registry with research status

### Long-term

1. Validate research structures
2. Prepare promotion documentation
3. Promote validated systems to production layer_0
4. Archive completed research

---

## Appendix: Command Reference

### Navigate to Research Structure

```bash
# View overall research organization
cd /home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/
cat 0AGNOSTIC.md

# View layer_0_group organization
cd layer_0_group/
cat README.md

# View systems research
cd layer_0_systems/
ls -d layer_-1_*/

# View projects research
cd ../layer_0_projects/
ls -d layer_-1_*/
```

### Add New Research

```bash
# Create new system (example)
/entity-creation --layer=-1 --type=system --name=new-system

# Create new project (example)
/entity-creation --layer=-1 --type=project --name=new-project
```

---

## Document Metadata

- **Created**: 2026-02-28
- **Stage Output Location**: `/home/dawson/dawson-workspace/code/0_layer_universal/layer_-1_research/layer_0_group/layer_0_systems/layer_-1_better_ai_system/layer_-1_group/layer_-1_99_stages/stage_-1_02_research/outputs/`
- **Related Documents**:
  - `.0agnostic/03_protocols/research_promotion_protocol.md`
  - `0AGNOSTIC.md` (layer_-1_research)
  - `layer_0_group/README.md`
  - `layer_0_systems/README.md`
  - `layer_0_projects/README.md`

**Reviewed By**: Claude Haiku 4.5
**Status**: Complete and committed to git
