---
resource_id: "f264846b-adbf-4d69-8dfc-d5bcf2c3ec6e"
resource_type: "document"
resource_name: "QUICK_START_PARALLEL_DEVELOPMENT"
---
# Quick Start: Parallel Development Guide

<!-- section_id: "1c34af14-8c5b-4a92-9c58-c2a5d8f0d987" -->
## What This Is

A fast-reference guide for AI agents working on the Language Tracker application in parallel. Read this first, then dive into detailed docs as needed.

---

<!-- section_id: "91a6f2e8-5ec5-4524-be04-2b53518c2f8e" -->
## 🎯 The Core Concept

**One Feature = One Directory**

Each feature lives in its own isolated folder under `features/`. Multiple AI agents can work on different features simultaneously without conflicts because each agent stays in their own directory.

---

<!-- section_id: "df817258-f399-4d65-b936-34e8a07f93a2" -->
## 📁 Where to Put Your Code

<!-- section_id: "873ec12c-cf6c-400c-a980-6b03f665ba59" -->
### I'm Working On...

| Feature | My Directory | I Own These Files |
|---------|-------------|-------------------|
| **Authentication** (Login/Register) | `features/auth/` | All `/login`, `/register`, `/logout` routes |
| **Dashboard** | `features/dashboard/` | `/dashboard` route and template |
| **Groups** | `features/groups/` | All `/groups/*` routes and group templates |
| **Projects** | `features/projects/` | All `/projects/*` routes, project management |
| **Variant Menu** | `features/variant_menu/` | `/main-menu` and project navigation |
| **Phonemes** | `features/phonemes/` | All `/phonemes/*` routes and views |
| **Words** | `features/words/` | All `/words/*` routes, word creation, search |
| **Administration** | `features/admin/` | All `/admin/*` routes and admin tools |

<!-- section_id: "6e274cb3-8e8e-492e-b052-655e8f999834" -->
### Basic Feature Structure

```
features/my_feature/
├── __init__.py          # Blueprint registration
├── routes.py            # Page routes (GET /my-feature)
├── api.py               # API endpoints (POST /api/my-feature/action)
├── models.py            # Database queries
├── business_logic.py    # Feature-specific logic
├── templates/           # HTML templates for this feature
│   └── my_template.html
├── static/              # CSS/JS for this feature
│   ├── css/
│   └── js/
└── tests/               # Tests for this feature
    └── test_my_feature.py
```

---

<!-- section_id: "7456f444-3396-424a-9d00-2d370c81db06" -->
## ✅ Quick Checklist

Before starting work:

- [ ] I know which feature I'm working on
- [ ] All my files will go in `features/<feature_name>/`
- [ ] I won't touch other features' directories
- [ ] If I need shared code, I'll check `core/` or `services/`

Before committing:

- [ ] All my routes are in `features/<feature>/routes.py`
- [ ] All my templates are in `features/<feature>/templates/`
- [ ] All my tests are in `features/<feature>/tests/`
- [ ] I only modified files in my feature directory (unless coordinated)

---

<!-- section_id: "12b4a157-677e-4964-944f-9d7d1fcb33d2" -->
## 🚦 Traffic Light System

<!-- section_id: "46f372df-7bbc-4581-9cb6-d5799d5e4fde" -->
### 🟢 GREEN - Work Freely (No Coordination Needed)

- Adding routes to your feature
- Creating templates in your feature
- Adding CSS/JS to your feature's static folder
- Writing tests for your feature
- Modifying business logic in your feature

<!-- section_id: "c1b4a0ef-93f6-4b2f-bc8c-d4a7d89d5e34" -->
### 🟡 YELLOW - Check First

- Using functions from `core/` or `services/`
- Importing from another feature's `models.py`
- Modifying global templates (`templates/base.html`)
- Adding database migrations

<!-- section_id: "1ea9d94b-afd7-4a6e-8aae-dddbf2350822" -->
### 🔴 RED - Must Coordinate

- Modifying `core/*` shared modules
- Modifying `services/*` shared services
- Changing database schema
- Modifying `app.py` (except adding new blueprint)
- Modifying another feature's code

---

<!-- section_id: "b37c7e14-42f3-4936-80ad-c05713ef2de9" -->
## 📖 Common Patterns

<!-- section_id: "93c03dfc-1e89-48cc-b872-6b830f813dad" -->
### Pattern 1: Create a New Route

```python
# features/my_feature/routes.py

from flask import render_template
from features.auth.helpers import require_auth, get_user_info
from . import my_feature_bp

@my_feature_bp.route('/my-feature')
@require_auth
def my_feature_page():
    user = get_user_info()
    return render_template('my_feature/page.html', user=user)
```

<!-- section_id: "89e9772f-aeaa-43bd-a7e5-efa31f42e752" -->
### Pattern 2: Create an API Endpoint

```python
# features/my_feature/api.py

from flask import jsonify, request
from features.auth.helpers import require_auth, get_user_info
from . import my_feature_bp

@my_feature_bp.route('/api/my-feature/action', methods=['POST'])
@require_auth
def api_do_action():
    user = get_user_info()
    data = request.get_json()

    # Call models layer
    from .models import perform_action
    result = perform_action(data, user['current_project']['id'])

    return jsonify({'success': True, 'data': result})
```

<!-- section_id: "5e3880af-403e-4d05-8d0d-6e2ffea5b89c" -->
### Pattern 3: Database Query

```python
# features/my_feature/models.py

from typing import List, Dict, Optional
from core.database import get_db_connection

def get_items(project_id: str) -> List[Dict]:
    """Retrieve all items for a project."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM items WHERE project_id = ?",
        (project_id,)
    )
    results = cursor.fetchall()
    conn.close()

    return [
        {'id': r[0], 'name': r[1], 'value': r[2]}
        for r in results
    ]
```

<!-- section_id: "0cfa2efc-9311-42bf-a5ea-8ce702c1765e" -->
### Pattern 4: Render Template

```python
# features/my_feature/routes.py

@my_feature_bp.route('/my-feature/list')
@require_auth
def list_items():
    user = get_user_info()
    from .models import get_items

    items = get_items(user['current_project']['id'])

    # Template path is relative to feature's templates/ folder
    return render_template('my_feature/list.html', items=items, user=user)
```

```html
<!-- features/my_feature/templates/my_feature/list.html -->

{% extends "base.html" %}

{% block title %}My Feature - Language Tracker{% endblock %}

{% block content %}
<div class="my-feature">
    <h1>Items</h1>
    {% for item in items %}
        <div>{{ item.name }}</div>
    {% endfor %}
</div>
{% endblock %}
```

---

<!-- section_id: "65a2a3f7-7f05-4352-8145-9b35158285fc" -->
## 🚫 What NOT to Do

<!-- section_id: "c6023105-3f87-4712-a5c0-f75e6c94a6c2" -->
### ❌ Don't Import Other Features' Routes

```python
# BAD - Don't do this!
from features.words.routes import create_word_page

@my_feature_bp.route('/my-feature')
def my_page():
    return create_word_page()  # ❌ Calling another feature's route
```

<!-- section_id: "dc1c5945-c53f-48b9-b93e-2bb6befd2a2b" -->
### ✅ Instead, Use Models or Redirect

```python
# GOOD - Use models layer
from features.words.models import get_all_words

@my_feature_bp.route('/my-feature')
def my_page():
    words = get_all_words(project_id)  # ✅ Using models
    return render_template('my_feature/page.html', words=words)

# OR redirect to the other feature
from flask import redirect, url_for

@my_feature_bp.route('/my-feature/to-words')
def go_to_words():
    return redirect(url_for('words.words_menu'))  # ✅ Redirect
```

<!-- section_id: "611c3491-ba2c-4e6d-b81b-3585e49f4c78" -->
### ❌ Don't Put Templates in Global Directory

```python
# BAD
return render_template('my_page.html')  # Looks in global templates/

# GOOD
return render_template('my_feature/my_page.html')  # Looks in features/my_feature/templates/
```

<!-- section_id: "85b6d88c-e1bb-4763-aba0-191898aaf987" -->
### ❌ Don't Hard-Code Database Paths

```python
# BAD
import sqlite3
conn = sqlite3.connect('/path/to/database.db')  # ❌

# GOOD
from core.database import get_db_connection
conn = get_db_connection()  # ✅
```

---

<!-- section_id: "58d60049-8f70-4a85-be1d-fbf97d8c523e" -->
## 🔍 Need More Detail?

<!-- section_id: "eec845ad-d859-493a-aa0a-9ff4366a5732" -->
### Detailed Architecture Documentation

**[Parallel Development Architecture](PARALLEL_DEVELOPMENT_ARCHITECTURE.md)**
- Complete folder structure design
- Feature ownership matrix
- Shared dependency interfaces
- Migration plan from current monolithic structure
- Conflict avoidance strategies

**[Development Conventions](DEVELOPMENT_CONVENTIONS.md)**
- File naming conventions
- Import order rules
- Blueprint registration patterns
- Testing conventions
- Error handling standards
- Type hints and documentation guidelines

<!-- section_id: "3b29cf53-3002-4372-81c6-595f5f09446d" -->
### Requirements Documentation

**[Requirements Overview](requirements/README.md)**
- All feature specifications organized by navigation level
- Maps features to their purpose and expected outcomes
- Links to detailed requirement documents

**[Parallel Feature Isolation Spec](requirements/parallel_feature_isolation.md)**
- Original requirements for parallel development capability
- Acceptance criteria and expected outcomes

---

<!-- section_id: "e0a34246-269b-4a04-98b7-0fa216b846b5" -->
## 🎮 Parallel Development Scenarios

<!-- section_id: "7cab63f7-70da-48bc-9f49-d3208b37ce26" -->
### Scenario 1: Three Agents, Three Features

**Agent 1** works on: `features/words/` (search enhancement)
**Agent 2** works on: `features/groups/` (invite system)
**Agent 3** works on: `features/admin/` (template import)

**Result**: Zero conflicts! Each agent has isolated workspace.

<!-- section_id: "f63b45cd-af0a-42b7-bd36-246c27fdd826" -->
### Scenario 2: One Shared Module Change

**Problem**: Agent 1 needs to add function to `core/database.py`

**Solutions**:
1. **Sequential**: Agent 1 creates PR, merges, others pull latest
2. **Interface First**: Define function signature (stub) first, implement later
3. **Feature-Local**: Keep logic in feature if only one feature needs it

<!-- section_id: "7376f8a4-ef7f-4019-8aec-21590427c246" -->
### Scenario 3: Database Migration

**Problem**: Agent 1 needs new column in `words` table

**Solution**:
1. Create migration file in `migrations/versions/`
2. Document which feature needs it
3. Coordinate with other agents to ensure they run migration
4. Only one agent creates migrations at a time

---

<!-- section_id: "c11cf24b-b29d-44a3-96ab-a3110d1d4b28" -->
## 💡 Pro Tips

1. **Stay in Your Lane**: 95% of your work should be in `features/<your_feature>/`

2. **Use Existing Helpers**: Before creating new shared code, check if it exists in `core/` or `services/`

3. **Type Hints Are Your Friend**: They help other agents understand your interfaces

4. **Test in Isolation**: Your tests should run without other features present

5. **Document Interfaces**: If you create a function another feature might use, document it well

6. **Check for PRs**: Before modifying shared code, check if another PR is touching it

7. **Small PRs**: Each PR should focus on one feature or one specific change

8. **Descriptive Commits**: Make it clear which feature you're working on

---

<!-- section_id: "169e25cb-b5ba-4eca-8697-4784ffbdfb6d" -->
## 🆘 Quick Reference

| I Want To... | Where Do I Look? |
|--------------|------------------|
| Add a new page route | `features/<feature>/routes.py` |
| Add an API endpoint | `features/<feature>/api.py` |
| Query the database | `features/<feature>/models.py` |
| Create a template | `features/<feature>/templates/` |
| Add CSS/JavaScript | `features/<feature>/static/` |
| Write a test | `features/<feature>/tests/` |
| Use auth helpers | `from features.auth.helpers import get_user_info` |
| Get database connection | `from core.database import get_db_connection` |
| Access Firebase | `from services.firebase.firestore import firestore_db` |
| Use TTS | `from services.tts.azure_tts import synthesize_phoneme` |

---

<!-- section_id: "7232a8a7-ff51-42c7-a4ff-24b2c8f6b4bd" -->
## 🚀 Getting Started

1. **Identify your feature** from the [Requirements Overview](requirements/README.md)
2. **Check if feature directory exists** in `features/<feature_name>/`
3. **If not, create it** with standard structure (see above)
4. **Add your code** following the patterns above
5. **Write tests** in `features/<feature>/tests/`
6. **Run tests** to verify everything works
7. **Commit** with clear feature prefix: `[Words] Add search all fields`
8. **Create PR** focused on your feature only

---

<!-- section_id: "56ceeff7-b6cf-4af7-b151-5e800f7ac099" -->
## Summary

**The Golden Rule**: If you're working on `words`, you touch `features/words/`. If you're working on `groups`, you touch `features/groups/`. Keep features isolated and you can work in parallel without conflicts!

For complete details, see:
- [Full Architecture Guide](PARALLEL_DEVELOPMENT_ARCHITECTURE.md)
- [Development Conventions](DEVELOPMENT_CONVENTIONS.md)
- [Requirements Overview](requirements/README.md)

Happy parallel developing! 🎉
