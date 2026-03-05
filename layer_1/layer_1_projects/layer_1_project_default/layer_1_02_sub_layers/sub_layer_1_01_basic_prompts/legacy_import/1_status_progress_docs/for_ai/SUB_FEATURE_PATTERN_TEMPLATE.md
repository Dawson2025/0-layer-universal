---
resource_id: "bc3a9fe9-36b2-404f-8fde-034ea3ac1f28"
resource_type: "document"
resource_name: "SUB_FEATURE_PATTERN_TEMPLATE"
---
# Sub-Feature Pattern Implementation Template

<!-- section_id: "ff7e8be5-83d1-4ff3-b774-cb05f3cd7441" -->
## How to Apply the Pattern to Any Feature

This template shows you exactly how to reorganize a feature for maximum parallel development.

---

<!-- section_id: "c5142ea5-a1d9-4907-b60a-794b73fb3846" -->
## Step 1: Analyze Routes

List all routes for the feature from app.py:

```bash
grep -n "^@app.route('/your_feature" app.py
```

Example for projects:
```
/projects                          - List projects
/projects/create                   - Create project
/projects/<id>/edit                - Edit project
/projects/<id>/migrate-to-cloud    - Cloud migration
/projects/<id>/enter               - Enter context
```

---

<!-- section_id: "a3e54cc2-2e40-4ec0-bcef-588fa6e34346" -->
## Step 2: Group by Concern

Organize routes into logical concerns:

**Example: Projects Feature**
- **Display**: List, view projects (1 route)
- **Creation**: Create new projects (1 route)
- **Editing**: Edit metadata (1 route)
- **Storage**: Migration, sync, fork (4 routes)
- **Context**: Enter/exit (2 routes)

---

<!-- section_id: "91c3c2e9-5cf4-4bc9-81ae-9105bfad1bf8" -->
## Step 3: Create Sub-Module Files

<!-- section_id: "394e6f60-d71c-47c9-976d-ef0277837eff" -->
### Template: display.py

```python
"""
[Feature] Display Module

Handles viewing and listing [feature items].
Agents can work on display enhancements without affecting other sub-modules.
"""

from flask import render_template, redirect, url_for, flash

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from . import [feature]_bp


@[feature]_bp.route('/[feature]')
@require_auth
def [feature]_list():
    """
    Display list of [feature items].

    Returns:
        Rendered template with [feature] list
    """
    user = get_user_info()

    # Get items logic here
    items = _get_items(user)

    return render_template('[feature]/[feature]_list.html', items=items, user=user)


def _get_items(user: dict) -> list:
    """
    Helper function to fetch items.

    Args:
        user: User information dictionary

    Returns:
        List of item dictionaries
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM [table]
        WHERE user_id = ?
        ORDER BY created_at DESC
    """, (user['id'],))

    results = cursor.fetchall()
    conn.close()

    return [dict(row) for row in results]


__all__ = ['[feature]_list']
```

<!-- section_id: "761ef7d7-74ff-4679-8841-f4fae74d1d42" -->
### Template: creation.py

```python
"""
[Feature] Creation Module

Handles creating new [feature items].
Agents can work on creation improvements without affecting other sub-modules.
"""

from flask import render_template, request, redirect, url_for, flash, jsonify

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from . import [feature]_bp


@[feature]_bp.route('/[feature]/create', methods=['GET', 'POST'])
@require_auth
def create_[feature]():
    """
    Create new [feature item].

    GET: Display creation form
    POST: Process form and create item
    """
    user = get_user_info()

    if request.method == 'POST':
        # Get form data
        data = request.form.to_dict() if not request.is_json else request.get_json()

        # Validate data
        if not _validate_[feature]_data(data):
            flash('Invalid data provided', 'error')
            return redirect(url_for('[feature].create_[feature]'))

        # Create item
        item_id = _create_[feature]_item(data, user['id'])

        if item_id:
            flash('[Feature] created successfully!', 'success')
            return redirect(url_for('[feature].[feature]_list'))
        else:
            flash('Failed to create [feature]', 'error')

    return render_template('[feature]/create_[feature].html', user=user)


def _validate_[feature]_data(data: dict) -> bool:
    """Validate [feature] creation data."""
    required_fields = ['name', 'description']  # Adjust as needed
    return all(field in data and data[field] for field in required_fields)


def _create_[feature]_item(data: dict, user_id: int) -> int:
    """
    Create [feature] item in database.

    Returns:
        ID of created item, or None on failure
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO [table] (name, description, user_id, created_at)
            VALUES (?, ?, ?, datetime('now'))
        """, (data['name'], data['description'], user_id))

        item_id = cursor.lastrowid
        conn.commit()
        return item_id
    except Exception as e:
        print(f"Error creating [feature]: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()


__all__ = ['create_[feature]']
```

<!-- section_id: "8b8a5a45-1329-4379-962f-42cdd64f64dd" -->
### Template: editing.py

```python
"""
[Feature] Editing Module

Handles editing existing [feature items].
Agents can work on editing improvements without affecting other sub-modules.
"""

from flask import render_template, request, redirect, url_for, flash

from core.database import get_db_connection, DB_NAME
from core.decorators import require_auth
from core.session import get_user_info
from . import [feature]_bp


@[feature]_bp.route('/[feature]/<int:item_id>/edit', methods=['GET', 'POST'])
@require_auth
def edit_[feature](item_id):
    """
    Edit existing [feature item].

    Args:
        item_id: ID of item to edit
    """
    user = get_user_info()

    if request.method == 'POST':
        data = request.form.to_dict() if not request.is_json else request.get_json()

        if _update_[feature]_item(item_id, data, user['id']):
            flash('[Feature] updated successfully!', 'success')
            return redirect(url_for('[feature].[feature]_list'))
        else:
            flash('Failed to update [feature]', 'error')

    # GET request: load item data
    item = _get_[feature]_item(item_id, user['id'])

    if not item:
        flash('[Feature] not found', 'error')
        return redirect(url_for('[feature].[feature]_list'))

    return render_template('[feature]/edit_[feature].html', item=item, user=user)


def _get_[feature]_item(item_id: int, user_id: int) -> dict:
    """Get [feature] item by ID."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM [table]
        WHERE id = ? AND user_id = ?
    """, (item_id, user_id))

    result = cursor.fetchone()
    conn.close()

    return dict(result) if result else None


def _update_[feature]_item(item_id: int, data: dict, user_id: int) -> bool:
    """Update [feature] item in database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE [table]
            SET name = ?, description = ?, updated_at = datetime('now')
            WHERE id = ? AND user_id = ?
        """, (data['name'], data['description'], item_id, user_id))

        conn.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print(f"Error updating [feature]: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()


__all__ = ['edit_[feature]']
```

<!-- section_id: "2cbc6b17-50fb-4aa4-8c31-bfcddcd6b2ff" -->
### Template: api.py

```python
"""
[Feature] API Module

API endpoints for [feature] operations.
Agents can work on API improvements without affecting routes.
"""

from flask import request, jsonify

from core.decorators import require_auth
from core.session import get_user_info
from . import [feature]_bp


@[feature]_bp.route('/api/[feature]', methods=['GET'])
@require_auth
def api_list_[feature]():
    """API endpoint to list [feature items]."""
    try:
        user = get_user_info()
        # Get items logic here

        return jsonify({
            'success': True,
            'items': [],  # Add items here
            'count': 0
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@[feature]_bp.route('/api/[feature]/<int:item_id>', methods=['GET'])
@require_auth
def api_get_[feature](item_id):
    """API endpoint to get single [feature item]."""
    try:
        user = get_user_info()
        # Get item logic here

        return jsonify({
            'success': True,
            'item': {}  # Add item here
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@[feature]_bp.route('/api/[feature]', methods=['POST'])
@require_auth
def api_create_[feature]():
    """API endpoint to create [feature item]."""
    try:
        user = get_user_info()
        data = request.get_json()

        # Create item logic here

        return jsonify({
            'success': True,
            'message': '[Feature] created successfully',
            'item_id': None  # Add created ID
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@[feature]_bp.route('/api/[feature]/<int:item_id>', methods=['PUT', 'PATCH'])
@require_auth
def api_update_[feature](item_id):
    """API endpoint to update [feature item]."""
    try:
        user = get_user_info()
        data = request.get_json()

        # Update item logic here

        return jsonify({
            'success': True,
            'message': '[Feature] updated successfully'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@[feature]_bp.route('/api/[feature]/<int:item_id>', methods=['DELETE'])
@require_auth
def api_delete_[feature](item_id):
    """API endpoint to delete [feature item]."""
    try:
        user = get_user_info()

        # Delete item logic here

        return jsonify({
            'success': True,
            'message': '[Feature] deleted successfully'
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


__all__ = [
    'api_list_[feature]',
    'api_get_[feature]',
    'api_create_[feature]',
    'api_update_[feature]',
    'api_delete_[feature]'
]
```

---

<!-- section_id: "b6f1368f-9a3c-419d-809c-9ec617b56bcb" -->
## Step 4: Update __init__.py

```python
"""
[Feature] Feature

Brief description of what this feature does.

Sub-modules organized by concern for parallel development:
- display: View and list [feature items]
- creation: Create new [feature items]
- editing: Edit existing [feature items]
- api: API endpoints for CRUD operations
"""

from flask import Blueprint

[feature]_bp = Blueprint(
    "[feature]",
    __name__,
    url_prefix="/[feature]",
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/[feature]",
)

# Import all sub-modules to register their routes
from . import display      # 🟢 Agent A
from . import creation     # 🟢 Agent B
from . import editing      # 🟢 Agent C
from . import api          # 🟢 Agent D

__all__ = ("[feature]_bp",)
```

---

<!-- section_id: "fa3407e1-29cf-46fa-8eef-5e75e05c7754" -->
## Step 5: Organize Templates

Move templates to feature-specific directory:

```
features/[feature]/templates/[feature]/
├── [feature]_list.html
├── create_[feature].html
├── edit_[feature].html
└── [feature]_detail.html
```

In templates, reference as:
```python
render_template('[feature]/[feature]_list.html', ...)
```

---

<!-- section_id: "c9a2ad4a-9680-4f50-afa9-8079491d3efa" -->
## Step 6: Create Tests

One test file per sub-module:

```
features/[feature]/tests/
├── test_display.py
├── test_creation.py
├── test_editing.py
└── test_api.py
```

---

<!-- section_id: "778010fd-2b64-4b52-a62b-644c6d95a6d1" -->
## Quick Reference Checklist

When applying the pattern to a feature:

- [ ] List all routes for the feature
- [ ] Group routes by concern (display, creation, editing, etc.)
- [ ] Create one .py file per concern
- [ ] Extract routes from app.py to sub-modules
- [ ] Update __init__.py to import all sub-modules
- [ ] Move templates to features/[feature]/templates/
- [ ] Create test files for each sub-module
- [ ] Update documentation

---

<!-- section_id: "3ebf6832-e1bf-4939-ba34-5c786fad4692" -->
## Benefits Achieved

After applying the pattern:

✅ Multiple agents can work on same feature simultaneously
✅ Clear separation of concerns
✅ Smaller, more focused files
✅ Easier testing and code review
✅ Zero file conflicts when working on different concerns

---

<!-- section_id: "f9c5771a-9d31-4695-824e-e68a6bae1cf2" -->
## Example: Already Implemented

See **features/words/** for a complete example:
- display.py (175 lines)
- creation.py (245 lines)
- search.py (152 lines)
- editing.py (68 lines)
- api_operations.py (426 lines)

**Result:** 5 agents can work on words simultaneously!
