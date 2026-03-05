---
resource_id: "7cc8a314-24b2-4c36-be0a-2448facf9034"
resource_type: "document"
resource_name: "instructions"
---
# AutoGen Agent Context

<!-- section_id: "35bca8fb-155b-4ef1-b4a0-fd7563b014ef" -->
## Identity

**Role**: L3 Users Layer Agent
**Scope**: User model, profiles, sessions
**Depends On**: L2 Infrastructure (auth, firebase)
**Provides**: IUserProvider

<!-- section_id: "2b88d256-ff1d-46f3-99db-534877105eae" -->
## Key Behaviors

<!-- section_id: "b755e7a1-debf-4851-9b52-e3422f855e74" -->
### Sub-layers
- L3.1 Model: User data structures and database operations
- L3.2 Profiles: Profile display and management
- L3.3 Sessions: Session management, authentication state, current project context

<!-- section_id: "ba5c6b76-d4d2-425e-942b-26d3c4ef27ee" -->
### Dependency Shape
Sequence: Model → Profiles → Sessions (each builds on previous)

<!-- section_id: "45c3a88f-11c6-47cd-897d-9b428ba9c8a5" -->
## Triggers

| Situation | Action |
|-----------|--------|
| User data issues | Check model/ sub-layer |
| Profile problems | Check profiles/ sub-layer |
| Session/auth state | Check sessions/ sub-layer |


<!-- section_id: "c06a388d-6cd9-4e40-b000-dfe16c97506d" -->
## Current Status

**Phase**: Routes extracted — user search and profile API routes
**Routes file**: routes.py (2 routes: user search, user profile)
**Key module**: sessions/session.py — provides get_user_info() used by all upper layers

<!-- section_id: "f584326e-d979-42c2-b6c7-ab469d95ab55" -->
## AutoGen-Specific Configuration

<!-- section_id: "c9f2978f-0f16-4560-ac3b-141196982649" -->
### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

<!-- section_id: "ce1b1ba3-f106-43ea-83f9-d8c88c10da18" -->
### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
