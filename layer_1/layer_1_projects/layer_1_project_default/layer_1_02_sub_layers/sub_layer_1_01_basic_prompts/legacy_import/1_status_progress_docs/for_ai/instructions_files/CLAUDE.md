<!-- derived_from: "d39b1b99-83b0-4e73-96b4-22fd8b03e835" -->
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 🚨 Terminal Execution Protocol

**MANDATORY**: See `0_context/trickle_down_0_universal/0_instruction_docs/MASTER_DOCUMENTATION.md` for complete documentation.

**Universal Terminal Execution**: See `0_context/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_TERMINAL_EXECUTION.md` for universal best practices.

**Quick Reference for Claude Code:**
- Node.js commands → `run_terminal_cmd("npx <command> ; exit")`
- System commands → `run_terminal_cmd("<command> ; exit")`
- Always add `; exit` to prevent hanging on both success and failure

**Note**: Python wrapper solutions are Cursor-specific. Claude Code can use `run_terminal_cmd` directly for Python scripts.

## Trickle-Down Documentation System

**CRITICAL:** This project uses a hierarchical trickle-down documentation system. You MUST follow the context loading order:

**Context Loading Order: TD0 ? TD0.5 ? TD1 ? TD2 ? TD3**

### Trickle-Down Levels (Located in /docs/0_context/1_trickle_down/)

1. **TD0 - Universal Principles** (	rickle-down-0-universal/)
   - Cross-project standards and methodologies
   - Universal coding standards and development philosophies

2. **TD0.5 - Environment Standards** (	rickle-down-0.5-environment/)
   - **WSL Ubuntu file system requirements** (MANDATORY)
   - Environment-specific tool configurations

3. **TD1 - Project Standards** (	rickle-down-1-project/)
   - Language Tracker project constitution
   - TDD framework and testing requirements

4. **TD2 - Feature Guidance** (	rickle-down-2-features/)
   - Authentication, learning, content-management, advanced, system
   - Feature-specific architecture and user stories

5. **TD3 - Implementation Details** (	rickle-down-3-components/)
   - Specific implementations and feature summaries

### Required Reading Order

**Before any work, load context in this exact order:**
1. /docs/1_trickle_down/trickle-down-0-universal/universal_instructions.md
2. /docs/1_trickle_down/trickle-down-0.5-environment/wsl-ubuntu-environment.md
3. /docs/1_trickle_down/trickle-down-1-project/constitution.md
4. Relevant TD2 feature documentation
5. Relevant TD3 implementation details

## Legacy Documentation Structure

**DEPRECATED:** The /docs/for_ai structure is being phased out in favor of the trickle-down system.

**Still Available for Reference:**
- /docs/for_ai/instructions_files - Legacy AI rules
- /docs/for_ai/requirements - Feature requirements  
- /docs/for_ai/prompts - Specific tasks


## Essential Reading

Before starting work, review these key documents:

### 1. Standing Rules for AI Agents
Also read: [../DEPTH_FIRST_SLICE.md](../DEPTH_FIRST_SLICE.md) — depth-first slice prototype strategy used across flows.
**[instructions_for_AI_agents.md](instructions_for_AI_agents.md)** - Mandatory workflow:
- Requirement documentation workflow
- TODO list requirements for every prompt
- Feature isolation guidelines
- Test creation mandate

### 2. Complete Feature Requirements
**[../requirements/README.md](../requirements/README.md)** - All implemented/planned features:
- Product goals and mission
- Navigation hierarchy (Levels 0-4)
- All feature specifications with acceptance criteria
- Expected outcomes for each feature

### 3. Architecture Documentation
**[../](../)** - Technical architecture:
- `PARALLEL_DEVELOPMENT_ARCHITECTURE.md` - Parallel development strategy
- `APP_PY_CLEANED_STATUS.md` - Current app.py structure
- `SUB_FEATURE_PATTERN_TEMPLATE.md` - Sub-feature implementation guide
- `NO_PROBLEMS_FOUND.md` - Latest health check results

## Running the Application

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the Flask app (default port 5000, or use PORT env var)
PORT=5001 python app.py

# The app will auto-initialize the SQLite database on first run
# Access at: http://localhost:5001
```

## Testing

```bash
# Run all tests
pytest

# Run tests for a specific feature
pytest features/words/tests/
pytest features/admin/tests/test_phoneme_management.py

# Run with verbose output
pytest -v

# Run integration tests only
pytest tests/integration/

# Run Firebase integration tests (requires credentials)
RUN_FIREBASE_INTEGRATION_TESTS=1 python3 -m unittest tests.integration.test_cloud_integration
```

### Pre-Push Validation (Non-Doc Changes)
- For any change that affects functionality (anything other than Markdown/docs-only):
  - Run all tests: `pytest`
  - Run user story automations as relevant: `python3 scripts/automation/run_user_stories.py --plan scripts/automation/story_plan.sample.json --concurrency 1`
- Do not mark the task complete or push until all tests and automations pass.

## Repository Structure

### Core Application Files
```
lang-trak-in-progress/
├── app.py                 # Flask bootstrap (489 lines) - registers blueprints only
├── main.py                # Database setup and terminal application
├── requirements.txt       # Python dependencies
├── pytest.ini             # Test configuration
└── README.md              # Main documentation
```

### Source Code
```
src/                       # Core application source
├── storage_manager.py     # Unified local/cloud storage interface
├── tts_ipa.py            # Text-to-speech integration
└── phonotactics.py       # Phonotactic rules engine
```

### Configuration
```
config/                    # All configuration files
├── firebase/              # Firebase configuration
│   ├── firebase-config.js
│   ├── firebase-service-account.json
│   ├── firebase-service-account-dev.json
│   └── firebase-service-account-prod.json
├── .claude_alias          # Claude Code aliases
├── .codex_alias           # Codex aliases
├── codex.env              # Codex environment
└── .replit                # Replit configuration
```

### Data
```
data/                      # Data files
├── phonemes.db            # Main SQLite database
├── test_phonemes.db       # Test database
└── phoneme_templates/     # Phoneme template JSON files
```

### Scripts
```
scripts/                   # Utility scripts (organized by purpose)
├── setup/                 # Setup and installation
│   ├── setup_claude_code.sh
│   ├── setup_codex.sh
│   └── set_api_key.sh
├── migration/             # Data migration
│   ├── migrate_to_firestore.py
│   ├── switch_environment.py
│   └── update_main.py
├── database/              # Database utilities
│   ├── fix_database.py
│   ├── verify_db.py
│   ├── add_sample_words.py
│   └── sample_data.py
├── demo/                  # Demo scripts
│   ├── demo_features.py
│   ├── demo_all_types_display.py
│   └── demo_letter_filtering.py
├── dev/                   # Development utilities
│   ├── start_webapp.py
│   ├── verify_menu.py
│   └── video_diagnostic.py
└── legacy/                # Deprecated scripts (for reference)
    ├── tts_ipa_old.py
    ├── flattened_dataset*.py (multiple versions)
    └── [other legacy scripts]
```

### Feature Modules (Green Zone - Work Here!)
```
features/                  # All features completely isolated for parallel work
├── auth/                 # Authentication & authorization (Level 0)
│   ├── login.py          # Login/logout routes
│   ├── registration.py   # User registration
│   ├── firebase_auth.py  # Firebase OAuth integration
│   ├── helpers.py        # get_user_info(), require_auth()
│   ├── templates/        # Auth-specific templates
│   └── tests/           # Auth tests
│
├── dashboard/           # User dashboard (Level 1)
│   ├── display.py       # Dashboard view with projects/groups
│   ├── api.py          # Dashboard API endpoints
│   └── templates/      # Dashboard templates
│
├── projects/           # Project management (Level 2)
│   ├── display.py      # List and view projects
│   ├── creation.py     # Create new projects
│   ├── editing.py      # Edit project metadata
│   ├── storage_ops.py  # Cloud migration, sync, fork
│   ├── context.py      # Enter/exit project context
│   ├── api.py          # Project API endpoints
│   ├── metadata.py     # Project metadata helpers
│   ├── templates/      # Project templates
│   └── tests/          # Project tests
│
├── groups/             # Group collaboration (Level 1)
│   ├── display.py      # List groups, view details
│   ├── creation.py     # Create groups with invites
│   ├── membership.py   # Join groups, manage members
│   ├── api.py          # Group API endpoints
│   ├── templates/      # Group templates
│   └── tests/          # Group tests
│
├── words/              # Word CRUD operations (Level 4b)
│   ├── display.py      # View and display words
│   ├── creation.py     # Create words with helpers
│   ├── search.py       # Search and lookup
│   ├── editing.py      # Edit existing words
│   ├── api_operations.py  # All CRUD API endpoints
│   ├── templates/      # Word templates
│   └── tests/          # Word tests
│
├── phonemes/           # Phoneme display (Level 4a)
│   ├── menu.py         # Phoneme overview menu
│   ├── display.py      # Flat/nested/full hierarchy views
│   ├── templates/      # Phoneme templates
│   └── tests/          # Phoneme tests
│
├── admin/              # Administration tools (Level 4c)
│   ├── dashboard.py    # Admin overview
│   ├── phoneme_management.py  # Phoneme CRUD operations
│   ├── template_system.py     # Template import/export/apply
│   ├── database_tools.py      # Database maintenance
│   ├── templates/      # Admin templates
│   └── tests/          # Admin tests
│
└── variant_menu/       # Placeholder (integrated into projects)
```

### Shared Infrastructure (Yellow Zone - Check First)
```
core/                   # Stable shared infrastructure
├── database.py        # Database connection helpers
├── session.py         # Session management utilities
└── decorators.py      # @require_auth, @require_project_admin

services/              # Cross-cutting services
├── firebase/          # Firebase/Firestore integration
│   ├── config.py     # Firebase configuration
│   ├── firestore.py  # Firestore database operations
│   └── __init__.py   # Exports clean_firebase_service, firestore_db
├── tts/              # Text-to-speech services
├── media/            # Media handling utilities
└── reset/            # Database reset service
```

### Documentation (Essential Reference)
```
docs/
├── for_ai/                     # AI agent documentation
│   ├── instructions_files/     # Working instructions (READ FIRST)
│   │   ├── instructions_for_AI_agents.md  # Standing rules
│   │   └── CLAUDE.md           # This file
│   ├── requirements/           # Feature requirements (REFERENCE OFTEN)
│   │   ├── README.md          # Complete requirements index
│   │   ├── user_authentication.md
│   │   ├── group_collaboration.md
│   │   ├── word_management.md
│   │   └── [30+ feature specs]
│   ├── prompts/                # Session-specific tasks (CHECK EACH SESSION)
│   │   └── [task files]
│   ├── PARALLEL_DEVELOPMENT_ARCHITECTURE.md  # Architecture overview
│   ├── APP_PY_CLEANED_STATUS.md             # Current app.py state
│   ├── SUB_FEATURE_PATTERN_TEMPLATE.md      # Implementation patterns
│   ├── NO_PROBLEMS_FOUND.md                 # Health check status
│   ├── FOLDER_REORGANIZATION_PLAN.md        # Folder structure reorganization
│   └── [12+ architecture docs]
├── archive/                    # Historical implementation docs
│   ├── ADMIN_IMPLEMENTATION.md
│   ├── ENHANCED_PHONEMES_SUMMARY.md
│   ├── IMPLEMENTATION_COMPLETE.md
│   └── [11+ archived docs]
├── setup/                      # Setup and configuration guides
│   ├── CLAUDE_CODE_CLI_GUIDE.md
│   ├── CODEX_SETUP_README.md
│   └── WEB_APP_README.md
├── api/                        # API documentation
└── README.md                   # User-facing documentation
```

### Tests
```
tests/                 # Integration and global tests
├── integration/       # Cross-feature integration tests
├── conftest.py       # Global pytest fixtures
└── __init__.py

features/*/tests/      # Feature-specific tests (colocated)
```

### Static Assets & Templates
```
templates/            # Global templates (base.html)
static/              # Global static assets
features/*/templates/  # Feature-specific templates
features/*/static/     # Feature-specific static assets
videos/              # Uploaded video files (auto-created)
```

## Architecture Overview

This is a Flask-based Language Tracker application with a **feature-isolated architecture** designed for parallel development by multiple AI agents or human developers.

### Navigation Hierarchy

The application follows a strict navigation hierarchy documented in [requirements/README.md](../requirements/README.md):

```
Level 0: Login/Register → Entry point (features/auth/)
    ↓
Level 1: Dashboard → My Projects | My Groups (features/dashboard/, features/groups/)
    ↓
Level 2: My Projects → List, search, create, manage (features/projects/)
    ↓
Level 3: Variant Menu → Project context, variant selection (/main-menu in app.py)
    ↓
Level 4: Work Areas
    ├── 4a: Phonemes → View/analyze phonemes (features/phonemes/)
    ├── 4b: Words → CRUD operations on words (features/words/)
    └── 4c: Administration → Manage phonemes, templates, DB (features/admin/)
```

### Core Architecture Principles

1. **Feature Isolation** - Each feature owns its routes, templates, tests, and business logic
2. **Sub-Feature Pattern** - Large features split into concern-based sub-modules (display, creation, editing, etc.)
3. **Parallel Safety** - Multiple developers work on different features simultaneously without file conflicts
4. **Minimal Bootstrap** - app.py (489 lines) only registers blueprints and initializes database

### Key Architecture Achievements

**Recent refactoring (October 2025):**
- Reduced app.py from 2,677 lines → 489 lines (81.7% reduction)
- Extracted 49 routes to feature modules
- Applied sub-feature pattern to all major features
- Achieved **27+ agent parallel development capacity**
- **Zero merge conflicts** between parallel development efforts

## Database

- **Type:** SQLite
- **Location:** `data/phonemes.db` (main), `data/test_phonemes.db` (tests)
- **Schema:** Auto-initialized by `app.py::init_users_table()` on startup
- **Main operations:** `main.py` contains core database operations
- **DB_NAME constant:** Set to `"data/phonemes.db"` in main.py
- **Tables:** users, projects, groups, group_memberships, words, phonemes, phoneme_templates, project_shares, etc.

## Firebase Integration

The app supports optional Firebase/Firestore for cloud storage:
- **Services:** `services/firebase/` (firestore operations, config)
- **Config:** Set `VITE_FIREBASE_*` environment variables
- **Credentials:** Place service account JSON in `config/firebase/firebase-service-account-{env}.json`
- **Config module:** `services/firebase/config.py` - resolves paths from project root
- **Availability check:** `clean_firebase_service.is_available()`
- **Environment switching:** Use `scripts/migration/switch_environment.py` to toggle between dev/production

## Feature Blueprint Registration

When adding a new feature:

1. Create feature directory: `features/new_feature/`
2. Create `__init__.py` with blueprint:
   ```python
   from flask import Blueprint

   new_feature_bp = Blueprint("new_feature", __name__,
                             template_folder="templates",
                             static_folder="static")

   # Import sub-modules to register routes
   from . import routes  # or display, creation, etc.
   ```
3. Register in `app.py`:
   ```python
   from features.new_feature import new_feature_bp
   # Add to registration loop
   for blueprint in (auth_bp, ..., new_feature_bp):
       app.register_blueprint(blueprint)
   ```

## Parallel Development Guidelines

**Traffic Light System** (from [PARALLEL_DEVELOPMENT_ARCHITECTURE.md](../PARALLEL_DEVELOPMENT_ARCHITECTURE.md)):

🟢 **Green Zone** (95% of work) - Work freely, zero coordination:
- Any file within your assigned feature directory (`features/<feature>/`)
- Feature-specific templates and tests
- New sub-modules within features
- Feature-specific static assets

🟡 **Yellow Zone** (4% of work) - Check with team first:
- `core/*` modules (stable interfaces)
- `services/*` modules (shared services)
- Global templates (`templates/base.html`)
- Shared utilities

🔴 **Red Zone** (1% of work) - Must coordinate:
- Database schema changes (`schema.sql`, migration functions)
- `app.py` (except blueprint registration)
- Breaking changes to shared services
- Core module interface changes

**Best Practice:** When working on a feature, only modify files in that feature's directory. This enables conflict-free parallel development.

## Import Patterns

**Correct imports:**
```python
# Core source modules (now in src/)
from src.storage_manager import storage_manager, StorageType
from src.phonotactics import PhonotacticRules
from src.tts_ipa import ipa_tts

# Firebase services
from services.firebase import clean_firebase_service, firestore_db

# Auth helpers
from features.auth import get_user_info, require_auth

# Project metadata
from features.projects import fetch_project_metadata

# Main database operations
import main
```

**Common mistakes to avoid:**
```python
# ❌ Wrong - old import paths (before reorganization)
from storage_manager import storage_manager
from phonotactics import PhonotacticRules
from tts_ipa import ipa_tts
from services.firebase.clean_firebase_service import ...

# ✅ Correct - updated paths after reorganization
from src.storage_manager import storage_manager
from src.phonotactics import PhonotacticRules
from src.tts_ipa import ipa_tts
from services.firebase import clean_firebase_service, firestore_db
```

**File Paths:**
```python
# Database path
DB_NAME = "data/phonemes.db"  # Not "phonemes.db"

# Firebase credentials
credentials_file = "config/firebase/firebase-service-account-dev.json"  # Not "firebase-service-account-dev.json"

# Phoneme templates
template_dir = "data/phoneme_templates"  # Not "phoneme_templates"
```

## Workflow for New Features

**IMPORTANT:** Follow the workflow in [instructions_for_AI_agents.md](instructions_for_AI_agents.md):

1. **Create TODO list** - For every prompt, explicitly state what you will do
2. **Document requirements** - Add/update spec in `docs/for_ai/requirements/` and update the index
3. **Find navigation level** - Determine where feature fits in navigation hierarchy (Level 0-4 or Cross-Cutting)
4. **Isolate in feature directory** - Create/use `features/<feature_name>/` directory
5. **Apply sub-feature pattern** - Split large features into concern-based modules (display, creation, editing, api)
6. **Write tests first** - Create tests in `features/<feature>/tests/` before implementation
7. **Implement feature** - Work only within feature directory (Green Zone)
8. **Run tests** - Verify all tests pass, including existing tests
9. **Update documentation** - Update requirement spec and architecture docs

## Testing Strategy

- **Feature tests:** Colocated in `features/<feature>/tests/`
- **Integration tests:** `tests/integration/`
- **Test isolation:** Each feature's tests should mock dependencies from other features
- **Fixtures:** Global fixtures in `tests/conftest.py`
- **Coverage:** Every new feature MUST have tests (see [instructions_for_AI_agents.md](instructions_for_AI_agents.md))

## Common Development Patterns

**Adding a new route to existing feature:**
1. Identify appropriate sub-module (e.g., `features/words/display.py` for viewing)
2. Add route function with `@<feature>_bp.route(...)`
3. No need to modify `__init__.py` if sub-module already imported
4. Add tests to feature's test directory
5. Update requirement spec if behavior changes

**Creating a new sub-module within a feature:**
1. Create file: `features/<feature>/new_module.py`
2. Add routes with `@<feature>_bp.route(...)`
3. Import in `features/<feature>/__init__.py`: `from . import new_module`
4. Add tests in `features/<feature>/tests/test_new_module.py`
5. Document in feature's requirement spec

**Accessing user context:**
```python
from features.auth import get_user_info, require_auth

@feature_bp.route('/protected')
@require_auth
def protected_route():
    user = get_user_info()
    # user['id'], user['username'], user['is_authenticated']
```

**Accessing current project:**
```python
user = get_user_info()
current_project = user.get('current_project')
if current_project:
    project_id = current_project['id']
    storage_type = current_project['storage_type']  # 'local' or 'cloud'
```

## Storage Manager

- **Module:** `src/storage_manager.py`
- **Purpose:** Unified interface for local SQLite and cloud Firestore storage
- **Storage types:** `StorageType.LOCAL` and `StorageType.CLOUD`
- **Project identifiers:** Format `"local:123"` or `"cloud:abc123"`
- **Methods:** `get_projects()`, `create_project()`, `delete_project()`, `migrate_to_cloud()`, `fork_to_local()`
- **Import:** `from src.storage_manager import storage_manager, StorageType`

## TTS (Text-to-Speech)

- **Module:** `src/tts_ipa.py`
- **Backend:** Azure TTS (requires `AZURE_SPEECH_KEY` env var)
- **Routes:** `/api/tts/ipa`, `/api/tts/phoneme`, `/api/tts/status` (in app.py)
- **Usage:** Generate audio for IPA sequences and individual phonemes
- **Import:** `from src.tts_ipa import ipa_tts`
- **Requirement:** See [tts_integration.md](../requirements/tts_integration.md)

## Phonotactics

- **Module:** `src/phonotactics.py`
- **Purpose:** Phonotactic rules engine for validating syllable structures
- **Import:** `from src.phonotactics import PhonotacticRules`

## Deployment

The app runs on port 5000 by default (configurable via `PORT` environment variable). On startup:
1. Creates `videos/` directory for uploads
2. Initializes SQLite database if not present
3. Runs schema migrations via `main.py::migrate_schema()`
4. Optionally inserts sample data

## Key Documentation Files

### For Implementation
- **[instructions_for_AI_agents.md](instructions_for_AI_agents.md)** - Mandatory workflow for all AI agents
- **[requirements/README.md](../requirements/README.md)** - Complete feature requirements and acceptance criteria
- **[SUB_FEATURE_PATTERN_TEMPLATE.md](../SUB_FEATURE_PATTERN_TEMPLATE.md)** - Template for splitting features

### For Architecture Understanding
- **[PARALLEL_DEVELOPMENT_ARCHITECTURE.md](../PARALLEL_DEVELOPMENT_ARCHITECTURE.md)** - Complete parallel development strategy
- **[APP_PY_CLEANED_STATUS.md](../APP_PY_CLEANED_STATUS.md)** - What was extracted from app.py and where it went
- **[DEVELOPMENT_CONVENTIONS.md](../DEVELOPMENT_CONVENTIONS.md)** - Coding standards and patterns

### For Current Status
- **[NO_PROBLEMS_FOUND.md](../NO_PROBLEMS_FOUND.md)** - Latest comprehensive health check
- **[FINAL_SUB_FEATURE_STATUS.md](../FINAL_SUB_FEATURE_STATUS.md)** - Sub-feature implementation status

## Development History

**Major refactoring (October 2025):**

### Phase 1: Sub-Feature Pattern Application
- Reduced app.py from 2,677 lines → 489 lines (81.7% reduction)
- Extracted 49 routes to feature modules
- Applied sub-feature pattern to all major features (auth, groups, dashboard, projects, words, phonemes, admin)
- Achieved 27+ agent parallel development capacity
- Zero merge conflicts in parallel development

### Phase 2: Folder Reorganization (October 16, 2025)
- Reduced root directory from 46 files to 13 essential files
- Organized 30 Python scripts into `scripts/` with 6 purpose-based subdirectories
- Created `src/` for core source code (storage_manager, tts_ipa, phonotactics)
- Created `config/` for all configuration files including Firebase credentials
- Created `data/` for database and template files
- Moved 16 markdown docs to `docs/archive/` and `docs/setup/`
- Updated 20+ files with new import paths
- Updated all database path references from `phonemes.db` to `data/phonemes.db`
- Updated Firebase config paths to resolve from project root
- All imports and tests verified working

**Benefits:**
- Clean root directory shows professional project organization
- Clear separation of concerns (source, config, scripts, data, docs)
- Easy to find files by purpose rather than alphabetically
- Legacy files isolated in `scripts/legacy/` for reference
- Scalable structure for future growth

See `docs/for_ai/` for complete architecture documentation and `docs/for_ai/FOLDER_REORGANIZATION_PLAN.md` for reorganization details.

