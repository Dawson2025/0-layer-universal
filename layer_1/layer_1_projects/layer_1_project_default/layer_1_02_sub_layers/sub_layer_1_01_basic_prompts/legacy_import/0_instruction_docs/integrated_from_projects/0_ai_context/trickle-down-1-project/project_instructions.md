---
resource_id: "99c4193d-2c72-487c-926e-624463879899"
resource_type: "document"
resource_name: "project_instructions"
---
# Lang-Trak Project Instructions

**Auto-loaded at the start of every Claude Code conversation**

<!-- section_id: "3a233104-e4a4-4500-9d22-64c502bf2fb4" -->
## Quick Start: Read These Files First

Before starting any work, read these four essential files:

1. **[@.claude/universal_instructions.md](universal_instructions.md)** - Universal best practices for all projects (workflow, testing, git, code quality)
2. **[@docs/for_ai/instructions_files/instructions_for_AI_agents.md](../docs/for_ai/instructions_files/instructions_for_AI_agents.md)** - Mandatory workflow rules for all AI agents
3. **[@docs/for_ai/instructions_files/CLAUDE.md](../docs/for_ai/instructions_files/CLAUDE.md)** - Complete repository guide and architecture
4. **[@docs/for_ai/requirements/README.md](../docs/for_ai/requirements/README.md)** - All feature requirements and product goals

<!-- section_id: "a89c9eb2-c262-4b78-ba50-0fdc6e622eea" -->
## Critical Rules (From instructions_for_AI_agents.md)

<!-- section_id: "8cd450f0-8f27-41af-a69d-0aaaa098dc37" -->
### 1. TODO List for Every Prompt
For every prompt, create a TODO list explicitly stating what you will do. Use the `TodoWrite` tool to track progress.

<!-- section_id: "e77c980f-1db1-4a64-b5b3-596803c433a6" -->
### 2. Feature Isolation
- Work only within `features/<feature_name>/` directories (Green Zone)
- Avoid editing `core/`, `services/`, or `app.py` unless absolutely necessary (Yellow/Red Zones)
- This enables parallel development without conflicts

<!-- section_id: "ebb1edb7-83a0-444c-9b45-99c62d373c06" -->
### 3. Requirement Documentation
- Capture all new requirements in `docs/for_ai/requirements/` specs
- Update the requirements index at `docs/for_ai/requirements/README.md`

<!-- section_id: "6fc92a38-6731-4a70-afcd-f6e2678ebbf8" -->
### 4. Testing is Mandatory
- Create tests for every feature you implement in `features/<feature>/tests/`
- Run tests after changes to verify nothing broke

<!-- section_id: "fec41a1d-ab28-459d-beda-00add68b56fe" -->
## Architecture Quick Reference

<!-- section_id: "126a85dc-0d9d-4041-938b-a74e35f81678" -->
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

<!-- section_id: "3a469bc2-fe36-4f55-a163-40b37720de34" -->
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

<!-- section_id: "535d7620-7ee0-40fd-a736-f6e1ee8332fa" -->
### File Paths
```python
DB_NAME = "data/phonemes.db"  # Not "phonemes.db"
credentials_file = "config/firebase/firebase-service-account-dev.json"
template_dir = "data/phoneme_templates"
```

<!-- section_id: "0ea72cf7-72a8-4460-96f5-80c9534478cf" -->
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

<!-- section_id: "dd823b89-c54e-4f0c-aa47-1e154f2c9667" -->
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

<!-- section_id: "31d96ee6-99c7-482a-b9e1-c3ab25c34ee6" -->
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

<!-- section_id: "e8766612-aed1-4c0e-a741-022dc6ad590b" -->
## Key Achievements

- **Feature-isolated architecture** enabling 27+ parallel agents
- **489-line app.py** (down from 2,677 lines - 81.7% reduction)
- **Zero merge conflicts** in parallel development
- **Clean folder structure** (reduced root from 46 to 13 files)
- **Sub-feature pattern** applied to all major features

<!-- section_id: "e7874bea-f7c8-4baa-8a6a-ac49215c094d" -->
## For Detailed Information

See the three essential files listed at the top. They contain:
- Complete workflow instructions
- Detailed architecture documentation
- All feature specifications with acceptance criteria
- Import patterns and development conventions
- Testing strategies and deployment notes

---

**Remember**: Before starting work, read the three essential files above. They are your source of truth.
