# resource_id: "5eb43760-8795-4cfc-aa1a-9209c7d40946"
# resource_type: "document"
# resource_name: "__init__"
"""
Projects Feature

Handles project management including creation, editing, storage operations, and context.

Sub-modules organized by concern for parallel development:
- display: View and list projects
- creation: Create new projects
- editing: Edit project metadata
- storage_ops: Cloud/local migration, sync, fork operations
- context: Enter/exit project context
- api: API endpoints for project operations
"""

from flask import Blueprint

projects_bp = Blueprint(
    "projects",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/projects",
)

# Import all sub-modules to register their routes
from . import display        # 🟢 Agent A
from . import creation       # 🟢 Agent B
from . import editing        # 🟢 Agent C
from . import storage_ops    # 🟢 Agent D
from . import context        # 🟢 Agent E
from . import api            # 🟢 Agent F

# Import metadata helpers
from .metadata import fetch_project_metadata, normalize_project_identifier

__all__ = [
    "projects_bp",
    "fetch_project_metadata",
    "normalize_project_identifier",
]
