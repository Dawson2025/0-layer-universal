---
resource_id: "e5608b24-efbf-4f79-89d0-cbc98b287f51"
resource_type: "document"
resource_name: "DEVELOPMENT_CONVENTIONS"
---
# Development Conventions for Parallel AI Agents

<!-- section_id: "c8c4e2a8-bc12-4b7a-9395-080256012e67" -->
## Purpose

This document provides specific coding standards and conventions to ensure multiple AI agents can develop features simultaneously without conflicts, confusion, or integration issues.

---

<!-- section_id: "fb0f5b77-6219-4a98-8e9b-ed9984d78a5b" -->
## File Naming Conventions

<!-- section_id: "d363930d-d309-4035-82e8-a4559cd3a061" -->
### Python Files

- **Routes**: `routes.py` - Contains all Flask route handlers for the feature
- **API Endpoints**: `api.py` - Contains all `/api/*` endpoints for the feature
- **Models**: `models.py` - Database operations and data access layer
- **Business Logic**: Descriptive name (e.g., `search.py`, `branching.py`, `template_system.py`)
- **Tests**: `test_<functionality>.py` (e.g., `test_word_creation.py`, `test_group_invites.py`)

<!-- section_id: "1182c814-d67d-419a-ad8a-a888c04a58cd" -->
### Template Files

- Use lowercase with underscores: `word_creation_table.html`
- Include feature prefix for clarity: `admin_phonemes.html`, `group_detail.html`
- Place in feature-specific `templates/` subdirectory

<!-- section_id: "6d01fcd5-5771-4b33-aa88-7bf70d912171" -->
### Static Files

- **JavaScript**: Descriptive names, lowercase with underscores: `project_search.js`
- **CSS**: Match related template or feature: `word_creation.css`, `projects.css`
- Place in feature-specific `static/js/` or `static/css/` subdirectory

---

<!-- section_id: "4b8eb627-3c71-49cf-a41b-1433620b109c" -->
## Code Organization Patterns

<!-- section_id: "b0c22bfd-a836-444e-a419-223f83a36418" -->
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

<!-- section_id: "a4816eac-9d27-46d4-8623-345dca0ac7fb" -->
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

<!-- section_id: "e6debfcd-bfa4-4162-9e1e-b1e730b6738d" -->
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

<!-- section_id: "46d50c5b-b516-41b9-98aa-eb4bc01bdd1c" -->
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

<!-- section_id: "c6796224-8ed2-4d9a-ab2e-879986561a81" -->
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

<!-- section_id: "c47aba93-d7a2-41d2-9d75-a1334e34ccd3" -->
## Import Conventions

<!-- section_id: "9ee9e3f5-bd4d-4f9f-bcb3-0f0e0e6c9160" -->
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

<!-- section_id: "9ad736df-631c-4738-b677-ff0c59e924fc" -->
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

<!-- section_id: "358b3d25-3ea1-499e-b88a-67085178409c" -->
## Template Conventions

<!-- section_id: "b13d4d3a-ca68-4487-be43-c43601b8b314" -->
### Template Location

Templates MUST be in feature's `templates/` subdirectory:
```
features/words/templates/word_creation.html  ✅
templates/word_creation.html                  ❌
```

<!-- section_id: "f97be7c5-9961-4bf9-8b18-8de463d6a9ea" -->
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

<!-- section_id: "e4f7c842-a06d-4439-a354-21edc80796ca" -->
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

<!-- section_id: "715c7bf3-a1bc-46ac-930c-b5577f2c43c2" -->
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

<!-- section_id: "89aed625-e8c7-474a-9bbf-ebafd1d5b85d" -->
## Static Asset Conventions

<!-- section_id: "2b59a18e-9522-41a6-b16c-f8eaf83bd281" -->
### Feature-Specific Assets

CSS and JavaScript specific to a feature MUST live in that feature's static directory:

```
features/words/static/css/word_creation.css   ✅
static/css/word_creation.css                  ❌
```

<!-- section_id: "faec77cf-bf51-47ba-9faa-d3fb0397fddb" -->
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

<!-- section_id: "9a7bde3f-75ad-4973-98ad-f6a86d42f6b3" -->
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

<!-- section_id: "6a22db8b-1925-402d-8c78-9b55c4e757f4" -->
## Testing Conventions

<!-- section_id: "5098aa98-7aaa-46c7-be2c-744848d33139" -->
### Test File Location

Tests MUST be in feature's `tests/` subdirectory:

```
features/words/tests/test_word_creation.py   ✅
tests/test_word_creation.py                  ❌ (unless integration test)
```

<!-- section_id: "b41663a6-a7df-4eba-8c53-58c67aee921b" -->
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

<!-- section_id: "bc6d45ca-fe1a-4570-9394-cb0b25773101" -->
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

<!-- section_id: "6c53780f-a382-4ebc-902a-acc805766575" -->
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

<!-- section_id: "1d0d2452-6aa8-4308-95a6-4be2c9f10cbe" -->
## Database Conventions

<!-- section_id: "c124cf14-9f9d-4202-86a7-e7fd88402494" -->
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

<!-- section_id: "1056100b-036c-48bb-8a81-f789578658a6" -->
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

<!-- section_id: "6ebfe0ed-5ff3-4f61-826b-037e8a11aeb4" -->
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

<!-- section_id: "b1204c68-c03a-42af-bcbf-9ff4098f7228" -->
## Error Handling Conventions

<!-- section_id: "92cd37c0-e9dd-47d0-96e1-3bf85eb05c6a" -->
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

<!-- section_id: "e4d3f2d1-e8a0-4ce0-b6d4-5096e5a4bcfa" -->
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

<!-- section_id: "89f0cd04-9492-46de-87c7-ecc2073e2e28" -->
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

<!-- section_id: "6a8f9c7f-a972-4e10-b8ea-3719b1d8c2fb" -->
## Type Hints and Documentation

<!-- section_id: "fc2a532b-be4b-4d76-b0fd-7cbc9233f022" -->
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

<!-- section_id: "5b510df0-4708-4102-9dfa-710293d06a8f" -->
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

<!-- section_id: "185c4679-dc3d-49c3-9c65-92a5af9637ea" -->
## Git Commit Conventions

<!-- section_id: "0c0791ec-8b28-4ee7-9072-55c86a516376" -->
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

<!-- section_id: "f622b203-d65a-42e5-9fd7-c960c75a9c4e" -->
### Branch Naming

- Feature work: `feature/<feature-name>/<task>`
  - Example: `feature/words/mobile-creation-flow`
- Bug fixes: `bugfix/<feature-name>/<issue>`
  - Example: `bugfix/words/search-all-fields`
- Refactoring: `refactor/<area>/<description>`
  - Example: `refactor/core/database-helpers`

---

<!-- section_id: "d07090bf-8d3b-4734-8d66-b001328e3e3f" -->
## Coordination Patterns

<!-- section_id: "ce81631f-57e7-491c-a6ec-8976f6214e84" -->
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

<!-- section_id: "c1d0c008-096a-4d33-8e2d-cc0a6fb175fd" -->
### How to Coordinate

1. **Check active PRs**: Look for other PRs touching the same shared files
2. **Comment on overlap**: If overlap detected, comment on both PRs
3. **Determine order**: Decide which PR should merge first
4. **Rebase after**: Second PR rebases after first merges

<!-- section_id: "99e1237e-911e-412e-9c73-b13a1dd4465f" -->
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

<!-- section_id: "53f3aa97-25e0-4495-bea2-025fe3d57e12" -->
## Anti-Patterns to Avoid

<!-- section_id: "5a3c2c83-464c-4768-9a41-3e6b71b31ef2" -->
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

<!-- section_id: "6ad7f2c9-9755-4f7d-b7bc-fc345b40835e" -->
### ❌ Anti-Pattern 2: Circular Dependencies

```python
# features/words/models.py
from features.phonemes.models import get_phoneme  # OK

# features/phonemes/models.py
from features.words.models import get_word  # ❌ Circular!
```

**Solution**: Extract shared logic to `core/` or use dependency injection

<!-- section_id: "ef5a7673-b80c-48dd-a46b-f838e59b2f58" -->
### ❌ Anti-Pattern 3: Hard-Coded Paths

```python
# Bad
return render_template('../../templates/words/word_creation.html')  # ❌

# Good
return render_template('words/word_creation.html')  # ✅
```

<!-- section_id: "c8b1af3b-2db6-4b73-96ac-48cd6efc37d4" -->
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

<!-- section_id: "292d2f0c-4d9b-4a03-8e5f-c5918b4dd4f0" -->
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

<!-- section_id: "e1b0bf93-0a6d-493e-a851-c5c250be5bfe" -->
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

<!-- section_id: "14233972-586d-414e-bca5-826c85965692" -->
## Summary

**The Golden Rule**: Each feature is an isolated vertical slice. If you're working on `words`, you should only be touching `features/words/`. If you need to touch something outside that directory, pause and coordinate.

Following these conventions ensures multiple AI agents can build features in parallel without stepping on each other's toes!
