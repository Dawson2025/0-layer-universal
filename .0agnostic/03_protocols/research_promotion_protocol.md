---
resource_id: "5732cbb7-5080-46eb-8682-4fb20f7acc24"
resource_type: "protocol"
resource_name: "research_promotion_protocol"
---
# Research-to-Production Promotion Protocol

**Scope**: All agents | **Trigger**: When promoting validated research findings to the default context chain

## 1. Definitions

| Term | Meaning |
|------|---------|
| **Default Context Chain** | The production system at `0_layer_universal/.0agnostic/` — entity_structure.md, knowledge docs, tools, templates, protocols. This is what agents use by default. Tried-and-true, stable. |
| **Research Context Chain** | Experimental entities in `layer_-1_research/` that test new structural patterns, knowledge architectures, and delegation models before promotion. Agents opt into this via the context chain mode rule. |
| **Promotion** | Moving validated research findings into the default context chain so they become the new production standard. |
| **Reference** | Pointing from production to research outputs without copying them. Research stays the source of truth for research content. |

## 2. Two Context Chain Modes

Agents operate in one of two modes (see `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/`):

- **Default Mode** (active unless user opts in): Use only production `.0agnostic/` resources, entity_structure.md, production protocols/rules/knowledge.
- **Research Mode** (user activates): Additionally load research entity knowledge, use experimental patterns from RESEARCH_KNOWLEDGE_INDEX.md references, apply research-specific rules/protocols on top of production defaults.

Default mode is always the safe baseline. Research mode extends it — never replaces it.

## 3. Promotion Workflow (5 Steps)

### Step 1: Identify
List what research changed:
- Structural patterns (entity structure, directory conventions)
- Knowledge (new concepts, architectures, findings)
- Rules (new constraints, behaviors)
- Protocols (new workflows)
- Tools (new scripts, utilities)

### Step 2: Validate
Confirm research was tested:
- Check `stage_*_07_testing/outputs/` for test results
- Check for working examples (entities using the pattern successfully)
- Minimum bar: pattern used in at least one real entity with documented results

### Step 3: Reference
Add pointers in `RESEARCH_KNOWLEDGE_INDEX.md`:
- Entry per research output with path, status, and description
- Prefer linking over copying — research stays source of truth for research content
- Mark promotion status: Referenced | Promoted | Experimental

### Step 4: Integrate
Copy ONLY distilled/consolidated findings to production:
- New protocol → `.0agnostic/03_protocols/`
- New rule → `.0agnostic/02_rules/{static,dynamic}/`
- New template → `.0agnostic/01_knowledge/`
- Structural change → update `entity_structure.md`
- New tool → `.0agnostic/01_knowledge/.../resources/tools/`

Do NOT copy raw research artifacts — reference them instead.

### Step 5: Verify
- Run `agnostic-sync.sh` on all affected entities
- Verify `entity_structure.md` reflects structural changes
- Verify no broken references in RESEARCH_KNOWLEDGE_INDEX.md
- Commit with `[AI Context]` prefix
- Push

## 4. What Gets Promoted vs Referenced vs Stays

| Category | Action | Examples |
|----------|--------|----------|
| **PROMOTE** | Copy to production | Proven structural patterns, validated rules/protocols, consolidated knowledge, tools |
| **REFERENCE** | Link from production | Raw research docs, intermediate findings, test artifacts, design explorations |
| **STAY** | Leave in research only | Entity-specific context, experimental/unvalidated features, WIP designs |

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

## 6. Research Entity Paths

| Entity | Path (relative to 0_layer_universal/) | Covers |
|--------|---------------------------------------|--------|
| **Agent Delegation System** | `layer_-1_research/layer_-1_better_ai_system/layer_0_group/layer_0_features/layer_0_feature_layer_stage_system/layer_1_group/layer_1_sub_features/layer_1_sub_feature_agent_delegation_system/` | Delegation patterns, stage agents, 0AGNOSTIC.md structure, two-halves pattern, three-tier knowledge |
| **Memory System** | `...agent_delegation_system/layer_2_group/layer_2_subx2_features/layer_2_subx2_feature_memory_system/` | Memory architecture, context flow, avenue web design, data-based avenues, SHIMI |
| **Context Chain System** | `...memory_system/layer_3_group/layer_3_subx3_features/layer_3_subx3_feature_context_chain_system/` | 8-avenue architecture, chain optimization, static/dynamic context, chain validation (76 PASS tests) |

## 7. Promotion History

| Date | Research Entity | What Was Promoted | Target Production File |
|------|----------------|-------------------|----------------------|
| 2026-02-20 | agent_delegation_system | Stage report protocol | `.0agnostic/03_protocols/stage_report_protocol.md` |
| 2026-02-20 | agent_delegation_system | Unified .0agnostic/ convention (01-07+) | `.0agnostic/06_.../entity_structure.md` |
| 2026-02-20 | context_chain_system | Avenue web architecture (8+5 avenues) | `.0agnostic/06_context_avenue_web/` |
| 2026-02-20 | agent_delegation_system | Stage guides (11 templates) | `.0agnostic/01_knowledge/layer_stage_system/stage_guides/` |
| 2026-02-25 | ALL | Research knowledge index + promotion protocol | `.0agnostic/01_knowledge/.../RESEARCH_KNOWLEDGE_INDEX.md`, `.0agnostic/03_protocols/research_promotion_protocol.md` |
| 2026-02-25 | ALL | Context chain mode switching | `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/` |

## Related

- **Knowledge index**: `.0agnostic/01_knowledge/layer_stage_system/docs/RESEARCH_KNOWLEDGE_INDEX.md`
- **Mode switching rule**: `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/context_chain_mode.md`
- **Source of truth protocol**: `.0agnostic/03_protocols/source_of_truth_protocol.md`
