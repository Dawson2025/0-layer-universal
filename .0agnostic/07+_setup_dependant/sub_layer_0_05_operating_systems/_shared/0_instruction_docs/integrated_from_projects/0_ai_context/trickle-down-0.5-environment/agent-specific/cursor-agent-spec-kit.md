---
resource_id: "dc7153f4-d9c7-4ec2-bab4-28ec521fa1e3"
resource_type: "document"
resource_name: "cursor-agent-spec-kit"
---
# Cursor Agent: Spec Kit Implementation Guide
*Agent-Specific Instructions for Language Tracker Project*

<!-- section_id: "4fe5cfe9-1d8a-4087-a6df-cd5a63c0c297" -->
## Session Initialization Protocol

**MANDATORY:** Start each session by declaring:
```
AI Agent: Cursor AI Assistant
Project: Language Tracker (lang-trak-in-progress)
Environment: WSL Ubuntu (/home/dawson/code/lang-trak-in-progress)
Coding System: GitHub Spec Kit
Session Focus: [specify current work area - e.g., "Authentication Feature", "TDD Setup", "Environment Config"]
```

<!-- section_id: "6636d18e-9da1-45de-88d9-e879257ab2ae" -->
## Cursor-Specific Spec Kit Integration

<!-- section_id: "4e4d4d7c-c956-4768-8d7a-f7df92cb757e" -->
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

<!-- section_id: "f1075950-86e3-408f-a59c-2db0227590a6" -->
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

<!-- section_id: "99ef753b-6999-4bb9-8993-33a97214c898" -->
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

<!-- section_id: "5c86ce31-0511-4fad-92d9-b78f90d9a006" -->
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

<!-- section_id: "60ead324-e7c2-4b73-bccb-b2daa9f23251" -->
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

<!-- section_id: "cb1ba35f-c7d1-468f-a4b1-ea2333a52596" -->
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

<!-- section_id: "41818e12-b110-4afc-a34d-24f193eac5a2" -->
## Cursor-Specific Workflow Patterns

<!-- section_id: "cd09baa1-21d3-4326-b650-a5cc3e6dbb3d" -->
### Pattern 1: Semantic Understanding First
```
Before implementing any feature:
1. codebase_search("How does <related-feature> work?", [])
2. Review results for patterns and conventions
3. Read relevant files identified in search
4. Follow established patterns in new implementation
```

<!-- section_id: "e2f153a0-7f8b-4864-9170-b64f11471efa" -->
### Pattern 2: TODO-Driven Development
```
For every task:
1. todo_write(merge=false, [...]) - Create initial TODO list
2. Mark one task as "in_progress"
3. Implement that task completely
4. todo_write(merge=true, [...]) - Mark as "completed"
5. Repeat for next task
```

<!-- section_id: "d82a3f73-6822-4ada-8f09-b7fbef4b9408" -->
### Pattern 3: Test-First Implementation
```
Following Constitution principle #3:
1. Read relevant user stories from USER_STORIES.md
2. Create test files first in features/<feature>/tests/
3. Implement feature code to pass tests
4. Run: python3 scripts/automation/run_user_stories.py --navigation-mode=both
5. Verify all tests pass before marking complete
```

<!-- section_id: "f0a6c912-4e09-411e-9365-8e7d45e7c4eb" -->
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

<!-- section_id: "26663737-2a5c-4ee1-a2c8-90863ea284a0" -->
## Cursor Advantages for Spec Kit

<!-- section_id: "0e66386f-b08a-442a-a27e-3e27e63d691b" -->
### Real-Time Code Understanding
**Cursor's `codebase_search`** provides semantic understanding:
- "How does user authentication work?" - Understands intent
- "Where are phoneme templates validated?" - Finds relevant code
- "What's the pattern for creating new features?" - Identifies conventions

<!-- section_id: "e7fe7a4a-730a-4d76-a4cf-bf3a5c5b9c6b" -->
### Efficient File Operations
**Cursor's file tools** enable precise changes:
- `search_replace` - Exact string replacements with context
- `write` - Complete file creation/overwrite
- `read_file` - Selective reading with offset/limit for large files

<!-- section_id: "cee3b668-2398-4e2d-a113-1387bb53a830" -->
### Integrated Testing
**Cursor's `run_terminal_cmd`** enables immediate validation:
- Run pytest after each implementation
- Execute golden rule tests
- Verify linter compliance
- Check git status

<!-- section_id: "bde324aa-5f1e-4f05-8d7e-bde2369adc78" -->
### Context-Aware Development
**Cursor's IDE integration** provides:
- Open file awareness
- Recent file tracking
- Linter error detection
- Multi-file editing in single session

<!-- section_id: "528b176d-f625-460f-8b7d-fba95d2606e0" -->
## Command Integration Examples

<!-- section_id: "0cde9e93-b37f-403c-9f47-e53cdb41aae1" -->
### Spec Kit CLI + Cursor Tools
```bash
# Hypothetical Spec Kit CLI usage (if installed):
# specify feature new auth-system --from-constitution
# → Cursor reads output and creates implementation files

# Cursor semantic search, Spec Kit provides guidance
cursor: codebase_search("authentication patterns", [])
# → Spec Kit suggests implementation approach based on results
```

<!-- section_id: "35da3975-c4c6-4b42-983e-4edb1bbe3016" -->
## Session Workflow Example

<!-- section_id: "8585bfc2-319d-4b67-836f-47f13263f7b2" -->
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

<!-- section_id: "27cafa22-d7db-4185-a06b-e423120350a8" -->
## Best Practices for Cursor + Spec Kit

<!-- section_id: "ba911148-cf77-4856-b9bb-7cfab0802334" -->
### DO:
✅ Use `codebase_search` for understanding, `grep` for exact matches
✅ Create TODO lists for every multi-step task
✅ Follow traffic light system (Green → Yellow → Red caution levels)
✅ Run tests after every implementation
✅ Update documentation as you implement
✅ Use `read_lints` to catch errors early
✅ Mark TODO items completed immediately after finishing

<!-- section_id: "39b063bc-c99f-4114-8259-4ff189b13058" -->
### DON'T:
❌ Skip the constitution/requirements reading phase
❌ Implement without understanding existing patterns
❌ Leave TODO items in "in_progress" when complete
❌ Make Red Zone changes without coordination
❌ Commit code without running tests
❌ Assume implementation details - always verify with search/read

<!-- section_id: "40194ffe-32f8-4857-9d87-ec8c08e31348" -->
## Cursor-Specific Initialization

<!-- section_id: "735a39ac-26e6-4171-b9fd-5d5061ab4aec" -->
### Every Session Checklist:
1. ✅ Declare agent identity and session focus
2. ✅ Verify WSL Ubuntu environment (`pwd` command)
3. ✅ Check git status
4. ✅ Load relevant constitution/requirements docs
5. ✅ Search codebase for existing patterns
6. ✅ Create TODO list for session goals
7. ✅ Begin implementation following Spec Kit phases

<!-- section_id: "b1f6610e-0a33-4b3b-9c3d-0b841d6f9052" -->
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

