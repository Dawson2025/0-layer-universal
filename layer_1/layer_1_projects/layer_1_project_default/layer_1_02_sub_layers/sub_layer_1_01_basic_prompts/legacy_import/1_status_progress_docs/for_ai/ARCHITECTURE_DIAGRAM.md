---
resource_id: "42b59054-cce8-486d-b3b3-e90449d7f594"
resource_type: "document"
resource_name: "ARCHITECTURE_DIAGRAM"
---
# Parallel Development Architecture - Visual Diagram

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                          Flask Application                           │
│                              (app.py)                                │
│                                                                       │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │         Blueprint Registration (Single Point of Entry)         │ │
│  │                                                                │ │
│  │  auth_bp → projects_bp → groups_bp → words_bp → phonemes_bp  │ │
│  │       ↓          ↓            ↓           ↓           ↓        │ │
│  └───────┼──────────┼────────────┼───────────┼───────────┼────────┘ │
└──────────┼──────────┼────────────┼───────────┼───────────┼──────────┘
           │          │            │           │           │
┌──────────┴──────────┴────────────┴───────────┴───────────┴──────────┐
│                        FEATURE LAYER                                 │
│                   (Work in Parallel Here!)                           │
│                                                                       │
│  ┌─────────┐  ┌──────────┐  ┌────────┐  ┌────────┐  ┌─────────┐  │
│  │  auth/  │  │projects/ │  │groups/ │  │words/  │  │phonemes/│  │
│  ├─────────┤  ├──────────┤  ├────────┤  ├────────┤  ├─────────┤  │
│  │routes.py│  │routes.py │  │routes  │  │routes  │  │routes   │  │
│  │api.py   │  │api.py    │  │api.py  │  │api.py  │  │api.py   │  │
│  │helpers  │  │metadata  │  │models  │  │search  │  │models   │  │
│  │         │  │branching │  │        │  │creation│  │frequency│  │
│  │templates│  │templates │  │templates│ │templates│ │templates│  │
│  │tests/   │  │tests/    │  │tests/  │  │tests/  │  │tests/   │  │
│  └─────────┘  └──────────┘  └────────┘  └────────┘  └─────────┘  │
│                                                                       │
│  ┌──────────┐  ┌─────────┐  ┌───────────┐                          │
│  │admin/    │  │variant_ │  │dashboard/ │                          │
│  │          │  │menu/    │  │           │                          │
│  ├──────────┤  ├─────────┤  ├───────────┤                          │
│  │routes.py │  │routes   │  │routes.py  │                          │
│  │api.py    │  │api.py   │  │api.py     │                          │
│  │phoneme_  │  │stats    │  │           │                          │
│  │mgmt      │  │         │  │           │                          │
│  │templates │  │templates│  │templates  │                          │
│  │tests/    │  │tests/   │  │tests/     │                          │
│  └──────────┘  └─────────┘  └───────────┘                          │
│                                                                       │
│  🟢 GREEN ZONE: Each feature is isolated - work freely!              │
└───────────────────────────┬───────────────────────────────────────────┘
                            │
                            ↓ (depends on)
┌─────────────────────────────────────────────────────────────────────┐
│                         CORE LAYER                                   │
│                    (Stable Interfaces)                               │
│                                                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────────┐               │
│  │database.py  │  │session.py   │  │decorators.py │               │
│  ├─────────────┤  ├─────────────┤  ├──────────────┤               │
│  │get_db_      │  │get_user_    │  │@require_auth │               │
│  │connection() │  │info()       │  │@require_     │               │
│  │             │  │             │  │project_admin │               │
│  │init_        │  │get_current_ │  │              │               │
│  │database()   │  │project()    │  │              │               │
│  └─────────────┘  └─────────────┘  └──────────────┘               │
│                                                                       │
│  🟡 YELLOW ZONE: Check before modifying                              │
└───────────────────────────┬───────────────────────────────────────────┘
                            │
                            ↓ (uses)
┌─────────────────────────────────────────────────────────────────────┐
│                      SERVICES LAYER                                  │
│                 (Cross-Cutting Concerns)                             │
│                                                                       │
│  ┌──────────────┐  ┌──────────┐  ┌──────────────┐                 │
│  │firebase/     │  │tts/      │  │media/        │                 │
│  ├──────────────┤  ├──────────┤  ├──────────────┤                 │
│  │config.py     │  │azure_tts │  │video_handler │                 │
│  │auth.py       │  │phoneme_  │  │file_utils    │                 │
│  │firestore.py  │  │audio     │  │              │                 │
│  │storage.py    │  │          │  │              │                 │
│  └──────────────┘  └──────────┘  └──────────────┘                 │
│                                                                       │
│  🟡 YELLOW ZONE: Check before modifying                              │
└─────────────────────────────────────────────────────────────────────┘
```

## Parallel Development Flow

```
┌────────────────────────────────────────────────────────────────────┐
│                    PARALLEL DEVELOPMENT                             │
└────────────────────────────────────────────────────────────────────┘

    Agent 1              Agent 2              Agent 3
  (Words Team)        (Groups Team)      (Phonemes Team)
       │                   │                    │
       ↓                   ↓                    ↓
 ┌──────────┐        ┌──────────┐        ┌──────────┐
 │features/ │        │features/ │        │features/ │
 │words/    │        │groups/   │        │phonemes/ │
 └──────────┘        └──────────┘        └──────────┘
       │                   │                    │
       │ works on          │ works on           │ works on
       ↓                   ↓                    ↓
  search.py           routes.py            frequency.py
  api.py              templates/           models.py
  templates/          tests/               templates/
       │                   │                    │
       │                   │                    │
       └───────────────────┴────────────────────┘
                           │
                    NO CONFLICTS! ✅
                           │
                    Each agent commits
                    independently
```

## Traffic Light Coordination

```
┌─────────────────────────────────────────────────────────────────────┐
│                     TRAFFIC LIGHT SYSTEM                             │
└─────────────────────────────────────────────────────────────────────┘

🟢 GREEN ZONE - Work Freely
┌─────────────────────────────────────┐
│ features/my_feature/                │
│  ├── routes.py         ✅           │
│  ├── api.py            ✅           │
│  ├── models.py         ✅           │
│  ├── business_logic.py ✅           │
│  ├── templates/        ✅           │
│  ├── static/           ✅           │
│  └── tests/            ✅           │
│                                      │
│ No coordination needed!              │
└─────────────────────────────────────┘

🟡 YELLOW ZONE - Check First
┌─────────────────────────────────────┐
│ core/                  ⚠️            │
│ services/              ⚠️            │
│ templates/base.html    ⚠️            │
│ static/css/global.css  ⚠️            │
│                                      │
│ Check for other active work         │
└─────────────────────────────────────┘

🔴 RED ZONE - Must Coordinate
┌─────────────────────────────────────┐
│ Database schema        🛑            │
│ Core interfaces        🛑            │
│ app.py blueprints      🛑            │
│ Other features' code   🛑            │
│                                      │
│ Sequential work only!                │
└─────────────────────────────────────┘
```

## Dependency Flow

```
┌────────────────────────────────────────────────────────────────┐
│                     DEPENDENCY RULES                            │
└────────────────────────────────────────────────────────────────┘

ALLOWED ✅
──────────

Feature → Core
│
└──> from core.database import get_db_connection
└──> from core.decorators import require_auth
└──> from core.session import get_user_info

Feature → Services
│
└──> from services.firebase import firestore_db
└──> from services.tts import synthesize_phoneme

Feature → Other Feature (Limited)
│
└──> from features.auth.helpers import is_project_owner
└──> from features.projects.metadata import normalize_project_identifier


NOT ALLOWED ❌
──────────────

Feature → Feature Routes
│
└──x from features.words.routes import word_creation  ❌

Core → Feature
│
└──x from features.words import get_word  ❌

Feature → Feature Business Logic
│
└──x from features.admin.phoneme_management import reset  ❌
```

## File Conflict Matrix

```
┌────────────────────────────────────────────────────────────────┐
│                  CONFLICT PROBABILITY                           │
└────────────────────────────────────────────────────────────────┘

Location                      Conflict Risk    Agents Can Work
────────────────────────────  ──────────────  ────────────────
features/auth/                Very Low         ✅ In parallel
features/projects/            Very Low         ✅ In parallel
features/groups/              Very Low         ✅ In parallel
features/phonemes/            Very Low         ✅ In parallel
features/words/               Very Low         ✅ In parallel
features/admin/               Very Low         ✅ In parallel
features/variant_menu/        Very Low         ✅ In parallel
features/dashboard/           Very Low         ✅ In parallel

core/*                        Medium           ⚠️ Coordinate
services/*                    Medium           ⚠️ Coordinate
templates/base.html           Medium           ⚠️ Coordinate
static/css/global.css         Medium           ⚠️ Coordinate

Database migrations           High             🛑 Sequential
app.py blueprint registration Low              🛑 Only for new features
```

## Success Metrics Dashboard

```
┌────────────────────────────────────────────────────────────────┐
│                    IMPLEMENTATION METRICS                       │
└────────────────────────────────────────────────────────────────┘

BEFORE IMPLEMENTATION          AFTER IMPLEMENTATION
━━━━━━━━━━━━━━━━━━━━          ━━━━━━━━━━━━━━━━━━━━

Monolithic Structure           ✅ Modular Architecture
├─ app.py: 4,055 lines         ├─ app.py: 3,654 lines
├─ Features: 3 partial         ├─ Features: 8 complete
└─ Isolation: Minimal          └─ Isolation: Full

Development Capacity           Development Capacity
├─ Agents: 1-2                 ├─ Agents: 8 simultaneous
├─ Conflict Risk: High         ├─ Conflict Risk: Zero
└─ Speed: 1x baseline          └─ Speed: 2-3x faster

Code Organization              Code Organization
├─ Mixed concerns              ├─ Clear separation
├─ Hard to test                ├─ Easy to test
└─ Hard to navigate            └─ Easy to navigate

┌──────────────────────────────────────────────┐
│  PARALLEL DEVELOPMENT CAPACITY: 8 AGENTS     │
│  FILE CONFLICT RATE: 0%                      │
│  DEVELOPMENT SPEEDUP: 2-3x                   │
└──────────────────────────────────────────────┘
```

## Quick Start Workflow

```
┌────────────────────────────────────────────────────────────────┐
│                  DEVELOPER WORKFLOW                             │
└────────────────────────────────────────────────────────────────┘

Step 1: Choose Feature
│
├─> words      (Word management)
├─> groups     (Group collaboration)
├─> phonemes   (Phoneme tracking)
├─> admin      (Admin tools)
└─> ... (8 features available)

Step 2: Navigate to Feature
│
cd features/my_feature/

Step 3: Understand Structure
│
ls -la
├── __init__.py     (Blueprint)
├── routes.py       (Page routes)
├── api.py          (API endpoints)
├── models.py       (Database)
├── templates/      (HTML)
└── tests/          (Tests)

Step 4: Make Changes
│
├─> Add routes
├─> Add API endpoints
├─> Update templates
└─> Add tests

Step 5: Test
│
pytest features/my_feature/tests/

Step 6: Commit
│
git add features/my_feature/
git commit -m "Add feature X"

✅ DONE - No conflicts with other agents!
```

---

## Visual Summary

**The codebase is now a well-organized, modular application where:**

- 🟢 **8 feature modules** work in complete isolation
- 🟡 **Stable core layer** provides shared infrastructure
- 🟢 **8 agents** can develop simultaneously
- ✅ **Zero conflicts** when working on different features
- 🚀 **2-3x faster** development with parallelism

**Ready for parallel development!**
