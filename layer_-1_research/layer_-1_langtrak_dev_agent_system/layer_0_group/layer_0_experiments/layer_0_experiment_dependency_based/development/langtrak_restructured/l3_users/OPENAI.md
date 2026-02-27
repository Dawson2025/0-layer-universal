# OpenAI Context

## Identity

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


## Current Status

**Phase**: Routes extracted — user search and profile API routes
**Routes file**: routes.py (2 routes: user search, user profile)
**Key module**: sessions/session.py — provides get_user_info() used by all upper layers

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
