---
resource_id: "f4818bf1-76cc-4e87-ba7b-ff2e85de4ff0"
resource_type: "document"
resource_name: "QUICK_START_PARALLEL_DEVELOPMENT"
---
# Quick Start: Parallel Development Guide

<!-- section_id: "4ef8dbe8-f30b-4d4c-9212-3551143de37e" -->
## What This Is

A fast-reference guide for AI agents working on the Language Tracker application in parallel. Read this first, then dive into detailed docs as needed.

---

<!-- section_id: "c6b10dbf-849f-4186-93b7-4345cec94252" -->
## 🎯 The Core Concept

**One Feature = One Directory**

Each feature lives in its own isolated folder under `features/`. Multiple AI agents can work on different features simultaneously without conflicts because each agent stays in their own directory.

---

<!-- section_id: "4d235b56-60ae-4327-903e-f77ca8c258eb" -->
## 📁 Where to Put Your Code

<!-- section_id: "602af085-d8e2-478f-a43f-bd1bd567f825" -->
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

<!-- section_id: "64590caf-c660-40e0-9572-b038cc9c47b4" -->
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

<!-- section_id: "089e50cd-1842-4cdc-a2fd-e75f592af094" -->
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

<!-- section_id: "2ea76027-95af-4501-8e4e-40bf0e752e89" -->
## 🚦 Traffic Light System

<!-- section_id: "3d61c84b-22f9-4dcf-b4da-345fde68067b" -->
### 🟢 GREEN - Work Freely (No Coordination Needed)

- Adding routes to your feature
- Creating templates in your feature
- Adding CSS/JS to your feature's static folder
- Writing tests for your feature
- Modifying business logic in your feature

<!-- section_id: "1449a1b7-d9bb-4b11-ae01-21e301b0d9af" -->
### 🟡 YELLOW - Check First

- Using functions from `core/` or `services/`
- Importing from another feature's `models.py`
- Modifying global templates (`templates/base.html`)
- Adding database migrations

<!-- section_id: "5c16cd91-8845-47e6-9c22-9ce8c7962c23" -->
### 🔴 RED - Must Coordinate

- Modifying `core/*` shared modules
- Modifying `services/*` shared services
- Changing database schema
- Modifying `app.py` (except adding new blueprint)
- Modifying another feature's code

---

<!-- section_id: "d9213532-e14f-4df4-bd52-6c477501311d" -->
## 📖 Common Patterns

<!-- section_id: "b42b7788-7a2e-4647-b974-55c221ec7e7f" -->
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

<!-- section_id: "c4938abe-b216-4045-8eb6-7036650f92a4" -->
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

<!-- section_id: "09773d87-dc23-4ae9-92c4-c0f72617e036" -->
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

<!-- section_id: "8b9ff232-be79-4b44-9ddc-9f177073ca35" -->
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

<!-- section_id: "84db8e75-229d-44f6-9259-be2d87fe7e00" -->
## 🚫 What NOT to Do

<!-- section_id: "90f6911e-295d-4fb7-b65c-9736183dc628" -->
### ❌ Don't Import Other Features' Routes

```python
# BAD - Don't do this!
from features.words.routes import create_word_page

@my_feature_bp.route('/my-feature')
def my_page():
    return create_word_page()  # ❌ Calling another feature's route
```

<!-- section_id: "e8ee0c0a-efad-4234-8795-d327a9a54929" -->
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

<!-- section_id: "f9c4fa34-3697-4fd8-829a-841700500e9e" -->
### ❌ Don't Put Templates in Global Directory

```python
# BAD
return render_template('my_page.html')  # Looks in global templates/

# GOOD
return render_template('my_feature/my_page.html')  # Looks in features/my_feature/templates/
```

<!-- section_id: "11ee3066-668b-48f2-8158-750399ac7973" -->
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

<!-- section_id: "138779cf-f18a-47eb-818e-275e2fd48c30" -->
## 🔍 Need More Detail?

<!-- section_id: "1528b0dd-6d8d-4b09-bcf2-c2d885543210" -->
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

<!-- section_id: "a12c02a2-b4d6-4272-8c9f-dfbb29b5ae8c" -->
### Requirements Documentation

**[Requirements Overview](requirements/README.md)**
- All feature specifications organized by navigation level
- Maps features to their purpose and expected outcomes
- Links to detailed requirement documents

**[Parallel Feature Isolation Spec](requirements/parallel_feature_isolation.md)**
- Original requirements for parallel development capability
- Acceptance criteria and expected outcomes

---

<!-- section_id: "d28497f4-2e75-463b-b506-02856f61eca6" -->
## 🎮 Parallel Development Scenarios

<!-- section_id: "4e65ebe2-a496-41ea-be63-9c3acae47522" -->
### Scenario 1: Three Agents, Three Features

**Agent 1** works on: `features/words/` (search enhancement)
**Agent 2** works on: `features/groups/` (invite system)
**Agent 3** works on: `features/admin/` (template import)

**Result**: Zero conflicts! Each agent has isolated workspace.

<!-- section_id: "1ebd554b-cc16-473c-8858-fcad4bda0bda" -->
### Scenario 2: One Shared Module Change

**Problem**: Agent 1 needs to add function to `core/database.py`

**Solutions**:
1. **Sequential**: Agent 1 creates PR, merges, others pull latest
2. **Interface First**: Define function signature (stub) first, implement later
3. **Feature-Local**: Keep logic in feature if only one feature needs it

<!-- section_id: "ec480242-a3b0-4879-af40-47386da5bb00" -->
### Scenario 3: Database Migration

**Problem**: Agent 1 needs new column in `words` table

**Solution**:
1. Create migration file in `migrations/versions/`
2. Document which feature needs it
3. Coordinate with other agents to ensure they run migration
4. Only one agent creates migrations at a time

---

<!-- section_id: "4ede4e68-8086-43cd-9334-15b47f85d977" -->
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

<!-- section_id: "64afef1d-7b1d-47e0-a93a-e790a7af0da5" -->
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

<!-- section_id: "659b4a4d-9cac-48b1-b4fe-8d5c7e9457c4" -->
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

<!-- section_id: "9805e096-8bd3-4f49-bd4f-dfb2b36f09b2" -->
## Summary

**The Golden Rule**: If you're working on `words`, you touch `features/words/`. If you're working on `groups`, you touch `features/groups/`. Keep features isolated and you can work in parallel without conflicts!

For complete details, see:
- [Full Architecture Guide](PARALLEL_DEVELOPMENT_ARCHITECTURE.md)
- [Development Conventions](DEVELOPMENT_CONVENTIONS.md)
- [Requirements Overview](requirements/README.md)

Happy parallel developing! 🎉
