# resource_id: "b3117206-4c74-40a8-abdb-466579529869"
# resource_type: "document"
# resource_name: "__init__"
"""
Authentication Feature

User authentication, authorization, and session management.
Supports both Firebase and legacy email/password authentication.
"""

from flask import Blueprint

# Create auth blueprint
auth_bp = Blueprint(
    'auth',
    __name__,
    template_folder='templates',
    url_prefix=''  # No prefix, routes are at root level (/login, /register, etc.)
)

# Import sub-modules to register routes
from . import firebase_auth  # noqa: E402
from . import login  # noqa: E402
from . import registration  # noqa: E402

# Export helpers for backward compatibility
from .helpers import get_user_info, require_auth, require_project_admin, is_project_owner

__all__ = ("auth_bp", "get_user_info", "require_auth", "require_project_admin", "is_project_owner")
