---
resource_id: "be827b61-4adb-4efb-8bd1-3e6cc283671e"
resource_type: "document"
resource_name: "SUB_FEATURE_PARALLELIZATION"
---
# Sub-Feature Parallelization Guide

<!-- section_id: "be6811ad-33ce-47ff-85cb-1bfb9ffd2eb3" -->
## The Next Level: Parallel Work Within a Feature

While the current architecture enables **8 agents to work on different features simultaneously**, we can go deeper: **multiple agents can work on different sub-concerns within the same feature**.

<!-- section_id: "542250e6-7e39-4da3-9bb9-b90d89acedd8" -->
## Example: Words Feature

The "words" feature has multiple distinct sub-concerns that can be developed in parallel:

<!-- section_id: "66867843-842d-4729-ad69-35030e3a0665" -->
### Current State (app.py - Not Yet Migrated)

```
Words Feature Routes (Still in app.py):
├── /words                          - Words menu/landing
├── /words/display                  - View all words
├── /words/create                   - Create word form
├── /words/create/table-based       - Table-based creation
├── /words/lookup                   - Search words
├── /words/edit/<id>                - Edit word
│
└── API Endpoints:
    ├── /api/create-word            - Create word
    ├── /api/lookup-word            - Search API
    ├── /api/update-word/<id>       - Update word
    ├── /api/delete-word/<id>       - Delete word
    └── /api/remove-video/<id>      - Remove video
```

<!-- section_id: "18a795a5-c283-45a4-8ac6-7752a1270287" -->
### Proposed Sub-Feature Organization

Break the words feature into **logical sub-modules** that can be worked on in parallel:

```
features/words/
│
├── __init__.py              # Blueprint registration
│
├── routes.py                # 🟢 Main navigation routes
│   ├── words_menu()         # Landing page
│   └── words_display()      # View all words
│
├── creation.py              # 🟢 Word creation logic
│   ├── create_word_form()   # GET /words/create
│   ├── create_word_table()  # GET /words/create/table-based
│   └── Functions:
│       ├── validate_word_data()
│       ├── check_duplicate()
│       └── create_word_entry()
│
├── search.py                # 🟢 Search & lookup logic
│   ├── lookup_form()        # GET /words/lookup
│   └── Functions:
│       ├── search_all_fields()
│       ├── search_by_phoneme()
│       └── filter_results()
│
├── editing.py               # 🟢 Word editing logic
│   ├── edit_word_form()     # GET /words/edit/<id>
│   └── Functions:
│       ├── load_word_data()
│       ├── validate_changes()
│       └── update_word()
│
├── api.py                   # 🟢 API endpoints
│   ├── api_create_word()    # POST /api/create-word
│   ├── api_lookup_word()    # GET /api/lookup-word
│   ├── api_update_word()    # POST /api/update-word/<id>
│   ├── api_delete_word()    # DELETE /api/delete-word/<id>
│   └── api_remove_video()   # POST /api/remove-video/<id>
│
├── models.py                # 🟡 Database operations (shared)
│   ├── get_word()
│   ├── get_all_words()
│   ├── create_word()
│   ├── update_word()
│   └── delete_word()
│
├── validation.py            # 🟡 Shared validation logic
│   ├── validate_word_structure()
│   ├── validate_phonemes()
│   └── check_duplicate_word()
│
├── templates/               # 🟢 Template files
│   ├── words_menu.html
│   ├── words_display.html
│   ├── create_word.html
│   ├── word_lookup.html
│   └── edit_word.html
│
└── tests/                   # 🟢 Test files
    ├── test_creation.py
    ├── test_search.py
    ├── test_editing.py
    └── test_api.py
```

<!-- section_id: "6794054b-a7f1-46d0-af02-3dd120b1c31a" -->
## Parallel Work Scenarios

<!-- section_id: "a63621d5-f24e-4c1f-a6f1-c96d8be41b12" -->
### Scenario 1: Three Agents in Words Feature

**Agent A** - Working on "All Fields Search"
```python
# features/words/search.py
Files touched:
- search.py (new search_all_fields function)
- api.py (update api_lookup_word endpoint)
- templates/word_lookup.html
- tests/test_search.py
```

**Agent B** - Working on "Word Creation Improvements"
```python
# features/words/creation.py
Files touched:
- creation.py (add validation, improve UX)
- api.py (update api_create_word endpoint)
- templates/create_word.html
- tests/test_creation.py
```

**Agent C** - Working on "Bulk Word Editing"
```python
# features/words/editing.py
Files touched:
- editing.py (new bulk edit function)
- api.py (new bulk update endpoint)
- templates/edit_word.html
- tests/test_editing.py
```

**Conflict Analysis:**
- ✅ **creation.py, search.py, editing.py** - No conflicts (different files)
- ⚠️ **api.py** - All three touch it (need coordination)
- ✅ **templates/** - Different templates, no conflicts
- ✅ **tests/** - Different test files, no conflicts

**Solution for api.py conflicts:**
1. Each agent adds their API endpoint in a designated section
2. Follow clear ordering convention (CRUD order: Create, Read, Update, Delete)
3. Or split api.py further: `api_creation.py`, `api_search.py`, `api_editing.py`

<!-- section_id: "ca1921f8-7319-4b4d-833f-bdfd49ff71d0" -->
### Scenario 2: Split api.py Further

```
features/words/
├── api/
│   ├── __init__.py          # Import all API routes
│   ├── creation_api.py      # 🟢 Word creation endpoints
│   ├── search_api.py        # 🟢 Search/lookup endpoints
│   ├── editing_api.py       # 🟢 Edit/update endpoints
│   └── deletion_api.py      # 🟢 Delete endpoints
```

Now **all three agents can work without ANY conflicts!**

<!-- section_id: "9f272c0f-169f-4f09-9af1-2f3bdf3b4d29" -->
## Pattern: File-Per-Concern

<!-- section_id: "6027a775-f329-4c29-bcf9-6e06f989cee4" -->
### Rule of Thumb:
**If two developers could reasonably work on the same concern at the same time, they should have separate files.**

<!-- section_id: "da6b56da-29d0-49d6-ad59-0d3c0be7536d" -->
### Apply to Other Features:

#### Projects Feature
```
features/projects/
├── routes.py                # Main navigation
├── creation.py              # 🟢 Create projects
├── editing.py               # 🟢 Edit project metadata
├── branching.py             # 🟢 Branch/merge operations
├── sharing.py               # 🟢 Share with groups
├── storage_ops.py           # 🟢 Cloud migration
├── api/
│   ├── creation_api.py
│   ├── branching_api.py
│   └── storage_api.py
└── models.py                # 🟡 Shared DB operations
```

#### Phonemes Feature
```
features/phonemes/
├── routes.py                # Main navigation
├── viewing.py               # 🟢 Display modes (flat, nested, full)
├── frequency.py             # 🟢 Frequency calculation
├── categorization.py        # 🟢 Phoneme categories
├── api.py                   # API endpoints
└── models.py                # 🟡 Shared DB operations
```

#### Admin Feature
```
features/admin/
├── routes.py                # Admin dashboard
├── phoneme_management.py    # 🟢 Phoneme admin operations
├── template_system.py       # 🟢 Template import/export/apply
├── database_tools.py        # 🟢 Database maintenance
├── bulk_operations.py       # 🟢 Bulk edit/delete
├── api/
│   ├── phoneme_api.py
│   ├── template_api.py
│   └── database_api.py
└── models.py                # 🟡 Shared DB operations
```

<!-- section_id: "81b2c120-402c-4acb-a40c-8d97c9c62ffd" -->
## Coordination Strategy

<!-- section_id: "56fe3c8c-d873-4e57-8c27-fca2927a9495" -->
### Shared Files (Need Coordination)

**models.py** - Database operations shared across sub-features
- **Strategy**: Define clear function boundaries
- **Pattern**: One function per operation (get_word, create_word, etc.)
- **Rule**: Add new functions, don't modify existing ones

**validation.py** - Shared validation logic
- **Strategy**: Pure functions, no side effects
- **Pattern**: Each validation function is independent
- **Rule**: Add new validators, don't modify existing ones

**api.py** (if not split)
- **Strategy**: Clear section comments for each sub-concern
- **Pattern**: Follow CRUD ordering
- **Rule**: Add endpoints in designated sections

<!-- section_id: "8841ed31-3880-4509-ac11-67d94e37291a" -->
### Example: models.py Coordination

```python
# features/words/models.py
"""
Database operations for words feature.

Coordination Rules:
- Add new functions at the bottom
- Don't modify existing function signatures
- If you need to change behavior, add a new function with a different name
"""

from core.database import get_db_connection

# ============================================================
# READ OPERATIONS (Agent working on search can add here)
# ============================================================

def get_word(word_id: int, project_id: str):
    """Get single word by ID."""
    # ... implementation

def get_all_words(project_id: str):
    """Get all words for a project."""
    # ... implementation

def search_words(query: str, project_id: str, fields: list):
    """Search words across specified fields."""
    # ... implementation (Agent A adds this)

# ============================================================
# CREATE OPERATIONS (Agent working on creation can add here)
# ============================================================

def create_word(word_data: dict, project_id: str):
    """Create new word entry."""
    # ... implementation

def create_word_batch(word_list: list, project_id: str):
    """Batch create multiple words."""
    # ... implementation (Agent B adds this)

# ============================================================
# UPDATE OPERATIONS (Agent working on editing can add here)
# ============================================================

def update_word(word_id: int, word_data: dict):
    """Update existing word."""
    # ... implementation

def update_word_bulk(word_ids: list, updates: dict):
    """Bulk update multiple words."""
    # ... implementation (Agent C adds this)

# ============================================================
# DELETE OPERATIONS
# ============================================================

def delete_word(word_id: int):
    """Delete single word."""
    # ... implementation
```

**Result**: Three agents can add new functions to models.py without conflicts!

<!-- section_id: "e3142e0f-78e1-4150-aa88-1b3594d2e0db" -->
## Migration Strategy

<!-- section_id: "eeaa0b84-96a8-4fb2-a619-c47222ca2d38" -->
### Phase 1: Extract Routes from app.py ✅ (Partially Done)
Move routes from app.py to feature blueprints

<!-- section_id: "cb4cac69-a77d-455d-a260-a75bbf8de34b" -->
### Phase 2: Organize by Sub-Concern (Next Step)
Split large route files into logical sub-modules:

**For Words Feature:**
1. Create `features/words/creation.py` - Extract creation routes
2. Create `features/words/search.py` - Extract search routes
3. Create `features/words/editing.py` - Extract editing routes
4. Update `features/words/__init__.py` to import all sub-modules
5. Create `features/words/models.py` - Extract DB operations
6. Update `features/words/api.py` with all API endpoints

**Pattern for Each Feature:**
```python
# features/words/__init__.py
from flask import Blueprint

words_bp = Blueprint('words', __name__,
                     template_folder='templates',
                     url_prefix='/words')

# Import all sub-modules to register routes
from . import routes       # Main navigation
from . import creation     # Word creation
from . import search       # Search & lookup
from . import editing      # Edit words
from . import api          # API endpoints

__all__ = ['words_bp']
```

<!-- section_id: "933d04b2-7f6e-4ff1-948f-e1c3a9129597" -->
## Benefits of Sub-Feature Organization

<!-- section_id: "b065f365-7c0a-42a4-ab2c-1d47c0f7ed58" -->
### 1. **Increased Parallel Capacity**
- Before: 8 agents (one per feature)
- After: 20+ agents (multiple per feature)

<!-- section_id: "456b8cfe-b039-4c1d-bd38-17d3e7dacc4a" -->
### 2. **Clearer Ownership**
- Agent knows exactly which file to modify
- "I'm working on word creation" → `creation.py`
- "I'm working on search" → `search.py`

<!-- section_id: "4226976e-ae47-433f-a61a-0b4bf7cecf00" -->
### 3. **Easier Code Review**
- PRs are smaller and focused
- Reviewer can focus on one concern at a time

<!-- section_id: "3b7eecde-1b3e-41cf-b6cb-ffb0eb7d1d87" -->
### 4. **Better Testing**
- Tests map directly to implementation files
- `test_creation.py` tests `creation.py`

<!-- section_id: "325ff841-b359-4e20-becc-79db2987a7c1" -->
### 5. **Reduced Cognitive Load**
- Each file handles one concern
- Easier to understand and modify

<!-- section_id: "c7f17b5a-7657-421f-a502-20f3ea0a72a7" -->
## Implementation Checklist

For each feature with multiple sub-concerns:

- [ ] Identify distinct sub-concerns (creation, viewing, searching, editing, etc.)
- [ ] Create separate files for each sub-concern
- [ ] Extract routes from app.py to appropriate files
- [ ] Create shared models.py for database operations
- [ ] Create shared validation.py if needed
- [ ] Update __init__.py to import all sub-modules
- [ ] Move API endpoints to api.py (or split further)
- [ ] Create corresponding test files for each sub-concern
- [ ] Update documentation with file organization

<!-- section_id: "3c449494-d6ae-44e1-91ce-b9b6d6472341" -->
## Quick Reference: When to Split Files

| Scenario | Action |
|----------|--------|
| 2+ agents could work on same concern simultaneously | ✅ Create separate files |
| File is over 300 lines | ✅ Consider splitting by concern |
| File has multiple distinct responsibilities | ✅ Split into focused modules |
| Functions are related but independent | ✅ Keep together but use clear sections |
| Functions share significant state | ⚠️ Keep together, add coordination rules |

<!-- section_id: "30a564d9-8a9b-4656-9d3a-7ec236e2a5bc" -->
## Summary

**Current Architecture:**
- 8 features → 8 agents can work in parallel

**Enhanced Architecture:**
- 8 features × 3-5 sub-concerns each → 24-40 agents can work in parallel!

**Key Principle:**
> One file per distinct sub-concern enables maximum parallelization with minimum coordination.

---

**Next Steps:**
1. Identify which features have multiple sub-concerns (words, projects, admin)
2. Create sub-module files for each concern
3. Extract routes from app.py to appropriate sub-modules
4. Update documentation with new structure

**This enables even more parallel development!** 🚀
