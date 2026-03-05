---
resource_id: "0bdb2433-692c-4a5a-97f9-e60b8487091b"
resource_type: "document"
resource_name: "warp-agent-spec-kit"
---
# Warp Agent: Spec Kit Implementation Guide
*Agent-Specific Instructions for Language Tracker Project*

<!-- section_id: "3c0e6cd7-8b0b-4b85-9a44-df9a02c6595e" -->
## Session Initialization Protocol

**MANDATORY:** Start each session by declaring:
```
AI Agent: Warp AI Assistant
Project: Language Tracker (lang-trak-in-progress)
Environment: WSL Ubuntu (/home/dawson/dawson-workspace/code/lang-trak-in-progress)
Coding System: GitHub Spec Kit
Session Focus: [specify current work area - e.g., "Authentication Feature", "TDD Setup", "Environment Config"]
```

<!-- section_id: "d59c7299-482a-4580-a77a-e24b114f1223" -->
## Warp-Specific Spec Kit Integration

<!-- section_id: "d275db28-138e-47ea-b446-d40af47cb3d7" -->
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

<!-- section_id: "6e94db3f-d123-41b3-b413-1aaff9214327" -->
### Phase 1: Constitution + Warp Tools
**Integration:**
- Warp: Load constitution with `read_any_files`
- Spec Kit: Parse and validate constitution structure
- Warp: Create `create_todo_list` for constitution implementation
- Spec Kit: Generate acceptance criteria from user stories

<!-- section_id: "db3f5877-dc29-4eb9-a68a-87b888f3c5b5" -->
### Phase 2: Feature Specification + Warp Tools  
**Integration:**
- Warp: Use `search_codebase` to understand existing architecture
- Spec Kit: Generate detailed feature specifications
- Warp: Create implementation specs with `create_file`
- Spec Kit: Map to TD2 domains and generate testable criteria

<!-- section_id: "8eb5ecfa-c00b-4058-b942-ce3ef7e78c18" -->
### Phase 3: Implementation Planning + Warp Tools
**Integration:**
- Spec Kit: Break specifications into implementable tasks
- Warp: Convert to `create_todo_list` with dependencies
- Warp: Use `find_files` and `grep` to assess current codebase
- Spec Kit: Provide implementation patterns and best practices

<!-- section_id: "a5049c3c-fd62-4c9d-a7a4-ad26dc370e90" -->
### Phase 4: Task Generation + Warp Tools
**Integration:**
- Spec Kit: Generate parallelizable implementation tasks
- Warp: Organize with TODO management system
- Warp: Use `mark_todo_as_done` for progress tracking
- Spec Kit: Provide task validation and completion criteria

<!-- section_id: "317c8e99-e692-421c-96ee-6ccb423316eb" -->
### Phase 5: Implementation + Warp Tools
**Integration:**
- Warp: Execute code changes with `edit_files`
- Spec Kit: Validate changes against specifications
- Warp: Run tests with `run_command`
- Spec Kit: Provide quality assurance patterns

<!-- section_id: "45a26e2b-ecae-41f0-82af-cb6f0f7eebd2" -->
## Command Integration Examples

<!-- section_id: "20d11828-a8a6-4045-aefc-fe409ceadf0b" -->
### Spec Kit CLI + Warp Tools
```bash
# Spec Kit generates spec, Warp implements
specify feature new auth-system --from-constitution
# → Warp reads output and creates implementation files

# Warp searches codebase, Spec Kit provides guidance
warp: search_codebase("authentication patterns")
# → Spec Kit suggests implementation approach
```

<!-- section_id: "eaf4f46f-a0dc-465d-a170-40a44cd5b66b" -->
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
