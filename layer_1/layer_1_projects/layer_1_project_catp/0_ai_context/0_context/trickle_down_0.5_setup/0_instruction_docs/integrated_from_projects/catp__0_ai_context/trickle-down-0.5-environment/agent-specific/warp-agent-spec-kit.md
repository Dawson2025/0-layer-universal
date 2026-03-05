---
resource_id: "871c201f-851e-4ea6-911f-ce8ad2fba3dd"
resource_type: "document"
resource_name: "warp-agent-spec-kit"
---
# Warp Agent: Spec Kit Implementation Guide
*Agent-Specific Instructions for Language Tracker Project*

<!-- section_id: "0d472cbb-147b-4ed8-9289-5858de7f9c1e" -->
## Session Initialization Protocol

**MANDATORY:** Start each session by declaring:
```
AI Agent: Warp AI Assistant
Project: Language Tracker (lang-trak-in-progress)
Environment: WSL Ubuntu (/home/dawson/dawson-workspace/code/lang-trak-in-progress)
Coding System: GitHub Spec Kit
Session Focus: [specify current work area - e.g., "Authentication Feature", "TDD Setup", "Environment Config"]
```

<!-- section_id: "f279fb4b-2260-46ba-898e-091237725195" -->
## Warp-Specific Spec Kit Integration

<!-- section_id: "c38f7104-45cb-4626-86e1-2f13dd8b1604" -->
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

<!-- section_id: "9680dd05-7cdd-480c-bbb6-3b993d30a62e" -->
### Phase 1: Constitution + Warp Tools
**Integration:**
- Warp: Load constitution with `read_any_files`
- Spec Kit: Parse and validate constitution structure
- Warp: Create `create_todo_list` for constitution implementation
- Spec Kit: Generate acceptance criteria from user stories

<!-- section_id: "1d4ea3bd-8e41-41a0-9140-f09923a02011" -->
### Phase 2: Feature Specification + Warp Tools  
**Integration:**
- Warp: Use `search_codebase` to understand existing architecture
- Spec Kit: Generate detailed feature specifications
- Warp: Create implementation specs with `create_file`
- Spec Kit: Map to TD2 domains and generate testable criteria

<!-- section_id: "dac57222-1a37-436d-a506-2bea706682b7" -->
### Phase 3: Implementation Planning + Warp Tools
**Integration:**
- Spec Kit: Break specifications into implementable tasks
- Warp: Convert to `create_todo_list` with dependencies
- Warp: Use `find_files` and `grep` to assess current codebase
- Spec Kit: Provide implementation patterns and best practices

<!-- section_id: "643a7bff-64de-4878-83c2-705ac0975890" -->
### Phase 4: Task Generation + Warp Tools
**Integration:**
- Spec Kit: Generate parallelizable implementation tasks
- Warp: Organize with TODO management system
- Warp: Use `mark_todo_as_done` for progress tracking
- Spec Kit: Provide task validation and completion criteria

<!-- section_id: "9402bf8c-2d37-4359-ba8f-06dedea5ad9d" -->
### Phase 5: Implementation + Warp Tools
**Integration:**
- Warp: Execute code changes with `edit_files`
- Spec Kit: Validate changes against specifications
- Warp: Run tests with `run_command`
- Spec Kit: Provide quality assurance patterns

<!-- section_id: "1a5ab5de-224e-4d6c-af10-3fc39ed5ffd0" -->
## Command Integration Examples

<!-- section_id: "2a41a094-67a8-4b83-8929-2e9b931e86db" -->
### Spec Kit CLI + Warp Tools
```bash
# Spec Kit generates spec, Warp implements
specify feature new auth-system --from-constitution
# → Warp reads output and creates implementation files

# Warp searches codebase, Spec Kit provides guidance
warp: search_codebase("authentication patterns")
# → Spec Kit suggests implementation approach
```

<!-- section_id: "ef3b44f6-bd7d-4993-a909-ab0eae4036b0" -->
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
