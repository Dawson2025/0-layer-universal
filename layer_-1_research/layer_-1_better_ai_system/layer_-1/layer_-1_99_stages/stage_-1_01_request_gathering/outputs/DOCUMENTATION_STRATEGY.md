# Documentation Strategy: Distributed Infrastructure in Request Gathering

**Date**: 2026-01-27
**Question Answered**: "Which stage(s) should we document the Syncthing-based distributed infrastructure?"

---

## Answer: Stage 01 (Request Gathering) in Two Locations

Your distributed infrastructure is documented in **stage_-1_01_request_gathering** in two key places:

### 1. **In `outputs/overview/`** → `existing_infrastructure.md`

**Purpose**: Background context for why these requirements exist

**Contains**:
- Current Syncthing setup (what's synced, which machines)
- How it works (session flow, sync latency)
- Current capabilities (what works well)
- Existing patterns (universal rules, handoffs, CLAUDE.md cascade)
- Gaps (what's missing: emergency mode, multi-user, conflict resolution)
- Integration with Tree of Needs (how infrastructure addresses each requirement)

**Audience**: Anyone wanting to understand the existing system and why the requirements were created

**Location in Workflow**: Read BEFORE diving into the Tree of Needs to understand the context

---

### 2. **In `outputs/requests/tree_of_needs/02_continuous/need_06_universal_rules_and_cross_device_access/`** → `existing_implementation.md`

**Purpose**: Connect the existing working infrastructure to the specific requirement

**Contains**:
- Summary of current setup
- What already works (and why)
- Specific gaps this need addresses
- How the requirement builds on current infrastructure
- Implementation path (phases 1-5 with effort estimates)
- Testing checklist against current system

**Audience**: Someone implementing `need_06` - shows what's already there and what to add

**Location in Workflow**: Read ALONGSIDE `requirements.md` to see both what's needed and what already exists

---

## Documentation Structure

```
stage_-1_01_request_gathering/outputs/
│
├── overview/                                 ← "Why do we need this?"
│   ├── README.md                            ← Overview index
│   ├── existing_infrastructure.md           ← Current system (BACKGROUND)
│   ├── system_vision.md                     ← Future vision
│   ├── consolidated_requirements.md         ← All requirements summary
│   ├── implementation_roadmap.md            ← Priority plan
│   └── dependencies.md                      ← How requirements relate
│
└── requests/tree_of_needs/                  ← "What exactly do we need?"
    └── 00_seamless_ai_collaboration/
        └── 02_continuous/
            └── need_06_universal_rules_and_cross_device_access/
                ├── README.md                ← Need overview (NEW)
                ├── requirements.md          ← Full spec (15 acceptance criteria)
                └── existing_implementation.md ← Current system analysis (NEW)
```

---

## Key Relationships

### Overview → Need Flow

```
existing_infrastructure.md (overview)
  ↓
  "We have Syncthing syncing universal rules"
  "Rules work across machines via CLAUDE.md cascade"
  "But we're missing emergency mode, multi-user support, etc."
  ↓
need_06/requirements.md
  ↓
  "Formally specify all the requirements to close these gaps"
  ↓
need_06/existing_implementation.md
  ↓
  "Here's exactly what already works and what's missing"
```

### Reading Order (Recommended)

1. **First time**: `overview/README.md` → `existing_infrastructure.md` → `need_06/README.md` → `need_06/requirements.md`
2. **Implementing**: `need_06/existing_implementation.md` → `need_06/requirements.md` → back to `overview/existing_infrastructure.md` for context
3. **Quick reference**: `overview/existing_infrastructure.md` (what we have) + `need_06/existing_implementation.md` (what we need)

---

## Why This Structure?

### Separation of Concerns

- **`outputs/overview/`**: Provides CONTEXT for why requirements exist (historical, architectural)
- **`outputs/requests/tree_of_needs/`**: Specifies REQUIREMENTS in formal detail

### Single Source of Truth

- Current infrastructure details only in `existing_infrastructure.md` (not repeated elsewhere)
- Requirements only in `need_06/requirements.md` (not duplicated)
- Both documents reference each other to show relationships

### Staged Discovery

- New reader starts with `overview/` to get the big picture
- Detailed implementer goes to specific `need_06/` documents for specifics
- No requirement to read everything before understanding what's needed

### Flexibility for Future

- New requirements can reference `existing_infrastructure.md` without duplication
- Infrastructure doc can be updated once, automatically informs all uses
- Stage 02 (Research) can build upon this documentation

---

## What Gets Documented Where

### ✓ In `outputs/overview/existing_infrastructure.md`

- Current Syncthing setup
- Which machines are synced
- What directories are synced
- How AI tools currently access the system
- Existing patterns that work
- Limitations and gaps
- Integration with Tree of Needs

### ✓ In `outputs/requests/tree_of_needs/need_06/existing_implementation.md`

- How current system inspired the requirement
- What parts of the requirement already work
- Implementation path to complete the requirement
- Acceptance criteria for testing

### ✓ In `outputs/requests/tree_of_needs/need_06/requirements.md`

- Full formal requirements (15 acceptance criteria)
- Technical specifications
- Access control model
- Multi-user considerations
- Cross-platform context
- Open questions

### ✗ NOT Documented Here (Belongs in Stage 02)

- Why Syncthing was chosen vs. alternatives
- Technical analysis of sync protocols
- Comparison with other distributed systems
- Architectural trade-offs
- Performance benchmarks

(These belong in `stage_-1_02_research/outputs/` where research analysis happens)

---

## Connection to System Context Hierarchy

This documentation reflects the **system context hierarchy** research:

- **Global CLAUDE.md**: `~/.claude/CLAUDE.md` and `~/.../CLAUDE.md` files
- **Workspace CLAUDE.md**: `/home/dawson/dawson-workspace/CLAUDE.md` (sync awareness)
- **Code CLAUDE.md**: `/home/dawson/dawson-workspace/code/CLAUDE.md`
- **System CLAUDE.md**: `/home/dawson/dawson-workspace/code/0_layer_universal/CLAUDE.md` (embedded rules)

Each level provides cascading context. The `existing_infrastructure.md` explains how this cascade works across machines.

See also: `stage_-1_02_research/outputs/01_understanding_in_progress/by_topic/system_context_hierarchy_research.md`

---

## Next Steps

### For Stage 02 (Research)

Research should now:
1. Read `existing_infrastructure.md` to understand current system
2. Research each gap (emergency mode, multi-user, conflict resolution) separately
3. Document findings in `stage_-1_02_research/outputs/by_need/need_06/`
4. Recommend approaches for each gap

### For Stage 04 (Design)

Design should:
1. Take research findings from Stage 02
2. Reference `existing_infrastructure.md` and `need_06/existing_implementation.md`
3. Design system-wide architecture that:
   - Preserves what works (Syncthing sync, CLAUDE.md cascade)
   - Fills gaps (emergency mode, multi-user, conflict resolution)
   - Extends to system locations (`/etc/`, `/opt/`, `/var/opt/`)

### For Stage 06 (Development)

Implementation should:
1. Phase 1: Formalize current system
2. Phase 2: Add emergency mode
3. Phase 3: Add multi-user support
4. Phase 4: Add conflict resolution
5. Phase 5: Standardize system-wide locations

---

## Summary

Your question was: **"Which stages should we document the distributed infrastructure?"**

**Answer**:
- **Stage 01 (Request Gathering)** documents it in TWO interconnected places
- `outputs/overview/existing_infrastructure.md` provides CONTEXT and BACKGROUND
- `outputs/requests/tree_of_needs/need_06/existing_implementation.md` connects infrastructure to REQUIREMENTS

This structure ensures:
- ✓ Existing infrastructure is formally documented
- ✓ Clear connection between what exists and what's needed
- ✓ Future stages can build upon this documentation
- ✓ No duplication or contradictions
- ✓ Easy to understand and navigate

