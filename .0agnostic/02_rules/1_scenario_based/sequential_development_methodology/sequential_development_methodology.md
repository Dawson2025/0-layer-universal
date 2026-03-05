---
resource_id: "845ee9a2-f2ca-4c33-8dfc-96384c021ba8"
resource_type: "rule"
resource_name: "sequential_development_methodology"
---
# Sequential Development Methodology

**Level**: Universal (0)
**Applies To**: All multi-task projects with shared context
**Last Updated**: November 13, 2025
**Derived From**: DS250 Unit 3 parallel development issues

---

<!-- section_id: "c7335cae-5696-4766-977a-2a7e3c49a051" -->
## Purpose

This document establishes a universal methodology for approaching multi-task work to ensure consistency, quality, and efficiency.

**Core Insight**: When tasks share data, patterns, or context, sequential completion prevents inconsistencies that parallel development creates.

---

<!-- section_id: "4360d58a-019b-4841-81ab-748a9702fad4" -->
## The Problem: Parallel Development Pitfalls

<!-- section_id: "9c5ae2e2-7241-4a67-8e4c-c13b9aa68697" -->
### What Happens in Parallel Development

```
Start all tasks simultaneously
├── Task 1: Discover pattern A, implement fix X
├── Task 2: Discover pattern A independently, implement fix Y
├── Task 3: Don't discover pattern A, has bug
└── Task 4: Discover pattern B, but miss pattern A

Result: Inconsistent approaches, duplicated bugs, wasted effort
```

<!-- section_id: "2fd1c6e8-e1c6-433d-8db5-2f4b920deec1" -->
### Real-World Example (DS250 Unit 3)

**Parallel Approach**:
- Task 1: Fixed -999 sentinel, case-insensitive n/a handling
- Task 2: Independently discovered "Febuary" typo, fixed it, but duplicated -999 bug in wrong order
- Task 3: Had Febuary fix but different approach to other cleaning
- Task 4: Had Febuary fix but duplicated calculation-before-cleaning bug

**Consequence**:
- 3 out of 4 tasks required rework
- Negative values (-299.7) appeared in 2 tasks
- Analysis-visual mismatches in 2 tasks
- Inconsistent data cleaning approaches across all tasks

**Time Impact**:
- Parallel: Initial work (4 hours) + Debugging (2 hours) + Rework (3 hours) = 9 hours
- Sequential would have been: 5 hours total (with lessons propagating)

---

<!-- section_id: "41a559a6-3072-412f-b6bd-3bfb27cb335f" -->
## The Solution: Sequential Development

<!-- section_id: "e1a80816-37e8-468c-9e53-26e2c087e9a9" -->
### Core Principle

> **Complete each task fully before starting the next one.**
> Each task builds on lessons learned from previous tasks.

<!-- section_id: "fa5ce0a5-48dc-4432-8306-fa9aedb2a378" -->
### The Sequential Process

```
Task 1 (Complete) → Document learnings →
Task 2 (Apply Task 1 learnings + complete) → Document new learnings →
Task 3 (Apply accumulated learnings + complete) → Document new learnings →
Task 4 (Apply all learnings + complete)

Result: Consistent approaches, lessons propagate naturally, less rework
```

<!-- section_id: "52ea007f-b8e8-47a2-80dd-aeed051c7b3b" -->
### Standard Sequential Workflow

#### Step 1: Complete First Task

1. Read requirements for Task 1
2. Implement Task 1 completely
3. Test and verify Task 1
4. **Document discoveries and patterns**
5. ✅ Mark Task 1 as COMPLETE
6. **STOP. Do not proceed yet.**

**Key Questions After Task 1**:
- What data cleaning was needed?
- What edge cases were discovered?
- What patterns should be reused?
- What bugs were fixed?

#### Step 2: Apply Learnings to Task 2

1. **Review Task 1 documented learnings**
2. **Apply all Task 1 fixes/patterns from the start**
3. Read Task 2 requirements
4. Implement Task 2 with accumulated knowledge
5. Test and verify Task 2
6. **Document any NEW discoveries**
7. ✅ Mark Task 2 as COMPLETE
8. **STOP. Do not proceed yet.**

#### Step 3: Continue Pattern

For each subsequent task N:

1. **Review all learnings from Tasks 1 through N-1**
2. **Apply accumulated fixes/patterns**
3. Read Task N requirements
4. Implement with full context
5. Test and verify
6. Document new discoveries
7. ✅ Mark as COMPLETE
8. **STOP before next task**

---

<!-- section_id: "f24930d6-b44c-4132-8c1e-2ae233182a5b" -->
## Decision Framework: When to Use Sequential vs Parallel

<!-- section_id: "0a2cad7a-46e8-4738-a8f0-b0075d9fa6b1" -->
### Use Sequential When:

✅ **Tasks share data sources** (same dataset, same database)
✅ **Tasks share patterns** (similar operations, similar cleaning)
✅ **Tasks build conceptually** (Task 2 extends Task 1 concepts)
✅ **Quality is critical** (production work, published analysis)
✅ **Learning is involved** (new techniques, unfamiliar domain)
✅ **Data cleaning is involved** (always use sequential for data work)

**Examples**:
- Unit tasks in coursework (Unit 1 Task 1 → Task 2 → Task 3 → Task 4)
- Multi-phase data pipeline (Extract → Transform → Load)
- Iterative analysis (Explore → Model → Validate → Report)
- Tutorial/learning sequences (Lesson 1 → Lesson 2 → Lesson 3)

<!-- section_id: "fd824c45-4af7-4184-9f70-b4c1bba7dcd7" -->
### Use Parallel When:

✅ **Tasks are completely independent** (no shared context)
✅ **No shared data or patterns** (different datasets, different operations)
✅ **Simple, well-understood operations** (no discoveries expected)
✅ **Different team members own tasks** (isolated ownership)
✅ **Time-critical deadlines** (parallel required for speed)

**Examples**:
- Separate unrelated projects
- Documentation updates in different sections
- Independent feature additions to different modules
- Bug fixes in unrelated subsystems

<!-- section_id: "647075a0-3b40-40c1-9d91-43adbe5ee52c" -->
### Gray Area: When Parallel is Necessary for Related Tasks

If you **must** work in parallel on related tasks:

#### Mitigation Strategies

1. **Complete "foundation" task first** (e.g., data cleaning baseline)
2. **Document patterns explicitly** before starting parallel work
3. **Create shared modules/imports** that all tasks use
4. **Test foundation thoroughly** before copying patterns
5. **Final review pass** across ALL tasks before publishing

---

<!-- section_id: "7c01dd48-5106-45f7-87be-4c55aa7ae1df" -->
## Implementation Best Practices

<!-- section_id: "0c57d1e9-b495-4bbc-b7d6-d15c714fa1a3" -->
### 1. Task Tracking

Use explicit task tracking with clear status:

```markdown
[x] Task 1: Data Cleaning - COMPLETE (documented patterns below)
    - Patterns: -999 → NaN, "Febuary" → "February", case-insensitive n/a
    - Edge cases: Empty strings in airport_name
[x] Task 1 learnings documented
[ ] Review Task 1 patterns before starting Task 2
[ ] Task 2: Weather Analysis - Apply Task 1 patterns first
...
```

<!-- section_id: "25f78066-fd2a-4f6f-bfa7-66b59ef353c5" -->
### 2. Pattern Documentation

After each task, explicitly document:

**What I discovered**:
- New edge cases (e.g., -999 sentinel values)
- New patterns (e.g., typo corrections needed)
- New best practices (e.g., clean before calculate)

**What I fixed**:
- Specific code changes (e.g., .replace(-999, np.nan))
- Reasoning (e.g., prevents negative values in calculations)

**What to apply to next task**:
- Checklist of patterns to copy
- Code snippets to reuse
- Verification steps

<!-- section_id: "593019b2-f5c6-4dd9-8d5a-5a3ae883df5f" -->
### 3. AI Agent Instructions

When working with AI assistants on multi-task work:

**DO**:
- ✅ Ask "Should we complete Task 1 fully before Task 2?"
- ✅ Request documentation of learnings after each task
- ✅ Explicitly ask for previous patterns to be applied to new tasks
- ✅ Use task tracking tools to maintain status
- ✅ Request verification before moving to next task

**DON'T**:
- ❌ Start all tasks simultaneously
- ❌ Skip documenting discoveries from early tasks
- ❌ Assume later tasks automatically inherit early fixes
- ❌ Render/publish all tasks before individual verification

---

<!-- section_id: "d983a995-5ade-424f-9fb7-11732c1400da" -->
## Benefits of Sequential Workflow

<!-- section_id: "b26431c5-174d-4c00-9cee-ff9e211318d1" -->
### Quality Benefits

- **Consistency**: All tasks use same patterns
- **Completeness**: Edge cases caught early and propagated
- **Correctness**: Fewer bugs through accumulated learning
- **Verification**: Issues caught before propagation

<!-- section_id: "e8e84b79-58a4-4cef-88be-2ddecade9b83" -->
### Efficiency Benefits

- **Less rework**: Fix once in Task 1, apply everywhere
- **Faster debugging**: Incremental changes easier to trace
- **Clear progress**: Linear advancement through tasks
- **Knowledge building**: Each task builds on previous understanding

<!-- section_id: "3f45dd3b-fd85-4353-bff1-0340ab0a8851" -->
### Learning Benefits

- **Progressive understanding**: Build knowledge step by step
- **Pattern recognition**: See patterns emerge across tasks
- **Deep comprehension**: Understand WHY not just WHAT
- **Documentation habit**: Natural to document as you learn

---

<!-- section_id: "d5fac1c3-0240-41d4-9e50-281ff4cf8cc2" -->
## Case Study: DS250 Unit 3

<!-- section_id: "180144d4-b08c-44b5-b6e4-2ff904098171" -->
### Background

Four related tasks analyzing flight delay data from the same dataset.

<!-- section_id: "b6ab6040-6b1e-4ba8-ae1a-c8b1eb3a6c43" -->
### Parallel Approach (What Happened)

**Timeline**:
1. Created all 4 templates simultaneously
2. Rendered all 4 together
3. Published all 4 at once
4. User reviewed and found issues across multiple tasks

**Issues Found**:
- Calculation-before-cleaning bugs in Tasks 2 and 4 (negative values)
- Chart rendering bugs in Task 4 (wrong scale)
- Analysis-visual mismatches in Tasks 2 and 3
- Inconsistent data cleaning across all tasks

**Rework Required**:
- Fixed Task 2 and Task 4 calculation order
- Fixed Task 4 chart rendering
- Updated Task 2 and Task 3 analyses
- Re-rendered and re-published multiple tasks

<!-- section_id: "7a8e087a-1236-4c9f-89ed-01b7f11a997e" -->
### Sequential Approach (Should Have Done)

**What Would Have Happened**:

**Task 1 (Data Cleaning)**:
- Discover -999 sentinel issue
- Discover "Febuary" typo
- Discover case-insensitive n/a needed
- Document: "Clean -999 BEFORE calculations"
- ✅ COMPLETE

**Task 2 (Weather Analysis)**:
- Apply Task 1 cleaning patterns
- Implement weather calculations with clean data
- No negative values (cleaned first!)
- ✅ COMPLETE with learnings applied

**Task 3 (Best Month)**:
- Apply Task 1 & 2 patterns
- Generate chart, examine data, write matching analysis
- ✅ COMPLETE with verified analysis

**Task 4 (Delay Comparison)**:
- Apply all previous patterns
- Use stat="identity" from start (learned visualization best practices)
- ✅ COMPLETE with all lessons applied

**Result**: All tasks consistent, no rework needed

---

<!-- section_id: "400d4f74-f323-4442-b0c3-1444ece73116" -->
## Quick Reference

<!-- section_id: "927dda6d-6d33-410c-863e-6354b73b9721" -->
### Sequential Workflow Checklist

**Before Starting Multi-Task Work**:
- [ ] Are these tasks related? (same data, similar operations)
- [ ] If yes → commit to sequential workflow
- [ ] Create task order list
- [ ] Define completion criteria for each task

**During Each Task**:
- [ ] Review ALL previous task learnings
- [ ] Apply known fixes/patterns from the start
- [ ] Complete task fully (code + test + verify)
- [ ] Document new discoveries
- [ ] Mark COMPLETE before next task

**After Task Completion**:
- [ ] Verify all fixes are in place
- [ ] Test edge cases from earlier tasks
- [ ] Update documentation
- [ ] ONLY THEN proceed to next task

<!-- section_id: "50820e64-19f7-4701-9ddb-d8ea0dfea62c" -->
### Red Flags (Parallel Work on Related Tasks)

🚩 Starting multiple related tasks simultaneously
🚩 Not documenting discoveries from early tasks
🚩 Assuming later tasks don't need early fixes
🚩 Rendering/publishing all tasks before individual testing
🚩 Finding same bug in multiple tasks during review

---

<!-- section_id: "945d8b9c-db4c-4518-a1a2-dff80726cca3" -->
## Integration with Other Methodologies

<!-- section_id: "bece7729-089b-42e5-8e70-640e0e18b11d" -->
### Agile/Scrum

Sequential development complements agile:
- Each task = one story/ticket
- Complete story before next sprint item
- Document learnings in story notes
- Apply patterns to subsequent stories

<!-- section_id: "0632f708-b935-4fc4-93c5-a6e9aabc4d1b" -->
### Test-Driven Development (TDD)

Sequential enhances TDD:
- Task 1: Write tests, discover edge cases
- Task 2+: Apply Task 1's test patterns
- Tests become more comprehensive with each task

<!-- section_id: "cfea7c9c-331d-4cff-85b2-0633085fa733" -->
### Continuous Integration

Sequential supports CI/CD:
- Each task passes CI before next starts
- Build confidence incrementally
- Issues caught early before propagation

---

<!-- section_id: "d58f7376-aa54-4ddc-802e-53a0e018819c" -->
## Summary

<!-- section_id: "c8084a62-4afc-4bb4-b3ba-63e901c5121a" -->
### The Core Rule

**If tasks share data, patterns, or context → always work sequentially.**

<!-- section_id: "ccc0893d-4498-4677-a18e-bf1b9c6d6f5c" -->
### The Core Process

```
Complete → Document → Review → Apply → Repeat
```

<!-- section_id: "b0f26b98-580f-43ee-b063-9276aba9961c" -->
### The Core Benefit

**Fix once, apply everywhere** vs **Fix same issue multiple times**

<!-- section_id: "6a037e73-842a-4914-8c66-4bf261da4147" -->
### The Core Principle

**"Measure twice, cut once" applies to multi-task work.**

The extra time spent completing tasks sequentially is recovered (and more) by avoiding rework, inconsistencies, and bugs.

---

<!-- section_id: "981db2dd-714d-433f-8bc2-42bce9dd07a4" -->
## Related Documentation

- Data Visualization Principles (trickle_down_0.75_universal_tools)
- Project-specific sequential workflow guidelines
- Task tracking and documentation standards

---

**Created**: November 13, 2025
**Source**: DS250 Unit 3 parallel development lessons learned
**Status**: Active universal methodology
**Applies To**: All multi-task work with shared context
