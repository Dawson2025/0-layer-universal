# resource_id: "4bd03616-aae9-4d02-ab29-fff0a8bfaac8"
# resource_type: "document"
# resource_name: "helpers"
"""
Reusable authentication utilities shared across the application.

These helpers were extracted from the monolithic Flask app module so
features dealing with authentication/authorization can evolve in
parallel without editing unrelated endpoints.
"""

from __future__ import annotations

import sqlite3
from functools import wraps
from typing import Any, Callable, Dict

from flask import flash, redirect, session, url_for
from werkzeug.routing import BuildError

import main
from services.firebase import clean_firebase_service, firestore_db


def get_user_info() -> Dict[str, Any]:
    """Get authenticated user information from session (supports both Firebase and legacy auth)."""
    if "firebase_uid" in session:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, username, email, firebase_uid FROM users WHERE firebase_uid = ? AND is_active = 1",
            (session["firebase_uid"],),
        )
        user_data = cursor.fetchone()

        current_project = None
        if user_data and "current_project_id" in session:
            if clean_firebase_service.is_available():
                try:
                    firebase_project = firestore_db.get_project(session["current_project_id"])
                    if firebase_project:
                        owner_id = firebase_project.get("user_id") or firebase_project.get("user_id_str")
                        if owner_id is not None and str(owner_id) == str(user_data[0]):
                            last_sync = firebase_project.get("updated_at")
                            if hasattr(last_sync, "isoformat"):
                                last_sync = last_sync.isoformat()
                            current_project = {
                                "id": firebase_project["id"],
                                "name": firebase_project["name"],
                                "is_owner": True,
                                "storage_type": "cloud",
                                "cloud_project_id": firebase_project["id"],
                                "cloud_last_sync": last_sync,
                                "local_project_id": (
                                    str(firebase_project.get("original_sqlite_id"))
                                    if firebase_project.get("original_sqlite_id")
                                    else None
                                ),
                            }
                except Exception as exc:  # pragma: no cover - diagnostic aid
                    print(f"Error checking Firebase current project: {exc}")

            if not current_project:
                try:
                    int_project_id = int(session["current_project_id"])
                    cursor.execute(
                        """
                        SELECT p.id, p.name, p.user_id, p.cloud_project_id, p.cloud_last_sync, p.migrated_to_cloud
                        FROM projects p
                        WHERE p.id = ? AND (
                            p.user_id = ? OR 
                            EXISTS (
                                SELECT 1 FROM project_shares ps
                                JOIN group_memberships gm ON ps.group_id = gm.group_id
                                WHERE gm.user_id = ?
                                  AND ps.project_identifier IN ('local:' || p.id, 'cloud:' || p.cloud_project_id)
                            )
                        )
                        """,
                        (int_project_id, user_data[0], user_data[0]),
                    )
                    project_data = cursor.fetchone()
                    if project_data:
                        cloud_last_sync = project_data[4]
                        if cloud_last_sync and hasattr(cloud_last_sync, "isoformat"):
                            cloud_last_sync = cloud_last_sync.isoformat()
                        current_project = {
                            "id": project_data[0],
                            "name": project_data[1],
                            "is_owner": project_data[2] == user_data[0],
                            "storage_type": "local",
                            "cloud_project_id": str(project_data[3]) if project_data[3] is not None else None,
                            "cloud_last_sync": cloud_last_sync,
                            "migrated_to_cloud": bool(project_data[5]),
                            "local_project_id": str(project_data[0]),
                        }
                except (ValueError, TypeError):
                    pass
                except Exception as exc:  # pragma: no cover - diagnostic aid
                    print(f"Error checking SQLite current project: {exc}")

        conn.close()

        if user_data:
            return {
                "id": user_data[0],
                "name": user_data[1],
                "email": user_data[2],
                "firebase_uid": user_data[3],
                "roles": "",
                "is_authenticated": True,
                "current_project": current_project,
            }

    if "user_id" in session:
        conn = sqlite3.connect(main.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, username, email FROM users WHERE id = ? AND is_active = 1",
            (session["user_id"],),
        )
        user_data = cursor.fetchone()

        current_project = None
        if user_data and "current_project_id" in session:
            # Check Firebase first if available (for cloud projects)
            if clean_firebase_service.is_available():
                try:
                    firebase_project = firestore_db.get_project(session["current_project_id"])
                    if firebase_project:
                        owner_id = firebase_project.get("user_id") or firebase_project.get("user_id_str")
                        if owner_id is not None and str(owner_id) == str(user_data[0]):
                            last_sync = firebase_project.get("updated_at")
                            if hasattr(last_sync, "isoformat"):
                                last_sync = last_sync.isoformat()
                            current_project = {
                                "id": firebase_project["id"],
                                "name": firebase_project["name"],
                                "is_owner": True,
                                "storage_type": "cloud",
                                "cloud_project_id": firebase_project["id"],
                                "cloud_last_sync": last_sync,
                                "local_project_id": (
                                    str(firebase_project.get("original_sqlite_id"))
                                    if firebase_project.get("original_sqlite_id")
                                    else None
                                ),
                            }
                except Exception as exc:  # pragma: no cover - diagnostic aid
                    print(f"Error checking Firebase current project: {exc}")

            # If not found in Firebase, check local SQLite
            if not current_project:
                try:
                    int_project_id = int(session["current_project_id"])
                    cursor.execute(
                        """
                        SELECT p.id, p.name, p.user_id, p.cloud_project_id, p.cloud_last_sync, p.migrated_to_cloud
                        FROM projects p
                        WHERE p.id = ? AND (
                            p.user_id = ? OR
                            EXISTS (
                                SELECT 1 FROM project_shares ps
                                JOIN group_memberships gm ON ps.group_id = gm.group_id
                                WHERE gm.user_id = ?
                                  AND ps.project_identifier IN ('local:' || p.id, 'cloud:' || p.cloud_project_id)
                            )
                        )
                        """,
                        (int_project_id, user_data[0], user_data[0]),
                    )
                    project_data = cursor.fetchone()
                    if project_data:
                        cloud_last_sync = project_data[4]
                        if cloud_last_sync and hasattr(cloud_last_sync, "isoformat"):
                            cloud_last_sync = cloud_last_sync.isoformat()
                        current_project = {
                            "id": project_data[0],
                            "name": project_data[1],
                            "is_owner": project_data[2] == user_data[0],
                            "storage_type": "local",
                            "cloud_project_id": str(project_data[3]) if project_data[3] is not None else None,
                            "cloud_last_sync": cloud_last_sync,
                            "migrated_to_cloud": bool(project_data[5]),
                            "local_project_id": str(project_data[0]),
                        }
                except (ValueError, TypeError):
                    pass
                except Exception as exc:  # pragma: no cover - diagnostic aid
                    print(f"Error checking SQLite current project: {exc}")

        conn.close()

        if user_data:
            return {
                "id": user_data[0],
                "name": user_data[1],
                "email": user_data[2],
                "roles": "",
                "is_authenticated": True,
                "current_project": current_project,
            }

    return {"is_authenticated": False}


def is_project_owner(project_id: Any, user_id: Any) -> bool:
    """Check if user is the owner of a project."""
    conn = sqlite3.connect(main.DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM projects WHERE id = ?", (project_id,))
    result = cursor.fetchone()
    conn.close()
    return bool(result and result[0] == user_id)


def require_auth(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to require authentication for routes."""

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
    """Decorator to require project admin access for routes."""

    @wraps(func)
    def decorated_function(*args: Any, **kwargs: Any):
        user = get_user_info()
        if not user["is_authenticated"]:
            try:
                return redirect(url_for("auth.login"))
            except BuildError:
                return redirect(url_for("login"))

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


__all__ = ("get_user_info", "require_auth", "require_project_admin", "is_project_owner")
