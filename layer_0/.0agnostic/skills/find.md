# /find Skill - Automated Traversal

## Purpose
Navigate the layer-stage hierarchy using semantic search. Uses 0INDEX.md files at branching points to find relevant content.

---

## How to Use

### Query Format
```
/find <natural language query>
```

### Examples
```
/find research about SHIMI multi-agent systems
/find rules for AI context modification
/find design documents for better AI system
/find episodic memory implementation
/find how to use file locking
```

---

## Algorithm

### Step 1: Start at Root
Begin at the nearest 0INDEX.md (usually `0_layer_universal/0INDEX.md`)

### Step 2: Read Index
Read the 0INDEX.md and examine the Children table:
- Name: directory or file name
- Keywords: semantic keywords for matching
- Description: what the child contains

### Step 3: Select Best Match
Compare query keywords against each child's keywords:
- Match query terms to keyword column
- Consider description for context
- Select the child with highest relevance

### Step 4: Recurse
If selected child has its own 0INDEX.md:
- Navigate to that child
- Repeat from Step 2

### Step 5: Return Result
When no more 0INDEX.md files or max depth reached:
- Return the current path
- Return the matching content or file

---

## Implementation (For AI Agents)

When executing /find:

```
1. Set current_path = root (0_layer_universal/)
2. Set max_depth = 5
3. For depth = 0 to max_depth:
   a. Read 0INDEX.md at current_path
   b. Extract children table
   c. For each child, calculate relevance:
      - keyword_matches = count(query_terms ∩ child_keywords)
      - description_matches = count(query_terms in child_description)
      - score = keyword_matches * 2 + description_matches
   d. Select child with highest score
   e. If child has 0INDEX.md:
      - current_path = current_path / child
      - Continue to next depth
   f. Else:
      - Return current_path / child
4. Return current_path (max depth reached)
```

---

## Index File Format

0INDEX.md files follow this structure:

```markdown
# Index: <directory_name>

## Purpose
<Brief description of this directory's purpose>

## Children

| Name | Type | Keywords | Description |
|------|------|----------|-------------|
| child1 | dir | keyword1, keyword2 | What child1 contains |
| child2 | file | keyword3, keyword4 | What child2 is about |

## Navigation Guide
<Tips for finding specific content>
```

---

## Fallback Behavior

If 0INDEX.md not found:
1. List directory contents
2. Use filename patterns to infer purpose
3. Read README.md or CLAUDE.md if present
4. Return best guess based on naming conventions

---

## Performance

- Typical traversal: 3-5 steps
- Each step: Read 1 file, compare ~5-10 children
- Total time: 3-5 seconds for full traversal
- Scales to 5,930+ nodes efficiently

---

## Integration

The /find skill integrates with:
- **0AGNOSTIC.md**: Uses navigation section for starting point
- **Episodic memory**: Logs queries and results
- **Context traversal**: Part of standard context discovery

---

## Example Execution

Query: `/find SHIMI multi-agent sync design`

```
Step 1: 0_layer_universal/0INDEX.md
  → Children: layer_0, layer_1, layer_-1_research
  → Query matches "research" in layer_-1_research keywords
  → Select: layer_-1_research

Step 2: layer_-1_research/0INDEX.md
  → Children: layer_-1_better_ai_system
  → Query matches "SHIMI", "agents" keywords
  → Select: layer_-1_better_ai_system

Step 3: layer_-1_better_ai_system/0INDEX.md
  → Children: layer_-1, design documents
  → Query matches "design" in stage_-1_04_design
  → Navigate to stage

Step 4: stage_-1_04_design/outputs/03_design_decisions/
  → Query matches "multi-agent sync"
  → Return: 01_multi_agent_sync_design.md

Result: Found in 4 steps
```

---

*This skill implements SHIMI's LLM-based hierarchical traversal concept.*

