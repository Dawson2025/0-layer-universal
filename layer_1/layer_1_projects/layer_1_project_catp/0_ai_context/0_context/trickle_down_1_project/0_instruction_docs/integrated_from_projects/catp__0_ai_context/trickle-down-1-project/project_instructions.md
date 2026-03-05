---
resource_id: "e0ca3200-a578-4ef5-952b-91260c220cd7"
resource_type: "document"
resource_name: "project_instructions"
---
# Lang-Trak Project Instructions

**Auto-loaded at the start of every Claude Code conversation**

<!-- section_id: "6e293ba7-b2bd-4b05-9601-a3643f736321" -->
## Quick Start: Read These Files First

Before starting any work, read these four essential files:

1. **[@.claude/universal_instructions.md](universal_instructions.md)** - Universal best practices for all projects (workflow, testing, git, code quality)
2. **[@docs/for_ai/instructions_files/instructions_for_AI_agents.md](../docs/for_ai/instructions_files/instructions_for_AI_agents.md)** - Mandatory workflow rules for all AI agents
3. **[@docs/for_ai/instructions_files/CLAUDE.md](../docs/for_ai/instructions_files/CLAUDE.md)** - Complete repository guide and architecture
4. **[@docs/for_ai/requirements/README.md](../docs/for_ai/requirements/README.md)** - All feature requirements and product goals

<!-- section_id: "5003331a-08ab-40a8-ac7f-f3907660701e" -->
## Critical Rules (From instructions_for_AI_agents.md)

<!-- section_id: "c4dff3a9-2414-4187-9efa-246352528dbe" -->
### 1. TODO List for Every Prompt
For every prompt, create a TODO list explicitly stating what you will do. Use the `TodoWrite` tool to track progress.

<!-- section_id: "268808fb-f459-4d77-b5d3-76594e4999fa" -->
### 2. Feature Isolation
- Work only within `features/<feature_name>/` directories (Green Zone)
- Avoid editing `core/`, `services/`, or `app.py` unless absolutely necessary (Yellow/Red Zones)
- This enables parallel development without conflicts

<!-- section_id: "ab0c7052-b0d6-45fb-8352-13c70d6fabc4" -->
### 3. Requirement Documentation
- Capture all new requirements in `docs/for_ai/requirements/` specs
- Update the requirements index at `docs/for_ai/requirements/README.md`

<!-- section_id: "4104a39e-39e5-433b-a149-0157c78000dd" -->
### 4. Testing is Mandatory
- Create tests for every feature you implement in `features/<feature>/tests/`
- Run tests after changes to verify nothing broke

<!-- section_id: "cc3981fb-4602-4ba5-8e59-ccdc75bf62a1" -->
## Architecture Quick Reference

<!-- section_id: "b0b0a906-7689-4001-94fb-42a6314459f8" -->
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

<!-- section_id: "484a219c-6467-4bf6-8ba0-58cd2211151a" -->
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

<!-- section_id: "9ba981f9-7caa-43d7-ab8c-ac3d73fd5a7c" -->
### File Paths
```python
DB_NAME = "data/phonemes.db"  # Not "phonemes.db"
credentials_file = "config/firebase/firebase-service-account-dev.json"
template_dir = "data/phoneme_templates"
```

<!-- section_id: "a78c8151-d11b-4684-810d-caf12c8c5800" -->
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

<!-- section_id: "d957ebe4-b749-430d-8e52-309d11f635de" -->
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

<!-- section_id: "35f231de-071f-4893-bb33-93bbae04044b" -->
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

<!-- section_id: "9a9bc914-111a-4103-9d15-bccccb75d4cd" -->
## Key Achievements

- **Feature-isolated architecture** enabling 27+ parallel agents
- **489-line app.py** (down from 2,677 lines - 81.7% reduction)
- **Zero merge conflicts** in parallel development
- **Clean folder structure** (reduced root from 46 to 13 files)
- **Sub-feature pattern** applied to all major features

<!-- section_id: "b6ba81a8-f716-4a61-97c7-c6b26acca9b4" -->
## For Detailed Information

See the three essential files listed at the top. They contain:
- Complete workflow instructions
- Detailed architecture documentation
- All feature specifications with acceptance criteria
- Import patterns and development conventions
- Testing strategies and deployment notes

---

**Remember**: Before starting work, read the three essential files above. They are your source of truth.
