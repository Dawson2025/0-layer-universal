---
resource_id: "8fb6ba0f-0476-4bdd-97d1-0dafe10bc071"
resource_type: "document"
resource_name: "SUB_FEATURE_PARALLELIZATION"
---
# Sub-Feature Parallelization Guide

<!-- section_id: "8ab3211f-d686-45c1-96bd-ec9e00d0ccd8" -->
## The Next Level: Parallel Work Within a Feature

While the current architecture enables **8 agents to work on different features simultaneously**, we can go deeper: **multiple agents can work on different sub-concerns within the same feature**.

<!-- section_id: "baa70ec5-1227-4a90-8533-767587928310" -->
## Example: Words Feature

The "words" feature has multiple distinct sub-concerns that can be developed in parallel:

<!-- section_id: "daca7e3e-6e46-4fbe-b92f-c3b1045ebf21" -->
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

<!-- section_id: "2338ab74-8a8d-43bf-9e66-c10d454e2fe8" -->
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

<!-- section_id: "5b4344c5-61ad-4f8a-ae0e-e64269a2d6d6" -->
## Parallel Work Scenarios

<!-- section_id: "8dc8f0b7-e43f-42ff-9c2b-8dd640e95d7d" -->
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

<!-- section_id: "d907aa0f-f383-4c5e-8fcb-a0c0922e9b39" -->
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

<!-- section_id: "994daf58-2f48-4b4e-aaaf-ee2af883b687" -->
## Pattern: File-Per-Concern

<!-- section_id: "c9a070ff-0ccb-46c9-80cd-09b08f2e75e7" -->
### Rule of Thumb:
**If two developers could reasonably work on the same concern at the same time, they should have separate files.**

<!-- section_id: "96980d65-09f3-4a3a-9ed5-7cf73650bbd3" -->
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

<!-- section_id: "ca5d6f07-93c7-4928-a4a9-04f12597b3eb" -->
## Coordination Strategy

<!-- section_id: "fa87c1c1-ef8a-4e5b-85d4-853d9d25ef7d" -->
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

<!-- section_id: "888dfab2-0710-480b-afb7-888920957b9b" -->
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

<!-- section_id: "58ec08bb-edd3-462d-8a12-f75f0c8b79a4" -->
## Migration Strategy

<!-- section_id: "bb5ee285-6373-43b5-bf30-b7762f22a3f4" -->
### Phase 1: Extract Routes from app.py ✅ (Partially Done)
Move routes from app.py to feature blueprints

<!-- section_id: "f4fa5ebb-e4e7-4d9e-8ebf-fdbcf2032b77" -->
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

<!-- section_id: "f9ab23e0-5f1e-4e78-b9df-a4875f10f0d5" -->
## Benefits of Sub-Feature Organization

<!-- section_id: "e89f73dc-6531-40c4-b9f0-e6b982c25463" -->
### 1. **Increased Parallel Capacity**
- Before: 8 agents (one per feature)
- After: 20+ agents (multiple per feature)

<!-- section_id: "ac519890-228f-4ba3-9634-332103b97705" -->
### 2. **Clearer Ownership**
- Agent knows exactly which file to modify
- "I'm working on word creation" → `creation.py`
- "I'm working on search" → `search.py`

<!-- section_id: "4dd7333f-4ffb-4cb7-ba3c-09eb2ea11123" -->
### 3. **Easier Code Review**
- PRs are smaller and focused
- Reviewer can focus on one concern at a time

<!-- section_id: "b0f4805a-dc71-493e-acbd-c14091594f2b" -->
### 4. **Better Testing**
- Tests map directly to implementation files
- `test_creation.py` tests `creation.py`

<!-- section_id: "1d037e6c-82f6-4e48-8737-edc8ab4ba9e7" -->
### 5. **Reduced Cognitive Load**
- Each file handles one concern
- Easier to understand and modify

<!-- section_id: "1a11705d-b523-4e34-9364-5464577ab9d9" -->
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

<!-- section_id: "9e692694-cb35-47ee-a46b-6332e72adad4" -->
## Quick Reference: When to Split Files

| Scenario | Action |
|----------|--------|
| 2+ agents could work on same concern simultaneously | ✅ Create separate files |
| File is over 300 lines | ✅ Consider splitting by concern |
| File has multiple distinct responsibilities | ✅ Split into focused modules |
| Functions are related but independent | ✅ Keep together but use clear sections |
| Functions share significant state | ⚠️ Keep together, add coordination rules |

<!-- section_id: "e739df72-d521-4da7-bf90-134c6acf1a3b" -->
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
