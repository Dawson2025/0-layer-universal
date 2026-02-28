# Automated Traversal Instructions

**Date**: 2026-01-30
**Stage**: stage_-1_03_instructions
**Status**: FINISHED - Ready for Design
**Revision**: 1.0

---

## Overview

Your system has 5,930+ directories nested across layers 1-5+. Manual traversal ("read this file, then that file") doesn't scale.

**Goal**: Enable AI agents to automatically discover relevant context in ~3-5 steps instead of requiring manual guidance.

---

## The Problem

**At 5,930 nodes, these fail:**

- ❌ "Read all CLAUDE.md files" - Too many files
- ❌ "Search through layer_1/" - 1000+ entries
- ❌ "Find anything about math" - Could be layer_3, layer_4, or layer_5
- ❌ Manual index - Goes stale constantly

**Solution**: Hierarchical semantic index with LLM-based traversal.

---

## Solution: 0INDEX.md at Branching Points

### What is 0INDEX.md?

A **semantic index** placed at directories where users need help navigating children.

**Purpose**:
- Helps AI agents understand what each child directory contains
- Enables LLM to pick "most relevant child" given a query
- Replaces manual navigation with automated search

**Content**: Short description of each child and keywords

### Where to Place 0INDEX.md

**NOT everywhere** (5,930 files is overkill). **AT BRANCHING POINTS:**

```
layer_1/
├── 0INDEX.md ← Place here (parent of projects)
├── layer_1_projects/
│   ├── 0INDEX.md ← Place here (parent of projects)
│   ├── layer_1_project_school/
│   │   ├── 0INDEX.md ← Place here (parent of layers 2-5)
│   │   ├── layer_2/
│   │   │   ├── 0INDEX.md ← Place here (parent of features/components)
│   │   │   ├── layer_2_features/
│   │   │   │   ├── 0INDEX.md ← Place here (parent of features)
│   │   │   │   ├── layer_2_feature_knowledge_tracking/
│   │   │   │   └── layer_2_feature_assessment_system/
│   │   │   └── layer_2_components/
│   │   │       ├── 0INDEX.md ← Place here
│   │   │       ├── layer_2_component_api/
│   │   │       └── layer_2_component_ui/
```

**Rule of thumb**: Place 0INDEX.md when a directory has multiple children that are not all equally relevant.

### 0INDEX.md Template

```markdown
# 0INDEX.md - layer_X_projects

**Purpose**: Navigate to projects

## Children

| Directory | Description | Keywords |
|-----------|-------------|----------|
| `layer_1_project_school` | School project infrastructure (courses, assignments, progress tracking) | school, courses, students, grades, assessments |
| `layer_1_project_work` | Work-related project tools and systems | work, projects, tasks, teams, collaboration |

## Navigation Rules

- **For course-related work**: Go to `layer_1_project_school/`
- **For work projects**: Go to `layer_1_project_work/`
- **If unsure**: Check both, their CLAUDE.md files explain scope

## See Also

- Full project list: `../../../layer_-1_research/`
- Universal rules: `../../../layer_0_group/`
```

### 0INDEX.md Content Guidelines

**Keep it SHORT:**
- ✅ "School project: course, student tracking" (1 sentence)
- ❌ "This project contains features for tracking school activities including courses, students, assignments..." (too verbose)

**Include Keywords:**
- ✅ Keywords: school, courses, students, grades, assessments
- ❌ No keywords (agent can't match queries)

**Focus on Differentiation:**
- ✅ What makes THIS child different from siblings?
- ❌ Generic description that could apply to everything

---

## Implementation: Three Phases

### Phase 1: Static Indices (IMMEDIATE)

Create 0INDEX.md files manually at key branching points.

**Locations to start:**

```
~/dawson-workspace/code/0_layer_universal/layer_1/0INDEX.md
~/dawson-workspace/code/0_layer_universal/layer_1/layer_1_projects/0INDEX.md
~/dawson-workspace/code/0_layer_universal/layer_1/layer_1_projects/layer_1_project_school/0INDEX.md
~/dawson-workspace/code/0_layer_universal/layer_1/layer_1_projects/layer_1_project_school/layer_2/0INDEX.md
```

**Time estimate**: 30 minutes to identify key branching points and write indices

**Deliverable**: 8-15 0INDEX.md files at decision points

### Phase 2: Manual Traversal Helper (NEXT)

Create a Skill that helps agents navigate using 0INDEX.md files.

**Skill name**: `/find`

**Inputs**:
- Query: "Where is the math course?"
- Starting point: "layer_1" (or "root")

**Process**:
1. Read 0INDEX.md at starting point
2. Extract children descriptions + keywords
3. Ask LLM: "Which child best matches query?"
4. Recursively descend into selected child
5. Repeat until leaf or exact match found

**Example execution**:

```
Query: "Find math course components"
Location: ~/layer_1/

Step 1: Read layer_1/0INDEX.md
  Children: [layer_1_projects, layer_-1_research]
  Keywords: projects|research

Step 2: LLM picks "layer_1_projects" (keyword: "courses")

Step 3: Read layer_1/layer_1_projects/0INDEX.md
  Children: [layer_1_project_school, layer_1_project_work]
  Keywords: school|work

Step 4: LLM picks "layer_1_project_school" (keyword: "school", "course")

Step 5: Read layer_1_project_school/0INDEX.md
  Children: [layer_2, layer_3, ...]

Step 6: LLM picks "layer_2" (keyword: "features")

Step 7: Read layer_2/0INDEX.md
  Children: [layer_2_feature_math_curriculum, layer_2_feature_assessment_system]
  Keywords: math|assessment

Step 8: LLM picks "layer_2_feature_math_curriculum"

Step 9: Descend to layer_2_feature_math_curriculum/layer_3/0INDEX.md

Step 10: Find "layer_3_feature_math_problems" (exact match)
  Result: layer_1_project_school/layer_2/layer_2_features/layer_2_feature_math_curriculum/layer_3_features/layer_3_feature_math_problems/
```

**Deliverable**: Skill that automates the above traversal

### Phase 3: Full Automation (ADVANCED)

If Phase 2 works well, add:
- **Indexed search**: Pre-compute all keywords, enable prefix search
- **Relevance ranking**: Return top 3 matches instead of just best
- **Fuzzy matching**: "math" matches "mathematical"
- **Cache 0INDEX.md** results to avoid re-reading

---

## CLAUDE.md Integration

Each agent should know how to find things:

```markdown
## Discovery Workflow

### Quick Find (Manual)

```bash
# Navigate manually using 0INDEX.md files:
cat layer_1/0INDEX.md                          # See top-level projects
cat layer_1/layer_1_projects/0INDEX.md         # See which project
cat layer_1/layer_1_projects/layer_1_project_school/0INDEX.md  # See layers
```

### Automated Find

```bash
# Use /find skill for automatic traversal:
/find "math course components"      # Query
/find "math course components" from "layer_1" # With starting point
/find "where is assessment system?"
```

### Manual Override

If /find doesn't work:
1. Read 0INDEX.md at current level
2. Pick most relevant child based on keywords
3. Descend and repeat
4. Log where /find failed for improvement
```

---

## Success Criteria

✅ **Automated traversal is working when:**

1. Agent can find any component in 5 steps or fewer
2. Keywords in 0INDEX.md enable LLM to pick correct child
3. Traversal is consistent (same query returns same path)
4. Agent can navigate without human guidance

❌ **Needs improvement if:**

1. Agent takes >5 steps to find things
2. Keywords are ambiguous or misleading
3. Agent picks wrong child (indicates bad keyword match)
4. New components added but indices not updated

---

## Maintenance

### When to Update 0INDEX.md

**Update when:**
- New child directory added
- Child's purpose changed
- Keywords no longer match content

**Check quarterly:**
- Read all 0INDEX.md files
- Verify keywords still match children
- Update if stale

### Versioning

Add version to each 0INDEX.md:

```markdown
# 0INDEX.md - layer_2_features

**Version**: 1.2.0
**Last Updated**: 2026-01-30
**Maintainer**: Research Agent

...
```

Increment version when updating.

---

## Comparison to SHIMI

Your implementation vs. SHIMI's:

| Aspect | SHIMI | Your Implementation |
|--------|-------|-------------------|
| Hierarchy | Yes (recursive) | Yes (recursive) |
| Semantic summaries | Yes (CRDT-based) | Yes (markdown tables) |
| LLM-based traversal | Yes (required) | Yes (via /find skill) |
| Network sync | Yes | Not needed (filesystem) |
| Decentralized | Yes | No (centralized filesystem) |

**Key difference**: SHIMI optimizes for decentralized multi-agent sync. You optimize for hierarchical organization in shared filesystem.

---

## Expected Benefits

### Discovery Speed
- **Before**: "Find X" requires manual reading, 10+ minutes
- **After**: "Find X" with /find skill, 30 seconds

### Scalability
- **At 100 nodes**: Manual still works
- **At 1,000 nodes**: Manual gets slow, automated essential
- **At 5,930 nodes**: Automated is mandatory

### Consistency
- **Same query** always produces **same result**
- No ambiguity about where things are
- New agents can discover context independently

---

## Implementation Checklist

- [ ] Identify all branching points (directories with multiple important children)
- [ ] Create 0INDEX.md for each branching point
- [ ] Test manual navigation using 0INDEX.md
- [ ] Design /find skill algorithm
- [ ] Implement /find skill
- [ ] Test /find with 10 sample queries
- [ ] Add traversal instructions to each CLAUDE.md
- [ ] Document keyword guidelines
- [ ] Set up quarterly maintenance schedule

