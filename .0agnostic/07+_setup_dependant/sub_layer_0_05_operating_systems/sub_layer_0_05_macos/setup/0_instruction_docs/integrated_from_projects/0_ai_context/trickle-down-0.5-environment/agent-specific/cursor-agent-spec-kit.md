---
resource_id: "46b24252-92bc-4f6e-83c2-b9c1a0949463"
resource_type: "document"
resource_name: "cursor-agent-spec-kit"
---
# Cursor Agent: Spec Kit Implementation Guide
*Agent-Specific Instructions for Language Tracker Project*

<!-- section_id: "c2c72f7a-ee3e-4e4e-89e4-b63d796ab229" -->
## Session Initialization Protocol

**MANDATORY:** Start each session by declaring:
```
AI Agent: Cursor AI Assistant
Project: Language Tracker (lang-trak-in-progress)
Environment: WSL Ubuntu (/home/dawson/code/lang-trak-in-progress)
Coding System: GitHub Spec Kit
Session Focus: [specify current work area - e.g., "Authentication Feature", "TDD Setup", "Environment Config"]
```

<!-- section_id: "fed53aa9-586f-4dfd-8635-f5318d20b6ce" -->
## Cursor-Specific Spec Kit Integration

<!-- section_id: "6d3d0442-be8b-48e3-b057-363c0f1d98ff" -->
### Cursor's Native Tools + Spec Kit Features
**Cursor Tools Available:**
- `codebase_search` - Semantic search for understanding code by meaning
- `grep` - Fast exact text/pattern matching
- `read_file`, `write`, `search_replace`, `edit_notebook` - File operations
- `run_terminal_cmd` - Command execution
- `glob_file_search`, `list_dir` - File system navigation
- `todo_write` - TODO management for task tracking
- `read_lints` - Linter error detection
- `web_search` - External information lookup

**Spec Kit Features for Cursor:**
- Constitution loading and parsing
- Feature specification generation
- Implementation planning with task breakdown
- Code generation aligned with specs
- Quality validation and testing

<!-- section_id: "bfc168c7-f8e9-47dd-bfae-9450d40776a8" -->
### Phase 1: Constitution + Cursor Tools
**Integration:**
- Cursor: Load constitution with `read_file`
- Spec Kit: Parse and validate constitution structure
- Cursor: Create `todo_write` for constitution implementation
- Spec Kit: Generate acceptance criteria from user stories

**Example Flow:**
```
1. read_file("docs/1_trickle_down/trickle-down-1-project/constitution.md")
2. Parse core principles, decision framework, non-negotiables
3. todo_write([
    {id: "const-1", content: "Validate constitution structure", status: "completed"},
    {id: "const-2", content: "Extract quality standards", status: "in_progress"}
   ])
4. Generate acceptance criteria based on constitution principles
```

<!-- section_id: "0733caa2-1541-49a4-802a-046e4a29e923" -->
### Phase 2: Feature Specification + Cursor Tools  
**Integration:**
- Cursor: Use `codebase_search` to understand existing architecture
- Spec Kit: Generate detailed feature specifications
- Cursor: Create implementation specs with `write`
- Spec Kit: Map to TD2 domains and generate testable criteria

**Example Flow:**
```
1. codebase_search("How does authentication work?", [])
2. Review existing patterns in features/auth/
3. Spec Kit: Generate new feature specification based on patterns
4. write("docs/2_features/<feature>/feature-spec.md", spec_content)
5. Create testable acceptance criteria aligned with USER_STORIES.md
```

<!-- section_id: "e42c3407-b90b-46f0-8e0c-48061c493119" -->
### Phase 3: Implementation Planning + Cursor Tools
**Integration:**
- Spec Kit: Break specifications into implementable tasks
- Cursor: Convert to `todo_write` with dependencies
- Cursor: Use `grep` and `codebase_search` to assess current codebase
- Spec Kit: Provide implementation patterns and best practices

**Example Flow:**
```
1. Spec Kit: Analyze feature spec, break into tasks
2. todo_write([
    {id: "impl-1", content: "Create feature blueprint", status: "pending"},
    {id: "impl-2", content: "Implement core logic", status: "pending"},
    {id: "impl-3", content: "Add tests", status: "pending"}
   ])
3. codebase_search("Where are similar features implemented?", ["features/"])
4. Identify patterns: display.py, creation.py, editing.py, search.py
```

<!-- section_id: "5a468262-1935-4f4d-871c-4c2cbd3f8d78" -->
### Phase 4: Task Generation + Cursor Tools
**Integration:**
- Spec Kit: Generate parallelizable implementation tasks
- Cursor: Organize with TODO management system
- Cursor: Track progress with `todo_write` merge updates
- Spec Kit: Provide task validation and completion criteria

**Example Flow:**
```
1. Spec Kit: Generate task list with dependencies
2. todo_write(merge=false, [
    {id: "task-1", content: "Create routes.py", status: "in_progress"},
    {id: "task-2", content: "Create display.py", status: "pending"},
    {id: "task-3", content: "Create tests/", status: "pending"}
   ])
3. Work on tasks sequentially
4. todo_write(merge=true, [{id: "task-1", status: "completed"}])
```

<!-- section_id: "8a242bc8-83da-43b8-93c9-d1272ee3651d" -->
### Phase 5: Implementation + Cursor Tools
**Integration:**
- Cursor: Execute code changes with `search_replace` or `write`
- Spec Kit: Validate changes against specifications
- Cursor: Run tests with `run_terminal_cmd`
- Spec Kit: Provide quality assurance patterns
- Cursor: Check linter errors with `read_lints`

**Example Flow:**
```
1. write("features/<feature>/routes.py", implementation)
2. run_terminal_cmd("pytest features/<feature>/tests/", is_background=false)
3. read_lints(["features/<feature>/routes.py"])
4. Spec Kit: Validate against feature specification
5. Verify acceptance criteria met
```

<!-- section_id: "97c6ce28-831b-4d12-aba9-667f04aed285" -->
## Cursor-Specific Workflow Patterns

<!-- section_id: "10e25300-39cd-493c-b9d9-fa0ab1a88084" -->
### Pattern 1: Semantic Understanding First
```
Before implementing any feature:
1. codebase_search("How does <related-feature> work?", [])
2. Review results for patterns and conventions
3. Read relevant files identified in search
4. Follow established patterns in new implementation
```

<!-- section_id: "7134e201-657d-4974-9a44-87a64899cd58" -->
### Pattern 2: TODO-Driven Development
```
For every task:
1. todo_write(merge=false, [...]) - Create initial TODO list
2. Mark one task as "in_progress"
3. Implement that task completely
4. todo_write(merge=true, [...]) - Mark as "completed"
5. Repeat for next task
```

<!-- section_id: "377d2676-8c8b-490b-a714-fb6d6d76f40f" -->
### Pattern 3: Test-First Implementation
```
Following Constitution principle #3:
1. Read relevant user stories from USER_STORIES.md
2. Create test files first in features/<feature>/tests/
3. Implement feature code to pass tests
4. Run: python3 scripts/automation/run_user_stories.py --navigation-mode=both
5. Verify all tests pass before marking complete
```

<!-- section_id: "97bce29b-0429-4dda-85eb-857940e110d9" -->
### Pattern 4: Traffic Light System Compliance
```
Green Zone (95% - Work freely):
- features/<feature>/* - All feature-specific files

Yellow Zone (4% - Check first):
- core/* - Shared infrastructure
- services/* - Cross-cutting services
- Use codebase_search to understand before modifying

Red Zone (1% - Must coordinate):
- app.py - Main application file
- Database schema changes
- Coordinate with user before changes
```

<!-- section_id: "0331eb79-dffc-425b-b3d1-c553589fa1f9" -->
## Cursor Advantages for Spec Kit

<!-- section_id: "834b00d1-3e7c-44fb-8fb0-06cbccfbdd7e" -->
### Real-Time Code Understanding
**Cursor's `codebase_search`** provides semantic understanding:
- "How does user authentication work?" - Understands intent
- "Where are phoneme templates validated?" - Finds relevant code
- "What's the pattern for creating new features?" - Identifies conventions

<!-- section_id: "1ce2c73e-9bf3-489f-8345-cfc149d84dc6" -->
### Efficient File Operations
**Cursor's file tools** enable precise changes:
- `search_replace` - Exact string replacements with context
- `write` - Complete file creation/overwrite
- `read_file` - Selective reading with offset/limit for large files

<!-- section_id: "1a987a80-c64b-459a-8408-23eb17e8df0d" -->
### Integrated Testing
**Cursor's `run_terminal_cmd`** enables immediate validation:
- Run pytest after each implementation
- Execute golden rule tests
- Verify linter compliance
- Check git status

<!-- section_id: "caff008a-72c4-48c2-a4aa-0883c7edd809" -->
### Context-Aware Development
**Cursor's IDE integration** provides:
- Open file awareness
- Recent file tracking
- Linter error detection
- Multi-file editing in single session

<!-- section_id: "c9a7533e-7c81-47b2-8d84-bf40b84c546a" -->
## Command Integration Examples

<!-- section_id: "c71a95d0-c480-48f6-8e54-f72e8667c207" -->
### Spec Kit CLI + Cursor Tools
```bash
# Hypothetical Spec Kit CLI usage (if installed):
# specify feature new auth-system --from-constitution
# → Cursor reads output and creates implementation files

# Cursor semantic search, Spec Kit provides guidance
cursor: codebase_search("authentication patterns", [])
# → Spec Kit suggests implementation approach based on results
```

<!-- section_id: "82fa3207-fba6-474b-905d-9b1e95c45fd3" -->
## Session Workflow Example

<!-- section_id: "e4f557c8-25cc-41b4-9fc1-4104c9a85cb6" -->
### Full Feature Implementation Session

**1. Initialize Session:**
```
AI Agent: Cursor AI Assistant
Project: Language Tracker
Coding System: GitHub Spec Kit
Session Focus: Media Management Feature
```

**2. Load Context (Spec Kit Phase 1):**
```javascript
read_file("docs/1_trickle_down/trickle-down-1-project/constitution.md")
read_file("docs/for_ai/requirements/media_management.md")
read_file("docs/for_ai/requirements/USER_STORIES.md", offset=500, limit=50)
```

**3. Understand Existing Patterns (Spec Kit Phase 2):**
```javascript
codebase_search("How are media files handled currently?", [])
codebase_search("Where are file uploads processed?", ["features/"])
grep("upload", path="features/", output_mode="files_with_matches")
```

**4. Create Specification (Spec Kit Phase 2):**
```javascript
write("docs/2_features/media/feature-spec.md", spec_content)
```

**5. Plan Implementation (Spec Kit Phase 3):**
```javascript
todo_write(merge=false, [
  {id: "media-1", content: "Create features/media/routes.py", status: "pending"},
  {id: "media-2", content: "Create features/media/upload.py", status: "pending"},
  {id: "media-3", content: "Create features/media/storage.py", status: "pending"},
  {id: "media-4", content: "Create features/media/tests/", status: "pending"},
  {id: "media-5", content: "Update documentation", status: "pending"}
])
```

**6. Implement Tasks (Spec Kit Phase 5):**
```javascript
// Task 1
todo_write(merge=true, [{id: "media-1", status: "in_progress"}])
write("features/media/routes.py", routes_implementation)
run_terminal_cmd("python3 -m py_compile features/media/routes.py", is_background=false)
todo_write(merge=true, [{id: "media-1", status: "completed"}])

// Task 2
todo_write(merge=true, [{id: "media-2", status: "in_progress"}])
// ... continue pattern
```

**7. Validate (Spec Kit Phase 5):**
```javascript
read_lints(["features/media/"])
run_terminal_cmd("pytest features/media/tests/", is_background=false)
run_terminal_cmd("python3 scripts/automation/run_user_stories.py --navigation-mode=both", is_background=false)
```

<!-- section_id: "c68cc8e3-73e6-4524-b892-f031b0ea1db3" -->
## Best Practices for Cursor + Spec Kit

<!-- section_id: "a565b986-8748-46a1-9286-a371a7a4d194" -->
### DO:
✅ Use `codebase_search` for understanding, `grep` for exact matches
✅ Create TODO lists for every multi-step task
✅ Follow traffic light system (Green → Yellow → Red caution levels)
✅ Run tests after every implementation
✅ Update documentation as you implement
✅ Use `read_lints` to catch errors early
✅ Mark TODO items completed immediately after finishing

<!-- section_id: "6daa4dac-5920-4de2-9ada-5067b1b4a40b" -->
### DON'T:
❌ Skip the constitution/requirements reading phase
❌ Implement without understanding existing patterns
❌ Leave TODO items in "in_progress" when complete
❌ Make Red Zone changes without coordination
❌ Commit code without running tests
❌ Assume implementation details - always verify with search/read

<!-- section_id: "c06f54ab-7696-4d34-88c0-41d9fb54930e" -->
## Cursor-Specific Initialization

<!-- section_id: "2c1bc191-a402-41a7-bb3d-5596272549ac" -->
### Every Session Checklist:
1. ✅ Declare agent identity and session focus
2. ✅ Verify WSL Ubuntu environment (`pwd` command)
3. ✅ Check git status
4. ✅ Load relevant constitution/requirements docs
5. ✅ Search codebase for existing patterns
6. ✅ Create TODO list for session goals
7. ✅ Begin implementation following Spec Kit phases

<!-- section_id: "43566864-9d34-4b16-9cca-965c45064230" -->
## Quality Gates (Constitution Compliance)

Before marking any task complete:
- [ ] TODO list created and tracked
- [ ] Existing patterns researched via `codebase_search`
- [ ] Implementation matches project conventions
- [ ] Tests written and passing
- [ ] Linter errors resolved (`read_lints`)
- [ ] Documentation updated
- [ ] Golden rule test passes (if applicable)
- [ ] Git status clean (no unexpected changes)

---
*Agent: Cursor AI Assistant*  
*Integration: Cursor Native Tools + GitHub Spec Kit*  
*Environment: WSL Ubuntu*  
*Effective: October 21, 2025*

