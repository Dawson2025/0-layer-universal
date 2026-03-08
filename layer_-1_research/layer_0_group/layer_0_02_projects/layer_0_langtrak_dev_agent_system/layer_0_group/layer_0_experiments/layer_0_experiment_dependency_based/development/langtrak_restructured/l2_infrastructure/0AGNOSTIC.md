---
resource_id: "06d6706e-6094-4e27-9b51-9351a6c327a0"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

<!-- section_id: "3f48acac-677d-4203-af33-4ffac25d50d2" -->
## Identity

entity_id: "0c1fc353-10b3-45c0-883f-3b7a916bc6ed"

**Role**: L2 Infrastructure Layer Agent
**Scope**: Foundation layer — everything the system needs to run
**Depends On**: Nothing (foundation layer)
**Provides**: IStorageProvider, IAuthProvider

<!-- section_id: "b8e09502-6f7f-4ab1-8e0b-9c41db68a364" -->
## Key Behaviors

<!-- section_id: "bbb3466f-c30c-4766-88f0-a8fd99426107" -->
### Sub-layers
- L2.1 App Factory: Flask app creation, configuration, blueprint registration
- L2.2 Database: SQLite connection, schema migrations, session management
- L2.3 Firebase: Firebase Admin SDK, Firestore client, cloud authentication
- L2.4 Storage: Storage abstraction (local/cloud), file operations
- L2.5 Auth: User authentication (Firebase + email/password), session management, decorators
- L2.6 DB Admin: Database reset, default data restoration
- L2.7 Firebase Sync: Cloud synchronization of projects and data
- L2.8 TTS: Text-to-speech integration (Azure) for phoneme and word pronunciation

<!-- section_id: "12385858-d7cc-42aa-a1a1-117c0256edd4" -->
### Dependency Shape
Star topology — all sub-layers depend on L2.2 Database (hub)

<!-- section_id: "8d84f28c-403d-410d-9458-70bd7284f89c" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Auth issues | Check auth/ sub-layer |
| Database problems | Check database/ sub-layer |
| Firebase/cloud issues | Check firebase/ sub-layer |
| TTS failures | Check tts/ sub-layer |
| Storage errors | Check storage/ sub-layer |

# ── Current Status ──

<!-- section_id: "f1335662-e555-488d-984e-bdc5461da671" -->
## Current Status

**Phase**: Routes extracted from monolithic app.py into l2_bp Blueprint
**Routes file**: routes.py (health, auth, TTS, storage, db admin routes)
**Sub-layer packages**: database, firebase, storage, auth, tts, db_admin, firebase_sync, app_factory

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── References ──

<!-- section_id: "15f16bf0-8b25-43d3-8967-05b1da31f02d" -->
## Navigation

| Resource | Path |
|----------|------|
| Blueprint | __init__.py |
| Routes | routes.py |
| Parent context | ../0AGNOSTIC.md |
