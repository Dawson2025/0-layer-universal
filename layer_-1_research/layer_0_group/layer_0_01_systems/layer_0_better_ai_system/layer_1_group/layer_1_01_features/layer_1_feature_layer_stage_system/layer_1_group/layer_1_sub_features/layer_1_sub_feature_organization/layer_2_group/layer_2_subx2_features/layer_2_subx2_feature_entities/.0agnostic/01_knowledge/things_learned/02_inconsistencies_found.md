---
resource_id: "0e43cb6d-f4f1-4699-b739-f2ed26af1959"
resource_type: "knowledge"
resource_name: "02_inconsistencies_found"
---
# Inconsistencies Found in Layer-Stage System

<!-- section_id: "67bbac42-32a9-4ac9-9385-9637116bc413" -->
## Date: 2026-01-25
<!-- section_id: "e1798d14-c1cd-47f8-80c3-6be09fa31f23" -->
## Source: Reference Implementation Analysis

---

<!-- section_id: "e2690b1a-c624-4ff8-b502-938c7b3ed18f" -->
## 1. Naming Convention Inconsistencies

<!-- section_id: "37769c29-202f-4dee-9dee-e4770d5756dd" -->
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

<!-- section_id: "1d2e788a-a753-445a-a097-fdcbeba0aeb0" -->
## 2. Stage Numbering Discrepancy

<!-- section_id: "91ac3220-f49c-42ec-aede-5a3c1663f7bc" -->
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

<!-- section_id: "c0383083-e511-4e6b-a214-d48a63882c6d" -->
## 3. Layer Component Numbering

<!-- section_id: "4f6109d4-d90a-4e22-bde5-b4936c0dcdcc" -->
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

<!-- section_id: "eb90120e-5765-478e-b3e3-ed838dccf272" -->
## 4. Relative vs Absolute Layer Numbers

<!-- section_id: "2f78c066-e4f2-4526-a4f5-9112e06cf966" -->
### Issue: L-1 Context Ambiguity

**Problem**: Research projects use "L-1" as a relative layer number, but the system was designed with absolute numbering.

**Example**:
```
0_layer_universal/           # Absolute L0
└── layer_-1_research/       # Relative L-1 (actually L1 absolutely)
    └── layer_-1_better_ai_system/
        └── layer_0_group/         # Relative L0 (L2 absolutely)
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

<!-- section_id: "7bf7d6b0-7000-4278-aefb-87a04a0d4802" -->
## 5. Documentation vs Implementation Drift

<!-- section_id: "6896a279-c1b0-4e6b-b266-0db5db7478f9" -->
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

<!-- section_id: "57ddad39-c54f-4902-9303-c7f2d9c538b6" -->
## 6. Sub-Layer Naming Pattern

<!-- section_id: "b57a33b7-229f-4dff-9fdb-90fed72c65c7" -->
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

<!-- section_id: "83d4406b-4536-42bc-83e0-949e0b49d59f" -->
## 7. Handoff Document Location

<!-- section_id: "fab7fc1b-86a8-4183-a78e-e1e0372a6a55" -->
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

<!-- section_id: "93f178b4-f77d-42cf-aac0-d4b2373b0255" -->
## 8. Registry Implementation Gaps

<!-- section_id: "e87706f8-0ae6-4ee9-a15e-5e180ab37941" -->
### Issue: Inconsistent Registry Usage

**Expected**:
- `layer_N_00_layer_registry/` at each layer
- `stage_0_00_stage_registry/` at stages

**Actual State**:
- Some layers have registries, others don't
- Registry content varies (some empty, some detailed)
- No standard schema defined

---

<!-- section_id: "c58d5889-5403-4736-bc0a-135df469a3cd" -->
## 9. Status File Variations

<!-- section_id: "2684eab4-f407-4b18-87c1-88d47c912da5" -->
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

<!-- section_id: "83e8d057-c4e5-4b56-bd44-2f3e32a62c86" -->
## 10. .claude Folder Integration

<!-- section_id: "5bc38348-d160-4aba-b9c0-7deb62402df1" -->
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

<!-- section_id: "7b71ed78-cbe6-4d1f-9e39-8830ab7a9f54" -->
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

<!-- section_id: "c8633e06-37a4-4970-bc28-807188a73097" -->
## Next Steps

See `03_improvement_proposals.md` for proposed solutions.
