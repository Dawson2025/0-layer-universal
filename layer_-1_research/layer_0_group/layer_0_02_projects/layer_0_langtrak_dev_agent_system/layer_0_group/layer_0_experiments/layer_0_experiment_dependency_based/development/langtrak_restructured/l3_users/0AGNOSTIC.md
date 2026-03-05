---
resource_id: "e110e59e-622f-4c0e-a07c-e8425aee96d8"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity

entity_id: "15103670-9902-4b01-89b1-8f45aa3f08b7"

**Role**: L3 Users Layer Agent
**Scope**: User model, profiles, sessions
**Depends On**: L2 Infrastructure (auth, firebase)
**Provides**: IUserProvider

## Key Behaviors

### Sub-layers
- L3.1 Model: User data structures and database operations
- L3.2 Profiles: Profile display and management
- L3.3 Sessions: Session management, authentication state, current project context

### Dependency Shape
Sequence: Model → Profiles → Sessions (each builds on previous)

## Triggers

| Situation | Action |
|-----------|--------|
| User data issues | Check model/ sub-layer |
| Profile problems | Check profiles/ sub-layer |
| Session/auth state | Check sessions/ sub-layer |

# ── Current Status ──

## Current Status

**Phase**: Routes extracted — user search and profile API routes
**Routes file**: routes.py (2 routes: user search, user profile)
**Key module**: sessions/session.py — provides get_user_info() used by all upper layers

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Session module | sessions/session.py |
| Parent context | ../0AGNOSTIC.md |
