---
resource_id: "98d8afc6-e694-4d13-8dda-14a02217dcaf"
resource_type: "document"
resource_name: "project_instructions"
---
# Lang-Trak Project Instructions

**Auto-loaded at the start of every Claude Code conversation**

<!-- section_id: "85dc859f-102d-4ae6-9b4a-dff0c618e4ec" -->
## Quick Start: Read These Files First

Before starting any work, read these four essential files:

1. **[@.claude/universal_instructions.md](universal_instructions.md)** - Universal best practices for all projects (workflow, testing, git, code quality)
2. **[@docs/for_ai/instructions_files/instructions_for_AI_agents.md](../docs/for_ai/instructions_files/instructions_for_AI_agents.md)** - Mandatory workflow rules for all AI agents
3. **[@docs/for_ai/instructions_files/CLAUDE.md](../docs/for_ai/instructions_files/CLAUDE.md)** - Complete repository guide and architecture
4. **[@docs/for_ai/requirements/README.md](../docs/for_ai/requirements/README.md)** - All feature requirements and product goals

<!-- section_id: "7047d5b3-ed67-4596-ba31-15aec96b8666" -->
## Critical Rules (From instructions_for_AI_agents.md)

<!-- section_id: "e6429a7c-0a47-487e-a49a-8e187ba0c965" -->
### 1. TODO List for Every Prompt
For every prompt, create a TODO list explicitly stating what you will do. Use the `TodoWrite` tool to track progress.

<!-- section_id: "bc54ddc4-e59f-4ca1-8619-6a005406e8db" -->
### 2. Feature Isolation
- Work only within `features/<feature_name>/` directories (Green Zone)
- Avoid editing `core/`, `services/`, or `app.py` unless absolutely necessary (Yellow/Red Zones)
- This enables parallel development without conflicts

<!-- section_id: "de4857b8-ca8f-40e7-aeb3-e6383eba5047" -->
### 3. Requirement Documentation
- Capture all new requirements in `docs/for_ai/requirements/` specs
- Update the requirements index at `docs/for_ai/requirements/README.md`

<!-- section_id: "7263badd-62d8-433c-9eee-c7b618d1b345" -->
### 4. Testing is Mandatory
- Create tests for every feature you implement in `features/<feature>/tests/`
- Run tests after changes to verify nothing broke

<!-- section_id: "f9af0a9c-a607-47e5-b391-214dcaea47da" -->
## Architecture Quick Reference

<!-- section_id: "eddc7337-0c95-489f-9818-26433f31850a" -->
### Folder Structure (Post-Reorganization)
```
lang-trak-in-progress/
├── src/                    # Core source (storage_manager, tts_ipa, phonotactics)
├── config/                 # All configuration (Firebase, aliases, env)
├── data/                   # Database files and phoneme templates
├── scripts/                # Organized utilities (setup, migration, database, demo, dev, legacy)
├── features/               # Feature modules (auth, dashboard, projects, groups, words, phonemes, admin)
├── core/                   # Shared infrastructure (database, session, decorators)
├── services/               # Cross-cutting services (firebase, tts, media, reset)
├── docs/                   # Documentation (for_ai/, archive/, setup/, api/)
└── tests/                  # Integration and global tests
```

<!-- section_id: "e26b0e78-2e34-456f-9616-8e3c891ab7bd" -->
### Import Patterns
```python
# Core modules (in src/)
from src.storage_manager import storage_manager, StorageType
from src.phonotactics import PhonotacticRules
from src.tts_ipa import ipa_tts

# Services
from services.firebase import clean_firebase_service, firestore_db

# Auth helpers
from features.auth import get_user_info, require_auth

# Database operations
import main
```

<!-- section_id: "0a755853-f857-401f-8f04-443b607dacc9" -->
### File Paths
```python
DB_NAME = "data/phonemes.db"  # Not "phonemes.db"
credentials_file = "config/firebase/firebase-service-account-dev.json"
template_dir = "data/phoneme_templates"
```

<!-- section_id: "037bf663-fdbb-4ffe-9731-5b5126ea92fe" -->
## Navigation Hierarchy

```
Level 0: Login/Register (features/auth/)
    ↓
Level 1: Dashboard → My Projects | My Groups (features/dashboard/, features/groups/)
    ↓
Level 2: My Projects → List, search, create, manage (features/projects/)
    ↓
Level 3: Variant Menu → Project context (/main-menu in app.py)
    ↓
Level 4: Work Areas
    ├── 4a: Phonemes (features/phonemes/)
    ├── 4b: Words (features/words/)
    └── 4c: Administration (features/admin/)
```

<!-- section_id: "0bf58366-0cbf-4199-97bd-9887676dcb6c" -->
## Traffic Light System

🟢 **Green Zone (95%)** - Work freely:
- Any file in your assigned feature directory (`features/<feature>/`)
- Feature templates, tests, and static assets

🟡 **Yellow Zone (4%)** - Check first:
- `core/*` modules
- `services/*` modules
- Global templates

🔴 **Red Zone (1%)** - Must coordinate:
- Database schema changes
- `app.py` modifications
- Breaking changes to shared services

<!-- section_id: "dfd2afd2-279d-42e7-8477-d4d1cb4b714a" -->
## Running the Application

```bash
# Activate virtual environment
source .venv/bin/activate

# Run Flask app
PORT=5001 python app.py

# Run tests
pytest
pytest features/words/tests/  # Feature-specific tests
```

<!-- section_id: "b81db982-3767-4ddf-b5d6-14b0f81da647" -->
## Key Achievements

- **Feature-isolated architecture** enabling 27+ parallel agents
- **489-line app.py** (down from 2,677 lines - 81.7% reduction)
- **Zero merge conflicts** in parallel development
- **Clean folder structure** (reduced root from 46 to 13 files)
- **Sub-feature pattern** applied to all major features

<!-- section_id: "32e45349-d732-4751-9107-706fa8ce7f75" -->
## For Detailed Information

See the three essential files listed at the top. They contain:
- Complete workflow instructions
- Detailed architecture documentation
- All feature specifications with acceptance criteria
- Import patterns and development conventions
- Testing strategies and deployment notes

---

**Remember**: Before starting work, read the three essential files above. They are your source of truth.
