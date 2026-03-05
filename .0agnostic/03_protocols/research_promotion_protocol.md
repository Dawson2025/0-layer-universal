---
resource_id: "5732cbb7-5080-46eb-8682-4fb20f7acc24"
resource_type: "protocol"
resource_name: "research_promotion_protocol"
---
# Research-to-Production Promotion Protocol

**Scope**: All agents | **Trigger**: When promoting validated research findings to the default context chain

<!-- section_id: "eebd569e-1992-4201-8b72-154dadafcc6d" -->
## 1. Definitions

| Term | Meaning |
|------|---------|
| **Default Context Chain** | The production system at `0_layer_universal/.0agnostic/` — entity_structure.md, knowledge docs, tools, templates, protocols. This is what agents use by default. Tried-and-true, stable. |
| **Research Context Chain** | Experimental entities in `layer_-1_research/` that test new structural patterns, knowledge architectures, and delegation models before promotion. Agents opt into this via the context chain mode rule. |
| **Promotion** | Moving validated research findings into the default context chain so they become the new production standard. |
| **Reference** | Pointing from production to research outputs without copying them. Research stays the source of truth for research content. |

<!-- section_id: "8faceea6-a338-4bd6-a812-d5d6c50999be" -->
## 2. Two Context Chain Modes

Agents operate in one of two modes (see `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/`):

- **Default Mode** (active unless user opts in): Use only production `.0agnostic/` resources, entity_structure.md, production protocols/rules/knowledge.
- **Research Mode** (user activates): Additionally load research entity knowledge, use experimental patterns from RESEARCH_KNOWLEDGE_INDEX.md references, apply research-specific rules/protocols on top of production defaults.

Default mode is always the safe baseline. Research mode extends it — never replaces it.

<!-- section_id: "85a2b3d8-b830-4da3-be3e-b8e659a71541" -->
## 3. Promotion Workflow (5 Steps)

<!-- section_id: "26b66499-0945-466b-9f1a-36182435d733" -->
### Step 1: Identify
List what research changed:
- Structural patterns (entity structure, directory conventions)
- Knowledge (new concepts, architectures, findings)
- Rules (new constraints, behaviors)
- Protocols (new workflows)
- Tools (new scripts, utilities)

<!-- section_id: "9fc3de83-2b75-4736-8517-a5b5dc165de1" -->
### Step 2: Validate
Confirm research was tested:
- Check `stage_*_07_testing/outputs/` for test results
- Check for working examples (entities using the pattern successfully)
- Minimum bar: pattern used in at least one real entity with documented results

<!-- section_id: "d1df2f43-9440-48e3-9c5d-dd1a3ead356d" -->
### Step 3: Reference
Add pointers in `RESEARCH_KNOWLEDGE_INDEX.md`:
- Entry per research output with path, status, and description
- Prefer linking over copying — research stays source of truth for research content
- Mark promotion status: Referenced | Promoted | Experimental

<!-- section_id: "1a772277-5d95-4156-ba53-eb2f00eff6aa" -->
### Step 4: Integrate
Copy ONLY distilled/consolidated findings to production:
- New protocol → `.0agnostic/03_protocols/`
- New rule → `.0agnostic/02_rules/{static,dynamic}/`
- New template → `.0agnostic/01_knowledge/`
- Structural change → update `entity_structure.md`
- New tool → `.0agnostic/01_knowledge/.../resources/tools/`

Do NOT copy raw research artifacts — reference them instead.

<!-- section_id: "9a237cfd-a8ac-4e20-9348-db25ae2adc94" -->
### Step 5: Verify
- Run `agnostic-sync.sh` on all affected entities
- Verify `entity_structure.md` reflects structural changes
- Verify no broken references in RESEARCH_KNOWLEDGE_INDEX.md
- Commit with `[AI Context]` prefix
- Push

<!-- section_id: "723fc6f1-d546-42cc-8f6c-a43c3f0e2566" -->
## 4. What Gets Promoted vs Referenced vs Stays

| Category | Action | Examples |
|----------|--------|----------|
| **PROMOTE** | Copy to production | Proven structural patterns, validated rules/protocols, consolidated knowledge, tools |
| **REFERENCE** | Link from production | Raw research docs, intermediate findings, test artifacts, design explorations |
| **STAY** | Leave in research only | Entity-specific context, experimental/unvalidated features, WIP designs |

<!-- section_id: "d09d1c47-e150-49b4-b60d-0ccf2be3ec94" -->
## 5. Promotion Checklist (Reusable)

For each promotion cycle:

- [ ] Research entity has stage_07 (testing) outputs or equivalent validation
- [ ] Key findings distilled into summary (not just raw research)
- [ ] `RESEARCH_KNOWLEDGE_INDEX.md` updated with new/modified entries
- [ ] Production templates updated if structural change (entity_structure.md)
- [ ] Production protocols updated if new workflow
- [ ] Production knowledge docs updated if new concepts
- [ ] Context chain mode rule updated if research mode behavior changes
- [ ] `agnostic-sync.sh` run on affected entities
- [ ] Root `0AGNOSTIC.md` updated with references to new docs
- [ ] Commit `[AI Context] promote: <description>`
- [ ] Push

<!-- section_id: "852c7f5c-5207-41e4-b976-0e315dfc2441" -->
## 6. Research Entity Paths

| Entity | Path (relative to 0_layer_universal/) | Covers |
|--------|---------------------------------------|--------|
| **Agent Delegation System** | `layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/` | Delegation patterns, stage agents, 0AGNOSTIC.md structure, two-halves pattern, three-tier knowledge |
| **Memory System** | `...agent_delegation_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/` | Memory architecture, context flow, avenue web design, data-based avenues, SHIMI |
| **Context Chain System** | `...memory_system/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_context_chain_system/` | 8-avenue architecture, chain optimization, static/dynamic context, chain validation (76 PASS tests) |

<!-- section_id: "d1c3f915-4866-4264-9950-3a60dee804db" -->
## 7. Promotion History

| Date | Research Entity | What Was Promoted | Target Production File |
|------|----------------|-------------------|----------------------|
| 2026-02-20 | agent_delegation_system | Stage report protocol | `.0agnostic/03_protocols/stage_report_protocol.md` |
| 2026-02-20 | agent_delegation_system | Unified .0agnostic/ convention (01-07+) | `.0agnostic/06_.../entity_structure.md` |
| 2026-02-20 | context_chain_system | Avenue web architecture (8+5 avenues) | `.0agnostic/06_context_avenue_web/` |
| 2026-02-20 | agent_delegation_system | Stage guides (11 templates) | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/` |
| 2026-02-25 | ALL | Research knowledge index + promotion protocol | `.0agnostic/01_knowledge/.../RESEARCH_KNOWLEDGE_INDEX.md`, `.0agnostic/03_protocols/research_promotion_protocol.md` |
| 2026-02-25 | ALL | Context chain mode switching | `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/` |

<!-- section_id: "a608e304-2552-4317-ae71-a619b9e58a3a" -->
## Related

- **Knowledge index**: `.0agnostic/01_knowledge/layer_stage_system/docs/RESEARCH_KNOWLEDGE_INDEX.md`
- **Mode switching rule**: `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/context_chain_mode.md`
- **Source of truth protocol**: `.0agnostic/03_protocols/source_of_truth_protocol.md`
