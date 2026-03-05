# resource_id: "da1ceeab-273a-41b1-b78c-75a0af27a842"
# resource_type: "document"
# resource_name: "__init__"
"""
Core Infrastructure Module

Shared utilities, database access, and decorators used across all features.
"""

from .database import get_db_connection, init_database
from .decorators import require_auth, require_project_admin
from .session import get_current_user_id, get_current_project, set_current_project

__all__ = [
    'get_db_connection',
    'init_database',
    'require_auth',
    'require_project_admin',
    'get_current_user_id',
    'get_current_project',
    'set_current_project',
]
