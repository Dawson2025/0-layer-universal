# resource_id: "98f4bbd1-4aac-4c05-87c3-ae0ae8055bd2"
# resource_type: "document"
# resource_name: "decorators"
"""
Core Decorators Module

Authentication and authorization decorators used across features.
"""

from functools import wraps
from typing import Any, Callable

from flask import flash, redirect, url_for
from werkzeug.routing import BuildError

from .session import get_user_info, is_project_owner


def require_auth(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to require authentication for routes.

    Usage:
        @blueprint.route('/protected')
        @require_auth
        def protected_route():
            # Only authenticated users can access this
            pass
    """
    @wraps(func)
    def decorated_function(*args: Any, **kwargs: Any):
        user = get_user_info()
        if not user["is_authenticated"]:
            try:
                return redirect(url_for("auth.login"))
            except BuildError:
                return redirect(url_for("login"))
        return func(*args, **kwargs)

    return decorated_function


def require_project_admin(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to require project admin access for routes.
    User must be authenticated AND be the owner of the current project.

    Usage:
        @blueprint.route('/admin/phonemes')
        @require_project_admin
        def admin_phonemes():
            # Only project owners can access this
            pass
    """
    @wraps(func)
    def decorated_function(*args: Any, **kwargs: Any):
        user = get_user_info()
        if not user["is_authenticated"]:
            return redirect(url_for("auth.login"))

        if not user.get("current_project"):
            flash("Please enter a project to access admin tools", "error")
            try:
                return redirect(url_for("dashboard.dashboard"))
            except BuildError:
                return redirect(url_for("dashboard"))

        current_project = user.get("current_project")
        if not current_project or not is_project_owner(current_project["id"], user["id"]):
            flash("Access denied. Only project owners can access admin tools.", "error")
            return redirect(url_for("main_menu"))

        return func(*args, **kwargs)

    return decorated_function


__all__ = ['require_auth', 'require_project_admin']
