<!-- derived_from: "0c1fc353-10b3-45c0-883f-3b7a916bc6ed" -->
# AutoGen Agent Context

## Identity

**Role**: L2 Infrastructure Layer Agent
**Scope**: Foundation layer — everything the system needs to run
**Depends On**: Nothing (foundation layer)
**Provides**: IStorageProvider, IAuthProvider

## Key Behaviors

### Sub-layers
- L2.1 App Factory: Flask app creation, configuration, blueprint registration
- L2.2 Database: SQLite connection, schema migrations, session management
- L2.3 Firebase: Firebase Admin SDK, Firestore client, cloud authentication
- L2.4 Storage: Storage abstraction (local/cloud), file operations
- L2.5 Auth: User authentication (Firebase + email/password), session management, decorators
- L2.6 DB Admin: Database reset, default data restoration
- L2.7 Firebase Sync: Cloud synchronization of projects and data
- L2.8 TTS: Text-to-speech integration (Azure) for phoneme and word pronunciation

### Dependency Shape
Star topology — all sub-layers depend on L2.2 Database (hub)

## Triggers

| Situation | Action |
|-----------|--------|
| Auth issues | Check auth/ sub-layer |
| Database problems | Check database/ sub-layer |
| Firebase/cloud issues | Check firebase/ sub-layer |
| TTS failures | Check tts/ sub-layer |
| Storage errors | Check storage/ sub-layer |


## Current Status

**Phase**: Routes extracted from monolithic app.py into l2_bp Blueprint
**Routes file**: routes.py (health, auth, TTS, storage, db admin routes)
**Sub-layer packages**: database, firebase, storage, auth, tts, db_admin, firebase_sync, app_factory

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
