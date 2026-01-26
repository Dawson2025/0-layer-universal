# stage_-1_01_request_gathering

## Purpose
Collect and clarify requirements from stakeholders for improving the AI system.

## Context
- **Project**: better_ai_system
- **Layer**: -1 (Research)
- **Stage**: 01 - Request Gathering
- **Status**: Active
- **Tree of Needs Version**: 1.4.0 (DAG structure)

---

## Tree of Needs (Primary Organization)

Requirements are organized as a **Tree of Needs** branching from a single root goal.

```
outputs/requests/tree_of_needs/
├── _meta/                               Future-proofing docs
│   ├── PRINCIPLES.md                    Guiding principles (P1-P5)
│   ├── EXTENSION_GUIDE.md               How to extend the tree
│   ├── DEPENDENCIES.md                  Need dependency map + shared needs
│   ├── CHANGELOG.md                     Version history
│   └── VERSION.md                       Versioning policy
│
└── 00_seamless_ai_collaboration/        ROOT NEED
    ├── 01_capable/                      "Can AI do the work?"
    │   ├── need_01_persistent_knowledge
    │   ├── need_02_scalable_context
    │   ├── need_03_discoverable
    │   └── need_04_multimodal ⟷         (shared with 05_engaging)
    ├── 02_continuous/                   "Does work keep going?"
    │   ├── need_01_tool_portable
    │   ├── need_02_session_resilient
    │   ├── need_03_failure_recoverable
    │   ├── need_04_evolvable
    │   └── need_05_cross_platform
    ├── 03_trustworthy/                  "Can I trust AI?"
    │   ├── need_01_rule_compliant
    │   ├── need_02_predictable
    │   └── need_03_bounded
    ├── 04_observable/                   "Can I see what's happening?"
    │   ├── need_01_transparent
    │   ├── need_02_debuggable
    │   └── need_03_auditable
    └── 05_engaging/                     "Is it enjoyable?"
        └── need_01_multimodal ⟷         (shared with 01_capable)
```

### The Four Branches

| Branch | Question | Needs |
|--------|----------|-------|
| **01_capable** | Can AI do the work? | persistent_knowledge, scalable_context, discoverable, multimodal ⟷ |
| **02_continuous** | Does work keep going? | tool_portable, session_resilient, failure_recoverable, evolvable, cross_platform |
| **03_trustworthy** | Can I trust AI? | rule_compliant, predictable, bounded |
| **04_observable** | Can I see what's happening? | transparent, debuggable, auditable |
| **05_engaging** | Is it enjoyable? | multimodal ⟷ |

⟷ = Shared need (multimodal belongs to both 01_capable and 05_engaging)

### Guiding Principles

| Principle | Summary |
|-----------|---------|
| **P1: Future-Proof** | Designed to evolve with AI technology |
| **P2: Technology Agnostic** | No dependency on specific AI tools |
| **P3: Incremental Adoption** | Adoptable piece by piece |
| **P4: Human-AI Partnership** | AI augments, doesn't replace judgment |
| **P5: Simplicity** | Simple solutions over clever ones |

---

## Quick Navigation

### Start Here
1. **Understand the vision**: `outputs/requests/tree_of_needs/00_seamless_ai_collaboration/README.md`
2. **See principles**: `outputs/requests/tree_of_needs/_meta/PRINCIPLES.md`
3. **Check dependencies**: `outputs/requests/tree_of_needs/_meta/DEPENDENCIES.md`

### Find a Specific Need
```
outputs/requests/tree_of_needs/00_seamless_ai_collaboration/
  └── [branch]/[need]/requirements.md
```

Example: `01_capable/need_01_persistent_knowledge/requirements.md`

### Extend the Tree
See: `outputs/requests/tree_of_needs/_meta/EXTENSION_GUIDE.md`

---

## Skills Available

| Skill | Purpose |
|-------|---------|
| `/01_request_gathering-workflow` | General request gathering workflow |
| `/tree-of-needs-status` | Check Tree of Needs status and coverage |
| `/add-need` | Add a new need to the tree |
| `/check-dependencies` | Verify need dependencies |

---

## Working with the Tree of Needs

### Reading Requirements
1. Start with the root: `tree_of_needs/00_seamless_ai_collaboration/README.md`
2. Navigate to relevant branch (01_capable, 02_continuous, etc.)
3. Read specific need's `requirements.md`
4. Check `_meta/DEPENDENCIES.md` for related needs

### Adding a New Need
1. Determine which branch it belongs to
2. Follow `_meta/EXTENSION_GUIDE.md` template
3. Create `need_NN_name/requirements.md`
4. Update branch README
5. Update `_meta/DEPENDENCIES.md`
6. Update `_meta/CHANGELOG.md`

### Modifying a Need
1. Update the `requirements.md` file
2. Bump version in the file header
3. Update `_meta/CHANGELOG.md`
4. Check if dependencies changed

---

## Key Metrics

- **Tree Version**: 1.2.0
- **Total Branches**: 5
- **Total Needs**: 15
- **Guiding Principles**: 5

---

## Next Stage

When request gathering is complete, transition to **Stage 02: Research** to explore solutions.

See: `../stage_-1_02_research/`

---

## Related Documents

- Project overview: `../../CLAUDE.md`
- Tree of Needs: `outputs/requests/tree_of_needs/README.md`
- Meta docs: `outputs/requests/tree_of_needs/_meta/`
