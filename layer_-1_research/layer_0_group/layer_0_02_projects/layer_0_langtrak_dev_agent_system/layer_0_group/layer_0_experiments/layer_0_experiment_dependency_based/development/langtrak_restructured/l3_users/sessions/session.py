# resource_id: "b92f6931-8c2c-48cd-a6ad-faf093ac0230"
# resource_type: "document"
# resource_name: "session"
"""
Core Session Module

Session management utilities for user authentication and project context.
"""

import sqlite3
from typing import Any, Dict, Optional

from flask import session

from .database import get_db_connection


def get_user_info() -> Dict[str, Any]:
    """
    Get authenticated user information from session.

    Supports both Firebase and legacy authentication.

    Returns:
        Dict containing:
        - id: User ID
        - name: Username
        - email: User email
        - firebase_uid: Firebase UID (if using Firebase auth)
        - is_authenticated: True if user is logged in
        - current_project: Current project context (if any)

    Example:
        user = get_user_info()
        if user['is_authenticated']:
            print(f"Welcome {user['name']}")
    """
    # Import here to avoid circular dependency
    from services.firebase import clean_firebase_service, firestore_db

    if "firebase_uid" in session:
        conn = get_db_connection()
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
                except Exception as exc:
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
                except Exception as exc:
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
        conn = get_db_connection()
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
                except Exception as exc:
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
                except Exception as exc:
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
    """
    Check if user is the owner of a project.

    Args:
        project_id: Project identifier
        user_id: User identifier

    Returns:
        True if user owns the project, False otherwise
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM projects WHERE id = ?", (project_id,))
    result = cursor.fetchone()
    conn.close()
    return bool(result and result[0] == user_id)


def get_current_user_id() -> Optional[int]:
    """
    Get current user ID from session.

    Returns:
        User ID if authenticated, None otherwise
    """
    user = get_user_info()
    return user.get('id') if user.get('is_authenticated') else None


def get_current_project() -> Optional[Dict[str, Any]]:
    """
    Get current project context from session.

    Returns:
        Project dict if user has entered a project, None otherwise
    """
    user = get_user_info()
    return user.get('current_project')


def set_current_project(project_id: str) -> None:
    """
    Set current project in session.

    Args:
        project_id: Project identifier to set as current
    """
    session['current_project_id'] = project_id


__all__ = [
    'get_user_info',
    'is_project_owner',
    'get_current_user_id',
    'get_current_project',
    'set_current_project',
]
