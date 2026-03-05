---
resource_id: "0a4ef96f-6baf-4120-bf67-1eb99fc415ca"
resource_type: "document"
resource_name: "QUICK_REFERENCE_PARALLEL_DEV"
---
# Quick Reference: Parallel Development

<!-- section_id: "c569f958-2c67-481f-bb62-d3a903b0ad53" -->
## 🚀 Start Here

**Your codebase is configured for parallel development!** Multiple agents can work on different features simultaneously without conflicts.

<!-- section_id: "9e2aaeb2-e1aa-47ed-91bd-c5ffdebe3c3d" -->
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

<!-- section_id: "3db12b78-5b63-40cb-a758-804325c27828" -->
## Traffic Light System

<!-- section_id: "5288f01f-320b-43b0-93c4-b8bbdcca2f21" -->
### 🟢 GREEN - Work Freely
- ✅ Add routes to your feature
- ✅ Modify templates in your feature
- ✅ Add static assets in your feature
- ✅ Create tests in your feature
- ✅ Modify business logic in your feature

<!-- section_id: "96594aa6-ea60-436a-be94-196f2b30b056" -->
### 🟡 YELLOW - Check First
- ⚠️ Using functions from `core/` or `services/`
- ⚠️ Modifying `templates/base.html`
- ⚠️ Adding database migrations
- ⚠️ Modifying global CSS

<!-- section_id: "baaf74e9-6c72-4922-a638-6f22a9495f6d" -->
### 🔴 RED - Must Coordinate
- 🛑 Modifying `core/*` or `services/*`
- 🛑 Changing database schema
- 🛑 Modifying another feature's code
- 🛑 Changing `app.py` blueprint registration

<!-- section_id: "d7f06fc5-3e76-4e69-8a23-fd90b35225c6" -->
## Common Code Patterns

<!-- section_id: "4ae508c5-2700-4c2c-bcad-6f64790c610f" -->
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

<!-- section_id: "6aa4bd6d-d9fe-4d2a-a098-8683ccc04f60" -->
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

<!-- section_id: "0f234dbb-d0bd-4f4a-b137-87ceb6b2aec4" -->
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

<!-- section_id: "e22a1945-da33-445f-bd09-2ec78157f508" -->
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

<!-- section_id: "67415604-fff8-4294-90d7-6cb1bafbe257" -->
### 5. Check Project Ownership

```python
from core.decorators import require_project_admin

@my_feature_bp.route('/admin/action')
@require_project_admin  # Only project owners can access
def admin_action():
    # ... admin logic
    pass
```

<!-- section_id: "d9f4f8ce-aa08-4191-96f5-775f08026cd2" -->
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

<!-- section_id: "1d421395-96c0-4f0c-944b-977c49d59d3a" -->
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

<!-- section_id: "6f1f6879-a778-4f5c-84e8-a8e79e1c05ee" -->
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

<!-- section_id: "862c9be1-a5c0-4ac8-a15a-91c4addb058c" -->
## Testing Your Feature

```bash
# Test your feature in isolation
pytest features/my_feature/tests/

# Test specific file
pytest features/my_feature/tests/test_routes.py

# Test with coverage
pytest --cov=features/my_feature features/my_feature/tests/
```

<!-- section_id: "b6d43010-0113-407c-871f-1df9747fe615" -->
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

<!-- section_id: "51e5d3cb-d0f9-4176-b0c5-f6d774d2f4c5" -->
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

<!-- section_id: "bbfda9a3-346e-413d-a84c-fd1dba9bdd9e" -->
## Help & Documentation

- **Full Architecture**: [PARALLEL_DEVELOPMENT_ARCHITECTURE.md](PARALLEL_DEVELOPMENT_ARCHITECTURE.md)
- **Coding Standards**: [DEVELOPMENT_CONVENTIONS.md](DEVELOPMENT_CONVENTIONS.md)
- **Implementation Summary**: [IMPLEMENTATION_SUMMARY_PARALLEL_DEV.md](IMPLEMENTATION_SUMMARY_PARALLEL_DEV.md)
- **Setup Guide**: [PARALLEL_DEVELOPMENT_SETUP_COMPLETE.md](PARALLEL_DEVELOPMENT_SETUP_COMPLETE.md)
- **Requirements**: [requirements/README.md](requirements/README.md)

<!-- section_id: "427946e3-bc3b-4bec-9537-c0170dab4b76" -->
## Key Reminders

1. **Stay in your feature directory** - That's your green zone
2. **Check active PRs** before modifying `core/` or `services/`
3. **Test in isolation** - Your feature tests should run independently
4. **Follow naming conventions** - `routes.py`, `api.py`, `models.py`
5. **Use core modules** - Don't duplicate database connection logic

---

**Ready to code!** Pick a feature and start working. 🚀
