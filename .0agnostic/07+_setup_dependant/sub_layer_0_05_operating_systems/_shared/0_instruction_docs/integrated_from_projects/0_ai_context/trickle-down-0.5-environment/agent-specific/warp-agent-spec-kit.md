---
resource_id: "c7ba7a65-8fa9-4fc0-8234-1f977b77bf5a"
resource_type: "document"
resource_name: "warp-agent-spec-kit"
---
# Warp Agent: Spec Kit Implementation Guide
*Agent-Specific Instructions for Language Tracker Project*

<!-- section_id: "0fa838ef-cfd4-4d4a-ab5c-612deba82530" -->
## Session Initialization Protocol

**MANDATORY:** Start each session by declaring:
```
AI Agent: Warp AI Assistant
Project: Language Tracker (lang-trak-in-progress)
Environment: WSL Ubuntu (/home/dawson/code/lang-trak-in-progress)
Coding System: GitHub Spec Kit
Session Focus: [specify current work area - e.g., "Authentication Feature", "TDD Setup", "Environment Config"]
```

<!-- section_id: "358236b0-002c-42d0-bda9-6aba8e69b988" -->
## Warp-Specific Spec Kit Integration

<!-- section_id: "3ecf9fa4-228e-48ce-99b2-9fe5d519c371" -->
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

<!-- section_id: "77cd3df3-0a2f-4b1d-a252-1b626044f5cc" -->
### Phase 1: Constitution + Warp Tools
**Integration:**
- Warp: Load constitution with `read_any_files`
- Spec Kit: Parse and validate constitution structure
- Warp: Create `create_todo_list` for constitution implementation
- Spec Kit: Generate acceptance criteria from user stories

<!-- section_id: "81612eb4-697a-4001-9b58-8d58a0e9c2b7" -->
### Phase 2: Feature Specification + Warp Tools  
**Integration:**
- Warp: Use `search_codebase` to understand existing architecture
- Spec Kit: Generate detailed feature specifications
- Warp: Create implementation specs with `create_file`
- Spec Kit: Map to TD2 domains and generate testable criteria

<!-- section_id: "d5880f40-c904-4c2e-9fce-7e5898864028" -->
### Phase 3: Implementation Planning + Warp Tools
**Integration:**
- Spec Kit: Break specifications into implementable tasks
- Warp: Convert to `create_todo_list` with dependencies
- Warp: Use `find_files` and `grep` to assess current codebase
- Spec Kit: Provide implementation patterns and best practices

<!-- section_id: "0998eecb-2da0-4f96-9d3d-218389e45144" -->
### Phase 4: Task Generation + Warp Tools
**Integration:**
- Spec Kit: Generate parallelizable implementation tasks
- Warp: Organize with TODO management system
- Warp: Use `mark_todo_as_done` for progress tracking
- Spec Kit: Provide task validation and completion criteria

<!-- section_id: "4ff1f738-d218-4801-b983-2c7b0d18436c" -->
### Phase 5: Implementation + Warp Tools
**Integration:**
- Warp: Execute code changes with `edit_files`
- Spec Kit: Validate changes against specifications
- Warp: Run tests with `run_command`
- Spec Kit: Provide quality assurance patterns

<!-- section_id: "ea3c9361-cb56-46d9-b39f-746c068ac14b" -->
## Command Integration Examples

<!-- section_id: "34339561-3c21-4cf7-9c46-ba56a23fe25d" -->
### Spec Kit CLI + Warp Tools
```bash
# Spec Kit generates spec, Warp implements
specify feature new auth-system --from-constitution
# → Warp reads output and creates implementation files

# Warp searches codebase, Spec Kit provides guidance
warp: search_codebase("authentication patterns")
# → Spec Kit suggests implementation approach
```

<!-- section_id: "71ac95b0-3683-4c0c-9812-823a19cb83d2" -->
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
