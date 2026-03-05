---
resource_id: "2fe6166c-d64e-4ce4-bc77-04f8e885cb29"
resource_type: "document"
resource_name: "PARALLEL_DEVELOPMENT_ARCHITECTURE"
---
# Parallel Development Architecture

<!-- section_id: "45e73a66-bd9c-4877-8654-962d5e11bf14" -->
## Purpose

This document defines the optimal code organization for the Language Tracker application to enable multiple AI agents (or human developers) to work on different features simultaneously without file conflicts or integration issues.

<!-- section_id: "512fe6ef-d696-49a1-8276-2b56033fc632" -->
## Current State Analysis

<!-- section_id: "ca9047c4-af60-4ab3-8315-c1ceb6eb4df2" -->
### Problems with Current Structure

1. **Monolithic app.py (4,055 lines)**: All routes, business logic, and API endpoints are in one file
2. **Mixed templates directory**: All HTML templates are flat in `/templates/` without feature grouping
3. **Scattered test files**: ~20 test files in root directory with unclear organization
4. **Minimal static assets organization**: JavaScript and CSS not separated by feature
5. **Limited feature isolation**: Only 3 feature modules started (`auth`, `firebase`, `projects`)

<!-- section_id: "449c25e7-1693-4f1b-91b4-21152d8bbd2a" -->
### What's Working

1. **Features directory exists**: Good foundation at `/features/` with Python package structure
2. **Some extraction started**: `auth/helpers.py` and `projects/metadata.py` show good patterns
3. **Docs are organized**: `/docs/for_ai/requirements/` has clear feature specs
4. **Template naming**: Templates use descriptive names that map to features

---

<!-- section_id: "2dfe3416-f286-41d1-911b-1fd3ec4ff3b7" -->
## Proposed Architecture

<!-- section_id: "18a05c2d-98ec-4aee-88ee-a67785c1e9fa" -->
### Core Principles

1. **Feature Isolation**: Each feature owns its routes, templates, static assets, business logic, and tests
2. **Shared Infrastructure**: Common utilities, database access, and cross-cutting concerns in dedicated modules
3. **Interface Contracts**: Clear APIs between features to minimize coupling
4. **Parallel Safety**: Multiple developers can work on different features without touching the same files

<!-- section_id: "925e4240-c26f-40fb-82f3-054f7e63e2fb" -->
### Directory Structure

```
lang-trak-in-progress/
│
├── app.py                          # Minimal Flask app - just blueprints and config
├── config.py                       # Application configuration
├── main.py                         # Entry point and database setup
│
├── core/                           # Shared infrastructure (rarely changes)
│   ├── __init__.py
│   ├── database.py                 # Database connection and helpers
│   ├── session.py                  # Session management utilities
│   ├── decorators.py               # Common decorators (auth, etc.)
│   └── exceptions.py               # Custom exceptions
│
├── services/                       # Cross-cutting services (shared but change more often)
│   ├── __init__.py
│   ├── firebase/
│   │   ├── __init__.py
│   │   ├── config.py               # Firebase configuration
│   │   ├── auth.py                 # Firebase authentication
│   │   ├── firestore.py            # Firestore database operations
│   │   └── storage.py              # Firebase Storage operations
│   ├── tts/
│   │   ├── __init__.py
│   │   ├── azure_tts.py            # Azure TTS integration
│   │   └── phoneme_audio.py        # Phoneme pronunciation logic
│   └── media/
│       ├── __init__.py
│       ├── video_handler.py        # Video upload/storage
│       └── file_utils.py           # File handling utilities
│
├── features/                       # Feature modules (THIS IS WHERE PARALLEL WORK HAPPENS)
│   │
│   ├── auth/                       # Level 0: Authentication
│   │   ├── __init__.py             # Exports blueprint
│   │   ├── routes.py               # /login, /register, /logout routes
│   │   ├── helpers.py              # get_user_info, require_auth (EXISTS)
│   │   ├── templates/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── tests/
│   │       └── test_auth.py
│   │
│   ├── dashboard/                  # Level 1: Dashboard
│   │   ├── __init__.py
│   │   ├── routes.py               # /dashboard route
│   │   ├── templates/
│   │   │   └── dashboard.html
│   │   └── tests/
│   │       └── test_dashboard.py
│   │
│   ├── groups/                     # Level 1: Group Collaboration
│   │   ├── __init__.py
│   │   ├── routes.py               # /groups/* routes
│   │   ├── models.py               # Group-related database operations
│   │   ├── templates/
│   │   │   ├── groups_menu.html
│   │   │   ├── group_detail.html
│   │   │   └── create_group.html
│   │   ├── static/
│   │   │   └── js/
│   │   │       └── group_invite.js
│   │   └── tests/
│   │       ├── test_group_creation.py
│   │       └── test_group_invites.py
│   │
│   ├── projects/                   # Level 2: Project Management
│   │   ├── __init__.py
│   │   ├── routes.py               # /projects/* routes (list, create, edit)
│   │   ├── api.py                  # API endpoints for projects
│   │   ├── metadata.py             # Project identifier helpers (EXISTS)
│   │   ├── branching.py            # Branch/merge operations
│   │   ├── sharing.py              # Project sharing logic
│   │   ├── storage_ops.py          # Migrate to cloud, fork to local
│   │   ├── templates/
│   │   │   ├── projects_menu.html
│   │   │   ├── create_project.html
│   │   │   ├── edit_project.html
│   │   │   └── admin_storage.html
│   │   ├── static/
│   │   │   ├── js/
│   │   │   │   ├── project_search.js
│   │   │   │   └── project_actions.js
│   │   │   └── css/
│   │   │       └── projects.css
│   │   └── tests/
│   │       ├── test_project_crud.py
│   │       ├── test_branching.py
│   │       ├── test_cloud_actions.py
│   │       └── test_project_search.py
│   │
│   ├── variant_menu/               # Level 3: Variant/Project Menu
│   │   ├── __init__.py
│   │   ├── routes.py               # /main-menu route
│   │   ├── stats.py                # Project statistics calculation
│   │   ├── templates/
│   │   │   └── main_menu.html
│   │   └── tests/
│   │       └── test_variant_menu.py
│   │
│   ├── phonemes/                   # Level 4a: Phonemes
│   │   ├── __init__.py
│   │   ├── routes.py               # /phonemes/* routes (views)
│   │   ├── api.py                  # /api/phonemes/* endpoints
│   │   ├── models.py               # Phoneme database operations
│   │   ├── frequency.py            # Frequency calculation logic
│   │   ├── templates/
│   │   │   ├── phonemes_flat.html
│   │   │   ├── phonemes_nested.html
│   │   │   └── phonemes_full.html
│   │   ├── static/
│   │   │   ├── js/
│   │   │   │   └── phoneme_display.js
│   │   │   └── css/
│   │   │       └── phonemes.css
│   │   └── tests/
│   │       ├── test_phoneme_views.py
│   │       └── test_phoneme_frequency.py
│   │
│   ├── words/                      # Level 4b: Words
│   │   ├── __init__.py
│   │   ├── routes.py               # /words/* routes
│   │   ├── api.py                  # /api/create-word, etc.
│   │   ├── models.py               # Word database operations
│   │   ├── search.py               # Search logic (all fields, etc.)
│   │   ├── creation.py             # Word creation logic
│   │   ├── templates/
│   │   │   ├── words_menu.html
│   │   │   ├── words_display.html
│   │   │   ├── add_word.html
│   │   │   ├── word_creation_table.html
│   │   │   ├── word_lookup.html
│   │   │   └── word_edit.html
│   │   ├── static/
│   │   │   ├── js/
│   │   │   │   ├── word_creation.js
│   │   │   │   ├── word_search.js
│   │   │   │   └── phoneme_blocks.js
│   │   │   └── css/
│   │   │       ├── word_creation.css
│   │   │       └── word_display.css
│   │   └── tests/
│   │       ├── test_word_creation.py
│   │       ├── test_word_editing.py
│   │       ├── test_word_search.py
│   │       └── test_all_fields_search.py
│   │
│   └── admin/                      # Level 4c: Administration
│       ├── __init__.py
│       ├── routes.py               # /admin/* routes
│       ├── api.py                  # /api/admin/* endpoints
│       ├── phoneme_management.py   # Admin phoneme operations
│       ├── template_system.py      # Template import/export/apply
│       ├── database_tools.py       # Database maintenance utilities
│       ├── templates/
│       │   ├── admin_menu.html
│       │   ├── admin_phonemes.html
│       │   └── admin_templates.html
│       ├── static/
│       │   ├── js/
│       │   │   └── admin_actions.js
│       │   └── css/
│       │       └── admin.css
│       └── tests/
│           ├── test_phoneme_admin.py
│           ├── test_template_system.py
│           └── test_database_tools.py
│
├── templates/                      # Global/shared templates only
│   ├── base.html                   # Base template with common layout
│   ├── index.html                  # Root redirect page
│   └── components/                 # Reusable template components
│       ├── navbar.html
│       └── flash_messages.html
│
├── static/                         # Global/shared static files only
│   ├── css/
│   │   ├── global.css              # Application-wide styles
│   │   └── components.css          # Reusable component styles
│   ├── js/
│   │   ├── firebase-config.js      # Firebase client config
│   │   └── global.js               # Global JavaScript utilities
│   └── images/
│       └── logo.svg
│
├── tests/                          # Integration and end-to-end tests only
│   ├── __init__.py
│   ├── conftest.py                 # Pytest fixtures
│   ├── integration/
│   │   └── test_cloud_integration.py   # Firebase integration tests
│   ├── test_integration.py         # Cross-feature integration tests
│   ├── test_end_to_end.py          # Full user workflow tests
│   └── test_user_story.py          # User story acceptance tests
│
├── migrations/                     # Database migrations (if using Alembic)
│   └── versions/
│
├── scripts/                        # Utility scripts (cleanup from root)
│   ├── add_sample_words.py
│   ├── fix_database.py
│   └── sample_data.py
│
└── docs/
    └── for_ai/
        ├── requirements/           # Feature requirements (already good)
        ├── PARALLEL_DEVELOPMENT_ARCHITECTURE.md  # This file
        └── DEVELOPMENT_CONVENTIONS.md            # Rules for parallel work
```

---

<!-- section_id: "041093e1-8932-45e1-a57a-cfb8b63ff4f9" -->
## Feature Ownership Matrix

This table shows which files/folders each feature "owns" for parallel development:

| Feature Area | Routes Owned | Templates Owned | Static Assets | Tests | Dependencies |
|--------------|-------------|-----------------|---------------|-------|--------------|
| **auth** | `/login`, `/register`, `/logout`, `/api/auth/*` | `auth/templates/*.html` | None | `auth/tests/` | `core.database`, `services.firebase.auth` |
| **dashboard** | `/dashboard` | `dashboard/templates/*.html` | None | `dashboard/tests/` | `auth.helpers` |
| **groups** | `/groups/*` | `groups/templates/*.html` | `groups/static/js/` | `groups/tests/` | `auth.helpers`, `core.database` |
| **projects** | `/projects/*`, `/api/projects/*`, `/api/project-groups/*` | `projects/templates/*.html` | `projects/static/` | `projects/tests/` | `auth.helpers`, `services.firebase`, `core.database` |
| **variant_menu** | `/main-menu`, `/projects/enter`, `/projects/exit` | `variant_menu/templates/*.html` | None | `variant_menu/tests/` | `auth.helpers`, `projects.metadata` |
| **phonemes** | `/phonemes/*`, `/api/phonemes/*` | `phonemes/templates/*.html` | `phonemes/static/` | `phonemes/tests/` | `auth.helpers`, `services.tts` |
| **words** | `/words/*`, `/api/create-word`, `/api/lookup-word`, `/api/update-word/*`, `/api/delete-word/*`, `/api/remove-video/*` | `words/templates/*.html` | `words/static/` | `words/tests/` | `auth.helpers`, `services.media`, `services.tts`, `phonemes.models` |
| **admin** | `/admin/*`, `/api/admin/*`, `/api/templates/*` | `admin/templates/*.html` | `admin/static/` | `admin/tests/` | `auth.helpers`, `phonemes.models`, `words.models` |

---

<!-- section_id: "dc6e550e-f7c7-45ae-807d-729ef1daeeeb" -->
## Shared Dependencies (Interfaces)

These modules are shared across features and should have stable interfaces:

<!-- section_id: "31a93d60-df82-426d-9e28-5adf34699cf3" -->
### Core Layer (Rarely Changes)

**`core/database.py`**
```python
def get_db_connection() -> sqlite3.Connection
def execute_query(query: str, params: tuple) -> Any
def transaction(func: Callable) -> Callable  # Decorator for transactions
```

**`core/decorators.py`**
```python
def require_auth(func: Callable) -> Callable
def require_project_admin(func: Callable) -> Callable
```

**`core/session.py`**
```python
def get_current_user_id() -> Optional[int]
def get_current_project_id() -> Optional[str]
def set_current_project(project_id: str) -> None
```

<!-- section_id: "588590d3-34dd-465f-b7e7-4df552ea8d73" -->
### Services Layer (Shared Logic)

**`services/firebase/firestore.py`**
```python
class FirestoreDB:
    def get_project(project_id: str) -> Optional[Dict]
    def create_project(data: Dict) -> str
    def update_project(project_id: str, data: Dict) -> bool
    # ... other Firestore operations
```

**`services/tts/azure_tts.py`**
```python
def synthesize_phoneme(ipa_symbol: str) -> Tuple[bool, str]  # (success, audio_data)
def synthesize_word(ipa_sequence: str) -> Tuple[bool, str]
def check_phoneme_pronounceable(ipa_symbol: str) -> bool
```

**`services/media/video_handler.py`**
```python
def save_video(file: FileStorage, project_id: str, word_id: int) -> str  # Returns path
def delete_video(video_path: str) -> bool
def get_video_url(video_path: str) -> str
```

<!-- section_id: "2c3252f2-dee8-4ac4-b32a-fc81985328b4" -->
### Feature-to-Feature Interfaces

**`auth/helpers.py`** (Already exists)
```python
def get_user_info() -> Dict[str, Any]
def is_project_owner(project_id: Any, user_id: Any) -> bool
```

**`projects/metadata.py`** (Already exists)
```python
def normalize_project_identifier(project_id: str) -> Tuple[str, str, str]
def fetch_project_metadata(storage_type: str, identifier: str) -> Optional[Dict]
```

**`phonemes/models.py`** (To be created)
```python
def get_phoneme(phoneme_id: int, project_id: str) -> Optional[Dict]
def get_all_phonemes(project_id: str) -> List[Dict]
def update_phoneme_frequency(phoneme_id: int, delta: int) -> bool
```

**`words/models.py`** (To be created)
```python
def get_word(word_id: int, project_id: str) -> Optional[Dict]
def create_word(data: Dict, project_id: str) -> int
def search_words(query: str, project_id: str, fields: List[str]) -> List[Dict]
```

---

<!-- section_id: "bb3dc417-8b8c-4ba8-a923-7705fac5eb30" -->
## Parallel Development Workflow

<!-- section_id: "d6554984-ac68-44d8-b730-3c7a73c65963" -->
### How AI Agents Work in Parallel

#### Scenario 1: Three Features at Once

**Agent 1** - Working on "All Fields Search" (words feature)
- Modifies: `features/words/search.py`
- Modifies: `features/words/api.py` (one function)
- Modifies: `features/words/templates/words_display.html`
- Adds: `features/words/tests/test_all_fields_search.py`

**Agent 2** - Working on "Group Invitations" (groups feature)
- Modifies: `features/groups/routes.py`
- Modifies: `features/groups/templates/group_detail.html`
- Modifies: `features/groups/static/js/group_invite.js`
- Adds: `features/groups/tests/test_group_invites.py`

**Agent 3** - Working on "Phoneme Template System" (admin feature)
- Modifies: `features/admin/template_system.py`
- Modifies: `features/admin/api.py`
- Modifies: `features/admin/templates/admin_templates.html`
- Adds: `features/admin/tests/test_template_system.py`

**Result**: ZERO file conflicts! Each agent works in isolated feature directories.

#### Scenario 2: When Shared Code Changes

**Problem**: Agent needs to add new function to `auth/helpers.py` (shared module)

**Solution 1 - Sequential Approach**:
1. Agent 1 creates PR with `auth/helpers.py` changes
2. Merge to main
3. Agents 2 and 3 pull latest main before starting their work

**Solution 2 - Interface Contract Approach**:
1. Define new function signature in `auth/helpers.py` stub first (merge this)
2. Multiple agents can now import and use it (with type hints)
3. Implementation filled in separately

**Solution 3 - Dependency Injection**:
```python
# Agent's feature code doesn't directly call shared function
# Instead, it receives it as a parameter or uses a registry pattern
def my_feature_function(get_user_func=get_user_info):
    user = get_user_func()
    # ... feature logic
```

<!-- section_id: "8aa8422b-262f-428e-a1d4-4631c058e946" -->
### Development Checklist

Before starting work on a feature, verify:

- [ ] I know which feature directory I'm working in (`features/<feature_name>/`)
- [ ] I've checked if any shared dependencies need changes
- [ ] If I'm modifying shared code, I've coordinated with other agents/PRs
- [ ] My tests are self-contained within my feature's test directory
- [ ] I'm not modifying `app.py` unless registering a new blueprint
- [ ] Templates I create go in my feature's `templates/` subdirectory
- [ ] Static assets go in my feature's `static/` subdirectory

---

<!-- section_id: "ed008083-d9f7-4532-81d2-96c2855aeca5" -->
## Migration Plan

<!-- section_id: "0095d9b4-98be-4fce-a144-dd6cd4a63c0c" -->
### Phase 1: Extract Core Infrastructure (Foundation)

**Goal**: Create stable shared layer that all features depend on

**Files to Create**:
- `core/database.py` - Extract DB connection logic from `main.py` and `app.py`
- `core/session.py` - Extract session helpers
- `core/decorators.py` - Move `@require_auth` and `@require_project_admin` from `auth/helpers.py`

**Estimated Conflicts**: Low - This is mostly extraction, not modification

<!-- section_id: "9d3b6af4-7465-47ef-bb8a-3a38a95b27a8" -->
### Phase 2: Extract Services (Shared Business Logic)

**Goal**: Isolate cross-cutting services

**Files to Move/Refactor**:
- `firebase_service.py` → `services/firebase/firestore.py`
- `firestore_db.py` → `services/firebase/firestore.py` (merge)
- `firebase_config.py` → `services/firebase/config.py`
- `tts_ipa.py` → `services/tts/azure_tts.py`
- Video handling from `app.py` → `services/media/video_handler.py`

**Estimated Conflicts**: Medium - Multiple features may touch these during phase 2

<!-- section_id: "b75c9f57-5531-4816-8958-28d56cb2f100" -->
### Phase 3: Feature Extraction (Can be done in parallel!)

Each feature can be extracted independently:

**Phase 3a - Auth Feature** (Low risk)
- Create `features/auth/routes.py`
- Move routes: `login`, `register`, `logout`, `firebase_login`, `api_logout` from `app.py`
- Move templates: `login.html`, `register.html` to `features/auth/templates/`
- Already have: `features/auth/helpers.py`
- Create: `features/auth/__init__.py` with Flask Blueprint

**Phase 3b - Groups Feature** (Low risk, isolated)
- Create `features/groups/routes.py`
- Move routes: `groups_menu`, `create_group`, `group_detail`, `join_group_via_invite`, etc.
- Move templates: `groups_menu.html`, `group_detail.html`, `create_group.html`
- Create: `features/groups/models.py` for DB operations

**Phase 3c - Projects Feature** (Medium risk - central feature)
- Create `features/projects/routes.py`
- Move routes: All `/projects/*` routes
- Already have: `features/projects/metadata.py`
- Create: `features/projects/branching.py`, `features/projects/sharing.py`
- Move templates: `projects_menu.html`, `create_project.html`, etc.

**Phase 3d - Variant Menu Feature** (Low risk)
- Create `features/variant_menu/routes.py`
- Move routes: `main_menu`, `enter_project`, `exit_project`
- Move template: `main_menu.html`

**Phase 3e - Phonemes Feature** (Low risk, isolated)
- Create `features/phonemes/routes.py`
- Move routes: All `/phonemes/*` routes
- Create: `features/phonemes/models.py`, `features/phonemes/frequency.py`
- Move templates: `phonemes_*.html`

**Phase 3f - Words Feature** (High complexity, but isolated)
- Create `features/words/routes.py`, `features/words/api.py`
- Move routes: All `/words/*` and word-related API routes
- Create: `features/words/models.py`, `features/words/search.py`, `features/words/creation.py`
- Move templates: All word templates
- Most complex feature, but self-contained

**Phase 3g - Admin Feature** (Medium complexity)
- Create `features/admin/routes.py`, `features/admin/api.py`
- Move routes: All `/admin/*` and `/api/admin/*` routes
- Create: `features/admin/phoneme_management.py`, `features/admin/template_system.py`
- Move templates: `admin_*.html`

<!-- section_id: "d7ca4e45-559d-4e1e-942d-fc678a3139fb" -->
### Phase 4: Update app.py (Final integration)

**Goal**: Convert `app.py` to just blueprint registration

```python
# New streamlined app.py (~100 lines instead of 4,055)
from flask import Flask, redirect, url_for
from core.database import init_db
from features.auth import auth_bp
from features.dashboard import dashboard_bp
from features.groups import groups_bp
from features.projects import projects_bp
from features.variant_menu import variant_menu_bp
from features.phonemes import phonemes_bp
from features.words import words_bp
from features.admin import admin_bp

app = Flask(__name__)
app.config.from_object('config')

# Initialize database
init_db()

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(groups_bp)
app.register_blueprint(projects_bp)
app.register_blueprint(variant_menu_bp)
app.register_blueprint(phonemes_bp)
app.register_blueprint(words_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
```

<!-- section_id: "b06b9a52-9ccd-4ea7-a024-e948f5b86313" -->
### Phase 5: Cleanup

- Move test files from root to appropriate `features/*/tests/` directories
- Move scripts from root to `scripts/` directory
- Update all imports across the codebase
- Update documentation

---

<!-- section_id: "be78c466-3f1a-4e3d-9b92-ac813b42645c" -->
## Parallel Development Rules

<!-- section_id: "a03fcb6b-a061-4323-bdf9-d962d27ffb6f" -->
### Golden Rules for AI Agents

1. **One Feature, One PR**: Each feature change should only touch files in that feature's directory (+ tests)

2. **Shared Code Changes Require Coordination**: If you need to modify `core/*` or `services/*`:
   - Check if another agent's PR is already modifying it
   - Consider if your feature can work with current interface
   - If must change, coordinate merge order

3. **Blueprint Registration**: Only modify `app.py` blueprint registration when adding entirely new feature areas

4. **Test Isolation**: Feature tests should mock dependencies from other features

5. **Template Inheritance**: Use global `base.html` but don't modify it without coordination

6. **Database Migrations**: Coordinate schema changes - only one agent should create migration at a time

<!-- section_id: "81f3c0d0-9595-4ffd-8dd2-40814b2141ea" -->
### File Conflict Probability Matrix

| File/Directory | Conflict Risk | Mitigation |
|----------------|---------------|------------|
| `features/<feature_name>/` | **Very Low** | Primary work area - isolated per feature |
| `core/*` | **Medium** | Stable interfaces - rarely needs changes |
| `services/*` | **Medium-High** | Use interface contracts; coordinate changes |
| `app.py` | **Low** | Only changed for new blueprints |
| `templates/base.html` | **Medium** | Coordinate major layout changes |
| `static/css/global.css` | **Medium** | Use feature-specific CSS when possible |
| `tests/` (integration) | **Low** | End-to-end tests - add new files |
| `migrations/` | **High** | Sequential only - coordinate DB changes |

<!-- section_id: "45f7f7f3-11bc-428f-9f91-558b676d5fe3" -->
### Recommended Parallel Work Patterns

**Pattern 1: Vertical Slice**
- Agent owns entire vertical slice: routes → templates → logic → tests
- Example: "Mobile Word Creation Flow" touches only `features/words/`

**Pattern 2: Horizontal Concerns**
- Each agent works on same concern across multiple features
- Example: Agent 1 adds search to words, Agent 2 adds search to phonemes
- Works if features are isolated!

**Pattern 3: New Feature + Enhancement**
- Agent 1: Creates entirely new feature in new directory
- Agent 2: Enhances existing feature
- Zero overlap possible

**Anti-Pattern: Shared File Editing**
- ❌ Agent 1 and Agent 2 both modifying `app.py` routes
- ✅ Instead: Use blueprints, each agent registers their own

---

<!-- section_id: "d485c123-b400-4619-800c-5451cd7b9127" -->
## Benefits of This Architecture

<!-- section_id: "b31db896-33e8-4587-a3d4-f97c7255b2c5" -->
### For Parallel AI Development

1. **Conflict Avoidance**: Features in separate directories = no merge conflicts
2. **Clear Ownership**: Each agent knows exactly which files it can modify
3. **Independent Testing**: Each feature has its own test suite
4. **Faster Iteration**: No waiting for other agents to finish in same file

<!-- section_id: "0361d0f7-5e9d-4c49-b223-2ac4798337fd" -->
### For Code Quality

1. **Modularity**: Features are self-contained and testable
2. **Maintainability**: Easy to find code related to a feature
3. **Scalability**: New features add new directories, don't expand existing files
4. **Clarity**: Directory structure matches feature requirements docs

<!-- section_id: "4f7973f0-9f6d-4bd5-b9a2-e6ab69c6e85f" -->
### For Debugging

1. **Feature Tracing**: Bug in words? Look in `features/words/`
2. **Dependency Tracking**: Clear imports show what each feature needs
3. **Test Isolation**: Feature tests can run independently

---

<!-- section_id: "f3b11001-76bc-45d3-8c05-75ac42eda869" -->
## Migration Effort Estimate

| Phase | Effort | Risk | Can Parallelize? |
|-------|--------|------|------------------|
| Phase 1: Core | 4 hours | Low | No - Foundation |
| Phase 2: Services | 6 hours | Medium | Partially (2-3 services at once) |
| Phase 3: Features | 20 hours | Low | **YES - All 8 features in parallel!** |
| Phase 4: app.py Update | 2 hours | Low | No - Final integration |
| Phase 5: Cleanup | 4 hours | Low | Yes |
| **Total Sequential** | **36 hours** | | |
| **Total with Parallelism** | **~16 hours** | | Phase 3 done by 8 agents at once |

---

<!-- section_id: "d26d7a90-07bd-455e-9d21-503245a6383a" -->
## Success Criteria

The migration is successful when:

- [ ] `app.py` is under 200 lines (currently 4,055)
- [ ] Each feature has its own directory under `features/`
- [ ] Feature tests are colocated with feature code
- [ ] All existing tests pass
- [ ] Three AI agents can work on three different features simultaneously without conflicts
- [ ] New features can be added by creating new feature directories
- [ ] Documentation maps features to directories (update requirements README)

---

<!-- section_id: "0c38acbb-5154-4d34-baa8-016a129cd03d" -->
## Next Steps

1. **Review and approve this architecture** with stakeholders
2. **Create Phase 1 (Core infrastructure)** - Required foundation
3. **Extract one pilot feature** (recommend `groups` - smallest, most isolated)
4. **Validate parallel development** with two agents on different features
5. **Extract remaining features** in parallel
6. **Update documentation** to reference new structure

---

<!-- section_id: "546864c7-4d3d-4bcb-8eba-3d0f010142c5" -->
## Related Documentation

- [Requirements Overview](requirements/README.md) - Maps features to this architecture
- [Parallel Feature Isolation](requirements/parallel_feature_isolation.md) - Original motivation
- Development Conventions (to be created) - Coding standards for parallel work
