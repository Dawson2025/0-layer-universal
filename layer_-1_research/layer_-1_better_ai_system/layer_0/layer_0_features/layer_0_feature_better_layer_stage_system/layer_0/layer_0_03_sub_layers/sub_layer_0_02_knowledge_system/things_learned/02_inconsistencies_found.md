# Inconsistencies Found in Layer-Stage System

## Date: 2026-01-25
## Source: Reference Implementation Analysis

---

## 1. Naming Convention Inconsistencies

### Issue: Mixed Dot and Underscore Notation

**Old Convention (Dot Notation)**:
```
layer_1.02_sub_layers
sub_layer_1.05+_setup_dependant
```

**New Convention (Underscore Notation)**:
```
layer_1_02_sub_layers
sub_layer_1_05+_setup_dependant
```

**Current State**: Mixed - some files use dots, others use underscores

**Affected Locations**:
- Reference implementation uses `layer_1.02_sub_layers` pattern
- Newer code uses `layer_1_02_sub_layers` pattern
- Documentation references both styles

**Impact**: Confusion when navigating, inconsistent glob patterns, broken relative references

---

## 2. Stage Numbering Discrepancy

### Issue: Multiple Stage Numbering Schemes

**Scheme A (Reference Implementation - 11 stages, 00-10)**:
| # | Stage |
|---|-------|
| 00 | request_gathering |
| 01 | research |
| ... | ... |
| 10 | archives |

**Scheme B (v3.0 - 12 stages, 00-11)**:
| # | Stage |
|---|-------|
| 00 | stage_registry |
| 01 | request_gathering |
| 02 | research |
| ... | ... |
| 11 | archives |

**Current State**:
- Reference implementation docs describe Scheme A
- Newer implementations use Scheme B
- CLAUDE.md files reference different schemes

**Impact**:
- Stage numbers don't match between documentation and implementation
- Automation scripts may target wrong stages
- Handoff references may be incorrect

---

## 3. Layer Component Numbering

### Issue: Inconsistent Component Positions

**Pattern A (Reference)**:
| Position | Component |
|----------|-----------|
| 00 | ai_manager_system |
| 01 | manager_handoff_documents |
| 02 | sub_layers |
| 99 | stages |

**Pattern B (v3.0)**:
| Position | Component |
|----------|-----------|
| 00 | layer_registry |
| 01 | ai_manager_system |
| 02 | manager_handoff_documents |
| 03 | sub_layers |
| 99 | stages |

**Current State**: Mixed implementations

**Impact**: Different entities have different internal numbering

---

## 4. Relative vs Absolute Layer Numbers

### Issue: L-1 Context Ambiguity

**Problem**: Research projects use "L-1" as a relative layer number, but the system was designed with absolute numbering.

**Example**:
```
0_layer_universal/           # Absolute L0
└── layer_-1_research/       # Relative L-1 (actually L1 absolutely)
    └── layer_-1_better_ai_system/
        └── layer_0/         # Relative L0 (L2 absolutely)
            └── layer_0_features/
```

**Confusion Points**:
- Is `layer_0` inside a research project at absolute L2 or relative L0?
- How should context gathering traverse L-1 boundaries?
- Which status files track which scope?

**Impact**:
- Unclear navigation rules
- Context gathering may miss relevant files
- Status tracking confusion

---

## 5. Documentation vs Implementation Drift

### Issue: Outdated References

**Examples Found**:

| Documentation Says | Implementation Has |
|-------------------|-------------------|
| "00 = request_gathering" | "00 = stage_registry" |
| "layer_1.02_sub_layers" | "layer_1_02_sub_layers" |
| "Stages 00-10" | "Stages 00-11" |
| No `.claude` folders | Full `.claude` structure |

**Locations with Drift**:
- `FLEXIBLE_LAYERING_SYSTEM.md` (v4.0 but references old patterns)
- `stage_definitions/` docs reference old numbering
- `layer_definitions/` docs predate registry system

**Impact**: Developers following docs create inconsistent structures

---

## 6. Sub-Layer Naming Pattern

### Issue: Plus Sign Ambiguity

**Pattern**: `sub_layer_N_05+_setup_dependant`

**Problem**:
- The `+` in `05+` is meant to indicate "05 and beyond"
- But some implementations interpret as literal "05+"
- Creates sorting/globbing issues

**Current State**:
- Some use `05+` literally
- Some create `05`, `06`, `07` separately
- No clear convention documented

---

## 7. Handoff Document Location

### Issue: Two Different Patterns

**Pattern A (Stages)**:
```
stage_N_XX_name/
└── hand_off_documents/
    ├── from_previous_stage.json
    └── to_next_stage.json
```

**Pattern B (Layers)**:
```
layer_N/
└── layer_N_01_manager_handoff_documents/
    ├── layer_N_00_to_universal/
    └── layer_N_01_to_specific/
```

**Problem**: Inconsistent naming (`hand_off_documents` vs `manager_handoff_documents`)

---

## 8. Registry Implementation Gaps

### Issue: Inconsistent Registry Usage

**Expected**:
- `layer_N_00_layer_registry/` at each layer
- `stage_0_00_stage_registry/` at stages

**Actual State**:
- Some layers have registries, others don't
- Registry content varies (some empty, some detailed)
- No standard schema defined

---

## 9. Status File Variations

### Issue: Inconsistent Status Schema

**Observed Variations**:
```json
// Variation A
{ "current_stage": "02_research", "progress_percent": 15 }

// Variation B
{ "stage": "research", "status": "in_progress" }

// Variation C
{ "stage_number": 2, "stage_name": "research", "completion": 0.15 }
```

**Impact**: Automation scripts must handle multiple formats

---

## 10. .claude Folder Integration

### Issue: Varying Completeness

**Expected Structure**:
```
.claude/
├── settings.json
├── agents/
├── commands/
├── skills/
├── hooks/
└── scripts/
```

**Current State**:
- Some stages have full structure (newly created)
- Reference implementation has minimal `.claude/`
- No standard for what each folder should contain

---

## Summary Matrix

| Issue | Severity | Scope | Fix Complexity |
|-------|----------|-------|----------------|
| Naming (dot vs underscore) | High | Framework-wide | Medium |
| Stage numbering | High | All stages | Medium |
| Layer component positions | Medium | All layers | Low |
| L-1 relative numbering | High | Research context | High |
| Documentation drift | Medium | All docs | Medium |
| Sub-layer + notation | Low | Sub-layers | Low |
| Handoff naming | Low | Handoff system | Low |
| Registry gaps | Medium | All entities | Medium |
| Status schema | Medium | All status files | Medium |
| .claude completeness | Low | All entities | Low |

---

## Next Steps

See `03_improvement_proposals.md` for proposed solutions.
