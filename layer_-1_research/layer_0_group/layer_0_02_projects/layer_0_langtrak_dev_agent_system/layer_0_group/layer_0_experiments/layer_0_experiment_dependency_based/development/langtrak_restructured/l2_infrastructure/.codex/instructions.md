---
resource_id: "27849cf1-870c-429f-9a75-f6f5031611e5"
resource_type: "document"
resource_name: "instructions"
---
# AutoGen Agent Context

<!-- section_id: "4409241f-9b46-4bdf-855b-afa6ab9322df" -->
## Identity

**Role**: L2 Infrastructure Layer Agent
**Scope**: Foundation layer — everything the system needs to run
**Depends On**: Nothing (foundation layer)
**Provides**: IStorageProvider, IAuthProvider

<!-- section_id: "8de4f62c-d27d-4751-a1c2-01e8035705eb" -->
## Key Behaviors

<!-- section_id: "8d0bd699-3781-43b7-9c3c-955dc8c09432" -->
### Sub-layers
- L2.1 App Factory: Flask app creation, configuration, blueprint registration
- L2.2 Database: SQLite connection, schema migrations, session management
- L2.3 Firebase: Firebase Admin SDK, Firestore client, cloud authentication
- L2.4 Storage: Storage abstraction (local/cloud), file operations
- L2.5 Auth: User authentication (Firebase + email/password), session management, decorators
- L2.6 DB Admin: Database reset, default data restoration
- L2.7 Firebase Sync: Cloud synchronization of projects and data
- L2.8 TTS: Text-to-speech integration (Azure) for phoneme and word pronunciation

<!-- section_id: "ac1949f2-43a4-4a75-a5e8-cddcc93c2db1" -->
### Dependency Shape
Star topology — all sub-layers depend on L2.2 Database (hub)

<!-- section_id: "33b72bf6-c3cb-4e7b-8294-b412db018222" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Auth issues | Check auth/ sub-layer |
| Database problems | Check database/ sub-layer |
| Firebase/cloud issues | Check firebase/ sub-layer |
| TTS failures | Check tts/ sub-layer |
| Storage errors | Check storage/ sub-layer |


<!-- section_id: "d225827f-89e0-4ea1-8724-35e8a3f77635" -->
## Current Status

**Phase**: Routes extracted from monolithic app.py into l2_bp Blueprint
**Routes file**: routes.py (health, auth, TTS, storage, db admin routes)
**Sub-layer packages**: database, firebase, storage, auth, tts, db_admin, firebase_sync, app_factory

<!-- section_id: "ae318ef8-d0ef-4902-a6e4-98518327cbd4" -->
## AutoGen-Specific Configuration

<!-- section_id: "48077d9b-709d-451f-9330-e3f72f74112f" -->
### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

<!-- section_id: "87506ec9-b859-45bb-a7b8-438f144ebe1f" -->
### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
