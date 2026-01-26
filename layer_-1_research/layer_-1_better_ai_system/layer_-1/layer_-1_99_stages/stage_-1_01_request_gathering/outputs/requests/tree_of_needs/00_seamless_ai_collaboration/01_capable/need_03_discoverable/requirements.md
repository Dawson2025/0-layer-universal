# Need: Discoverable

**Branch**: [01_capable](../)
**Question**: "Can AI find what it needs by exploring the structure?"

---

## Definition

AI can navigate the system to locate relevant information without constant hand-holding.
- Clear hierarchy (layers, stages, components)
- Self-describing system prompts at each level
- AI can understand "where am I" and "what's happening here"

---

## Why This Matters

- AI needs information to be effective
- Users shouldn't have to point AI to everything
- System structure should be discoverable
- AI should understand "where am I" and "what's here"

---

## Requirements

### Layer-Stage Structure (from request_01)
- MUST have consistent layer-stage-component structure
- MUST use unified naming convention: `layer_N_XX_name`, `stage_N_XX_name`
- MUST adopt single stage numbering scheme across all layers
- MUST have system prompt at each level explaining that level

### Registry System (from request_01)
- MUST have `layer_registry.yaml` listing all layers
- MUST have `stage_registry.yaml` listing all stages
- Registries MUST be the authoritative source
- MUST have consistent status tracking via `status.json`

### Self-Describing Prompts
- MUST have each CLAUDE.md/AGNOSTIC.md explain its context
- MUST include navigation hints (what's above, below, related)
- MUST describe available resources at each level
- SHOULD include entry points for common tasks

### Documentation Alignment (from request_05)
- MUST have tooling to validate all path references in docs
- MUST keep docs aligned with actual structure
- MUST designate authoritative doc for each topic
- MUST have single, clear entry point chain
- MUST maintain master index of all docs
- SHOULD auto-fix simple path issues

### Entry Point Chain (from request_06)
- MUST have single starting CLAUDE.md
- MUST chain to layer/project/feature CLAUDE.md logically
- MUST document chain order
- SHOULD support skipping irrelevant levels

---

## Acceptance Criteria

- [ ] No naming inconsistencies found by validation script
- [ ] All registries exist and are populated
- [ ] All `layer_N_99_stages/` directories have `status.json`
- [ ] AI can determine its location in the hierarchy
- [ ] Each level has a prompt explaining context and structure
- [ ] AI can navigate up/down the hierarchy
- [ ] Path validator exists and runs in CI
- [ ] Zero broken paths in documentation
- [ ] Single init prompt chain is documented
- [ ] Master documentation index exists

---

## Integrated From

- request_01: REQ-01-F01, REQ-01-F02, REQ-01-F03, REQ-01-F04
- request_05: REQ-05-F01, REQ-05-F02, REQ-05-F03, REQ-05-F04, REQ-05-F05
- request_06: REQ-06-F03
