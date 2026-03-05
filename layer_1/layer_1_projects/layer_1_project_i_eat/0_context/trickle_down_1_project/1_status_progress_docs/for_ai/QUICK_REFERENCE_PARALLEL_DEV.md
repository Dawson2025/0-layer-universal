---
resource_id: "d5b62187-fab1-4c62-931a-08018e8fa78e"
resource_type: "document"
resource_name: "QUICK_REFERENCE_PARALLEL_DEV"
---
# Quick Reference: Parallel Development

<!-- section_id: "6592fda4-7764-4a7b-8b48-0ef5768bafbf" -->
## 🚀 Start Here

**Your codebase is configured for parallel development!** Multiple agents can work on different features simultaneously without conflicts.

<!-- section_id: "ef59ad40-43bb-4e69-a65b-20b19b8940fa" -->
## Feature Directory Map

| Feature | Directory | Your Work Area |
|---------|-----------|----------------|
| **Authentication** | `features/auth/` | Login, registration, Firebase auth |
| **Dashboard** | `features/dashboard/` | User dashboard, project overview |
| **Groups** | `features/groups/` | Group creation, invitations, membership |
| **Projects** | `features/projects/` | Project CRUD, branching, cloud migration |
| **Variant Menu** | `features/variant_menu/` | Project variant navigation |
| **Phonemes** | `features/phonemes/` | Phoneme viewing, frequency tracking |
| **Words** | `features/words/` | Word creation, search, editing, media |
| **Admin** | `features/admin/` | Phoneme management, templates, DB tools |

<!-- section_id: "cae1d17c-c3d6-41ef-aac4-e781e5981aa7" -->
## Traffic Light System

<!-- section_id: "6b2c9a28-7f2d-4dc7-b137-62720a698255" -->
### 🟢 GREEN - Work Freely
- ✅ Add routes to your feature
- ✅ Modify templates in your feature
- ✅ Add static assets in your feature
- ✅ Create tests in your feature
- ✅ Modify business logic in your feature

<!-- section_id: "d6948212-9f32-40d9-9f1d-68918bf2bf36" -->
### 🟡 YELLOW - Check First
- ⚠️ Using functions from `core/` or `services/`
- ⚠️ Modifying `templates/base.html`
- ⚠️ Adding database migrations
- ⚠️ Modifying global CSS

<!-- section_id: "e9a481e4-2969-44ef-87e5-25e1ce320132" -->
### 🔴 RED - Must Coordinate
- 🛑 Modifying `core/*` or `services/*`
- 🛑 Changing database schema
- 🛑 Modifying another feature's code
- 🛑 Changing `app.py` blueprint registration

<!-- section_id: "c8074294-624b-4772-96dc-7b601076bf83" -->
## Common Code Patterns

<!-- section_id: "90337f5e-a374-449b-846e-0a6706d365f4" -->
### 1. Add a Route

```python
# features/my_feature/routes.py
from flask import render_template
from core.decorators import require_auth
from core.session import get_user_info
from . import my_feature_bp

@my_feature_bp.route('/my-page')
@require_auth
def my_page():
    user = get_user_info()
    return render_template('my_feature/my_page.html', user=user)
```

<!-- section_id: "7e831425-cc8e-4faf-9290-d106a2af3c4f" -->
### 2. Add an API Endpoint

```python
# features/my_feature/api.py
from flask import jsonify, request
from core.decorators import require_auth
from . import my_feature_bp

@my_feature_bp.route('/api/my-feature/action', methods=['POST'])
@require_auth
def api_action():
    data = request.get_json()
    # ... business logic
    return jsonify({'success': True, 'data': result})
```

<!-- section_id: "f6e57143-3640-4df9-a4af-8882b10e1a78" -->
### 3. Database Query

```python
# features/my_feature/models.py
from core.database import get_db_connection

def get_items(user_id, project_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM items WHERE user_id = ? AND project_id = ?",
        (user_id, project_id)
    )
    results = cursor.fetchall()
    conn.close()
    return results
```

<!-- section_id: "cdff68bd-c450-4530-8d1c-ae2cf3937c47" -->
### 4. Render Template with User Context

```python
from core.session import get_user_info

@my_feature_bp.route('/page')
@require_auth
def page():
    user = get_user_info()
    # user['id'], user['name'], user['current_project']
    return render_template('my_feature/page.html', user=user)
```

<!-- section_id: "c1b135cb-4e5e-4fa5-be75-a4f979866ef8" -->
### 5. Check Project Ownership

```python
from core.decorators import require_project_admin

@my_feature_bp.route('/admin/action')
@require_project_admin  # Only project owners can access
def admin_action():
    # ... admin logic
    pass
```

<!-- section_id: "eddee93f-cd09-4b35-a9b1-a461e8e1b1f4" -->
## Quick Task Lookup

| I want to... | Location | Example |
|-------------|----------|---------|
| Add a login flow | `features/auth/routes.py` | `/login`, `/register` |
| Create project | `features/projects/routes.py` | `/projects/create` |
| List phonemes | `features/phonemes/routes.py` | `/phonemes/flat` |
| Add a word | `features/words/routes.py` | `/words/create` |
| Manage groups | `features/groups/routes.py` | `/groups/create` |
| Admin tools | `features/admin/routes.py` | `/admin/phonemes` |
| Project menu | `features/variant_menu/routes.py` | `/main-menu` |
| Dashboard | `features/dashboard/routes.py` | `/dashboard` |

<!-- section_id: "e9b1d018-2391-45b1-8532-ad8da5d1361a" -->
## Import Quick Reference

```python
# Database
from core.database import get_db_connection, init_database

# Authentication
from core.decorators import require_auth, require_project_admin

# Session
from core.session import get_user_info, get_current_project, set_current_project

# Your blueprint
from . import my_feature_bp

# Other feature helpers (minimal)
from features.auth.helpers import is_project_owner
from features.projects.metadata import normalize_project_identifier
```

<!-- section_id: "0c7b7156-1678-4ee3-971a-5f5700304404" -->
## Feature Structure Template

```
features/my_feature/
├── __init__.py          # Blueprint registration
├── routes.py            # Page routes (@require_auth)
├── api.py               # API endpoints (JSON responses)
├── models.py            # Database operations
├── business_logic.py    # Feature-specific logic
├── templates/
│   ├── my_feature_page1.html
│   └── my_feature_page2.html
├── static/
│   ├── js/
│   │   └── my_feature.js
│   └── css/
│       └── my_feature.css
└── tests/
    ├── test_routes.py
    └── test_api.py
```

<!-- section_id: "2a046836-eadf-44e9-b31e-0493a2cb81c3" -->
## Testing Your Feature

```bash
# Test your feature in isolation
pytest features/my_feature/tests/

# Test specific file
pytest features/my_feature/tests/test_routes.py

# Test with coverage
pytest --cov=features/my_feature features/my_feature/tests/
```

<!-- section_id: "9fc63bc6-0f69-4dbf-abd9-d2fd0775957f" -->
## Starting a New Feature

1. **Create directory**: `mkdir -p features/my_feature/templates`
2. **Create blueprint** (`__init__.py`):
   ```python
   from flask import Blueprint

   my_feature_bp = Blueprint('my_feature', __name__,
                             template_folder='templates',
                             url_prefix='/my-feature')
   from . import routes
   __all__ = ['my_feature_bp']
   ```

3. **Create routes** (`routes.py`)
4. **Register in app.py**:
   ```python
   from features.my_feature import my_feature_bp
   # Add to blueprint registration loop
   ```

5. **Add tests** (`tests/test_my_feature.py`)

<!-- section_id: "b02eab6e-f326-4292-a584-a931c22c467a" -->
## Parallel Work Example

**Scenario: 3 agents working simultaneously**

**Agent A** (Words): Adding search filters
- Files: `features/words/search.py`, `features/words/routes.py`
- Safe ✅ - No conflicts

**Agent B** (Groups): Adding role permissions
- Files: `features/groups/models.py`, `features/groups/api.py`
- Safe ✅ - No conflicts

**Agent C** (Phonemes): Adding categories
- Files: `features/phonemes/models.py`, `features/phonemes/templates/`
- Safe ✅ - No conflicts

**Result**: All three can commit without merge conflicts!

<!-- section_id: "57e475b4-4cfa-44ca-b014-29f8f2feec13" -->
## Help & Documentation

- **Full Architecture**: [PARALLEL_DEVELOPMENT_ARCHITECTURE.md](PARALLEL_DEVELOPMENT_ARCHITECTURE.md)
- **Coding Standards**: [DEVELOPMENT_CONVENTIONS.md](DEVELOPMENT_CONVENTIONS.md)
- **Implementation Summary**: [IMPLEMENTATION_SUMMARY_PARALLEL_DEV.md](IMPLEMENTATION_SUMMARY_PARALLEL_DEV.md)
- **Setup Guide**: [PARALLEL_DEVELOPMENT_SETUP_COMPLETE.md](PARALLEL_DEVELOPMENT_SETUP_COMPLETE.md)
- **Requirements**: [requirements/README.md](requirements/README.md)

<!-- section_id: "83d0667f-dc32-4dda-9585-d122904b3363" -->
## Key Reminders

1. **Stay in your feature directory** - That's your green zone
2. **Check active PRs** before modifying `core/` or `services/`
3. **Test in isolation** - Your feature tests should run independently
4. **Follow naming conventions** - `routes.py`, `api.py`, `models.py`
5. **Use core modules** - Don't duplicate database connection logic

---

**Ready to code!** Pick a feature and start working. 🚀
