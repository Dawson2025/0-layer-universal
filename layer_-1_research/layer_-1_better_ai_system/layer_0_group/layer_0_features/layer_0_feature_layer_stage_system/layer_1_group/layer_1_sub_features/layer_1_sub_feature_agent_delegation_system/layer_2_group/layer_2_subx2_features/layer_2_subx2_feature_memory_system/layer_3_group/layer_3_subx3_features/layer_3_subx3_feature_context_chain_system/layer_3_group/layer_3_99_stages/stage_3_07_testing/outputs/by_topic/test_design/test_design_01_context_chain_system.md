# Test Design: 01 Context Chain System Design

**Validates**: `stage_3_04_design/outputs/by_topic/01_context_chain_system_design.md`
**Type**: Structural (bash) + Integration (bash) + Behavioral (manual/agent)
**Script name**: `test_context_chain_system_design.sh`

---

## What We're Testing

The foundational architecture: 4 architecture layers (Static, Dynamic Retrieval, Orchestration, Trust/Governance), 8 MVP avenues, dual-chain model (context chaining vs reference chaining), dual-path reachability requirement, JSON-LD coverage contract, and compaction-safe subset.

---

## Test Cases

### TC-01-01: Architecture layers — all 4 layers have representatives

**Steps**:
1. **Static Context Layer**: Verify 0AGNOSTIC.md, CLAUDE.md (and other tool files), and `.claude/rules/` exist for context_chain_system
2. **Dynamic Retrieval Layer**: Verify `.claude/skills/` has at least one skill, `.0agnostic/04_episodic_memory/` exists
3. **Orchestration Layer**: Verify at least one `.gab.jsonld` exists in the entity hierarchy (orchestrators/agents)
4. **Trust/Governance Layer**: Check for provenance markers (auto-generated footers in tool files, `promote: hot` frontmatter in rules)

**Expected**: All 4 architecture layers have concrete artifacts
**Type**: Structural

### TC-01-02: 8 MVP avenues — all present and functional

**Steps**:
1. Avenue 1 (System prompt chain): CLAUDE.md exists and has content
2. Avenue 2 (Path-specific rules): `.claude/rules/` has .md files
3. Avenue 3 (Skills): `.claude/skills/` has subdirs with SKILL.md
4. Avenue 4 (@import references): 0AGNOSTIC.md contains path references to `.0agnostic/` resources
5. Avenue 5 (JSON-LD graph): At least one `.gab.jsonld` exists in entity tree
6. Avenue 6 (Integration summaries): For each `.gab.jsonld`, a matching `.integration.md` exists
7. Avenue 7 (Episodic memory): `.0agnostic/04_episodic_memory/` has index.md
8. Avenue 8 (0AGNOSTIC fallback): 0AGNOSTIC.md exists and is readable

**Expected**: All 8 avenues have at least one artifact present
**Note**: Extends existing test_avenue_coverage_functional with stricter per-avenue checks
**Type**: Structural

### TC-01-03: Avenue 5/6 paired contract — JSON-LD always has integration.md

**Steps**:
1. Find all `.gab.jsonld` files recursively from entity root
2. For each, derive expected `.integration.md` path (same directory, same base name)
3. Verify `.integration.md` exists
4. Find all `.integration.md` files
5. For each, verify a matching `.gab.jsonld` exists (bidirectional)

**Expected**: 1:1 pairing — no orphan JSON-LD without summary, no orphan summary without JSON-LD
**Type**: Structural

### TC-01-04: JSON-LD coverage contract — required graph classes discoverable

**Steps**:
1. Scan hierarchy for `.gab.jsonld` and other `.jsonld` files
2. Categorize by class:
   - Layer orchestrators (`layer_*_orchestrator.gab.jsonld`) — expect at least 1
   - Stage orchestrators (`*_99_stages_orchestrator.gab.jsonld`) — if stages dir exists
   - Stage agents (`stage_*_agent.jsonld`) — for active stages
   - Layer/feature indexes (`index.jsonld`) — for registry dirs
3. Report coverage: which classes found, which missing

**Expected**: At minimum layer orchestrator class is present; report completeness of other classes
**Type**: Structural (audit)

### TC-01-05: Context chaining vs reference chaining distinction

**Steps**:
1. Read CLAUDE.md for context_chain_system
2. Identify **context chain** elements (content loaded inline — identity, rules, triggers)
3. Identify **reference chain** elements (pointers to other locations — "Read .0agnostic/...", path references)
4. Verify both types are present
5. Verify reference chains use path syntax (not inline content dumps)

**Expected**: CLAUDE.md contains both inline context and pointer-based references — the two chain types are distinguishable
**Type**: Structural

### TC-01-06: Dual-path reachability — critical rules reachable via 2+ avenues

**Steps**:
1. Define critical rules to check:
   - "AI Context Modification Protocol"
   - "Stage Completeness Rule"
   - "AI Context Commit/Push Rule"
2. For each critical rule, check reachability:
   - **Static path 1**: Present in CLAUDE.md cascade (hot)
   - **Static path 2**: Present in `.claude/rules/` or `.0agnostic/02_rules/` (warm/cold)
   - **Dynamic path**: Discoverable via skill WHEN conditions, rule `promote: hot` pointers, or JSON-LD constraints
3. Count reachable paths per rule

**Expected**: Each critical rule is reachable through at least 2 independent avenues
**Type**: Integration

### TC-01-07: Compaction-safe subset — essential identity survives truncation

**Steps**:
1. Read CLAUDE.md for entity
2. Extract the first 30 lines (simulating aggressive compaction)
3. Verify these 30 lines contain:
   - Entity identity (role, scope)
   - Parent reference (navigation)
   - At least one trigger (how to load more)
4. Verify at least one pointer to deeper content exists in first 30 lines

**Expected**: Minimal viable context (identity + navigation + triggers) lives in the top of CLAUDE.md
**Type**: Structural

### TC-01-08: Design goal validation — progressive disclosure in practice

**Steps**:
1. Count lines in CLAUDE.md (hot — always loaded)
2. Count lines in `.claude/rules/*.md` (warm — loaded on path match)
3. Count total lines in `.0agnostic/` content (cold — loaded on demand)
4. Verify the ratio: hot < warm < cold (progressive disclosure pyramid)

**Expected**: Context volume increases as temperature decreases — hot is leanest, cold is largest
**Type**: Structural (heuristic)

---

## Coverage Gap Analysis

| Design Concept | Test Case | Status |
|---------------|-----------|--------|
| 4 architecture layers | TC-01-01 | New |
| 8 MVP avenues | TC-01-02 | Extends existing |
| Avenue 5/6 paired contract | TC-01-03 | New |
| JSON-LD coverage classes | TC-01-04 | New (audit) |
| Context vs reference chaining | TC-01-05 | New |
| Dual-path reachability | TC-01-06 | New |
| Compaction-safe subset | TC-01-07 | New |
| Progressive disclosure | TC-01-08 | New |
| Governance layer (trust/policy) | TC-01-01 partial | Minimal — governance not yet implemented |
| MCP integration (post-MVP) | Not testable | Not yet built |
