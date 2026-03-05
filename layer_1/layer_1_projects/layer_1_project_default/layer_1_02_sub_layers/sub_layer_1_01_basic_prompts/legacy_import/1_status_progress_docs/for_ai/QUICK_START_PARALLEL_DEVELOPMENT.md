---
resource_id: "d75ed266-1fa5-42a2-8a8c-fd0cff60cbeb"
resource_type: "document"
resource_name: "QUICK_START_PARALLEL_DEVELOPMENT"
---
# Quick Start: Parallel Development Guide

<!-- section_id: "80dfc4b3-9bfb-4ec8-ae55-0f4e8ede5968" -->
## What This Is

A fast-reference guide for AI agents working on the Language Tracker application in parallel. Read this first, then dive into detailed docs as needed.

---

<!-- section_id: "e0d6953c-d29b-48c7-8565-533c01d8c6a8" -->
## 🎯 The Core Concept

**One Feature = One Directory**

Each feature lives in its own isolated folder under `features/`. Multiple AI agents can work on different features simultaneously without conflicts because each agent stays in their own directory.

---

<!-- section_id: "1a174542-b9ed-407a-a1ed-9e3a58398250" -->
## 📁 Where to Put Your Code

<!-- section_id: "6b3e2402-82c6-45ac-ab5a-6bc80d838e8b" -->
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

<!-- section_id: "01570a9b-1c47-405f-9b96-5c013a47c990" -->
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

<!-- section_id: "eb109f9a-fcf8-416c-a12c-78ce4f8ee6f6" -->
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

<!-- section_id: "3083dd39-4695-4bb2-84d6-82fe817ddd6d" -->
## 🚦 Traffic Light System

<!-- section_id: "f277aee3-b9a7-4f73-952b-3772ef3a36f2" -->
### 🟢 GREEN - Work Freely (No Coordination Needed)

- Adding routes to your feature
- Creating templates in your feature
- Adding CSS/JS to your feature's static folder
- Writing tests for your feature
- Modifying business logic in your feature

<!-- section_id: "3eb32c6a-e53f-4260-a516-8801e124044d" -->
### 🟡 YELLOW - Check First

- Using functions from `core/` or `services/`
- Importing from another feature's `models.py`
- Modifying global templates (`templates/base.html`)
- Adding database migrations

<!-- section_id: "112e4133-5088-4297-8438-004aab488c2c" -->
### 🔴 RED - Must Coordinate

- Modifying `core/*` shared modules
- Modifying `services/*` shared services
- Changing database schema
- Modifying `app.py` (except adding new blueprint)
- Modifying another feature's code

---

<!-- section_id: "de8aba62-e816-4614-8423-0fafd7223fae" -->
## 📖 Common Patterns

<!-- section_id: "9ba01af8-6762-4112-8882-d0012a22da23" -->
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

<!-- section_id: "6b1a93e3-3f7c-4931-b0e5-8e4c25f42454" -->
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

<!-- section_id: "78116e38-9bee-4f99-b907-e3183af64ee1" -->
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

<!-- section_id: "4663750e-e401-46a3-bb9b-f67a573c3e4a" -->
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

<!-- section_id: "333b0733-bd21-470e-81fa-5f4fa90089ff" -->
## 🚫 What NOT to Do

<!-- section_id: "0bf73174-d549-4923-bedf-873f74f72745" -->
### ❌ Don't Import Other Features' Routes

```python
# BAD - Don't do this!
from features.words.routes import create_word_page

@my_feature_bp.route('/my-feature')
def my_page():
    return create_word_page()  # ❌ Calling another feature's route
```

<!-- section_id: "ad70086c-adef-4583-b9b2-e447c3ce0035" -->
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

<!-- section_id: "b07d6118-1f20-43aa-afce-7e6827a1efc5" -->
### ❌ Don't Put Templates in Global Directory

```python
# BAD
return render_template('my_page.html')  # Looks in global templates/

# GOOD
return render_template('my_feature/my_page.html')  # Looks in features/my_feature/templates/
```

<!-- section_id: "cf24ba3d-ec7e-4f63-99e2-9c272b7bc1fa" -->
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

<!-- section_id: "4078df17-4374-4c8c-b269-a47e4eb8071e" -->
## 🔍 Need More Detail?

<!-- section_id: "797400f3-b12a-4618-a7c4-006758ea0b0c" -->
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

<!-- section_id: "2bbe4e99-d92d-403b-8afa-698304b9e1f5" -->
### Requirements Documentation

**[Requirements Overview](requirements/README.md)**
- All feature specifications organized by navigation level
- Maps features to their purpose and expected outcomes
- Links to detailed requirement documents

**[Parallel Feature Isolation Spec](requirements/parallel_feature_isolation.md)**
- Original requirements for parallel development capability
- Acceptance criteria and expected outcomes

---

<!-- section_id: "3fb117e0-ae10-4591-a893-15caf3a824a3" -->
## 🎮 Parallel Development Scenarios

<!-- section_id: "3abee7e4-90f2-4b4c-a325-ec6db32c9b9e" -->
### Scenario 1: Three Agents, Three Features

**Agent 1** works on: `features/words/` (search enhancement)
**Agent 2** works on: `features/groups/` (invite system)
**Agent 3** works on: `features/admin/` (template import)

**Result**: Zero conflicts! Each agent has isolated workspace.

<!-- section_id: "ed27a9f7-7b03-4c64-b7ec-a9a2355aee89" -->
### Scenario 2: One Shared Module Change

**Problem**: Agent 1 needs to add function to `core/database.py`

**Solutions**:
1. **Sequential**: Agent 1 creates PR, merges, others pull latest
2. **Interface First**: Define function signature (stub) first, implement later
3. **Feature-Local**: Keep logic in feature if only one feature needs it

<!-- section_id: "04914883-fc6d-4ced-a40c-d555f7498963" -->
### Scenario 3: Database Migration

**Problem**: Agent 1 needs new column in `words` table

**Solution**:
1. Create migration file in `migrations/versions/`
2. Document which feature needs it
3. Coordinate with other agents to ensure they run migration
4. Only one agent creates migrations at a time

---

<!-- section_id: "ddb8840c-535a-44f1-a521-638f6f7753fe" -->
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

<!-- section_id: "b0283971-d06a-42f2-9561-c3d73592afc4" -->
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

<!-- section_id: "5df5a612-e4f2-4ac4-97a3-5836010608c9" -->
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

<!-- section_id: "3e04e6ca-b9e1-4f52-8fa6-9752d37f1cb7" -->
## Summary

**The Golden Rule**: If you're working on `words`, you touch `features/words/`. If you're working on `groups`, you touch `features/groups/`. Keep features isolated and you can work in parallel without conflicts!

For complete details, see:
- [Full Architecture Guide](PARALLEL_DEVELOPMENT_ARCHITECTURE.md)
- [Development Conventions](DEVELOPMENT_CONVENTIONS.md)
- [Requirements Overview](requirements/README.md)

Happy parallel developing! 🎉
