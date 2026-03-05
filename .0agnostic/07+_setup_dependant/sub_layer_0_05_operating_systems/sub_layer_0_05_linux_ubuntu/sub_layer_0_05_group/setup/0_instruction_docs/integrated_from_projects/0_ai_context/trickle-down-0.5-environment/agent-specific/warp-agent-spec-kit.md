---
resource_id: "13003732-bac7-45c4-a351-77d101784d52"
resource_type: "document"
resource_name: "warp-agent-spec-kit"
---
# Warp Agent: Spec Kit Implementation Guide
*Agent-Specific Instructions for Language Tracker Project*

<!-- section_id: "12da6eb3-d3c3-4b8a-bc79-91cf4b161695" -->
## Session Initialization Protocol

**MANDATORY:** Start each session by declaring:
```
AI Agent: Warp AI Assistant
Project: Language Tracker (lang-trak-in-progress)
Environment: WSL Ubuntu (/home/dawson/code/lang-trak-in-progress)
Coding System: GitHub Spec Kit
Session Focus: [specify current work area - e.g., "Authentication Feature", "TDD Setup", "Environment Config"]
```

<!-- section_id: "6e7e5b74-f2b4-416f-b4b9-d540f43e4e67" -->
## Warp-Specific Spec Kit Integration

<!-- section_id: "51c9a9f2-56d5-4c32-9fe7-245a5529cd1c" -->
### Warp's Native Tools + Spec Kit Features
**Warp Tools Available:**
- `read_any_files`, `edit_files`, `create_file`
- `run_command`, `grep`, `find_files`, `search_codebase`
- `create_todo_list`, `mark_todo_as_done`, TODO management

**Spec Kit Features for Warp:**
- Constitution loading and parsing
- Feature specification generation
- Implementation planning with task breakdown
- Code generation aligned with specs
- Quality validation and testing

<!-- section_id: "d0732bc9-bb66-4620-b61f-3e50916b7cee" -->
### Phase 1: Constitution + Warp Tools
**Integration:**
- Warp: Load constitution with `read_any_files`
- Spec Kit: Parse and validate constitution structure
- Warp: Create `create_todo_list` for constitution implementation
- Spec Kit: Generate acceptance criteria from user stories

<!-- section_id: "06ebaaeb-f682-4ffc-b62b-468e8a83d380" -->
### Phase 2: Feature Specification + Warp Tools  
**Integration:**
- Warp: Use `search_codebase` to understand existing architecture
- Spec Kit: Generate detailed feature specifications
- Warp: Create implementation specs with `create_file`
- Spec Kit: Map to TD2 domains and generate testable criteria

<!-- section_id: "5f4a190b-376d-4341-b2f3-bb5a0600effd" -->
### Phase 3: Implementation Planning + Warp Tools
**Integration:**
- Spec Kit: Break specifications into implementable tasks
- Warp: Convert to `create_todo_list` with dependencies
- Warp: Use `find_files` and `grep` to assess current codebase
- Spec Kit: Provide implementation patterns and best practices

<!-- section_id: "5acff700-3898-49a1-abfd-9c0769ba7b61" -->
### Phase 4: Task Generation + Warp Tools
**Integration:**
- Spec Kit: Generate parallelizable implementation tasks
- Warp: Organize with TODO management system
- Warp: Use `mark_todo_as_done` for progress tracking
- Spec Kit: Provide task validation and completion criteria

<!-- section_id: "a5779141-5b52-43d8-8969-e880f3553fee" -->
### Phase 5: Implementation + Warp Tools
**Integration:**
- Warp: Execute code changes with `edit_files`
- Spec Kit: Validate changes against specifications
- Warp: Run tests with `run_command`
- Spec Kit: Provide quality assurance patterns

<!-- section_id: "52cedced-b6d3-4276-b677-99d23488e019" -->
## Command Integration Examples

<!-- section_id: "40cdd38c-17b0-4e70-a1f2-1c803d91de66" -->
### Spec Kit CLI + Warp Tools
```bash
# Spec Kit generates spec, Warp implements
specify feature new auth-system --from-constitution
# → Warp reads output and creates implementation files

# Warp searches codebase, Spec Kit provides guidance
warp: search_codebase("authentication patterns")
# → Spec Kit suggests implementation approach
```

<!-- section_id: "cf752a17-e7f6-4abc-aa9a-15165a0a4d81" -->
## Other AI Agent Templates

Create similar guides for:
- **Claude Code Agent**: VS Code extensions + Spec Kit
- **Cursor Agent**: IDE features + Spec Kit  
- **GitHub Copilot**: Code completion + Spec Kit
- **Windsurf**: Web-based tools + Spec Kit

---
*Agent: Warp AI Assistant*  
*Integration: Warp Native Tools + GitHub Spec Kit*
*Environment: WSL Ubuntu*
