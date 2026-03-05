---
resource_id: "e110e59e-622f-4c0e-a07c-e8425aee96d8"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "227c6edc-d981-4dbd-9ef0-7e0594024250" -->
## Identity

entity_id: "15103670-9902-4b01-89b1-8f45aa3f08b7"

**Role**: L3 Users Layer Agent
**Scope**: User model, profiles, sessions
**Depends On**: L2 Infrastructure (auth, firebase)
**Provides**: IUserProvider

<!-- section_id: "72f5b4f7-e467-47b3-b062-a3409b5cc5ff" -->
## Key Behaviors

<!-- section_id: "8c731a5e-ac9e-473e-8598-41b56aaa3c0a" -->
### Sub-layers
- L3.1 Model: User data structures and database operations
- L3.2 Profiles: Profile display and management
- L3.3 Sessions: Session management, authentication state, current project context

<!-- section_id: "3cb44805-f5c4-46f3-9d06-8371baee0584" -->
### Dependency Shape
Sequence: Model → Profiles → Sessions (each builds on previous)

<!-- section_id: "83dda782-4ebf-46ee-958b-c555a97cdc2f" -->
## Triggers

| Situation | Action |
|-----------|--------|
| User data issues | Check model/ sub-layer |
| Profile problems | Check profiles/ sub-layer |
| Session/auth state | Check sessions/ sub-layer |

# ── Current Status ──

<!-- section_id: "33ffa1e3-5f28-49f9-a7f2-17f3e48c5bcf" -->
## Current Status

**Phase**: Routes extracted — user search and profile API routes
**Routes file**: routes.py (2 routes: user search, user profile)
**Key module**: sessions/session.py — provides get_user_info() used by all upper layers

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

<!-- section_id: "4c90fcf6-4978-4946-b504-328fcf86933e" -->
## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Session module | sessions/session.py |
| Parent context | ../0AGNOSTIC.md |
