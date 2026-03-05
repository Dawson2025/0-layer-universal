---
resource_id: "d479dd41-a51d-4340-adc3-f99a41f77de8"
resource_type: "document"
resource_name: "DEVELOPMENT_CONVENTIONS"
---
# Development Conventions for Parallel AI Agents

<!-- section_id: "4a33661a-7246-46de-8e54-cf0caca6ae04" -->
## Purpose

This document provides specific coding standards and conventions to ensure multiple AI agents can develop features simultaneously without conflicts, confusion, or integration issues.

---

<!-- section_id: "a0f3741c-98e6-409a-af24-bc0cb85e5c8d" -->
## File Naming Conventions

<!-- section_id: "7bc2f15e-65d9-4f85-9e94-b310b915495a" -->
### Python Files

- **Routes**: `routes.py` - Contains all Flask route handlers for the feature
- **API Endpoints**: `api.py` - Contains all `/api/*` endpoints for the feature
- **Models**: `models.py` - Database operations and data access layer
- **Business Logic**: Descriptive name (e.g., `search.py`, `branching.py`, `template_system.py`)
- **Tests**: `test_<functionality>.py` (e.g., `test_word_creation.py`, `test_group_invites.py`)

<!-- section_id: "e338f7d3-4830-4695-bc92-4f06de131fda" -->
### Template Files

- Use lowercase with underscores: `word_creation_table.html`
- Include feature prefix for clarity: `admin_phonemes.html`, `group_detail.html`
- Place in feature-specific `templates/` subdirectory

<!-- section_id: "d81d9b21-d782-4dd5-8122-fadea2a91fc4" -->
### Static Files

- **JavaScript**: Descriptive names, lowercase with underscores: `project_search.js`
- **CSS**: Match related template or feature: `word_creation.css`, `projects.css`
- Place in feature-specific `static/js/` or `static/css/` subdirectory

---

<!-- section_id: "d2b846f9-45aa-4430-97c7-82b0bad2f600" -->
## Code Organization Patterns

<!-- section_id: "9ed77f22-c301-44c1-ab92-1624b0408062" -->
### Feature Module Structure

Every feature module MUST follow this structure:

```
features/<feature_name>/
├── __init__.py          # Blueprint registration and exports
├── routes.py            # Page route handlers (@blueprint.route('/...'))
├── api.py               # API endpoint handlers (optional, if feature has APIs)
├── models.py            # Database operations
├── <business_logic>.py  # Feature-specific logic (search.py, branching.py, etc.)
├── templates/
│   └── *.html
├── static/
│   ├── js/
│   │   └── *.js
│   └── css/
│       └── *.css
└── tests/
    └── test_*.py
```

<!-- section_id: "f0e263be-999d-40e9-a8d1-cf99b82a712d" -->
### Blueprint Definition (`__init__.py`)

Every feature must register a Flask Blueprint:

```python
"""
<Feature Name> Feature

<Brief description of what this feature does>
"""

from flask import Blueprint

# Create blueprint
<feature>_bp = Blueprint(
    '<feature>',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/<feature>'
)

# Import routes to register them with blueprint
from . import routes
if hasattr('api', __name__):
    from . import api

__all__ = ['<feature>_bp']
```

**Example** (`features/words/__init__.py`):
```python
from flask import Blueprint

words_bp = Blueprint(
    'words',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/static/words'
)

from . import routes
from . import api

__all__ = ['words_bp']
```

<!-- section_id: "46321762-d066-4d47-9116-20651b5cef8e" -->
### Routes Definition (`routes.py`)

```python
"""
Route handlers for <feature> feature.

All user-facing pages for <feature> functionality.
"""

from flask import render_template, request, redirect, url_for, flash
from features.auth.helpers import require_auth, get_user_info
from . import <feature>_bp

@<feature>_bp.route('/<feature>')
@require_auth
def <feature>_menu():
    """Display <feature> main page."""
    user = get_user_info()
    # ... implementation
    return render_template('<feature>/<template>.html', user=user)

# More routes...
```

**Example** (`features/words/routes.py`):
```python
from flask import render_template
from features.auth.helpers import require_auth, get_user_info
from . import words_bp

@words_bp.route('/words')
@require_auth
def words_menu():
    """Display words main menu."""
    user = get_user_info()
    return render_template('words/words_menu.html', user=user)

@words_bp.route('/words/display')
@require_auth
def display_words():
    """Display all words for current project."""
    user = get_user_info()
    from .models import get_all_words
    words = get_all_words(user['current_project']['id'])
    return render_template('words/words_display.html', words=words, user=user)
```

<!-- section_id: "a8dd3772-48c2-4d1b-8ef2-07b365dc0204" -->
### API Endpoints (`api.py`)

```python
"""
API endpoints for <feature> feature.

All JSON-returning API routes for <feature> functionality.
"""

from flask import jsonify, request
from features.auth.helpers import require_auth, get_user_info
from . import <feature>_bp

@<feature>_bp.route('/api/<feature>/<action>', methods=['POST'])
@require_auth
def api_<action>():
    """API endpoint to <do something>."""
    user = get_user_info()
    data = request.get_json()

    # Business logic
    from .models import perform_action
    result = perform_action(data, user['current_project']['id'])

    return jsonify({'success': True, 'data': result})
```

<!-- section_id: "3b80799e-2f94-42ee-81fd-2680a886833f" -->
### Models/Database Layer (`models.py`)

```python
"""
Database operations for <feature> feature.

All SQL queries and data access logic for <feature>.
"""

from typing import List, Dict, Optional
import sqlite3
from core.database import get_db_connection, execute_query

def get_<entity>(entity_id: int, project_id: str) -> Optional[Dict]:
    """Retrieve a single <entity> by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM <table> WHERE id = ? AND project_id = ?",
        (entity_id, project_id)
    )
    result = cursor.fetchone()
    conn.close()

    if not result:
        return None

    return {
        'id': result[0],
        'name': result[1],
        # ... map columns to dict
    }

def get_all_<entities>(project_id: str) -> List[Dict]:
    """Retrieve all <entities> for a project."""
    # ... implementation
    pass

def create_<entity>(data: Dict, project_id: str) -> int:
    """Create a new <entity>."""
    # ... implementation
    pass
```

---

<!-- section_id: "1ecb497f-61ba-4f8b-8ed9-a896c7e9cf32" -->
## Import Conventions

<!-- section_id: "9538dc03-7d7a-4da6-8c3b-4fdbcb6d0db9" -->
### Import Order

1. Standard library imports
2. Third-party imports (Flask, etc.)
3. Core/shared imports (`core.*`, `services.*`)
4. Cross-feature imports (`features.<other_feature>.*`)
5. Relative imports from current feature (`. import`)

```python
# 1. Standard library
import sqlite3
from typing import Dict, List, Optional
from datetime import datetime

# 2. Third-party
from flask import Blueprint, render_template, request, jsonify

# 3. Core/shared
from core.database import get_db_connection
from services.firebase.firestore import firestore_db
from features.auth.helpers import require_auth, get_user_info

# 4. Cross-feature (minimize these!)
from features.projects.metadata import normalize_project_identifier

# 5. Relative imports
from . import words_bp
from .models import get_all_words
```

<!-- section_id: "3d72f282-50c0-4654-898c-cc68c298f298" -->
### Dependency Rules

**Allowed**:
- ✅ Feature → Core (`features.words` → `core.database`)
- ✅ Feature → Services (`features.words` → `services.tts`)
- ✅ Feature → Auth helpers (`features.words` → `features.auth.helpers`)
- ✅ Feature → Project metadata (`features.words` → `features.projects.metadata`)

**Not Allowed**:
- ❌ Feature → Feature routes (`features.words.routes` → `features.phonemes.routes`)
- ❌ Feature → Feature business logic (`features.words` → `features.admin.template_system`)
- ❌ Core → Feature (`core.database` → `features.words`)
- ❌ Service → Feature (`services.tts` → `features.words`)

**If you need cross-feature data**:
- Use models layer: `from features.phonemes.models import get_phoneme`
- Don't call routes or business logic directly

---

<!-- section_id: "bb0058d7-5415-429f-92dc-d878e08182c7" -->
## Template Conventions

<!-- section_id: "6ec26d3a-8958-4b63-b576-5136e2b8549f" -->
### Template Location

Templates MUST be in feature's `templates/` subdirectory:
```
features/words/templates/word_creation.html  ✅
templates/word_creation.html                  ❌
```

<!-- section_id: "fc022f55-9800-4753-9d6f-c0e97947bbb5" -->
### Template Rendering

Use feature-relative paths when rendering:

```python
# In features/words/routes.py
@words_bp.route('/words/create')
def create_word():
    # Correct - Flask knows to look in words/templates/
    return render_template('words/word_creation.html')

    # Incorrect - would look in global templates/
    # return render_template('word_creation.html')
```

<!-- section_id: "d2f176ed-089c-4c81-8eb2-07b51fe05d7e" -->
### Template Inheritance

All feature templates should extend the global base template:

```html
{% extends "base.html" %}

{% block title %}Word Creation - Language Tracker{% endblock %}

{% block content %}
<div class="words-feature">
    <!-- Feature-specific content -->
</div>
{% endblock %}
```

<!-- section_id: "8f5453b6-62a0-425f-a040-7daff55c7059" -->
### Template Variables

Always pass `user` context to templates:

```python
from features.auth.helpers import get_user_info

@words_bp.route('/words')
def words_menu():
    user = get_user_info()
    # Always include user in template context
    return render_template('words/words_menu.html', user=user)
```

---

<!-- section_id: "794c86c0-3f1d-48e6-af93-7798666ee39b" -->
## Static Asset Conventions

<!-- section_id: "22e87841-0ba4-44e3-a1c9-bcc29a880a4a" -->
### Feature-Specific Assets

CSS and JavaScript specific to a feature MUST live in that feature's static directory:

```
features/words/static/css/word_creation.css   ✅
static/css/word_creation.css                  ❌
```

<!-- section_id: "d5182654-e2cd-4cb2-8fc9-457dd4e3dd9e" -->
### Loading Feature Assets in Templates

```html
{% extends "base.html" %}

{% block head %}
<!-- Feature-specific CSS -->
<link rel="stylesheet" href="{{ url_for('words.static', filename='css/word_creation.css') }}">
{% endblock %}

{% block content %}
<!-- Content here -->
{% endblock %}

{% block scripts %}
<!-- Feature-specific JavaScript -->
<script src="{{ url_for('words.static', filename='js/word_creation.js') }}"></script>
{% endblock %}
```

<!-- section_id: "10c0ddcb-369d-46d0-a3ad-d7581516185a" -->
### Global vs Feature Assets

**Global assets** (`static/`):
- Base styles used across all features
- Global JavaScript utilities
- Shared images/logos

**Feature assets** (`features/<name>/static/`):
- Feature-specific styling
- Feature-specific JavaScript
- Feature-unique images

---

<!-- section_id: "a0cfd46a-c07c-4e89-9e1d-ab37ec690456" -->
## Testing Conventions

<!-- section_id: "626ce102-51cb-47a5-97da-56baa59e076c" -->
### Test File Location

Tests MUST be in feature's `tests/` subdirectory:

```
features/words/tests/test_word_creation.py   ✅
tests/test_word_creation.py                  ❌ (unless integration test)
```

<!-- section_id: "60474653-c203-479d-af88-c2edca291882" -->
### Test Naming

- Filename: `test_<functionality>.py`
- Test class: `Test<Functionality>`
- Test method: `test_<specific_behavior>`

```python
# features/words/tests/test_word_creation.py

import unittest
from unittest.mock import patch, MagicMock

class TestWordCreation(unittest.TestCase):
    """Tests for word creation functionality."""

    def test_create_word_with_valid_data(self):
        """Should create word when all required fields provided."""
        # ... test implementation

    def test_create_word_rejects_duplicate(self):
        """Should reject word creation if word already exists."""
        # ... test implementation

    def test_create_word_updates_phoneme_frequencies(self):
        """Should increment phoneme frequency counts after word creation."""
        # ... test implementation
```

<!-- section_id: "04ea1ee0-8d12-4493-bd1b-62e6d6db4ca9" -->
### Test Isolation

Feature tests should NOT depend on other features being present:

```python
# Good - Mock cross-feature dependencies
@patch('features.phonemes.models.get_phoneme')
def test_word_validates_phonemes(self, mock_get_phoneme):
    mock_get_phoneme.return_value = {'id': 1, 'ipa': 'a'}
    # ... test implementation

# Bad - Direct dependency on phonemes feature
def test_word_validates_phonemes(self):
    from features.phonemes.models import get_phoneme
    phoneme = get_phoneme(1, 'project123')  # Requires phonemes feature to work!
    # ... test implementation
```

<!-- section_id: "a0d5500b-a3d0-4c83-b96e-d7788184f2e4" -->
### Integration Tests

Full cross-feature tests go in global `tests/` directory:

```python
# tests/test_integration.py

class TestWordPhonemeIntegration(unittest.TestCase):
    """Integration tests between words and phonemes features."""

    def test_creating_word_updates_phoneme_frequencies(self):
        """End-to-end test of word creation affecting phonemes."""
        # This test can touch both features
```

---

<!-- section_id: "db1e9fd7-aa73-40fa-a534-704d7ca9bb4b" -->
## Database Conventions

<!-- section_id: "413953c7-97b9-44cf-a6ea-7c778697a4a5" -->
### Schema Changes

Database migrations must be coordinated:

1. **One agent at a time** creates migrations
2. Create migration file in `migrations/versions/`
3. Name migration descriptively: `001_add_phoneme_categories.sql`
4. Document in migration what feature needs it

```sql
-- migrations/versions/003_add_word_media_fields.sql
-- Required for: features/words (media management)
-- Author: AI Agent 3
-- Date: 2025-10-15

ALTER TABLE words ADD COLUMN video_path TEXT;
ALTER TABLE words ADD COLUMN image_path TEXT;
```

<!-- section_id: "671dca51-980c-42d3-a170-4f007acfb3a5" -->
### Database Access Patterns

**Always use the core database helper**:

```python
# Good - Use core helper
from core.database import get_db_connection

def get_word(word_id: int):
    conn = get_db_connection()
    # ... query
    conn.close()

# Bad - Direct sqlite3 usage
import sqlite3

def get_word(word_id: int):
    conn = sqlite3.connect('language_tracker.db')  # ❌ Hard-coded path
    # ... query
```

<!-- section_id: "b7e11406-e3cc-4a88-a46d-d1dd7faa80b7" -->
### Transaction Pattern

For multi-statement operations, use transactions:

```python
from core.database import get_db_connection

def create_word_with_phonemes(word_data: Dict, phoneme_ids: List[int]):
    """Create word and update phoneme frequencies atomically."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()

        # Insert word
        cursor.execute("INSERT INTO words (...) VALUES (...)", word_data)
        word_id = cursor.lastrowid

        # Update phoneme frequencies
        for phoneme_id in phoneme_ids:
            cursor.execute(
                "UPDATE phonemes SET frequency = frequency + 1 WHERE id = ?",
                (phoneme_id,)
            )

        conn.commit()
        return word_id

    except Exception as e:
        conn.rollback()
        raise
    finally:
        conn.close()
```

---

<!-- section_id: "97408c96-bd55-4adf-bd52-1e5446c158dd" -->
## Error Handling Conventions

<!-- section_id: "93ba2e7f-8be5-48f0-846b-eb5494613195" -->
### API Endpoints

Always return consistent JSON structure:

```python
# Success
return jsonify({
    'success': True,
    'data': result,
    'message': 'Word created successfully'
}), 201

# Error
return jsonify({
    'success': False,
    'error': 'Word already exists',
    'details': {'field': 'word', 'value': 'test'}
}), 400
```

<!-- section_id: "4565fe69-42e9-4169-95c9-285202e767c7" -->
### Route Handlers

Use Flask's `flash()` for user messages:

```python
from flask import flash, redirect, url_for

@words_bp.route('/words/create', methods=['POST'])
def create_word():
    try:
        # ... create word
        flash('Word created successfully!', 'success')
        return redirect(url_for('words.words_menu'))
    except ValueError as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('words.create_word_menu'))
```

<!-- section_id: "9fbcb60e-3a4d-4fc4-985a-7dacc217cc50" -->
### Logging

Use consistent logging format:

```python
import logging

logger = logging.getLogger(__name__)

@words_bp.route('/api/create-word', methods=['POST'])
def api_create_word():
    logger.info(f"Creating word for user {user['id']}, project {project_id}")
    try:
        # ... logic
        logger.info(f"Word {word_id} created successfully")
    except Exception as e:
        logger.error(f"Error creating word: {str(e)}", exc_info=True)
        raise
```

---

<!-- section_id: "b99643c2-0753-4e57-8a3a-11e17fdc74c2" -->
## Type Hints and Documentation

<!-- section_id: "80e2bbaa-8481-4e11-8fb4-2048ecfa25c5" -->
### Function Signatures

Always include type hints:

```python
from typing import List, Dict, Optional

def get_words_by_phoneme(
    phoneme_id: int,
    project_id: str,
    limit: Optional[int] = None
) -> List[Dict[str, Any]]:
    """
    Retrieve all words containing a specific phoneme.

    Args:
        phoneme_id: ID of the phoneme to search for
        project_id: Project identifier (local int or cloud string)
        limit: Maximum number of results (None for unlimited)

    Returns:
        List of word dictionaries with keys: id, word, english, phonemes

    Raises:
        ValueError: If phoneme_id or project_id invalid
    """
    # Implementation
```

<!-- section_id: "53571e7a-a9aa-4319-850c-ff7ac73074f8" -->
### Class Documentation

```python
class WordCreationService:
    """
    Service for creating and validating new words.

    This service handles business logic for word creation including:
    - Phoneme validation
    - Duplicate checking
    - Media attachment
    - Frequency updates
    """

    def __init__(self, project_id: str):
        """
        Initialize word creation service.

        Args:
            project_id: Project identifier for all operations
        """
        self.project_id = project_id
```

---

<!-- section_id: "780892c1-ae9a-46e0-aefe-81fedf12952f" -->
## Git Commit Conventions

<!-- section_id: "c3403c37-5ac5-4e77-af71-27fadfcbc81e" -->
### Commit Message Format

```
[Feature] Brief description

Detailed explanation of what changed and why.

Affected routes:
- GET /words/create
- POST /api/create-word

Files modified:
- features/words/routes.py
- features/words/api.py
- features/words/templates/word_creation.html

Related requirement: word_management.md
```

<!-- section_id: "5b0c1c30-a0b9-4127-a201-819b8ac8076a" -->
### Branch Naming

- Feature work: `feature/<feature-name>/<task>`
  - Example: `feature/words/mobile-creation-flow`
- Bug fixes: `bugfix/<feature-name>/<issue>`
  - Example: `bugfix/words/search-all-fields`
- Refactoring: `refactor/<area>/<description>`
  - Example: `refactor/core/database-helpers`

---

<!-- section_id: "b23b47c7-cf5a-44e5-8978-7f1520c518d7" -->
## Coordination Patterns

<!-- section_id: "02295c85-7397-4ce7-b7a0-c355066861cc" -->
### When to Coordinate

**No coordination needed** (work freely):
- Adding new routes to your feature
- Adding new templates to your feature
- Adding new static assets to your feature
- Adding tests to your feature
- Modifying feature-specific business logic

**Coordination required**:
- Modifying `core/*` or `services/*`
- Adding new database tables/columns
- Modifying global templates (`templates/base.html`)
- Modifying global static assets (`static/css/global.css`)
- Changing shared function signatures

<!-- section_id: "ced8ac8e-8185-4d88-94bf-394d34419717" -->
### How to Coordinate

1. **Check active PRs**: Look for other PRs touching the same shared files
2. **Comment on overlap**: If overlap detected, comment on both PRs
3. **Determine order**: Decide which PR should merge first
4. **Rebase after**: Second PR rebases after first merges

<!-- section_id: "ae9f3d37-1211-4acb-b550-7a2ae9868007" -->
### Example Coordination

**Scenario**: Agent A needs new auth decorator, Agent B needs database helper

**Agent A**:
```python
# core/decorators.py
def require_project_owner(func):
    """New decorator for project ownership check."""
    # ... implementation
```

**Agent B**:
```python
# core/database.py
def get_project_owner(project_id: str) -> int:
    """New helper to get project owner ID."""
    # ... implementation
```

**Both touching `core/`**:
- Check if editing different files (`decorators.py` vs `database.py`) ✅ OK
- If editing same file → coordinate merge order

---

<!-- section_id: "36e3c2f7-9f34-4757-816f-99ddf857e6db" -->
## Anti-Patterns to Avoid

<!-- section_id: "3e73cc8c-3f1b-47d4-9dae-ea8dedda8915" -->
### ❌ Anti-Pattern 1: Cross-Feature Route Calls

```python
# Bad - Feature calling another feature's route
from features.phonemes.routes import display_phonemes

@words_bp.route('/words/with-phoneme')
def words_with_phoneme():
    return display_phonemes()  # ❌ Don't do this!
```

**Solution**: Use redirect or call models layer instead:
```python
from flask import redirect, url_for
from features.phonemes.models import get_all_phonemes

@words_bp.route('/words/with-phoneme')
def words_with_phoneme():
    # Option 1: Redirect
    return redirect(url_for('phonemes.display_phonemes'))

    # Option 2: Use models layer
    phonemes = get_all_phonemes(project_id)
    # ... render with phoneme data
```

<!-- section_id: "d37ae122-f9f1-492c-bab4-298325ccd89e" -->
### ❌ Anti-Pattern 2: Circular Dependencies

```python
# features/words/models.py
from features.phonemes.models import get_phoneme  # OK

# features/phonemes/models.py
from features.words.models import get_word  # ❌ Circular!
```

**Solution**: Extract shared logic to `core/` or use dependency injection

<!-- section_id: "9013a8a0-73c8-43d0-a88d-be37cc907028" -->
### ❌ Anti-Pattern 3: Hard-Coded Paths

```python
# Bad
return render_template('../../templates/words/word_creation.html')  # ❌

# Good
return render_template('words/word_creation.html')  # ✅
```

<!-- section_id: "28ae9850-34ba-485c-aa8d-dba63beb7261" -->
### ❌ Anti-Pattern 4: Direct Database Access in Routes

```python
# Bad - Database logic in route handler
@words_bp.route('/words/<int:word_id>')
def view_word(word_id):
    conn = sqlite3.connect('database.db')  # ❌
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM words WHERE id = ?", (word_id,))
    # ... more SQL in route handler
```

**Solution**: Use models layer:
```python
# Good - Route calls model
@words_bp.route('/words/<int:word_id>')
def view_word(word_id):
    from .models import get_word
    word = get_word(word_id, project_id)
    return render_template('words/word_detail.html', word=word)
```

<!-- section_id: "df258c25-7e25-4aff-b1eb-b0277d715ed8" -->
### ❌ Anti-Pattern 5: Global State

```python
# Bad - Global mutable state
CURRENT_PROJECT = None

@words_bp.route('/words')
def words_menu():
    global CURRENT_PROJECT  # ❌ Not thread-safe!
    CURRENT_PROJECT = session.get('current_project_id')
```

**Solution**: Use session or pass as parameter:
```python
# Good
@words_bp.route('/words')
def words_menu():
    user = get_user_info()  # Gets from session
    project_id = user['current_project']['id']
```

---

<!-- section_id: "d6a102d4-70cd-435f-8f86-30313973cdd3" -->
## Quick Reference Checklist

Before committing feature work:

- [ ] All routes in `features/<feature>/routes.py`
- [ ] All API endpoints in `features/<feature>/api.py`
- [ ] All database queries in `features/<feature>/models.py`
- [ ] All templates in `features/<feature>/templates/`
- [ ] All static assets in `features/<feature>/static/`
- [ ] All tests in `features/<feature>/tests/`
- [ ] Type hints on all functions
- [ ] Docstrings on all public functions
- [ ] No cross-feature route imports
- [ ] Used core/services for shared logic
- [ ] Coordinated if touching shared files
- [ ] Tests pass in isolation
- [ ] Updated feature requirements doc if behavior changed

---

<!-- section_id: "05ecfd4b-e804-40f6-be07-2809e7740be9" -->
## Summary

**The Golden Rule**: Each feature is an isolated vertical slice. If you're working on `words`, you should only be touching `features/words/`. If you need to touch something outside that directory, pause and coordinate.

Following these conventions ensures multiple AI agents can build features in parallel without stepping on each other's toes!
