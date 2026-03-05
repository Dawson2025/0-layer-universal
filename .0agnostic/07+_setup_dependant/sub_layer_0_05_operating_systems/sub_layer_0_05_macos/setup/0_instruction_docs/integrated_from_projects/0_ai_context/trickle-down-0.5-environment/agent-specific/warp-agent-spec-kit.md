---
resource_id: "7d5d456e-80d6-49f4-8b97-6692816d7069"
resource_type: "document"
resource_name: "warp-agent-spec-kit"
---
# Warp Agent: Spec Kit Implementation Guide
*Agent-Specific Instructions for Language Tracker Project*

<!-- section_id: "2b009e28-f39d-4630-94e8-1ab763a86074" -->
## Session Initialization Protocol

**MANDATORY:** Start each session by declaring:
```
AI Agent: Warp AI Assistant
Project: Language Tracker (lang-trak-in-progress)
Environment: WSL Ubuntu (/home/dawson/code/lang-trak-in-progress)
Coding System: GitHub Spec Kit
Session Focus: [specify current work area - e.g., "Authentication Feature", "TDD Setup", "Environment Config"]
```

<!-- section_id: "0ca6d437-7aa4-4290-9764-8d145217e2c2" -->
## Warp-Specific Spec Kit Integration

<!-- section_id: "cca7e42e-782a-4ee8-8017-2df530c74a61" -->
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

<!-- section_id: "eb90f881-9435-48c6-ac44-9590806d8367" -->
### Phase 1: Constitution + Warp Tools
**Integration:**
- Warp: Load constitution with `read_any_files`
- Spec Kit: Parse and validate constitution structure
- Warp: Create `create_todo_list` for constitution implementation
- Spec Kit: Generate acceptance criteria from user stories

<!-- section_id: "eef7ae74-30f2-4d09-b175-5d27d52cd6e9" -->
### Phase 2: Feature Specification + Warp Tools  
**Integration:**
- Warp: Use `search_codebase` to understand existing architecture
- Spec Kit: Generate detailed feature specifications
- Warp: Create implementation specs with `create_file`
- Spec Kit: Map to TD2 domains and generate testable criteria

<!-- section_id: "e1abe469-62cf-4106-b8aa-795981f6ab94" -->
### Phase 3: Implementation Planning + Warp Tools
**Integration:**
- Spec Kit: Break specifications into implementable tasks
- Warp: Convert to `create_todo_list` with dependencies
- Warp: Use `find_files` and `grep` to assess current codebase
- Spec Kit: Provide implementation patterns and best practices

<!-- section_id: "93a5353c-9e4b-45f0-a3f2-ef5ac16879dc" -->
### Phase 4: Task Generation + Warp Tools
**Integration:**
- Spec Kit: Generate parallelizable implementation tasks
- Warp: Organize with TODO management system
- Warp: Use `mark_todo_as_done` for progress tracking
- Spec Kit: Provide task validation and completion criteria

<!-- section_id: "15c4993f-b67d-44d9-abf8-8810ad7a204b" -->
### Phase 5: Implementation + Warp Tools
**Integration:**
- Warp: Execute code changes with `edit_files`
- Spec Kit: Validate changes against specifications
- Warp: Run tests with `run_command`
- Spec Kit: Provide quality assurance patterns

<!-- section_id: "50370056-11d8-47fe-96af-ab08cbd29bd7" -->
## Command Integration Examples

<!-- section_id: "a30579e5-54ce-4b4a-aeb3-4d549481be63" -->
### Spec Kit CLI + Warp Tools
```bash
# Spec Kit generates spec, Warp implements
specify feature new auth-system --from-constitution
# → Warp reads output and creates implementation files

# Warp searches codebase, Spec Kit provides guidance
warp: search_codebase("authentication patterns")
# → Spec Kit suggests implementation approach
```

<!-- section_id: "d12d402b-1459-46b6-bfd4-8fff0c916a7d" -->
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
