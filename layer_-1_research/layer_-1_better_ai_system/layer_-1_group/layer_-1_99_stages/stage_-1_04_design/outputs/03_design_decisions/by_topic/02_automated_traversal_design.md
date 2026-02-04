# Automated Traversal System Design

**Date**: 2026-01-30
**Stage**: stage_-1_04_design
**Status**: FINISHED - Ready for Planning
**Revision**: 1.0

---

## Architecture Overview

```
┌───────────────────────────────────────────────────────────────────┐
│                   Automated Traversal System                      │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │                     /find Skill                               │ │
│  │                                                               │ │
│  │  Input: Query string                                         │ │
│  │  Example: "Find math course components"                      │ │
│  └────────────────────────┬────────────────────────────────────┘ │
│                           │                                      │
│                           ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │               Query Preprocessor                             │ │
│  │  - Remove common words: "the", "a", "is"                    │ │
│  │  - Extract keywords: ["math", "course", "components"]       │ │
│  │  - Tokenize for matching                                    │ │
│  └────────────────────────┬────────────────────────────────────┘ │
│                           │                                      │
│                           ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │              Index Reader (Hierarchical)                     │ │
│  │                                                               │ │
│  │  Current level: ~/layer_1/0INDEX.md                          │ │
│  │  ├─ layer_1_projects (keywords: school, work)               │ │
│  │  └─ layer_-1_research (keywords: research)                  │ │
│  └────────────────────────┬────────────────────────────────────┘ │
│                           │                                      │
│                           ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │             LLM-Based Child Selector                         │ │
│  │                                                               │ │
│  │  Input: Query keywords + child descriptions                 │ │
│  │  Output: Best matching child directory                      │ │
│  │                                                               │ │
│  │  Prompt: "Query: 'Find math courses'                        │ │
│  │           Which child is most relevant?                     │ │
│  │           - layer_1_projects (school, work)                │ │
│  │           - layer_-1_research (research)"                  │ │
│  │  Answer: "layer_1_projects (matches 'school')"             │ │
│  └────────────────────────┬────────────────────────────────────┘ │
│                           │                                      │
│                           ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │           Recursive Descent Controller                       │ │
│  │                                                               │ │
│  │  if (at leaf directory):                                    │ │
│  │    return current_path                                      │ │
│  │  else:                                                       │ │
│  │    next_child = select_best_child(query, children)         │ │
│  │    recurse(query, next_child)                              │ │
│  │                                                               │ │
│  │  Max depth: 10 levels                                       │ │
│  │  Max retries: 3 (if selector keeps picking bad child)      │ │
│  └────────────────────────┬────────────────────────────────────┘ │
│                           │                                      │
│                           ▼                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │              Result Validator                                │ │
│  │  - Verify path exists                                       │ │
│  │  - Verify has CLAUDE.md or relevant content                │ │
│  │  - Return with confidence score                            │ │
│  └────────────────────────┬────────────────────────────────────┘ │
│                           │                                      │
│                           ▼                                      │
│                    Output: Path                                  │
│         Example: ~/layer_1/layer_1_projects/                    │
│         layer_1_project_school/layer_2/layer_2_features/        │
│         layer_2_feature_math_curriculum/layer_3_features/       │
│         layer_3_feature_math_problems/                          │
│                                                                    │
└───────────────────────────────────────────────────────────────────┘
```

---

## Component 1: Query Preprocessor

### Purpose
Convert free-form query into structured keywords for matching.

### Design

```
Function: preprocess_query(query_string):
  // Remove stopwords
  stopwords = ["the", "a", "an", "is", "are", "in", "at", "to", "for"]
  words = query_string.lower().split()
  keywords = [w for w in words if w not in stopwords]

  // Handle common abbreviations
  keywords = replace(keywords, "math", ["math", "mathematics"])
  keywords = replace(keywords, "cs", ["cs", "computer science"])

  // Dedup
  keywords = list(set(keywords))

  // Sort by length (longer words usually more specific)
  keywords.sort(key=len, reverse=True)

  return keywords
```

**Example**:

```
Input: "Find me the math course components"
Stopwords removed: ["find", "math", "course", "components"]
Deduped: ["math", "course", "components", "find"]
Output: ["math", "course", "components", "find"]
```

---

## Component 2: Index Reader

### Purpose
Read 0INDEX.md at current directory and extract child descriptions.

### Design

```
Function: read_index(directory_path):
  index_file = directory_path + "/0INDEX.md"

  if not exists(index_file):
    return {"children": [], "description": "No index found"}

  content = read_file(index_file)

  // Extract "Children" section (markdown table)
  children_section = extract_section(content, "## Children")

  // Parse table: | Directory | Description | Keywords |
  children = []
  for row in parse_table(children_section):
    child = {
      "name": row["Directory"],
      "description": row["Description"],
      "keywords": row["Keywords"].split(","),  // CSV list
      "full_path": directory_path + "/" + row["Directory"]
    }
    children.append(child)

  return children
```

**0INDEX.md Format** (Assumed):

```markdown
# 0INDEX.md - [Directory Name]

## Children

| Directory | Description | Keywords |
|-----------|-------------|----------|
| `layer_1_projects` | Projects including school and work | school, work, projects |
| `layer_-1_research` | Research and experimental projects | research, experiments |

[Optional additional sections]
```

---

## Component 3: LLM-Based Child Selector

### Purpose
Use LLM to pick the best-matching child given query keywords.

### Design

```
Function: select_best_child(query_keywords, children, depth):
  // Build prompt for LLM
  prompt = f"""
  Query: {join(query_keywords)}

  Available children and their keywords:
  """

  for child in children:
    prompt += f"- {child.name}: {child.description}"
    prompt += f"  Keywords: {join(child.keywords)}\n"

  prompt += """
  Which child is MOST RELEVANT to the query?
  Respond with ONLY the child name, nothing else.
  Example: layer_1_projects
  """

  // Call LLM
  response = llm.complete(prompt)
  selected_name = response.strip()

  // Validate response
  matching_child = find(children, lambda c: c.name == selected_name)

  if matching_child:
    return matching_child
  else:
    // Fallback: pick child with highest keyword overlap
    best_score = 0
    best_child = children[0]

    for child in children:
      overlap = count(intersection(query_keywords, child.keywords))
      if overlap > best_score:
        best_score = overlap
        best_child = child

    log_warning(f"LLM selected invalid child, falling back to keyword overlap: {best_child.name}")
    return best_child
```

**Example Interaction**:

```
Query keywords: ["math", "course", "components"]

Prompt sent to LLM:
  Query: math course components

  Available children and their keywords:
  - layer_1_projects: Projects including school and work
    Keywords: school, work, projects
  - layer_-1_research: Research and experimental projects
    Keywords: research, experiments

  Which child is MOST RELEVANT to the query?
  Respond with ONLY the child name, nothing else.
  Example: layer_1_projects

LLM Response: "layer_1_projects"

Selected child: layer_1_projects (matches "school" keyword)
```

---

## Component 4: Recursive Descent Controller

### Purpose
Coordinate the recursive traversal from root to leaf.

### Design

```
Function: find_context(query, start_path="~/", max_depth=10, depth=0):
  if depth > max_depth:
    log_error("Max traversal depth exceeded")
    return None

  // Read index at current level
  children = read_index(start_path)

  // Are we at a leaf? (no children found or reached target)
  if not children or is_likely_target(start_path, query_keywords):
    if exists(start_path + "/CLAUDE.md"):
      return {
        "path": start_path,
        "type": "leaf",
        "confidence": "high",
        "depth": depth
      }

  // Get query keywords
  if depth == 0:
    query_keywords = preprocess_query(query)

  // Select best child
  best_child = select_best_child(query_keywords, children, depth)

  // Recurse into best child
  next_path = best_child.full_path
  return find_context(query, next_path, max_depth, depth+1)
```

**Example Traversal**:

```
Query: "Where is the math course component?"
Keywords: ["math", "course", "component"]

Level 0: ~/
  Children: [layer_1_projects, layer_-1_research]
  Selection: layer_1_projects (matches school)

Level 1: ~/layer_1/layer_1_projects/
  Children: [layer_1_project_school, layer_1_project_work]
  Selection: layer_1_project_school (matches school→course)

Level 2: ~/layer_1/layer_1_projects/layer_1_project_school/
  Children: [layer_2, layer_3, layer_4, ...]
  Selection: layer_2 (branching point)

Level 3: ~/layer_1/layer_1_projects/layer_1_project_school/layer_2/
  Children: [layer_2_features, layer_2_components]
  Selection: layer_2_features (matches course)

Level 4: ~/layer_1/.../layer_2_features/
  Children: [layer_2_feature_math_curriculum, layer_2_feature_assessment_system]
  Selection: layer_2_feature_math_curriculum (matches math)

Level 5: ~/layer_1/.../layer_2_feature_math_curriculum/layer_3_features/
  Children: [layer_3_feature_math_problems, layer_3_feature_solutions, ...]
  Selection: layer_3_feature_math_problems (matches component)

Result: Return path with confidence=high, depth=6
```

---

## Component 5: Result Validator

### Purpose
Verify that the returned path is actually relevant and accessible.

### Design

```
Function: validate_result(path, query_keywords):
  // Check 1: Path exists
  if not exists(path):
    return {
      "valid": false,
      "reason": "Path does not exist",
      "confidence": 0.0
    }

  // Check 2: Has context file
  has_claude = exists(path + "/CLAUDE.md")
  has_agnostic = exists(path + "/0AGNOSTIC.md")
  has_index = exists(path + "/0INDEX.md")

  if not (has_claude or has_agnostic or has_index):
    return {
      "valid": false,
      "reason": "No context files found",
      "confidence": 0.3
    }

  // Check 3: Path name matches query keywords
  path_name = extract_directory_name(path)
  keyword_match = count(intersection(query_keywords, tokenize(path_name)))

  if keyword_match == 0:
    confidence = 0.5  // Might be correct but unclear
  elif keyword_match >= 2:
    confidence = 0.95  // Very likely correct
  else:
    confidence = 0.7   // Probably correct

  return {
    "valid": true,
    "reason": "Path found with context",
    "confidence": confidence,
    "context_files": {
      "CLAUDE.md": has_claude,
      "0AGNOSTIC.md": has_agnostic,
      "0INDEX.md": has_index
    }
  }
```

---

## 0INDEX.md File Format

### Required Structure

```markdown
# 0INDEX.md - [Directory Name]

**Version**: 1.0
**Last Updated**: 2026-01-30

## Purpose

[1-2 sentence description of what this level contains]

## Children

| Directory | Description | Keywords |
|-----------|-------------|----------|
| `child_1` | What this child contains | keyword1, keyword2 |
| `child_2` | Another child | keyword3, keyword4 |

## Navigation Rules

- **When query mentions X**: Go to `child_1`
- **When query mentions Y**: Go to `child_2`

[Optional additional sections like "See Also", "Examples"]
```

### Keywords Guidelines

- **Be specific**: Use exact terms from domain (e.g., "math", "courses", "assessment")
- **Include synonyms**: "math, mathematics, math-courses"
- **Avoid overlap**: Each child should have unique keywords if possible
- **Case insensitive**: Keywords matched case-insensitively

### Example 0INDEX.md

```markdown
# 0INDEX.md - layer_1_projects

**Version**: 1.2.0
**Last Updated**: 2026-01-30

## Purpose

Navigate to all major projects (school, work, research)

## Children

| Directory | Description | Keywords |
|-----------|-------------|----------|
| `layer_1_project_school` | School project infrastructure (courses, assignments, students) | school, education, courses, students, assignments, grades |
| `layer_1_project_work` | Work projects (tasks, teams, collaboration) | work, projects, tasks, teams, collaboration |

## Navigation Rules

- **For school/course work**: Go to `layer_1_project_school`
- **For work-related tasks**: Go to `layer_1_project_work`
- **If unsure**: Check both projects' CLAUDE.md files for detailed scope

## See Also

- Project details: Each project has its own CLAUDE.md
- Universal rules: `../../../layer_0_group/`
```

---

## /find Skill Implementation

### Skill.md Entry Point

```yaml
# ~/.claude/skills/find/SKILL.md

## Purpose
Automatically discover context at scale using hierarchical traversal.

## Usage
/find "query string"
/find "query string" from "path"
/find "find math course components"

## Examples
/find "Where is the assessment system?"
  Result: ~/layer_1/layer_1_projects/layer_1_project_school/layer_2/...

/find "How do I track student progress?"
  Result: ~/layer_1/layer_1_projects/layer_1_project_school/layer_2/layer_2_features/...

/find "What about parallel execution?"
  Result: ~/layer_0_group/layer_0_03_sub_layers/sub_layer_0_04_rules/...
```

### Implementation Flow

```
User calls: /find "find math course components"

1. Parse command → extract query
2. Preprocess query → keywords
3. Call find_context(query, "~/")
4. Recursive descent:
   - Read 0INDEX.md at each level
   - LLM selects best child
   - Recurse into child
   - Stop at leaf
5. Validate result
6. Return path + confidence
7. Display: "Found at [path] (confidence: 95%)"
```

---

## Error Cases & Recovery

### Case 1: Query Doesn't Match Any Child

**Scenario**: Query = "flying unicorns" (no relevant keywords)

**Handling**:
```
1. Keyword extraction fails to find meaningful terms
2. LLM sees vague query
3. LLM picks first child (arbitrary)
4. Validator returns low confidence (0.3)
5. Display: "Query too vague. Try more specific terms."
6. Suggest: "Did you mean: [similar queries]?"
```

### Case 2: Max Depth Exceeded

**Scenario**: Traversal goes 10+ levels without finding target

**Handling**:
```
1. Depth counter exceeds max_depth=10
2. Return current path with warning
3. Display: "Traversal depth limit exceeded. Returned best match: [path]"
4. User can then navigate manually from that point
```

### Case 3: 0INDEX.md Missing at Level

**Scenario**: Directory has children but no 0INDEX.md

**Handling**:
```
1. read_index() returns empty list
2. Treat as leaf node
3. Return current path
4. Log warning: "No 0INDEX.md at [path], treating as leaf"
5. Suggest: "Please create 0INDEX.md to improve traversal"
```

---

## Performance Considerations

| Operation | Expected Time | Notes |
|-----------|---------------|-------|
| Preprocess query | <10ms | Simple string operations |
| Read 0INDEX.md | <50ms | File I/O |
| LLM call | 500-1000ms | Network + inference |
| Single recursive level | 600-1100ms | Read + LLM |
| Full traversal (5 levels) | 3-5.5 seconds | 5 × (read + LLM) |

**Optimization Strategy**:
- Cache 0INDEX.md files in memory during session
- Batch LLM calls if multiple queries in same session
- Use keyword matching as fast-path before LLM

---

## Integration with Other Systems

### With Multi-Agent Sync

```
Agent starts session:
  1. Read 0AGNOSTIC.md (context)
  2. /find "Where is my research from last session?"
  3. Navigates to outputs/episodic/sessions/
  4. Reads previous session notes
  5. Resumes work with full context
```

### With Episodic Memory

```
After session:
  /find "Where should I document my findings?"
  → Points to outputs/01_understanding_in_progress/by_topic/
  → Agent writes session findings there
  → Creates outputs/episodic/sessions/ entry
  → Next agent uses /find to read episodic memory
```

---

## Testing Strategy

### Unit Tests

- [ ] Preprocess_query removes stopwords correctly
- [ ] read_index parses table correctly
- [ ] select_best_child picks reasonable child
- [ ] validate_result checks all conditions

### Integration Tests

- [ ] Full traversal from root to leaf
- [ ] Traversal with missing 0INDEX.md
- [ ] Traversal with vague query
- [ ] Traversal exceeding max depth

### Accuracy Tests

- [ ] /find "math" finds math-related content
- [ ] /find "school" finds school project
- [ ] /find "assessment" finds assessment system
- [ ] /find "rules" finds layer_0 rules

### Performance Tests

- [ ] Single query: <6 seconds
- [ ] 10 consecutive queries: <60 seconds total
- [ ] Memory usage: <50MB for session

---

## Implementation Checklist

- [ ] Design 0INDEX.md file format
- [ ] Implement preprocess_query()
- [ ] Implement read_index()
- [ ] Implement select_best_child() with LLM
- [ ] Implement recursive descent
- [ ] Implement validate_result()
- [ ] Create /find skill wrapper
- [ ] Create 0INDEX.md at 20-30 branching points
- [ ] Test manual traversal before LLM
- [ ] Create LLM fallback (keyword matching)
- [ ] Performance optimization (caching)
- [ ] Error handling for edge cases

